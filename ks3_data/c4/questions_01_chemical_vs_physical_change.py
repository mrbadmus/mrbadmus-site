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
             "why": "Nothing new was made. The solution still tastes of salt "
                    "because the salt is still salt, spread out among the "
                    "water."},
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
        "band": "s",
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
        "band": "s",
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
        "band": "s",
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
        "band": "s",
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
        "band": "h",
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
        "band": "h",
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
        "band": "h",
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
        "band": "h",
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
]
