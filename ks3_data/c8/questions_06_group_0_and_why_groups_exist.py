"""C8 lesson 06 — Group 0 and why groups exist: twelve questions (MRB-281).

The lesson's argument is one shape: the group number is the number of outer
electrons, and that single fact is why every group has the family resemblance
it does — including the group whose resemblance is that it does nothing. The
page teaches it with a four-row shell strip, four unknown elements to place,
and three real uses of a gas chosen BECAUSE it will not react.

These twelve probe the angles the mastery ladder leaves alone: why being a gas
is not the reason, what a full shell forbids, and what unreactive is worth.

The distractors are built from the lesson's two declared misconceptions.

`PTAB-09` (the noble gases are unreactive because they are gases) drives the
wrong options in e01, s01, s03 and h01. Each treats state of matter as a cause.
s03 is the one that matters: it puts fluorine and helium side by side, two
gases with opposite behaviour, so the belief has to explain the difference and
cannot.

`PTAB-10` (unreactive means useless) drives e03, s02, h02 and h04, where doing
nothing is read as being worth nothing. h04 is the register's own case put as
a purchasing decision, which is where a student actually meets it.

A third strand, on the page and in neither register entry, is that a rule can
survive a footnote: e04 and h03 are built on Bartlett's xenon compounds, which
qualify "reacts with nothing" without overturning it (MRB-225).

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "group-0-and-why-groups-exist"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-06-e01",
        "band": "easier",
        # ⚑ Asks about HELIUM'S EXCEPTION rather than about group 0 in
        # general — the recall rung already asks why the group is unreactive,
        # and check 6 is right that a bank restating a rung adds no depth.
        # This also puts flag 9's authored exception in front of the student.
        "text": "Helium is in group 0 but has only two outer electrons, not "
                "eight. Why is it still unreactive?",
        "options": [
            {"text": "Because two electrons completely fill the only shell "
                     "helium has",
             "correct": True},
            {"text": "Because two is too few electrons for any reaction to "
                     "use",
             "correct": False,
             "why": "Hydrogen has one and is ferociously reactive. The number "
                    "matters only against the space available."},
            {"text": "Because helium is so light that it escapes before it "
                     "can react",
             "correct": False,
             "why": "Helium in a sealed jar stays put and still reacts with "
                    "nothing."},
            {"text": "Because helium is really in group 2, where the metals "
                     "are",
             "correct": False,
             "why": "Helium sits at the right-hand end of period 1, in "
                    "group 0. It is not a metal at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e02",
        "band": "easier",
        # ⚑ Runs the group/atomic-number distinction the OTHER WAY — the
        # apply rung asks what the group number means, so this one gives the
        # group and asks for the total. Check 6 is right that a bank
        # restating a rung adds no depth.
        "text": "Chlorine is in group 7 and each atom has 17 electrons "
                "altogether. What is chlorine's atomic number?",
        "options": [
            {"text": "7, because that is the group it is in",
             "correct": False,
             "why": "7 is the outer-shell count. The atomic number counts "
                    "every electron, and every proton."},
            {"text": "17, the total number of electrons in the atom",
             "correct": True},
            {"text": "3, because chlorine has three shells of electrons",
             "correct": False,
             "why": "Three is the period number, read down the side of the "
                    "table."},
            {"text": "24, adding the group number to the total",
             "correct": False,
             "why": "The two numbers are not added. One of them is part of "
                    "the other."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e03",
        "band": "easier",
        "text": "Why is a filament light bulb filled with argon rather than "
                "with air?",
        "options": [
            {"text": "Because argon conducts electricity better than air does",
             "correct": False,
             "why": "The current goes through the filament, not the gas. "
                    "Argon is doing a different job."},
            {"text": "Because argon makes the light look brighter and whiter",
             "correct": False,
             "why": "The gas contributes no light at all. The filament does "
                    "all of it."},
            {"text": "Because argon will not react with the white-hot "
                     "filament",
             "correct": True},
            {"text": "Because argon is cheaper than the air used to be",
             "correct": False,
             "why": "Argon has to be separated from air, so it costs more. "
                    "It is bought for what it does not do."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e04",
        "band": "easier",
        "text": "In 1962 xenon was made to form a compound. What did that do "
                "to the rule that noble gases react with nothing?",
        "options": [
            {"text": "It overturned the rule, so the noble gases are ordinary "
                     "elements",
             "correct": False,
             "why": "Nothing has ever been made from helium or neon, and "
                    "xenon needed extreme conditions."},
            {"text": "It proved the rule had never been based on any evidence",
             "correct": False,
             "why": "The rule rested on decades of failed attempts, which is "
                    "real evidence."},
            {"text": "It showed the whole periodic table needed to be redrawn",
             "correct": False,
             "why": "Group 0 stayed exactly where it was. The table absorbed "
                    "the result without changing shape."},
            {"text": "It added a footnote: the rule holds, with a known "
                     "exception",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-06-s01",
        "band": "standard",
        "text": "Argon makes up nearly one per cent of the air, yet it was "
                "not discovered until 1894. Why was it missed for so long?",
        "options": [
            {"text": "Because it forms no compounds, so it left no trace in "
                     "any analysis",
             "correct": True},
            {"text": "Because it had not yet entered the atmosphere in 1869",
             "correct": False,
             "why": "It had been there throughout human history, going in and "
                    "out of every pair of lungs."},
            {"text": "Because it is colourless, and every colourless gas was "
                     "missed",
             "correct": False,
             "why": "Nitrogen and oxygen are colourless and both were found "
                    "long before."},
            {"text": "Because instruments of the time could not weigh a gas "
                     "at all",
             "correct": False,
             "why": "Weighing gases is exactly how argon was eventually "
                    "caught."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s02",
        "band": "standard",
        "text": "Hydrogen is lighter and cheaper than helium. Why are weather "
                "balloons filled with helium?",
        "options": [
            {"text": "Because helium gives noticeably more lift than hydrogen "
                     "does",
             "correct": False,
             "why": "Hydrogen gives slightly MORE lift. Helium is chosen "
                    "despite that, not because of it."},
            {"text": "Because helium will not burn and hydrogen will",
             "correct": True},
            {"text": "Because hydrogen escapes through the fabric far too "
                     "quickly",
             "correct": False,
             "why": "Both leak. Leakage is a nuisance; burning is a "
                    "catastrophe."},
            {"text": "Because helium is easier to make than hydrogen is",
             "correct": False,
             "why": "Hydrogen can be made from water anywhere. Helium has to "
                    "be mined."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s03",
        "band": "standard",
        "text": "Fluorine and helium are both gases at room temperature, but "
                "one is the most reactive element in the table and the other "
                "reacts with almost nothing. What does that show?",
        "options": [
            {"text": "That fluorine must actually be a liquid under "
                     "laboratory conditions",
             "correct": False,
             "why": "Fluorine is genuinely a gas. The premise is right; it is "
                    "the inference from it that fails."},
            {"text": "That reactivity cannot be predicted from the periodic "
                     "table at all",
             "correct": False,
             "why": "It is predicted very well — from the GROUP, which is the "
                    "whole point of the lesson."},
            {"text": "That being a gas has no bearing on whether an element "
                     "reacts",
             "correct": True},
            {"text": "That helium's atoms are much larger and so collide less "
                     "often",
             "correct": False,
             "why": "Helium's atoms are the smallest of any element after "
                    "hydrogen."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s04",
        "band": "standard",
        "text": "An unknown element is in group 0, period 4. What will it "
                "react with?",
        "options": [
            {"text": "Water, because period 4 elements are reactive with "
                     "water",
             "correct": False,
             "why": "Period says how many shells, not what the element does. "
                    "Group 0 settles this one."},
            {"text": "Oxygen, because almost every element burns in air",
             "correct": False,
             "why": "The noble gases are exactly the elements that do not."},
            {"text": "Only the elements directly above and below it in the "
                     "group",
             "correct": False,
             "why": "Elements in a group do not react with each other as a "
                    "rule, and these react with nothing."},
            {"text": "Essentially nothing, because its outer shell is full",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-06-h01",
        "band": "harder",
        "text": "The lesson says the noble gases are gases BECAUSE they are "
                "unreactive, rather than the other way round. What does that "
                "mean?",
        "options": [
            {"text": "That their atoms attract each other so weakly that "
                     "nothing holds them together",
             "correct": True},
            {"text": "That they were named as gases before anyone tested "
                     "their reactions",
             "correct": False,
             "why": "This is about physics, not naming. The order of "
                    "discovery is irrelevant."},
            {"text": "That they turn into solids as soon as they react with "
                     "anything",
             "correct": False,
             "why": "They do not react, so there is nothing for them to turn "
                    "into."},
            {"text": "That a gas is any substance with a full outer shell of "
                     "electrons",
             "correct": False,
             "why": "Oxygen and nitrogen are gases and neither has a full "
                    "outer shell."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h02",
        "band": "harder",
        "text": "A neon sign glows for decades without the neon being used "
                "up. Why not?",
        "options": [
            {"text": "Because neon reacts so slowly that decades are needed "
                     "to see it",
             "correct": False,
             "why": "It is not reacting slowly. It is not reacting."},
            {"text": "Because the electrons excite the atoms and no reaction "
                     "occurs at all",
             "correct": True},
            {"text": "Because the neon is replaced automatically from a small "
                     "reservoir",
             "correct": False,
             "why": "A neon tube is sealed. Nothing is added to it after it "
                    "is made."},
            {"text": "Because the glass supplies new neon as the old is "
                     "consumed",
             "correct": False,
             "why": "Glass supplies nothing. If it did, the tube would be "
                    "reacting with its own container."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h03",
        "band": "harder",
        "text": "Why was xenon, rather than helium, the noble gas that could "
                "be made to form a compound?",
        "options": [
            {"text": "Because xenon is a solid and helium is a gas",
             "correct": False,
             "why": "Xenon is a gas at room temperature too."},
            {"text": "Because helium had never been tested by anyone before "
                     "1962",
             "correct": False,
             "why": "Helium had been tested repeatedly and had refused "
                    "every time."},
            {"text": "Because xenon's outer electrons are furthest out and "
                     "held least tightly",
             "correct": True},
            {"text": "Because xenon has an incomplete outer shell, unlike the "
                     "others",
             "correct": False,
             "why": "Xenon's outer shell is full like the rest. Its size is "
                    "what makes the difference."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h04",
        "band": "harder",
        "text": "A welding company pays more for argon than it would for "
                "compressed air. What are they buying?",
        "options": [
            {"text": "A gas that burns cleanly and adds heat to the weld",
             "correct": False,
             "why": "Argon does not burn at all. A gas that burned would "
                    "ruin the weld."},
            {"text": "A gas that conducts the welding current to the metal",
             "correct": False,
             "why": "The current runs through the electrode and the "
                    "workpiece, not through the shielding gas."},
            {"text": "A gas that dissolves into the metal and strengthens it",
             "correct": False,
             "why": "Nothing dissolves in. The argon leaves the way it "
                    "arrived."},
            {"text": "A gas that will not react with hot metal, keeping "
                     "oxygen away",
             "correct": True},
        ],
        "figure": None,
    },
]
