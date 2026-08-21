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
]
