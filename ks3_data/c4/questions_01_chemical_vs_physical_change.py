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
        "text": "The comparison table lists where you meet each kind of "
                "change. Which list is the CHEMICAL one?",
        "options": [
            {"text": "Burning, rusting, cooking, acid on marble, respiration",
             "correct": True},
            {"text": "Melting, boiling, dissolving, breaking, mixing",
             "correct": False,
             "why": "Every one of those leaves the same substances behind. "
                    "That is the physical list"},
            {"text": "Heating, cooling, stirring, pouring, weighing",
             "correct": False,
             "why": "Those are things you DO. Some of them start a reaction "
                    "and none of them is one"},
            {"text": "Anything that gives off a gas, changes colour, or gets "
                     "warm",
             "correct": False,
             "why": "All three of those clues appear on both sides of the "
                    "line, which is why none of them is the test"},
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
]
