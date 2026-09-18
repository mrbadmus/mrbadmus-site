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
            {"text": "A list of the metals in order of how heavy each one of "
                     "them happens to be",
             "correct": False,
             "why": "Mass has nothing to do with it. Sodium is light and near "
                    "the top"},
            {"text": "The order that the metals appear in as you read across "
                     "the periodic table",
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
            {"text": "Because they behave exactly like the metals in every "
                     "other way that has ever been looked at",
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
            {"text": "It is harder and denser than any less reactive metal is, "
                     "and a great deal harder to scratch too",
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

    # ── easier · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c5-04-e11",
        "band": "easier",
        "text": "Of copper, magnesium, iron and zinc, which is the least "
                "reactive?",
        "options": [
            {"text": "Magnesium",
             "correct": False,
             "why": "Magnesium is the most reactive of the four. It displaces "
                    "all three of the others"},
            {"text": "Zinc",
             "correct": False,
             "why": "Zinc sits above both iron and copper, so it displaces two "
                    "of the four"},
            {"text": "Copper",
             "correct": True},
            {"text": "Iron",
             "correct": False,
             "why": "Iron displaces copper, so there is one metal here it "
                    "beats"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e12",
        "band": "easier",
        "text": "Copper sulfate solution is blue. What colour is iron sulfate "
                "solution?",
        "options": [
            {"text": "Pale green",
             "correct": True},
            {"text": "A deeper blue than copper sulfate, because iron is the "
                     "heavier of the two metals",
             "correct": False,
             "why": "Iron sulfate is not blue at all, and the mass of a metal "
                    "has nothing to do with the colour of its solution"},
            {"text": "Colourless",
             "correct": False,
             "why": "Magnesium sulfate and zinc sulfate are the colourless "
                    "ones on this bench"},
            {"text": "Orange-brown",
             "correct": False,
             "why": "Orange-brown is the colour of copper metal, which is a "
                    "solid rather than a solution"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e13",
        "band": "easier",
        "text": "An iron nail is taken out of copper sulfate solution coated "
                "in a new solid. What colour is that solid?",
        "options": [
            {"text": "Silvery-grey, because the fresh iron underneath has been "
                     "exposed by the reaction",
             "correct": False,
             "why": "The new solid is not iron at all. Iron is the metal that "
                    "has left the nail and gone into the solution"},
            {"text": "Black",
             "correct": False,
             "why": "Nothing black is made here. Black copper oxide comes from "
                    "heating copper in air, which is a different reaction"},
            {"text": "Orange-brown",
             "correct": True},
            {"text": "Pale green",
             "correct": False,
             "why": "Pale green is the colour the solution turns. The solid on "
                    "the nail is a metal"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e14",
        "band": "easier",
        "text": "A metal at the very bottom of the reactivity series is the "
                "one that does what?",
        "options": [
            {"text": "Reacts least readily of all",
             "correct": True},
            {"text": "Is dug up as a compound",
             "correct": False,
             "why": "The metals at the bottom are the ones found as the metal. "
                    "That is why gold was worked so early"},
            {"text": "Is the commonest metal in the crust",
             "correct": False,
             "why": "Aluminium is the commonest metal in the crust, and it "
                    "sits near the top of the list"},
            {"text": "Cannot be displaced from its compound",
             "correct": False,
             "why": "Exactly backwards. The bottom metal is the one every "
                    "other metal can displace"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e15",
        "band": "easier",
        "text": "Which of the four bench metals would displace all three of "
                "the others from their solutions?",
        "options": [
            {"text": "Copper",
             "correct": False,
             "why": "Copper displaces none of them. It is the one at the "
                    "bottom of these four"},
            {"text": "Magnesium",
             "correct": True},
            {"text": "Iron",
             "correct": False,
             "why": "Iron displaces copper and nothing else. Magnesium and "
                    "zinc are both above it"},
            {"text": "Whichever one is put into the solution first, since the "
                     "first metal in has the dissolved metal to itself",
             "correct": False,
             "why": "Order of addition decides nothing. Which metal wins is "
                    "fixed by the reactivity order"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e16",
        "band": "easier",
        "text": "Which of these metals sits ABOVE carbon in the reactivity "
                "series?",
        "options": [
            {"text": "Iron",
             "correct": False,
             "why": "Iron is below carbon, which is exactly why carbon can "
                    "pull it out of its ore in a furnace"},
            {"text": "Zinc",
             "correct": False,
             "why": "Zinc sits below carbon, between carbon and iron in the "
                    "list"},
            {"text": "Copper",
             "correct": False,
             "why": "Copper is a long way below carbon. It is near the bottom "
                    "of the whole series"},
            {"text": "Aluminium",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e17",
        "band": "easier",
        "text": "A piece of iron is left in magnesium sulfate solution for a "
                "week. What happens?",
        "options": [
            {"text": "Magnesium collects on the iron as a silvery-grey solid, "
                     "because the iron takes its place in the sulfate",
             "correct": False,
             "why": "Iron is below magnesium, so it cannot take the "
                    "magnesium's place. Nothing collects on it"},
            {"text": "The iron dissolves",
             "correct": False,
             "why": "The iron would only dissolve if it could displace the "
                    "magnesium, and it is the weaker of the two"},
            {"text": "The solution turns pale green",
             "correct": False,
             "why": "That is what iron in COPPER sulfate does. Here the iron "
                    "stays where it is, so no iron sulfate forms"},
            {"text": "Nothing at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e18",
        "band": "easier",
        "text": "Railway track is welded in the middle of nowhere using a "
                "displacement reaction in a crucible. What is that reaction "
                "called?",
        "options": [
            {"text": "Thermite",
             "correct": True},
            {"text": "Galvanising, which is the name for any process where one "
                     "metal is laid down on another",
             "correct": False,
             "why": "Galvanising is coating steel with zinc to protect it, and "
                    "nothing is welded by it"},
            {"text": "Smelting",
             "correct": False,
             "why": "Smelting is getting a metal out of its ore in a furnace, "
                    "which is a different job"},
            {"text": "Electrolysis",
             "correct": False,
             "why": "Electrolysis needs a power supply, and the point of this "
                    "reaction is that it needs none"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e19",
        "band": "easier",
        "text": "Which two substances are mixed in the crucible for a thermite "
                "reaction?",
        "options": [
            {"text": "Iron powder and aluminium oxide, which is the pair that "
                     "leaves molten aluminium behind",
             "correct": False,
             "why": "That is the pair the wrong way round, and it would do "
                    "nothing: iron is below aluminium"},
            {"text": "Aluminium powder and iron oxide",
             "correct": True},
            {"text": "Carbon powder and iron oxide, heated until the iron runs "
                     "out of the bottom",
             "correct": False,
             "why": "That pair is the blast furnace. Thermite needs no furnace "
                    "and takes seconds"},
            {"text": "Aluminium powder and copper oxide",
             "correct": False,
             "why": "That pair does react, and it gives molten copper. It is "
                    "iron that is wanted for welding a rail"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e20",
        "band": "easier",
        "text": "A displacement reaction is run in a test tube. What happens "
                "to the temperature of the mixture?",
        "options": [
            {"text": "It falls, because energy is taken in to break the "
                     "compound apart",
             "correct": False,
             "why": "Displacement gives energy out rather than taking it in. "
                    "The tube gets warmer, not colder"},
            {"text": "It stays the same",
             "correct": False,
             "why": "Nothing was heated from outside, and the reaction itself "
                    "supplies warmth a thermometer can pick up"},
            {"text": "It rises slightly",
             "correct": True},
            {"text": "It rises only if the tube is warmed first to start the "
                     "reaction going",
             "correct": False,
             "why": "These reactions start on their own at room temperature. "
                    "No warming is needed"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e21",
        "band": "easier",
        "text": "Magnesium is put into copper sulfate solution. Which metal "
                "ends up dissolved in the solution?",
        "options": [
            {"text": "The magnesium",
             "correct": True},
            {"text": "The copper",
             "correct": False,
             "why": "The copper starts dissolved and finishes as a solid. That "
                    "swap is the whole reaction"},
            {"text": "Both of them",
             "correct": False,
             "why": "A sulfate holds one metal. The one it lets go of comes "
                    "out as a solid"},
            {"text": "Neither of them",
             "correct": False,
             "why": "The magnesium does dissolve, which is why the piece gets "
                    "smaller as the reaction runs"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e22",
        "band": "easier",
        "text": "Zinc displaces copper from copper sulfate solution. What has "
                "happened to the zinc by the end?",
        "options": [
            {"text": "It is coated in copper and otherwise unchanged",
             "correct": False,
             "why": "Copper does coat it, and some of the zinc has gone: it is "
                    "the zinc that went into the solution"},
            {"text": "It has broken down into simpler substances",
             "correct": False,
             "why": "Zinc is an element, so there are no simpler substances "
                    "inside it to break into"},
            {"text": "It has turned into copper, so the piece looks brown",
             "correct": False,
             "why": "Zinc atoms cannot become copper atoms. The brown metal "
                    "came out of the solution"},
            {"text": "It has dissolved, and zinc sulfate is left in the "
                     "solution",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e23",
        "band": "easier",
        "text": "What does the word reactivity mean when it is used about a "
                "metal?",
        "options": [
            {"text": "How easily it melts",
             "correct": False,
             "why": "Melting is a physical change and needs no reaction. "
                    "Reactivity is about taking part in reactions"},
            {"text": "How readily it takes part in a reaction",
             "correct": True},
            {"text": "How much of it is in the ground",
             "correct": False,
             "why": "Aluminium is the commonest metal in the crust and is also "
                    "one of the more reactive. The two are not the same"},
            {"text": "How strong it is as a bar",
             "correct": False,
             "why": "Strength is a physical property. Sodium is weak and soft "
                    "and violently reactive"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e24",
        "band": "easier",
        "text": "Silver and gold are found in the ground as the metal itself "
                "rather than as a compound. What does that tell you about "
                "them?",
        "options": [
            {"text": "They are very unreactive",
             "correct": True},
            {"text": "They are too rare to react",
             "correct": False,
             "why": "How rare a metal is has nothing to do with whether it "
                    "sits in the ground as a compound"},
            {"text": "They are light metals",
             "correct": False,
             "why": "Gold and silver are among the densest metals there are. "
                    "What keeps them as the metal is their lack of reactivity"},
            {"text": "They melt easily",
             "correct": False,
             "why": "Both melt at around a thousand degrees, and melting would "
                    "not separate a metal from its compound anyway"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e25",
        "band": "easier",
        "text": "Magnesium is put into zinc sulfate solution and a grey solid "
                "collects on the ribbon. Which metal is that grey solid?",
        "options": [
            {"text": "Magnesium, which has come off the ribbon and settled "
                     "again lower down the tube",
             "correct": False,
             "why": "The magnesium is going into the solution, not settling "
                    "out of it"},
            {"text": "A mixture of the two metals joined together into one new "
                     "grey substance",
             "correct": False,
             "why": "Nothing joins in a displacement. One metal goes in and "
                    "the other comes out"},
            {"text": "Zinc",
             "correct": True},
            {"text": "Sulfur",
             "correct": False,
             "why": "The sulfate is not broken open, so no sulfur is set free. "
                    "It simply changes which metal it is holding"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e26",
        "band": "easier",
        "text": "Which of these tubes would show a reaction?",
        "options": [
            {"text": "Copper in iron sulfate solution",
             "correct": False,
             "why": "Copper is below iron, so it cannot take the iron's place"},
            {"text": "Zinc in iron sulfate solution",
             "correct": True},
            {"text": "Iron in magnesium sulfate solution",
             "correct": False,
             "why": "Iron is below magnesium, so nothing happens in that tube"},
            {"text": "Copper in magnesium sulfate solution, since any metal "
                     "put into any salt solution will displace something",
             "correct": False,
             "why": "Only a metal ABOVE the dissolved one displaces it, and "
                    "copper is below all three of the others"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e27",
        "band": "easier",
        "text": "Potassium is the first substance in the reactivity series. "
                "What does being first mean?",
        "options": [
            {"text": "It was discovered first",
             "correct": False,
             "why": "Gold and copper were known thousands of years earlier. "
                    "The list is not a history"},
            {"text": "It is displaced by the rest",
             "correct": False,
             "why": "That describes the metal at the BOTTOM. Potassium is the "
                    "one nothing else can displace"},
            {"text": "It is the lightest metal",
             "correct": False,
             "why": "The list is not ordered by mass. Lithium is lighter than "
                    "potassium and gold is far heavier"},
            {"text": "It is the most reactive of them all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e28",
        "band": "easier",
        "text": "An iron nail displaces copper from copper sulfate solution. "
                "What compound is left dissolved in the solution?",
        "options": [
            {"text": "Copper sulfate",
             "correct": False,
             "why": "The copper has left the solution altogether. What is "
                    "dissolved now holds a different metal"},
            {"text": "Iron oxide",
             "correct": False,
             "why": "No oxygen is involved anywhere in this reaction. The "
                    "sulfate keeps the partner it had"},
            {"text": "Iron sulfate",
             "correct": True},
            {"text": "Sulfuric acid",
             "correct": False,
             "why": "There is always a metal in the solution. One simply "
                    "replaces the other"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e29",
        "band": "easier",
        "text": "Iron is obtained by heating iron oxide with carbon in a blast "
                "furnace. What is the carbon doing there?",
        "options": [
            {"text": "Melting the ore",
             "correct": False,
             "why": "Carbon is not there to melt anything. It is taking the "
                    "oxygen off the iron"},
            {"text": "Displacing the iron",
             "correct": True},
            {"text": "Joining on to the iron, which is what makes the steel "
                     "that comes out of the furnace",
             "correct": False,
             "why": "A little carbon does end up in steel, and that is not the "
                    "reaction that frees the iron from its ore"},
            {"text": "Keeping the air away from the iron so that it cannot "
                     "rust while it is still hot",
             "correct": False,
             "why": "The furnace is not there to stop rust. It is there to get "
                    "the metal out of the compound"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-e30",
        "band": "easier",
        "text": "Put magnesium, zinc, iron and copper in order, most reactive "
                "first.",
        "options": [
            {"text": "Copper, iron, zinc, magnesium",
             "correct": False,
             "why": "That is the right order written upside down, with the "
                    "least reactive metal first"},
            {"text": "Magnesium, zinc, iron, copper",
             "correct": True},
            {"text": "Zinc, magnesium, copper, iron",
             "correct": False,
             "why": "Magnesium displaces zinc, and iron displaces copper, so "
                    "both of those pairs are the wrong way round"},
            {"text": "Iron, copper, magnesium, zinc",
             "correct": False,
             "why": "Iron is displaced by both magnesium and zinc, so it "
                    "cannot be at the top"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 top-up ───────────────────────────────────────
    {
        "id": "c5-04-s11",
        "band": "standard",
        "text": "Iron filings are stirred into zinc sulfate solution. Predict "
                "what happens and give the reason.",
        "options": [
            {"text": "Zinc appears as a grey solid, because the iron pushes "
                     "the zinc out of the sulfate",
             "correct": False,
             "why": "Zinc is above iron, so the iron cannot push it out. The "
                    "push only ever runs downwards"},
            {"text": "Nothing, because iron is below zinc and cannot take its "
                     "place",
             "correct": True},
            {"text": "Nothing yet, because filings are too fine and a solid "
                     "strip would be needed to see it",
             "correct": False,
             "why": "Filings react faster than a strip, not slower. The reason "
                    "nothing happens is the order, not the shape"},
            {"text": "The solution turns pale green, because the iron "
                     "dissolves into it",
             "correct": False,
             "why": "Iron only dissolves when it can displace something. Here "
                    "it stays as it is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s12",
        "band": "standard",
        "text": "Magnesium is put into zinc sulfate solution. Magnesium "
                "sulfate and zinc sulfate are both colourless. What would you "
                "see?",
        "options": [
            {"text": "Nothing, because a colour change is the only sign of a "
                     "displacement",
             "correct": False,
             "why": "A colour change is one sign among several. A solid "
                    "appearing and a tube warming are signs too"},
            {"text": "The colourless solution turning blue as the magnesium "
                     "sulfate forms",
             "correct": False,
             "why": "Magnesium sulfate is colourless. Blue is copper sulfate, "
                    "which is not in this tube"},
            {"text": "A grey solid on the ribbon and a tube that warms, with "
                     "no colour change to watch",
             "correct": True},
            {"text": "The ribbon getting thicker as the solution fades to a "
                     "pale grey",
             "correct": False,
             "why": "Zinc is laid down, and the solution has no colour to fade "
                    "from. Both solutions here are colourless"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s13",
        "band": "standard",
        "text": "A student writes: iron + copper sulfate makes iron sulfate + "
                "copper. Which part of that line shows that iron is the more "
                "reactive metal?",
        "options": [
            {"text": "Iron is written first on the left, and the more reactive "
                     "reactant is always written first",
             "correct": False,
             "why": "Which reactant is written first is a matter of habit and "
                    "carries no chemical claim at all"},
            {"text": "Both metals appear on both sides, which shows they have "
                     "exchanged their strengths",
             "correct": False,
             "why": "Each metal appears once on each side, and neither of them "
                    "changes into anything else"},
            {"text": "The word sulfate appears twice, once with each metal",
             "correct": False,
             "why": "The sulfate is the partner both metals can have. It says "
                    "nothing about which one wins it"},
            {"text": "Iron ends up in the compound and copper ends up as the "
                     "metal on its own",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s14",
        "band": "standard",
        "text": "Four metals are each put into all four sulfate solutions, and "
                "exactly six tubes react. Why six?",
        "options": [
            {"text": "There are six pairs of different metals, and each pair "
                     "reacts one way round only",
             "correct": True},
            {"text": "Six of the sixteen tubes were set up with the more "
                     "reactive metal on top, and a metal has to be above the "
                     "solution to reach it",
             "correct": False,
             "why": "Where a piece of metal sits in a tube decides nothing. "
                    "The order of the metals decides it"},
            {"text": "Six of the solutions were coloured, and only a coloured "
                     "solution can show a reaction",
             "correct": False,
             "why": "Only two of the four are coloured, and a colourless tube "
                    "can react perfectly well"},
            {"text": "Ten of the sixteen were spoiled by the metal in its own "
                     "solution, leaving six that could work",
             "correct": False,
             "why": "Only four tubes hold a metal in its own solution, and "
                    "those four are results rather than spoiled tubes"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s15",
        "band": "standard",
        "text": "A student predicts that iron will displace magnesium because "
                "iron is the harder and stronger of the two metals. What is "
                "wrong with that reasoning?",
        "options": [
            {"text": "Hardness is not reactivity, and magnesium is above iron",
             "correct": True},
            {"text": "Nothing is wrong with it, but the reaction would be far "
                     "too slow to see in one lesson",
             "correct": False,
             "why": "The reaction does not happen at all, however long it is "
                    "left"},
            {"text": "Iron is in fact the softer of the two, so the prediction "
                     "fails",
             "correct": False,
             "why": "Magnesium is the softer one, and hardness would still not "
                    "settle which metal wins"},
            {"text": "Hardness does decide it, and the student has simply "
                     "remembered the order the wrong way round",
             "correct": False,
             "why": "Hardness decides nothing here. Sodium is soft enough to "
                    "cut and is one of the most reactive metals there is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s16",
        "band": "standard",
        "text": "Calcium sits above magnesium in the reactivity series. "
                "Predict what happens when calcium is put into magnesium "
                "sulfate solution.",
        "options": [
            {"text": "Nothing, because magnesium is one of the four bench "
                     "metals and calcium is not",
             "correct": False,
             "why": "Which metals are on a particular bench decides nothing. "
                    "The order decides it"},
            {"text": "The calcium displaces the magnesium, which appears as a "
                     "solid",
             "correct": True},
            {"text": "The magnesium displaces the calcium, which appears as a "
                     "solid",
             "correct": False,
             "why": "Calcium is above magnesium, so the swap runs the other "
                    "way"},
            {"text": "The two metals share the sulfate between them, giving a "
                     "solution holding both",
             "correct": False,
             "why": "A sulfate holds one metal. There is no sharing in a "
                    "displacement"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s17",
        "band": "standard",
        "text": "Two tubes are set up side by side: magnesium in copper "
                "sulfate, and copper in magnesium sulfate. Only one of them "
                "warms up. Which, and why?",
        "options": [
            {"text": "The copper one, because copper conducts heat better than "
                     "magnesium does",
             "correct": False,
             "why": "Conducting heat is not making heat. No reaction runs in "
                    "that tube at all"},
            {"text": "Both of them, because a reaction runs in each and every "
                     "reaction gives out energy",
             "correct": False,
             "why": "Only one of the two can run, and reactions that take "
                    "energy in exist as well"},
            {"text": "The magnesium one, because that is the only tube where a "
                     "reaction runs",
             "correct": True},
            {"text": "The magnesium one, because magnesium is the lighter "
                     "metal and light metals warm up faster",
             "correct": False,
             "why": "Right tube, wrong reason. The warmth comes from the "
                    "reaction, not from what the metal weighs"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s18",
        "band": "standard",
        "text": "A student writes \"no data\" in every cell of the grid where "
                "nothing happened. Why is that the wrong thing to write?",
        "options": [
            {"text": "Because the tube should be run again until something "
                     "does happen and a reading can be taken",
             "correct": False,
             "why": "Repeating a tube that cannot react gives the same answer "
                    "every time, and that answer is the data"},
            {"text": "Because a blank is a result: it says the metal is below "
                     "the metal in the solution",
             "correct": True},
            {"text": "Because the cell should be left completely empty, so "
                     "that only real results appear on the grid",
             "correct": False,
             "why": "An empty cell cannot be told apart from a tube nobody "
                    "ran. What happened has to be recorded"},
            {"text": "Because the words should say which metal was added, "
                     "rather than what came out of the tube",
             "correct": False,
             "why": "The metal added is already named by the row. What the "
                    "cell records is the outcome"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s19",
        "band": "standard",
        "text": "Aluminium powder is mixed with zinc oxide and the mixture is "
                "lit. Aluminium is above zinc. Predict the result.",
        "options": [
            {"text": "The zinc is displaced, leaving aluminium oxide behind",
             "correct": True},
            {"text": "Nothing happens, because displacement works in solutions "
                     "rather than between two solids",
             "correct": False,
             "why": "Thermite is two solids, and it is a displacement. The "
                    "rule is about the order, not the state"},
            {"text": "The aluminium is displaced, leaving zinc oxide behind",
             "correct": False,
             "why": "Aluminium is the more reactive one here, so it is the "
                    "metal that takes the oxygen"},
            {"text": "The two oxides both form, because oxygen is shared out "
                     "between the two metals in the crucible",
             "correct": False,
             "why": "The oxygen goes to the more reactive metal. It is not "
                    "divided between them"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s20",
        "band": "standard",
        "text": "Every tube on the grid gets the same volume of solution, the "
                "same concentration and a piece of metal the same size. Why "
                "does that matter?",
        "options": [
            {"text": "Because none of the tubes then runs out before the "
                     "others",
             "correct": False,
             "why": "Running out is not the worry. Being able to compare the "
                    "tubes with each other is"},
            {"text": "Because a reaction only runs if the amounts are matched",
             "correct": False,
             "why": "A reaction runs or does not run according to the order of "
                    "the metals, whatever the amounts"},
            {"text": "Because the only thing left differing between tubes is "
                     "which metals are in them",
             "correct": True},
            {"text": "Because a table can only hold results measured in the "
                     "same units",
             "correct": False,
             "why": "Nothing here is measured in units. What is being compared "
                    "is whether a reaction happened"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s21",
        "band": "standard",
        "text": "A magnesium ribbon is left in blue copper sulfate solution "
                "until the liquid is completely colourless. What does the "
                "colourless liquid tell you?",
        "options": [
            {"text": "That the magnesium has now dissolved completely, leaving "
                     "nothing solid in the tube",
             "correct": False,
             "why": "Solid copper is in the tube whether or not the ribbon has "
                    "gone. The colour is about the dissolved metal"},
            {"text": "That the reaction stopped early and would restart if "
                     "warmed",
             "correct": False,
             "why": "It has run to the end rather than stopping early. There "
                    "is no dissolved copper left to react with"},
            {"text": "That the water has evaporated and taken the blue colour "
                     "with it",
             "correct": False,
             "why": "Evaporating water leaves the dissolved substance behind, "
                    "so the colour would deepen rather than go"},
            {"text": "That all the dissolved copper has been displaced out of "
                     "the solution",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s22",
        "band": "standard",
        "text": "Copper is orange-brown, iron is dark grey, zinc is grey and "
                "magnesium is silvery-grey. A dark grey solid collects on a "
                "magnesium ribbon. Which solution was it in?",
        "options": [
            {"text": "Copper sulfate",
             "correct": False,
             "why": "Copper sulfate would give an orange-brown solid, and the "
                    "blue would fade as it formed"},
            {"text": "Iron sulfate",
             "correct": True},
            {"text": "Magnesium sulfate",
             "correct": False,
             "why": "A metal cannot displace itself, so no solid would appear "
                    "in that tube at all"},
            {"text": "Any of the three, because every displacement leaves a "
                     "dark grey solid whichever metals are involved",
             "correct": False,
             "why": "The solid is the displaced metal, so its colour is that "
                    "metal's colour"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s23",
        "band": "standard",
        "text": "An iron nail is dipped only half-way into copper sulfate "
                "solution. After an hour only the lower half is brown. Why "
                "not the whole nail?",
        "options": [
            {"text": "Because the copper sinks to the bottom of the beaker "
                     "before it can reach the upper half",
             "correct": False,
             "why": "The copper is deposited where the reaction happens, on "
                    "the metal itself, rather than settling out"},
            {"text": "Because only the part touching the solution can react",
             "correct": True},
            {"text": "Because air stops a displacement from running",
             "correct": False,
             "why": "Air takes no part in this reaction either way. What the "
                    "top half is missing is the solution"},
            {"text": "Because the reaction starts at the bottom and would "
                     "reach the top of the nail if it were left overnight",
             "correct": False,
             "why": "The dry half never reacts, however long it is left. "
                    "Nothing travels up the nail"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s24",
        "band": "standard",
        "text": "Zinc displaces copper, and magnesium displaces zinc. What can "
                "you say about magnesium and copper without running that tube?",
        "options": [
            {"text": "Nothing, until that pair has been tested",
             "correct": False,
             "why": "The results already place all three in one order, and an "
                    "order settles every pair in it"},
            {"text": "That magnesium will displace copper",
             "correct": True},
            {"text": "That copper will displace magnesium, because copper is "
                     "the metal at the far end of the two results",
             "correct": False,
             "why": "Being at the far end puts copper at the BOTTOM. It is the "
                    "one that loses to both"},
            {"text": "That neither will displace the other, since they were "
                     "never compared with each other directly",
             "correct": False,
             "why": "A single order settles pairs that were never put in a "
                    "tube together. That is what makes it useful"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s25",
        "band": "standard",
        "text": "Metal X is put into a solution of metal Y's sulfate and a "
                "reaction happens. Which metal is the solid at the end?",
        "options": [
            {"text": "Y",
             "correct": True},
            {"text": "X",
             "correct": False,
             "why": "X is the metal that dissolves. It is the one taking the "
                    "other's place in the compound"},
            {"text": "Both, as a grey mixture of the two",
             "correct": False,
             "why": "Only the displaced metal comes out. The other has gone "
                    "into the solution"},
            {"text": "Neither, because both metals end up dissolved in the "
                     "solution once the reaction has finished",
             "correct": False,
             "why": "A displacement always puts one metal out as a solid. That "
                    "solid is what you see"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s26",
        "band": "standard",
        "text": "A student says the reactivity series must have been copied "
                "out of the periodic table. Give the strongest evidence "
                "against that.",
        "options": [
            {"text": "The series has twelve entries, and the periodic table "
                     "has far more than twelve",
             "correct": False,
             "why": "A short list can be a piece of a long one. What settles "
                    "it is that the order is different"},
            {"text": "The series lists the metals in the order they were "
                     "discovered",
             "correct": False,
             "why": "The series is not a list of discovery dates. Gold and "
                    "copper were known first and both sit near the bottom"},
            {"text": "The series cuts across the table, and it includes two "
                     "substances that are not metals",
             "correct": True},
            {"text": "The periodic table arranges elements by mass, not by "
                     "reactivity",
             "correct": False,
             "why": "The modern table is arranged by atomic number rather than "
                    "by mass, so that reason does not hold"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s27",
        "band": "standard",
        "text": "A works recovers copper from waste copper sulfate solution by "
                "adding scrap metal. Why is scrap iron used rather than scrap "
                "silver?",
        "options": [
            {"text": "Because iron is above copper and silver is below it",
             "correct": True},
            {"text": "Because iron is cheaper than silver, and either metal "
                     "would recover the copper equally well",
             "correct": False,
             "why": "Iron is cheaper, and silver would recover nothing at all. "
                    "Cost is not what decides it"},
            {"text": "Because iron rusts, and a metal that rusts reacts with "
                     "solutions more readily than one that does not",
             "correct": False,
             "why": "Rusting is a reaction with air and water. What matters "
                    "here is where each metal sits in the order"},
            {"text": "Because there is never any silver scrap to use",
             "correct": False,
             "why": "Silver scrap is common. It simply cannot displace copper"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s28",
        "band": "standard",
        "text": "On a completed grid, the magnesium row reads \"displaced "
                "everything\" and the copper row reads \"displaced nothing\". "
                "What do those two rows fix?",
        "options": [
            {"text": "That magnesium is the top of these four and copper is "
                     "the bottom",
             "correct": True},
            {"text": "That magnesium is the top and copper is the bottom of "
                     "the whole reactivity series, not only of these four",
             "correct": False,
             "why": "Four tubes cannot reach past four metals. Potassium is "
                    "above magnesium and gold is below copper"},
            {"text": "That magnesium reacts fastest and copper reacts slowest "
                     "of the four",
             "correct": False,
             "why": "The grid records whether a reaction happened rather than "
                    "how fast. Copper had none to be slow at"},
            {"text": "That the order of the middle two is settled as well, "
                     "since the ends of a list decide everything between them",
             "correct": False,
             "why": "Zinc against iron is a separate tube. The ends of a list "
                    "say nothing about the middle"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s29",
        "band": "standard",
        "text": "Displacements in test tubes are run by classes every week, "
                "but a displacement between two solid powders is never run in "
                "a school laboratory. What is the chemical reason?",
        "options": [
            {"text": "Thermite is a different kind of reaction, and only "
                     "reactions that happen in solution are safe enough for a "
                     "school bench",
             "correct": False,
             "why": "It is the same kind of reaction. What differs is how much "
                    "energy comes out"},
            {"text": "Thermite gives out so much energy that it reaches "
                     "temperatures no school equipment can hold",
             "correct": True},
            {"text": "Thermite takes energy in rather than giving it out, so a "
                     "furnace is needed",
             "correct": False,
             "why": "It gives energy out, which is the whole difficulty. "
                    "Nothing has to be supplied once it is lit"},
            {"text": "Thermite uses aluminium, and aluminium is too expensive "
                     "to be used up in a school lesson",
             "correct": False,
             "why": "Aluminium is one of the cheapest metals there is. The "
                    "objection is the temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-s30",
        "band": "standard",
        "text": "Two unknown metals are tested. P displaces copper from copper "
                "sulfate and Q does not. Which is the more reactive, and how "
                "much does that tell you?",
        "options": [
            {"text": "P, and it tells you only that P is above copper and Q is "
                     "below it",
             "correct": True},
            {"text": "P, and it places both metals exactly in the reactivity "
                     "series, since one tube each is all a metal needs",
             "correct": False,
             "why": "One tube each puts them on either side of copper and no "
                    "closer than that"},
            {"text": "Q, because giving no reaction shows a stronger hold",
             "correct": False,
             "why": "Q has no partner in this tube — it is a metal on its own. "
                    "Giving no reaction puts it below copper"},
            {"text": "Neither can be called more reactive until they are put "
                     "into a solution of each other's sulfate",
             "correct": False,
             "why": "One is above copper and one is below it, so the copper "
                    "tube has already separated them"},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c5-04-h11",
        "band": "harder",
        "text": "Equal pieces of magnesium, zinc and iron are dropped into "
                "separate tubes of copper sulfate solution and the temperature "
                "rise is measured in each. Magnesium gives much the biggest "
                "rise. What does that suggest?",
        "options": [
            {"text": "Magnesium reacts fastest, and a fast reaction must give "
                     "out more energy than a slow one",
             "correct": False,
             "why": "Speed and total energy are separate. A slow reaction can "
                    "give out just as much, spread over longer"},
            {"text": "The further apart two metals are in the reactivity "
                     "series, the more energy the displacement gives out",
             "correct": True},
            {"text": "Magnesium is the only one of the three that is above "
                     "copper in the series",
             "correct": False,
             "why": "Zinc and iron are above copper as well, which is why all "
                    "three tubes warm up at all"},
            {"text": "A lighter metal warms its tube more, and magnesium is "
                     "the lightest of the three",
             "correct": False,
             "why": "How heavy a metal is has nothing to do with the energy "
                    "released. What changed is the gap in reactivity"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h12",
        "band": "harder",
        "text": "Zinc added to dilute hydrochloric acid gives off hydrogen; "
                "copper added to the same acid gives no reaction. Hydrogen "
                "is in the reactivity series. What do those results show?",
        "options": [
            {"text": "That the acid is too weak to attack copper, and a "
                     "stronger one would push the hydrogen out",
             "correct": False,
             "why": "Concentration changes the speed of a reaction that can "
                    "happen. Copper sits below hydrogen at every strength"},
            {"text": "That zinc is a metal and copper is not, so only one of "
                     "them can react with an acid",
             "correct": False,
             "why": "Copper is a metal. It is simply a less reactive one than "
                    "hydrogen"},
            {"text": "That hydrogen is listed only because it is a gas rather "
                     "than because it displaces",
             "correct": False,
             "why": "Hydrogen is in the list because it takes part in "
                    "displacement on the same rule the metals follow"},
            {"text": "That zinc is above hydrogen in the series and copper is "
                     "below it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h13",
        "band": "harder",
        "text": "A stream of hydrogen over hot copper oxide leaves orange-brown "
                "copper behind. The same stream over hot magnesium oxide "
                "leaves the magnesium oxide unchanged. Explain the pair of "
                "results.",
        "options": [
            {"text": "Hydrogen is above copper in the series and far below "
                     "magnesium, so it can take copper's oxygen but not "
                     "magnesium's",
             "correct": True},
            {"text": "Copper oxide is a powder and magnesium oxide a solid "
                     "lump, so only one of them gives the hydrogen a surface "
                     "to reach",
             "correct": False,
             "why": "Both can be used as powders and the results do not "
                    "change. Surface area alters the speed, not the "
                    "direction"},
            {"text": "Magnesium oxide is already an oxide, so it cannot lose "
                     "its oxygen to anything",
             "correct": False,
             "why": "Copper oxide is an oxide too, and it loses its oxygen "
                    "here. What decides it is which element holds oxygen more "
                    "strongly"},
            {"text": "Hydrogen is a gas, so it reacts only with a metal "
                     "compound heated to melting",
             "correct": False,
             "why": "Neither oxide is melted. Both are hot solids, and one of "
                    "them reacts"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h14",
        "band": "harder",
        "text": "A coil of copper wire is left in colourless silver nitrate "
                "solution. Grey needles grow along the wire and the liquid "
                "slowly turns blue. Explain what has happened.",
        "options": [
            {"text": "The nitrate has stained the wire grey, and the copper "
                     "has coloured the liquid as it wears away",
             "correct": False,
             "why": "Nothing is stained. The grey needles are solid silver "
                    "that has come out of the solution"},
            {"text": "Silver is above copper, so the silver has pushed copper "
                     "out of the wire as grey crystals",
             "correct": False,
             "why": "The grey solid is silver and the wire is losing copper, "
                    "so the swap has gone the other way. Copper is the more "
                    "reactive of the two"},
            {"text": "Copper is above silver, so it has displaced the silver, "
                     "and the blue is dissolved copper",
             "correct": True},
            {"text": "The wire has begun to rust, and rust looks grey under a "
                     "colourless solution",
             "correct": False,
             "why": "Only iron and steel rust, and rust is orange-brown. There "
                    "is no iron anywhere in this tube"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h15",
        "band": "harder",
        "text": "A piece of zinc is added to a solution that holds copper "
                "sulfate and magnesium sulfate together. Predict what the zinc "
                "does.",
        "options": [
            {"text": "It displaces both metals, because a metal reacts with "
                     "everything dissolved around it",
             "correct": False,
             "why": "A displacement runs only where the added metal is the "
                    "more reactive one, and zinc is below magnesium"},
            {"text": "It displaces the copper and leaves the dissolved "
                     "magnesium untouched",
             "correct": True},
            {"text": "It displaces the magnesium and leaves the copper, since "
                     "magnesium is the more reactive",
             "correct": False,
             "why": "Being more reactive is what protects magnesium here. Zinc "
                    "cannot push out a metal above it"},
            {"text": "It displaces neither, because two salts in one "
                     "solution cancel out",
             "correct": False,
             "why": "The dissolved copper is still there to be displaced. A "
                    "second salt does not stop it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h16",
        "band": "harder",
        "text": "None of the bench metals — copper, magnesium, zinc or iron — "
                "will get magnesium out of magnesium sulfate solution. Suggest "
                "how magnesium could be obtained from its compounds.",
        "options": [
            {"text": "By heating the solution hard enough that the water "
                     "boils away and the magnesium is left behind as a solid",
             "correct": False,
             "why": "Boiling the water off leaves magnesium sulfate behind, "
                    "partner and all. Heat does not part a metal from its "
                    "partner"},
            {"text": "By adding far more zinc than there is magnesium sulfate, "
                     "so the zinc wins on quantity",
             "correct": False,
             "why": "Quantity does not reverse the order. Zinc is below "
                    "magnesium at any amount"},
            {"text": "By waiting, since a slow reaction between zinc and "
                     "magnesium sulfate finishes eventually",
             "correct": False,
             "why": "There is no slow reaction to wait for. A metal below "
                    "magnesium has no route to displace it"},
            {"text": "By using a metal above magnesium in the series, or by "
                     "using electricity to break the compound apart",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h17",
        "band": "harder",
        "text": "A fifth metal joins the bench and every metal is tested "
                "against every solution. How many tubes are there now, and how "
                "many of them react?",
        "options": [
            {"text": "Twenty-five tubes, of which ten react",
             "correct": True},
            {"text": "Twenty-five tubes, of which twelve react",
             "correct": False,
             "why": "Five metals make ten pairs, and each pair reacts one way "
                    "round only"},
            {"text": "Twenty tubes, of which ten react",
             "correct": False,
             "why": "Every metal goes into every solution, its own included, "
                    "so there are five rows of five"},
            {"text": "Twenty-five tubes, of which twenty react",
             "correct": False,
             "why": "At most half the grid can react, and the five cells down "
                    "the diagonal cannot"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h18",
        "band": "harder",
        "text": "Nickel sits between iron and copper in the reactivity series. "
                "A piece of nickel is put into iron sulfate solution and "
                "another into copper sulfate solution. Predict both results.",
        "options": [
            {"text": "A reaction in both, because nickel is a metal and both "
                     "solutions hold a metal compound",
             "correct": False,
             "why": "Being a metal is not enough. Nickel has to be above the "
                    "dissolved metal, and it is below iron"},
            {"text": "A reaction in the iron sulfate, and nothing in the "
                     "copper sulfate",
             "correct": False,
             "why": "That is the order reversed. Nickel is below iron and "
                    "above copper"},
            {"text": "Nothing in the iron sulfate, and a reaction in the "
                     "copper sulfate",
             "correct": True},
            {"text": "Nothing in either, because a metal from the middle of "
                     "the series is displaced rather than displacing",
             "correct": False,
             "why": "Sitting in the middle means it is above some metals and "
                    "below others. Copper is one it is above"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h19",
        "band": "harder",
        "text": "Three unknown metals are tested. A displaces B from B's "
                "sulfate, and C displaces A from A's sulfate. Put the three in "
                "order, most reactive first.",
        "options": [
            {"text": "A, then B, then C",
             "correct": False,
             "why": "C displaced A, so C belongs above A rather than at the "
                    "bottom"},
            {"text": "C, then A, then B",
             "correct": True},
            {"text": "B, then A, then C",
             "correct": False,
             "why": "That is the order upside down. The metal that does the "
                    "displacing is the more reactive one"},
            {"text": "A, then C, then B",
             "correct": False,
             "why": "A is above B, but C displaced A, so C has to come above A "
                    "as well"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h20",
        "band": "harder",
        "text": "A student records no reaction for a magnesium ribbon in "
                "copper sulfate solution, though every other group saw a brown "
                "solid within a minute. The ribbon was dull and grey going in. "
                "Suggest the reason.",
        "options": [
            {"text": "Magnesium and copper are too far apart in the series for "
                     "a reaction to run between them",
             "correct": False,
             "why": "A wide gap makes a reaction more vigorous, not less. "
                    "Magnesium displaces copper readily"},
            {"text": "The copper sulfate had been used by an earlier class, so "
                     "the copper dissolved in it had all been displaced "
                     "already",
             "correct": False,
             "why": "Every other group drew the same solution and saw a "
                    "reaction. A used-up one would be colourless"},
            {"text": "Magnesium reacts so fast that the copper had fallen off "
                     "before the tube was looked at",
             "correct": False,
             "why": "Copper that had come out would be lying in the tube as a "
                    "brown sludge. Nothing was seen at all"},
            {"text": "The ribbon carried a dull coating that had not been "
                     "cleaned off, so the metal was not touching the solution",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h21",
        "band": "harder",
        "text": "Metal X is tested both ways: it displaces none of the four "
                "bench metals from their solutions, and none of them displaces "
                "X from X's sulfate. Both sets of tubes were run properly. "
                "What should be concluded?",
        "options": [
            {"text": "The two sets of results contradict each other, so at "
                     "least one of them is wrong",
             "correct": True},
            {"text": "That X sits exactly in the middle of the four, neither "
                     "above them nor below them",
             "correct": False,
             "why": "Every metal is above or below every other one. No "
                    "position leaves both sets of tubes empty"},
            {"text": "That X takes no part in displacement, so it cannot be "
                     "placed in the order at all",
             "correct": False,
             "why": "A metal below all four would still be displaced BY all "
                    "four, so the second set should have reacted"},
            {"text": "That X is the most reactive metal on the bench, since "
                     "nothing could displace it",
             "correct": False,
             "why": "Then X would have displaced all four in the first set. "
                    "Being on top gives reactions, not silence"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h22",
        "band": "harder",
        "text": "A student says it is circular to predict the grid from the "
                "reactivity series and then treat the grid as support for the "
                "series. What is the strongest reply?",
        "options": [
            {"text": "That a prediction is not meant to be tested, only used "
                     "to save running tubes",
             "correct": False,
             "why": "A prediction nothing could contradict would be worth "
                    "nothing. Being testable is what makes it useful"},
            {"text": "That the student is right, so the list should be put "
                     "away until the grid is finished",
             "correct": False,
             "why": "The grid agreeing with an order measured elsewhere is "
                    "evidence. Hiding the list throws that check away"},
            {"text": "That the prediction could have failed and did not, and "
                     "the list was itself built from results of this kind",
             "correct": True},
            {"text": "That the series is read off the periodic table, so the "
                     "list and the grid have separate origins",
             "correct": False,
             "why": "The order is not read off the periodic table. Potassium "
                    "and sodium share a group and calcium is in another"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h23",
        "band": "harder",
        "text": "A student mixes iron powder with aluminium oxide in a "
                "crucible and lights it, expecting molten metal to pour out. "
                "Predict what happens.",
        "options": [
            {"text": "A vigorous reaction, since a metal and a metal oxide are "
                     "both in the crucible",
             "correct": False,
             "why": "Which metal is holding the oxygen is the whole question. "
                    "Here the oxygen is already held by the more reactive of "
                    "the two"},
            {"text": "Nothing — iron is below aluminium, so it cannot take the "
                     "oxygen from aluminium oxide",
             "correct": True},
            {"text": "A slower reaction, because iron carries less energy "
                     "than aluminium",
             "correct": False,
             "why": "There is no slow version. The reaction has no route to "
                    "run in that direction at any speed"},
            {"text": "Molten aluminium pours out, leaving iron oxide in the "
                     "crucible",
             "correct": False,
             "why": "That would need iron to displace aluminium, which is "
                    "above it. The mixture simply sits there"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h24",
        "band": "harder",
        "text": "0.24 g of magnesium ribbon displaces 0.64 g of copper from "
                "copper sulfate solution. What mass of copper would 0.72 g of "
                "the same ribbon displace, given plenty of solution?",
        "options": [
            {"text": "1.92 g",
             "correct": True},
            {"text": "0.64 g",
             "correct": False,
             "why": "Three times the magnesium displaces three times the "
                    "copper. The solution is not the limit here"},
            {"text": "2.16 g",
             "correct": False,
             "why": "That is three times the mass of the magnesium rather than "
                    "three times the mass of the copper"},
            {"text": "0.21 g",
             "correct": False,
             "why": "That divides where it should multiply. More magnesium "
                    "displaces more copper, not less"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h25",
        "band": "harder",
        "text": "An iron nail is left in copper sulfate solution until no blue "
                "is left in the liquid. A second nail is then added and left "
                "another day. Predict what the second nail does.",
        "options": [
            {"text": "It plates with copper as well, since there is twice as "
                     "much iron in the tube now",
             "correct": False,
             "why": "Iron is not what has run out. The dissolved copper has "
                    "already all been displaced"},
            {"text": "It dissolves faster than the first did, because the "
                     "liquid is now iron sulfate",
             "correct": False,
             "why": "Iron cannot displace itself from its own sulfate. The "
                    "second nail has nothing to react with"},
            {"text": "It turns the liquid blue again by putting the copper "
                     "back into solution",
             "correct": False,
             "why": "Displacement runs one way only. Iron cannot push copper "
                    "back into solution"},
            {"text": "Nothing, because there is no dissolved copper left for "
                     "it to displace",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h26",
        "band": "harder",
        "text": "Two tubes of copper sulfate are set up with the same mass of "
                "zinc: one as a single strip, one as a powder. Describe how "
                "the two reactions differ.",
        "options": [
            {"text": "The powder displaces more copper, because more of its "
                     "metal is in contact with the solution",
             "correct": False,
             "why": "Contact area sets the speed. How much copper comes out is "
                    "set by how much was dissolved"},
            {"text": "The powder finishes much sooner, and both tubes end with "
                     "the same amount of copper",
             "correct": True},
            {"text": "The strip displaces more copper, because a solid piece "
                     "holds together long enough to finish",
             "correct": False,
             "why": "Both hold the same mass of zinc and both can finish. "
                    "Shape does not change the amount"},
            {"text": "The powder reacts and the strip does not, since a strip "
                     "is too large a piece to react",
             "correct": False,
             "why": "A strip reacts perfectly well, as the bench grid shows. "
                    "It is simply slower"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h27",
        "band": "harder",
        "text": "20 cm3 of copper sulfate solution gives 0.25 g of copper when "
                "excess iron is added. What mass of copper would 60 cm3 of the "
                "same solution give with excess iron?",
        "options": [
            {"text": "0.25 g",
             "correct": False,
             "why": "Three times the volume holds three times the dissolved "
                    "copper, and the iron is in excess in both"},
            {"text": "0.08 g",
             "correct": False,
             "why": "More solution gives more copper, not less. That divides "
                    "where it should multiply"},
            {"text": "0.75 g",
             "correct": True},
            {"text": "0.50 g",
             "correct": False,
             "why": "That doubles the copper when the volume was trebled"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h28",
        "band": "harder",
        "text": "A colourless solution is known to be either zinc sulfate or "
                "magnesium sulfate. Only magnesium ribbon and copper wire are "
                "available. Which test identifies it?",
        "options": [
            {"text": "Put the magnesium in: a grey solid means zinc sulfate, "
                     "and no change means magnesium sulfate",
             "correct": True},
            {"text": "Put the copper in: a reaction means zinc sulfate, and no "
                     "reaction means magnesium sulfate",
             "correct": False,
             "why": "Copper is below both metals, so nothing happens either "
                    "way and the tube says nothing"},
            {"text": "Put the magnesium in: any warming means magnesium "
                     "sulfate, since a metal warms its own solution",
             "correct": False,
             "why": "A metal in its own solution has nobody to displace, so "
                    "nothing happens and nothing warms"},
            {"text": "Neither metal settles it, because both solutions are "
                     "colourless and only a colour change counts as evidence",
             "correct": False,
             "why": "A grey solid appearing on the ribbon is evidence every "
                    "bit as good as a colour change"},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h29",
        "band": "harder",
        "text": "A nail is weighed, left in copper sulfate until it is fully "
                "coated, then rinsed, dried and weighed again. Some brown "
                "solid is lying at the bottom of the tube. What does that do "
                "to the measured mass gain?",
        "options": [
            {"text": "Nothing, because the solid at the bottom came out of the "
                     "nail rather than out of the solution",
             "correct": False,
             "why": "All of the copper came out of the solution. Copper that "
                    "has fallen off is copper the balance never sees"},
            {"text": "It makes the gain larger, since loose copper in the tube "
                     "adds to what the nail weighs",
             "correct": False,
             "why": "Only the nail goes on the balance. Anything lying in the "
                    "tube is left behind"},
            {"text": "It makes no difference as long as the nail has been "
                     "rinsed and dried carefully",
             "correct": False,
             "why": "Rinsing removes solution, not the missing copper. The "
                    "lost solid is still absent from the reading"},
            {"text": "It makes the gain smaller than it should be, because "
                     "some displaced copper is not on the nail",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-04-h30",
        "band": "harder",
        "text": "On a finished grid the cell for copper in copper sulfate and "
                "the cell for copper in zinc sulfate both read none. Explain "
                "why those two blanks do not mean the same thing.",
        "options": [
            {"text": "They do mean the same, because a blank cell is a blank "
                     "cell however it was produced",
             "correct": False,
             "why": "A result is an answer to what the tube asked, and those "
                    "two tubes asked different questions"},
            {"text": "One had no other metal to displace; the other held one "
                     "copper is not reactive enough to displace",
             "correct": True},
            {"text": "One is a failed experiment and the other is a real "
                     "result",
             "correct": False,
             "why": "Neither is a failure. A test that cannot give a result is "
                    "still evidence about the order"},
            {"text": "One means copper is too weak a metal to react at all, "
                     "and the other means that particular solution was too "
                     "dilute",
             "correct": False,
             "why": "Every cell used the same dilution, and copper is not "
                    "weak — it is simply the lowest of the four"},
        ],
        "figure": None,
    },
]
