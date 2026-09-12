"""C3 lesson 02 — Dissolving and solutions: twelve questions.

The lesson's argument is a split: stirring and grinding change HOW FAST a
solute dissolves, and only the solute and the temperature change HOW MUCH can
dissolve at all. These twelve probe the split from the angles the ladder leaves
alone — what the balance reads, what grinding buys you, what a saturated
solution does when you attack it, and what happens to the rule "hot water
dissolves more" when you point it at salt or at a gas.

The distractors are built from the lesson's three declared misconceptions.
MIX-03 (dissolving destroys the solute, or turns it into liquid) drives the
wrong options in e01, e02, h01 and h02 — every one of them treats a solute you
cannot see as a solute that is no longer there. MIX-04 (stirring harder makes
more dissolve) drives e03, s01, s04 and h03, where a dial that belongs to the
clock is imagined moving the grams. MIX-05 (dissolving is melting) drives s03,
h01 and h04, where the water is imagined heating the solid from the inside.

A fourth strand runs through the lesson and is not in the register: "hot water
dissolves more" taken as a law rather than a rough rule about solids. Salt
(35.8 g cold, 38.1 g hot) and the dissolved gases are the two counter-examples,
and s02 and h02 are built on them.

⚠️ Every figure quoted here is the figure the bench computes — 240 g of sugar
in 100 g of water at 40 °C, 35.8 g and 38.1 g of salt at 10 °C and 80 °C, and
190 g and 360 g of sugar at the same two temperatures. If the bench payload
ever moves, these move with it: the instrument is the measurement.
"""

