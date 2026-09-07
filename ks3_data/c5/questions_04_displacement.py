"""C5 lesson 04 — Displacement: twelve questions (MRB-246).

The lesson's argument is one rule with a direction in it: a more reactive metal
takes a less reactive metal's place in its compound, and never the reverse.
These twelve probe the angles the mastery ladder leaves alone — where the
displaced metal actually came from, what a blank cell means, how the grid's
shape becomes an order, and the two places outside the lab where the rule
decides the answer.

The distractors are built from the lesson's two declared misconceptions.
`REACT-16` (the displaced metal came out of the metal you added) drives the
wrong options in e01 and h02, and it is the same belief in two costumes: once
as "the surface changed into copper" and once as a mass gain explained by the
iron becoming something else. `REACT-17` (a less reactive metal will displace a
more reactive one if you heat it or wait longer) drives s02 entirely and one
option each in e02 and h01 — heat, time and concentration are three ways of
saying the same wrong thing, which is that the direction is a matter of degree
rather than of order.

A third strand runs through e03, s01 and s03 and is in neither register entry,
because it is not a wrong idea about displacement — it is a wrong idea about
what a NEGATIVE RESULT is. A blank cell read as a failed experiment, a diagonal
read as a weak metal, and half a table read as sixteen tests badly done are
three ways of throwing away the half of the evidence that carries the order.

Word equations are written with "makes" rather than a typed arrow, exactly as
Design writes them in her own instrument. The shipped font subsets contain no
U+2192, so an arrow in a question bank is a drawn mark or it is nothing.

The mass figures in h02 are computed rather than invented: 0.01 mol of iron
dissolving deposits 0.01 mol of copper, which is 0.56 g out and 0.64 g in, so a
4.00 g nail comes out at 4.08 g.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §13's: each distractor is a WRONG
RULE in the correct answer's own shape, and each is a mistake a real student in
a real lab actually makes.
"""

