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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-06-e05",
        "band": "easier",
        "text": "What does inert mean?",
        "options": [
            {"text": "Unable to move, which is why an inert gas settles to "
                     "the bottom of a container instead of mixing with the "
                     "air above it",
             "correct": False,
             "why": "Its particles move like any gas, and it mixes freely. "
                    "Inert is about chemistry, not motion"},
            {"text": "Unreactive — especially of a gas put somewhere to keep "
                     "air out",
             "correct": True},
            {"text": "Colourless and invisible",
             "correct": False,
             "why": "Chlorine is coloured and reactive; nitrogen is "
                    "colourless and fairly unreactive. Appearance is not the "
                    "word"},
            {"text": "Poisonous",
             "correct": False,
             "why": "Almost the opposite. An inert gas takes part in nothing, "
                    "including in you"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e06",
        "band": "easier",
        "text": "How many electrons are in a full outer shell, for most "
                "atoms?",
        "options": [
            {"text": "Two, which is how many helium has and helium is the "
                     "example the whole of group 0 is named after",
             "correct": False,
             "why": "Two is right for helium, which has only one shell. For "
                    "the rest it is eight"},
            {"text": "Seven",
             "correct": False,
             "why": "Seven is one short, which is group 7 — the most reactive "
                    "non-metals there are"},
            {"text": "Eight",
             "correct": True},
            {"text": "It depends on the element, and there is no usual "
                     "number",
             "correct": False,
             "why": "Eight is the usual number, with helium the one exception "
                    "you meet"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e07",
        "band": "easier",
        "text": "Which of these is a noble gas?",
        "options": [
            {"text": "Nitrogen, which makes up most of the air and takes part "
                     "in almost nothing that happens in a laboratory",
             "correct": False,
             "why": "Fairly unreactive and not a noble gas. Nitrogen is group "
                    "5 and its outer shell is not full"},
            {"text": "Hydrogen",
             "correct": False,
             "why": "Hydrogen burns explosively. It is nowhere near group 0"},
            {"text": "Chlorine",
             "correct": False,
             "why": "Group 7, and one of the most reactive elements in the "
                    "table"},
            {"text": "Neon",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-06-s05",
        "band": "standard",
        "text": "A neon sign glows because its electrons are EXCITED. Why is "
                "that not a chemical reaction?",
        "options": [
            {"text": "Because a reaction has to involve two substances, and "
                     "there is only neon inside the tube for anything to "
                     "happen to",
             "correct": False,
             "why": "One substance can decompose all by itself. What rules "
                    "this out is that nothing is joined or separated"},
            {"text": "Because nothing joins or separates — the electrons "
                     "return, and the neon is unchanged",
             "correct": True},
            {"text": "Because no heat is given out",
             "correct": False,
             "why": "The tube does warm up a little, and plenty of reactions "
                    "give out no heat worth noticing"},
            {"text": "Because neon cannot react at all under any "
                     "circumstances",
             "correct": False,
             "why": "True of neon so far, and it is not the reason. Even a "
                    "reactive gas would only be glowing here"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s06",
        "band": "standard",
        "text": "Argon is used to keep air away from hot metal while it is "
                "welded. What is the welder buying?",
        "options": [
            {"text": "A gas cold enough to take heat out of the weld as it "
                     "forms, so that the metal cools evenly and does not "
                     "crack afterwards",
             "correct": False,
             "why": "Argon arrives at room temperature like any bottled gas. "
                    "What it does is exclude oxygen"},
            {"text": "A gas that burns and adds heat to the weld",
             "correct": False,
             "why": "Argon burns in nothing. A fuel gas is a different bottle "
                    "for a different job"},
            {"text": "A gas that will not react with the hot metal, so oxygen "
                     "is kept off it",
             "correct": True},
            {"text": "A gas heavy enough to hold the metal down",
             "correct": False,
             "why": "It is denser than air, which helps it stay over the "
                    "weld — and it holds nothing down"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s07",
        "band": "standard",
        "text": "Chlorine has 17 electrons altogether and 7 in its outer "
                "shell. How many more would fill that shell, and what does "
                "that predict?",
        "options": [
            {"text": "Ten more, since 17 and 10 make a whole number of "
                     "shells and that is what filling one means",
             "correct": False,
             "why": "The outer shell holds eight, and seven are in it. One "
                    "more completes it"},
            {"text": "One more, and it predicts that chlorine is unreactive",
             "correct": False,
             "why": "Being one short is what makes it reactive. A FULL shell "
                    "is what makes group 0 unreactive"},
            {"text": "Seven more",
             "correct": False,
             "why": "Seven is how many it already has. It needs the "
                    "difference between that and eight"},
            {"text": "One more, and it predicts that chlorine reacts readily "
                     "by gaining an electron",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-06-h05",
        "band": "harder",
        "text": "Helium is made underground, collected from natural gas, and "
                "escapes the atmosphere altogether once released. Why does "
                "that make it a genuinely finite resource?",
        "options": [
            {"text": "Because the underground supply is being used faster "
                     "than it is being made, which is the same problem as "
                     "coal and oil and has the same kind of answer",
             "correct": False,
             "why": "Coal can at least be replaced by other fuels. Helium "
                    "leaves the planet, and nothing else cools a "
                    "superconducting magnet"},
            {"text": "Because it cannot be manufactured, cannot be recovered "
                     "once lost, and cannot be substituted in its main use",
             "correct": True},
            {"text": "Because it is one of the rarest elements in the "
                     "universe",
             "correct": False,
             "why": "It is the second commonest element in the universe. The "
                    "problem is specific to Earth"},
            {"text": "Because it is radioactive",
             "correct": False,
             "why": "Helium is stable. It is PRODUCED by radioactive decay, "
                    "which is a different thing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h06",
        "band": "harder",
        "text": "In 1962 xenon was persuaded to form a compound. Why is the "
                "rule about noble gases still taught?",
        "options": [
            {"text": "Because the exception was later withdrawn, and no "
                     "compound of any noble gas has ever been made to hold "
                     "together outside the conditions it was made in",
             "correct": False,
             "why": "A whole shelf of xenon compounds followed and they are "
                    "real. The rule survives with a footnote instead"},
            {"text": "Because xenon is not really a noble gas",
             "correct": False,
             "why": "It is group 0 with a full outer shell. It is simply the "
                    "one whose outer electrons are held least tightly"},
            {"text": "Because it holds for almost everything, and the "
                     "exception is known and bounded",
             "correct": True},
            {"text": "Because school chemistry does not need the exception",
             "correct": False,
             "why": "The exception is worth knowing, and the reason the rule "
                    "survives is that it is still nearly always right"},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h07",
        "band": "harder",
        "text": "A student says the noble gases are unreactive BECAUSE they "
                "are gases. Which single fact settles it?",
        "options": [
            {"text": "That helium is the lightest of them and just as "
                     "unreactive as the heaviest, so weight cannot be doing "
                     "the work either",
             "correct": False,
             "why": "A good point about weight, and the student's claim was "
                    "about being a GAS. Something answers that directly"},
            {"text": "That the noble gases can be liquefied by cooling",
             "correct": False,
             "why": "Liquid helium is just as unreactive as the gas, which is "
                    "suggestive — and a reactive gas is the sharper "
                    "counter-example"},
            {"text": "That air is mostly nitrogen",
             "correct": False,
             "why": "Nitrogen is a fairly unreactive gas and is not a noble "
                    "gas. It settles nothing about the claim"},
            {"text": "That fluorine and oxygen are gases and both react "
                     "ferociously",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e08",
        "band": "easier",
        "text": "The elements in group 0 of the periodic table are known by "
                "one family name. What is it?",
        "options": [
            {"text": "The noble gases",
             "correct": True},
            {"text": "The alkali metals",
             "correct": False,
             "why": "That is group 1 — the metals that react with water to "
              "leave an alkaline solution behind."},
            {"text": "The halogens",
             "correct": False,
             "why": "That is group 7 — a set of reactive non-metals that form "
              "salts with metals."},
            {"text": "The transition metals",
             "correct": False,
             "why": "That is the block sitting between groups 2 and 3, and "
              "every one of them is an ordinary reactive metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e09",
        "band": "easier",
        "text": "How many electrons are in the outer shell of a neon atom?",
        "options": [
            {"text": "Two, and the shell is full",
             "correct": False,
             "why": "Two fills the outer shell of helium and of nothing else. "
              "Neon's outer shell holds eight."},
            {"text": "Eight, and the shell is full",
             "correct": True},
            {"text": "Ten, and the shell is full",
             "correct": False,
             "why": "Ten is the total number of electrons in a neon atom, not "
              "the number sitting in its outer shell."},
            {"text": "None, and the shell is empty",
             "correct": False,
             "why": "Every atom has electrons. A full shell is one with every "
              "place taken, not one with nothing in it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e10",
        "band": "easier",
        "text": "Helium's outer shell is full with only two electrons, "
                "while the other noble gases need eight. How can two be a "
                "full shell?",
        "options": [
            {"text": "Because helium gives away its two electrons and is then "
              "left with an empty shell",
             "correct": False,
             "why": "Helium gives nothing away. Its shell is already complete, "
              "which is the reason it reacts with nothing."},
            {"text": "Because helium counts two of its inner electrons as outer "
              "ones to make the number up",
             "correct": False,
             "why": "Helium has no inner electrons at all — the two it has are "
              "the only electrons in the atom."},
            {"text": "Because helium's outer shell has room for two, and both "
              "places are taken",
             "correct": True},
            {"text": "Because two is the smallest number of electrons that any "
              "atom in the table is allowed",
             "correct": False,
             "why": "Hydrogen manages with one electron, so there is no such "
              "minimum anywhere in the table."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e11",
        "band": "easier",
        "text": "Roughly what share of the air is argon?",
        "options": [
            {"text": "About 21 per cent",
             "correct": False,
             "why": "That is oxygen's share of the air, twenty times argon's."},
            {"text": "About 78 per cent",
             "correct": False,
             "why": "That is nitrogen's share, and nitrogen is the gas argon "
              "was found hiding inside."},
            {"text": "About 50 per cent",
             "correct": False,
             "why": "No gas in the air is present at half. Argon is a minor "
              "part of a mixture that is mostly nitrogen."},
            {"text": "About 1 per cent",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e12",
        "band": "easier",
        "text": "Which noble gas is used in the glass tubes of signs that "
                "glow orange-red?",
        "options": [
            {"text": "Neon",
             "correct": True},
            {"text": "Helium",
             "correct": False,
             "why": "Helium is used where lightness matters. In a tube it glows "
              "a pale peach, not orange-red."},
            {"text": "Krypton",
             "correct": False,
             "why": "Krypton is the rarer, heavier gas used in some lamps, and "
              "it glows a pale blue-white."},
            {"text": "Radon",
             "correct": False,
             "why": "Radon is radioactive and is never put into a sign of any "
              "kind."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e13",
        "band": "easier",
        "text": "What does having a full outer shell mean for an atom?",
        "options": [
            {"text": "It has no electrons at all, so nothing can happen to it",
             "correct": False,
             "why": "Every atom has electrons. A full shell is one in which "
              "every place is already taken."},
            {"text": "It has one electron left to lose before the shell is "
              "complete",
             "correct": False,
             "why": "That describes a group 1 atom. A full shell has nothing "
              "left to shed."},
            {"text": "It has no electron to lose and no room for one to arrive",
             "correct": True},
            {"text": "It has so many electrons that they are too crowded to move",
             "correct": False,
             "why": "Helium is full with two electrons, which is nobody's idea "
              "of crowded. Fullness is the point, not crowding."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e14",
        "band": "easier",
        "text": "Helium is used to cool the magnets inside an MRI scanner. "
                "Which fact about helium does that use depend on?",
        "options": [
            {"text": "It reacts with the metal of the magnet and draws heat out "
              "of it",
             "correct": False,
             "why": "Helium reacts with nothing at all. A reaction is the one "
              "thing it cannot be asked to do."},
            {"text": "It glows when a current is passed through it",
             "correct": False,
             "why": "That is what a sign does, and it warms the gas slightly "
              "rather than cooling anything."},
            {"text": "It is lighter than every other gas in the table",
             "correct": False,
             "why": "Hydrogen is the lighter of the two. Lightness is what a "
              "balloon needs, not a magnet."},
            {"text": "It stays liquid at a lower temperature than anything else",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e15",
        "band": "easier",
        "text": "Argon was finally caught in 1894 when nitrogen taken from "
                "the air was weighed against nitrogen made in the "
                "laboratory. What did the weighing show?",
        "options": [
            {"text": "The air sample was slightly heavier",
             "correct": True},
            {"text": "The air sample was slightly lighter",
             "correct": False,
             "why": "Argon atoms are heavier than nitrogen molecules, so the "
              "sample carrying argon weighed more, not less."},
            {"text": "The two samples weighed exactly the same",
             "correct": False,
             "why": "A difference is what gave argon away. Two identical "
              "readings would have shown nothing at all."},
            {"text": "The laboratory sample was slightly heavier",
             "correct": False,
             "why": "The laboratory sample was the pure one. The extra mass was "
              "in the air sample, where the argon was hiding."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e16",
        "band": "easier",
        "text": "A gas in a sign is said to be excited by the electricity "
                "passing through it. What does excited mean here?",
        "options": [
            {"text": "Its atoms are broken apart by the current",
             "correct": False,
             "why": "The atoms come through unchanged. Only their electrons "
              "move between energy levels."},
            {"text": "Its electrons are pushed to a higher energy level",
             "correct": True},
            {"text": "It is slowly reacting with the tube's glass",
             "correct": False,
             "why": "Nothing is made and nothing is used up, so no reaction is "
              "taking place anywhere in the tube."},
            {"text": "It is hot enough to have started burning",
             "correct": False,
             "why": "A noble gas cannot burn at all, because burning is a "
              "reaction with oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e17",
        "band": "easier",
        "text": "Helium is not manufactured — it is made deep underground. "
                "What makes it?",
        "options": [
            {"text": "Water seeping through limestone and dissolving it",
             "correct": False,
             "why": "That makes a solution of calcium compounds and no helium "
              "whatsoever."},
            {"text": "The slow radioactive decay of heavy elements in rock",
             "correct": True},
            {"text": "Plants deep in the soil releasing it as they respire",
             "correct": False,
             "why": "Respiring releases carbon dioxide. No living thing makes "
              "helium at any depth."},
            {"text": "Hydrogen atoms being squeezed together under pressure",
             "correct": False,
             "why": "That happens inside stars, and it is not where any of the "
              "Earth's helium comes from."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e18",
        "band": "easier",
        "text": "All the group 0 elements are gases at ordinary room "
                "temperature. Why?",
        "options": [
            {"text": "Their atoms are too light to settle into a liquid",
             "correct": False,
             "why": "Xenon is a heavy atom and is still a gas. Weight is not "
              "what decides it."},
            {"text": "Their atoms push each other apart very strongly",
             "correct": False,
             "why": "There is no strong pushing apart. There is simply almost "
              "no attraction holding them together."},
            {"text": "They are kept warm by the reactions going on inside them "
              "all the time",
             "correct": False,
             "why": "No reaction is going on inside them. That is the one thing "
              "these elements never do."},
            {"text": "Their atoms attract each other far too weakly to hold "
              "together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e19",
        "band": "easier",
        "text": "Which description fits every member of group 0?",
        "options": [
            {"text": "A colourless gas with a full outer shell",
             "correct": True},
            {"text": "A coloured gas with one outer electron",
             "correct": False,
             "why": "One outer electron is group 1, and those are solid metals "
              "rather than gases."},
            {"text": "A soft metal with a full outer shell",
             "correct": False,
             "why": "A full outer shell is right, but no group 0 element is a "
              "metal or a solid at room temperature."},
            {"text": "A colourless gas one electron short of full",
             "correct": False,
             "why": "One short of full is group 7, and being one short is "
              "exactly what makes those elements react."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e20",
        "band": "easier",
        "text": "A group 1 atom has one outer electron to lose and a group 2 "
                "atom has two. Which of the two groups reacts more readily, "
                "and why?",
        "options": [
            {"text": "Group 1, because losing one electron is easier than "
                     "losing two",
             "correct": True},
            {"text": "Group 2, because two electrons make for twice as much "
                     "reaction",
             "correct": False,
             "why": "A second electron does not double anything. Getting rid "
              "of two takes more energy than getting rid of one."},
            {"text": "Group 2, because a group 2 atom is the heavier of the "
                     "two",
             "correct": False,
             "why": "Mass is not what sets reactivity. How many electrons "
              "have to go, and how easily, is."},
            {"text": "Neither, because both have outer electrons to lose and "
                     "so react alike",
             "correct": False,
             "why": "Magnesium sits quietly in cold water and sodium, one "
              "square to its left, does not."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e21",
        "band": "easier",
        "text": "Which list contains only noble gases?",
        "options": [
            {"text": "Helium, neon, argon, krypton, xenon",
             "correct": True},
            {"text": "Helium, neon, argon, chlorine, xenon",
             "correct": False,
             "why": "Chlorine is a group 7 element, and it is one of the most "
              "reactive gases there is."},
            {"text": "Helium, sodium, argon, krypton, xenon",
             "correct": False,
             "why": "Sodium is a group 1 metal, and it reacts violently with "
              "water rather than sitting in a jar."},
            {"text": "Hydrogen, neon, argon, krypton, xenon",
             "correct": False,
             "why": "Hydrogen sits on its own at the top of the table and burns "
              "readily, which no noble gas does."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e22",
        "band": "easier",
        "text": "A bright strip of magnesium is sealed in a jar of argon "
                "and left on a shelf for a year. What would you expect to "
                "find when the jar is opened?",
        "options": [
            {"text": "A thick layer of white powder on the strip",
             "correct": False,
             "why": "That white powder would be magnesium oxide, and making it "
              "needs oxygen, which the argon has kept out."},
            {"text": "The magnesium dissolved into the argon",
             "correct": False,
             "why": "A gas does not dissolve a metal, and this gas takes part "
              "in no change whatsoever."},
            {"text": "The magnesium still bright and unchanged",
             "correct": True},
            {"text": "The argon turned a pale green colour",
             "correct": False,
             "why": "Argon is colourless and stays colourless, because nothing "
              "at all has happened to it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e23",
        "band": "easier",
        "text": "Helium is not taken out of the air. Where is the world's "
                "helium collected from?",
        "options": [
            {"text": "Sea water, by evaporating it in shallow pans",
             "correct": False,
             "why": "Evaporating sea water leaves salt behind. There is no "
              "helium dissolved in it to collect."},
            {"text": "Natural gas, as a by-product of drilling for it",
             "correct": True},
            {"text": "Limestone, by heating it in a kiln",
             "correct": False,
             "why": "Heating limestone drives off carbon dioxide, which is a "
              "compound and not a noble gas."},
            {"text": "Coal, by burning it and trapping the fumes",
             "correct": False,
             "why": "Burning coal gives carbon dioxide and smoke. Helium takes "
              "part in no burning at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e24",
        "band": "easier",
        "text": "A helium atom has two electrons in total, and both are in "
                "its outer shell. What does that tell you about its inner "
                "shells?",
        "options": [
            {"text": "It has none — the outer shell is its only shell",
             "correct": True},
            {"text": "It has one inner shell holding six more electrons",
             "correct": False,
             "why": "Helium has two electrons altogether, so there is nothing "
              "left over to put in an inner shell."},
            {"text": "It has two inner shells, one for each of its electrons",
             "correct": False,
             "why": "A shell holds electrons; an electron is not given a shell "
              "of its own to sit in."},
            {"text": "It has eight inner electrons that are not counted",
             "correct": False,
             "why": "Eight is the number that fills the other noble gases' "
              "outer shells. Helium simply has two electrons."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e25",
        "band": "easier",
        "text": "In which year was argon, the first of the noble gases, "
                "isolated?",
        "options": [
            {"text": "1807",
             "correct": False,
             "why": "1807 is when Davy pulled the first group 1 metals out of "
              "their compounds using electricity."},
            {"text": "1869",
             "correct": False,
             "why": "1869 is when Mendeleev published his table, which had no "
              "square anywhere for argon."},
            {"text": "1894",
             "correct": True},
            {"text": "1962",
             "correct": False,
             "why": "1962 is when a noble gas was first made to form a "
              "compound, nearly seventy years later."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e26",
        "band": "easier",
        "text": "A museum seals a fragile old document in a case filled "
                "with argon instead of air. What is the argon there to do?",
        "options": [
            {"text": "Hold the paper flat against the glass",
             "correct": False,
             "why": "A gas presses evenly on every side of the paper and holds "
              "it flat against nothing."},
            {"text": "Keep the case cooler than the room",
             "correct": False,
             "why": "The argon sits at room temperature like everything else "
              "inside the case."},
            {"text": "Keep oxygen away so the paper cannot react with it",
             "correct": True},
            {"text": "Make the paper look brighter",
             "correct": False,
             "why": "Argon is colourless and invisible, so it changes nothing "
              "about how the paper looks."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e27",
        "band": "easier",
        "text": "Argon is sometimes flushed into a packet of food just "
                "before it is sealed. What does that stop?",
        "options": [
            {"text": "The food reacting with oxygen and going stale",
             "correct": True},
            {"text": "The packet being crushed on its way to the shop",
             "correct": False,
             "why": "Any gas at all would hold the packet's shape. Argon is "
              "chosen for what it will not do chemically."},
            {"text": "The food losing its colour in the light",
             "correct": False,
             "why": "Argon is invisible and lets light straight through, so it "
              "shades nothing."},
            {"text": "The food freezing while it is being stored",
             "correct": False,
             "why": "Argon is at the same temperature as everything else in the "
              "packet and cools nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e28",
        "band": "easier",
        "text": "Which of these jobs needs a gas that will NOT react?",
        "options": [
            {"text": "Filling a sealed case so a metal inside cannot corrode",
             "correct": True},
            {"text": "Feeding the flame of a gas cooker",
             "correct": False,
             "why": "A cooker needs a gas that burns, and an unreactive gas "
              "would put the flame straight out."},
            {"text": "Bleaching a stain out of a white shirt",
             "correct": False,
             "why": "Bleaching is a reaction, and it needs something that "
              "attacks the stain rather than leaving it alone."},
            {"text": "Rusting an iron nail overnight for a classroom "
              "demonstration",
             "correct": False,
             "why": "Rusting needs oxygen and water, and an unreactive gas "
              "would stop the rust forming at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-e29",
        "band": "easier",
        "text": "Neon, argon and helium are all used inside glass tubes and "
                "bulbs that carry electricity. What do all three have in "
                "common that makes that safe?",
        "options": [
            {"text": "None of them will burn or attack the glass",
             "correct": True},
            {"text": "Each of the three is heavier than air and sinks to the "
                     "bottom",
             "correct": False,
             "why": "Helium and neon are both lighter than air, so weight is "
              "not what they share."},
            {"text": "Every one of them conducts electricity better than "
                     "copper",
             "correct": False,
             "why": "A gas is a poor conductor. Copper is far better than any "
              "of them at carrying a current."},
            {"text": "All three are made industrially from natural gas",
             "correct": False,
             "why": "Helium comes from natural gas, but neon and argon are "
              "separated out of the air instead."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s08",
        "band": "standard",
        "text": "Radon is a group 0 gas that seeps out of certain rocks. A "
                "student says it must react with the rock in order to get "
                "out. What is wrong with that?",
        "options": [
            {"text": "Radon reacts with nothing; it simply spreads out of the "
              "rock as a gas",
             "correct": True},
            {"text": "Radon reacts with the rock, but so slowly that nobody has "
              "managed to measure it",
             "correct": False,
             "why": "A full outer shell gives radon no slow reaction either. It "
              "has no way to react at any speed."},
            {"text": "Radon does react, but only with the water inside the rock "
              "rather than the rock itself",
             "correct": False,
             "why": "Group 0 elements do not react with water any more than "
              "with rock. The shell is full against both."},
            {"text": "Radon is made by the rock reacting, so the reaction "
              "happens before the gas exists",
             "correct": False,
             "why": "Radon comes from radioactive decay inside the rock, which "
              "is a change in the nucleus and not a reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s09",
        "band": "standard",
        "text": "Helium is the second lightest element in the whole table, "
                "and it is every bit as unreactive as the far heavier "
                "xenon. Which idea does that support?",
        "options": [
            {"text": "Heavier atoms are always the less reactive of any pair",
             "correct": False,
             "why": "Caesium is very heavy and violently reactive. Mass sets no "
              "rule about reactivity at all."},
            {"text": "Whether an element reacts depends on its outer shell, not "
              "on its mass",
             "correct": True},
            {"text": "Lighter atoms move faster, so they have less time to react "
              "with anything",
             "correct": False,
             "why": "Hydrogen atoms move fastest of all and hydrogen burns "
              "readily. Speed is not what decides it."},
            {"text": "Unreactive elements are all found near the middle of the "
              "table by mass",
             "correct": False,
             "why": "Group 0 runs from the lightest end of the table to the "
              "heaviest, and every member is unreactive."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s10",
        "band": "standard",
        "text": "A filament bulb is assembled by mistake with oxygen inside "
                "it instead of argon. Predict what happens when it is "
                "switched on.",
        "options": [
            {"text": "The bulb glows more brightly and lasts much longer than "
                     "normal",
             "correct": False,
             "why": "Oxygen adds nothing to the light. It attacks the filament, "
              "which shortens the bulb's life sharply."},
            {"text": "The light comes out a different colour, because oxygen "
                     "changes it",
             "correct": False,
             "why": "The light comes from the white-hot filament, not from the "
              "gas around it."},
            {"text": "The bulb does not glow at all, because oxygen will not "
                     "carry a current",
             "correct": False,
             "why": "The current runs through the filament, not the gas, so the "
              "bulb lights before it fails."},
            {"text": "The filament burns through almost as soon as it gets hot",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s11",
        "band": "standard",
        "text": "A strip of copper is heated until it glows and then held "
                "in a jar of oxygen, and a second hot strip is held in a "
                "jar of argon. Predict what is seen in each jar.",
        "options": [
            {"text": "Both strips go black, because heat alone blackens hot "
              "copper",
             "correct": False,
             "why": "The black coating is copper oxide, and making it needs "
              "oxygen. Heat on its own leaves the copper bright."},
            {"text": "It goes black in the oxygen and stays bright in the argon",
             "correct": True},
            {"text": "It stays bright in the oxygen and goes black in the argon",
             "correct": False,
             "why": "That is the wrong way round. Argon is the gas that leaves "
              "the copper alone."},
            {"text": "Neither strip changes, because copper is too unreactive to "
              "be attacked",
             "correct": False,
             "why": "Hot copper takes oxygen readily. The black coating in the "
              "oxygen jar is proof of it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s12",
        "band": "standard",
        "text": "A party balloon filled with helium is floating on the "
                "ceiling, and a day later it is lying on the floor. A "
                "student says the helium must have reacted with the rubber. "
                "What is the better explanation?",
        "options": [
            {"text": "The helium reacted slowly with the rubber and became a "
              "heavier compound",
             "correct": False,
             "why": "Helium forms no compound with rubber or with anything "
              "else. Nothing chemical has happened."},
            {"text": "The helium atoms have slipped out through tiny gaps, "
              "unchanged",
             "correct": True},
            {"text": "The helium has turned into a heavier gas over the course "
              "of the day",
             "correct": False,
             "why": "An element does not turn into another element by sitting "
              "in a balloon overnight."},
            {"text": "The helium has been used up in making the balloon float",
             "correct": False,
             "why": "Floating uses nothing up. The gas is either in the balloon "
              "or out of it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s13",
        "band": "standard",
        "text": "Air is 78 per cent nitrogen and 21 per cent oxygen, and a "
                "mixture of other gases makes up the rest. Calculate the "
                "volume of those other gases in 500 litres of air.",
        "options": [
            {"text": "About 50 litres",
             "correct": False,
             "why": "That is a tenth of the sample. Nitrogen and oxygen between "
              "them leave far less than a tenth behind."},
            {"text": "About 105 litres",
             "correct": False,
             "why": "That is oxygen's share of 500 litres, not the share left "
              "over once the oxygen has been counted."},
            {"text": "About 5 litres",
             "correct": True},
            {"text": "About 1 litre",
             "correct": False,
             "why": "That is one litre for every hundred, which forgets that "
                    "the sample is five hundred litres and not one hundred."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s14",
        "band": "standard",
        "text": "A student predicts that neon will react with fluorine, "
                "because fluorine reacts with almost every element there "
                "is. Which response is best?",
        "options": [
            {"text": "The prediction is right, because nothing resists fluorine "
              "for long",
             "correct": False,
             "why": "Neon has resisted it since fluorine was first isolated. No "
              "neon compound has ever been made."},
            {"text": "The prediction is wrong, because neon is a gas and "
              "fluorine can only attack solids",
             "correct": False,
             "why": "Fluorine attacks gases readily — it reacts with hydrogen "
              "explosively. The reason lies with neon's shell."},
            {"text": "The prediction is wrong, because neon's outer shell is "
              "already full",
             "correct": True},
            {"text": "The prediction is right, but only at temperatures far "
              "below freezing",
             "correct": False,
             "why": "Cooling makes reactions slower, never more likely. Neon "
              "reacts with fluorine at no temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s15",
        "band": "standard",
        "text": "Two balloons are prepared, one filled with hydrogen and "
                "one with helium, and a lit splint is held to each in turn. "
                "Describe what happens.",
        "options": [
            {"text": "The hydrogen burns with a squeaky pop and the helium does "
              "nothing",
             "correct": True},
            {"text": "Both burn, but the helium burns with a quieter pop than "
              "the hydrogen",
             "correct": False,
             "why": "Helium does not burn at all. There is no quiet version of "
              "a reaction it cannot have."},
            {"text": "The helium burns and the hydrogen puts the splint out",
             "correct": False,
             "why": "That is the wrong way round. Hydrogen is the gas that "
              "burns with a pop."},
            {"text": "Neither burns, because a balloon keeps the air away from "
              "the splint",
             "correct": False,
             "why": "The gas escapes as the balloon bursts and meets plenty of "
              "air. Hydrogen pops every time."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s16",
        "band": "standard",
        "text": "A steel joint welded in the open air, with no shield of "
                "unreactive gas around it, comes out weak and pitted. "
                "Explain why.",
        "options": [
            {"text": "The metal cools too fast in moving air and cracks",
             "correct": False,
             "why": "Cooling rate matters, but the pitting is chemical: the hot "
              "metal has taken oxygen from the air."},
            {"text": "The nitrogen in the air pushes the molten metal out",
             "correct": False,
             "why": "A gas at ordinary pressure pushes molten metal nowhere. "
              "The damage is done by oxygen reacting."},
            {"text": "The hot metal reacts with oxygen in the air while it is "
              "still molten",
             "correct": True},
            {"text": "The dust in ordinary air settles into the joint and "
              "weakens it",
             "correct": False,
             "why": "A weld made in a filtered clean room is just as pitted. It "
              "is the oxygen, not the dust."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s17",
        "band": "standard",
        "text": "There is helium in the air, yet the world's helium is "
                "taken from natural gas wells instead. Suggest why.",
        "options": [
            {"text": "Helium in the air has already reacted and cannot be "
              "recovered",
             "correct": False,
             "why": "Helium never reacts with anything, so the helium in the "
              "air is as pure as any other."},
            {"text": "There is so little of it in the air that separating it is "
              "not worth the cost",
             "correct": True},
            {"text": "Helium in the air is a different form of helium from the "
              "underground kind",
             "correct": False,
             "why": "Helium is helium wherever it is found. There is only one "
              "kind of the element."},
            {"text": "Taking helium out of the air would leave the atmosphere "
              "short of oxygen",
             "correct": False,
             "why": "Helium is a trace gas, and removing all of it would change "
              "the oxygen in the air not at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s18",
        "band": "standard",
        "text": "An unknown element is a colourless gas. It will not burn, "
                "it makes no acid or alkali when shaken with water, and it "
                "forms no compound with any metal. Which group is it in?",
        "options": [
            {"text": "Group 7",
             "correct": False,
             "why": "Group 7 elements react with metals to make salts, and this "
              "one forms no compound with any metal."},
            {"text": "Group 1",
             "correct": False,
             "why": "Group 1 elements are solid metals, and they leave an "
              "alkaline solution when they meet water."},
            {"text": "Group 6",
             "correct": False,
             "why": "Group 6 elements such as oxygen and sulfur react readily "
              "with metals, and this gas forms no compound with any "
              "metal."},
            {"text": "Group 0",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s19",
        "band": "standard",
        "text": "A small piece of freshly cut sodium is sealed in a jar of "
                "argon. Predict what its surface looks like a month later.",
        "options": [
            {"text": "Dull grey, because the argon has slowly coated it",
             "correct": False,
             "why": "Argon coats nothing. It cannot form a layer on the metal "
              "because it cannot react with it."},
            {"text": "White and powdery, as though it had been left in air",
             "correct": False,
             "why": "That white coating needs oxygen from the air, and the "
              "argon has kept the air out."},
            {"text": "Still bright, because argon will not attack it",
             "correct": True},
            {"text": "Gone, because argon dissolves soft metals slowly",
             "correct": False,
             "why": "No gas dissolves a metal, and argon takes part in no "
              "change of any kind."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s20",
        "band": "standard",
        "text": "A gas is described as inert. Which observation would cast "
                "real doubt on that description?",
        "options": [
            {"text": "It has been made to form a compound under extreme "
              "conditions",
             "correct": True},
            {"text": "It glows brightly when a current is passed through it",
             "correct": False,
             "why": "Glowing is electrons moving between energy levels. Nothing "
              "is made and nothing is used up."},
            {"text": "It is heavier than air and sinks in a jar",
             "correct": False,
             "why": "Density says nothing about reactivity. Argon is heavier "
              "than air and inert."},
            {"text": "It dissolves very slightly in cold water",
             "correct": False,
             "why": "Dissolving is a physical change, and the gas comes back "
              "out of the water unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s21",
        "band": "standard",
        "text": "Some very bright lamps run their filaments hotter than an "
                "ordinary bulb does, and are filled with krypton. Which "
                "property of krypton matters most there?",
        "options": [
            {"text": "It conducts heat away from the filament far faster than "
              "argon does, keeping it cool",
             "correct": False,
             "why": "Cooling the filament would dim the lamp. The gas is there "
              "to protect it, not to chill it."},
            {"text": "It will not react with the filament at any temperature the "
              "lamp reaches",
             "correct": True},
            {"text": "It gives out a white light of its own when it gets hot",
             "correct": False,
             "why": "The light comes from the filament. Krypton glows only when "
              "a current is driven through it."},
            {"text": "It burns away slowly and keeps the pressure inside steady",
             "correct": False,
             "why": "Krypton cannot burn at all, which is the whole reason it "
              "is in there."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s22",
        "band": "standard",
        "text": "Helium boils at −269 °C, the lowest boiling point of any "
                "element. What does that tell you about helium atoms?",
        "options": [
            {"text": "They are so heavy that they need extreme cold to settle "
              "down",
             "correct": False,
             "why": "Helium is the second lightest element there is. Weight is "
              "not what its boiling point measures."},
            {"text": "They repel one another so strongly that only extreme cold "
              "can force them together",
             "correct": False,
             "why": "There is no repulsion to overcome. There is simply almost "
              "no attraction to begin with."},
            {"text": "They react with one another only at very low temperatures",
             "correct": False,
             "why": "Helium atoms never react with each other. Boiling is a "
              "physical change, not a reaction."},
            {"text": "They attract each other so weakly that almost nothing "
              "holds them together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s23",
        "band": "standard",
        "text": "Four unlabelled cylinders are tested. One relights a "
                "glowing splint, one gives a squeaky pop with a lit splint, "
                "one turns limewater milky, and one does nothing in any "
                "test. Which holds the noble gas?",
        "options": [
            {"text": "The one that relights a glowing splint",
             "correct": False,
             "why": "Relighting a splint is the test for oxygen, which is one "
              "of the most reactive gases in the air."},
            {"text": "The one that gives a squeaky pop",
             "correct": False,
             "why": "The pop is hydrogen burning, and burning is a reaction a "
              "noble gas cannot have."},
            {"text": "The one that turns limewater milky",
             "correct": False,
             "why": "That is carbon dioxide, a compound of two non-metals "
              "rather than an element from group 0."},
            {"text": "The one that does nothing in any test",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s24",
        "band": "standard",
        "text": "A liquid in an open tank must be covered with a layer of "
                "unreactive gas to keep air off its surface. Helium is "
                "lighter than air and argon is heavier. Which should be "
                "used, and why?",
        "options": [
            {"text": "Argon, because it is denser than air and stays as a layer "
              "on the surface",
             "correct": True},
            {"text": "Helium, because being lighter it spreads over the surface "
              "more evenly",
             "correct": False,
             "why": "Being lighter than air, helium rises straight off the tank "
              "and lets the air back in."},
            {"text": "Helium, because a lighter gas presses down on the liquid "
              "less and disturbs it less",
             "correct": False,
             "why": "Neither gas disturbs the liquid. The point is which one "
              "will stay where it is put."},
            {"text": "Argon, because a denser gas dissolves into the liquid and "
              "protects it from inside",
             "correct": False,
             "why": "Argon does not dissolve in and protect from inside. It "
              "works by sitting on top as a blanket."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s25",
        "band": "standard",
        "text": "A window is advertised as being filled with inert gas. "
                "What does the word inert tell a buyer, and what does it "
                "not?",
        "options": [
            {"text": "It tells them the gas is invisible, but not whether it is "
              "safe",
             "correct": False,
             "why": "Inert is a word about reacting, not about how the gas "
              "looks. Air is invisible and not inert."},
            {"text": "It tells them the gas is dry, but not whether it is "
              "unreactive",
             "correct": False,
             "why": "That reverses the meaning. Inert is precisely the claim "
              "that the gas will not react."},
            {"text": "It tells them the gas will not react, but not how well it "
              "insulates",
             "correct": True},
            {"text": "It tells them the gas insulates well, but not whether it "
              "will react",
             "correct": False,
             "why": "Insulation is what the window is sold on, but inert makes "
              "no claim about it at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s26",
        "band": "standard",
        "text": "Signs use neon and filament bulbs use argon, although both "
                "gases are equally unreactive. Suggest why the two jobs use "
                "different gases.",
        "options": [
            {"text": "Neon gives out the orange-red light a sign is wanted for",
             "correct": True},
            {"text": "Argon is the only noble gas that will not attack a hot "
              "filament",
             "correct": False,
             "why": "Every noble gas leaves a filament alone. Krypton is used "
              "in some lamps for exactly that reason."},
            {"text": "Neon is the only noble gas that will carry an electric "
              "current",
             "correct": False,
             "why": "Any gas will carry a current if the voltage is high "
              "enough. Argon tubes glow lilac."},
            {"text": "Argon is the only noble gas heavy enough to stay inside a "
              "glass bulb",
             "correct": False,
             "why": "A sealed bulb holds any gas put into it, whatever its "
              "weight."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s27",
        "band": "standard",
        "text": "Helium and argon are both unreactive, yet argon is the one "
                "used in almost every job that needs air kept out. Suggest "
                "why.",
        "options": [
            {"text": "Argon is far cheaper, because it is taken straight out of "
              "the air",
             "correct": True},
            {"text": "Argon is the more unreactive of the two",
             "correct": False,
             "why": "Neither has ever reacted in a workshop. There is nothing "
              "to choose between them on that."},
            {"text": "Helium would react with the hot metal it protects",
             "correct": False,
             "why": "Helium reacts with nothing at all, hot metal included."},
            {"text": "Helium cannot be compressed into a cylinder safely",
             "correct": False,
             "why": "Helium is stored and sold in cylinders every day. Cost, "
              "not safety, is what decides."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s28",
        "band": "standard",
        "text": "A student stores a freshly cut, easily tarnished metal in "
                "a sealed tin of completely dry air. Explain why the metal "
                "tarnishes anyway.",
        "options": [
            {"text": "Drying the air makes it more reactive than ordinary air",
             "correct": False,
             "why": "Drying removes water vapour and changes nothing about how "
              "the oxygen behaves."},
            {"text": "Dry air still contains oxygen, and oxygen is what "
              "tarnishes the metal",
             "correct": True},
            {"text": "The tin itself reacts with the metal wherever the two "
              "touch",
             "correct": False,
             "why": "The tarnish covers the whole surface, including the part "
              "touching nothing."},
            {"text": "Sealing the tin traps heat inside it, and heat on its own "
              "is enough to tarnish a metal",
             "correct": False,
             "why": "A metal heated in argon stays bright. Heat speeds a "
              "reaction up but cannot supply the oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s29",
        "band": "standard",
        "text": "A neon tube in a shop window has been running for twenty "
                "years and the glass is as clear as the day it was made. "
                "What does that tell you about neon?",
        "options": [
            {"text": "It does not attack the glass at any temperature the tube "
              "reaches",
             "correct": True},
            {"text": "It coats the glass with a thin protective layer as it runs",
             "correct": False,
             "why": "Neon leaves no layer anywhere. Forming a coating would "
              "mean reacting, which it cannot do."},
            {"text": "It is cold enough inside the tube to stop any reaction "
              "starting",
             "correct": False,
             "why": "The tube is warm in use, and neon would still not react if "
              "it were hotter."},
            {"text": "It has been replaced regularly, which is why nothing has "
              "built up",
             "correct": False,
             "why": "Nothing is used up in a neon tube, so it never needs "
              "refilling."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s30",
        "band": "standard",
        "text": "Asked how many electrons a xenon atom has in its outer "
                "shell, one student says eight and another says fifty-four. "
                "Who is right, and what does the other number count?",
        "options": [
            {"text": "Fifty-four is right; eight counts the shells the atom has",
             "correct": False,
             "why": "Eight is the outer-shell count. Xenon has nowhere near "
              "eight shells."},
            {"text": "Eight is right; fifty-four counts the atom's electrons "
              "altogether",
             "correct": True},
            {"text": "Both are right; the outer shell can be counted either way",
             "correct": False,
             "why": "There is only one outer-shell count, and it is eight. The "
              "other number is a different quantity."},
            {"text": "Fifty-four is right; eight counts xenon's place along its "
              "period",
             "correct": False,
             "why": "Fifty-four is the total electron count. Eight is what sits "
              "in the outer shell."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s31",
        "band": "standard",
        "text": "A student suggests filling a balloon with argon, so that "
                "it floats and cannot catch fire. Explain why the balloon "
                "will not float.",
        "options": [
            {"text": "Argon is denser than air, so the balloon sinks rather than "
              "rises",
             "correct": True},
            {"text": "Argon reacts with the rubber and loses its lift within "
              "minutes",
             "correct": False,
             "why": "Argon reacts with nothing, rubber included. The problem is "
              "its density, not its chemistry."},
            {"text": "Argon leaks out of rubber faster than any other gas",
             "correct": False,
             "why": "Argon atoms are larger than helium atoms and leak more "
              "slowly, not faster."},
            {"text": "Argon has to be kept under pressure, so it cannot fill a "
              "soft balloon",
             "correct": False,
             "why": "Argon fills a balloon perfectly well at ordinary pressure. "
              "It simply weighs more than the air it displaces."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-s32",
        "band": "standard",
        "text": "Helium's outer shell is full with two electrons and "
                "xenon's is full with eight, and both elements are equally "
                "unreactive. What does that show?",
        "options": [
            {"text": "What matters is that the shell is full, not how many "
              "electrons fill it",
             "correct": True},
            {"text": "What matters is the number eight, and helium is an "
              "exception to the rule",
             "correct": False,
             "why": "Helium is not an exception to anything. Its shell is "
              "genuinely full, and full is what counts."},
            {"text": "What matters is the number of shells, which both atoms "
              "share",
             "correct": False,
             "why": "Helium has one shell and xenon has five. They do not share "
              "that at all."},
            {"text": "What matters is the number of electrons in the atom "
              "altogether",
             "correct": False,
             "why": "Helium has two electrons and xenon fifty-four, and both "
              "are unreactive. The total settles nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h08",
        "band": "harder",
        "text": "Group 0 used to be called the inert gases and is now "
                "usually called the noble gases. Evaluate which name is the "
                "better description today.",
        "options": [
            {"text": "Noble, because a few of these gases have since been made "
              "to form compounds and inert claims too much",
             "correct": True},
            {"text": "Inert, because it is by far the older of the two names, "
              "and the older names in chemistry are the more exact ones",
             "correct": False,
             "why": "Age is no argument. Inert became the weaker name the day "
              "the first compound was made."},
            {"text": "Inert, because none of these gases has ever been made to "
              "react with anything at all",
             "correct": False,
             "why": "Xenon compounds have been made since 1962, so the flat "
              "claim is no longer true."},
            {"text": "Noble, because these gases are the rarest and most "
              "valuable elements in the whole table",
             "correct": False,
             "why": "Argon is one of the commonest gases in the air, and rarity "
              "is not what the name is about."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h09",
        "band": "harder",
        "text": "In 1894 nitrogen taken from air was found to be under half "
                "a per cent denser than nitrogen made in the laboratory. "
                "Explain why so small a difference was enough to claim a "
                "new element.",
        "options": [
            {"text": "Because a small difference is always more convincing than "
              "a large one in careful work",
             "correct": False,
             "why": "Size on its own convinces nobody. What mattered was that "
              "the difference was bigger than the error."},
            {"text": "Because the difference came back every time and was larger "
              "than the error in the measurement",
             "correct": True},
            {"text": "Because the two samples were prepared by different "
              "chemists",
             "correct": False,
             "why": "Different hands would weaken the claim, not strengthen it. "
              "It was repeating the result that counted."},
            {"text": "Because a density difference can only ever be caused by an "
              "undiscovered element",
             "correct": False,
             "why": "A wet sample or a leak would do it too, which is exactly "
              "why the result had to be repeated."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h10",
        "band": "harder",
        "text": "A student argues that the noble gases must all be rare, "
                "since they are unreactive and therefore never get built "
                "into anything. Evaluate the argument.",
        "options": [
            {"text": "It is sound, because an element that forms no compounds "
              "cannot be stored anywhere on Earth",
             "correct": False,
             "why": "An unreactive gas is stored perfectly well as itself, "
              "which is why the air holds so much argon."},
            {"text": "It is sound, because reactive elements are made in greater "
              "quantities inside the Earth",
             "correct": False,
             "why": "How much of an element exists has nothing to do with how "
              "readily it reacts."},
            {"text": "It fails, because how common an element is has nothing to "
              "do with how readily it reacts",
             "correct": True},
            {"text": "It fails, because the noble gases react slowly enough to "
              "be built into rock over long periods",
             "correct": False,
             "why": "They are not reacting slowly. They are not reacting at "
              "all, and they are still common."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h11",
        "band": "harder",
        "text": "Suppose an element were found that had a full outer shell "
                "but was a solid at room temperature. Would that break the "
                "argument this unit makes about group 0?",
        "options": [
            {"text": "Yes, because a full outer shell is what makes an element a "
              "gas in the first place",
             "correct": False,
             "why": "A full shell explains why it does not react. Being a gas "
              "follows from weak attraction, which is a separate matter."},
            {"text": "No, because the argument links a full shell to not "
              "reacting, not to being a gas",
             "correct": True},
            {"text": "Yes, because every element in group 0 has to be a gas for "
              "the group to hold together",
             "correct": False,
             "why": "A group is held together by its outer-shell count, not by "
              "the state its members happen to be in."},
            {"text": "No, because a solid with a full shell would simply be "
              "placed in a different group",
             "correct": False,
             "why": "Its group is settled by its outer electrons, so it would "
              "stay in group 0 whatever its state."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h12",
        "band": "harder",
        "text": "A new element with 118 protons is made and placed at the "
                "foot of group 0. Only a few atoms are ever made and each "
                "lasts a fraction of a second. Evaluate how much to trust a "
                "prediction that it is unreactive.",
        "options": [
            {"text": "Complete trust, because the group argument has never "
              "failed anywhere in the table",
             "correct": False,
             "why": "The group argument is strong, but a prediction nobody can "
              "test stays a prediction."},
            {"text": "No trust at all, because an element whose atoms last a "
              "fraction of a second cannot be said to have any chemistry",
             "correct": False,
             "why": "Chemists do measure the chemistry of such atoms, a few at "
              "a time. It is difficult, not impossible."},
            {"text": "No trust at all, because the trends in the table stop "
              "working past period 6",
             "correct": False,
             "why": "There is no period at which the table simply switches off. "
              "The trends weaken rather than vanish."},
            {"text": "Some trust — the group argument is strong, but a "
              "prediction that cannot be checked stays a prediction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h13",
        "band": "harder",
        "text": "Two ways of stopping hot metal reacting are proposed: "
                "flood the workspace with argon, or pump the air out to "
                "leave a vacuum. Compare them.",
        "options": [
            {"text": "Only the vacuum works, because argon still leaves a gas "
              "touching the metal",
             "correct": False,
             "why": "The gas touching the metal is the point. Argon touches it "
              "and does nothing to it."},
            {"text": "Only the argon works, because a vacuum makes hot metal "
              "boil away",
             "correct": False,
             "why": "Metals are welded in vacuum chambers routinely. A vacuum "
              "excludes oxygen perfectly well."},
            {"text": "Both keep oxygen away; the vacuum needs a sealed chamber "
              "and the argon does not",
             "correct": True},
            {"text": "Both keep oxygen away, but only the vacuum can be used on "
              "a metal that is already hot",
             "correct": False,
             "why": "Argon is used on metal that is already molten, every day "
              "in every welding shop."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h14",
        "band": "harder",
        "text": "A workshop replaces its argon shielding gas with nitrogen "
                "to save money. Its steel welds come out sound, but its "
                "titanium welds crack. Suggest why.",
        "options": [
            {"text": "Nitrogen is denser than argon and blows the molten "
              "titanium out of the joint",
             "correct": False,
             "why": "Nitrogen is the lighter of the two gases, and neither "
              "blows molten metal anywhere."},
            {"text": "Hot titanium reacts with nitrogen, and the steel did not",
             "correct": True},
            {"text": "Nitrogen conducts heat away so fast that the titanium "
              "cools before it joins",
             "correct": False,
             "why": "The cracking is chemical. A gas blanket does not chill a "
              "weld enough to stop it joining."},
            {"text": "Titanium needs a heavier gas above it, and nitrogen floats "
              "off before the weld is finished",
             "correct": False,
             "why": "Nitrogen stays in place as well as argon does. What it "
              "will not do is stay unreactive against hot titanium."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h15",
        "band": "harder",
        "text": "Xenon was made to form a compound in 1962 and argon in "
                "2000, while helium and neon still have none. What does "
                "that pattern suggest about radon, at the foot of the "
                "group?",
        "options": [
            {"text": "Radon should resist more strongly than any of them, being "
              "the largest atom",
             "correct": False,
             "why": "That reverses the pattern. The larger the atom, the looser "
              "its outer electrons are held."},
            {"text": "Radon should behave exactly like helium, because both sit "
              "at an end of the group",
             "correct": False,
             "why": "Sitting at opposite ends of a column is a reason to expect "
              "a difference, not a likeness."},
            {"text": "Radon should form compounds more readily than any of the "
              "others",
             "correct": True},
            {"text": "Radon should form no compounds, because the pattern stops "
              "at the elements that have been tested",
             "correct": False,
             "why": "A pattern that runs the whole way down the group is "
              "evidence about the next member, not silence about it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h16",
        "band": "harder",
        "text": "Helium makes up about 0.3 per cent of the gas from a "
                "helium well and about 0.0005 per cent of the air. "
                "Calculate how many times richer the well is as a source.",
        "options": [
            {"text": "About 60 times richer",
             "correct": False,
             "why": "That drops a power of ten. Dividing 0.3 by 0.0005 gives "
              "six hundred, not sixty."},
            {"text": "About 600 times richer",
             "correct": True},
            {"text": "About 6000 times richer",
             "correct": False,
             "why": "That adds a power of ten. The ratio of 0.3 to 0.0005 is "
              "six hundred."},
            {"text": "About 300 times richer",
             "correct": False,
             "why": "That comes from halving 0.3 rather than dividing it by "
              "0.0005."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h17",
        "band": "harder",
        "text": "A cylinder holds 40 litres of argon and a welding torch "
                "uses 2.5 litres of it every minute. Calculate how long the "
                "cylinder lasts.",
        "options": [
            {"text": "16 minutes",
             "correct": True},
            {"text": "100 minutes",
             "correct": False,
             "why": "That multiplies 40 by 2.5 instead of dividing. The rate "
              "goes underneath, not on top."},
            {"text": "1.6 minutes",
             "correct": False,
             "why": "That is the right division with a power of ten dropped. "
              "Forty divided by 2.5 is sixteen."},
            {"text": "42.5 minutes",
             "correct": False,
             "why": "That adds the two numbers, which have different units and "
              "cannot be added at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h18",
        "band": "harder",
        "text": "Evaluate the claim that the periodic table is simply a "
                "list of the elements.",
        "options": [
            {"text": "Correct, because everything the table contains can be "
              "written out as a plain list in order of atomic number",
             "correct": False,
             "why": "The order can be written as a list; the columns are what a "
              "list throws away."},
            {"text": "Correct, because the table tells you nothing that cannot "
              "be looked up element by element",
             "correct": False,
             "why": "It told chemists about elements nobody had looked up, "
              "because nobody had found them yet."},
            {"text": "Wrong, because the table is only a way of storing facts "
              "that were already known",
             "correct": False,
             "why": "That is the same claim in different words, and the "
              "predictions are what refute it."},
            {"text": "Wrong, because one number — the group — predicts how an "
              "element behaves before anyone has met it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h19",
        "band": "harder",
        "text": "A sealed tube of an unknown colourless gas will not burn, "
                "will not relight a splint and does nothing to limewater. "
                "Which single further measurement would be most useful in "
                "identifying it?",
        "options": [
            {"text": "Its density, compared against the densities of the known "
              "gases",
             "correct": True},
            {"text": "Its colour, viewed against a white background",
             "correct": False,
             "why": "The gas has already been described as colourless, so "
              "looking again adds nothing."},
            {"text": "Its pH, found by bubbling it through universal indicator",
             "correct": False,
             "why": "A gas that forms no acid or alkali leaves the indicator at "
              "seven, which is what every noble gas does."},
            {"text": "Its mass, found by weighing the sealed tube on a balance",
             "correct": False,
             "why": "The mass of the tube tells you nothing until you know the "
              "volume, which is what density supplies."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h20",
        "band": "harder",
        "text": "A student argues that because a gas is unreactive, it must "
                "be harmless to breathe. Explain why that does not follow.",
        "options": [
            {"text": "It does follow — a gas can only do harm by reacting with "
              "something inside the person who breathes it",
             "correct": False,
             "why": "A gas that takes the place of the air does harm without "
              "reacting with anything at all."},
            {"text": "It does not follow, because unreactive gases turn reactive "
              "at body temperature",
             "correct": False,
             "why": "Body temperature is nothing like hot enough to change a "
              "noble gas, which stays unreactive throughout."},
            {"text": "It does not follow, because a gas that takes the place of "
              "air leaves no oxygen to breathe",
             "correct": True},
            {"text": "It does not follow, because unreactive gases are always "
              "radioactive as well",
             "correct": False,
             "why": "Only radon is radioactive, and that has nothing to do with "
              "its full outer shell."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h21",
        "band": "harder",
        "text": "Group 1 elements have one outer electron and group 7 have "
                "seven, but most group 0 atoms have eight rather than none. "
                "Explain what the 0 in the group's name is counting.",
        "options": [
            {"text": "It counts the shells the atom has, which is zero for a "
              "full one",
             "correct": False,
             "why": "Every atom has at least one shell, and a full shell is "
              "still a shell."},
            {"text": "It counts the electrons the atom has available to react, "
              "which is none",
             "correct": True},
            {"text": "It counts the electrons in the outer shell, and eight is "
              "written as 0 by convention",
             "correct": False,
             "why": "Eight is never written as zero. The 0 is a different count "
              "from the outer-shell count."},
            {"text": "It counts the number of compounds the element forms, which "
              "was thought to be none",
             "correct": False,
             "why": "The other group numbers do not count compounds, so the 0 "
              "cannot be counting them either."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h22",
        "band": "harder",
        "text": "A lamp maker swaps the argon in a bulb for krypton and "
                "finds the bulb lasts noticeably longer. Both gases are "
                "equally unreactive. Suggest why the change helped.",
        "options": [
            {"text": "Krypton reacts with the metal that evaporates and turns it "
              "back into filament",
             "correct": False,
             "why": "Krypton reacts with nothing. Nothing is turned back into "
              "anything inside the bulb."},
            {"text": "Krypton conducts electricity itself, so far less of the "
              "current has to pass through the filament",
             "correct": False,
             "why": "The current runs through the filament alone. The gas "
              "carries none of it."},
            {"text": "Krypton is colourless, so more of the filament's light "
              "escapes the bulb",
             "correct": False,
             "why": "Argon is colourless too, so the swap changes nothing about "
              "the light getting out."},
            {"text": "Krypton atoms are heavier, so they slow the escape of "
              "metal evaporating off the filament",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h23",
        "band": "harder",
        "text": "Evaluate the claim that because the noble gases react with "
                "nothing, they have no chemistry worth learning.",
        "options": [
            {"text": "Fair, because a group that has no reactions can teach "
              "nothing about reactions",
             "correct": False,
             "why": "A group with no reactions is the clean case that shows "
              "what causes reactions everywhere else."},
            {"text": "Fair, because everything worth knowing about them fits "
              "into a single sentence",
             "correct": False,
             "why": "The sentence is short. What follows from it runs through "
              "every other group in the table."},
            {"text": "Unfair, because they are the only elements whose uses are "
              "worth anything industrially",
             "correct": False,
             "why": "Iron, copper and chlorine are all used far more heavily. "
              "Usefulness is not the reason."},
            {"text": "Unfair, because their lack of reaction is what explains "
              "every other group's reactions",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h24",
        "band": "harder",
        "text": "Helium boils at −269 °C and xenon at −108 °C, and both "
                "have full outer shells. Explain the difference between the "
                "two boiling points.",
        "options": [
            {"text": "Xenon's shell is fuller than helium's and holds its "
                     "atoms together more tightly",
             "correct": False,
             "why": "A shell is either full or it is not. Neither atom's shell "
              "is fuller than the other's."},
            {"text": "Xenon's atoms are larger and attract one another more "
              "strongly than helium's do",
             "correct": True},
            {"text": "Xenon reacts weakly with itself at low temperature, which "
              "helium cannot do",
             "correct": False,
             "why": "Neither gas reacts with itself. Boiling is a physical "
              "change throughout."},
            {"text": "Helium is under greater pressure in the atmosphere, which "
              "lowers its boiling point",
             "correct": False,
             "why": "Both boiling points are quoted at the same pressure, and "
              "helium is under no special pressure anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h25",
        "band": "harder",
        "text": "Compare what the isolation of argon did to the periodic "
                "table with what the first xenon compound did to the rule "
                "that noble gases do not react.",
        "options": [
            {"text": "Both overturned what had gone before and forced a fresh "
              "start",
             "correct": False,
             "why": "Neither overturned anything. One extended the table and "
              "the other narrowed a rule."},
            {"text": "The argon result narrowed a rule about reacting; the xenon "
              "result added a whole new column to the table",
             "correct": False,
             "why": "That is the two results the wrong way round."},
            {"text": "The argon result added a new column to the table; the "
              "xenon result narrowed a rule without ending it",
             "correct": True},
            {"text": "Both left the table and the rule exactly as they were and "
              "only added detail",
             "correct": False,
             "why": "A new column is not a detail, and a rule that gains an "
              "exception has genuinely changed."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h26",
        "band": "harder",
        "text": "A document can be protected either in a case flooded with "
                "argon or in a case pumped out to a vacuum. Suggest one "
                "practical advantage of the argon.",
        "options": [
            {"text": "The argon reacts with any oxygen that leaks into the case "
              "and takes it back out of the air inside",
             "correct": False,
             "why": "Argon removes nothing. It keeps oxygen out by taking up "
              "the space, not by reacting with it."},
            {"text": "The argon holds the paper at ordinary pressure, so nothing "
              "is stressed or distorted",
             "correct": True},
            {"text": "The argon keeps the paper cooler than a vacuum would",
             "correct": False,
             "why": "Both cases sit at room temperature. Neither cools the "
              "paper at all."},
            {"text": "The argon blocks the light that would otherwise fade the "
              "ink",
             "correct": False,
             "why": "Argon is colourless and invisible, and lets light through "
              "exactly as a vacuum does."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h27",
        "band": "harder",
        "text": "A supplier advertises a cylinder of nitrogen as having "
                "zero reactivity. Evaluate the claim.",
        "options": [
            {"text": "Sound, because nitrogen makes up most of the air and the "
              "air reacts with nothing",
             "correct": False,
             "why": "The oxygen in that same air reacts with a great deal. Air "
              "is not an unreactive mixture."},
            {"text": "Sound, because nitrogen has a full outer shell in the same "
              "way group 0 does",
             "correct": False,
             "why": "Nitrogen is in group 5 and its outer shell is not full. It "
              "is unreactive for a different reason."},
            {"text": "Too strong, because nitrogen is unreactive at room "
              "temperature but reacts when hot enough",
             "correct": True},
            {"text": "Too strong, because nitrogen dissolves readily in water "
              "and turns the solution distinctly acidic",
             "correct": False,
             "why": "Nitrogen gas does not dissolve to give an acid. It sits in "
              "water unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h28",
        "band": "harder",
        "text": "Two students explain group 0's lack of reaction "
                "differently. One says the outer shells are full; the other "
                "says the atoms are too far apart to meet. Which evidence "
                "settles it?",
        "options": [
            {"text": "Liquid xenon has its atoms touching and still does not "
              "react",
             "correct": True},
            {"text": "Argon is one of the commonest gases in the air and still "
              "does not react",
             "correct": False,
             "why": "Being common says nothing about how close the atoms are to "
              "one another."},
            {"text": "Helium is lighter than argon and both fail to react",
             "correct": False,
             "why": "Mass is not what either student claimed, so it settles "
              "neither explanation."},
            {"text": "Neon glows when a current is passed through it and still "
              "does not react",
             "correct": False,
             "why": "Glowing shows the electrons moving, not how far apart the "
              "atoms are."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h29",
        "band": "harder",
        "text": "An MRI magnet is topped up with 1500 litres of liquid "
                "helium every three years. Calculate the volume needed over "
                "twelve years at the same rate.",
        "options": [
            {"text": "4500 litres",
             "correct": False,
             "why": "That is nine years' worth. Twelve years is four top-ups, "
              "not three."},
            {"text": "18 000 litres",
             "correct": False,
             "why": "That multiplies by twelve rather than by the four top-ups "
              "twelve years contains."},
            {"text": "6000 litres",
             "correct": True},
            {"text": "500 litres",
             "correct": False,
             "why": "That divides 1500 by three, which gives one year's share "
              "rather than twelve years' total."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h30",
        "band": "harder",
        "text": "A student predicts that the undiscovered element below "
                "radon in group 0 would be a solid at room temperature. "
                "Evaluate the prediction.",
        "options": [
            {"text": "Unreasonable, because every group 0 element must be a gas "
              "by definition",
             "correct": False,
             "why": "Group 0 is defined by a full outer shell, not by the state "
              "its members happen to take."},
            {"text": "Unreasonable, because boiling points fall going down group "
              "0",
             "correct": False,
             "why": "They rise going down the group, from helium's −269 °C "
              "towards radon's −62 °C."},
            {"text": "Reasonable, because boiling points rise down the group — "
              "but the element has never been made in useful amounts",
             "correct": True},
            {"text": "Reasonable, because the atoms at the foot of the group are "
              "so heavy that they can no longer move about as a gas",
             "correct": False,
             "why": "Heavy atoms move perfectly well. What rises down the group "
              "is the attraction between them."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h31",
        "band": "harder",
        "text": "Compare what a shield of argon does for a weld with what a "
                "coat of paint does for a steel gate.",
        "options": [
            {"text": "Both keep oxygen off the metal — the argon for minutes, "
              "the paint for years",
             "correct": True},
            {"text": "Both react with the oxygen in the air before it can reach "
              "the metal underneath",
             "correct": False,
             "why": "Neither reacts with the oxygen. Both work by keeping it "
              "physically away from the metal."},
            {"text": "The argon keeps oxygen away and the paint keeps the metal "
              "warm enough not to rust",
             "correct": False,
             "why": "Warmth speeds rusting up rather than preventing it. Paint "
              "works as a barrier."},
            {"text": "The paint keeps oxygen away and the argon simply cools the "
              "weld more evenly",
             "correct": False,
             "why": "Argon is a shield, not a coolant. Keeping oxygen off the "
              "molten metal is its whole job."},
        ],
        "figure": None,
    },
    {
        "id": "c8-06-h32",
        "band": "harder",
        "text": "Evaluate the claim that group 0 is the strongest evidence "
                "that chemistry is decided by outer-shell electrons.",
        "options": [
            {"text": "Weak evidence, because a group that does nothing cannot "
              "demonstrate a cause",
             "correct": False,
             "why": "A group that does nothing is exactly the control case, and "
              "controls are strong evidence."},
            {"text": "Weak evidence, because group 0 was the last group to be "
              "added to the table",
             "correct": False,
             "why": "When a group was found has no bearing on what it "
              "demonstrates."},
            {"text": "Strong evidence, because these elements are the only ones "
              "whose outer electrons have ever been counted exactly",
             "correct": False,
             "why": "Electrons have been counted for every element in the "
              "table, not only for group 0."},
            {"text": "Strong evidence, because the one group with no electrons "
              "available to react is the one group that does not react",
             "correct": True},
        ],
        "figure": None,
    },
]
