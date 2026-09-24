"""C4 lesson 01 — Chemical change vs physical change: twelve questions (MRB-246).

The lesson's argument is one sentence long — a chemical change makes at least
one new substance and a physical change makes none — and the whole page is
built to stop the visible clue doing the deciding. These twelve probe the
angles the mastery ladder leaves alone: a clue on its own, the same clue on
both sides of the line, and what the answer is EVIDENCE for rather than what
the answer is.

The distractors are built from the lesson's two declared misconceptions.

`REACT-01` (if it cannot be undone it is chemical; if it can, it is physical)
drives the wrong options in e01, e02, s02, h01 and h03. Each treats how hard
a change is to undo as though it were a fact about the substances rather than
a fact about energy and equipment — and s02 and h01 are the two that matter,
because a student who has learnt the rule can still be caught by an example
that FITS it (three of s02's four options do) and by a reversal that happens
in a furnace rather than on a bench.

`REACT-02` (something disappearing into a liquid is always the same kind of
change) drives e03, s01 and h04, where a solid vanishing is treated as
evidence of something. It is evidence of nothing: it happens on both sides of
pair 2 and the two events are not the same event.

A third strand, everywhere on the page and in neither register entry, is that
a clue is a proof — that speed, heat, a flame nearby or a colour change
settles it. e01, e02, e04, s03, s04, h02 and h04 each carry a distractor that
does exactly that, because it is the mistake a student makes in front of a
real bench with something bubbling on it.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §13's: each distractor is a WRONG
RULE in the correct answer's own shape, at the correct answer's own length,
and each is a mistake a real student in a real lab makes. Every option set
below was counted; no correct answer is strictly the longest in its set by
four words or by 1.4×.
"""