UNIT = "C3"
LESSON = "dissolving-and-solutions"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-02-e01",
        "band": "easier",
        "text": "20 g of salt is stirred into 100 g of water on a balance, "
                "until every grain has disappeared. What does the balance "
                "read now?",
        "options": [
            {"text": "120 g", "correct": True},
            {"text": "100 g", "correct": False,
             "why": "Nothing was destroyed. The salt is still in the beaker, "
                    "broken up into particles too small to see — and a "
                    "particle you cannot see still weighs what it weighed."},
            {"text": "110 g", "correct": False,
             "why": "None of the salt is lost, so there is no reason for half "
                    "of it to survive. All 20 g is in there, spread through "
                    "the water."},
            {"text": "140 g", "correct": False,
             "why": "Dissolving does not make anything. Nothing is added to "
                    "the beaker except the 20 g of salt, so the reading goes "
                    "up by exactly 20 g."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e02",
        "band": "easier",
        "text": "Sugar is stirred into a cup of tea until you cannot see it "
                "any more. Which part of that is the solute?",
        "options": [
            {"text": "The tea", "correct": False,
             "why": "The tea is the liquid doing the dissolving, which makes "
                    "it the solvent. The solute is the substance that "
                    "dissolves in it."},
            {"text": "The sugar", "correct": True},
            {"text": "The sweetened tea", "correct": False,
             "why": "That is the solution — the solute and the solvent "
                    "together, once they are mixed. The solute is just the "
                    "part that dissolved."},
            {"text": "Nothing — the sugar has gone", "correct": False,
             "why": "Taste it. Every particle of sugar is still in the cup, "
                    "spread evenly through the tea, which is exactly why "
                    "every mouthful is sweet."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e03",
        "band": "easier",
        "text": "Salt disappears sooner when the water is stirred than when "
                "it is left to stand. What else does stirring change?",
        "options": [
            {"text": "It gets more salt in than leaving it to stand would",
             "correct": False,
             "why": "Stirring only moves fresh water past the solid faster. "
                    "The amount that can dissolve is set by the solute and "
                    "the temperature, and a spoon reaches neither."},
            {"text": "Nothing else — stirring changes how fast, not how much",
             "correct": True},
            {"text": "It lifts the limit a little, so a bit more salt fits in",
             "correct": False,
             "why": "The limit does not move at all. Stir a saturated "
                    "solution for an hour and the solid on the bottom is "
                    "still there when you stop."},
            {"text": "It warms the water enough to melt the salt into it",
             "correct": False,
             "why": "A spoon does not warm water in any way you could "
                    "measure, and salt melts at about 800 °C. Stirring moves "
                    "water; it does not heat it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e04",
        "band": "easier",
        "text": "Sand is stirred into water for five minutes. The water goes "
                "cloudy, and then the sand settles on the bottom. Which word "
                "describes the sand?",
        "options": [
            {"text": "Soluble", "correct": False,
             "why": "A soluble solid disappears into the water and stays "
                    "there. This one went cloudy and then came back down, "
                    "which is what insoluble looks like."},
            {"text": "Saturated", "correct": False,
             "why": "Saturated describes a solution that is holding as much "
                    "as it can. Nothing here dissolved at all, so there is no "
                    "solution to be saturated."},
            {"text": "A solvent", "correct": False,
             "why": "The solvent is the liquid doing the dissolving — here, "
                    "the water. The sand is the solid that refused to "
                    "dissolve in it."},
            {"text": "Insoluble", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-02-s01",
        "band": "standard",
        "text": "A lump of sugar is ground to a powder before it is dropped "
                "into cold water. What difference does the grinding make?",
        "options": [
            {"text": "It dissolves sooner, and more of it dissolves in the "
                     "end", "correct": False,
             "why": "Only the first half of that is right. Grinding gives the "
                    "water more surface to work on, which is a change to the "
                    "clock — the grams are set by the solute and the "
                    "temperature."},
            {"text": "More of it dissolves, though it takes just as long",
             "correct": False,
             "why": "This has the two halves the wrong way round. Grinding "
                    "changes the time and nothing else; the amount that can "
                    "dissolve is untouched by it."},
            {"text": "It dissolves sooner; the same amount goes in either way",
             "correct": True},
            {"text": "It lowers the temperature the sugar needs to dissolve "
                     "at", "correct": False,
             "why": "Sugar dissolves in cold water already — there is no "
                    "temperature it has to reach. Grinding changes how "
                    "quickly the water can get at it, and that is all."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s02",
        "band": "standard",
        "text": "100 g of water takes 35.8 g of salt at 10 °C and 38.1 g at "
                "80 °C. The same 100 g of water takes 190 g of sugar at "
                "10 °C and 360 g at 80 °C. What do those four numbers show "
                "together?",
        "options": [
            {"text": "Temperature changes how much dissolves, and by how "
                     "much depends on the solute", "correct": True},
            {"text": "Hot water dissolves more of everything, by about the "
                     "same amount each time", "correct": False,
             "why": "Look at the size of the two jumps. Sugar nearly doubles; "
                    "salt moves by about two grams. Same water, same "
                    "temperatures, completely different answers."},
            {"text": "Sugar is the odd one out, and every other solute "
                     "behaves the way salt does", "correct": False,
             "why": "Neither one is the odd one out. There is no general "
                    "rule to be the exception to — the temperature effect is "
                    "a property of each solute."},
            {"text": "The salt must have been stirred less thoroughly than "
                     "the sugar was", "correct": False,
             "why": "Stirring cannot appear in these numbers at all. It "
                    "changes how long the solute takes to disappear, never "
                    "how many grams go in."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s03",
        "band": "standard",
        "text": "Sugar melts at about 186 °C, and it dissolves perfectly well "
                "in cold tap water. Why is dissolving not melting?",
        "options": [
            {"text": "They are one change with two names: melting for a "
                     "solid, dissolving for a liquid", "correct": False,
             "why": "They are two different events with two different causes. "
                    "Melting needs heat and nothing else; dissolving needs a "
                    "solvent and no particular heat at all."},
            {"text": "Dissolving is melting, only slower, because the water "
                     "is cold rather than hot", "correct": False,
             "why": "Cold water is nowhere near 186 °C, and no amount of "
                    "waiting will take it there. The sugar is being spread "
                    "through the water, not heated by it."},
            {"text": "The water heats the sugar to its melting point from "
                     "the inside, grain by grain", "correct": False,
             "why": "Nothing in the beaker is hot. Water at room temperature "
                    "cannot bring anything to 186 °C, and melted sugar goes "
                    "brown and turns to caramel — this stays clear."},
            {"text": "Dissolving needs a solvent, and it happens far below "
                     "the melting point", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s04",
        "band": "standard",
        "text": "No more sugar will dissolve in a beaker of water at 40 °C, "
                "and there is undissolved sugar sitting on the bottom. Which "
                "change would get more of it in?",
        "options": [
            {"text": "Stirring it harder", "correct": False,
             "why": "Stirring gets a solute to its limit sooner. This "
                    "solution is already at its limit, so there is nowhere "
                    "for the sugar on the bottom to go."},
            {"text": "Warming the water", "correct": True},
            {"text": "Grinding the sugar on the bottom", "correct": False,
             "why": "Grinding is the other way of speeding a solute up, and "
                    "speed is not the problem here. The water is holding as "
                    "much as it can hold at 40 °C."},
            {"text": "Adding more sugar", "correct": False,
             "why": "More solute cannot help when the solvent is full. The "
                    "extra would settle on top of what is already sitting "
                    "there."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-02-h01",
        "band": "harder",
        "text": "15 g of salt is dissolved in 200 g of water. The beaker is "
                "left on a sunny windowsill until all the water has gone, "
                "leaving white crystals behind. What do the crystals weigh?",
        "options": [
            {"text": "0 g", "correct": False,
             "why": "The crystals are the salt, back where it started. "
                    "Dissolving hid it and the water leaving has un-hidden "
                    "it; at no point was any of it destroyed."},
            {"text": "7.5 g", "correct": False,
             "why": "Nothing about dissolving costs you half of a solute. "
                    "Every gram that went into the water comes back out of "
                    "it when the water goes."},
            {"text": "15 g", "correct": True},
            {"text": "215 g", "correct": False,
             "why": "The water has left the beaker — that is why the "
                    "crystals are dry. What stays behind is the salt alone, "
                    "and the salt weighed 15 g."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h02",
        "band": "harder",
        "text": "A shallow river in a heatwave holds less dissolved oxygen "
                "than the same river in winter, and a warm fizzy drink goes "
                "flat faster than a cold one. What do those two facts show?",
        "options": [
            {"text": "Gases get less soluble as the water warms — the "
                     "opposite way round to sugar", "correct": True},
            {"text": "Gases behave just as sugar does, so warm water holds "
                     "more of them", "correct": False,
             "why": "Then a warm drink would keep its fizz better than a cold "
                    "one, and it does not. Solids and gases go opposite ways "
                    "as the temperature rises."},
            {"text": "The warmth destroys the dissolved gas rather than "
                     "letting it go", "correct": False,
             "why": "The gas is not destroyed — it leaves. That is what the "
                    "bubbles rising out of a warm drink are, and it is why "
                    "the drink beside them tastes flat."},
            {"text": "Warm water evaporates, and it takes the dissolved gas "
                     "up with it", "correct": False,
             "why": "The gas escapes on its own, from water that is nowhere "
                    "near boiling. Warm water simply cannot hold as much "
                    "dissolved gas as cold water can."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h03",
        "band": "harder",
        "text": "Two students each tip 300 g of sugar into 100 g of water at "
                "40 °C, where 240 g of sugar can dissolve. One stirs hard "
                "for ten minutes; the other leaves the beaker standing for "
                "two hours. Compare what they end up with.",
        "options": [
            {"text": "The one who stirred ends up with all 300 g in, and the "
                     "one who waited with 240 g", "correct": False,
             "why": "Stirring is a change to the clock. It got that student "
                    "to the same 240 g sooner, and the 60 g the water cannot "
                    "hold is on the bottom of both beakers."},
            {"text": "Both end up with all 300 g dissolved, because two "
                     "hours is long enough for anything", "correct": False,
             "why": "Time is not the barrier once a solution is saturated. "
                    "At 40 °C the water holds 240 g however long you leave "
                    "it, and the rest simply sits there."},
            {"text": "The one who waited ends up with more in, because time "
                     "does what stirring cannot", "correct": False,
             "why": "Neither of them beats the limit. Waiting and stirring "
                    "are two routes to the same 240 g — one of them is just "
                    "quicker to arrive."},
            {"text": "Both have 240 g in and 60 g left over; the stirrer got "
                     "there sooner", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h04",
        "band": "harder",
        "text": "Nail varnish will not dissolve in water, but it dissolves "
                "easily in nail varnish remover. What does that tell you "
                "about the word insoluble?",
        "options": [
            {"text": "It means the same thing whichever liquid you try, so "
                     "the remover cannot count", "correct": False,
             "why": "The remover counts: it is a solvent, exactly as water "
                    "is. Insoluble in water and insoluble in everything are "
                    "two very different claims."},
            {"text": "It only means anything once you say which solvent",
             "correct": True},
            {"text": "The remover melts the varnish instead of dissolving "
                     "it, so it is a different change", "correct": False,
             "why": "Nothing here is hot enough to melt anything. The varnish "
                    "is being spread through the remover as particles — that "
                    "is dissolving, in a solvent that is not water."},
            {"text": "The remover dissolves absolutely anything, so it is "
                     "not a fair comparison", "correct": False,
             "why": "It dissolves varnish and it would leave sand or chalk "
                    "sitting there. Every solvent has its own list, which is "
                    "why the solvent has to be named."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-02-e05",
        "band": "easier",
        "text": "What does it mean to say a solution is saturated?",
        "options": [
            {"text": "No more solute will dissolve in it at that temperature",
             "correct": True},
            {"text": "It has been stirred for so long that every last grain "
                     "of the solid has finally been broken up and spread out",
             "correct": False,
             "why": "Stirring changes how fast, never how much. A saturated "
                    "solution stays saturated however long you stir it"},
            {"text": "It is completely full to the top of the beaker",
             "correct": False,
             "why": "The word is about how much solute the liquid holds, not "
                    "about how full the glass is"},
            {"text": "The solute in it has stopped moving about",
             "correct": False,
             "why": "Dissolved particles never stop moving. Saturated means "
                    "no more can join them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e06",
        "band": "easier",
        "text": "Grease will not dissolve in water, but it dissolves easily "
                "in white spirit. What is the white spirit called?",
        "options": [
            {"text": "The solute, because it is the substance doing the work "
                     "of breaking the grease up and carrying it away",
             "correct": False,
             "why": "The solute is the thing that dissolves — here, the "
                    "grease. The liquid it dissolves in is the solvent"},
            {"text": "The solvent",
             "correct": True},
            {"text": "The solution",
             "correct": False,
             "why": "The solution is the two of them together, once the "
                    "grease has dissolved in the spirit"},
            {"text": "The filtrate",
             "correct": False,
             "why": "That word belongs to filtering. It is the liquid that "
                    "passes through the paper"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e07",
        "band": "easier",
        "text": "A solution is described as even. What does that mean?",
        "options": [
            {"text": "It has the same amount of solvent as it has solute, "
                     "measured out carefully before the two were mixed",
             "correct": False,
             "why": "The amounts do not have to match at all. Even is about "
                    "the spread, not the recipe"},
            {"text": "It has been left standing until the solute has settled "
                     "flat",
             "correct": False,
             "why": "A solute that settles has not dissolved. A solution "
                    "never settles out"},
            {"text": "Every spoonful of it holds the same amount of solute",
             "correct": True},
            {"text": "Its surface is flat and level in the beaker",
             "correct": False,
             "why": "Every liquid's surface is level. The word is about what "
                    "is in it, not about its shape"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e08",
        "band": "easier",
        "text": "100 g of water takes 35.8 g of salt at 10 °C and 38.1 g at "
                "80 °C. What does that pair of numbers show about salt?",
        "options": [
            {"text": "That salt dissolves far better in hot water, which is "
                     "why it goes into a hot pan so much faster than a cold "
                     "one",
             "correct": False,
             "why": "The difference is about 2 g in 36 — barely anything. "
                    "Going in FASTER is a different question from how much "
                    "goes in"},
            {"text": "That salt becomes less soluble as the water is heated",
             "correct": False,
             "why": "38.1 is larger than 35.8, so it goes very slightly the "
                    "other way. Gases are the ones that fall"},
            {"text": "That salt stops dissolving completely above 80 °C",
             "correct": False,
             "why": "Nothing in these two numbers says anything about "
                    "temperatures above 80 °C"},
            {"text": "Heating the water hardly changes how much salt will "
                     "dissolve",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-02-s05",
        "band": "standard",
        "text": "Two beakers each hold 100 g of water — one at 20 °C, one at "
                "80 °C — and 300 g of sugar is tipped into each. What is on "
                "the bottom of each afterwards?",
        "options": [
            {"text": "More undissolved sugar in the cold beaker",
             "correct": True},
            {"text": "Nothing in either, because sugar dissolves completely "
                     "in water at any temperature you can reach in a beaker",
             "correct": False,
             "why": "There is a limit at every temperature. 300 g is well "
                    "past it in cold water"},
            {"text": "More undissolved sugar in the hot beaker",
             "correct": False,
             "why": "The wrong way round for a solid. Hot water takes nearly "
                    "twice as much sugar as cold"},
            {"text": "The same amount in each, because both hold 100 g of "
                     "water",
             "correct": False,
             "why": "The amount of water is the same and the temperature is "
                    "not, and temperature is what changes the limit"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s06",
        "band": "standard",
        "text": "Calcium sulfate gets slightly LESS soluble as water warms, "
                "which is why it plates out inside hot pipes. What does that "
                "do to the rule “hot water dissolves more”?",
        "options": [
            {"text": "It disproves it, so the rule should be replaced by "
                     "“cold water dissolves more” instead",
             "correct": False,
             "why": "That would be just as wrong in the other direction. "
                    "Sugar really does go in better hot"},
            {"text": "It shows the rule is a rough one about solids, with "
                     "exceptions in both directions",
             "correct": True},
            {"text": "Nothing — calcium sulfate is an exception and a rule is "
                     "allowed one",
             "correct": False,
             "why": "It is not a lone exception. Salt barely changes, and "
                    "every gas runs the other way"},
            {"text": "It shows calcium sulfate is insoluble",
             "correct": False,
             "why": "It dissolves, or there would be nothing in the water to "
                    "plate out on the pipe"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s07",
        "band": "standard",
        "text": "A beaker holds a clear sugar solution. How would you get the "
                "sugar back as a solid?",
        "options": [
            {"text": "Filter it through a fine paper, which holds the sugar "
                     "back and lets the water run through into a flask below",
             "correct": False,
             "why": "Dissolved sugar is single particles, far smaller than "
                    "any gap in a paper. It goes straight through"},
            {"text": "Cool it in a fridge until the sugar sinks",
             "correct": False,
             "why": "Cooling brings some out of a saturated solution, and "
                    "most of it stays dissolved. It does not all sink"},
            {"text": "Evaporate the water and leave the sugar behind",
             "correct": True},
            {"text": "Stir it hard in the opposite direction",
             "correct": False,
             "why": "Nothing about stirring undoes dissolving. Direction is "
                    "not a variable here"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s08",
        "band": "standard",
        "text": "Which of these is a solution?",
        "options": [
            {"text": "Sand stirred into water, which goes cloudy at first and "
                     "then settles out into a layer on the bottom",
             "correct": False,
             "why": "Sand is insoluble. Anything that settles out has not "
                    "dissolved"},
            {"text": "Chalk powder shaken up in water",
             "correct": False,
             "why": "Also insoluble — that is why it goes cloudy rather than "
                    "clear"},
            {"text": "Oil floating on water",
             "correct": False,
             "why": "It is a mixture, but the oil has not dissolved. You can "
                    "see the two layers"},
            {"text": "Sea water",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-02-h05",
        "band": "harder",
        "text": "100 g of water at 40 °C dissolves 240 g of sugar. How much "
                "sugar will dissolve in 50 g of water at the same "
                "temperature?",
        "options": [
            {"text": "120 g",
             "correct": True},
            {"text": "240 g, because the temperature has not changed and the "
                     "temperature is what sets the limit",
             "correct": False,
             "why": "Temperature sets how much goes into a GIVEN amount of "
                    "water. Half the water holds half as much"},
            {"text": "480 g",
             "correct": False,
             "why": "That is doubling where you should halve. Less solvent "
                    "means less solute"},
            {"text": "190 g",
             "correct": False,
             "why": "190 g is the figure for 100 g of water at 10 °C. It is "
                    "the wrong temperature and the wrong amount of water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h06",
        "band": "harder",
        "text": "A saturated salt solution made in 100 g of water at 80 °C is cooled to 10 °C. Salt goes from 38.1 g to 35.8 g per 100 g of water. What happens?",
        "options": [
            {
             "text": "All 38.1 g comes out, because a cold solution cannot hold any salt at all",
             "correct": False,
             "why": "Cold water holds 35.8 g perfectly well. Only what no longer fits comes out",
            },
            {
             "text": "About 2.3 g of salt comes out of solution",
             "correct": True,
            },
            {
             "text": "Nothing comes out, because the salt is already dissolved and dissolved salt stays dissolved however cold it gets",
             "correct": False,
             "why": "A solution that becomes over-full does drop its excess. Here it is a small amount, not none",
            },
            {
             "text": "About 2.3 g of water evaporates instead",
             "correct": False,
             "why": "Cooling does not drive water off. It is the salt that no longer fits",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h07",
        "band": "harder",
        "text": "Solution A is 10 g of salt in 100 g of water. Solution B is 10 g of salt in 200 g of water. How do they compare?",
        "options": [
            {
             "text": "A holds more salt than B, because the same mass of salt in less water counts as a larger amount of solute",
             "correct": False,
             "why": "Both hold exactly 10 g of salt. What differs is how much water it is spread through",
            },
            {
             "text": "B holds more salt, because there is more water for it to dissolve in",
             "correct": False,
             "why": "More water could hold more, but only 10 g was added. Capacity is not the same as contents",
            },
            {
             "text": "They hold the same mass of salt, and B is more dilute",
             "correct": True,
            },
            {
             "text": "They are identical in every way, because the same salt was used",
             "correct": False,
             "why": "The same salt is spread through twice as much water in B, so the two solutions are not identical",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h08",
        "band": "harder",
        "text": "Two cans of the same drink are opened at the same "
                "moment; one is left in a warm room and one in a "
                "fridge. The warm one goes flat first. Why?",
        "options": [
            {"text": "The carbon dioxide reacts with the air, and the "
                     "products of that reaction are what escape from the open "
                     "can",
             "correct": False,
             "why": "Nothing reacts. The gas that leaves is the same carbon "
                    "dioxide that was dissolved in it"},
            {"text": "The drink evaporates, and what is left is too "
                     "concentrated to hold any gas",
             "correct": False,
             "why": "Very little liquid is lost in an hour, and the drink "
                    "would still be fizzy if it were"},
            {"text": "The bubbles were made by the can rather than by "
                     "anything dissolved in the drink",
             "correct": False,
             "why": "The can holds nothing but the drink. The gas was "
                    "dissolved in the liquid all along"},
            {"text": "Gas was dissolved in it, and gases become less soluble "
                     "as the liquid warms",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ────────────────────────────────────────
    {
        "id": "c3-02-e09",
        "band": "easier",
        "text": "Hot chocolate powder is stirred into a mug of hot milk and a mug of cold milk, both for the same time. Which mug has more powder left undissolved?",
        "options": [
            {
             "text": "The cold one — the powder dissolves more slowly in cold milk",
             "correct": True,
            },
            {
             "text": "The hot one, because heat destroys some of the powder before it can dissolve",
             "correct": False,
             "why": "Nothing is destroyed by warm milk. The powder is still there, just slower to disappear in the cold mug.",
            },
            {
             "text": "Neither — both dissolve at exactly the same rate in water of any temperature",
             "correct": False,
             "why": "Temperature does change the rate, which is why the same stirring time gives two different results here.",
            },
            {
             "text": "The hot one, because heat makes cocoa powder insoluble",
             "correct": False,
             "why": "Cocoa powder is soluble at any drinkable temperature. Heat speeds it up rather than stopping it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e10",
        "band": "easier",
        "text": "A vitamin C tablet dissolves faster when it is crushed "
                "to a powder first than when it is dropped in whole. "
                "Why?",
        "options": [
            {"text": "Crushing turns the tablet into a different, more "
                     "soluble substance", "correct": False,
             "why": "Crushing changes the shape, not the substance. The "
                    "same tablet, ground up, is still the same tablet."},
            {"text": "Crushing gives the water more surface to work on "
                     "at once", "correct": True},
            {"text": "Crushing removes some of the tablet before it goes "
                     "in the water", "correct": False,
             "why": "None of it is lost by crushing. All of it still "
                    "ends up dissolved either way."},
            {"text": "Crushed powder weighs less than a whole tablet",
             "correct": False,
             "why": "Crushing does not change the mass at all. It only "
                    "changes how quickly the water can reach it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e11",
        "band": "easier",
        "text": "An aquarium pump bubbles air through the tank water all day. Does that raise the most oxygen the water could ever hold, or just get the water there faster?",
        "options": [
            {
             "text": "It raises the maximum the water can hold",
             "correct": False,
             "why": "The maximum is set by the water's temperature, not by how the air reaches it.",
            },
            {
             "text": "It does neither — bubbling air through water has no effect on the dissolved oxygen",
             "correct": False,
             "why": "It does have an effect. More contact with the air means the water reaches its maximum sooner.",
            },
            {
             "text": "Just gets the water to its existing maximum faster",
             "correct": True,
            },
            {
             "text": "It lowers the maximum, because bubbles push dissolved oxygen back out",
             "correct": False,
             "why": "The bubbles bring oxygen in rather than pushing it out. The tank ends up with more dissolved oxygen, not less.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e12",
        "band": "easier",
        "text": "Washing powder dissolves faster in a hot wash than in a cold wash. A normal dose is nowhere near enough to saturate the water. Does the hot wash fit more washing powder into the same water?",
        "options": [
            {
             "text": "Yes — hot water always dissolves more of everything",
             "correct": False,
             "why": "Salt barely changes with temperature at all. Heat does not raise the limit for every solute.",
            },
            {
             "text": "Yes — a hot wash needs far more powder than a cold one to work",
             "correct": False,
             "why": "The recommended amount of powder is set by the washing job, not by the water temperature.",
            },
            {
             "text": "No — a cold wash and a hot wash dissolve exactly the same amount in exactly the same time",
             "correct": False,
             "why": "The times differ. A hot wash gets the powder dissolved sooner.",
            },
            {
             "text": "No — the heat mainly speeds up how fast it disappears, not how much can go in",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e13",
        "band": "easier",
        "text": "A hot, saturated sugar solution is left to cool slowly "
                "with a string hanging in it. Sugar crystals grow on the "
                "string as it cools. Where did that extra sugar come "
                "from?",
        "options": [
            {"text": "It was already dissolved in the hot solution and "
                     "came out as the water cooled", "correct": True},
            {"text": "It was made by a chemical reaction as the solution "
                     "cooled down", "correct": False,
             "why": "Nothing reacts here. The sugar was dissolved all "
                    "along and simply comes out of solution as it cools."},
            {"text": "It travelled up the string from the bottom of the "
                     "jar", "correct": False,
             "why": "The string is just something for it to grow on. The "
                    "sugar comes out of the solution around it, not up "
                    "it."},
            {"text": "It condensed out of the air above the jar",
             "correct": False,
             "why": "Sugar does not travel through the air. It stays "
                    "dissolved in the liquid until the cooling solution "
                    "can no longer hold it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e14",
        "band": "easier",
        "text": "Instant coffee granules disappear completely into hot water. Coffee grounds, stirred into hot water the same way, do not. What is the difference?",
        "options": [
            {
             "text": "Instant coffee is a liquid already, so it mixes in easily",
             "correct": False,
             "why": "Instant coffee granules are a dry solid, exactly like coffee grounds are, before either goes in the water.",
            },
            {
             "text": "Instant coffee dissolves completely; the solid in coffee grounds does not",
             "correct": True,
            },
            {
             "text": "Coffee grounds have not been stirred for long enough",
             "correct": False,
             "why": "No amount of stirring dissolves the solid in coffee grounds. Being insoluble is not a matter of time.",
            },
            {
             "text": "Instant coffee is hotter than coffee grounds when it is added",
             "correct": False,
             "why": "Both are added to the same hot water. Temperature is not what makes the difference here.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e15",
        "band": "easier",
        "text": "An effervescent aspirin tablet fizzes and dissolves in seconds. A coated aspirin tablet dissolves slowly over an hour inside the body. Is one of them not really dissolving?",
        "options": [
            {
             "text": "Yes — the fizzing tablet is reacting, not dissolving",
             "correct": False,
             "why": "The fizzing does come from a reaction, but the aspirin itself still dissolves into the liquid either way.",
            },
            {
             "text": "Yes — the coated tablet cannot begin to dissolve while the coating is on",
             "correct": False,
             "why": "The coating dissolves too, slowly, which is exactly what lets the tablet release its contents over time.",
            },
            {
             "text": "No — both are dissolving, just at very different rates by design",
             "correct": True,
            },
            {
             "text": "No — but only the fizzing one is a true solution afterwards",
             "correct": False,
             "why": "Both end up as the aspirin dissolved in a liquid, however differently they got there.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e16",
        "band": "easier",
        "text": "A gardener tips fertiliser granules into a watering can of water, and separately scatters slow-release granules straight onto the soil. Which will dissolve fully sooner?",
        "options": [
            {
             "text": "The slow-release granules",
             "correct": False,
             "why": "Made to work over time means made to dissolve SLOWLY, over weeks — that is the opposite of sooner.",
            },
            {
             "text": "Both at the same rate",
             "correct": False,
             "why": "One is designed to dissolve fast in a can of water; the other is designed to dissolve slowly in soil.",
            },
            {
             "text": "Neither — fertiliser granules never fully dissolve",
             "correct": False,
             "why": "Fertiliser granules are soluble and do dissolve fully, just at different speeds depending on how they are made.",
            },
            {
             "text": "The ones in the watering can",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e17",
        "band": "easier",
        "text": "A sugar cube and a teaspoon of granulated sugar, the same mass, are dropped into two identical cups of tea at the same temperature, with no stirring. Which dissolves first?",
        "options": [
            {
             "text": "The granulated sugar",
             "correct": True,
            },
            {
             "text": "The sugar cube",
             "correct": False,
             "why": "A cube packs the same sugar into far less exposed surface than loose grains do. It is slower, not faster.",
            },
            {
             "text": "Both at the same time",
             "correct": False,
             "why": "Same mass and same sugar, but very different surface area — and that changes how fast the water can get at it.",
            },
            {
             "text": "Neither — sugar needs stirring",
             "correct": False,
             "why": "Sugar dissolves without stirring too. Stirring only changes how fast it happens.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e18",
        "band": "easier",
        "text": "Oil and vinegar, shaken together for salad dressing, "
                "separate back into two layers within seconds of being "
                "left still. Has the oil dissolved in the vinegar?",
        "options": [
            {"text": "Yes — shaking is a form of stirring, and stirring "
                     "makes things dissolve", "correct": False,
             "why": "Stirring only speeds up a dissolving that is "
                    "already going to happen. Oil and vinegar never "
                    "properly mix, however hard they are shaken."},
            {"text": "No — a dissolved substance stays mixed and does "
                     "not settle back out into layers", "correct": True},
            {"text": "Yes, but only while the bottle is still being "
                     "shaken", "correct": False,
             "why": "A true solution stays mixed once you stop stirring "
                    "it. Oil and vinegar separate again almost at once."},
            {"text": "It cannot be answered without tasting the "
                     "dressing", "correct": False,
             "why": "Watching the two layers reappear is already the "
                    "answer. Tasting tells you nothing extra here."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e19",
        "band": "easier",
        "text": "A student warms a glass of water and stirs it at the same time, and finds that more sugar dissolves in it than in a cold, unstirred glass. What caused that — the warming, the stirring, or can you not tell from this test alone?",
        "options": [
            {
             "text": "The stirring, since stirring is what gets sugar into water",
             "correct": False,
             "why": "Stirring alone never raises how much can dissolve. It only gets you there faster.",
            },
            {
             "text": "The warming, because temperature is always the answer whenever more dissolves",
             "correct": False,
             "why": "It might well be the warming, but this test cannot prove it — the stirring changed too, at the same time.",
            },
            {
             "text": "You cannot tell — both were changed at once, so either could be responsible",
             "correct": True,
            },
            {
             "text": "Both equally, since both changes always contribute the same amount",
             "correct": False,
             "why": "There is no reason to assume an equal split. The test simply cannot separate the two effects.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e20",
        "band": "easier",
        "text": "Sea water holds about 35 g of dissolved salt per litre. "
                "Water can hold over 350 g of salt per litre before it "
                "is saturated. Is sea water saturated with salt?",
        "options": [
            {"text": "Yes — the sea is full of dissolved salt, so it "
                     "must be at its limit", "correct": False,
             "why": "Containing a lot is not the same as containing the "
                    "most possible. 35 g is far short of the true "
                    "limit."},
            {"text": "Yes, because you cannot add any more salt to sea "
                     "water and have it dissolve", "correct": False,
             "why": "You could add a great deal more salt to sea water "
                    "and it would still dissolve, well before it reached "
                    "the true limit."},
            {"text": "It cannot be answered without knowing the sea's "
                     "exact temperature", "correct": False,
             "why": "Even allowing for temperature, 35 g is nowhere near "
                    "350 g. The comparison already answers it."},
            {"text": "No — it holds only a small fraction of what the "
                     "water could actually dissolve", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e21",
        "band": "easier",
        "text": "A tiny pinch of salt vanishes into a cup of water in a "
                "couple of seconds. A whole teaspoon of salt in the same "
                "cup takes much longer to fully disappear, well before "
                "any limit is reached. Why?",
        "options": [
            {"text": "There is simply more of it for the water to work "
                     "through", "correct": True},
            {"text": "The teaspoon of salt is a different, less soluble "
                     "substance", "correct": False,
             "why": "It is exactly the same salt, just more of it. "
                    "Nothing about the substance itself has changed."},
            {"text": "The water became saturated after the pinch went "
                     "in", "correct": False,
             "why": "A cup of water can hold far more than a teaspoon of "
                    "salt. The limit has not been reached here at all."},
            {"text": "Salt dissolves more slowly the second time it is "
                     "added to the same water", "correct": False,
             "why": "It is not about being added a second time. A bigger "
                    "single amount simply takes the water longer to get "
                    "through."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e22",
        "band": "easier",
        "text": "In one experiment, sugar takes 120 seconds to disappear and salt takes 90 seconds, under exactly the same conditions. What does that show?",
        "options": [
            {
             "text": "Sugar must be less soluble than salt",
             "correct": False,
             "why": "Taking longer to dissolve is not the same as being less soluble. Far more sugar than salt can dissolve in the same water.",
            },
            {
             "text": "Different solutes can dissolve at different speeds even under identical conditions",
             "correct": True,
            },
            {
             "text": "The test must have been run at two different temperatures",
             "correct": False,
             "why": "The conditions are stated to be identical. The difference comes from the two substances themselves.",
            },
            {
             "text": "One of the two readings must be a mistake",
             "correct": False,
             "why": "Different solutes genuinely can take different amounts of time under the same conditions. Neither reading needs to be wrong.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e23",
        "band": "easier",
        "text": "Chalk powder is shaken hard in water for twenty minutes "
                "straight. Does it ever dissolve if you shake it for "
                "long enough?",
        "options": [
            {"text": "Yes — enough energy from shaking will dissolve any "
                     "solid eventually", "correct": False,
             "why": "Being insoluble is not about a lack of energy. "
                    "Chalk stays undissolved no matter how much shaking "
                    "it gets."},
            {"text": "Yes, once the water has been warmed up by the "
                     "shaking", "correct": False,
             "why": "Shaking does not meaningfully warm the water, and "
                    "even warm water does not dissolve chalk."},
            {"text": "No — chalk is insoluble in water, however long or "
                     "hard it is shaken", "correct": True},
            {"text": "It depends on how finely the chalk was ground "
                     "before shaking", "correct": False,
             "why": "Grinding it finer only makes it look cloudier for "
                    "longer. It never actually dissolves."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e24",
        "band": "easier",
        "text": "The same amount of salt is stirred into hot water and into cold water, well below the point where either solution is saturated. Which disappears sooner?",
        "options": [
            {
             "text": "The salt in the cold water",
             "correct": False,
             "why": "For salt, hot and cold barely differ in how much can dissolve. Speed, not capacity, is what is being asked here — and hot water wins on speed.",
            },
            {
             "text": "Both at exactly the same time",
             "correct": False,
             "why": "Being far from saturated is about how much CAN dissolve. Temperature still changes how FAST it happens.",
            },
            {
             "text": "Neither — salt only dissolves once a solution reaches saturation",
             "correct": False,
             "why": "Salt starts dissolving the instant it touches water. Saturation is the limit, not the starting point.",
            },
            {
             "text": "The salt in the hot water",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e25",
        "band": "easier",
        "text": "A recipe says to dissolve milk powder in warm water rather than cold. What is most likely to go wrong if cold water is used instead?",
        "options": [
            {
             "text": "The milk powder dissolves too slowly to be ready in time",
             "correct": True,
            },
            {
             "text": "The milk powder turns into a completely different substance in cold water",
             "correct": False,
             "why": "It is still milk powder either way. Cold water simply slows down how quickly it dissolves.",
            },
            {
             "text": "Cold water cannot dissolve milk powder at any temperature below warm",
             "correct": False,
             "why": "Milk powder does dissolve in cold water eventually — just far more slowly than in warm water.",
            },
            {
             "text": "The milk powder will dissolve, but there will be less of it in the mixture",
             "correct": False,
             "why": "None of it is lost by using cold water. All of it still ends up dissolved, given enough time.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e26",
        "band": "easier",
        "text": "Baking soda stirred into a glass of water disappears "
                "quietly. Baking soda stirred into vinegar fizzes and "
                "bubbles vigorously. Are both of these dissolving?",
        "options": [
            {"text": "Yes — both are examples of dissolving, one just "
                     "happens to be noisier", "correct": False,
             "why": "The fizzing in vinegar is a chemical reaction "
                    "making a new gas. Dissolving makes nothing new."},
            {"text": "No — the water is dissolving; the vinegar is "
                     "reacting", "correct": True},
            {"text": "No — neither is dissolving, both are reactions",
             "correct": False,
             "why": "Baking soda in water is ordinary dissolving. "
                    "Nothing new is made, and it can be got back by "
                    "removing the water."},
            {"text": "It cannot be told apart without a laboratory test",
             "correct": False,
             "why": "The fizzing itself is the evidence. A reaction "
                    "makes a new gas; plain dissolving in water makes "
                    "nothing at all."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e27",
        "band": "easier",
        "text": "A floating chlorine dispenser in a swimming pool releases chlorine tablets that dissolve over several weeks rather than all at once. What is that an example of?",
        "options": [
            {
             "text": "A substance that only dissolves once the dispenser is opened",
             "correct": False,
             "why": "The tablets genuinely are dissolving the whole time, just very slowly, through a small exposed surface.",
            },
            {
             "text": "A tablet slowly worn away by the movement of the pool water",
             "correct": False,
             "why": "The dispenser sits still in the water. The tablet is going into the water as a solution, not being rubbed away.",
            },
            {
             "text": "Dissolving deliberately slowed down by design",
             "correct": True,
            },
            {
             "text": "A tablet that only dissolves above a certain water temperature",
             "correct": False,
             "why": "It dissolves at ordinary pool temperature the whole time. The slow release comes from its shape and size, not from temperature.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e28",
        "band": "easier",
        "text": "Dishwasher salt is sold as coarse granules rather than fine table salt. Why choose the coarser form?",
        "options": [
            {
             "text": "Because coarse granules hold more salt in each spoonful than fine ones do",
             "correct": False,
             "why": "A spoonful of coarse granules actually holds slightly less salt, because of the air gaps between the grains. Grain size is about how fast it dissolves.",
            },
            {
             "text": "Because fine table salt cannot dissolve in the water a dishwasher uses",
             "correct": False,
             "why": "Fine salt would dissolve perfectly well in a dishwasher — the problem is it would dissolve too fast, all at once.",
            },
            {
             "text": "Because coarse granules do not actually dissolve, they just get washed away",
             "correct": False,
             "why": "The granules do dissolve, gradually, which is exactly the point of choosing a coarser grain.",
            },
            {
             "text": "So that it dissolves more slowly, over the whole wash rather than all at once",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e29",
        "band": "easier",
        "text": "A bar of soap gets smaller and smaller with every wash "
                "over several weeks. How is it dissolving?",
        "options": [
            {"text": "From the outside surface inwards, a little at a "
                     "time", "correct": True},
            {"text": "All at once, evenly through the whole bar, every "
                     "time it gets wet", "correct": False,
             "why": "If the whole bar dissolved at once it would vanish "
                    "in a single wash. Only the wet surface is being "
                    "dissolved away each time."},
            {"text": "From the middle outwards, leaving a hollow shell "
                     "at the end", "correct": False,
             "why": "Water reaches the outside of the bar first. What "
                    "shrinks is the surface, not a hidden core."},
            {"text": "It does not dissolve — it simply wears away like a "
                     "pencil", "correct": False,
             "why": "Soap genuinely dissolves in water; that is why it "
                    "lathers. Wearing away is a different, physical "
                    "process."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e30",
        "band": "easier",
        "text": "A hiker drops an iodine tablet into a bottle of stream "
                "water to make it safer to drink. The tablet disappears "
                "within a minute. What has happened to it?",
        "options": [
            {"text": "It has been filtered out by the water",
             "correct": False,
             "why": "Filtering removes an insoluble solid from a "
                    "liquid. This tablet has gone into the water, not "
                    "been caught by anything."},
            {"text": "It has dissolved into the water", "correct": True},
            {"text": "It has evaporated into the air above the bottle",
             "correct": False,
             "why": "Evaporation is a liquid turning to gas. A solid "
                    "tablet disappearing into a liquid is dissolving."},
            {"text": "It has been destroyed by the stream water",
             "correct": False,
             "why": "Nothing is destroyed. The tablet is still there, "
                    "spread through the water as particles too small to "
                    "see."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e31",
        "band": "easier",
        "text": "5 g of sugar is dissolved in 50 g of water, and "
                "separately 5 g of sugar is dissolved in 200 g of "
                "water. Both dissolve completely. Do the two drinks "
                "taste the same?",
        "options": [
            {"text": "Yes — the same mass of sugar was used both times",
             "correct": False,
             "why": "Using the same mass of sugar does not mean the same "
                    "strength of taste. Spreading it through more water "
                    "makes it weaker."},
            {"text": "Yes, because both solutions are equally saturated "
                     "with sugar", "correct": False,
             "why": "Neither solution is anywhere near saturated at 5 g. "
                    "That is not what decides how strong they taste."},
            {"text": "No — the smaller amount of water makes a "
                     "stronger-tasting drink", "correct": True},
            {"text": "It cannot be known without tasting them both "
                     "first", "correct": False,
             "why": "Less water for the same sugar always tastes "
                    "stronger. That much can be worked out without "
                    "tasting anything."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-e32",
        "band": "easier",
        "text": "A student says grinding a solute and warming the solvent are really the same trick, because both make dissolving happen sooner. Is that a fair way to put it?",
        "options": [
            {
             "text": "No — grinding and warming affect completely unrelated things",
             "correct": False,
             "why": "They do share one effect: both can make a solute disappear sooner. It is not true that they are unrelated.",
            },
            {
             "text": "Yes, and both of them also raise how much can dissolve",
             "correct": False,
             "why": "Grinding never changes how much can dissolve, only how fast. That is exactly where the two stop being the same trick.",
            },
            {
             "text": "No — only warming changes the speed; grinding does nothing to it",
             "correct": False,
             "why": "Grinding does speed dissolving up, by giving the solvent more surface to work on at once.",
            },
            {
             "text": "Yes for speed — though warming can also raise how much dissolves, which grinding never does",
             "correct": True,
            },
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-02-s09",
        "band": "standard",
        "text": "A cafe wants hot chocolate powder mixed into milk as fast as possible. Explain why warming the milk helps with this.",
        "options": [
            {
             "text": "Warming the milk speeds up how fast the powder disappears, in the same way warm water speeds up sugar or salt",
             "correct": True,
            },
            {
             "text": "Warming the milk lets far more powder be used than cold milk ever could, which is the real reason it helps",
             "correct": False,
             "why": "The cafe wants speed, not a bigger limit. Salt barely raises its limit with heat at all, and speed is a separate effect from how much can dissolve.",
            },
            {
             "text": "Warming the milk changes the powder into a different, more soluble substance",
             "correct": False,
             "why": "The powder stays exactly the same substance. Only how quickly the milk can dissolve it changes.",
            },
            {
             "text": "Warming the milk has no real effect; only stirring speeds anything up",
             "correct": False,
             "why": "Temperature is one of the two things that change the rate, stirring being the other. Both work here.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s10",
        "band": "standard",
        "text": "Two identical vitamin C tablets are dropped into two "
                "identical glasses of water at the same temperature. One "
                "tablet is whole; the other has been crushed to powder "
                "first. Explain the difference in how they behave.",
        "options": [
            {"text": "The whole tablet actually dissolves faster overall, because a solid lump holds itself together far better once it is in water", "correct": False,
             "why": "The opposite happens. A whole tablet exposes far "
                    "less surface to the water than the same tablet "
                    "crushed."},
            {"text": "The crushed tablet dissolves faster, because more "
                     "of its surface touches the water at once",
             "correct": True},
            {"text": "Both dissolve at the same rate, since crushing "
                     "does not change the total mass", "correct": False,
             "why": "Total mass is unchanged, but the SHAPE has changed "
                    "— and shape decides how much surface the water can "
                    "reach at once."},
            {"text": "The crushed tablet will not fully dissolve, "
                     "because crushing destroys some of the vitamin C",
             "correct": False,
             "why": "Nothing is destroyed by crushing. Every crushed "
                    "particle still dissolves, and the crushed tablet "
                    "ends up fully dissolved too."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s11",
        "band": "standard",
        "text": "An aquarium keeper argues that a bubbling air pump lets the tank hold more fish than a still tank of the same size and temperature, because it raises the maximum dissolved oxygen the water can hold. Is that argument right?",
        "options": [
            {
             "text": "Yes — bubbling air continuously through the water is the only way to raise its true dissolved oxygen limit",
             "correct": False,
             "why": "The limit is set by the water's temperature. Bubbling gets the water up to that existing limit rather than moving the limit itself.",
            },
            {
             "text": "Yes, because the bubbles themselves become part of the dissolved oxygen",
             "correct": False,
             "why": "A bubble is a pocket of gas, not dissolved gas. It is the oxygen leaving the bubble's surface into the water that counts, up to the same limit as before.",
            },
            {
             "text": "No — the maximum is set by temperature; the pump only gets the water there sooner and keeps it there",
             "correct": True,
            },
            {
             "text": "No — a pump has no effect on the dissolved oxygen",
             "correct": False,
             "why": "It does have an effect: without it, oxygen used up by the fish is replaced more slowly, and the tank can sit well below its true limit.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s12",
        "band": "standard",
        "text": "A washing machine manual recommends a hot wash for "
                "\"better cleaning\" with the same amount of powder as a "
                "cold wash. What is the powder most likely doing "
                "differently in the two washes?",
        "options": [
            {"text": "Dissolving into a stronger detergent solution in "
                     "the hot wash, because heat raises how much powder "
                     "can dissolve", "correct": False,
             "why": "The amount of powder used is the same in both "
                    "washes. What changes with heat here is speed, not "
                    "a bigger limit being reached."},
            {"text": "Reacting with the hot water to make a new cleaning "
                     "chemical", "correct": False,
             "why": "Nothing new is made. The powder is dissolving, the "
                    "same substance, in both washes."},
            {"text": "Being destroyed by the cold water before it can "
                     "work", "correct": False,
             "why": "Cold water does not destroy the powder. It simply "
                    "dissolves it more slowly than hot water does."},
            {"text": "Dissolving fully and quickly in the hot wash, "
                     "possibly not fully dissolving in time in the cold "
                     "one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s13",
        "band": "standard",
        "text": "A hot, saturated sugar solution is left to cool, and crystals form as it does. Explain why cooling causes crystals to appear rather than the solution simply staying as it was.",
        "options": [
            {
             "text": "Cooling lowers how much sugar the water can hold, so the extra sugar comes out of solution as crystals",
             "correct": True,
            },
            {
             "text": "Cooling makes the water evaporate, leaving the sugar behind as crystals",
             "correct": False,
             "why": "Cooling a closed jar does not evaporate the water away. The water is still there; the sugar has simply stopped being able to stay dissolved in all of it.",
            },
            {
             "text": "Cooling turns part of the dissolved sugar into an entirely new, chemically different substance that is insoluble",
             "correct": False,
             "why": "It is still ordinary sugar, unchanged. It has come out of solution, not turned into anything new.",
            },
            {
             "text": "Cooling has no effect on how much can dissolve; the crystals form simply because a very long time has now passed",
             "correct": False,
             "why": "Time passing alone would not do it. It is specifically the drop in temperature that lowers how much sugar the water can hold.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s14",
        "band": "standard",
        "text": "Instant coffee granules and coffee grounds are both dry, brown, made from roasted coffee beans, and both are stirred into the same hot water. Explain why only one of them disappears.",
        "options": [
            {
             "text": "The grounds are simply larger pieces than the granules, so they just need longer to dissolve",
             "correct": False,
             "why": "No amount of extra time dissolves the solid in coffee grounds. Grinding them further would only make finer insoluble particles, not a solution.",
            },
            {
             "text": "Instant coffee has been processed so that all of it dissolves in water; the solid in the grounds has not",
             "correct": True,
            },
            {
             "text": "The granules are hotter than the grounds when they are added, which is why they disappear",
             "correct": False,
             "why": "Both are added to water at the same temperature. Heat is not the difference between them.",
            },
            {
             "text": "Both dissolve fully; the grounds are simply too small to see once stirred in",
             "correct": False,
             "why": "The grounds can be filtered back out afterwards, which shows the solid never dissolved.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s15",
        "band": "standard",
        "text": "An effervescent tablet dissolves in seconds; a coated tablet dissolves over an hour. A student says \"the coated one must be far less soluble.\" Is that a fair conclusion from the two times alone?",
        "options": [
            {
             "text": "Yes — a substance that takes longer to dissolve is always less soluble",
             "correct": False,
             "why": "Sugar takes longer than salt to disappear under the same conditions, yet far more sugar than salt can dissolve. Time alone does not measure solubility.",
            },
            {
             "text": "Yes, because solubility itself is properly defined as how quickly a substance disappears completely into a liquid solvent",
             "correct": False,
             "why": "Solubility is about how MUCH can dissolve, not how fast. Rate and amount are two different things.",
            },
            {
             "text": "No — the difference could just as easily be designed rate rather than a difference in solubility",
             "correct": True,
            },
            {
             "text": "It cannot be judged without first knowing the mass of each of the tablets",
             "correct": False,
             "why": "Mass would help compare exact amounts, but the central point stands without it: a slow coating can explain the whole time difference on its own.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s16",
        "band": "standard",
        "text": "Fertiliser granules dissolve within minutes in a "
                "watering can, but similar granules scattered on soil "
                "are designed to dissolve over several weeks. What is "
                "most likely different between the two kinds of "
                "granule?",
        "options": [
            {"text": "The slow-release kind is a completely different, "
                     "far less soluble chemical", "correct": False,
             "why": "Both are still soluble fertiliser. The difference "
                    "engineered in is the RATE, achieved by exposing far "
                    "less surface to water at a time."},
            {"text": "The watering-can granules are warmed by the water "
                     "before they are used, unlike the soil granules",
             "correct": False,
             "why": "Tap water for a watering can is not meaningfully "
                    "warmer than damp soil. Temperature is not the "
                    "engineered difference here."},
            {"text": "The soil granules have simply not yet had enough rainfall to properly start dissolving into the ground around them", "correct": False,
             "why": "They start dissolving as soon as they meet any "
                    "moisture. They are just built to release very "
                    "slowly, week after week."},
            {"text": "The slow-release kind is made or coated so that "
                     "far less of its surface meets water at once",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s17",
        "band": "standard",
        "text": "A sugar cube and the same mass of granulated sugar are "
                "dropped into two identical, unstirred cups of tea. "
                "Explain why the granulated sugar disappears first, "
                "without mentioning stirring at all.",
        "options": [
            {"text": "The loose grains expose far more total surface to "
                     "the tea than the compact cube does",
             "correct": True},
            {"text": "The granulated sugar is a more soluble form of "
                     "sugar than a pressed cube", "correct": False,
             "why": "It is the same sugar either way, pressed or loose. "
                    "Nothing about the sugar itself has changed, only "
                    "its shape."},
            {"text": "The cube floats at first, delaying when it starts "
                     "to dissolve", "correct": False,
             "why": "A sugar cube does not float on tea; it sits in the "
                    "liquid and starts dissolving from the moment it "
                    "goes in, just more slowly."},
            {"text": "The granulated sugar reacts with the tea, while "
                     "the cube only dissolves", "correct": False,
             "why": "Both are doing the same thing, dissolving. Nothing "
                    "new is made by either the loose grains or the cube."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s18",
        "band": "standard",
        "text": "Oil and vinegar separate back into layers once shaken salad dressing is left standing. Explain why this shows that oil has not dissolved in vinegar, using what a true solution does.",
        "options": [
            {
             "text": "Oil is always denser than vinegar, so it must settle to the bottom given time",
             "correct": False,
             "why": "Oil is actually less dense than vinegar and rises to the top. Either way, density is not what proves it has not dissolved.",
            },
            {
             "text": "A true solution stays evenly mixed once left still; separating out shows the oil was never spread through the vinegar as particles",
             "correct": True,
            },
            {
             "text": "The two liquids actually react chemically with each other while being shaken hard, and the two layers left behind are the two separate products of that reaction",
             "correct": False,
             "why": "Nothing reacts. The oil and vinegar are the same two substances before and after shaking; they simply do not mix into one another.",
            },
            {
             "text": "Shaking is not the same as stirring, so nothing should have been expected to dissolve",
             "correct": False,
             "why": "Shaking and stirring both mix things the same way. The reason oil and vinegar separate is that oil is not soluble in vinegar, not the mixing method used.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s19",
        "band": "standard",
        "text": "A student warms a glass of water and stirs a spoonful of sugar into it at the same time, and more sugar dissolves than in a cold, unstirred glass. A second student says this proves stirring raises how much can dissolve. What is the flaw in that conclusion?",
        "options": [
            {
             "text": "There is no flaw — the result proves stirring raises the limit",
             "correct": False,
             "why": "The test changed two variables together. It cannot show which one, or whether both, caused the extra sugar to dissolve.",
            },
            {
             "text": "The flaw is that stirring has no effect whatsoever on dissolving, so it cannot have raised anything",
             "correct": False,
             "why": "Stirring does speed dissolving up. The flaw is not that stirring does nothing, but that warming was changed at the same time, so neither change can be credited.",
            },
            {
             "text": "Two things changed at once, warming and stirring, so neither one alone has been shown to be responsible",
             "correct": True,
            },
            {
             "text": "The flaw is that the two glasses were not stirred for the same length of time",
             "correct": False,
             "why": "Timing is not the issue raised here. The problem is that warming and stirring were both changed together, with nothing to tell them apart.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s20",
        "band": "standard",
        "text": "A cook brines a chicken in water that holds 60 g of "
                "dissolved salt in every litre. At kitchen temperature a "
                "litre of water will take about 350 g of salt before no "
                "more of it will dissolve. Explain what would have to "
                "happen to that brine for it to become saturated.",
        "options": [
            {"text": "Nothing further needs to happen — a brine strong "
                     "enough to season a whole chicken must already be "
                     "holding every gram of salt it can", "correct": False,
             "why": "60 g is far short of the roughly 350 g limit. The "
                    "brine has a long way to go before it is saturated."},
            {"text": "The brine would simply need to be chilled in the "
                     "fridge overnight", "correct": False,
             "why": "Salt's limit barely moves with temperature at all. "
                    "Cooling the brine would not meaningfully close a gap "
                    "this large."},
            {"text": "Only adding more salt could do it — taking water "
                     "out of the brine cannot saturate a solution",
             "correct": False,
             "why": "Saturation depends on how much solute is dissolved "
                    "in how much solvent, so removing solvent reaches it "
                    "just as surely as adding solute."},
            {"text": "A great deal more salt would need to dissolve "
                     "into it, or a great deal of its water would need "
                     "to be removed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s21",
        "band": "standard",
        "text": "A tiny pinch of salt dissolves in a couple of seconds; a whole teaspoon in the same cup of water takes much longer, well before either gets anywhere near saturating the water. Explain the difference without mentioning saturation at all.",
        "options": [
            {
             "text": "There is simply far more salt for the same amount of water to work through",
             "correct": True,
            },
            {
             "text": "A teaspoon of salt is packed more tightly than a pinch, which slows the water down",
             "correct": False,
             "why": "How the salt happens to be arranged before it goes in barely matters. It is the total amount that has to be dissolved that takes the extra time.",
            },
            {
             "text": "The cup of water cools slightly between adding the pinch and adding the teaspoon",
             "correct": False,
             "why": "Nothing here suggests a meaningful temperature change between the two. The amount of salt is the stated difference.",
            },
            {
             "text": "A teaspoon of salt is less soluble than a pinch of the very same salt",
             "correct": False,
             "why": "It is exactly the same salt either way. Solubility does not change depending on how much you start with.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s22",
        "band": "standard",
        "text": "In one experiment, sugar takes 120 seconds and salt takes 90 seconds to disappear under identical conditions. Explain why this does not mean sugar is less soluble than salt.",
        "options": [
            {
             "text": "It does mean sugar is less soluble, because taking longer is the definition of being less soluble",
             "correct": False,
             "why": "Solubility is a measure of AMOUNT, not of time taken. Rate and solubility are two different things.",
            },
            {
             "text": "Solubility is about how much can dissolve, and far more sugar than salt can dissolve in the same water",
             "correct": True,
            },
            {
             "text": "The two readings cannot both be trusted, since one substance must be measured wrongly",
             "correct": False,
             "why": "Both readings can be correct. Different solutes genuinely take different times under the same conditions.",
            },
            {
             "text": "It shows sugar particles are physically larger than salt particles",
             "correct": False,
             "why": "Particle size is not what the timings measure here, and nothing about the two times tells you the relative sizes of the particles.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s23",
        "band": "standard",
        "text": "Chalk powder is shaken vigorously in water for twenty minutes and stays cloudy the whole time. A student argues that shaking it for two hours instead would finally dissolve it. Evaluate that argument.",
        "options": [
            {
             "text": "It is right — shaking supplies energy, and enough energy dissolves anything eventually",
             "correct": False,
             "why": "Insolubility is not a lack of energy. Shaking never gets chalk any closer to dissolving, however long it goes on for.",
            },
            {
             "text": "It is right, but only if the water is also warmed while it is shaken",
             "correct": False,
             "why": "Warming does not make chalk soluble either. Chalk stays undissolved whatever combination of shaking and heat is used.",
            },
            {
             "text": "It is wrong — chalk is insoluble in water, and no amount of shaking changes that",
             "correct": True,
            },
            {
             "text": "It cannot really be evaluated without first knowing exactly how much chalk powder was originally used",
             "correct": False,
             "why": "The amount used does not change the verdict. Chalk is insoluble regardless of how much or how little is shaken with the water.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s24",
        "band": "standard",
        "text": "The same mass of salt is stirred into hot water and into cold water, both well below saturation. The salt in the hot water disappears sooner. Explain what that does, and does not, tell you about how much salt each glass could hold.",
        "options": [
            {
             "text": "It does not get dissolved any sooner — the two should take exactly the same time",
             "correct": False,
             "why": "Warmer water speeds up dissolving for salt too, even though its LIMIT barely shifts with temperature. Rate and limit are separate effects.",
            },
            {
             "text": "Hot water contains less salt to begin with, so there is less for it to dissolve",
             "correct": False,
             "why": "Neither glass has any salt in it until the teaspoon is stirred in. The starting amount is the same in both.",
            },
            {
             "text": "The barely-changing limit means temperature has no effect on how salt dissolves",
             "correct": False,
             "why": "Temperature still changes the rate for salt, even though it barely changes the limit. Those are two different effects.",
            },
            {
             "text": "Temperature speeds up how fast a solute disappears even when it barely changes how much can dissolve",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s25",
        "band": "standard",
        "text": "A recipe says to dissolve milk powder in warm water rather than cold. Explain what would most likely go wrong if a cook used fridge-cold water instead, and why simply waiting longer might not fix it in time for the recipe.",
        "options": [
            {
             "text": "The milk powder would still dissolve, but far more slowly, and the recipe's timing might not allow for that",
             "correct": True,
            },
            {
             "text": "The milk powder would not dissolve in cold water at any speed, however long it was left",
             "correct": False,
             "why": "Milk powder does dissolve in cold water eventually — just much more slowly than in warm water.",
            },
            {
             "text": "The milk powder would dissolve just as quickly, but would make a thinner drink afterwards",
             "correct": False,
             "why": "The problem the recipe is guarding against is speed of dissolving at this stage, not how thick the finished drink is.",
            },
            {
             "text": "Using cold water would mean less milk powder ends up dissolved overall",
             "correct": False,
             "why": "Given enough time, the same amount of milk powder dissolves in cold water as in warm. The difference is purely how long it takes.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s26",
        "band": "standard",
        "text": "Baking soda disappears quietly into water, but fizzes vigorously and bubbles when stirred into vinegar. Explain how you would prove which of the two is dissolving and which is reacting, without tasting either one.",
        "options": [
            {
             "text": "Look at which one is noisier — the noisier change is always the dissolving one",
             "correct": False,
             "why": "It is the other way round here. The quiet change, in water, is the dissolving; the noisy, fizzing one is the reaction.",
            },
            {
             "text": "Leave each liquid in a warm place until it has evaporated: the water sample gives back the baking soda unchanged, while the vinegar sample does not, since a new substance was made",
             "correct": True,
            },
            {
             "text": "Weigh the baking soda carefully before it is added to each liquid in both cases; comparing the two starting masses will already tell you which sample is reacting",
             "correct": False,
             "why": "The starting mass is the same both times. It is what happens to the sample afterwards — recovering the original substance or not — that tells them apart.",
            },
            {
             "text": "There is no way to tell the two apart without using specialist laboratory equipment",
             "correct": False,
             "why": "Evaporating each mixture and seeing what is left behind is a test that needs nothing more advanced than a dish and some heat.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s27",
        "band": "standard",
        "text": "A swimming pool's floating chlorine dispenser is "
                "designed to make its tablets last for weeks rather than "
                "dissolving in one afternoon. Explain, in terms of "
                "surface area, how the dispenser achieves that.",
        "options": [
            {"text": "It keeps the tablets in air rather than water most "
                     "of the time", "correct": False,
             "why": "The dispenser floats in the pool, with the tablets "
                    "in continuous contact with the water. Surface "
                    "exposure, not being kept dry, is the mechanism."},
            {"text": "It chills the tablets, which slows dissolving down "
                     "the way cold water does", "correct": False,
             "why": "The dispenser does not cool anything; pool water "
                    "stays at roughly the same temperature throughout. "
                    "The slow release comes from limited surface, not "
                    "temperature."},
            {"text": "It exposes only a small part of each tablet to "
                     "the water at any one time", "correct": True},
            {"text": "It dissolves the tablets completely on day one and "
                     "simply releases the chlorine gradually afterwards",
             "correct": False,
             "why": "The tablets themselves are still dissolving, "
                    "gradually, over the weeks — they are not fully "
                    "dissolved on day one with the result stored "
                    "elsewhere."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s28",
        "band": "standard",
        "text": "Dishwasher salt is sold as coarse granules, while table salt is fine. Explain why a manufacturer would choose coarse granules for a dishwasher rather than simply using cheaper, more readily available fine table salt.",
        "options": [
            {
             "text": "Coarse granules pack more salt into the same size of compartment than fine salt would",
             "correct": False,
             "why": "Coarse grains pack less tightly, not more, because of the air gaps between them. The reason for the coarse grain is how slowly it dissolves.",
            },
            {
             "text": "Fine table salt would react with the dishwasher's metal parts, unlike coarse granules",
             "correct": False,
             "why": "Grain size does not change what a substance reacts with. The choice is about controlling how quickly it dissolves, not about avoiding a reaction.",
            },
            {
             "text": "Coarse granules are considerably cheaper to manufacture in bulk than finely ground salt, which is the real underlying reason for the choice",
             "correct": False,
             "why": "Cost is not the stated reason dishwasher salt is coarse; the coarser grain is chosen specifically to slow dissolving down.",
            },
            {
             "text": "Coarser granules dissolve more slowly, spreading the salt's effect over the whole wash instead of using it all up at once",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s29",
        "band": "standard",
        "text": "A bar of soap shrinks a little with every wash over "
                "several weeks, always keeping roughly the same shape "
                "just smaller. Explain what that tells you about how it "
                "dissolves.",
        "options": [
            {"text": "It dissolves from its outer surface inwards, a "
                     "thin layer at a time, rather than all through the "
                     "bar at once", "correct": True},
            {"text": "It tells you soap does not actually dissolve, it "
                     "just wears away physically like chalk on a "
                     "blackboard", "correct": False,
             "why": "Soap genuinely dissolves — that dissolved soap is "
                    "what makes the lather. Keeping the same shape while "
                    "shrinking is exactly what dissolving from the "
                    "surface looks like."},
            {"text": "It tells you the whole bar dissolves evenly "
                     "through its entire volume with every wash",
             "correct": False,
             "why": "If the whole bar dissolved evenly through its "
                    "volume, the bar's shape would blur and soften "
                    "rather than staying roughly the same shape while "
                    "getting smaller."},
            {"text": "It tells you the bar is made of two different "
                     "substances, one soluble and one not", "correct": False,
             "why": "Nothing about a shrinking, same-shaped bar suggests "
                    "two substances. One soluble solid dissolving from "
                    "the outside in explains it perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s30",
        "band": "standard",
        "text": "A hiker's water-purification tablet disappears from a bottle of stream water within a minute. Explain how you would show, without drinking any of it, that the tablet is still in the water rather than gone.",
        "options": [
            {
             "text": "There is no way to show it without drinking the water and noticing the taste",
             "correct": False,
             "why": "Tasting is neither safe nor necessary. Evaporating a sample is a way of checking that does not involve drinking anything at all.",
            },
            {
             "text": "Evaporate a sample of the water; a solid residue from the tablet would be left behind",
             "correct": True,
            },
            {
             "text": "Filter the water through a paper; the tablet would be caught in the filter",
             "correct": False,
             "why": "Anything dissolved passes straight through filter paper along with the water.",
            },
            {
             "text": "Weigh the bottle before and after; if the reading has not changed, the tablet must have vanished",
             "correct": False,
             "why": "The reading would not change either way, because nothing left the bottle. An unchanged reading shows the tablet is still there, not that it has gone.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s31",
        "band": "standard",
        "text": "5 g of sugar is dissolved in 50 g of water, and separately in 200 g of water, both well below saturation. Explain why the two drinks taste different even though the same mass of sugar was used each time.",
        "options": [
            {
             "text": "The sugar in the 200 g of water has actually partly failed to dissolve properly, leaving noticeably less of it actually around to be tasted in the drink",
             "correct": False,
             "why": "5 g of sugar is nowhere near enough to fail to dissolve in 200 g of water. All of it dissolves in both cases.",
            },
            {
             "text": "Sugar in more water becomes a different, less sweet-tasting substance",
             "correct": False,
             "why": "It is the same sugar in both drinks. Nothing about the substance itself has changed — only how spread out it is.",
            },
            {
             "text": "The same amount of sugar is spread through very different amounts of water, making one drink more concentrated than the other",
             "correct": True,
            },
            {
             "text": "They should not taste different, since the same mass of sugar was used in each",
             "correct": False,
             "why": "Taste depends on concentration, not just on the total mass of sugar used. Less water for the same sugar tastes stronger.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-s32",
        "band": "standard",
        "text": "Explain why grinding a solute and warming the solvent "
                "are not simply \"the same trick\" for making dissolving "
                "happen sooner, even though both can speed it up.",
        "options": [
            {"text": "They are exactly the same trick, since both ultimately work by heating up the solute's individual particles directly", "correct": False,
             "why": "Grinding does not heat anything. It works purely "
                    "by exposing more surface to the solvent, which is a "
                    "different mechanism from warming."},
            {"text": "Grinding only works on liquids, while warming only "
                     "works on solids", "correct": False,
             "why": "Grinding is done to a solid solute, and warming is "
                    "done to the solvent — but both act on the same "
                    "dissolving process, just through different routes."},
            {"text": "They are not the same trick because grinding is "
                     "always faster than warming", "correct": False,
             "why": "Neither is always the faster of the two. The real "
                    "difference is what each one can and cannot change "
                    "— rate alone, or rate and limit together."},
            {"text": "Warming can also raise how much of some solutes "
                     "can dissolve, while grinding never changes that "
                     "limit at all", "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ────────────────────────────────────────
    {
        "id": "c3-02-h09",
        "band": "harder",
        "text": "A cafe manager notices hot chocolate powder disappears "
                "faster in hot milk than in cold, and concludes that "
                "warming milk always dissolves more of everything. Is "
                "that conclusion sound?",
        "options": [
            {"text": "It is unsound — speeding up dissolving and raising "
                     "the amount that can dissolve are two separate "
                     "things, and salt shows they do not always travel "
                     "together", "correct": True},
            {"text": "It is sound, because seeing heat speed up dissolving for one solute is proof enough that it must raise the maximum limit for absolutely every solute there is",
             "correct": False,
             "why": "Salt disproves this directly: its limit barely "
                    "moves with temperature, even though warming still "
                    "speeds up how fast it disappears."},
            {"text": "It is unsound, because heat never has any effect "
                     "on how fast anything dissolves", "correct": False,
             "why": "Heat clearly does speed dissolving up here — that "
                    "is the very observation the manager is drawing on. "
                    "The flaw is in the conclusion drawn from it."},
            {"text": "It is sound only for drinks, not for solids "
                     "dissolved in a laboratory beaker", "correct": False,
             "why": "The kind of container or drink involved makes no "
                    "difference. The flaw is treating rate and limit as "
                    "the same thing, which fails for salt regardless of "
                    "setting."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h10",
        "band": "harder",
        "text": "A whole vitamin C tablet and an identical tablet ground "
                "to powder are both dissolved completely, in separate "
                "glasses, given enough time. Compare the two end "
                "results and explain what, if anything, differs between "
                "them once both are fully dissolved.",
        "options": [
            {"text": "The ground tablet's glass ends up holding more "
                     "dissolved vitamin C than the whole tablet's does",
             "correct": False,
             "why": "Grinding changes only the time taken, not the "
                    "final amount dissolved. Given enough time, both "
                    "glasses end up holding exactly the same amount."},
            {"text": "Nothing differs once both are fully dissolved — "
                     "the same mass ends up dissolved in each glass "
                     "either way", "correct": True},
            {"text": "The whole tablet's glass ends up clearer, because grinding introduces tiny air bubbles into the solution as it dissolves, which slowly rise and clear over time", "correct": False,
             "why": "Grinding a tablet does not trap air in the "
                    "finished solution. Once fully dissolved, both "
                    "glasses look the same."},
            {"text": "The ground tablet produces a slightly different "
                     "dissolved substance, because grinding is itself a "
                     "chemical change", "correct": False,
             "why": "Grinding is a physical change to shape and size "
                    "only. The substance that ends up dissolved is "
                    "identical either way."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h11",
        "band": "harder",
        "text": "A tank with an air pump reaches its full dissolved-oxygen level in an hour. An identical tank with no pump reaches the very same level after a full day, left undisturbed. Evaluate the claim that the pump increases the total amount of oxygen the tank can hold.",
        "options": [
            {
             "text": "The claim is true, since the pumped tank clearly and measurably ends up holding more dissolved oxygen in it than the tank that has no pump running",
             "correct": False,
             "why": "Both tanks reach the SAME final level eventually — an hour apart, but the same amount. The limit itself has not moved.",
            },
            {
             "text": "The claim cannot be judged without knowing the exact size of both tanks",
             "correct": False,
             "why": "Tank size would not change this comparison: both tanks are described as reaching the identical final level, whatever size they are.",
            },
            {
             "text": "The claim is false — both tanks reach the same final level, so the true limit is unchanged; only the time taken to reach it differs",
             "correct": True,
            },
            {
             "text": "The claim is true only for the first hour, after which the limit falls back down again to somewhere close to where it originally started out",
             "correct": False,
             "why": "Nothing in this comparison suggests the level falls afterwards. Both tanks simply settle at the same steady level, reached at different speeds.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h12",
        "band": "harder",
        "text": "A washing machine manufacturer claims a hot cycle \"dissolves detergent more completely\" than a cold cycle using the identical dose. Assess whether this is a claim about rate, about limit, or genuinely both, using ordinary washing powder amounts that never come close to saturating the water.",
        "options": [
            {
             "text": "It is a claim about limit — the hot cycle can dissolve a larger dose of detergent overall",
             "correct": False,
             "why": "The dose used is well below saturation in both cycles. There is no limit being approached for the temperature to raise.",
            },
            {
             "text": "It is a claim about both rate and limit equally, since heat always changes both of them together, by exactly the same proportional amount, for every solute that is dissolved in it",
             "correct": False,
             "why": "Heat does not always change both by the same amount — salt's limit barely moves with temperature at all, even though its rate does.",
            },
            {
             "text": "It is neither — temperature has no real bearing on how detergent behaves in water",
             "correct": False,
             "why": "Temperature does change how fast the detergent disappears, which is exactly the effect the manufacturer's claim is describing, however loosely.",
            },
            {
             "text": "It is really a claim about rate — well below saturation, both cycles will fully dissolve the identical dose given enough time, but the hot cycle gets there sooner",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h13",
        "band": "harder",
        "text": "A jar of hot, saturated sugar solution is divided into two identical jars. One is cooled quickly in a fridge; the other is left to cool slowly on a shelf overnight. Both end up at the same final temperature. Predict and explain any difference between the crystals in the two jars.",
        "options": [
            {
             "text": "Both hold the same total mass of crystals, but the slowly cooled jar's crystals are larger and more regular",
             "correct": True,
            },
            {
             "text": "The quickly cooled jar ends up with more crystals in total mass, because the sudden cold traps extra sugar out of solution",
             "correct": False,
             "why": "The final temperature is the same for both jars, so the same total mass of sugar comes out of solution in each — only the crystal size differs.",
            },
            {
             "text": "The two jars end up completely identical, since the rate of cooling has no effect on a solution",
             "correct": False,
             "why": "Cooling rate does have an effect, on the crystals themselves — fast cooling starts many small crystals at once, while slow cooling grows fewer, larger ones.",
            },
            {
             "text": "The slowly cooled jar ends up with less sugar out of solution overall, since it had more time to redissolve gradually back into the surrounding liquid as it cooled",
             "correct": False,
             "why": "Once the temperature has settled, the amount out of solution is fixed by that temperature, not by how slowly it was reached.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h14",
        "band": "harder",
        "text": "A drinks company develops a new instant coffee that dissolves in cold water as easily as ordinary instant coffee dissolves in hot water. Explain what property of the granules must have changed to achieve this, and what has NOT changed.",
        "options": [
            {
             "text": "The granules must now be an entirely different, completely non-coffee substance that has simply been flavoured to taste convincingly similar to real brewed coffee",
             "correct": False,
             "why": "Nothing requires the coffee itself to change substance. Only how easily it dissolves at a given temperature needs to be different.",
            },
            {
             "text": "How fast it dissolves in cold water has changed; it was soluble before and it is still soluble now",
             "correct": True,
            },
            {
             "text": "The granules must now dissolve into a gas rather than staying in the liquid",
             "correct": False,
             "why": "Dissolving into a solution does not mean becoming a gas. The coffee stays dissolved in the liquid drink, exactly as before.",
            },
            {
             "text": "Nothing has really changed — any instant coffee dissolves equally well in cold water already, given long enough and a reasonably vigorous stir",
             "correct": False,
             "why": "The comparison in the question is with ordinary instant coffee, which is markedly slower to dissolve in cold water. Something genuine has changed.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h15",
        "band": "harder",
        "text": "A pharmaceutical company designs a tablet that dissolves in exactly six hours, neither faster nor slower, whatever the patient drinks it with. Explain why controlling for temperature is especially important for such a design, given how much temperature can change dissolving speed.",
        "options": [
            {
             "text": "Temperature never affects tablets, only powders and granules, so this is not actually a concern",
             "correct": False,
             "why": "Temperature affects dissolving generally, tablets included — which is exactly why a coated tablet's release timing needs to be engineered carefully.",
            },
            {
             "text": "It matters only because hot drinks would destroy the medicine chemically before it could dissolve",
             "correct": False,
             "why": "The concern here is about the SPEED of dissolving changing with temperature, not about the medicine being destroyed by heat.",
            },
            {
             "text": "If temperature strongly affected the tablet's dissolving rate, drinking it with a hot drink or a cold one could make the dose act far sooner or later than intended",
             "correct": True,
            },
            {
             "text": "It does not matter, because a six-hour release tablet is designed to dissolve at exactly the same rate in water of any temperature it is likely to meet",
             "correct": False,
             "why": "That consistency is the ENGINEERING GOAL, not something true automatically. Achieving it is precisely why controlling for temperature's effect matters so much.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h16",
        "band": "harder",
        "text": "A gardener wants fertiliser to release nutrients evenly "
                "over an entire growing season rather than all in the "
                "first week. Explain one way to achieve this with "
                "granules made of exactly the same soluble fertiliser.",
        "options": [
            {"text": "Use granules that are chemically different from "
                     "ordinary fertiliser, since surface area cannot "
                     "control release speed on its own", "correct": False,
             "why": "Surface area alone genuinely can control release "
                    "speed without changing the chemical at all — one "
                    "solid block dissolves far more slowly than the same "
                    "mass ground to powder."},
            {"text": "Grind the fertiliser to a much finer powder before "
                     "scattering it on the soil", "correct": False,
             "why": "Grinding finer would expose MORE surface to "
                    "moisture, making it dissolve faster, not slower — "
                    "the opposite of what is wanted here."},
            {"text": "Water the soil more often, so the fertiliser is released a little at a time with each watering session throughout the entire growing season",
             "correct": False,
             "why": "More frequent watering would tend to dissolve "
                    "exposed fertiliser faster overall, not spread its "
                    "release out more evenly across the season."},
            {"text": "Make or coat the granules so that only a small "
                     "part of each one is exposed to soil moisture at "
                     "any given time", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h17",
        "band": "harder",
        "text": "A sugar cube, granulated sugar and caster sugar (finer still) — all the same mass of the same sugar — are dropped into three identical cups of tea at the same time, unstirred. Predict the order in which they fully dissolve, and explain your reasoning.",
        "options": [
            {
             "text": "Caster sugar first, then granulated, then the cube last — finer grains expose more surface to the tea",
             "correct": True,
            },
            {
             "text": "The cube first, because a single solid piece dissolves more efficiently than loose grains",
             "correct": False,
             "why": "A compact cube exposes far LESS surface to the tea than the same mass broken into grains. It should be slowest, not fastest.",
            },
            {
             "text": "All three at the same time, since it is the same mass of the same sugar in every cup",
             "correct": False,
             "why": "Same mass and same sugar, but very different surface area exposed to the tea in each case — and that changes the order.",
            },
            {
             "text": "It cannot be predicted without first stirring each of the cups",
             "correct": False,
             "why": "Stirring is not needed to predict the order here. Surface area alone, without any stirring, already decides which dissolves fastest.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h18",
        "band": "harder",
        "text": "A student claims that because oil and vinegar can be shaken into a temporary, cloudy-looking mixture, oil must be at least a little bit soluble in vinegar. Evaluate this claim using what a solution does once left standing.",
        "options": [
            {
             "text": "The claim is right — any liquid that can be mixed with another, even briefly, counts as at least a little soluble in it",
             "correct": False,
             "why": "Briefly looking mixed while being shaken is not what dissolving means. A true solution stays evenly mixed once you stop disturbing it.",
            },
            {
             "text": "The claim is wrong — a genuine solution stays mixed once left still, and the cloudy mixture separates back into two layers within seconds",
             "correct": True,
            },
            {
             "text": "The claim is right, but only while the mixture is actually cloudy",
             "correct": False,
             "why": "The cloudiness is tiny droplets of oil suspended for a moment, not oil spread through the vinegar as dissolved particles. It is not dissolving at any point.",
            },
            {
             "text": "The claim cannot be evaluated without a laboratory test for solubility",
             "correct": False,
             "why": "Watching the layers reappear within seconds of standing still is itself a clear, sufficient test here.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h19",
        "band": "harder",
        "text": "Two students run the same test: warming a glass of water AND stirring it at the same time, then comparing how much sugar dissolves against a cold, unstirred glass. Design a fairer pair of tests that would let them work out the separate effects of warming and stirring.",
        "options": [
            {
             "text": "Repeat the original test several more times, using the same warm-and-stirred glass each time",
             "correct": False,
             "why": "Repeating the same combined test only shows it is repeatable. It still cannot separate warming's effect from stirring's.",
            },
            {
             "text": "Use a bigger glass of water for the warm-and-stirred test, to make the difference more obvious and easier for everybody watching to see clearly",
             "correct": False,
             "why": "A bigger glass changes yet another variable rather than isolating the two already in question.",
            },
            {
             "text": "Compare warm-unstirred against cold-unstirred, and separately compare cold-stirred against cold-unstirred, changing only one thing each time",
             "correct": True,
            },
            {
             "text": "There is no fair way to test this — warming and stirring can never be separated from one another in any experiment, however carefully it is designed",
             "correct": False,
             "why": "They can be separated, simply by changing only one of the two at a time across a set of tests, keeping everything else the same.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h20",
        "band": "harder",
        "text": "Sea water holds about 35 g of salt per litre. A saltwater lake, cut off from the ocean for thousands of years in a hot, rainless desert, now holds close to 300 g of salt per litre. Explain what has happened to the lake in terms of the amount of solvent, not the amount of solute.",
        "options": [
            {
             "text": "Extra salt has been added to the lake from an outside source over the thousands of years",
             "correct": False,
             "why": "The question specifically points to the SOLVENT changing. Nothing here suggests salt was added; evaporation losing water fits far better.",
            },
            {
             "text": "The lake's water has itself slowly turned into salt over time",
             "correct": False,
             "why": "Water cannot turn into salt. The salt was already dissolved in the lake; only the amount of water around it has changed.",
            },
            {
             "text": "The lake has simply become colder, and cold water concentrates dissolved salt",
             "correct": False,
             "why": "Temperature does not concentrate a solution on its own. Losing solvent through evaporation is what raises the concentration here.",
            },
            {
             "text": "Most of the water has left as vapour, leaving roughly the same dissolved salt spread through far less water",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h21",
        "band": "harder",
        "text": "A cook adds a pinch of salt to a large pan of water and "
                "it vanishes almost instantly. Later, adding a whole "
                "packet of salt to the same pan takes noticeably "
                "longer, even though the pan is nowhere near "
                "saturating. Explain why increasing the amount of "
                "solute added increases the time taken, even below "
                "saturation.",
        "options": [
            {"text": "There is simply more solute for the same volume "
                     "of solvent to work through before all of it has "
                     "gone into solution", "correct": True},
            {"text": "The larger amount raises the pan towards "
                     "saturation, which always slows dissolving right "
                     "down near the limit", "correct": False,
             "why": "The question states the pan is nowhere near "
                    "saturating. The slower time here is simply about "
                    "there being more solute to get through, not "
                    "approaching any limit."},
            {"text": "A whole packet of salt is a different grade, less "
                     "soluble than a small pinch of the same salt",
             "correct": False,
             "why": "It is exactly the same salt either way; only the "
                    "amount used has changed, not the substance."},
            {"text": "The water has cooled slightly by the time the "
                     "packet is added, which is what slows it down",
             "correct": False,
             "why": "Nothing in the scenario suggests a meaningful "
                    "temperature drop. The stated difference is simply "
                    "how much salt was added."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h22",
        "band": "harder",
        "text": "In one experiment, sugar takes 120 seconds to disappear and salt takes 90 seconds under identical conditions. A student concludes that salt must be the more soluble of the two. Explain why the timings cannot settle that question.",
        "options": [
            {
             "text": "The timings do settle it — the substance that disappears sooner is always the more soluble one",
             "correct": False,
             "why": "Disappearing sooner is a statement about rate. Solubility is about how much can dissolve, and the two are not linked.",
            },
            {
             "text": "Rate (how fast) and solubility (how much) are two independent properties of a solute, and neither one predicts the other",
             "correct": True,
            },
            {
             "text": "The timings cannot settle it because the two runs were made at different temperatures",
             "correct": False,
             "why": "The conditions are described as identical for the comparison. Two different properties of the two solutes explain the results, not a hidden temperature difference.",
            },
            {
             "text": "The timings settle it the other way round: sugar taking longer proves sugar is the more soluble",
             "correct": False,
             "why": "Taking longer is not what makes something more soluble. The two facts are about two different questions — speed, and capacity.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h23",
        "band": "harder",
        "text": "A student shakes chalk powder in water for twenty "
                "minutes, then argues that shaking it inside a sealed, "
                "pressurised container for a further two hours would "
                "finally dissolve it, since pressure adds even more "
                "energy than shaking alone. Evaluate this argument.",
        "options": [
            {"text": "The argument is sound, since pressure is simply a "
                     "more concentrated form of the same energy that "
                     "shaking supplies", "correct": False,
             "why": "Extra energy from shaking, however it is supplied, "
                    "does not make an insoluble solid dissolve. That is "
                    "not what stops chalk from dissolving."},
            {"text": "The argument is sound only if the water is also "
                     "warmed inside the sealed container", "correct": False,
             "why": "Warming does not make chalk soluble either. It "
                    "remains insoluble under any combination of shaking, "
                    "pressure and heat."},
            {"text": "The argument is flawed — chalk's insolubility is "
                     "not a lack of energy, so no amount of shaking or "
                     "pressure will dissolve it", "correct": True},
            {"text": "The argument cannot be evaluated without first "
                     "testing it in a real sealed container",
             "correct": False,
             "why": "It can be evaluated directly: chalk is insoluble in "
                    "water regardless of how it is agitated, which is "
                    "enough to settle the claim without a new test."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h24",
        "band": "harder",
        "text": "A student points out that salt's own solubility limit barely shifts between hot and cold water, then argues this means temperature cannot really speed up how quickly salt disappears either. Explain why that second claim does not follow from the first, and reconcile it with \"temperature mainly changes how much dissolves\".",
        "options": [
            {
             "text": "It does contradict the usual rule, and the usual claim about temperature must simply be wrong",
             "correct": False,
             "why": "The usual rule is about temperature's typical effect on the AMOUNT. Salt is the exception on amount, but temperature can still affect rate for any solute, salt included.",
            },
            {
             "text": "It does not contradict it, because stirring rather than temperature is what actually speeds salt up, so temperature is doing nothing here",
             "correct": False,
             "why": "Temperature speeds salt's dissolving up on its own, with no stirring at all. Stirring is a second, separate way of speeding it up.",
            },
            {
             "text": "It does not contradict it, because temperature changes only how much of a solute can dissolve and never how quickly any of it dissolves",
             "correct": False,
             "why": "Temperature changes the rate for every solute, alongside stirring and grinding. That is well established, and it is separate from the effect on the amount.",
            },
            {
             "text": "Temperature changes both rate and limit in general, but for salt specifically the limit barely moves while the rate still clearly does",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h25",
        "band": "harder",
        "text": "A recipe writer wants a milkshake to come out smooth and lump-free every time, and specifies warm rather than cold water for dissolving the milk powder, with an exact number of minutes to stir. Explain why BOTH the temperature and the stirring time need to be specified precisely, rather than just one of them.",
        "options": [
            {
             "text": "Either one on its own, warm water or a long enough stir, could get the milk powder fully dissolved — specifying both together simply makes the timing reliable for an ordinary cook",
             "correct": True,
            },
            {
             "text": "Only the temperature matters here; the stirring time is listed purely as a formality and has no effect on the result",
             "correct": False,
             "why": "Stirring speeds dissolving too, alongside temperature. Leaving it unspecified could still leave milk powder undissolved within a sensible mixing time.",
            },
            {
             "text": "Only the stirring time matters here; the temperature of the water makes no difference to how milk powder dissolves",
             "correct": False,
             "why": "Warm water speeds dissolving compared with cold, for milk powder as for most solids. Temperature is not irrelevant here.",
            },
            {
             "text": "Neither the temperature nor the stirring time matters for a smooth milkshake — smoothness depends only on how hard the drink is shaken at the end",
             "correct": False,
             "why": "Shaking at the end assumes the powder is already fully dissolved. If it never properly dissolved, the lumps are still there however hard it is shaken.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h26",
        "band": "harder",
        "text": "Baking soda in water disappears with no bubbles; baking "
                "soda in vinegar disappears with vigorous fizzing. A "
                "student argues that the fizzing simply means the "
                "baking soda is dissolving \"more thoroughly\" in "
                "vinegar. Evaluate this using what a reaction, as "
                "opposed to dissolving, actually does.",
        "options": [
            {"text": "The argument is right — more bubbles simply mean more of the baking soda has broken up into smaller and smaller particles as the reaction proceeds around it", "correct": False,
             "why": "The bubbles are a new gas, formed by a reaction "
                    "between the baking soda and the vinegar, not "
                    "smaller particles of baking soda itself."},
            {"text": "The argument is wrong — the fizzing is a sign of a "
                     "new gas being made, which never happens in "
                     "ordinary dissolving", "correct": True},
            {"text": "The argument is right, since \"thoroughly\" simply "
                     "describes how completely a solid has vanished from "
                     "view either way", "correct": False,
             "why": "Vanishing from view happens in both cases, quietly "
                    "or with fizzing. The fizzing specifically signals a "
                    "reaction is under way, not a more complete "
                    "dissolving."},
            {"text": "It cannot be evaluated without weighing the "
                     "baking soda before and after each test",
             "correct": False,
             "why": "The presence of a new gas — the fizzing itself — is "
                    "already enough evidence that something more than "
                    "dissolving is happening in the vinegar."},
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h27",
        "band": "harder",
        "text": "A swimming pool's floating chlorine dispenser and a slow-release fertiliser granule both use limited surface area to control dissolving rate over weeks. Explain the one key difference in what each is designed to release the substance INTO.",
        "options": [
            {
             "text": "There is no real difference — both release their substance into exactly the same kind of environment, whether that environment happens to be wet, damp or fully submerged",
             "correct": False,
             "why": "A swimming pool and damp garden soil are very different environments for a slowly dissolving solid, even though both use the same surface-area principle.",
            },
            {
             "text": "The chlorine dispenser releases into air, and the fertiliser releases into water",
             "correct": False,
             "why": "The chlorine tablets are in constant contact with pool water, not air. Both examples release into a moist or wet environment.",
            },
            {
             "text": "The chlorine dispenser releases into a large body of standing pool water, while the fertiliser releases into damp soil around plant roots",
             "correct": True,
            },
            {
             "text": "The fertiliser is designed to be taken up by the plant straight from the granule, while the chlorine never leaves its dispenser",
             "correct": False,
             "why": "The fertiliser has to dissolve into the soil moisture before a root can take it up, and the chlorine spreads right through the pool. Both leave the solid and enter what surrounds it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h28",
        "band": "harder",
        "text": "A student proposes using very fine table salt instead of coarse dishwasher salt \"because fine salt is cheaper and dissolves just fine in water\". Explain the flaw in this reasoning for a dishwasher specifically.",
        "options": [
            {
             "text": "There is no real flaw here — fine salt dissolving \"just fine\" in ordinary water is all that matters for how a dishwasher gets its dishes clean and properly rinsed",
             "correct": False,
             "why": "How fast it dissolves matters just as much as whether it dissolves at all, since the whole point of the coarse grain is spreading the effect across the wash.",
            },
            {
             "text": "Fine table salt would react with the dishwasher's detergent and stop it from working",
             "correct": False,
             "why": "The concern with fine salt in a dishwasher is its dissolving RATE, not a chemical reaction with the detergent.",
            },
            {
             "text": "Fine table salt is a chemically different substance from coarse dishwasher salt",
             "correct": False,
             "why": "Both are essentially the same substance, sodium chloride, at different grain sizes. The difference that matters here is the dissolving rate, not the chemistry.",
            },
            {
             "text": "Fine salt would dissolve almost immediately rather than gradually, so the dishwasher would run out of its intended effect partway through the wash",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h29",
        "band": "harder",
        "text": "A bar of soap shrinks, keeping roughly the same shape, over several weeks of use. A sugar cube left completely submerged in water for the same length of time dissolves away entirely far sooner. Explain why the soap lasts so much longer even though both are dissolving from the outside in.",
        "options": [
            {
             "text": "The soap is used briefly and rinsed rather than left constantly submerged, so far less total time is actually spent in contact with water",
             "correct": True,
            },
            {
             "text": "Soap simply does not dissolve in water, unlike sugar, which is why it lasts so much longer",
             "correct": False,
             "why": "Soap genuinely does dissolve — the dissolved soap is what produces the lather. It lasts longer for a different reason.",
            },
            {
             "text": "A bar of soap is always a very much larger mass than a small sugar cube, and that difference in starting mass fully explains the time difference on its own",
             "correct": False,
             "why": "Mass alone would not explain a difference measured in weeks against minutes. The real driver is how much time each spends actually in contact with water.",
            },
            {
             "text": "Soap becomes less soluble the more it is used, slowing its own dissolving down over time",
             "correct": False,
             "why": "Nothing about repeated use changes soap's solubility. It dissolves at a similar rate each time it gets wet; it is simply wet for far less total time than a submerged sugar cube.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h30",
        "band": "harder",
        "text": "A hiker uses one purification tablet per litre of stream water, and it dissolves within a minute. A second hiker uses two tablets in the same litre, and finds the water takes noticeably longer to clear of visible tablet fragments. Explain why doubling the tablets increases the time.",
        "options": [
            {
             "text": "Two tablets react with each other, forming a less soluble compound that resists dissolving",
             "correct": False,
             "why": "The tablets do not react with one another. Each dissolves independently; there are simply twice as many particles for the water to work through.",
            },
            {
             "text": "There is simply more solid for the same litre of water to dissolve, so it takes longer even though neither amount is anywhere near saturating it",
             "correct": True,
            },
            {
             "text": "The extra tablet noticeably cools the stream water down as it dissolves, and that drop in temperature is what slows the whole process down compared with using a single tablet",
             "correct": False,
             "why": "A purification tablet dissolving does not meaningfully change the water's temperature. The extra time comes from the extra amount of solid, not a temperature change.",
            },
            {
             "text": "One litre of stream water becomes saturated once a second tablet is added",
             "correct": False,
             "why": "A litre of water can dissolve far more than two small tablets before reaching any limit. Saturation is not what is slowing this down.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h31",
        "band": "harder",
        "text": "5 g of sugar dissolved in 50 g of water tastes noticeably sweeter than 5 g of sugar dissolved in 200 g of water, even though the same mass of sugar was used both times. A student concludes that \"the same amount of a solute always tastes the same, however much solvent it is in\". Evaluate this conclusion.",
        "options": [
            {
             "text": "The conclusion is right, and the two differently-diluted drinks described in the example must actually taste exactly the same to any careful taster who tries them side by side",
             "correct": False,
             "why": "The example itself states the two drinks taste noticeably different, which already contradicts the conclusion being evaluated.",
            },
            {
             "text": "The conclusion is right for solids, but not for liquids or gases dissolved in water",
             "correct": False,
             "why": "The example that disproves it is a solid, sugar, dissolved in water. The flaw is in the reasoning about mass and taste, not about which state the solute is in.",
            },
            {
             "text": "The conclusion is wrong — how strong something tastes depends on concentration, the solute spread through a given amount of solvent, not on the solute's mass alone",
             "correct": True,
            },
            {
             "text": "The conclusion cannot be evaluated without measuring the exact temperature of both drinks",
             "correct": False,
             "why": "Temperature is not the variable at issue here. The amount of water the same mass of sugar is spread through is what changes the taste.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-02-h32",
        "band": "harder",
        "text": "A student writes: \"grinding and warming are basically the same trick, since both just add energy to help dissolving along.\" Assess this claim by identifying what grinding actually changes, as opposed to what warming changes.",
        "options": [
            {
             "text": "The claim is correct, since the physical act of grinding also heats up the solute slightly through friction, and that slight extra warmth is really the underlying reason why grinding works",
             "correct": False,
             "why": "Any slight warming from friction while grinding is not what makes crushed solutes dissolve faster. Exposed surface area is the actual mechanism.",
            },
            {
             "text": "The claim is correct, because both grinding and warming always raise how much solute the solvent can hold",
             "correct": False,
             "why": "Grinding never raises how much can dissolve, only how fast. That is exactly where the claim's comparison breaks down.",
            },
            {
             "text": "The claim is wrong because grinding has no effect on dissolving speed, only warming does",
             "correct": False,
             "why": "Grinding does speed dissolving up, by exposing more surface to the solvent at once. It works through a different mechanism from warming, not through no mechanism at all.",
            },
            {
             "text": "Grinding changes the surface area exposed to the solvent; warming changes the energy in the particles themselves — two different mechanisms that can both speed dissolving up",
             "correct": True,
            },
        ],
        "figure": None,
    },
]
