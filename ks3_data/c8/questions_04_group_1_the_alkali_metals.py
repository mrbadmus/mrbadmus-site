"""C8 lesson 04 — Group 1, the alkali metals: twelve questions (MRB-281).

The lesson's argument is one shape: every member of group 1 does the SAME
thing with water — hydroxide plus hydrogen, leaving an alkali — and what
changes down the column is only how hard the reaction is pushed. The page
teaches it by running lithium, sodium and potassium one at a time.

These twelve probe the angles the mastery ladder leaves alone: what stays the
same as well as what changes, where the heat comes from, and how far a trend
can be pushed into elements the student has never seen.

The distractors are built from the lesson's declared misconception.

`PTAB-07` (sodium melted because the water was hot) drives the wrong options
in e03, s01, s03 and h01. Each puts the energy into the trough rather than
into the reaction. s03 is the one that matters: the water is at room
temperature and lithium in the SAME trough does not melt, so the belief has to
explain why one metal melted and the other did not.

A second strand is the trend itself, and it is the one the next lesson exists
to break: e02, s02, h03 and h04 turn on reactivity rising DOWNWARD and on the
reason for it — an outer electron further from the nucleus and more easily
lost.

⚠️ **NO QUESTION HERE STATES A DENSITY TREND** (MRB-281, R4 flag 11). Lithium
0.53, sodium 0.97, potassium 0.86 is not monotonic, so there is no trend to
test and a distractor asserting one would be teaching a falsehood by offering
it. e04 uses floating — which all three do — and says only that.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "group-1-the-alkali-metals"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-04-e01",
        "band": "easier",
        # ⚑ Asks what the LEFTOVER SOLUTION proves, not what the products
        # are — the recall rung already asks for the products, and check 6 is
        # right that a bank restating a rung adds no depth.
        "text": "After a group 1 metal has reacted, the water in the trough "
                "turns universal indicator purple. What does that show?",
        "options": [
            {"text": "The solution is alkaline, because a metal hydroxide has "
                     "dissolved in it",
             "correct": True},
            {"text": "The solution is acidic, because hydrogen was given off "
                     "into it",
             "correct": False,
             "why": "The hydrogen leaves as a gas. What stays behind is the "
                    "hydroxide, and purple is the alkali end of the scale."},
            {"text": "The solution is neutral, because the metal has been "
                     "used up",
             "correct": False,
             "why": "Neutral is green. The metal being used up does not "
                    "remove what it turned into."},
            {"text": "The water was already alkaline before the metal went "
                     "in",
             "correct": False,
             "why": "Tap water is close to neutral. The colour appeared with "
                    "the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e02",
        "band": "easier",
        "text": "Which of lithium, sodium and potassium reacts most "
                "violently with water?",
        "options": [
            {"text": "Lithium, because it is at the top of the group",
             "correct": False,
             "why": "Top of group 1 is the LEAST violent. Lithium fizzes "
                    "steadily for nearly a minute."},
            {"text": "Potassium, because reactivity increases down the group",
             "correct": True},
            {"text": "Sodium, because it is in the middle and best balanced",
             "correct": False,
             "why": "There is nothing special about the middle. Sodium is "
                    "more violent than lithium and less than potassium."},
            {"text": "All three equally, because they are in the same group",
             "correct": False,
             "why": "Same group means the same REACTION, not the same "
                    "vigour."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e03",
        "band": "easier",
        "text": "A piece of sodium melts into a ball as it moves across the "
                "water. Where does the heat come from?",
        "options": [
            {"text": "From the water, which must have been warm to start with",
             "correct": False,
             "why": "The water is at room temperature. Lithium in the same "
                    "trough does not melt."},
            {"text": "From friction as the ball skates across the surface",
             "correct": False,
             "why": "The ball has already melted before it moves. Friction on "
                    "water is nowhere near enough."},
            {"text": "From the reaction, which releases energy as it happens",
             "correct": True},
            {"text": "From the air, which warms the metal once the oil is off",
             "correct": False,
             "why": "Air at room temperature cannot bring a metal to 98 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e04",
        "band": "easier",
        "text": "Lithium, sodium and potassium all sit on the surface of the "
                "water rather than sinking. What does that show?",
        "options": [
            {"text": "That they get less dense as you go down the group",
             "correct": False,
             "why": "There is no such trend: lithium is 0.53, sodium 0.97 and "
                    "potassium 0.86. All that can be said is that all three "
                    "float."},
            {"text": "That they get more dense as you go down the group",
             "correct": False,
             "why": "The figures do not run that way either, and no trend in "
                    "density is claimed anywhere in this lesson."},
            {"text": "That they are not really metals, since metals sink",
             "correct": False,
             "why": "They are metals — shiny when cut and good conductors. "
                    "Floating is one of the habits they break."},
            {"text": "That all three are less dense than water",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-04-s01",
        "band": "standard",
        "text": "Why does sodium melt during its reaction with water when "
                "lithium does not?",
        "options": [
            {"text": "Sodium releases energy faster and melts at a much lower "
                     "temperature",
             "correct": True},
            {"text": "Sodium is put into warmer water than lithium is",
             "correct": False,
             "why": "Both go into the same trough at the same temperature. "
                    "The metal is the only thing that changed."},
            {"text": "Sodium is softer, so it melts more easily in any "
                     "situation",
             "correct": False,
             "why": "Softness at room temperature and melting point are "
                    "different properties. Lithium is soft too."},
            {"text": "Sodium absorbs heat from the water and so warms up",
             "correct": False,
             "why": "The water gets warmer, not colder. The energy is coming "
                    "OUT of the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s02",
        "band": "standard",
        "text": "Why does reactivity increase going down group 1?",
        "options": [
            {"text": "Because the atoms get heavier and heavier atoms react "
                     "faster",
             "correct": False,
             "why": "Mass is not the mechanism. Group 7 gets heavier downwards "
                    "and gets LESS reactive."},
            {"text": "Because the outer electron sits further out and is "
                     "lost more easily",
             "correct": True},
            {"text": "Because there are more outer electrons to lose lower "
                     "down",
             "correct": False,
             "why": "Every group 1 atom has exactly one outer electron. That "
                    "is what makes them a group."},
            {"text": "Because the metals lower down are softer to cut",
             "correct": False,
             "why": "Softness runs alongside reactivity; it does not cause "
                    "it. Both come from the same loose outer electron."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s03",
        "band": "standard",
        "text": "A student says the trough water must be hot, because the "
                "sodium melted in it. What one observation would settle it?",
        "options": [
            {"text": "Watch whether the sodium floats, since hot water is "
                     "less dense",
             "correct": False,
             "why": "Sodium floats in cold water too. Floating tells you "
                    "nothing about temperature here."},
            {"text": "Check the indicator, since hot water turns it purple "
                     "faster",
             "correct": False,
             "why": "The indicator responds to the hydroxide formed, not to "
                    "temperature."},
            {"text": "Put a thermometer in the trough before the sodium goes "
                     "in",
             "correct": True},
            {"text": "Try again with a bigger piece to see whether it melts "
                     "sooner",
             "correct": False,
             "why": "A bigger piece is more dangerous and tests the wrong "
                    "thing — it changes the reaction, not the water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s04",
        "band": "standard",
        "text": "Why are the group 1 metals stored under oil?",
        "options": [
            {"text": "To stop them drying out and crumbling into powder",
             "correct": False,
             "why": "They do not dry out. The problem is what the air DOES to "
                    "them, not what it takes away."},
            {"text": "To keep them cold, since they melt at low temperatures",
             "correct": False,
             "why": "Oil at room temperature keeps nothing cold, and 63 °C is "
                    "still far above a laboratory."},
            {"text": "To make them easier to cut with a knife when needed",
             "correct": False,
             "why": "They cut easily either way. The oil is a barrier, not a "
                    "lubricant."},
            {"text": "To keep air and water away from the metal surface",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-04-h01",
        "band": "harder",
        "text": "A hand warmer and a piece of sodium on water both get hot "
                "without anything being plugged in. What do the two have in "
                "common?",
        "options": [
            {"text": "Both release energy that was already stored in the "
                     "chemicals",
             "correct": True},
            {"text": "Both take heat in from the room and concentrate it",
             "correct": False,
             "why": "Taking heat in would COOL the room. Both of these warm "
                    "their surroundings."},
            {"text": "Both create new energy as the reaction proceeds",
             "correct": False,
             "why": "Energy is never created. It was stored in the "
                    "arrangement of the chemicals beforehand."},
            {"text": "Both need to be heated before anything begins",
             "correct": False,
             "why": "Neither does. A hand warmer starts with a snap and "
                    "sodium starts the moment it touches water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h02",
        "band": "harder",
        "text": "Caesium is two places below potassium in group 1. Which "
                "prediction about its reaction with water is best supported?",
        "options": [
            {"text": "It reacts less violently, since the trend levels off "
                     "lower down",
             "correct": False,
             "why": "Nothing in the group suggests a levelling off, and "
                    "caesium is in fact the most violent of them."},
            {"text": "It reacts more violently and still gives a hydroxide "
                     "and hydrogen",
             "correct": True},
            {"text": "It reacts more violently and gives a different set of "
                     "products",
             "correct": False,
             "why": "The products are what does NOT change down a group. Only "
                    "the vigour does."},
            {"text": "It does not react, because very large atoms are "
                     "unreactive",
             "correct": False,
             "why": "Large atoms in group 1 are the MOST reactive, because "
                    "the outer electron is furthest out."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h03",
        "band": "harder",
        "text": "Group 1 gets more reactive downwards and group 7 gets less "
                "reactive downwards. What single idea explains both?",
        "options": [
            {"text": "That heavier atoms always react more slowly than "
                     "lighter ones",
             "correct": False,
             "why": "That would predict both groups running the same way, and "
                    "they do not."},
            {"text": "That each group happens to follow its own unrelated "
                     "rule",
             "correct": False,
             "why": "Two unrelated rules is what you say when you have not "
                    "found the reason. There is one reason."},
            {"text": "That the outer electron is further from the nucleus in "
                     "a bigger atom",
             "correct": True},
            {"text": "That metals become less metallic further down the "
                     "table",
             "correct": False,
             "why": "Group 1 becomes more strongly metallic downwards, and "
                    "group 7 contains no metals at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h04",
        "band": "harder",
        "text": "Why is a prediction about rubidium more trustworthy than a "
                "prediction about a brand-new element placed in group 1, "
                "period 8?",
        "options": [
            {"text": "Because rubidium is lighter, and light elements are "
                     "easier to predict",
             "correct": False,
             "why": "Mass is not what makes a prediction safe. Evidence is."},
            {"text": "Because rubidium is a metal and the new element might "
                     "not be",
             "correct": False,
             "why": "Anything placed in group 1 is expected to be a metal. "
                    "That part is not in doubt."},
            {"text": "Because group 1 stops at rubidium and goes no further",
             "correct": False,
             "why": "Caesium and francium are both below it. The group does "
                    "not stop there."},
            {"text": "Because rubidium sits inside the range where the trend "
                     "has been tested",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-04-e05",
        "band": "easier",
        "text": "Why are the group 1 metals called ALKALI metals?",
        "options": [
            {"text": "Because the metal itself is an alkali, which is why it "
                     "burns skin on contact and has to be handled with tongs "
                     "at all times",
             "correct": False,
             "why": "The metal is not an alkali. It is named for what it "
                    "leaves behind in the water"},
            {"text": "Because they are found in alkaline rocks, and are always "
                     "dug out from them",
             "correct": False,
             "why": "Where they are found is not the reason. The name comes "
                    "from the reaction"},
            {"text": "Because they neutralise any acid the moment they come "
                     "into contact with it",
             "correct": False,
             "why": "Their hydroxides do that. The metals react violently "
                    "with acid rather than gently neutralising it"},
            {"text": "Because their reaction with water leaves an alkaline "
                     "solution",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e06",
        "band": "easier",
        "text": "What does the word trend mean in this lesson?",
        "options": [
            {"text": "A change that runs steadily in one direction through a "
                     "group",
             "correct": True},
            {"text": "The property that every element in a group has in "
                     "common with every other element in it, which is what "
                     "makes them a family in the first place",
             "correct": False,
             "why": "That is what a family shares. A trend is what CHANGES as "
                    "you go down it"},
            {"text": "The most popular explanation among chemists at the "
                     "time",
             "correct": False,
             "why": "That is the everyday use of the word. Here it names a "
                    "pattern in the elements"},
            {"text": "An exception to a rule",
             "correct": False,
             "why": "An exception breaks a pattern. A trend is the pattern"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e07",
        "band": "easier",
        "text": "A group 1 metal is dropped into water. Which gas is given "
                "off?",
        "options": [
            {"text": "Oxygen, because it is the water that is being broken "
                     "apart and oxygen is what water is mostly made of by "
                     "mass",
             "correct": False,
             "why": "The oxygen stays behind in the hydroxide. The gas that "
                    "leaves is hydrogen"},
            {"text": "Hydrogen",
             "correct": True},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "There is no carbon anywhere in the trough. Nothing could "
                    "make it"},
            {"text": "No gas at all — the fizzing is the metal melting",
             "correct": False,
             "why": "Melting makes no bubbles. Collect the gas and it pops "
                    "with a lit splint"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-04-s05",
        "band": "standard",
        "text": "Freshly cut sodium is a mirror for about four seconds and "
                "then dulls, with nothing touching it. What is attacking it?",
        "options": [
            {"text": "The oil it was stored under, which clings to the "
                     "surface and spreads across the fresh cut as soon as the "
                     "knife has passed through",
             "correct": False,
             "why": "The oil is there to keep this from happening. What dulls "
                    "the surface is the air"},
            {"text": "The knife, which leaves metal behind on the cut",
             "correct": False,
             "why": "A clean knife leaves nothing that would dull a whole "
                    "surface in seconds"},
            {"text": "Nothing — the shine fades because the surface dries",
             "correct": False,
             "why": "Nothing is drying. A new compound is forming on the "
                    "surface, which is why it goes dull"},
            {"text": "The air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s06",
        "band": "standard",
        "text": "Rubidium is one place below potassium. Which prediction "
                "about it is best supported by the trend?",
        "options": [
            {"text": "It reacts more violently with water than potassium "
                     "does",
             "correct": True},
            {"text": "It sinks in water, because the group 1 metals get "
                     "denser going down and rubidium is heavy enough to go "
                     "under",
             "correct": False,
             "why": "Density does rise down the group, and lithium, sodium "
                    "and potassium all float. Reactivity is the trend this "
                    "lesson establishes"},
            {"text": "It reacts less violently with water than potassium does, "
                     "being lower down",
             "correct": False,
             "why": "The wrong way round. Group 1 gets more reactive going "
                    "down"},
            {"text": "It does not react with water at all",
             "correct": False,
             "why": "Every group 1 metal reacts with water. That is what "
                    "makes them a family"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s07",
        "band": "standard",
        "text": "Sodium melts at 98 °C, which is low for a metal. Why does "
                "that matter for its reaction with water?",
        "options": [
            {"text": "Because water boils at 100 °C, so the sodium and the "
                     "water reach their two temperatures at almost exactly "
                     "the same moment",
             "correct": False,
             "why": "The trough stays cold. The reaction reaches 98 °C in the "
                    "metal itself, and the water never boils"},
            {"text": "Because the reaction releases enough energy fast enough "
                     "to reach that temperature, so the metal melts into a "
                     "ball",
             "correct": True},
            {"text": "Because it means sodium is not really a metal",
             "correct": False,
             "why": "A low melting point is unusual for a metal and does not "
                    "disqualify it. Mercury's is lower still"},
            {"text": "Because it lets the sodium dissolve in the water",
             "correct": False,
             "why": "It reacts rather than dissolving. Melting and dissolving "
                    "are different things"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-04-h05",
        "band": "harder",
        "text": "No group 1 metal has ever been found as the metal in nature. "
                "What does that tell you about them?",
        "options": [
            {"text": "That they are extremely rare, so any that formed was "
                     "used up long ago and none is left anywhere near the "
                     "surface of the Earth",
             "correct": False,
             "why": "Sodium and potassium are both abundant. What they are "
                    "not is UNCOMBINED"},
            {"text": "That they can only be made artificially, in a laboratory "
                     "rather than found in rock",
             "correct": False,
             "why": "They are extracted from their compounds rather than "
                    "made. The atoms were always there"},
            {"text": "That they are not really elements",
             "correct": False,
             "why": "They are elements, locked into compounds. Gold is an "
                    "element too and is found uncombined"},
            {"text": "That they are reactive enough to have combined with "
                     "something long ago",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h06",
        "band": "harder",
        "text": "Davy isolated sodium in 1807 by passing electricity through "
                "its molten hydroxide. Why had nobody managed it before?",
        "options": [
            {"text": "Because heating and chemical methods could not break "
                     "the compound, and the battery was new",
             "correct": True},
            {"text": "Because sodium had not been recognised as an element "
                     "until then, so nobody had any reason to try to separate "
                     "it out of anything",
             "correct": False,
             "why": "Its compounds had been used for centuries and were "
                    "suspected of holding a metal. What was missing was the "
                    "technique"},
            {"text": "Because sodium is far too rare to have been collected in "
                     "any useful quantity by anybody before that time",
             "correct": False,
             "why": "It is one of the commonest elements in the crust. "
                    "Getting it OUT was the difficulty"},
            {"text": "Because nobody had thought of melting the compound "
                     "first",
             "correct": False,
             "why": "Melting is part of the method and not the missing piece. "
                    "The electricity is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h07",
        "band": "harder",
        "text": "A student says the group 1 trend must be about mass, since "
                "the metals get heavier going down. What is the fault in that "
                "reasoning?",
        "options": [
            {"text": "The metals do not get heavier going down the group, so "
                     "the observation the reasoning rests on is simply "
                     "mistaken",
             "correct": False,
             "why": "They do get heavier. The fault is in what follows from "
                    "it"},
            {"text": "Mass and reactivity happen to run together here, and "
                     "the reason is the outer electron sitting further out in "
                     "a bigger atom",
             "correct": True},
            {"text": "Heavier things always react less, so the student has "
                     "the direction backwards",
             "correct": False,
             "why": "There is no such rule either way. Mass is not what "
                    "drives reactivity"},
            {"text": "Nothing is wrong — mass is the reason",
             "correct": False,
             "why": "If mass were the reason, group 7 would get more reactive "
                    "going down too, and it does the opposite"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e08",
        "band": "easier",
        "text": "Group 1 contains six elements. Which list gives them in "
                "order from the top of the group downwards?",
        "options": [
            {"text": "Lithium, sodium, magnesium, calcium, rubidium, caesium",
             "correct": False,
             "why": "Magnesium and calcium sit one column across in group 2 "
                    "and are not alkali metals"},
            {"text": "Lithium, sodium, potassium, rubidium, caesium, francium",
             "correct": True},
            {"text": "Francium, caesium, rubidium, potassium, sodium, lithium",
             "correct": False,
             "why": "That is the group read from the bottom upwards. Lithium "
                    "is the one at the top"},
            {"text": "Lithium, potassium, sodium, caesium, rubidium, francium",
             "correct": False,
             "why": "Two pairs have been swapped. Sodium comes directly below "
                    "lithium, and rubidium directly below potassium"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e09",
        "band": "easier",
        "text": "A group 1 atom has exactly one electron in its outer shell. "
                "What happens to that electron when the metal reacts?",
        "options": [
            {"text": "It is pulled in closer to the nucleus",
             "correct": False,
             "why": "Reacting is not a change of distance. The electron "
                    "leaves the atom altogether"},
            {"text": "It is joined by a second electron from the water",
             "correct": False,
             "why": "A group 1 atom never picks up an extra electron from "
                    "anywhere. It parts with the one it has"},
            {"text": "It is lost from the atom",
             "correct": True},
            {"text": "It stays exactly where it started",
             "correct": False,
             "why": "If nothing happened to it there would be no reaction. "
                    "Losing it is what reacting means here"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e10",
        "band": "easier",
        "text": "Which word equation describes potassium reacting with "
                "water?",
        "options": [
            {"text": "potassium + water → potassium oxide + hydrogen",
             "correct": False,
             "why": "The oxide is what forms in dry air. In water the metal "
                    "makes a hydroxide"},
            {"text": "potassium + water → potassium chloride + hydrogen",
             "correct": False,
             "why": "There is no chlorine anywhere in the reaction, so no "
                    "chloride can be made"},
            {"text": "potassium + water → potassium hydroxide + oxygen",
             "correct": False,
             "why": "No oxygen is given off. The gas that streams away burns, "
                    "and oxygen does not burn"},
            {"text": "potassium + water → potassium hydroxide + hydrogen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e11",
        "band": "easier",
        "text": "A lit splint is held to the gas coming off a group 1 metal "
                "reacting with water. What happens?",
        "options": [
            {"text": "It is put out at once, as though smothered",
             "correct": False,
             "why": "This gas burns readily. It does not smother a flame, it "
                    "feeds one"},
            {"text": "It flares brighter and the splint relights",
             "correct": False,
             "why": "A splint relighting is the test for oxygen, and oxygen "
                    "is not what comes off here"},
            {"text": "It burns with a sharp squeaky pop", "correct": True},
            {"text": "It burns quietly with a bright green flame",
             "correct": False,
             "why": "Neither the colour nor the quiet matches. The test for "
                    "this gas is one you hear"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e12",
        "band": "easier",
        "text": "Universal indicator is stirred into the trough water before "
                "any metal is added, and it is green. What does green show "
                "about the water at that point?",
        "options": [
            {"text": "It is alkaline", "correct": False,
             "why": "An alkaline solution takes universal indicator to blue "
                    "or purple, never to green"},
            {"text": "It is neutral", "correct": True},
            {"text": "It is acidic", "correct": False,
             "why": "An acidic solution takes universal indicator to yellow, "
                    "orange or red, never to green"},
            {"text": "It already holds a dissolved metal", "correct": False,
             "why": "A dissolved group 1 metal would have made the water "
                    "alkaline, and the indicator would not be green"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e13",
        "band": "easier",
        "text": "A lithium compound is held in a hot flame. What colour does "
                "the flame turn?",
        "options": [
            {"text": "Crimson red", "correct": True},
            {"text": "Lilac", "correct": False,
             "why": "Lilac belongs to a different group 1 metal, and the two "
                    "are told apart by exactly this test"},
            {"text": "Orange-yellow", "correct": False,
             "why": "Orange-yellow belongs to another group 1 metal, and it "
                    "is the commonest contamination in a flame test"},
            {"text": "Bright green", "correct": False,
             "why": "No group 1 metal gives a green flame, so green would "
                    "rule the whole group out"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e14",
        "band": "easier",
        "text": "Potassium's reaction with water ends in a flame above the "
                "surface. What colour is that flame?",
        "options": [
            {"text": "Crimson", "correct": False,
             "why": "Crimson belongs to a different member of group 1, one "
                    "whose reaction never catches fire at all"},
            {"text": "Blue", "correct": False,
             "why": "Hydrogen burning on its own is very nearly colourless. "
                    "The colour here is put there by the metal"},
            {"text": "Green", "correct": False,
             "why": "No group 1 metal colours a flame green, so green would "
                    "rule the whole group out"},
            {"text": "Lilac", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e15",
        "band": "easier",
        "text": "A group 1 metal can be cut through with an ordinary knife. "
                "What does that tell you about it?",
        "options": [
            {"text": "It is far softer than most metals", "correct": True},
            {"text": "It is not a metal", "correct": False,
             "why": "Softness is a physical property. It still conducts and "
                    "still shines when cut, so it is a metal"},
            {"text": "It is liquid, not solid", "correct": False,
             "why": "Anything you can cut with a knife is a solid. Being soft "
                    "is not the same as being molten"},
            {"text": "Its melting point is high", "correct": False,
             "why": "Group 1 melting points are unusually low for metals "
                    "rather than high"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e16",
        "band": "easier",
        "text": "Which observation is seen with lithium, sodium and "
                "potassium alike when a piece of each is put on water?",
        "options": [
            {"text": "Melting into a ball within a second or two of landing",
             "correct": False,
             "why": "The one at the top of the three stays a solid lump the "
                    "whole way through"},
            {"text": "Sinking to the bottom of the trough", "correct": False,
             "why": "All three are less dense than water, and not one of them "
                    "sinks"},
            {"text": "Fizzing as gas streams off it", "correct": True},
            {"text": "A flame burning above the metal", "correct": False,
             "why": "Only the most vigorous of the three sets its own gas "
                    "alight. The gentlest never does"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e17",
        "band": "easier",
        "text": "The water in the trough is measurably warmer after a group 1 "
                "metal has finished reacting in it. What word describes a "
                "reaction that gives out heat?",
        "options": [
            {"text": "Endothermic", "correct": False,
             "why": "An endothermic reaction takes heat in, and the water "
                    "would have ended up cooler"},
            {"text": "Electrolytic", "correct": False,
             "why": "Electrolytic means split apart by electricity, and no "
                    "electricity is used here"},
            {"text": "Neutral", "correct": False,
             "why": "Neutral describes a pH of 7. It says nothing about "
                    "energy"},
            {"text": "Exothermic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e18",
        "band": "easier",
        "text": "Potassium melts at 63 °C. A trough of water is at 20 °C. By "
                "how many degrees must the reaction raise the potassium's "
                "temperature before it melts?",
        "options": [
            {"text": "83 °C", "correct": False,
             "why": "That adds the two figures. The metal starts at 20 °C, "
                    "not at 0 °C"},
            {"text": "43 °C", "correct": True},
            {"text": "63 °C", "correct": False,
             "why": "That is the melting point itself, not the rise needed "
                    "from a start of 20 °C"},
            {"text": "20 °C", "correct": False,
             "why": "That is where the metal starts, not how far it has to be "
                    "taken"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e19",
        "band": "easier",
        "text": "A small piece of lithium is dropped into water. Which "
                "description matches what happens?",
        "options": [
            {"text": "It melts into a ball and skates about the surface, fizzing",
             "correct": False,
             "why": "Lithium stays solid throughout. Melting takes a fiercer "
                    "reaction than lithium's"},
            {"text": "It floats and fizzes steadily for nearly a minute",
             "correct": True},
            {"text": "It sets its own gas alight and burns with a flame",
             "correct": False,
             "why": "Lithium's reaction is far too gentle for that. Nothing "
                    "catches fire"},
            {"text": "It sinks and fizzes quietly on the bottom",
             "correct": False,
             "why": "Lithium is less dense than water and stays on the "
                    "surface from start to finish"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e20",
        "band": "easier",
        "text": "Compounds of which group 1 element are an essential "
                "ingredient of fertilisers?",
        "options": [
            {"text": "Caesium", "correct": False,
             "why": "Caesium is rare, expensive and far too violent to spread "
                    "on a field"},
            {"text": "Francium", "correct": False,
             "why": "Francium is radioactive and so scarce that no visible "
                    "piece has ever been gathered"},
            {"text": "Rubidium", "correct": False,
             "why": "Rubidium has no part in growing crops. It is a "
                    "laboratory metal, not an agricultural one"},
            {"text": "Potassium", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e21",
        "band": "easier",
        "text": "Why is only a piece about the size of a grain of rice used "
                "in a group 1 water demonstration?",
        "options": [
            {"text": "More metal means more energy released, and more danger",
             "correct": True},
            {"text": "A larger piece would sink",
             "correct": False,
             "why": "Floating depends on density, not on size. A larger piece "
                    "floats just as well"},
            {"text": "It would react too slowly to see",
             "correct": False,
             "why": "More metal does not slow the reaction. It makes it "
                    "faster and fiercer"},
            {"text": "The metal is too costly to use in bulk",
             "correct": False,
             "why": "Sodium is one of the cheapest metals there is. The "
                    "reason for a small piece is safety"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e22",
        "band": "easier",
        "text": "What does the word reactivity mean?",
        "options": [
            {"text": "How heavy one atom is compared with another",
             "correct": False,
             "why": "That is atomic mass. A heavy element is not "
                    "automatically a reactive one"},
            {"text": "How readily and how vigorously an element reacts",
             "correct": True},
            {"text": "How hard an element is to scratch or to cut",
             "correct": False,
             "why": "That is hardness, which is a physical property and no "
                    "guide to how an element reacts"},
            {"text": "How much of an element there is in the Earth's crust "
                     "overall",
             "correct": False,
             "why": "That is abundance. Sodium is abundant and reactive, and "
                    "gold is scarce and unreactive"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e23",
        "band": "easier",
        "text": "Lithium has a density of 0.53 g/cm³. What is the mass of a "
                "piece of lithium whose volume is 10 cm³?",
        "options": [
            {"text": "0.053 g", "correct": False,
             "why": "That divides by the volume. Mass is density multiplied "
                    "by volume"},
            {"text": "10.53 g", "correct": False,
             "why": "That adds the volume to the density. Two different "
                    "quantities cannot be added"},
            {"text": "5.3 g", "correct": True},
            {"text": "18.9 g", "correct": False,
             "why": "That divides the volume by the density, which gives no "
                    "useful quantity at all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e24",
        "band": "easier",
        "text": "A piece of a group 1 metal left out in the open air becomes "
                "coated in a dull layer. What kind of compound is that layer?",
        "options": [
            {"text": "A hydroxide", "correct": False,
             "why": "The hydroxide is what the metal makes with water, not "
                    "with dry air"},
            {"text": "A chloride", "correct": False,
             "why": "There is no chlorine in ordinary air, so no chloride can "
                    "be formed"},
            {"text": "A carbonate", "correct": False,
             "why": "A carbonate would need carbon dioxide, and the dulling "
                    "happens far too fast for that"},
            {"text": "An oxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e25",
        "band": "easier",
        "text": "Potassium can crack or spit at the very end of its reaction "
                "with water. What does that mean for the safety screen?",
        "options": [
            {"text": "It stays up until the fizzing has completely stopped",
             "correct": True},
            {"text": "It comes down once the metal has gone in",
             "correct": False,
             "why": "The most dangerous moment can arrive at the end, long "
                    "after the metal went in"},
            {"text": "It is needed only while the metal is cut",
             "correct": False,
             "why": "Cutting is not the hazardous step. The reaction with "
                    "water is"},
            {"text": "It is needed for sodium but not potassium",
             "correct": False,
             "why": "Potassium is the more violent of those two and needs the "
                    "screen at least as much"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e26",
        "band": "easier",
        "text": "Lithium melts at 180 °C, sodium at 98 °C and potassium at "
                "63 °C. What is the trend in melting point going down "
                "group 1?",
        "options": [
            {"text": "It rises", "correct": False,
             "why": "The three figures run downwards from 180 °C to 63 °C, so "
                    "the trend goes the other way"},
            {"text": "It stays the same", "correct": False,
             "why": "180 °C, 98 °C and 63 °C are three very different "
                    "temperatures"},
            {"text": "It rises and then falls", "correct": False,
             "why": "Each value is lower than the one above it, so there is "
                    "no turning point anywhere"},
            {"text": "It falls", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e27",
        "band": "easier",
        "text": "A ball of molten sodium whizzes round and round the water "
                "surface. What is pushing it along?",
        "options": [
            {"text": "The gas streaming off it", "correct": True},
            {"text": "A current in the water", "correct": False,
             "why": "The water in a trough is standing still and nothing is "
                    "stirring it"},
            {"text": "Heat rising from the metal", "correct": False,
             "why": "Rising heat travels upwards and cannot push a ball "
                    "sideways across a surface"},
            {"text": "The indicator dissolved in the water", "correct": False,
             "why": "The indicator only changes colour. It takes no part in "
                    "the reaction itself"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e28",
        "band": "easier",
        "text": "How does the reactivity of the group 1 metals compare with "
                "that of most other metals?",
        "options": [
            {"text": "They are far less reactive", "correct": False,
             "why": "Most metals will sit on a shelf in air for years. No "
                    "group 1 metal can"},
            {"text": "They are about the same", "correct": False,
             "why": "Ordinary metals do not fizz apart in cold water, and "
                    "every group 1 metal does"},
            {"text": "It depends on the temperature", "correct": False,
             "why": "They outdo ordinary metals in cold water, in warm water "
                    "and in air alike"},
            {"text": "They are far more reactive", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e29",
        "band": "easier",
        "text": "Can a class carry out the group 1 and water reactions "
                "themselves, at their own benches?",
        "options": [
            {"text": "Yes, so long as everyone wears eye protection",
             "correct": False,
             "why": "Eye protection is necessary but nowhere near enough for "
                    "a reaction this vigorous"},
            {"text": "Yes, so long as only lithium is used and the pieces are "
                     "small",
             "correct": False,
             "why": "Lithium is the gentlest of the three and is still "
                    "demonstrated, never handed out. A small piece lowers the "
                    "hazard without removing it"},
            {"text": "No — it is a teacher demonstration only",
             "correct": True},
            {"text": "No — the metals cost far too much to hand round a class",
             "correct": False,
             "why": "Sodium is one of the cheapest metals there is. It is the "
                    "hazard, not the cost, that keeps this a demonstration"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e30",
        "band": "easier",
        "text": "Group 1 shows a clear trend in reactivity. What does knowing "
                "a trend let you do?",
        "options": [
            {"text": "Measure an element without any apparatus",
             "correct": False,
             "why": "A trend predicts. It never measures, and the prediction "
                    "still has to be tested"},
            {"text": "Prove that a prediction must be correct",
             "correct": False,
             "why": "A trend supports a prediction. Only an experiment can "
                    "show that it was right"},
            {"text": "Explain why the trend is there at all",
             "correct": False,
             "why": "The trend is the pattern itself. The reason behind it is "
                    "a separate question"},
            {"text": "Describe an element you have never seen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e31",
        "band": "easier",
        "text": "Caesium melts at 28 °C. Would a lump of caesium be solid or "
                "liquid in a room at 35 °C?",
        "options": [
            {"text": "Solid, because every known metal is a solid at ordinary "
                     "room temperature",
             "correct": False,
             "why": "Mercury is a liquid metal at room temperature, and "
                    "caesium melts at only 28 °C"},
            {"text": "Liquid, because the room is above its melting point",
             "correct": True},
            {"text": "Solid, because 35 °C cannot melt any metal at all",
             "correct": False,
             "why": "35 °C is seven degrees above caesium's melting point of "
                    "28 °C"},
            {"text": "Liquid, because metals melt as soon as they are warmed",
             "correct": False,
             "why": "A metal melts once it reaches its own melting point, not "
                    "as soon as it is warmed at all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e32",
        "band": "easier",
        "text": "Why must a piece of a group 1 metal never be picked up with "
                "bare fingers?",
        "options": [
            {"text": "The moisture on skin would react with it",
             "correct": True},
            {"text": "The metal would stain the skin a dull grey",
             "correct": False,
             "why": "Staining is not the hazard. A reaction happening on the "
                    "skin itself is"},
            {"text": "The warmth of a hand would boil the metal",
             "correct": False,
             "why": "No group 1 metal boils anywhere near the temperature of "
                    "a human hand"},
            {"text": "Fingerprints would spoil the shine on the cut surface",
             "correct": False,
             "why": "The cut surface dulls in air whatever you do. Tongs are "
                    "used for safety"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s08",
        "band": "standard",
        "text": "Rubidium is a group 1 metal. Which word equation describes "
                "it reacting with water?",
        "options": [
            {"text": "rubidium + water → rubidium oxide + hydrogen",
             "correct": False,
             "why": "The oxide is what a group 1 metal makes with air. With "
                    "water it always makes the hydroxide"},
            {"text": "rubidium + water → rubidium hydroxide + hydrogen",
             "correct": True},
            {"text": "rubidium + water → rubidium hydroxide + oxygen",
             "correct": False,
             "why": "The gas released burns readily, and oxygen does not "
                    "burn. No oxygen is set free here"},
            {"text": "rubidium + water → rubidium carbonate + hydrogen",
             "correct": False,
             "why": "A carbonate needs carbon dioxide, and there is no carbon "
                    "anywhere in the trough"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s09",
        "band": "standard",
        "text": "A student says the bubbles rising from a group 1 metal on "
                "water are just trapped air escaping from the metal. Which "
                "observation rules that out?",
        "options": [
            {"text": "The bubbling lasts as long as the metal does and stops "
                     "when it has gone",
             "correct": True},
            {"text": "The metal floats on the surface rather than sinking",
             "correct": False,
             "why": "Floating follows from the metal's density and says "
                    "nothing about where the bubbles come from"},
            {"text": "The metal had been stored under oil beforehand",
             "correct": False,
             "why": "How the metal was stored beforehand tells you nothing "
                    "about what the bubbles are made of"},
            {"text": "The water in the trough ends up warmer",
             "correct": False,
             "why": "A warmer trough shows energy was released. It does not "
                    "identify what is bubbling off"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s10",
        "band": "standard",
        "text": "Lithium fizzes on water for nearly a minute; potassium's "
                "reaction is over in about a second. Equal pieces are used "
                "and both leave the same kind of solution. What does that "
                "difference in time measure?",
        "options": [
            {"text": "How much hydroxide each one makes",
             "correct": False,
             "why": "Equal pieces make comparable amounts. Time taken is no "
                    "measure of how much is produced"},
            {"text": "How strong the alkali that is left behind is",
             "correct": False,
             "why": "Both leave a strongly alkaline solution. Speed is no "
                    "measure of alkalinity"},
            {"text": "How pure each piece of metal was",
             "correct": False,
             "why": "Purity was not varied, and the same difference turns up "
                    "every time the demonstration is run"},
            {"text": "How vigorously the metal reacts", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s11",
        "band": "standard",
        "text": "Lithium's reaction on water is gentle, sodium's melts the "
                "metal, and potassium's ends in flames. Which part of that is "
                "the trend and which part is not?",
        "options": [
            {"text": "The products change; the vigour does not",
             "correct": False,
             "why": "Every one of them makes a hydroxide and the same gas. It "
                    "is the violence that shifts"},
            {"text": "Both the products and the vigour change",
             "correct": False,
             "why": "The products are the same family every time, and that "
                    "sameness is what makes them one group"},
            {"text": "Neither the products nor the vigour changes at all",
             "correct": False,
             "why": "A gentle fizz and a flame are plainly not the same "
                    "thing, so the vigour does change"},
            {"text": "The vigour changes; the products do not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s12",
        "band": "standard",
        "text": "A jar of sodium is found with its lid off and the oil long "
                "since evaporated. The lumps inside are covered in a thick "
                "white crust. What is the crust?",
        "options": [
            {"text": "Dried oil, left behind as the liquid slowly evaporated",
             "correct": False,
             "why": "Evaporating oil leaves no white crust. It is the exposed "
                    "metal that has been attacked"},
            {"text": "Sodium compounds, made by reaction with the air",
             "correct": True},
            {"text": "Sodium metal that has crystallised out of the oil",
             "correct": False,
             "why": "Sodium does not dissolve in the oil, so there is nothing "
                    "for it to crystallise out of"},
            {"text": "Dust that has settled out of the air onto the metal",
             "correct": False,
             "why": "Settled dust wipes off. This layer is the surface of the "
                    "metal itself, turned into compound"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s13",
        "band": "standard",
        "text": "A teacher wants to collect enough of the gas from a group 1 "
                "metal and water to test it. Why is lithium the most "
                "practical of the three to collect it from?",
        "options": [
            {"text": "It is the only one of the three that gives off any gas at all",
             "correct": False,
             "why": "All three give off the same gas. They differ only in how "
                    "fast they hand it over"},
            {"text": "It gives off far more gas than the other two do",
             "correct": False,
             "why": "An equal-sized piece gives a comparable amount. Lithium "
                    "simply releases it more slowly"},
            {"text": "Its reaction is slow and steady enough to collect from",
             "correct": True},
            {"text": "It is the only one safe to handle with bare hands",
             "correct": False,
             "why": "No group 1 metal is handled with bare hands, and lithium "
                    "is no exception"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s14",
        "band": "standard",
        "text": "The solution left in the trough after sodium has reacted is "
                "poured into a dish and the water left to evaporate. A white "
                "solid remains. What is it?",
        "options": [
            {"text": "Sodium hydroxide", "correct": True},
            {"text": "Sodium metal", "correct": False,
             "why": "The metal was used up in the reaction and cannot come "
                    "back by letting water evaporate"},
            {"text": "Sodium oxide", "correct": False,
             "why": "The oxide is what forms in dry air. What dissolved in "
                    "the trough was the hydroxide"},
            {"text": "Nothing is left at all", "correct": False,
             "why": "The dissolved product does not evaporate away with the "
                    "water. It stays in the dish"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s15",
        "band": "standard",
        "text": "Caesium sits below rubidium, which sits below potassium. "
                "Put those three in order of increasing reactivity.",
        "options": [
            {"text": "Caesium, rubidium, potassium", "correct": False,
             "why": "That is the order of decreasing reactivity. The lowest "
                    "member of the group is the fiercest"},
            {"text": "Rubidium, potassium, caesium", "correct": False,
             "why": "Rubidium sits between the other two in the group, so it "
                    "sits between them in reactivity"},
            {"text": "Potassium, rubidium, caesium", "correct": True},
            {"text": "Potassium, caesium, rubidium", "correct": False,
             "why": "Caesium is below rubidium, so caesium comes last rather "
                    "than in the middle"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s16",
        "band": "standard",
        "text": "A teacher wants to show that lithium, sodium and potassium "
                "all leave the same kind of solution behind. What is the "
                "simplest way to show it?",
        "options": [
            {"text": "Hold a lit splint at each trough",
             "correct": False,
             "why": "That tests the gas coming off, which is not the "
                    "solution left behind"},
            {"text": "Weigh each piece before and after",
             "correct": False,
             "why": "Mass shows how much metal reacted, not what kind of "
                    "solution was made"},
            {"text": "Time each of the three reactions",
             "correct": False,
             "why": "Timing measures the vigour, which is the thing that "
                    "differs rather than the thing that is shared"},
            {"text": "Stir universal indicator into all three troughs",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s17",
        "band": "standard",
        "text": "Two completely different sodium compounds are each held in a "
                "hot flame, and both give exactly the same colour. What does "
                "a flame test identify?",
        "options": [
            {"text": "The metal in the compound", "correct": True},
            {"text": "The whole compound", "correct": False,
             "why": "Two different compounds gave one colour, so the colour "
                    "cannot be picking out the compound"},
            {"text": "The non-metal part of the whole compound", "correct": False,
             "why": "The two compounds hold different non-metals and still "
                    "gave the same single colour"},
            {"text": "How reactive the compound is", "correct": False,
             "why": "Colour is no measure of reactivity. It tells you which "
                    "element is present, nothing more"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s18",
        "band": "standard",
        "text": "Lithium's density is 0.53 g/cm³, sodium's is 0.97 g/cm³ and "
                "potassium's is 0.86 g/cm³. Water's is 1.00 g/cm³. What do "
                "those four numbers show?",
        "options": [
            {"text": "Density rises steadily as you go down the group from lithium",
             "correct": False,
             "why": "Potassium's 0.86 g/cm³ is lower than sodium's "
                    "0.97 g/cm³, so the figures do not rise steadily"},
            {"text": "Density falls steadily as you go down the group",
             "correct": False,
             "why": "Sodium's 0.97 g/cm³ is higher than lithium's "
                    "0.53 g/cm³, so the figures do not fall steadily"},
            {"text": "All three float, and the densities run in no one "
                     "direction",
             "correct": True},
            {"text": "All three are denser than water and sink straight to the bottom",
             "correct": False,
             "why": "Every one of the three figures is below 1.00 g/cm³, so "
                    "not one of them sinks"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s19",
        "band": "standard",
        "text": "Sodium is less dense than water, and sodium also reacts "
                "with water. Which of those two facts explains why the "
                "reaction happens on the surface rather than at the bottom?",
        "options": [
            {"text": "How fiercely it reacts", "correct": False,
             "why": "Vigour sets the speed of the reaction, not the place in "
                    "the trough where it happens"},
            {"text": "How dense it is", "correct": True},
            {"text": "Both, equally", "correct": False,
             "why": "Only one of the two fixes the position. It would react "
                    "just as fiercely wherever it sat"},
            {"text": "Neither of them", "correct": False,
             "why": "One of the two does fix it: a solid less dense than "
                    "water cannot sink through it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s20",
        "band": "standard",
        "text": "Why is universal indicator stirred into the trough before "
                "the metal goes in, rather than afterwards?",
        "options": [
            {"text": "So that the indicator itself can react with the metal",
             "correct": False,
             "why": "The indicator takes no part in the reaction. It only "
                    "reports on the solution"},
            {"text": "So that the water is made alkaline in advance",
             "correct": False,
             "why": "Indicator makes nothing alkaline. The product of the "
                    "reaction is what does that"},
            {"text": "So that the colour change is seen as it happens",
             "correct": True},
            {"text": "So that the metal is stopped from floating off anywhere",
             "correct": False,
             "why": "Nothing about the indicator affects where the metal sits "
                    "or how it moves"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s21",
        "band": "standard",
        "text": "A piece of a group 1 metal contains nothing but metal "
                "atoms, yet a gas streams off it the moment it touches "
                "water. Which substance must have supplied the atoms in that "
                "gas?",
        "options": [
            {"text": "The metal", "correct": False,
             "why": "The piece holds only metal atoms, so the gas cannot have "
                    "come out of the metal"},
            {"text": "The air above the trough", "correct": False,
             "why": "The gas appears at the surface of the metal where it "
                    "meets the water, not up in the air"},
            {"text": "The indicator dissolved in the water", "correct": False,
             "why": "The indicator is there in traces and is not used up. It "
                    "only changes colour"},
            {"text": "The water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s22",
        "band": "standard",
        "text": "Potassium's reaction with water ends in flames and "
                "lithium's does not, although the two reactions make the "
                "same products. What makes the difference?",
        "options": [
            {"text": "Potassium makes an extra product, and that extra product "
                     "is flammable",
             "correct": False,
             "why": "Both make a hydroxide and the same gas. The products are "
                    "not where they differ"},
            {"text": "Potassium releases the energy far faster, and so gets "
                     "much hotter",
             "correct": True},
            {"text": "The water used for potassium is warmer to start with",
             "correct": False,
             "why": "The same cold trough is used for both, and the "
                    "difference shows up every single time"},
            {"text": "Lithium's reaction takes energy in from the water rather "
                     "than giving it out",
             "correct": False,
             "why": "Both reactions give energy out. Lithium's simply gives "
                    "it out more slowly"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s23",
        "band": "standard",
        "text": "Rubidium is predicted to be softer to cut than potassium, "
                "though nobody in the room has ever handled any. Which trend "
                "is that prediction built on?",
        "options": [
            {"text": "The group gets harder going down", "correct": False,
             "why": "Lithium is the firmest of them, and every member below "
                    "it cuts more easily still"},
            {"text": "The group gets softer going down", "correct": True},
            {"text": "The atoms get lighter going down", "correct": False,
             "why": "The atoms get heavier going down, and mass is not what "
                    "hardness follows from in any case"},
            {"text": "The group's melting points rise going down",
             "correct": False,
             "why": "They fall going down: 180 °C, then 98 °C, then 63 °C "
                    "through the first three"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s24",
        "band": "standard",
        "text": "A student predicts that francium will be the least reactive "
                "group 1 metal, because it is right at the bottom of the "
                "group. What has gone wrong?",
        "options": [
            {"text": "The trend has been read the wrong way round",
             "correct": True},
            {"text": "Francium is not actually a member of group 1",
             "correct": False,
             "why": "Francium is the last member of group 1, sitting "
                    "directly below caesium"},
            {"text": "Francium is too rare for the trend to apply to it",
             "correct": False,
             "why": "How rare an element is has no bearing on how its atoms "
                    "behave when they do react"},
            {"text": "Nothing — the bottom of a group is always the least "
                     "reactive",
             "correct": False,
             "why": "There is no such rule. In group 1 the member at the "
                    "bottom is the most reactive of the lot"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s25",
        "band": "standard",
        "text": "Every group 1 atom has exactly one outer electron, yet "
                "caesium reacts far more fiercely than lithium. Why does "
                "having the same number of outer electrons not make them "
                "equally reactive?",
        "options": [
            {"text": "What matters is the number of outer electrons, and "
                     "caesium carries more",
             "correct": False,
             "why": "Every group 1 atom has exactly one outer electron, and "
                    "caesium is no exception"},
            {"text": "What matters is the mass, and a heavier atom always "
                     "reacts harder",
             "correct": False,
             "why": "Mass is not what drives a reaction. How the electrons "
                    "are arranged is"},
            {"text": "What matters is how tightly that one electron is held",
             "correct": True},
            {"text": "What matters is the size of the piece, and caesium is "
                     "used in bigger ones",
             "correct": False,
             "why": "The comparison is made with equal pieces, and the "
                    "difference is still there"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s26",
        "band": "standard",
        "text": "Sodium's reaction with water can finish with an orange "
                "flame above the trough. What is burning?",
        "options": [
            {"text": "The water at the very surface of the trough",
             "correct": False,
             "why": "Water does not burn. It is what you get when hydrogen "
                    "burns, not a fuel"},
            {"text": "The indicator that was dissolved in the water",
             "correct": False,
             "why": "The indicator is there in traces and takes no part in "
                    "the reaction at all"},
            {"text": "The trough itself, made hot by the reaction inside it",
             "correct": False,
             "why": "A trough does not catch fire, and the flame sits above "
                    "the water rather than at the rim"},
            {"text": "The gas the reaction has been giving off",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s27",
        "band": "standard",
        "text": "A piece of lithium fizzes on water until it has completely "
                "disappeared. Has the lithium been destroyed?",
        "options": [
            {"text": "No — its atoms are now in the dissolved product",
             "correct": True},
            {"text": "Yes — it has been used up and no longer exists",
             "correct": False,
             "why": "Atoms are never destroyed in a reaction. They end up in "
                    "a different substance"},
            {"text": "Yes — it has all turned into the gas that bubbled away",
             "correct": False,
             "why": "The gas came from the water. The metal's own atoms "
                    "stayed behind in the solution"},
            {"text": "No — it has sunk to the bottom in tiny pieces",
             "correct": False,
             "why": "The water stays clear and nothing collects below. The "
                    "metal left as a dissolved compound"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s28",
        "band": "standard",
        "text": "Which single observation in the trough is the direct "
                "evidence that a gas is being produced?",
        "options": [
            {"text": "Bubbles streaming off the metal", "correct": True},
            {"text": "Colour appearing in the indicator", "correct": False,
             "why": "The colour change reports on what is dissolved in the "
                    "water, not on any gas"},
            {"text": "Steady shrinking of the piece of metal",
             "correct": False,
             "why": "Shrinking shows the metal is being used up, whatever it "
                    "is being turned into"},
            {"text": "Warming of the water in the trough", "correct": False,
             "why": "A temperature rise shows energy was released, not that "
                    "anything gaseous was made"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s29",
        "band": "standard",
        "text": "Caesium melts at 28 °C. Explain why a piece of caesium "
                "dropped onto cold water would almost certainly be molten "
                "within an instant.",
        "options": [
            {"text": "The water in the trough is already warmer than 28 °C",
             "correct": False,
             "why": "The trough holds cold tap water, which sits well below "
                    "28 °C"},
            {"text": "It starts a few degrees below 28 °C and the reaction "
                     "heats it fast",
             "correct": True},
            {"text": "Caesium takes heat out of the water and so melts "
                     "itself",
             "correct": False,
             "why": "The reaction gives heat out rather than taking it in. "
                    "The trough ends up warmer"},
            {"text": "Caesium dissolves rather than melts, which looks the "
                     "same",
             "correct": False,
             "why": "It genuinely melts. The reaction releases enough heat to "
                    "carry it past 28 °C"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s30",
        "band": "standard",
        "text": "A teacher demonstrates lithium first, then sodium, then "
                "potassium. Why is that a sensible order?",
        "options": [
            {"text": "It runs from the heaviest of the metals to the lightest",
             "correct": False,
             "why": "Lithium is the lightest of the three, so the order runs "
                    "the other way round"},
            {"text": "It runs from the cheapest metal to the priciest",
             "correct": False,
             "why": "Cost is not what sets the order. The danger of each "
                    "reaction is"},
            {"text": "It runs from the gentlest reaction to the fiercest",
             "correct": True},
            {"text": "It runs from the most reactive metal to the least",
             "correct": False,
             "why": "Lithium is the least reactive of the three, so that order "
                    "runs the other way round"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s31",
        "band": "standard",
        "text": "Lithium is the least reactive metal in group 1, and it is "
                "still kept sealed away from air and from water. Why?",
        "options": [
            {"text": "Air attacks lithium and no other member of the whole "
                     "group",
             "correct": False,
             "why": "Air attacks every member of the group, and the ones "
                    "below lithium faster still"},
            {"text": "Left in the open, lithium would slowly evaporate away",
             "correct": False,
             "why": "It is a solid that melts at 180 °C. Nothing about it "
                    "evaporates in a storeroom"},
            {"text": "Being radioactive, lithium has to be kept behind lead "
                     "shielding",
             "correct": False,
             "why": "Lithium is not radioactive. It is sealed away because "
                    "it is chemically attacked"},
            {"text": "Even the gentlest member of the group is attacked by "
                     "both",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s32",
        "band": "standard",
        "text": "The solution left in the trough conducts electricity and "
                "reads pH 13. Which single product of the reaction explains "
                "both of those results?",
        "options": [
            {"text": "The gas given off during the reaction", "correct": False,
             "why": "The gas leaves the trough altogether. Nothing that has "
                    "gone can be read by a pH probe"},
            {"text": "The unreacted metal left over", "correct": False,
             "why": "Nothing is left over once the fizzing stops, and the "
                    "metal itself does not dissolve"},
            {"text": "The universal indicator that was added to the water",
             "correct": False,
             "why": "Indicator is present in traces, reports a colour, and "
                    "does not itself make a solution alkaline"},
            {"text": "The dissolved metal hydroxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h08",
        "band": "harder",
        "text": "A group 1 metal and some water are sealed in a strong tube "
                "with a barrier between them. The tube is weighed, the "
                "barrier is broken so the reaction runs, and the tube is "
                "weighed again. What does the balance read?",
        "options": [
            {"text": "Less, because a gas was produced inside",
             "correct": False,
             "why": "The gas is still inside the sealed tube, so not one atom "
                    "of it has left the balance"},
            {"text": "Exactly what it read before", "correct": True},
            {"text": "More — the metal has turned into a compound inside",
             "correct": False,
             "why": "Nothing came in from outside. The atoms already present "
                    "were only rearranged"},
            {"text": "Less than it read before",
             "correct": False,
             "why": "Used up means turned into something else, not destroyed. "
                    "Its atoms are still in the tube"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h09",
        "band": "harder",
        "text": "Francium is so rare and so radioactive that nobody has ever "
                "collected a visible piece of it, yet books state that it is "
                "the most reactive metal in group 1. What does that statement "
                "rest on?",
        "options": [
            {"text": "A direct measurement made on a weighed sample",
             "correct": False,
             "why": "No weighable sample has ever existed, so no such "
                    "measurement can ever have been made"},
            {"text": "The fact that francium has the heaviest atoms in the "
                     "group",
             "correct": False,
             "why": "Mass is not what sets reactivity. The trend turns on "
                    "where the outer electron sits"},
            {"text": "A rule that the last element in any group is the most "
                     "reactive",
             "correct": False,
             "why": "There is no such rule. A direction has to be established "
                    "for each group separately"},
            {"text": "The group's trend, extended one step further",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h10",
        "band": "harder",
        "text": "Two predictions are made about caesium: that it will float "
                "on water, and that its reaction will be more violent than "
                "potassium's. Which of the two is the safer prediction?",
        "options": [
            {"text": "Floating, because every member already does it",
             "correct": True},
            {"text": "The violence, because a trend is always stronger "
                     "evidence than a shared property",
             "correct": False,
             "why": "The trend is being pushed past its last measured member. "
                    "A property every member already shows is not"},
            {"text": "Both equally, because both of them come from the same "
                     "group",
             "correct": False,
             "why": "Belonging to a group is not what makes a prediction "
                    "safe. How far past the evidence it reaches is"},
            {"text": "Neither, because caesium is never demonstrated in a "
                     "school",
             "correct": False,
             "why": "Evidence does not have to come from a school laboratory "
                    "in order to count as evidence"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h11",
        "band": "harder",
        "text": "A student plans to compare how vigorously lithium, sodium "
                "and potassium react with water. Which variable matters most "
                "to keep the same?",
        "options": [
            {"text": "The colour of the indicator that is added",
             "correct": False,
             "why": "One indicator is used throughout and it reads the same "
                    "scale whatever is dissolved in it"},
            {"text": "The order in which the three metals are run through",
             "correct": False,
             "why": "Each trough stands on its own. The order changes nothing "
                    "about any single reaction"},
            {"text": "The size of the piece used each time", "correct": True},
            {"text": "The shape of the trough that is used",
             "correct": False,
             "why": "The shape of the container has no effect on how fiercely "
                    "the metal inside it reacts"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h12",
        "band": "harder",
        "text": "A student times the three reactions and records lithium at "
                "55 s, sodium at 4 s and potassium at 1 s. Can those figures "
                "be used to work out how long rubidium's reaction will last?",
        "options": [
            {"text": "Yes — the times quarter each step, so rubidium takes "
                     "0.25 s",
             "correct": False,
             "why": "55, 4 and 1 do not quarter. No arithmetic pattern runs "
                    "through those three figures"},
            {"text": "Yes — take off the same amount again, so rubidium "
                     "takes 0 s",
             "correct": False,
             "why": "A reaction cannot take no time at all, which shows the "
                    "subtraction has no meaning"},
            {"text": "No — a timing is never evidence about anything",
             "correct": False,
             "why": "The timings are good evidence for the direction of the "
                    "trend. They simply give no value to extend"},
            {"text": "No — they give the direction but no value to extend",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h13",
        "band": "harder",
        "text": "Lithium tarnishes in air over minutes, sodium in seconds "
                "and potassium almost instantly. The water trough had already "
                "put the three in that same order. What does the second set "
                "of observations add?",
        "options": [
            {"text": "That the order belongs to the metals, not the water",
             "correct": True},
            {"text": "That the metals react faster with air than they ever do "
                     "with cold water",
             "correct": False,
             "why": "The two sets are being compared for their order, not for "
                    "which attacker is quicker"},
            {"text": "That air and water are chemically the same kind of "
                     "substance",
             "correct": False,
             "why": "They are quite different substances. It is the metals "
                    "that are behaving consistently"},
            {"text": "Nothing, because tarnishing is not a chemical "
                     "reaction",
             "correct": False,
             "why": "Tarnishing is a reaction. The shiny metal is being "
                    "turned into a dull compound"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h14",
        "band": "harder",
        "text": "A piece of sodium melts during its reaction with water "
                "while a piece of lithium in an identical trough does not. A "
                "student concludes that sodium's reaction must release more "
                "energy in total. Is that justified?",
        "options": [
            {"text": "Yes — melting is direct proof that more energy was "
                     "released",
             "correct": False,
             "why": "Melting shows a temperature was reached, and what "
                    "temperature is needed differs between the two metals"},
            {"text": "No — two things differ at once, the melting points "
                     "among them",
             "correct": True},
            {"text": "Yes — the same trough was used, so nothing else could "
                     "possibly differ",
             "correct": False,
             "why": "The metals themselves differ, and one of the things that "
                    "differs is where each one melts"},
            {"text": "No — neither reaction releases any energy at all",
             "correct": False,
             "why": "Both release energy, which is why the trough is left "
                    "warmer than it started"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h15",
        "band": "harder",
        "text": "A newly made element is claimed to belong in group 1, one "
                "place below francium. Which single observation would count "
                "most strongly against the claim?",
        "options": [
            {"text": "It sits in water without reacting", "correct": True},
            {"text": "It is softer than any element made before it",
             "correct": False,
             "why": "Getting softer further down is exactly what group 1 "
                    "predicts, so that supports the claim"},
            {"text": "Its solution with water turns universal indicator purple",
             "correct": False,
             "why": "That is precisely what a group 1 metal does, so it "
                    "supports the claim rather than damaging it"},
            {"text": "It reacts with water faster than caesium does",
             "correct": False,
             "why": "Beating the member above it is what the trend predicts, "
                    "so that fits the claim too"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h16",
        "band": "harder",
        "text": "No group 1 metal occurs as the metal in the ground, yet "
                "their compounds are among the commonest substances on Earth. "
                "What must be true of those compounds?",
        "options": [
            {"text": "They break down slowly on their own into the metal",
             "correct": False,
             "why": "If they did, lumps of the metal would turn up in the "
                    "ground, and none ever has"},
            {"text": "They hold no group 1 atoms, only the metal's name",
             "correct": False,
             "why": "They do hold the metal's atoms. That is precisely why "
                    "the metal can be got out of them"},
            {"text": "They form only where the metal has been mined first",
             "correct": False,
             "why": "They are natural and everywhere, and were there long "
                    "before anybody mined anything"},
            {"text": "They are more stable than the metal, which has to be "
                     "forced out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h17",
        "band": "harder",
        "text": "Lithium is in the battery of nearly every phone, and "
                "lithium also reacts fiercely with water. A student says the "
                "two facts have nothing to do with one another. Evaluate "
                "that.",
        "options": [
            {"text": "Right — a battery is physics and a reaction is "
                     "chemistry",
             "correct": False,
             "why": "A battery works by moving electrons about, which is the "
                    "very property the reaction with water uses"},
            {"text": "Wrong — both rest on how readily lithium parts with an "
                     "electron",
             "correct": True},
            {"text": "Right — the battery holds a compound and the reaction "
                     "uses the metal",
             "correct": False,
             "why": "The connection is the behaviour of the atom, and that is "
                    "the same whichever form it is in"},
            {"text": "Wrong — anything that reacts with water can be made "
                     "into a battery",
             "correct": False,
             "why": "Plenty of substances react with water and make no useful "
                    "battery whatsoever"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h18",
        "band": "harder",
        "text": "A student says: potassium reacts with water faster than "
                "sodium does, so potassium hydroxide must be a stronger "
                "alkali than sodium hydroxide. Evaluate that.",
        "options": [
            {"text": "Right — a faster reaction always leaves a more "
                     "concentrated solution",
             "correct": False,
             "why": "Speed is not concentration. Equal pieces leave "
                    "comparable amounts dissolved however fast they go"},
            {"text": "Right — the more reactive metal always makes the "
                     "stronger alkali",
             "correct": False,
             "why": "There is no such rule. The trend is in how the metal "
                    "behaves, not in what its product is like"},
            {"text": "Wrong — how fast the metal reacts says nothing about "
                     "its product",
             "correct": True},
            {"text": "Wrong — potassium does not react faster than sodium "
                     "does",
             "correct": False,
             "why": "It does react faster. The fault lies in what the student "
                    "concluded from that"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h19",
        "band": "harder",
        "text": "The trough demonstration is repeated with water at 40 °C "
                "instead of cold water. All three reactions go faster, and "
                "the order between the three is unchanged. Why?",
        "options": [
            {"text": "Warming speeds every reaction; the order comes from "
                     "the atoms",
             "correct": True},
            {"text": "Warming has an effect on only the fastest of the three",
             "correct": False,
             "why": "All three went faster, which is exactly what the "
                    "observation reports"},
            {"text": "The order is set by the water, and the water was the "
                     "same each time",
             "correct": False,
             "why": "The water was warmer and the order still held, so the "
                    "order cannot be coming from the water"},
            {"text": "Warmer water makes all three metals equally reactive",
             "correct": False,
             "why": "If it did, the three reactions would have become "
                    "indistinguishable, and they did not"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h20",
        "band": "harder",
        "text": "A student argues that potassium's flame in the trough is a "
                "different colour from sodium's, and that this proves "
                "potassium is the more reactive of the two. Evaluate that.",
        "options": [
            {"text": "Right — colour measures how much energy was released",
             "correct": False,
             "why": "The colour comes from which element is present, not from "
                    "the energy the reaction gave out"},
            {"text": "Right — the more reactive metal always gives the "
                     "brighter colour",
             "correct": False,
             "why": "There is no such rule. Each element has its own colour "
                    "whatever its reactivity"},
            {"text": "Wrong — the two flames are in fact the same colour",
             "correct": False,
             "why": "They are genuinely different colours. The fault is in "
                    "the conclusion drawn from that"},
            {"text": "Wrong — a flame colour names an element, it does not "
                     "rank it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h21",
        "band": "harder",
        "text": "In one school the gas above a piece of sodium catches fire "
                "and in another it does not, with the same apparatus and the "
                "same cold tap water. Which is the most likely reason?",
        "options": [
            {"text": "The two pieces were not the same size", "correct": True},
            {"text": "One of the two schools used a different element by "
                     "mistake",
             "correct": False,
             "why": "The same metal was used in both, and the same metal can "
                    "go either way from one run to the next"},
            {"text": "One school's tap water was chemically different",
             "correct": False,
             "why": "Both used cold tap water, and the difference turns up "
                    "with water from the same tap"},
            {"text": "The gas is only flammable on some days",
             "correct": False,
             "why": "It is the same substance every time and it is always "
                    "flammable"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h22",
        "band": "harder",
        "text": "Rubidium is expensive and almost never demonstrated in "
                "schools. Does that weaken the claim that rubidium reacts "
                "with water more violently than potassium does?",
        "options": [
            {"text": "Yes — a claim no school has seen is not scientific",
             "correct": False,
             "why": "Whether a school has watched it has no bearing on "
                    "whether the evidence exists"},
            {"text": "Yes — cost is a reason to doubt any claim about an "
                     "element",
             "correct": False,
             "why": "Cost decides who can afford to do the experiment, not "
                    "what the experiment shows"},
            {"text": "No — the claim rests on the trend and on work done "
                     "elsewhere",
             "correct": True},
            {"text": "No — a claim that follows from a group needs no "
                     "evidence",
             "correct": False,
             "why": "A prediction from a group still has to be tested, and "
                    "rubidium's has been tested"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h23",
        "band": "harder",
        "text": "Universal indicator is added to a trough only after a "
                "group 1 metal has completely finished reacting, and it "
                "still turns purple. Why does that still count as evidence "
                "about the reaction?",
        "options": [
            {"text": "Because the indicator reacts with the leftover metal",
             "correct": False,
             "why": "There is no metal left. The colour comes from what "
                    "dissolved while the reaction was running"},
            {"text": "Because the indicator is purple in any water at all",
             "correct": False,
             "why": "It is green in plain water. Purple means something "
                    "alkaline is dissolved in it"},
            {"text": "It does not count, because the reaction was over",
             "correct": False,
             "why": "The evidence is the product left behind, and that "
                    "product does not vanish when the fizzing stops"},
            {"text": "The product stayed dissolved after the metal had gone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h24",
        "band": "harder",
        "text": "A small piece of caesium dropped into water can shatter the "
                "container. Explain that in terms of both how much energy is "
                "released and how quickly.",
        "options": [
            {"text": "A large amount of energy arrives in a very short time",
             "correct": True},
            {"text": "A large amount of energy arrives over a long period",
             "correct": False,
             "why": "Energy spread over a long period warms the water "
                    "gradually rather than breaking anything"},
            {"text": "A small amount of energy arrives in a very short time",
             "correct": False,
             "why": "A small amount would break nothing, however quickly it "
                    "turned up"},
            {"text": "The container is dissolved chemically by the product that "
                     "forms",
             "correct": False,
             "why": "The container breaks at once, far faster than any "
                    "chemical attack on it could work"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h25",
        "band": "harder",
        "text": "Lithium, sodium, potassium, rubidium and caesium all make a "
                "hydroxide and the same gas with water, however much else "
                "changes. What does that constancy tell you about their "
                "atoms?",
        "options": [
            {"text": "Each carries the same number of shells altogether",
             "correct": False,
             "why": "The number of shells rises going down the group, which "
                    "is why the atoms get bigger"},
            {"text": "Each has the same one outer electron to hand over",
             "correct": True},
            {"text": "Each has an outer shell that is already full",
             "correct": False,
             "why": "An atom with nothing to give away would not react at "
                    "all, and these react with cold water"},
            {"text": "Each has the same mass as the others",
             "correct": False,
             "why": "Their masses are all different, and they rise steadily "
                    "going down the group"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h26",
        "band": "harder",
        "text": "Two pieces of sodium, one of 0.1 g and one of 0.5 g, are "
                "dropped into two identical troughs. Which would differ "
                "between the two troughs and which would not?",
        "options": [
            {"text": "The products would differ; the vigour would not",
             "correct": False,
             "why": "Both make the same hydroxide and the same gas. Size "
                    "changes how hard the reaction is pushed"},
            {"text": "Neither of them would differ in any way",
             "correct": False,
             "why": "Five times the metal releases far more energy, and the "
                    "reaction is plainly fiercer for it"},
            {"text": "Both would differ, since more metal makes new products",
             "correct": False,
             "why": "More of a reactant makes more of the same products. It "
                    "never makes different ones"},
            {"text": "The vigour would differ; the products would not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h27",
        "band": "harder",
        "text": "Sodium melts at 98 °C and it melts during its reaction with "
                "water. A student concludes that sodium must melt whenever it "
                "reacts with anything at all. Evaluate that.",
        "options": [
            {"text": "Right — 98 °C is low enough for any reaction to reach "
                     "it",
             "correct": False,
             "why": "Plenty of reactions release their energy far too slowly "
                    "to raise a metal by that much"},
            {"text": "Wrong — it melts only when a reaction is fast enough "
                     "to get there",
             "correct": True},
            {"text": "Right — a metal always melts at the start of any "
                     "reaction",
             "correct": False,
             "why": "Most metals react without melting at all. Melting is not "
                    "part of what reacting means"},
            {"text": "Wrong — sodium does not really melt, it only looks "
                     "like it",
             "correct": False,
             "why": "It genuinely melts into a ball. The fault is in "
                    "stretching that to every reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h28",
        "band": "harder",
        "text": "A student explains the group 1 trend by writing: the atoms "
                "get bigger going down the group, so the outer electron is "
                "further from the nucleus. What has to be added for that to "
                "be a complete explanation?",
        "options": [
            {"text": "That a bigger atom takes up more room in the solid",
             "correct": False,
             "why": "That is true of the atoms' size and says nothing at all "
                    "about how readily an electron is lost"},
            {"text": "That a bigger atom must therefore weigh more",
             "correct": False,
             "why": "Mass is not the missing step. How firmly the electron is "
                    "held is the missing step"},
            {"text": "That the electron moves faster in a bigger atom",
             "correct": False,
             "why": "Speed is not what the explanation turns on. How firmly "
                    "the electron is held is"},
            {"text": "That a more distant electron is held less tightly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h29",
        "band": "harder",
        "text": "In three troughs the indicator turns purple in every one, "
                "but the colour appears fastest in the trough holding "
                "potassium. Is that speed evidence about the alkali or about "
                "the metal?",
        "options": [
            {"text": "About the alkali — a faster colour change means a stronger "
                     "alkali",
             "correct": False,
             "why": "All three leave a strongly alkaline solution. Speed is "
                    "no measure of how strong an alkali is"},
            {"text": "About the metal — how fast it hands its product over",
             "correct": True},
            {"text": "About the indicator — it works faster in some troughs",
             "correct": False,
             "why": "The same indicator is used in all three and responds at "
                    "the same rate in each"},
            {"text": "About neither — a colour change has no timing to read",
             "correct": False,
             "why": "It does have one, and it tracks how quickly the metal is "
                    "getting through its reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h30",
        "band": "harder",
        "text": "Sodium is present in every cell of your body, and a lump of "
                "sodium metal reacts violently with water. Explain how both "
                "of those statements can be true.",
        "options": [
            {"text": "The body's sodium is a different element of the same "
                     "name",
             "correct": False,
             "why": "It is the very same element. What differs is whether it "
                    "is combined with anything"},
            {"text": "The body keeps its sodium dry, so it never gets the "
                     "chance",
             "correct": False,
             "why": "A body is mostly water. If the metal were in there it "
                    "would react at once"},
            {"text": "The body holds sodium in compounds, never as the metal",
             "correct": True},
            {"text": "The reaction with water happens in large amounts only",
             "correct": False,
             "why": "A grain-sized piece reacts just as readily. Amount "
                    "changes the violence, not whether it happens"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h31",
        "band": "harder",
        "text": "A chemical supplier lists sodium as a metal shipped under "
                "mineral oil and classed as a dangerous good. Which two of "
                "sodium's properties justify that classification?",
        "options": [
            {"text": "It is soft to cut and it has a low density",
             "correct": False,
             "why": "Both are true and neither is a hazard. A soft, light "
                    "solid is not a dangerous good"},
            {"text": "It reacts fiercely with water and gives off a "
                     "flammable gas",
             "correct": True},
            {"text": "It is shiny when cut and it conducts electricity",
             "correct": False,
             "why": "Those are ordinary metal properties, shared by materials "
                    "shipped with no restriction at all"},
            {"text": "It is radioactive and melts at a low temperature",
             "correct": False,
             "why": "Sodium is not radioactive, and a low melting point on "
                    "its own is no shipping hazard"},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h32",
        "band": "harder",
        "text": "What would have to be observed for the statement that "
                "reactivity increases going down group 1 to be abandoned?",
        "options": [
            {"text": "A member of the group failing to float on water",
             "correct": False,
             "why": "Floating is a separate property. Losing it would say "
                    "nothing about the order of reactivity"},
            {"text": "A lower member reacting less fiercely than one above "
                     "it",
             "correct": True},
            {"text": "A member of the group making a completely different product "
                     "with water",
             "correct": False,
             "why": "That would change what the group does, not the direction "
                    "in which its reactivity runs"},
            {"text": "A new member of the group being found below francium",
             "correct": False,
             "why": "A new member would be a fresh chance to test the trend, "
                    "not a reason to give it up"},
        ],
        "figure": None,
    },
]