UNIT = "C5"
LESSON = "displacement"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c5-04-e01",
        "band": "easier",
        "text": "An iron nail is left in blue copper sulfate solution. After "
                "an hour the nail is coated with orange-brown copper. Where "
                "did that copper come from?",
        "options": [
            {"text": "Out of the solution, where it was dissolved before the "
                     "nail went in", "correct": True},
            {"text": "Out of the iron nail, whose surface changed into copper "
                     "metal", "correct": False,
             "why": "Iron atoms cannot turn into copper atoms. A reaction "
                    "rearranges atoms; it never changes one element into "
                    "another."},
            {"text": "Out of the water, which slowly turned into copper as it "
                     "stood", "correct": False,
             "why": "Water is not made of copper and cannot supply any. The "
                    "copper was already dissolved in the liquid, which is "
                    "what made it blue."},
            {"text": "Out of the air, which supplied it once the nail was "
                     "wet", "correct": False,
             "why": "Nothing came from the air. The blue draining out of the "
                    "solution is the dissolved copper leaving it."},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e02",
        "band": "easier",
        "text": "Zinc is more reactive than copper. Which of these will "
                "happen?",
        "options": [
            {"text": "Copper put into zinc sulfate solution will displace the "
                     "zinc", "correct": False,
             "why": "It only runs one way. A less reactive metal cannot push "
                    "a more reactive one out of its compound."},
            {"text": "Zinc put into copper sulfate solution will displace the "
                     "copper", "correct": True},
            {"text": "Each will displace the other, depending on which one is "
                     "added first", "correct": False,
             "why": "Displacement is not a swap you can run either way. The "
                    "more reactive metal wins, whichever went in first."},
            {"text": "Copper put into zinc sulfate will displace the zinc if "
                     "it is warmed", "correct": False,
             "why": "Warming speeds up a reaction that can happen. This one "
                    "cannot happen at any temperature, because zinc is above "
                    "copper."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-e03",
        "band": "easier",
        "text": "A student puts a piece of zinc into zinc sulfate solution "
                "and nothing happens. Why not?",
        "options": [
            {"text": "Zinc is too unreactive to displace anything at all "
                     "from a solution", "correct": False,
             "why": "Zinc displaces both iron and copper from their "
                    "solutions. The trouble here is that it has been offered "
                    "its own metal."},
            {"text": "The solution was not concentrated enough for the "
                     "reaction to be seen", "correct": False,
             "why": "Concentration changes how fast a reaction goes. There is "
                    "no reaction here to go fast or slow."},
            {"text": "The metal and the dissolved metal are the same, so "
                     "there is nothing to displace", "correct": True},
            {"text": "The zinc needed to be heated first before it would "
                     "react with anything", "correct": False,
             "why": "Heating cannot make a metal displace itself. Both the "
                    "metal and the dissolved metal are zinc, so there is no "
                    "swap to make."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-e04",
        "band": "easier",
        "text": "Magnesium is put into iron sulfate solution and a dark grey "
                "solid appears on it. What does that show?",
        "options": [
            {"text": "Iron is more reactive than magnesium, so it has taken "
                     "the magnesium's place", "correct": False,
             "why": "The metal pushed out is the less reactive one, and here "
                    "that is the iron — the dark grey solid appearing IS the "
                    "iron."},
            {"text": "The magnesium has broken down into the darker "
                     "substances it was made of", "correct": False,
             "why": "Magnesium is an element and cannot be broken down. The "
                    "dark solid came out of the solution."},
            {"text": "The two metals have joined together to make a new grey "
                     "compound", "correct": False,
             "why": "Nothing joins in a displacement. One metal goes into "
                    "the solution and the other comes out of it."},
            {"text": "Magnesium is more reactive than iron, so it has taken "
                     "the iron's place", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c5-04-s01",
        "band": "standard",
        "text": "In a grid of four metals against four solutions, every "
                "reaction sits on one side of the diagonal and every blank on "
                "the other. What does that shape tell you?",
        "options": [
            {"text": "The four metals can be put in one order of reactivity, "
                     "from most to least", "correct": True},
            {"text": "The metals fall into two groups, reactive ones and "
                     "unreactive ones", "correct": False,
             "why": "Two groups would give a table split into blocks, not a "
                    "clean diagonal. A diagonal means every metal has its own "
                    "place in a single line."},
            {"text": "Half of the sixteen tests were set up wrongly and gave "
                     "no result", "correct": False,
             "why": "A blank is a real result. It says the metal in the tube "
                    "is below the metal in the solution, which is exactly the "
                    "information the order is built from."},
            {"text": "The metals react with each other in pairs but not with "
                     "themselves", "correct": False,
             "why": "Only four of the sixteen cells are a metal with itself. "
                    "The other blanks are pairs of different metals where "
                    "nothing happened."},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s02",
        "band": "standard",
        "text": "A copper wire is left in zinc sulfate solution for two weeks "
                "and the tube is warmed every day. Nothing happens. What "
                "should the student conclude?",
        "options": [
            {"text": "Two weeks was not long enough, so a slower experiment "
                     "would show it", "correct": False,
             "why": "Time only helps a reaction that can happen. This one has "
                    "no way to run, so waiting longer changes nothing."},
            {"text": "Copper is below zinc, so the reaction cannot happen at "
                     "any temperature", "correct": True},
            {"text": "The tube was not warmed enough, so a stronger heat "
                     "would start it", "correct": False,
             "why": "Heat speeds reactions up; it does not reverse the "
                    "reactivity order. Zinc stays above copper at every "
                    "temperature."},
            {"text": "Copper takes no part in displacement, so no solution "
                     "will ever affect it", "correct": False,
             "why": "Copper is displaced by zinc, iron and magnesium. It "
                    "takes part constantly — always on the losing side."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-s03",
        "band": "standard",
        "text": "Which word equation describes magnesium reacting with copper "
                "sulfate solution?",
        "options": [
            {"text": "copper + magnesium sulfate makes copper sulfate + "
                     "magnesium", "correct": False,
             "why": "That is the same reaction written backwards. Copper is "
                    "below magnesium, so it cannot displace it."},
            {"text": "magnesium + copper sulfate makes magnesium copper + "
                     "sulfate", "correct": False,
             "why": "\"Magnesium copper\" is not a substance. The displaced "
                    "metal comes out on its own, and the sulfate stays with "
                    "the metal that dissolved."},
            {"text": "magnesium + copper sulfate makes magnesium sulfate + "
                     "copper", "correct": True},
            {"text": "magnesium + copper sulfate + heat makes magnesium "
                     "sulfate + copper", "correct": False,
             "why": "Heat is not a substance and never goes in the line of an "
                    "equation. This reaction gives heat out anyway."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-s04",
        "band": "standard",
        "text": "A silver spoon is left in a beaker of copper sulfate "
                "solution overnight. What would you expect?",
        "options": [
            {"text": "Copper on the spoon, because any metal will displace "
                     "copper from its salt", "correct": False,
             "why": "Only a metal above copper can displace it. Silver is "
                    "below copper, so nothing happens at all."},
            {"text": "Silver in the solution, because the copper would push "
                     "the silver out", "correct": False,
             "why": "Displacement is a metal taking another metal's place in "
                    "a COMPOUND. The silver here is not in a compound, so "
                    "there is nothing to take it out of."},
            {"text": "The solution turning green, because the spoon would "
                     "slowly dissolve into it", "correct": False,
             "why": "The spoon would only dissolve if silver could displace "
                    "copper, and it cannot. The green solution in this lesson "
                    "is iron sulfate."},
            {"text": "Nothing, because silver is less reactive than copper "
                     "and cannot displace it", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c5-04-h01",
        "band": "harder",
        "text": "Iron is obtained from iron oxide by heating it with carbon. "
                "Aluminium oxide cannot be treated the same way. Why not?",
        "options": [
            {"text": "Aluminium is above carbon in the reactivity order, so "
                     "carbon cannot displace it", "correct": True},
            {"text": "Carbon is a non-metal, so it cannot displace a metal "
                     "from its compound", "correct": False,
             "why": "Carbon is a non-metal and it displaces iron in a blast "
                    "furnace every day. It sits in the reactivity order like "
                    "any metal."},
            {"text": "Aluminium oxide melts at too high a temperature for a "
                     "furnace to reach", "correct": False,
             "why": "A hotter furnace still would not do it. Carbon is below "
                    "aluminium, so the swap cannot happen at any "
                    "temperature."},
            {"text": "Aluminium is below carbon in the order, so the reaction "
                     "runs the wrong way", "correct": False,
             "why": "Aluminium is above carbon, not below it. If it were "
                    "below, carbon would displace it and a furnace would be "
                    "enough."},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h02",
        "band": "harder",
        "text": "An iron nail weighing 4.00 g is left in copper sulfate "
                "solution, then taken out and dried. It now weighs 4.08 g. "
                "What has happened?",
        "options": [
            {"text": "The iron has gained mass by taking copper atoms into "
                     "its own structure", "correct": False,
             "why": "The copper sits on the surface as a separate metal. The "
                    "iron underneath is still iron, and some of it has gone "
                    "into the solution."},
            {"text": "Some of the iron has dissolved, and more copper than "
                     "that has been deposited on it", "correct": True},
            {"text": "The iron has turned into copper, which is heavier than "
                     "iron atom for atom", "correct": False,
             "why": "Iron atoms cannot become copper atoms. The copper came "
                    "out of the solution and the iron went into it."},
            {"text": "Nothing has been lost, so the extra mass must have come "
                     "from the water", "correct": False,
             "why": "The water supplied nothing. Iron did leave the nail, and "
                    "the copper that replaced it is heavier, which is why the "
                    "nail still gained."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-h03",
        "band": "harder",
        "text": "An unknown metal displaces copper from copper sulfate but "
                "does not displace iron from iron sulfate. Where does it sit "
                "in the order?",
        "options": [
            {"text": "Above iron, because displacing any metal at all puts it "
                     "near the top", "correct": False,
             "why": "Displacing copper only puts it above copper. Failing "
                    "against iron puts it below iron, and that is the other "
                    "half of the answer."},
            {"text": "Below copper, because it failed one of the two tests it "
                     "was given", "correct": False,
             "why": "It displaced copper, so it must be above copper. A metal "
                    "below copper would have done nothing in either tube."},
            {"text": "Between iron and copper, because it beat one of them "
                     "and not the other", "correct": True},
            {"text": "Nowhere yet, because two tests can never place a metal "
                     "in the order", "correct": False,
             "why": "Two tests are enough when they name neighbours. A "
                    "reaction with the lower one and none with the upper one "
                    "traps the metal between them."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-04-h04",
        "band": "harder",
        "text": "Why is copper sulfate solution kept in plastic bottles "
                "rather than in steel drums?",
        "options": [
            {"text": "Copper sulfate is an acid, and acids eat through any "
                     "metal container", "correct": False,
             "why": "Copper sulfate is a salt, not an acid. What attacks the "
                    "drum is displacement, and only metals above copper can "
                    "do it."},
            {"text": "Steel is below copper in the order, so the copper would "
                     "plate the drum", "correct": False,
             "why": "The copper would plate the drum, but not for that "
                    "reason. Iron is ABOVE copper, and it is the iron "
                    "dissolving that puts the copper there."},
            {"text": "Plastic is cheaper than steel, and the solution does "
                     "not react with either", "correct": False,
             "why": "The solution reacts with steel and not with plastic, and "
                    "that is what decides the choice. Cost is not what is "
                    "doing the work here."},
            {"text": "Steel is mostly iron, which is above copper, so the "
                     "drum would displace it", "correct": True},
                   ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-04-e05",
        "band": "easier",
        "text": "What is the reactivity series?",
        "options": [
            {"text": "The order in which the metals were discovered, running "
                     "from the ones the ancient world could work up to the "
                     "ones that needed electricity",
             "correct": False,
             "why": "The two orders are related and are not the same. The "
                    "series is a measured order of reactivity"},
            {"text": "A list of metals in order of how heavy they are",
             "correct": False,
             "why": "Mass has nothing to do with it. Sodium is light and near "
                    "the top"},
            {"text": "The order the metals appear on the periodic table",
             "correct": False,
             "why": "The table is arranged by atomic number. The series cuts "
                    "across it"},
            {"text": "A list of metals in order of reactivity, most reactive "
                     "first",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e06",
        "band": "easier",
        "text": "Zinc is put into copper sulfate solution. What happens?",
        "options": [
            {"text": "The zinc displaces the copper, which appears as a brown "
                     "solid",
             "correct": True},
            {"text": "Nothing, because a solid cannot react with something "
                     "dissolved",
             "correct": False,
             "why": "That is exactly what displacement is, and it happens "
                    "readily here"},
            {"text": "The copper displaces the zinc",
             "correct": False,
             "why": "The wrong way round. Zinc is the more reactive of the "
                    "two, so it is the one that displaces"},
            {"text": "The solution turns blue",
             "correct": False,
             "why": "It starts blue and FADES as the dissolved copper "
                    "leaves"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e07",
        "band": "easier",
        "text": "Why are carbon and hydrogen included in the reactivity "
                "series, when neither is a metal?",
        "options": [
            {"text": "Because every list of elements has to include them, "
                     "since they are the two commonest elements in the "
                     "universe and in living things",
             "correct": False,
             "why": "Commonness is no reason to be in this list. They are "
                    "there because they take part in displacement"},
            {"text": "Because they displace on the same rule, so they can be "
                     "placed in the same order",
             "correct": True},
            {"text": "Because they are needed to make the metals react",
             "correct": False,
             "why": "Zinc displaces copper with neither of them present"},
            {"text": "Because they behave like metals in every other way",
             "correct": False,
             "why": "They behave like non-metals in almost every other way. "
                    "Displacement is the exception"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e08",
        "band": "easier",
        "text": "What is an ore?",
        "options": [
            {"text": "A rock containing a metal in its pure form, ready to be "
                     "melted down",
             "correct": False,
             "why": "That happens for gold and almost nothing else. An ore "
                    "holds the metal as a COMPOUND"},
            {"text": "A metal that has been dug out of the ground",
             "correct": False,
             "why": "The ore is the rock. The metal is what comes out of it"},
            {"text": "A rock containing enough of a metal's compound to be "
                     "worth extracting the metal from",
             "correct": True},
            {"text": "Any rock with a metal atom anywhere in it",
             "correct": False,
             "why": "Almost every rock qualifies on that test. The word means "
                    "enough to be worth the trouble"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e09",
        "band": "easier",
        "text": "All the solutions on the displacement bench are SULFATES. "
                "Why does that matter?",
        "options": [
            {"text": "Because sulfates are the only compounds that dissolve "
                     "well enough",
             "correct": False,
             "why": "Chlorides and nitrates dissolve well too. Keeping the "
                    "partner the same is about making the tubes comparable"},
            {"text": "Because a sulfate is the only compound a metal can be "
                     "displaced from",
             "correct": False,
             "why": "Displacement works from chlorides and oxides too. "
                    "Thermite uses an oxide"},
            {"text": "Because sulfates are all the same colour",
             "correct": False,
             "why": "They are not — copper sulfate is blue and zinc sulfate "
                    "is colourless. The colours are part of what you "
                    "observe"},
            {"text": "Because keeping the same partner means the only thing "
                     "changing between tubes is the metal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e10",
        "band": "easier",
        "text": "A more reactive metal is described as holding on to a "
                "partner more strongly. What follows?",
        "options": [
            {"text": "It can take a partner away from a less reactive metal, "
                     "and not the other way round",
             "correct": True},
            {"text": "It dissolves in water more readily than a less reactive "
                     "one, which is why the solutions of reactive metals are "
                     "the most concentrated ones on the bench",
             "correct": False,
             "why": "How much dissolves is a separate property. What follows "
                    "is which metal wins a partner"},
            {"text": "It is harder and denser than a less reactive metal",
             "correct": False,
             "why": "Sodium is soft and light and highly reactive. Hardness "
                    "does not follow"},
            {"text": "It gives its partner up more easily",
             "correct": False,
             "why": "Exactly backwards, and it is what makes the order run "
                    "one way only"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c5-04-s05",
        "band": "standard",
        "text": "An iron nail in copper sulfate goes brown and the blue "
                "solution fades to pale green. What has the green colour told "
                "you?",
        "options": [
            {"text": "That the copper is still dissolved in the solution, and "
                     "the green is what copper sulfate looks like once it has "
                     "been diluted by the reaction",
             "correct": False,
             "why": "Diluting blue gives paler blue. The green is a new "
                    "substance"},
            {"text": "That the nail is rusting",
             "correct": False,
             "why": "Rust is orange-brown and on the nail. The green is in "
                    "the liquid"},
            {"text": "That iron sulfate has formed, so the iron has gone into "
                     "solution",
             "correct": True},
            {"text": "That the solution has been contaminated",
             "correct": False,
             "why": "It is the expected product of the reaction. Nothing has "
                    "gone wrong"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s06",
        "band": "standard",
        "text": "Thermite is iron oxide mixed with aluminium powder, lit to "
                "weld a rail. Which metal ends up with the oxygen?",
        "options": [
            {"text": "The iron keeps it, and the aluminium melts and pours "
                     "into the gap between the rails as the weld",
             "correct": False,
             "why": "It is the IRON that pours out white-hot. Aluminium is "
                    "more reactive and takes the oxygen"},
            {"text": "Neither — the oxygen is given off as a gas",
             "correct": False,
             "why": "No gas is produced. The oxygen changes partner"},
            {"text": "Both share it equally",
             "correct": False,
             "why": "Displacement is not a sharing. The more reactive metal "
                    "takes it"},
            {"text": "The aluminium, because it is the more reactive of the "
                     "two",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s07",
        "band": "standard",
        "text": "A grid of four metals against four solutions has sixteen "
                "tubes, and four of them are a metal in its own solution. What "
                "are those four for?",
        "options": [
            {"text": "To show that a metal cannot displace itself from its "
                     "own compound",
             "correct": True},
            {"text": "To show the colour each solution starts at, so that any "
                     "change in the other twelve can be judged against it",
             "correct": False,
             "why": "The bottle already shows the starting colour. These "
                    "tubes show that a metal cannot displace itself"},
            {"text": "To check the metals have been cleaned properly",
             "correct": False,
             "why": "A tube where nothing should happen cannot test the "
                    "cleaning"},
            {"text": "To act as spares in case a tube is broken",
             "correct": False,
             "why": "Every tube on the grid is a real test with a result"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s08",
        "band": "standard",
        "text": "Gold and copper were worked thousands of years before iron. "
                "What does the reactivity series say about that?",
        "options": [
            {"text": "That gold and copper are hard enough to shape with "
                     "stone tools",
             "correct": False,
             "why": "Gold and copper are the SOFTER metals, and the "
                    "difference is chemical rather than mechanical"},
            {"text": "That both are unreactive enough to be found as the "
                     "metal, while iron has to be displaced from its ore",
             "correct": True},
            {"text": "That gold and copper were more common in the ancient "
                     "world",
             "correct": False,
             "why": "Iron is far more abundant than either. Getting it out "
                    "was the difficulty"},
            {"text": "That iron ore had not formed yet",
             "correct": False,
             "why": "Iron ore is older than the human species. What was "
                    "missing was the furnace"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s09",
        "band": "standard",
        "text": "Magnesium is put into zinc sulfate and a dark solid appears; "
                "zinc is put into magnesium sulfate and nothing happens. What "
                "have those two tubes together established?",
        "options": [
            {"text": "That magnesium reacts faster than zinc does, which is "
                     "what a solid appearing in one tube and not in the other "
                     "is a measure of",
             "correct": False,
             "why": "One tube has no reaction at all rather than a slow one. "
                    "That is a difference of order, not of rate"},
            {"text": "That zinc sulfate is more concentrated than magnesium "
                     "sulfate",
             "correct": False,
             "why": "Concentration was kept the same. What differs is the "
                    "metals"},
            {"text": "That magnesium is above zinc, and that the order runs "
                     "one way only",
             "correct": True},
            {"text": "That both metals are more reactive than copper",
             "correct": False,
             "why": "True from other tubes on the grid, and not from these "
                    "two. They compare magnesium with zinc"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s10",
        "band": "standard",
        "text": "Why does the displacement grid come out half full, with "
                "every reaction on one side of the diagonal?",
        "options": [
            {"text": "Because half the tubes were a metal in its own "
                     "solution, and those can never react whichever way round "
                     "they are set up",
             "correct": False,
             "why": "Only four of the sixteen are like that. The diagonal "
                    "shape comes from the order running one way"},
            {"text": "Because half the solutions were too dilute to react",
             "correct": False,
             "why": "All were made up the same way. Concentration is not what "
                    "makes the pattern"},
            {"text": "Because the grid was only half filled in",
             "correct": False,
             "why": "Every tube was run. The blanks are results"},
            {"text": "Because a metal displaces every metal below it and none "
                     "above it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-04-h05",
        "band": "harder",
        "text": "Aluminium was once more valuable than silver, and is now in "
                "every kitchen. What changed?",
        "options": [
            {"text": "New ore deposits were found, and the price fell",
             "correct": False,
             "why": "Aluminium is the commonest metal in the crust and always "
                    "was. Extracting it was the problem"},
            {"text": "Chemists discovered that it was not really a metal",
             "correct": False,
             "why": "It is very much a metal. Its value fell when it became "
                    "easy to obtain"},
            {"text": "It was found to be more reactive than carbon",
             "correct": False,
             "why": "Being above carbon is WHY a furnace fails. Knowing it "
                    "did not solve anything by itself"},
            {"text": "Electricity made it possible to break its ore apart, "
                     "which no furnace could do",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h06",
        "band": "harder",
        "text": "An unknown metal displaces zinc from zinc sulfate but not "
                "magnesium from magnesium sulfate. Where does it sit?",
        "options": [
            {"text": "Between magnesium and zinc",
             "correct": True},
            {"text": "Above magnesium, since a metal that can displace one of "
                     "the two must be more reactive than both of them",
             "correct": False,
             "why": "It failed against magnesium, which puts it below. Only "
                    "the zinc test went its way"},
            {"text": "Below zinc",
             "correct": False,
             "why": "Then it could not have displaced zinc at all"},
            {"text": "It cannot be placed from two results",
             "correct": False,
             "why": "One win and one loss brackets it between the two, which "
                    "is exactly what the series is built from"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h07",
        "band": "harder",
        "text": "A student says an iron nail in copper sulfate turns into "
                "copper on the outside. What is the strongest single reply?",
        "options": [
            {"text": "Iron and copper are different elements, so one cannot "
                     "become the other, and any claim that they can is a "
                     "claim about alchemy rather than chemistry",
             "correct": False,
             "why": "Perfectly true and it is an argument from principle. The "
                    "fading blue is EVIDENCE, on the bench, in front of "
                    "them"},
            {"text": "Iron and copper are different elements, so one cannot "
                     "become the other",
             "correct": True},
            {"text": "The nail gets heavier, which shows something was "
                     "added",
             "correct": False,
             "why": "It does gain mass, and that is consistent with several "
                    "stories. The fading solution names where the copper came "
                    "from"},
            {"text": "Copper is less reactive than iron",
             "correct": False,
             "why": "That explains why the reaction runs and does not by "
                    "itself answer where the copper came from"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h08",
        "band": "harder",
        "text": "Copper sulfate solution is kept in plastic rather than in "
                "steel drums. Suppose it were stored in a ZINC-lined drum "
                "instead. What would happen?",
        "options": [
            {"text": "Nothing, because zinc is not iron and only iron "
                     "displaces copper",
             "correct": False,
             "why": "Zinc is above copper too, and it displaces copper "
                    "readily"},
            {"text": "The copper would plate the lining and protect it",
             "correct": False,
             "why": "Copper does deposit, and the zinc underneath is being "
                    "consumed to put it there"},
            {"text": "The zinc would displace the copper, so the lining would "
                     "be eaten away as well",
             "correct": True},
            {"text": "The solution would turn from blue to a deeper blue",
             "correct": False,
             "why": "The blue fades as the dissolved copper leaves. It does "
                    "not deepen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h09",
        "band": "harder",
        "text": "A thermite reaction reaches 2500 °C with no power supply at "
                "all. Where does that energy come from?",
        "options": [
            {"text": "From the match used to light it, which supplies enough "
                     "energy to reach that temperature once it is concentrated "
                     "into a small crucible",
             "correct": False,
             "why": "A match supplies only the start. What follows releases "
                    "far more than the match ever held"},
            {"text": "From the iron oxide decomposing as it heats",
             "correct": False,
             "why": "No decomposition is happening. The oxygen changes "
                    "partner rather than being released"},
            {"text": "From the friction of the powders mixing",
             "correct": False,
             "why": "Mixing releases almost nothing. The energy is chemical"},
            {"text": "From the reaction itself, which is exothermic — "
                     "displacement gives energy out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h10",
        "band": "harder",
        "text": "A student proposes finding a metal's place in the series by "
                "testing it against EVERY solution on the shelf. Why is that "
                "more work than it needs to be?",
        "options": [
            {"text": "Because each result narrows the range, so the next "
                     "solution can be chosen from the last answer",
             "correct": True},
            {"text": "Because a metal only has to be tested against the "
                     "solution directly above it and the one directly below "
                     "it, and those two can be read off the series in "
                     "advance",
             "correct": False,
             "why": "You cannot know which two are adjacent until you have "
                    "placed it. Narrowing is how you find out"},
            {"text": "Because most of the tubes would give the same result",
             "correct": False,
             "why": "They would split into wins and losses, and every one "
                    "would be a real result. The saving is in not needing "
                    "them all"},
            {"text": "Because testing every solution would use up the metal",
             "correct": False,
             "why": "A small piece goes into each tube. Supply is not the "
                    "objection"},
        ],
        "figure": None,
    },
]