UNIT = "C4"
LESSON = "chemical-vs-physical-change"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c4-01-e01",
        "band": "easier",
        "text": "Which one of these tells you for certain that a chemical "
                "change has happened?",
        "options": [
            {"text": "One or more new substances have been made",
             "correct": True},
            {"text": "The change happened faster than you expected",
             "correct": False,
             "why": "Speed tells you nothing about what was made. Rusting "
                    "takes months and is chemical; a sugar cube dissolves in "
                    "seconds and is not."},
            {"text": "The change cannot be undone by cooling it",
             "correct": False,
             "why": "Cooling undoes melting and very little else. Smashing a "
                    "glass cannot be undone by cooling either, and no new "
                    "substance was made."},
            {"text": "Something about the way it looks has changed",
             "correct": False,
             "why": "Looks change on both sides of the line. Ice going "
                    "cloudy and a nail going orange look alike, and only one "
                    "of them made something new."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e02",
        "band": "easier",
        "text": "Wax near a candle flame melts and runs down the side. What "
                "kind of change is that?",
        "options": [
            {"text": "Chemical, because a flame was involved in it",
             "correct": False,
             "why": "A flame nearby does not make a change chemical. The wax "
                    "that ran down is still wax, and it sets back into wax "
                    "as it cools."},
            {"text": "Physical, because the wax is still wax",
             "correct": True},
            {"text": "Chemical, because the solid turned into a liquid",
             "correct": False,
             "why": "Solid to liquid is a change of state. The particles are "
                    "the same particles, arranged more loosely — nothing new "
                    "has been made."},
            {"text": "Chemical, because the wax will never be a candle again",
             "correct": False,
             "why": "It can be. Let the wax cool and it is solid wax again. "
                    "Even if it could not be reshaped, that would say "
                    "nothing about new substances."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e03",
        "band": "easier",
        "text": "A spoon of salt is stirred into water until the crystals "
                "disappear. What kind of change is this?",
        "options": [
            {"text": "Chemical, because the salt has disappeared into the "
                     "water", "correct": False,
             "why": "Disappearing is not evidence of anything. Evaporate the "
                    "water and every gram of the salt comes back, "
                    "unchanged."},
            {"text": "Chemical, because the water and the salt made "
                     "something new", "correct": False,
             # SYS-7 — the bank echo of c4-01's salt line, carrying the same
             # tasting credit. Aligned with the lesson so the two cannot
             # drift.
             "why": "Nothing new was made. Evaporate the water and the salt "
                    "comes back unchanged, because the salt is still salt, "
                    "spread out among the water."},
            {"text": "Physical, because the salt is still salt in the water",
             "correct": True},
            {"text": "Physical, because nothing that dissolves is ever a "
                     "reaction", "correct": False,
             "why": "The verdict is right and the rule is not. Marble chips "
                    "dissolve in acid and that is a reaction — dissolving "
                    "can be either kind."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e04",
        "band": "easier",
        "text": "An iron nail left outside turns orange-brown and flakes. "
                "Which piece of evidence shows this is a chemical change?",
        "options": [
            {"text": "It happened slowly, over weeks rather than seconds",
             "correct": False,
             "why": "How long it took decides nothing. Ice melting in a warm "
                    "room also takes time, and no new substance is made."},
            {"text": "Its colour changed from grey to orange-brown",
             "correct": False,
             "why": "Colour changes on both sides of the line. The ice block "
                    "goes cloudy as it melts, and that is not a reaction."},
            {"text": "The nail was left outdoors instead of indoors",
             "correct": False,
             "why": "Where it was kept is not the evidence. It explains why "
                    "air and water reached the nail, not what the flakes "
                    "are."},
            {"text": "The orange flakes are a new substance with new "
                     "properties", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c4-01-s01",
        "band": "standard",
        "text": "Marble chips fizz in acid and slowly disappear. Salt "
                "stirred into water also disappears. Why is only one of them "
                "a chemical change?",
        "options": [
            {"text": "Because the marble disappeared faster than the salt "
                     "did", "correct": False,
             "why": "Speed is not the test, and it is not even reliably "
                    "true. A reaction can be far slower than dissolving, as "
                    "rusting is."},
            {"text": "Because the salt can be got back and the marble "
                     "cannot", "correct": False,
             "why": "That is true, and it is a consequence rather than the "
                    "reason. It follows from the marble having become new "
                    "substances."},
            {"text": "Because the marble was a solid and the salt was a "
                     "crystal", "correct": False,
             "why": "Both are solids, and salt crystals are solid too. What "
                    "separates them is what is in the liquid afterwards."},
            {"text": "Because the marble made new substances and the salt "
                     "did not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s02",
        "band": "standard",
        "text": "A student says \"if a change cannot be undone, it must be "
                "chemical\". Which example shows that the rule is wrong?",
        "options": [
            {"text": "A candle burns away and the wax cannot be got back",
             "correct": False,
             "why": "Burning fits the rule rather than breaking it — it "
                    "cannot be undone and it is chemical, so it tells you "
                    "nothing new."},
            {"text": "A glass smashes on the floor and cannot be put back "
                     "together", "correct": True},
            {"text": "An ice cube melts and can be frozen again in a "
                     "freezer", "correct": False,
             "why": "Melting fits the rule too. It can be undone and it is "
                    "physical, which is the half of the rule that does "
                    "work."},
            {"text": "A nail rusts outside and cannot be cleaned back to "
                     "new", "correct": False,
             "why": "Rusting also fits the rule as stated. To break a rule "
                    "you need a case it gets wrong, not another case it gets "
                    "right."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s03",
        "band": "standard",
        "text": "A candle burns down and the balance underneath it reads "
                "less than it did before. What has happened to the mass?",
        "options": [
            {"text": "Some of the mass has been destroyed by the flame",
             "correct": False,
             "why": "Nothing is destroyed. Every atom that was in the wax is "
                    "still there, in the gases that went up into the room."},
            {"text": "It has been turned into the heat and light given out",
             "correct": False,
             "why": "Heat and light are not made of matter and they weigh "
                    "nothing. The mass left as carbon dioxide and water "
                    "vapour."},
            {"text": "It has left as gases, and the products weigh more than "
                     "the wax", "correct": True},
            {"text": "The balance is wrong, because mass never changes at "
                     "all", "correct": False,
             "why": "The reading is right. Mass does not change in a sealed "
                    "container, and this candle is open to the room, so its "
                    "gases leave."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s04",
        "band": "standard",
        "text": "Sugar in a pan first melts to a clear syrup, then turns "
                "brown and smells of caramel. How many changes are there?",
        "options": [
            {"text": "Two changes: a physical one, then a chemical one",
             "correct": True},
            {"text": "One change, because the pan was heated only once",
             "correct": False,
             "why": "The heating is one action and the changes are two. "
                    "Melted sugar is still sugar; browned sugar is not."},
            {"text": "One change, because the sugar was hot the whole time",
             "correct": False,
             "why": "Staying hot does not make it one change. What matters "
                    "is that the substance itself changed only in the second "
                    "half."},
            {"text": "Two changes, and both of them are chemical changes",
             "correct": False,
             "why": "Melting is not chemical. The syrup is still sugar, and "
                    "it would set back into sugar if it cooled before it "
                    "browned."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c4-01-h01",
        "band": "harder",
        "text": "Rust can be turned back into iron in a steelworks, using a "
                "furnace and carbon. What does that tell you about rusting?",
        "options": [
            {"text": "It is a physical change, because it can be reversed",
             "correct": False,
             "why": "Reversing tells you how much energy and equipment it "
                    "takes, not what was made. Rust is a different substance "
                    "from iron either way."},
            {"text": "It is chemical outdoors and physical inside a furnace",
             "correct": False,
             "why": "A change does not swap kinds depending on the room. "
                    "Rusting made a new substance, and the furnace then "
                    "makes another one."},
            {"text": "It is still a chemical change, because being "
                     "reversible is not the test", "correct": True},
            {"text": "It is a chemical change only while it cannot be "
                     "reversed", "correct": False,
             "why": "There is no such condition. Whether new substances were "
                    "made is settled at the time, not by what somebody "
                    "manages to do later."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h02",
        "band": "harder",
        "text": "Marble chips and acid fizz in an open flask on a balance "
                "and the reading falls. The same reaction is run in a sealed "
                "flask. What does the balance read?",
        "options": [
            {"text": "Less than before, because the gas pushes up on the "
                     "lid", "correct": False,
             "why": "The gas presses on the lid from inside and stays in the "
                    "flask. Nothing has left it, so nothing has been lost."},
            {"text": "Less than before, but by a smaller amount each time",
             "correct": False,
             "why": "There is no smaller loss. In a sealed flask there is no "
                    "loss at all, because nothing can get out."},
            {"text": "More than before, because the gas is packed in "
                     "tightly", "correct": False,
             "why": "Squeezing a gas does not add mass. The same atoms are "
                    "in the flask whether they are packed tight or spread "
                    "out."},
            {"text": "The same as before, because the gas is still inside",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h03",
        "band": "harder",
        "text": "Cream is whipped until it separates and butter forms. No "
                "new substance is made. What kind of change is it?",
        "options": [
            {"text": "Physical, because the fat droplets have only clumped "
                     "together", "correct": True},
            {"text": "Chemical, because the cream will never pour again",
             "correct": False,
             "why": "Being hard to undo is not the test, and the question "
                    "has already told you that no new substance was made."},
            {"text": "Chemical, because butter and cream taste quite "
                     "different", "correct": False,
             "why": "Taste and texture change when things are only "
                    "rearranged. The fat, water and protein in the butter "
                    "came from the cream."},
            {"text": "Physical, because it can be turned back into cream",
             "correct": False,
             "why": "The verdict is right and the reason is not — you cannot "
                    "whip butter back into cream. It is physical because "
                    "nothing new was made."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h04",
        "band": "harder",
        "text": "You want to find out whether a change inside a sealed jar "
                "was chemical. Which test gives you the best evidence?",
        "options": [
            {"text": "Time how long the change takes from start to finish",
             "correct": False,
             "why": "How long it took settles nothing either way. Rusting "
                    "is slow and chemical; boiling is quick and is not."},
            {"text": "Test whether what is in the jar now behaves like what "
                     "went in", "correct": True},
            {"text": "See whether the jar felt warmer while the change "
                     "happened", "correct": False,
             "why": "Warmth appears on both sides of the line. Dissolving "
                    "some solids warms the water, and no new substance is "
                    "made."},
            {"text": "Check whether the colour inside the jar has changed at "
                     "all", "correct": False,
             "why": "Colour changes in both kinds of change. It is a clue "
                    "worth noticing and it settles nothing on its own."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-01-e05",
        "band": "easier",
        "text": "What is a physical change?",
        "options": [
            {"text": "A change that makes no new substance",
             "correct": True},
            {"text": "A change that can be undone easily, by cooling it down "
                     "again or by putting the pieces back where they came "
                     "from",
             "correct": False,
             "why": "Being easy to undo is a clue, not the definition. A "
                    "smashed glass cannot be undone and is physical"},
            {"text": "A change you can see happening",
             "correct": False,
             "why": "Rusting can be watched over weeks and is chemical. "
                    "Seeing it settles nothing"},
            {"text": "A change that needs no heat",
             "correct": False,
             "why": "Melting needs heat and is physical; rusting needs none "
                    "and is chemical. Heat is not the test"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e06",
        "band": "easier",
        "text": "What does the word property mean in this lesson?",
        "options": [
            {"text": "Where a substance is normally found, and what it is "
                     "used for",
             "correct": False,
             "why": "Where it comes from and what it is for are not "
                    "properties. A property is something you can test"},
            {"text": "Something you can find out about a substance by testing "
                     "it",
             "correct": True},
            {"text": "How much of a substance you have",
             "correct": False,
             "why": "That is an amount. A gram of iron and a tonne of it have "
                    "the same properties"},
            {"text": "The name a substance is sold under",
             "correct": False,
             "why": "A name is a label. A property is how the substance "
                    "behaves"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e07",
        "band": "easier",
        "text": "Which of these is a chemical change?",
        "options": [
            {"text": "A mug slipping off a table and smashing into pieces on "
                     "the kitchen floor, so that it can never be used again",
             "correct": False,
             "why": "Every piece is still the same china. Being impossible to "
                    "undo does not make a change chemical"},
            {"text": "Ice melting in a glass of lemonade",
             "correct": False,
             "why": "The ice becomes water, which is the same substance in a "
                    "different state"},
            {"text": "A slice of bread turning to black toast",
             "correct": True},
            {"text": "Sugar stirred into hot tea",
             "correct": False,
             "why": "The sugar is spread through the tea and is still sugar. "
                    "Boil the tea dry and it comes back"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e08",
        "band": "easier",
        "text": "What is another name for a chemical change?",
        "options": [
            {"text": "A change of state",
             "correct": False,
             "why": "That is melting, boiling or freezing — all of them "
                    "physical"},
            {"text": "A separation",
             "correct": False,
             "why": "Filtering and distilling separate mixtures and make "
                    "nothing new"},
            {"text": "A reversible change, since almost every chemical change "
                     "can be run backwards given the right equipment and "
                     "enough energy to do it with",
             "correct": False,
             "why": "Some can be reversed and most are hard to. Either way it "
                    "is not another name for the same thing"},
            {"text": "A chemical reaction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e09",
        "band": "easier",
        "text": "Which list contains only chemical changes?",
        "options": [
            {"text": "Burning, rusting, cooking, acid on marble, respiration",
             "correct": True},
            {"text": "Melting, boiling, dissolving, breaking, mixing",
             "correct": False,
             "why": "Every one of those leaves the same substances behind. "
                    "They are all physical changes"},
            {"text": "Heating, cooling, stirring, pouring, weighing",
             "correct": False,
             "why": "Those are things you DO. Some of them start a reaction "
                    "and none of them is one"},
            {"text": "Anything that gives off a gas, changes colour, or gets "
                     "warm",
             "correct": False,
             "why": "Each of those clues can also happen in a physical "
                    "change, which is why none of them is the test"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e10",
        "band": "easier",
        "text": "A steel nail is bent into a hook. What kind of change is "
                "that?",
        "options": [
            {"text": "Chemical, because the nail cannot be straightened back "
                     "to exactly the shape it had before it was bent",
             "correct": False,
             "why": "Reversibility is not the test, and the hook is still "
                    "steel throughout"},
            {"text": "Physical",
             "correct": True},
            {"text": "Chemical, because bending it takes a lot of force",
             "correct": False,
             "why": "How much effort a change takes has nothing to do with "
                    "what kind it is"},
            {"text": "Neither — bending is not a change",
             "correct": False,
             "why": "It is certainly a change. The question is whether a new "
                    "substance was made, and none was"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e11",
        "band": "easier",
        "text": "In a physical change, what happens to the particles?",
        "options": [
            {"text": "They are broken apart and joined back together in a "
                     "different order, which is what makes the substance look "
                     "different afterwards",
             "correct": False,
             "why": "Breaking joins and making new ones is what a CHEMICAL "
                    "change does"},
            {"text": "Some of them are destroyed",
             "correct": False,
             "why": "Nothing is destroyed in either kind of change. Melting "
                    "ice weighs what the ice weighed"},
            {"text": "They are unchanged — only their arrangement or spacing "
                     "differs",
             "correct": True},
            {"text": "They change into particles of a different substance",
             "correct": False,
             "why": "No particle changes kind in any change on this page. "
                    "That is not even what a reaction does"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-01-e12",
        "band": "easier",
        "text": "A marshmallow held over a flame turns golden-brown, crisp "
                "and smells of caramel. What kind of change is that?",
        "options": [
            {"text": "Chemical, because new substances with a new smell and "
                     "colour have formed", "correct": True},
            {"text": "Physical, because it is still made of sugar",
             "correct": False,
             "why": "The golden colour and new smell are new substances. "
                    "Being built from sugar to start with does not mean "
                    "nothing new was made."},
            {"text": "Physical, because holding it near a flame is not the "
                     "same as burning it", "correct": False,
             "why": "Browning is the flame doing its work. The marshmallow "
                    "is changing exactly because of the heat it is given."},
            {"text": "Chemical, because it cannot be un-browned",
             "correct": False,
             "why": "Not being able to undo it is a clue, not the test. "
                    "What decides it is that new substances have "
                    "appeared."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e13",
        "band": "easier",
        "text": "A rubber band is stretched right out and then let go, and "
                "snaps back to its original size. What kind of change is "
                "that?",
        "options": [
            {"text": "Chemical, because it took real force to stretch",
             "correct": False,
             "why": "How much force a change takes says nothing about what "
                    "was made. The band is still rubber throughout."},
            {"text": "Physical, because it is still the same rubber, just "
                     "stretched", "correct": True},
            {"text": "Chemical, because the shape changed twice",
             "correct": False,
             "why": "Changing shape and changing back is exactly what a "
                    "physical change looks like. No new substance appeared "
                    "at any point."},
            {"text": "Physical, because stretching happens instantly",
             "correct": False,
             "why": "Speed decides nothing. A change is physical because "
                    "of what it does to the substance, not how fast it "
                    "happens."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e14",
        "band": "easier",
        "text": "Baking soda is mixed with vinegar in a model volcano and "
                "the mixture froths up and overflows. What kind of change "
                "is that?",
        "options": [
            {"text": "Chemical, because a gas has been made that was not "
                     "there before", "correct": True},
            {"text": "Physical, because the two liquids have just been "
                     "poured into the same bowl and stirred around a bit",
             "correct": False,
             "why": "They have done more than mix — bubbling gas is coming "
                    "from somewhere, and it is a new substance, carbon "
                    "dioxide, made by the two reacting."},
            {"text": "Chemical, because it fizzes so vigorously",
             "correct": False,
             "why": "Fizzing on its own proves nothing — an opened fizzy "
                    "drink does the same and makes nothing new. The gas "
                    "being a new substance is the evidence."},
            {"text": "Physical, because the froth eventually settles back "
                     "down", "correct": False,
             "why": "Settling down is not the same as reversing. The gas "
                    "that escaped is gone for good and cannot be poured "
                    "back in to remake the baking soda."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e15",
        "band": "easier",
        "text": "A copper statue left outdoors for years slowly turns from "
                "shiny orange-brown to a dull blue-green. What kind of "
                "change is that?",
        "options": [
            {"text": "Physical, because copper does not disappear, it just "
                     "changes colour", "correct": False,
             "why": "Colour changes on both sides of the line. What "
                    "matters is that the green coating is a different "
                    "substance from copper, with different properties."},
            {"text": "Chemical, because rain has washed the shine off the "
                     "surface", "correct": False,
             "why": "Washing removes dirt and leaves the copper underneath "
                    "unchanged. This coating is new and does not wash "
                    "away."},
            {"text": "Chemical — a new substance with new properties has "
                     "formed on the surface", "correct": True},
            {"text": "Physical, because it happens far too slowly to be a "
                     "reaction", "correct": False,
             "why": "Speed says nothing about what kind of change it is. "
                    "Rusting is just as slow and is a reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e16",
        "band": "easier",
        "text": "A metal paperclip is bent back and forth until it snaps in "
                "two. What kind of change is that?",
        "options": [
            {"text": "Physical — it is still the same metal, in two "
                     "pieces", "correct": True},
            {"text": "Chemical, because it cannot be bent back into one "
                     "piece", "correct": False,
             "why": "Not being able to undo it is a clue, not the test. "
                    "The metal in both pieces is still the same metal it "
                    "always was."},
            {"text": "Chemical, because bending it took a lot of effort",
             "correct": False,
             "why": "Effort is not the test either. Bending metal is "
                    "entirely physical, however much force it takes."},
            {"text": "Chemical, because the shape has changed completely",
             "correct": False,
             "why": "Shape changing is exactly what a physical change "
                    "does. No new substance was made anywhere along the "
                    "wire."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e17",
        "band": "easier",
        "text": "What does calling a change \"reversible\" actually tell "
                "you?",
        "options": [
            {"text": "That it can be undone, which is a fact about energy "
                     "and equipment rather than about which kind of change "
                     "it is", "correct": True},
            {"text": "That it is definitely a physical change",
             "correct": False,
             "why": "Some physical changes are hard or impossible to "
                    "reverse — smashing a glass, for instance — so "
                    "reversibility does not sort changes into the two "
                    "kinds."},
            {"text": "That no new substance was made, because a change "
                     "that can be undone by cooling, squeezing or waiting "
                     "can never make anything that was not already there",
             "correct": False,
             "why": "Reversibility is a separate fact from whether a new "
                    "substance was made. A reaction can even be reversed, "
                    "given the right equipment, and it is still chemical."},
            {"text": "That the change happened quickly", "correct": False,
             "why": "Speed and reversibility are unrelated facts about a "
                    "change. Neither one is the test for chemical or "
                    "physical."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e18",
        "band": "easier",
        "text": "Milk left out of the fridge for a week turns lumpy, "
                "sour-smelling and undrinkable. What kind of change is "
                "that?",
        "options": [
            {"text": "Chemical — new substances have formed that were not "
                     "in the fresh milk", "correct": True},
            {"text": "Physical, because the milk has just separated into "
                     "its parts", "correct": False,
             "why": "Separating parts already there would leave you with "
                    "milk and cream, not a sour, lumpy substance with a "
                    "completely different smell."},
            {"text": "Physical, because it happened without anyone heating "
                     "it", "correct": False,
             "why": "Heat is not required for a reaction. This one happens "
                    "at room temperature and still makes new substances."},
            {"text": "Chemical, because it smells much worse than fresh "
                     "milk", "correct": False,
             "why": "Smell alone is a clue rather than proof. What settles "
                    "it is that the sourness and lumps are substances the "
                    "fresh milk never contained."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e19",
        "band": "easier",
        "text": "An orange is squeezed and juice runs out into a glass. "
                "What kind of change is that?",
        "options": [
            {"text": "Chemical, because the orange is destroyed in the "
                     "process", "correct": False,
             "why": "Nothing is destroyed — the juice, pulp and peel are "
                    "exactly the substances that were inside the orange "
                    "already."},
            {"text": "Physical — the juice was already inside the orange",
             "correct": True},
            {"text": "Chemical, because squeezing needs force",
             "correct": False,
             "why": "Force does not decide it. Squashing something is "
                    "physical, however hard you press."},
            {"text": "Physical, because the juice tastes the same as the "
                     "orange it came from", "correct": False,
             "why": "Taste is a clue rather than the test — what matters "
                    "is that no new substance was made, whatever it tastes "
                    "like."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e20",
        "band": "easier",
        "text": "A silver spoon left in a drawer for months develops a "
                "dark, dull coating. What kind of change is that?",
        "options": [
            {"text": "Physical, because the silver is still there "
                     "underneath", "correct": False,
             "why": "Being underneath is not the point. The dark coating "
                    "on top is a new substance with new properties, not "
                    "silver."},
            {"text": "Chemical — the dark coating is a new substance",
             "correct": True},
            {"text": "Physical, because polishing brings the shine "
                     "straight back", "correct": False,
             "why": "Being possible to reverse with polish is a clue about "
                    "difficulty, not about what was made. A new substance "
                    "still formed on the surface."},
            {"text": "Chemical, because the spoon feels rougher than "
                     "before", "correct": False,
             "why": "Texture is a clue and not the test. What matters is "
                    "that the dark coating is a different substance from "
                    "silver."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e21",
        "band": "easier",
        "text": "A stick of chalk is ground up into a fine white powder "
                "using a pestle and mortar. What kind of change is that?",
        "options": [
            {"text": "Chemical, because the chalk has been broken into "
                     "such tiny pieces", "correct": False,
             "why": "Breaking something into smaller pieces makes no new "
                    "substance, however small the pieces get. The powder "
                    "is still the same substance."},
            {"text": "Physical — it is still the same substance, just "
                     "smaller pieces", "correct": True},
            {"text": "Chemical, because grinding needs a lot of force",
             "correct": False,
             "why": "Effort does not decide it. Grinding is physical, "
                    "however hard the pestle is pushed."},
            {"text": "Physical, because the powder can be squeezed back "
                     "into a solid lump", "correct": False,
             "why": "The verdict is right and the reason is not — chalk "
                    "powder does not squeeze back into a solid stick. It is "
                    "physical because no new substance was made."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e22",
        "band": "easier",
        "text": "A firework banger goes off with a loud bang, a flash and a "
                "puff of grey smoke. What kind of change is that?",
        "options": [
            {"text": "Chemical — the smoke and gases are new substances",
             "correct": True},
            {"text": "Physical, because it is over in a fraction of a "
                     "second", "correct": False,
             "why": "Speed says nothing about what kind of change it is. A "
                    "reaction can be instant or take years."},
            {"text": "Physical, because the bang is just air being pushed "
                     "suddenly", "correct": False,
             "why": "The bang comes from hot gases expanding fast — and "
                    "those gases are new substances that were not inside "
                    "the banger before it went off."},
            {"text": "Chemical, because it is impossible to put back "
                     "together", "correct": False,
             "why": "Being impossible to reverse is a clue and not the "
                    "test. The smoke being new substances is the actual "
                    "evidence."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e23",
        "band": "easier",
        "text": 'In a chemical reaction the atoms are joined up differently. '
                'Compared with before the reaction, how many atoms of each kind '
                'are there afterwards?',
        "options": [
            {"text": "Fewer, because some are used up making the new "
                     "substance", "correct": False,
             "why": "Used up means joined to something else, not gone. "
                    "Every atom that went in is still there afterwards."},
            {"text": "More, because new substances have appeared",
             "correct": False,
             "why": "A new substance is a new arrangement of the same "
                    "atoms, not extra atoms. None are added."},
            {"text": "It depends on how much heat the reaction gives out",
             "correct": False,
             "why": "Heat given out changes the temperature of the "
                    "surroundings. It has no effect on how many atoms "
                    "exist."},
            {"text": "Exactly the same number", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e24",
        "band": "easier",
        "text": "A block of butter left on a hot kitchen counter melts into "
                "a pool of oil. What kind of change is that?",
        "options": [
            {"text": "Chemical, because a solid has turned into a liquid",
             "correct": False,
             "why": "A change of state is physical. The melted butter is "
                    "still exactly the same substance as the solid block."},
            {"text": "Chemical, because the kitchen was hot",
             "correct": False,
             "why": "Being warm is not the test. Melting needs heat and "
                    "makes nothing new, so it stays physical."},
            {"text": "Physical — it is still butter, just in liquid form",
             "correct": True},
            {"text": "Physical, because it will set solid again once it "
                     "cools", "correct": False,
             "why": "Setting again is a consequence rather than the "
                    "reason. It is physical because no new substance was "
                    "made, whether or not it later cools."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e25",
        "band": "easier",
        "text": "Vinegar poured onto a piece of limestone rock outdoors "
                "makes it fizz, and a gas bubbles off. What kind of change "
                "is that?",
        "options": [
            {"text": "Physical, because the rock is only dissolving into "
                     "the vinegar", "correct": False,
             "why": "Something more than dissolving is happening here — a "
                    "gas is escaping, which is a new substance the rock "
                    "and the vinegar did not contain."},
            {"text": "Chemical, because the rock slowly disappears",
             "correct": False,
             "why": "Disappearing is not evidence of anything on its own "
                    "— salt disappears into water and makes nothing new. "
                    "The gas is the evidence here."},
            {"text": "Physical, because it happens outdoors rather than in "
                     "a lab", "correct": False,
             "why": "Where a change happens has no bearing on what kind it "
                    "is. The same reaction fizzes just as well on a bench."},
            {"text": "Chemical — a new gas has been produced",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e26",
        "band": "easier",
        "text": "A sparkler burns with bright white light and leaves behind "
                "a bent grey wire coated in ash. What kind of change is "
                "that?",
        "options": [
            {"text": "Chemical — the ash is a new substance with new "
                     "properties", "correct": True},
            {"text": "Physical, because the wire is still there "
                     "afterwards, and a physical change is any change that "
                     "leaves the original object in one recognisable piece",
             "correct": False,
             "why": "The wire being there is not the point. What has "
                    "coated it is a new substance, made by the metal "
                    "reacting as it burns."},
            {"text": "Physical, because light is not a substance",
             "correct": False,
             "why": "True about light, and beside the point. The verdict "
                    "is decided by the ash, which is a new substance."},
            {"text": "Chemical, because it gives out so much light",
             "correct": False,
             "why": "Brightness is a clue rather than the test. The new "
                    "grey coating is the actual evidence."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e27",
        "band": "easier",
        "text": "Which of these is generally true of a PHYSICAL change?",
        "options": [
            {"text": "It always needs a naked flame to start it",
             "correct": False,
             "why": "Most physical changes need no flame at all — melting "
                    "ice needs nothing but a warm room."},
            {"text": "It always produces a gas, because breaking the "
                     "joins between particles releases whatever was "
                     "trapped inside them", "correct": False,
             "why": "Very few physical changes make a gas. Melting, "
                    "freezing and dissolving make none at all."},
            {"text": "It is usually easy to reverse, and the same total "
                     "mass comes back", "correct": True},
            {"text": "It can only happen to solids", "correct": False,
             "why": "Liquids and gases undergo physical changes too — "
                    "boiling and condensing are both physical."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e28",
        "band": "easier",
        "text": "A puddle of rainwater on a path freezes solid overnight in "
                "cold weather. What kind of change is that?",
        "options": [
            {"text": "Physical — it is still water, just in a different "
                     "state", "correct": True},
            {"text": "Chemical, because a liquid has turned into a solid",
             "correct": False,
             "why": "A change of state is physical, whichever way it "
                    "goes. Freezing makes ice, and ice is still water."},
            {"text": "Chemical, because it is now hard enough to slip on",
             "correct": False,
             "why": "A new texture is not evidence of a new substance. Ice "
                    "is water, arranged differently."},
            {"text": "Physical, because it happened without anyone doing "
                     "anything to it", "correct": False,
             "why": "Whether a person caused it makes no difference to the "
                    "kind of change. What matters is that no new substance "
                    "appeared."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e29",
        "band": "easier",
        "text": "A snowman left out on a warmer day slowly shrinks into a "
                "puddle. What kind of change is that?",
        "options": [
            {"text": "Chemical, because so much of it has disappeared",
             "correct": False,
             "why": "Disappearing on its own proves nothing. The puddle is "
                    "exactly the same water the snow was made of."},
            {"text": "Physical — the puddle is the same water the snow "
                     "was made of", "correct": True},
            {"text": "Chemical, because it cannot be turned back into the "
                     "same snowman shape", "correct": False,
             "why": "Being unable to rebuild the shape is not the test. "
                    "The water itself has not become anything new."},
            {"text": "Physical, because it happens slowly over the day",
             "correct": False,
             "why": "Speed decides nothing here either way. It is "
                    "physical because the substance itself, water, has not "
                    "changed."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e30",
        "band": "easier",
        "text": "A clean iron nail is dipped into a blue copper sulfate "
                "solution and comes out coated in a pinkish-orange layer. "
                "What kind of change is that?",
        "options": [
            {"text": "Physical, because the nail is still solid metal",
             "correct": False,
             "why": "Still being a solid says nothing about what it is "
                    "made of now. The pinkish-orange coating is a new "
                    "substance, not iron."},
            {"text": "Physical, because the solution has just stained the "
                     "nail", "correct": False,
             "why": "Staining leaves the surface the same substance "
                    "underneath a layer of dye. Here the coating itself is "
                    "a different metal from iron."},
            {"text": "Chemical — a new substance has coated the nail",
             "correct": True},
            {"text": "Chemical, because the solution changed colour too",
             "correct": False,
             "why": "The colour change is a clue rather than the proof. "
                    "The new coating on the nail is the actual evidence of "
                    "a new substance."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e31",
        "band": "easier",
        "text": "Sugar is dissolved in a cup of tea. The tea is left "
                "uncovered on a windowsill until all the water has "
                "evaporated, leaving dry crystals in the bottom. What kind "
                "of change was the dissolving?",
        "options": [
            {"text": "Chemical, because the sugar completely disappeared "
                     "into the tea", "correct": False,
             "why": "Disappearing into a liquid is not evidence of "
                    "anything by itself. Evaporating the tea brings the "
                    "exact same sugar back."},
            {"text": "Chemical, because tea and sugar are two different "
                     "substances mixed together", "correct": False,
             "why": "Being two different substances does not make mixing "
                    "them a reaction. Nothing new was made when the sugar "
                    "dissolved."},
            {"text": "Physical, because tea is a liquid", "correct": False,
             "why": "What state the tea is in has nothing to do with it. "
                    "It is physical because the sugar is still sugar, "
                    "dissolved or not."},
            {"text": "Physical — the crystals left behind are the same "
                     "sugar", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-e32",
        "band": "easier",
        "text": "A used match, black and brittle where it burned, will not "
                "light again and cannot be turned back into a fresh "
                "matchstick. What kind of change happened when it burned?",
        "options": [
            {"text": "Physical, because the match is still the same "
                     "shape", "correct": False,
             "why": "Keeping its shape says nothing about what it is made "
                    "of now. The charred tip is a new substance, not the "
                    "wood it started as."},
            {"text": "Physical, because burning just dries the wood out "
                     "completely", "correct": False,
             "why": "Drying leaves wood as wood, only lighter. Burning "
                    "turns it into ash and gases, which are new "
                    "substances."},
            {"text": "Chemical, because it will never look like a fresh "
                     "match again", "correct": False,
             "why": "Looking different is a clue and not the test. The "
                    "new, brittle black substance is what actually decides "
                    "it."},
            {"text": "Chemical — the black material is a new substance, "
                     "not wood", "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c4-01-s05",
        "band": "standard",
        "text": "Bubbling is often given as a sign of a chemical change. "
                "Which example shows that it is not a reliable one?",
        "options": [
            {"text": "A pan of water boiling on a hob",
             "correct": True},
            {"text": "Marble chips fizzing in hydrochloric acid until the "
                     "chips have gone and the tube has stopped bubbling "
                     "altogether",
             "correct": False,
             "why": "That one IS chemical. To show the sign is unreliable you "
                    "need bubbling with no reaction"},
            {"text": "Magnesium fizzing in dilute acid",
             "correct": False,
             "why": "Also chemical — the bubbles are hydrogen, a new "
                    "substance"},
            {"text": "Bread rising in an oven",
             "correct": False,
             "why": "The gas comes from a reaction in the dough, so this is a "
                    "chemical change too"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s06",
        "band": "standard",
        "text": "An egg is fried and sets solid, and cooling it does not make "
                "it runny again. Which piece of evidence shows the change is "
                "chemical?",
        "options": [
            {"text": "That cooling it does not undo it, since a physical "
                     "change always can be",
             "correct": False,
             "why": "A smashed glass is physical and cannot be undone at all. "
                    "Reversibility is a clue, not the test"},
            {"text": "That the set egg is a new substance which behaves "
                     "nothing like the runny one",
             "correct": True},
            {"text": "That heat was needed",
             "correct": False,
             "why": "Melting ice needs heat and makes nothing new"},
            {"text": "That the egg changed colour",
             "correct": False,
             "why": "Ice going cloudy changes colour and is physical. Colour "
                    "appears on both sides of the line"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s07",
        "band": "standard",
        "text": "Iron filings and sulfur are stirred together, then heated "
                "until the mixture glows. Which of the two steps is the "
                "chemical change?",
        "options": [
            {"text": "The stirring, because that is when the two substances "
                     "first come into contact with each other and can begin "
                     "to affect one another",
             "correct": False,
             "why": "Stirring puts them in the same dish and joins nothing. A "
                    "magnet still pulls the iron out afterwards"},
            {"text": "Both of them",
             "correct": False,
             "why": "Only one of them makes a new substance. Before heating, "
                    "both elements are still themselves"},
            {"text": "The heating",
             "correct": True},
            {"text": "Neither — the same two elements are there throughout",
             "correct": False,
             "why": "The same ATOMS are there throughout, and after heating "
                    "they are joined into a new substance"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s08",
        "band": "standard",
        "text": "A student says heat always means a chemical change is "
                "happening. Which single example deals with that?",
        "options": [
            {"text": "A candle burning, which needs heat to start and gives "
                     "out a great deal more of it once it is going",
             "correct": False,
             "why": "That is a chemical change WITH heat, so it agrees with "
                    "the student rather than refuting them"},
            {"text": "Iron rusting in a damp shed",
             "correct": False,
             "why": "This is a chemical change with no heat at all — which "
                    "shows heat is not NEEDED, a different point"},
            {"text": "Sugar caramelising in a hot pan",
             "correct": False,
             "why": "Chemical, and hot. It supports the student's rule rather "
                    "than breaking it"},
            {"text": "Ice melting on a warm windowsill",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s09",
        "band": "standard",
        "text": "Green copper carbonate is heated. It turns black and a gas "
                "comes off that turns limewater cloudy. Which verdict and "
                "evidence are both right?",
        "options": [
            {"text": "Chemical, because a black solid and a gas are both "
                     "substances that were not there before",
             "correct": True},
            {"text": "Physical, because the powder is still a powder "
                     "afterwards",
             "correct": False,
             "why": "The gas turns limewater cloudy, so it is carbon dioxide "
                    "— a substance that was not there before"},
            {"text": "Chemical, because the colour changed",
             "correct": False,
             "why": "Right verdict, wrong evidence. Colour changes on both "
                    "sides of the line"},
            {"text": "Physical, because heating is a physical process",
             "correct": False,
             "why": "Heating is something you do. What matters is what you "
                    "have afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s10",
        "band": "standard",
        "text": "Electricity is passed through water and two different gases "
                "bubble off. What kind of change is that?",
        "options": [
            {"text": "Physical, because the water has only been split into "
                     "the parts it was already made of, and nothing new has "
                     "had to be built out of anything",
             "correct": False,
             "why": "Hydrogen and oxygen are substances water is not. Being "
                    "made of the same atoms is true of every reaction"},
            {"text": "Chemical",
             "correct": True},
            {"text": "Physical, because it is a kind of separation like "
                     "filtering",
             "correct": False,
             "why": "Filtering separates substances already sitting side by "
                    "side. Here the joins between atoms are broken"},
            {"text": "Neither, because electricity is not a substance",
             "correct": False,
             "why": "Electricity is the condition that drives it. The change "
                    "itself is judged by what is made"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s11",
        "band": "standard",
        "text": "Dry ice put on a bench turns straight into a gas and leaves "
                "no puddle at all. Which kind of change is it?",
        "options": [
            {"text": "Chemical, because a solid turning into a gas with no "
                     "liquid stage in between can only happen if the "
                     "substance itself has been changed",
             "correct": False,
             "why": "Sublimation is a change of state like any other. The "
                    "substance is carbon dioxide before and after"},
            {"text": "Chemical, because the solid disappears completely",
             "correct": False,
             "why": "Disappearing is not evidence of anything. Salt "
                    "disappears into water and is still salt"},
            {"text": "Physical",
             "correct": True},
            {"text": "Chemical, because carbon dioxide is a new substance",
             "correct": False,
             "why": "It is not new — dry ice IS carbon dioxide, in the solid "
                    "state"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 top-up ────────────────────────────────────────
    {
        "id": "c4-01-s12",
        "band": "standard",
        "text": "A spoon of sugar is heated in a pan until it blackens and "
                "smells of smoke, while a second spoon of sugar is stirred "
                "into a cup of tea and disappears. Only one of these is a "
                "chemical change. Which, and why?",
        "options": [
            {"text": "The heated sugar, because it smells much stronger than "
                     "the sugar in the tea",
             "correct": False,
             "why": "Smell is a clue rather than the test. What matters is "
                    "whether a new substance was made, not how strong the "
                    "smell is."},
            {"text": "The sugar in the tea, because it vanished completely and "
                     "the heated sugar is still visible in the pan",
             "correct": False,
             "why": "Vanishing is not evidence of anything — the dissolved "
                    "sugar is still sugar and comes back on evaporating. The "
                    "blackened sugar does not."},
            {"text": "The heated sugar, because burnt sugar is a new substance "
                     "and the dissolved sugar is still sugar", "correct": True},
            {"text": "Both, because heat and stirring both count as ways of "
                     "starting a reaction, whatever the substance being heated "
                     "or stirred",
             "correct": False,
             "why": "Stirring starts nothing chemical. The tea sugar can be "
                    "recovered unchanged; the burnt sugar cannot."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s13",
        "band": "standard",
        "text": "A rusty garden gate is given a fresh coat of paint. Has the "
                "paint reversed the rusting?",
        "options": [
            {"text": "No — the rust is still rust underneath the paint", "correct": True},
            {"text": "Yes — the gate looks like new again",
             "correct": False,
             "why": "Looking new is not the test. The rust is still there "
                    "under the paint, unchanged — it has been hidden, not "
                    "turned back into iron."},
            {"text": "Yes, because paint stops the gate rusting any further",
             "correct": False,
             "why": "Stopping future rusting is real, and it is a different "
                    "question from whether the rust already there has been "
                    "undone. It has not."},
            {"text": "No — paint can never be applied to a rusty surface",
             "correct": False,
             "why": "Paint is applied to rusty gates all the time. What it "
                    "cannot do is turn the rust back into iron."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s14",
        "band": "standard",
        "text": 'Two identical ice cubes are set out: one melts completely in '
                'the sun, the other is taken out an hour later and melts slowly '
                'on a cold windowsill. Are both changes physical, even though '
                'one took far longer?',
        "options": [
            {"text": 'No — only the fast one counts as melting; the slow one is '
                     'the ice soaking into the air',
             "correct": False,
             "why": 'Both cubes melt: the water runs out of the solid in each '
                    'case. Taking longer over it does not make it a different '
                    'kind of change.'},
            {"text": 'Yes, because melting is always chemical when it happens '
                     'fast enough in the sun, especially on a very warm day',
             "correct": False,
             "why": "Speed never decides it, and melting is never chemical "
                    "however fast it happens. The ice is still water either "
                    "way."},
            {"text": 'No — a change of state can only be called physical once '
                     'it has actually finished happening',
             "correct": False,
             "why": 'Melting is physical the whole time it is happening, not '
                    'only once it is complete. The slow cube is midway through '
                    'the same change.'},
            {"text": 'Yes — melting is a physical change whatever the speed, '
                     'because the water is the same water throughout', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s15",
        "band": "standard",
        "text": "A limestone statue outdoors is slowly worn away by acid rain "
                "over several decades, its surface pitted and flaking. What "
                "kind of change is that?",
        "options": [
            {"text": "Physical, because it happens far too slowly to be "
                     "noticed on any single day",
             "correct": False,
             "why": "Speed says nothing about the kind of change. Rusting is "
                    "just as slow and is chemical throughout."},
            {"text": "Chemical — the acid reacts with the limestone to make "
                     "new, soluble substances that wash away", "correct": True},
            {"text": "Physical, because rain is just water wearing the stone "
                     "away like a river wears down a rock",
             "correct": False,
             "why": "Plain water wearing stone down is physical erosion — and "
                    "acid rain does more than that: it reacts with the "
                    "limestone and dissolves it into new substances."},
            {"text": "Chemical, because the statue looks much rougher than it "
                     "used to",
             "correct": False,
             "why": "Texture is a clue rather than the test. What settles it "
                    "is that the acid has made new substances out of the "
                    "limestone."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s16",
        "band": "standard",
        "text": "A slice of bread is toasted until golden, then left in the "
                "toaster too long and turns black and smoky. Are both stages "
                "the same kind of change?",
        "options": [
            {"text": "No — only the black, smoky stage is chemical, because "
                     "that is when new substances such as smoke and carbon "
                     "appear",
             "correct": False,
             "why": "Read the browning again: the golden stage already has new "
                    "substances forming — that is what makes toast taste of "
                    "toast rather than bread."},
            {"text": "No — only the golden stage is chemical, because burnt "
                     "toast is simply toast with the water removed",
             "correct": False,
             "why": "Burning is not drying. The black material has different "
                    "properties from bread and cannot be turned back into it "
                    "by adding water."},
            {"text": "Yes — both stages make new substances, and the second "
                     "stage simply makes more of them", "correct": True},
            {"text": "Yes, but only because a toaster uses heat for both "
                     "stages",
             "correct": False,
             "why": "Using heat both times is true and is not the reason. Both "
                    "stages are chemical because both make new substances, "
                    "whatever supplied the heat."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s17",
        "band": "standard",
        "text": "A cold pack is activated by snapping an inner pouch, and the "
                "outside of the pack turns icy cold as a solid dissolves in "
                "the water inside. No new substance is made. Why does a "
                "student mistake this for a chemical change?",
        "options": [
            {"text": "Because they think only a chemical change can make "
                     "something feel colder or hotter", "correct": True},
            {"text": "Because dissolving can never make a mixture colder than "
                     "either substance started at",
             "correct": False,
             "why": "It can, and this pack does it. That fact does not make "
                    "the dissolving chemical — it stays physical either way."},
            {"text": "Because snapping the pouch makes a loud noise",
             "correct": False,
             "why": "A noise on its own is not why this looks chemical. The "
                    "temperature drop is what misleads a student."},
            {"text": "Because the pack cannot be reused once it has been "
                     "activated",
             "correct": False,
             "why": "Being single-use is a fact about the packaging, not about "
                    "the chemistry. Nothing here is irreversible in the way a "
                    "reaction is."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s18",
        "band": "standard",
        "text": "An antacid tablet dropped into water fizzes hard and slowly "
                "disappears. A sugar cube dropped into water also slowly "
                "disappears, with no fizzing. Why is only the tablet a "
                "chemical change?",
        "options": [
            {"text": "Because fizzing always means a chemical change is "
                     "happening, since bubbles can only appear when brand new "
                     "substances are being made",
             "correct": False,
             "why": "Fizzing is a strong clue and still only a clue — a shaken "
                    "fizzy drink bubbles and makes nothing new. The gas being "
                    "a new substance is the real evidence."},
            {"text": "Because the tablet makes a gas that was not there "
                     "before, and the sugar does not", "correct": True},
            {"text": "Because sugar dissolves much faster in water than the "
                     "tablet ever does",
             "correct": False,
             "why": "Speed of dissolving decides nothing about the kind of "
                    "change. What matters is whether a new substance appears."},
            {"text": "Because the tablet is a solid and sugar is a crystal in "
                     "the cupboard",
             "correct": False,
             "why": "Sugar crystals are solid too. The difference is what the "
                    "tablet makes in the water, not what shape either one "
                    "started as."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s19",
        "band": "standard",
        "text": "A blacksmith heats a bar of iron until it glows white-hot and "
                "hammers it into the shape of a horseshoe. Which piece of "
                "evidence shows this is a physical change?",
        "options": [
            {"text": "That hammering the hot iron requires so much strength "
                     "and skill that only a real chemical reaction could "
                     "possibly need that much effort",
             "correct": False,
             "why": "How much effort a change takes is not the test. Skilled "
                    "work can be entirely physical."},
            {"text": "That the glowing bar is far too hot to touch",
             "correct": False,
             "why": "Temperature is a clue and not the test. Rusting needs no "
                    "heat at all and is chemical."},
            {"text": "That the cooled horseshoe is still iron, with the same "
                     "properties as the bar it was made from", "correct": True},
            {"text": "That the horseshoe keeps its new shape once it has "
                     "cooled down, instead of springing back to being a "
                     "straight bar",
             "correct": False,
             "why": "Keeping a new shape happens in plenty of chemical changes "
                    "too — a set jelly keeps its mould shape. What matters is "
                    "whether the substance itself is new."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s20",
        "band": "standard",
        "text": "Yeast is stirred into a warm sugar solution and left covered "
                "for a day. The mixture bubbles steadily and develops a "
                "strong, sharp smell it did not have before. What kind of "
                "change is that?",
        "options": [
            {"text": "Chemical — the bubbling gas and the new smell are "
                     "evidence of new substances", "correct": True},
            {"text": "Physical, because yeast is a living thing rather than a "
                     "chemical",
             "correct": False,
             "why": "What the yeast is made of does not decide it. The sugar "
                    "solution itself is changing into substances it did not "
                    "contain before."},
            {"text": "Physical, because the sugar is only dissolving further "
                     "as it warms up",
             "correct": False,
             "why": "Warming would dissolve more sugar and would not produce a "
                    "gas or a new smell on its own. Something is being made "
                    "here, not just dissolved."},
            {"text": "Chemical, because it has been left covered for a whole "
                     "day",
             "correct": False,
             "why": "How long it was left is not the evidence. Some reactions "
                    "finish in seconds and some physical changes take days, "
                    "like a puddle drying."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s21",
        "band": "standard",
        "text": 'Cream is whipped into soft peaks for a dessert, and a second '
                'bowl of cream is whipped much further until it separates into '
                'butter and a watery liquid. Both of these are physical '
                'changes. What is the same about them?',
        "options": [
            {"text": "In both, air is trapped inside the fat in exactly the "
                     "same amount",
             "correct": False,
             "why": "Butter has almost no air trapped in it — whipping it that "
                    "far knocks the air back out. The similarity is not about "
                    "air."},
            {"text": "In both, the cream has been heated to make it change",
             "correct": False,
             "why": "No heating is needed for either — whisking alone does "
                    "both, at room temperature."},
            {"text": "In both, a new substance called butterfat has been "
                     "created",
             "correct": False,
             "why": "There is no such thing as \"butterfat\" being newly "
                    "created — the fat in butter is the same fat that was "
                    "already in the cream."},
            {"text": "In both, the fat in the cream is rearranged rather than "
                     "turned into a new substance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s22",
        "band": "standard",
        "text": "A student says a piece of wood cannot be undergoing a "
                "chemical change as it burns, because it never bubbles or "
                "fizzes the way a reaction in a test tube does. What is the "
                "reply?",
        "options": [
            {"text": "Bubbling only happens to liquids, and wood is a solid, "
                     "so the rule does not apply to it",
             "correct": False,
             "why": "The rule was never about liquids and solids. It is that "
                    "bubbling is only ever a clue, present in some reactions "
                    "and absent from others, chemical or not."},
            {"text": "Burning wood does bubble, just too fast to see",
             "correct": False,
             "why": "There is no hidden bubbling to find. The evidence for "
                    "burning being chemical is the ash, smoke and gases made, "
                    "not bubbles."},
            {"text": "Bubbling is one possible clue among several, and its "
                     "absence proves nothing either way", "correct": True},
            {"text": "The student is right, and burning wood is a physical "
                     "change just like melting or sawing it would be",
             "correct": False,
             "why": "Burning makes ash and gases that were not in the wood "
                    "before, with different properties from wood. That makes "
                    "it chemical, bubbles or none."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s23",
        "band": "standard",
        "text": "A puddle of water is left in the sun and slowly disappears, "
                "while a bowl of the same water is boiled until it has all "
                "boiled away. Are these two the same kind of change?",
        "options": [
            {"text": "No — boiling is chemical because it needs heat, and "
                     "evaporating in the sun is physical because it does not",
             "correct": False,
             "why": "Both need energy to turn liquid into gas — the sun "
                    "supplies it slowly, the flame quickly. Needing energy "
                    "does not make either one chemical."},
            {"text": "Yes — both are water turning into water vapour, which is "
                     "still water", "correct": True},
            {"text": "No — only evaporation in the sun can be reversed, so "
                     "only that one is physical",
             "correct": False,
             "why": "Both can be reversed — the vapour from boiling condenses "
                    "back into water just as the puddle's vapour does. Both "
                    "are physical."},
            {"text": "Yes, but only because both happen outdoors in warm "
                     "weather",
             "correct": False,
             "why": "The setting is not the reason. Both are physical because "
                    "the substance stays water throughout, indoors or out."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s24",
        "band": "standard",
        "text": "Zinc granules dropped into dilute acid fizz hard as hydrogen "
                "gas is given off. The same granules dropped into a beaker of "
                "plain water do nothing at all. What does the comparison show?",
        "options": [
            {"text": "That whether a chemical change happens depends on which "
                     "substances are brought together, not just on which one "
                     "you are watching", "correct": True},
            {"text": "That zinc always reacts, and the water sample must have "
                     "been contaminated with something, the way a dirty beaker "
                     "can leave invisible traces of other chemicals behind "
                     "between experiments",
             "correct": False,
             "why": "There is no such rule. Whether a reaction happens depends "
                    "on what the zinc is put with, not on some fixed habit of "
                    "the metal."},
            {"text": "That zinc is only a real substance when it is reacting "
                     "with something",
             "correct": False,
             "why": "Zinc sitting quietly in water is still zinc, whether or "
                    "not it is reacting. Reacting is not what makes it a "
                    "substance."},
            {"text": "That water can never take part in a chemical change",
             "correct": False,
             "why": "Water reacts readily with plenty of substances — sodium, "
                    "for one. It simply does not react with zinc."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s25",
        "band": "standard",
        "text": "A balloon is inflated until it stretches thin and pops with a "
                "loud bang. No new substance is made anywhere in this. What "
                "kind of change is it, despite the bang?",
        "options": [
            {"text": "Chemical, because a bang that loud can only come from a "
                     "reaction",
             "correct": False,
             "why": "A bang is a clue about energy released suddenly, not "
                    "about what kind of change caused it. Popped rubber is "
                    "still rubber."},
            {"text": "Chemical, because the balloon cannot be put back "
                     "together afterwards, which is exactly the kind of "
                     "permanent change a reaction is supposed to leave behind",
             "correct": False,
             "why": "Being unable to reverse it is not the test — the question "
                    "already says no new substance was made, which settles it "
                    "as physical."},
            {"text": "Physical — the rubber and the air inside are exactly the "
                     "same substances as before it popped", "correct": True},
            {"text": "Physical, but only because it happened so suddenly",
             "correct": False,
             "why": "Speed is not the reason. It is physical because nothing "
                    "new was made, whether the change takes a second or a "
                    "year."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s26",
        "band": "standard",
        "text": "A hand warmer sachet is squeezed, and a solid slowly "
                "crystallises out of the liquid inside as the sachet gets "
                "noticeably hot. Is heat being given out proof that a new "
                "substance has been made?",
        "options": [
            {"text": "Yes — only a chemical change can ever warm its "
                     "surroundings up the way this sachet has",
             "correct": False,
             "why": "This sachet warms up and makes no new substance at all — "
                    "crystallising can give out heat just as much as a "
                    "reaction can."},
            {"text": "No — crystallising is physical and can still give out "
                     "heat as it happens", "correct": True},
            {"text": "Yes, because squeezing the sachet is what triggers a "
                     "hidden reaction inside it",
             "correct": False,
             "why": "The squeeze only disturbs the liquid enough to start it "
                    "crystallising. The solid that forms is the same substance "
                    "the liquid was made of."},
            {"text": "No, because a physical change is never warm to touch",
             "correct": False,
             "why": "Some physical changes do feel warm, as this one does. "
                    "What decides chemical or physical is whether a new "
                    "substance forms, not the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s27",
        "band": "standard",
        "text": "Powdered marble fizzes furiously in acid and finishes "
                "reacting in seconds. A single large marble chip in the same "
                "acid fizzes gently and takes several minutes. Is one of these "
                "reactions and the other not?",
        "options": [
            {"text": "Yes — only the fast one counts as a genuine chemical "
                     "reaction",
             "correct": False,
             "why": "Speed of a reaction is not what makes it chemical. Both "
                    "the powder and the chip end up as the same new "
                    "substances, just at different rates."},
            {"text": "Yes — the slow chip is only dissolving, and the fast "
                     "powder is reacting",
             "correct": False,
             "why": "Both produce the same fizzing gas and both chips vanish "
                    "for the same reason. Neither is simple dissolving."},
            {"text": "No, because marble always reacts at exactly the same "
                     "rate whatever size it is broken into",
             "correct": False,
             "why": "Rate very much depends on the size of the pieces — that "
                    "is why the powder reacts faster. The kind of change is "
                    "what stays the same."},
            {"text": "No — both are the same reaction, going at different "
                     "speeds", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s28",
        "band": "standard",
        "text": "Butter melts into a pool in a hot pan, and a spoonful of cake "
                "batter poured into the same hot pan sets into solid sponge. "
                "Which of the two is the chemical change?",
        "options": [
            {"text": "The batter, because heat has turned the liquid mixture "
                     "into new substances that were not there in the raw "
                     "batter", "correct": True},
            {"text": "The butter, because it changes shape from a solid block "
                     "into a liquid pool, in exactly the dramatic way people "
                     "expect a real reaction to look on a hot pan",
             "correct": False,
             "why": "Melting is a change of state and stays physical. The "
                    "butter poured back out and cooled is still butter."},
            {"text": "Neither — both are simply reactions to the heat of the "
                     "pan",
             "correct": False,
             "why": "Reacting to heat is not the same as being a chemical "
                    "reaction. The butter's response to heat is entirely "
                    "physical."},
            {"text": "Both, because both change from liquid or soft to a "
                     "different texture",
             "correct": False,
             "why": "Texture changing on its own proves nothing. The butter's "
                    "new texture is still butter; the sponge's new texture is "
                    "new substances."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s29",
        "band": "standard",
        "text": "A strip of magnesium ribbon is held near a lit candle without "
                "touching the flame, and nothing happens to it. The same "
                "ribbon held directly in the flame catches fire and burns "
                "brightly. What does the comparison show?",
        "options": [
            {"text": "That magnesium reacts with heat alone, wherever it is in "
                     "a room with a flame",
             "correct": False,
             "why": "Being near a flame did nothing to the first ribbon. The "
                    "reaction needs the ribbon to actually reach the flame's "
                    "temperature and the oxygen at it."},
            {"text": "That the first ribbon must have been a different metal "
                     "from the second",
             "correct": False,
             "why": "There is no reason to think that. The same ribbon behaves "
                    "differently because only one of the two trials reaches "
                    "burning temperature."},
            {"text": "That being near heat is not enough — the reaction needs "
                     "the temperature and contact the flame itself supplies", "correct": True},
            {"text": "That magnesium can only burn once, so the first ribbon "
                     "had already used up its ability to react, the way a "
                     "spent match cannot be relit",
             "correct": False,
             "why": "Simply being near a flame uses nothing up. The first "
                    "ribbon is entirely unreacted magnesium, ready to burn "
                    "exactly like the second."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s30",
        "band": "standard",
        "text": "Two white powders look identical. One is table salt, which "
                "dissolves in water and can be recovered unchanged by "
                "evaporating it. The other is an indigestion tablet, which "
                "dissolves in water while fizzing and giving off a gas. Why is "
                "only one of these a chemical change?",
        "options": [
            {"text": "Because the salt is a pure substance and the tablet is a "
                     "mixture of ingredients, and only a mixture of several "
                     "ingredients reacting together can ever make something "
                     "new",
             "correct": False,
             "why": "Being a mixture of ingredients does not make something "
                    "react. What decides it is whether a new substance "
                    "appears, and the fizzing gas is exactly that."},
            {"text": "Because only the tablet makes a new substance — the gas "
                     "— that neither the powder nor the water contained before", "correct": True},
            {"text": "Because the tablet dissolves more slowly than the salt "
                     "does",
             "correct": False,
             "why": "Speed of dissolving is not the evidence here. The gas "
                    "given off is."},
            {"text": "Because salt cannot ever take part in a chemical "
                     "reaction",
             "correct": False,
             "why": "Salt certainly can react under the right conditions. This "
                    "particular dissolving is physical because nothing new is "
                    "made, not because salt never reacts at all."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s31",
        "band": "standard",
        "text": "A bronze sculpture kept indoors stays bright and shiny for "
                "decades, while an identical sculpture outdoors develops a "
                "green coating within a few years. What is the best "
                "explanation for the difference?",
        "options": [
            {"text": "The indoor sculpture is a different, more resistant kind "
                     "of bronze",
             "correct": False,
             "why": "There is no reason to assume that from the description. "
                    "The obvious difference between the two sculptures is "
                    "their surroundings, not their metal."},
            {"text": "The green coating is dust and dirt that has simply "
                     "settled on the outdoor sculpture over time, the same way "
                     "dust settles on a shelf indoors",
             "correct": False,
             "why": "Dust wipes off, and this coating does not. A green patina "
                    "is a new substance bonded to the surface of the bronze."},
            {"text": "Sculptures naturally turn green with age, whatever is "
                     "done with them",
             "correct": False,
             "why": "Age on its own explains nothing — the indoor sculpture is "
                    "the same age and has stayed bright. Exposure is what "
                    "makes the difference."},
            {"text": "The outdoor sculpture reacts with the air and rain it is "
                     "exposed to, and the indoor one is not exposed in the "
                     "same way", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-s32",
        "band": "standard",
        "text": "A candle burns steadily: melted wax drips down its side while "
                "the wick itself burns with a flame. Both are happening on the "
                "same candle at the same time. Which is which?",
        "options": [
            {"text": "The dripping is physical — it is still wax; the burning "
                     "wick is chemical — it makes new substances", "correct": True},
            {"text": "Both are chemical, because they are both part of one "
                     "candle burning",
             "correct": False,
             "why": "Being part of the same event does not make both halves "
                    "the same kind of change. The dripping wax is still wax; "
                    "the flame is making new substances."},
            {"text": "The dripping is chemical, because it is caused directly "
                     "by the flame next to it",
             "correct": False,
             "why": "Being caused by the flame's heat does not make melting "
                    "chemical. The dripped wax sets back into solid wax "
                    "exactly as it was."},
            {"text": "Both are physical, because a candle can burn for hours "
                     "without running out",
             "correct": False,
             "why": "How long a candle lasts says nothing about the kind of "
                    "change at the wick. New substances — carbon dioxide and "
                    "water vapour — are being made there the whole time."},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-01-h05",
        "band": "harder",
        "text": "The lesson calls boiling a potato MOSTLY physical, and "
                "browning a steak chemical. Why the hedge on the potato?",
        "options": [
            {"text": "Because some chemical change happens in it as well, and "
                     "the word describes the main one",
             "correct": True},
            {"text": "Because the potato is a mixture rather than one "
                     "substance, and the words physical and chemical can only "
                     "be applied to a pure substance in the first place",
             "correct": False,
             "why": "Both words apply perfectly well to mixtures. The hedge "
                    "is about there being more than one change at once"},
            {"text": "Because nobody has tested what happens inside a boiled "
                     "potato",
             "correct": False,
             "why": "It has been studied in detail. The hedge is an honest "
                    "description, not an admission of ignorance"},
            {"text": "Because water is involved, and water makes every change "
                     "partly physical",
             "correct": False,
             "why": "There is no such rule. Acid on marble involves water and "
                    "is wholly chemical"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h06",
        "band": "harder",
        "text": "Food is digested and the body absorbs what comes out of it. "
                "Chemical or physical, and on what evidence?",
        "options": [
            {"text": "Physical, because the food is only being broken into "
                     "smaller and smaller pieces until the bits are small "
                     "enough to pass through the gut wall",
             "correct": False,
             "why": "Chewing does that and is physical. Digestion goes "
                    "further and makes substances the food did not contain"},
            {"text": "Chemical, because substances are made that the food did "
                     "not contain",
             "correct": True},
            {"text": "Physical, because nothing is burnt",
             "correct": False,
             "why": "Burning is one chemical change among thousands. Not "
                    "burning proves nothing"},
            {"text": "Chemical, because it cannot be undone",
             "correct": False,
             "why": "Right verdict, wrong evidence. Reversibility is never "
                    "the test"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h07",
        "band": "harder",
        "text": "Photographic film darkens where light falls on it, at room "
                "temperature, with no heating at all. What does that show?",
        "options": [
            {"text": "That light is a substance, and that it must therefore "
                     "appear as one of the reactants in any equation written "
                     "for the darkening",
             "correct": False,
             "why": "Light is a condition rather than a substance. It goes "
                    "above the arrow, never in the line"},
            {"text": "That the change must be physical, since no heat was "
                     "supplied",
             "correct": False,
             "why": "A new substance is made, so it is chemical. Heat is not "
                    "what decides it"},
            {"text": "That heat is not needed for a chemical change",
             "correct": True},
            {"text": "That film is not made of ordinary substances",
             "correct": False,
             "why": "It is made of ordinary substances behaving ordinarily. "
                    "Light supplies the energy instead of heat"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h08",
        "band": "harder",
        "text": "Two reasons are offered for calling rusting chemical: that a "
                "hammer cannot undo it, and that the flakes do not behave like "
                "iron. Which is the better reason?",
        "options": [
            {"text": "The hammer one, because a change you cannot undo has "
                     "made something new",
             "correct": False,
             "why": "A smashed glass cannot be undone with a hammer either, "
                    "and no new substance was made"},
            {"text": "Both equally, since they lead to the same verdict",
             "correct": False,
             "why": "They do agree here and one of them would mislead you on "
                    "the next example. The reasoning has to be right too"},
            {"text": "Neither — only a chemical test settles it",
             "correct": False,
             "why": "Behaving differently IS the evidence, and noticing it "
                    "counts. No further test is needed"},
            {"text": "The flakes one, because new properties mean a new "
                     "substance",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h09",
        "band": "harder",
        "text": "The lesson says one pan can host both kinds of change in the "
                "same minute. Which pair is an example?",
        "options": [
            {"text": "Butter melting in the pan, and the meat in it browning",
             "correct": True},
            {"text": "Butter melting in the pan, and the melted butter "
                     "running down to the low side of it and pooling there "
                     "against the edge",
             "correct": False,
             "why": "Both halves are physical. Melting and flowing make "
                    "nothing new"},
            {"text": "Meat browning, and the smell of it filling the "
                     "kitchen",
             "correct": False,
             "why": "The smell is those new substances spreading through the "
                    "air, which is diffusion. Only one change here is "
                    "chemical"},
            {"text": "Water boiling, and steam condensing on the window",
             "correct": False,
             "why": "Both are changes of state, so both are physical"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h10",
        "band": "harder",
        "text": "Respiration is on the chemical list. Which substances does "
                "it make that were not there before?",
        "options": [
            {"text": "Oxygen and glucose, which is why breathing out feels "
                     "like getting rid of something the body has finished "
                     "with",
             "correct": False,
             "why": "Those are what respiration USES. The products are what "
                    "comes out of it"},
            {"text": "Carbon dioxide and water",
             "correct": True},
            {"text": "Heat, which is a new substance the body has made",
             "correct": False,
             "why": "Heat is given out and it is not a substance at all"},
            {"text": "None — respiration only moves substances about",
             "correct": False,
             "why": "Breathe onto cold glass and the water appears; breathe "
                    "into limewater and it goes cloudy. Both are new"},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h11",
        "band": "harder",
        "text": "Violence is often taken as a sign of a chemical change. Give "
                "a violent change that is physical.",
        "options": [
            {"text": "A firework going off in a fraction of a second",
             "correct": False,
             "why": "A firework is a chemical change — the smoke and the gas "
                    "are new substances"},
            {"text": "Petrol igniting in an engine",
             "correct": False,
             "why": "Burning is chemical. New substances leave the exhaust "
                    "pipe"},
            {"text": "A sealed can of water bursting as the water inside it "
                     "boils",
             "correct": True},
            {"text": "Sodium catching fire on water",
             "correct": False,
             "why": "Chemical, and violently so. New substances are made in "
                    "the beaker"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-01-h12",
        "band": "harder",
        "text": "An electric current is passed through water between two "
                "electrodes, and bubbles of gas collect at each one. Stirring "
                "the same water with a plastic rod, with no current, produces "
                "nothing at all. What does comparing the two show?",
        "options": [
            {"text": "That the current splits the water into new substances, "
                     "and stirring alone supplies no energy able to do that", "correct": True},
            {"text": "That electricity is a substance, and it becomes part of "
                     "the gas collected at each electrode",
             "correct": False,
             "why": "Electricity supplies energy to break the joins in water; "
                    "it does not become part of the gas. Hydrogen and oxygen "
                    "come from the water itself."},
            {"text": "That water always contains hidden gas, which the current "
                     "simply shakes loose",
             "correct": False,
             "why": "Water is one substance, not a mixture with gas hidden "
                    "inside it. The gases are made by the current breaking the "
                    "water apart."},
            {"text": "That plastic rods can never start a chemical change, "
                     "whatever current is applied through them",
             "correct": False,
             "why": "The rod is not the reason nothing happens. No current was "
                    "applied in the stirring trial, so there was no energy to "
                    "break any joins at all."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h13",
        "band": "harder",
        "text": "A self-heating drink can warms up because a real chemical "
                "reaction inside it gives out heat. A reusable hand warmer "
                "also warms up, but because a solid crystallises out of a "
                "liquid inside it. Told only that both packs get warm, how "
                "would you tell which is which?",
        "options": [
            {"text": "You could not — warming up always means the same kind of "
                     "change is happening inside",
             "correct": False,
             "why": "A physical change can warm its surroundings too, as the "
                    "crystallising pack does. Warmth alone cannot sort the "
                    "two."},
            {"text": "Try to reset each one by heating it: the crystallised "
                     "pack redissolves back to a liquid, and the chemical "
                     "can's contents do not turn back into what they started "
                     "as", "correct": True},
            {"text": "Check which pack is sold as reusable, since a chemical "
                     "change could never be built into a product meant to be "
                     "used more than once",
             "correct": False,
             "why": "That is a fact about how a product is marketed, not "
                    "about the chemistry inside a single use. A reusable "
                    "product could in principle be refilled with fresh "
                    "chemicals each time, even though these two happen not "
                    "to be."},
            {"text": 'Weigh both packs before and after, since only the '
                     'chemical one will have changed mass, because a reaction '
                     'turns some of its contents into heat',
             "correct": False,
             "why": "Neither pack changes mass — nothing enters or leaves "
                    "either sealed pack. Mass is conserved whichever kind of "
                    "change is inside."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h14",
        "band": "harder",
        "text": "An unknown change is reported with three facts: it gave off a "
                "gas, it warmed up, and the colour changed. A student says "
                "that is now enough facts together to prove it chemical. Are "
                "they right?",
        "options": [
            {"text": 'Yes — three clues together are much stronger evidence '
                     'than any one clue alone, since three separate things '
                     'would not all change at once unless a reaction were '
                     'running',
             "correct": False,
             "why": "Clues do not add up into proof, however many there are. A "
                    "fizzy drink opened gives off gas, and stirring solids "
                    "into water can warm the water and change its colour, and "
                    "neither is a reaction on its own."},
            {"text": "Yes, but only because a gas was one of the three facts "
                     "given",
             "correct": False,
             "why": "A gas given off is a strong clue and still only a clue — "
                    "a shaken fizzy drink gives one off and makes nothing new."},
            {"text": "No — none of the three is the test, and adding clues "
                     "together does not change that", "correct": True},
            {"text": 'No — the facts would need to include whether it can be '
                     'reversed as well, because an irreversible change is what '
                     'marks a reaction out',
             "correct": False,
             "why": "Adding a fourth clue does not fix the problem. No number "
                    "of clues proves it; only whether a new substance was made "
                    "does."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h15",
        "band": "harder",
        "text": "One kind of invisible ink is made of a chemical that stays "
                "colourless until it is heated, when it darkens and cannot be "
                "made invisible again. Another kind is simply diluted lemon "
                "juice, which shows the same way when heated, but the writing "
                "fades back to invisible after a while as it dries. Which uses "
                "a chemical change to reveal itself, and which does not?",
        "options": [
            {"text": 'Neither — both only ever show up because of the heat of '
                     'the iron or candle held near the paper, which is warming '
                     'the paper rather than changing either ink',
             "correct": False,
             "why": "Heat starts both, and what happens once it is supplied is "
                    "not the same in each case. One makes a lasting new "
                    "substance and one does not."},
            {"text": "Both — heating paper to reveal writing is always a "
                     "chemical reaction, whatever the ink",
             "correct": False,
             "why": "The lemon-juice writing fades back to invisible, which a "
                    "truly new substance would not do. Its darkening does not "
                    "last."},
            {"text": 'The lemon juice reveals itself chemically, because citric '
                     'acid is an acid, and an acid on paper always reacts with '
                     'it when heat is applied',
             "correct": False,
             "why": "Being natural or artificial decides nothing. What decides "
                    "it is whether the darkened writing stays a new substance, "
                    "and only one of the two inks does."},
            {"text": "The chemical ink reveals itself chemically, and the "
                     "lemon juice's fading shows it was never a lasting new "
                     "substance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h16",
        "band": "harder",
        "text": "Bread dough rises because yeast produces carbon dioxide "
                "bubbles. A sponge cake mixture rises because egg whites are "
                "whisked in, trapping air bubbles mechanically. Which of the "
                "two risings is the odd one out, and why?",
        "options": [
            {"text": "The bread, because carbon dioxide is a new substance "
                     "made by the yeast, while whisking only traps air that "
                     "was already there", "correct": True},
            {"text": "The bread, because yeast is a living thing rather than a "
                     "chemical ingredient",
             "correct": False,
             "why": "What the yeast is made of is beside the point. What "
                    "matters is that it makes a genuinely new gas, which "
                    "whisking never does."},
            {"text": 'The cake, because the air trapped in the whisked egg '
                     'white is a new substance that was not in the raw mixture '
                     'before',
             "correct": False,
             "why": "The air was already in the room and is simply beaten into "
                    "the mixture; nothing is made. The bread's carbon dioxide "
                    "did not exist before the yeast made it."},
            {"text": "Neither — both are physical, because both simply trap a "
                     "gas inside the mixture as it rises",
             "correct": False,
             "why": "The yeast's gas is made by a reaction, not trapped from "
                    "somewhere it already existed. Only the whisked air was "
                    "already there before mixing began."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h17",
        "band": "harder",
        "text": "Caramelising sugar in a pan and toasting a slice of bread are "
                "both called chemical changes because both go brown with heat. "
                "Does that mean the two are the same reaction happening to two "
                "different foods?",
        "options": [
            {"text": 'Yes — anything that browns with heat is undergoing '
                     'exactly the same reaction, because the brown colour '
                     'itself is the substance being made in each case',
             "correct": False,
             "why": "Browning is a family of related reactions between "
                    "different starting substances, not one single reaction. "
                    "Sugar alone and the starches and proteins in bread are "
                    "not the same substances to begin with."},
            {"text": "No — sharing the verdict \"chemical\" does not mean "
                     "sharing the same substances or the same new substances "
                     "made", "correct": True},
            {"text": "No, because only one of the two actually makes a new "
                     "substance",
             "correct": False,
             "why": "Both make new substances — new flavours, new smells and "
                    "new colours that neither the raw sugar nor the raw bread "
                    "had."},
            {"text": 'Yes, but only because both need a source of heat to get '
                     'started, and two changes needing the same trigger must be '
                     'the same change',
             "correct": False,
             "why": "Needing heat to start is true of both and is not what "
                    "makes them the same reaction. Different starting "
                    "substances make different products either way."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h18",
        "band": "harder",
        "text": "Two clear liquids are mixed and the beaker instantly turns "
                "cloudy white. A student says cloudiness always means a new "
                "substance has been made. Is that reliable?",
        "options": [
            {"text": 'Yes — a liquid cannot turn cloudy unless something new '
                     'has formed inside it, since a clear liquid has nothing in '
                     'it that could scatter light until a new solid appears',
             "correct": False,
             "why": "Oil shaken into water turns the mixture cloudy white, and "
                    "nothing new is made — it is tiny droplets of oil "
                    "scattered through the water, still oil and still water."},
            {"text": 'Yes, but only when both liquids started out completely '
                     'clear, since anything cloudy at the start could have been '
                     'carrying the cloudiness all along',
             "correct": False,
             "why": "Starting clear tells you nothing about the cloudiness "
                    "that follows. Oil and water are both clear before shaking "
                    "and cloudy after, with nothing new made."},
            {"text": "No — cloudiness can come from tiny droplets of an "
                     "unreacted substance spread through the liquid, as well "
                     "as from a new solid forming", "correct": True},
            {"text": "No — cloudiness is never any kind of evidence at all",
             "correct": False,
             "why": "It genuinely is evidence when an insoluble new solid "
                    "forms in a reaction. It is simply not reliable on its "
                    "own, without knowing what caused it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h19",
        "band": "harder",
        "text": "A dry-cleaning solvent lifts a grease stain out of a jacket "
                "by dissolving the grease. A bleach solution removes a "
                "fruit-juice stain from a shirt by breaking down the coloured "
                "molecule in the juice. Which of the two is the chemical "
                "change?",
        "options": [
            {"text": "The dry cleaning, because the solvent smells strongly of "
                     "chemicals",
             "correct": False,
             "why": "Smell is not the test. The solvent dissolves the grease "
                    "without changing it — the grease could be recovered from "
                    "the solvent unchanged."},
            {"text": 'Both, because both remove a stain that will not simply '
                     'wash out with water, and a stain that resists water has '
                     'to be broken apart rather than lifted',
             "correct": False,
             "why": "Being stubborn to remove is not the test. The grease is "
                    "unchanged by the solvent; the dye is genuinely changed by "
                    "the bleach."},
            {"text": 'Neither, because stain removal is always a physical '
                     'process by definition, since the stain is carried away '
                     'rather than turned into anything else',
             "correct": False,
             "why": "That is true of dissolving a stain and not of destroying "
                    "one. The bleach makes new, colourless substances out of "
                    "the dye."},
            {"text": "The bleaching, because the coloured molecule is broken "
                     "down into different, colourless substances", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h20",
        "band": "harder",
        "text": "A rechargeable battery is drained flat by a torch, then "
                "plugged into a charger and returned almost to full. Real "
                "chemical reactions run inside it both times, forwards to "
                "discharge it and backwards to charge it. Does being "
                "reversible like this make the battery's changes physical?",
        "options": [
            {"text": "No — the substances inside are genuinely different when "
                     "charged and when flat, and being reversible does not "
                     "change that", "correct": True},
            {"text": "Yes — anything that can be run backwards with the right "
                     "equipment counts as physical",
             "correct": False,
             "why": "Reversibility is a fact about energy and equipment, never "
                    "the test. The battery's substances are genuinely "
                    "different when flat from when full."},
            {"text": "Yes, because the charger puts exactly the same energy "
                     "back in that the torch took out",
             "correct": False,
             "why": "Even a change that could be reversed exactly is still "
                    "chemical if new substances are being made and unmade. "
                    "Energy balancing is not the test."},
            {"text": "No, because a battery can only be recharged a limited "
                     "number of times before it wears out",
             "correct": False,
             "why": "Wearing out eventually is a separate, real fact about "
                    "batteries and is not the reason the change is chemical. "
                    "It is chemical because the substances inside genuinely "
                    "change."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h21",
        "band": "harder",
        "text": "Two identical iron gateposts stand side by side outdoors. One "
                "is coated in a protective wax and stays bright for years; the "
                "other, left bare, rusts within months. Has the wax stopped "
                "the iron undergoing a chemical change, or stopped it being "
                "one kind of change rather than another?",
        "options": [
            {"text": "It has turned what would be a chemical change into a "
                     "physical one",
             "correct": False,
             "why": "The wax has not changed what KIND of change rusting would "
                    "be. It has kept the air and water that cause it away from "
                    "the iron altogether."},
            {"text": "It has stopped the reaction from starting at all, by "
                     "keeping the iron out of contact with the air and water "
                     "it needs", "correct": True},
            {"text": 'It has made the rusting reversible, so that removing the '
                     'wax would let the gatepost rust back to bright iron, '
                     'because the wax has held the rusting halfway through',
             "correct": False,
             "why": "Removing the wax only exposes the iron to the air again — "
                    "it does not undo any rusting, because none has happened "
                    "underneath it."},
            {"text": 'It has slowed the rusting down without changing anything '
                     'else about it, the way cold slows down a reaction, since '
                     'air and water still seep through a wax layer given long '
                     'enough',
             "correct": False,
             "why": "This is more than slower rusting — the coated post has "
                    "effectively no reaction happening on its surface at all, "
                    "because the reactants cannot reach the iron."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h22",
        "band": "harder",
        "text": "One batch of bread dough is put straight into a hot oven and "
                "bakes into a loaf. An identical batch is frozen solid "
                "instead. Which of these two things happening to the dough is "
                "the chemical change?",
        "options": [
            {"text": "Freezing, because turning a soft dough into a hard block "
                     "is a dramatic change",
             "correct": False,
             "why": "Freezing is a change of state — the same dough, just "
                    "colder and solid. Thaw it and it is soft dough again."},
            {"text": "Both, because both change how the dough behaves when you "
                     "press it",
             "correct": False,
             "why": "Changing how something feels is not the test. The frozen "
                    "dough is unreacted dough throughout; the baked loaf "
                    "contains new substances the raw dough did not."},
            {"text": "Baking, because heat sets the structure and browns the "
                     "crust into new substances", "correct": True},
            {"text": 'Neither, because dough is a mixture and mixtures cannot '
                     'undergo chemical changes, since the ingredients are only '
                     'stirred together and never joined',
             "correct": False,
             "why": "Mixtures react all the time — the yeast, flour and water "
                    "in this one certainly do once the oven's heat gets to "
                    "work on them."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h23",
        "band": "harder",
        "text": "A tarnished silver spoon is treated two ways: rubbing it hard "
                "with a dry cloth makes it look a little brighter, while "
                "dipping it in a silver-cleaning solution makes the dark "
                "coating disappear completely. Which treatment reverses a "
                "chemical change, and which does not?",
        "options": [
            {"text": "Rubbing reverses it, because the dark coating is being "
                     "physically removed from the surface either way",
             "correct": False,
             "why": "Rubbing only smooths and thins the dark layer; the "
                    "tarnish compound is still there, not turned back into "
                    "silver."},
            {"text": 'Neither reverses it, because tarnish can never be removed '
                     'once it has formed, and both treatments only polish the '
                     'surface above it',
             "correct": False,
             "why": "The solution genuinely removes it — the spoon comes out "
                    "looking like the untarnished metal, not merely brighter."},
            {"text": "Both reverse it equally well, since both leave the spoon "
                     "looking shinier than before",
             "correct": False,
             "why": "Looking shinier is not the same as the tarnish being "
                    "gone. Rubbing leaves a thinner layer of the same dark "
                    "compound behind."},
            {"text": "The solution reverses it, because it turns the silver "
                     "sulfide back into silver metal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h24",
        "band": "harder",
        "text": "Two identical-looking white crystals are heated on separate "
                "spoons. One turns brown, smells of caramel and will not set "
                "back to a clear solid on cooling. The other melts to a clear "
                "liquid that sets back to an identical white solid once it "
                "cools. Which is the sugar and which is the citric acid, and "
                "how do you know?",
        "options": [
            {"text": "The browning one is the sugar, because it has been "
                     "turned into new substances that cannot set back to the "
                     "original crystal", "correct": True},
            {"text": "The browning one is the citric acid, because acids "
                     "always react when heated",
             "correct": False,
             "why": "Plenty of acids simply melt on heating, as this one does. "
                    "Reacting on heating is not automatic for every acid."},
            {"text": "Neither can be identified from this evidence — melting "
                     "and browning look too similar to tell apart",
             "correct": False,
             "why": "They do not behave alike at all here — one sets back to a "
                    "solid unchanged and one does not, which is exactly the "
                    "evidence needed."},
            {"text": "The one that melts cleanly must be the sugar, because "
                     "sugar is well known for melting easily in cooking",
             "correct": False,
             "why": "Sugar in this description does the opposite — it is the "
                    "one that browns and changes. The clean, reversible melt "
                    "belongs to the citric acid."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h25",
        "band": "harder",
        "text": "A recycling plant crushes glass bottles, melts the crushed "
                "glass, and moulds it into new bottles. Has the plant made a "
                "new substance out of the old glass?",
        "options": [
            {"text": "Yes — new bottles are a new product that did not exist "
                     "before",
             "correct": False,
             "why": "A new shape is not a new substance. The glass in the new "
                    "bottles is chemically identical to the glass in the old "
                    "ones."},
            {"text": "No — crushing and melting glass rearranges its shape and "
                     "state, but it is still the same glass throughout", "correct": True},
            {"text": 'Yes, because melting glass requires such a high '
                     'temperature that it must be reacting, since nothing '
                     'survives that much heat without being changed into '
                     'something else',
             "correct": False,
             "why": "High temperature melts glass without changing what it is "
                    "made of. Needing a lot of heat is not evidence of a "
                    "reaction on its own."},
            {"text": "No, because glass can never take part in any chemical "
                     "change whatsoever",
             "correct": False,
             "why": "Glass reacts under the right conditions, with strong "
                    "acids for example. This process simply is not one of "
                    "those — it is melting and moulding."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h26",
        "band": "harder",
        "text": 'A crystal-growing kit dissolves a compound in hot water. Small '
                'bubbles rise as the hot water is poured, and the solution is '
                'then left to cool and grow crystals. Are the bubbling and the '
                'crystal growth the same kind of change?',
        "options": [
            {"text": 'No — the bubbles are a gas being made, and a gas being '
                     'made is always evidence that a reaction has run',
             "correct": False,
             "why": 'Hot water holds less dissolved air than cold, so pouring '
                    'it drives air out that was already there. Nothing new is '
                    'made.'},
            {"text": 'No — the crystals are a new substance, made out of the '
                     'solution as it cools',
             "correct": False,
             "why": 'The crystals are the very compound that was tipped in, '
                    'coming back out of solution unchanged. Evaporate the water '
                    'instead and the same compound is left.'},
            {"text": 'Yes — the bubbles are dissolved air driven out of the hot '
                     'water, and the crystals are the same compound coming back '
                     'out of solution, so neither makes anything new', "correct": True},
            {"text": 'Yes, but only because both happen in the same beaker on '
                     'the same afternoon',
             "correct": False,
             "why": 'The verdict is right and the reason is not. Sharing a '
                    'beaker settles nothing; what settles it is that neither '
                    'step makes a new substance.'},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h27",
        "band": "harder",
        "text": "Tempering chocolate is a careful process of melting it and "
                "cooling it again through specific temperatures, which changes "
                "how its cocoa butter is arranged and gives the chocolate a "
                "glossy snap. No new substance is made at any point. Is "
                "tempering a chemical change, given how technical and precise "
                "it sounds?",
        "options": [
            {"text": "Yes — a process this precise and technical has to be a "
                     "chemical reaction",
             "correct": False,
             "why": "How careful or technical a process is says nothing about "
                    "its kind. Tempering is precise because of how fussy cocoa "
                    "butter's physical structure is, not because a reaction is "
                    "involved."},
            {"text": 'Yes, because the glossy snap the chocolate gains is a new '
                     'property it did not have before, and a new property can '
                     'only belong to a new substance',
             "correct": False,
             "why": "A new PROPERTY without a new SUBSTANCE is exactly what a "
                    "physical change can produce — the cocoa butter has simply "
                    "settled into a different, more stable arrangement."},
            {"text": "No, but only because it involves cooling rather than "
                     "heating overall",
             "correct": False,
             "why": "Whether the net effect is heating or cooling is not the "
                    "test. It is physical because no new substance is made at "
                    "either stage."},
            {"text": "No — it is physical throughout, because the chocolate is "
                     "the same substance before and after, just rearranged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h28",
        "band": "harder",
        "text": "A firefighter sprays water onto a burning log. The fire goes "
                "out, steam rises from the wet, blackened wood, and the fire "
                "stops making any more smoke. Which parts of this whole event "
                "were chemical, and which were physical?",
        "options": [
            {"text": "The burning was chemical; the water turning to steam was "
                     "physical", "correct": True},
            {"text": "All of it was chemical, because it all happened as part "
                     "of putting out one fire",
             "correct": False,
             "why": "Being part of one event does not make every part of it "
                    "the same kind of change. The water simply turning to "
                    "steam is a change of state."},
            {"text": "All of it was physical, because water was what stopped "
                     "the fire",
             "correct": False,
             "why": "The burning that happened before the water arrived was "
                    "chemical — new substances, smoke and ash, had already "
                    "been made."},
            {"text": "The steam was chemical, because it was made suddenly and "
                     "violently by the heat of the fire",
             "correct": False,
             "why": "However suddenly it appears, steam is still water, just "
                    "as a gas instead of a liquid. No new substance has been "
                    "made."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h29",
        "band": "harder",
        "text": "A tin of quicklime is left open in a humid room. Over several "
                "days it slowly warms very slightly and turns from hard lumps "
                "into a soft, crumbly powder. A student says the warming on "
                "its own would have been enough to prove this chemical. Are "
                "they right?",
        "options": [
            {"text": "Yes — anything that warms up on its own, with no flame "
                     "nearby, must be reacting, since it is the plainest "
                     "possible explanation and the one most people would reach "
                     "for first",
             "correct": False,
             "why": "A physical change can warm up on its own too — "
                    "crystallising salt out of a hot solution does. Warming "
                    "alone is never enough."},
            {"text": "No — the warming alone would not have been enough, "
                     "though the combination with a genuinely new substance "
                     "forming is what actually settles it", "correct": True},
            {"text": 'Yes, because the powder is definitely a new substance and '
                     'warming always goes with a new substance forming, since '
                     'the heat has to come from the joins being made',
             "correct": False,
             "why": "The powder being new is the real evidence — but that does "
                    "not mean warming and new substances always go together. "
                    "Some reactions cool down instead."},
            {"text": "No, because quicklime cannot react without a flame to "
                     "start it",
             "correct": False,
             "why": "This reaction runs at room temperature with nothing lit "
                    "near it. Not every reaction needs a flame to begin."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h30",
        "band": "harder",
        "text": "A student claims that any change giving off a strong smell "
                "must be chemical, because a smell means new molecules are "
                "spreading through the air. Evaluate the claim using perfume "
                "left open on a shelf, which smells strong for hours and then "
                "fades away completely.",
        "options": [
            {"text": 'The claim holds for perfume too — the smell proves new '
                     'molecules have been made in the bottle, because a liquid '
                     'that sits still cannot reach the nose unless something '
                     'new leaves it',
             "correct": False,
             "why": "The perfume simply evaporates into the air as the very "
                    "same molecules it always was. Nothing new is made by it "
                    "drying out."},
            {"text": "The claim only fails once the smell has completely faded "
                     "away",
             "correct": False,
             "why": "It fails from the very start, the moment the bottle is "
                    "opened — the smell is real and the change is physical "
                    "throughout, not only once it ends."},
            {"text": "The claim is wrong — perfume smells strongly while "
                     "evaporating, which is physical, so smell alone does not "
                     "prove a reaction", "correct": True},
            {"text": "The claim is right, because burning toast also smells "
                     "strongly and is chemical",
             "correct": False,
             "why": "Burning toast being chemical does not make smell the test "
                    "— it only shows that a chemical change CAN smell "
                    "strongly, not that only chemical changes do."},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h31",
        "band": "harder",
        "text": "A jeweller tests a ring by placing a drop of strong acid on "
                "it: gold shows no reaction at all, while a cheap look-alike "
                "metal fizzes and dissolves. Is the gold ring's lack of any "
                "visible change itself useful evidence?",
        "options": [
            {"text": "No — only a change that actually happens can ever be "
                     "evidence of anything",
             "correct": False,
             "why": "The absence of a reaction is real evidence here — it is "
                    "exactly what tells the jeweller the ring is genuine gold "
                    "rather than a reactive look-alike."},
            {"text": 'No, because the acid must be too weak to react with '
                     'either metal in this test, and the fizzing on the '
                     'look-alike is only the drop spreading out',
             "correct": False,
             "why": "The acid is clearly strong enough — it dissolves the "
                    "look-alike straight away. It is simply that gold does not "
                    "react with it."},
            {"text": 'Yes, but only because the fizzing look-alike proves every '
                     'metal fizzes in acid, gold included, given long enough',
             "correct": False,
             "why": "The two metals are being contrasted precisely because "
                    "they behave differently. Gold not fizzing is the whole "
                    "point of the test."},
            {"text": "Yes — gold staying unreacted is itself the evidence that "
                     "confirms what the metal is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-01-h32",
        "band": "harder",
        "text": "Dry ice sitting on a bench gives off a dense white fog that "
                "rolls along the floor. Burning magnesium ribbon also gives "
                "off a bright white smoke that drifts through the air. Both "
                "look like clouds of \"smoke\". What is actually happening in "
                "each case?",
        "options": [
            {"text": "The dry ice fog is condensed water vapour, and the "
                     "magnesium smoke is a new substance made as the metal "
                     "burns", "correct": True},
            {"text": "Both are the same — solid particles of the original "
                     "substance floating in the air",
             "correct": False,
             "why": "The magnesium smoke is genuinely new — tiny particles of "
                    "magnesium oxide. The dry ice fog is not carbon dioxide at "
                    "all; it is ordinary water vapour condensing in the cold "
                    "air."},
            {"text": "The magnesium smoke is condensed water vapour too, "
                     "cooled by the heat of the reaction",
             "correct": False,
             "why": "Burning releases heat rather than cold, so nothing is "
                    "condensing near the flame. The white smoke is solid "
                    "magnesium oxide, made directly by the reaction."},
            {"text": 'Neither is really smoke, because true smoke can only come '
                     'from something organic burning, like wood or paper, and '
                     'neither dry ice nor a metal is organic',
             "correct": False,
             "why": "Whether something counts as \"smoke\" in everyday speech "
                    "is not the question here. What matters is that one cloud "
                    "is a new substance and the other is not."},
        ],
        "figure": None,
    },
]
