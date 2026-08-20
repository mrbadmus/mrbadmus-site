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
]
