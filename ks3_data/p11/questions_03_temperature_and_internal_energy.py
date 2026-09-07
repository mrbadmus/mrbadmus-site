"""P11 lesson 03 — Temperature, particle motion and internal energy:
twelve questions (MRB-223).

Written against Design's page. The spark and the bath, the four amounts of
water on one thermometer and the logarithmic panel are hers.

The discriminations, in the order the lesson builds them:

  · what a thermometer reading IS — an average per particle, and not an
    amount of anything (`ENER-28`);
  · internal energy as the TOTAL, in joules, depending on how much there
    is (`ENER-13`);
  · which way heating goes, and what decides how much there is to move;
  · energy going in without the temperature moving (`ENER-29`) — the
    harder band sits there and on storage.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NEITHER MARKED RUNG IS RESTATED: the two beakers at 50 °C and the
spark landing on an arm are the ladder's. `s03` asks the spark question
from the other end — what makes it harmless, rather than which statement
about it is right — and is the only place the two come near.
"""

UNIT = "P11"
LESSON = "temperature-and-internal-energy"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p11-03-e01",
        "band": "easier",
        "text": "What does a temperature reading tell you?",
        "options": [
            {"text": "How much kinetic energy one particle has, on average",
             "correct": True},
            {"text": "How much energy the whole object contains, particle "
                     "by particle", "correct": False,
             "why": "That is the internal energy, and it depends on how many "
                    "particles there are as well."},
            {"text": "How many particles there are in the object altogether",
             "correct": False,
             "why": "A thermometer says nothing at all about how much there "
                    "is."},
            {"text": "How much heat the object has stored up inside it",
             "correct": False,
             "why": "An object does not contain heat. Heating is energy on "
                    "the move; what an object holds is internal energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e02",
        "band": "easier",
        "text": "Internal energy is measured in which unit?",
        "options": [
            {"text": "Degrees Celsius", "correct": False,
             "why": "That is the unit of temperature. Internal energy is an "
                    "amount of energy."},
            {"text": "Joules", "correct": True},
            {"text": "Grams", "correct": False,
             "why": "Grams measure mass. Mass is one of the things internal "
                    "energy depends on, but it is not the unit."},
            {"text": "Watts", "correct": False,
             "why": "A watt is a joule every second — a rate. Internal energy "
                    "is a total, not a rate."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e03",
        "band": "easier",
        "text": "Two identical mugs of water are at 70 °C and 30 °C and are "
                "put in contact. Which way does energy travel?",
        "options": [
            {"text": "From the colder one to the hotter one, because the "
                     "hotter one pulls it in", "correct": False,
             "why": "Energy travels from hotter to colder on its own. Being "
                    "hot does not let an object pull energy in."},
            {"text": "Neither way, because they are both water at the same "
                     "pressure", "correct": False,
             "why": "Being the same substance at the same pressure makes no "
                    "difference. What decides it is the temperature "
                    "difference."},
            {"text": "From the hotter one to the colder one, until both read "
                     "the same", "correct": True},
            {"text": "Both ways at exactly the same rate, so nothing changes "
                     "at all", "correct": False,
             "why": "The net flow is one way. If nothing changed the two "
                    "temperatures would never meet, and they do."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e04",
        "band": "easier",
        "text": "A teaspoon and a bathful of water are both at 40 °C. Which "
                "holds more internal energy?",
        "options": [
            {"text": "The teaspoon, because the energy is concentrated in it",
             "correct": False,
             "why": "Nothing is concentrated. Both have the same energy per "
                    "particle; the bath simply has far more particles."},
            {"text": "Neither — the same temperature means the same energy",
             "correct": False,
             "why": "The same temperature means the same average per "
                    "particle. The total also depends on how many there "
                    "are."},
            {"text": "It cannot be compared unless the temperatures differ",
             "correct": False,
             "why": "It compares perfectly well: the same average, and "
                    "vastly different numbers of particles."},
            {"text": "The bathful, because it has far more particles",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p11-03-s01",
        "band": "standard",
        "text": "A kettleful of water is at 100 °C and a swimming pool is at "
                "20 °C. Which statement is right?",
        "options": [
            {"text": "The kettle holds more internal energy, because it is "
                     "at the far higher temperature", "correct": False,
             "why": "Temperature is an average per particle. A pool has so "
                    "many more particles that its total is vastly larger."},
            {"text": "The pool holds far more internal energy, and the kettle "
                     "is at the higher temperature", "correct": True},
            {"text": "They hold the same amount, because energy is always "
                     "conserved", "correct": False,
             "why": "Conservation says energy is not created or destroyed. It "
                    "does not make two different objects hold equal "
                    "amounts."},
            {"text": "The pool is at the higher temperature, because it holds "
                     "far more energy in total", "correct": False,
             "why": "More total energy does not mean a higher temperature. "
                    "The pool reads 20 °C on any thermometer."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s02",
        "band": "standard",
        "text": "Ice and water sit together in a beaker on a hotplate and the "
                "thermometer reads 0 °C for several minutes. What is "
                "happening to the energy going in?",
        "options": [
            {"text": "It is being destroyed, because nothing in the beaker "
                     "is getting any hotter", "correct": False,
             "why": "Energy is never destroyed. It is going somewhere the "
                    "thermometer cannot see."},
            {"text": "It is escaping to the room as fast as it arrives, so "
                     "none of it is absorbed at all", "correct": False,
             "why": "Some always escapes, and the beaker is absorbing energy "
                    "the whole time — the ice is melting."},
            {"text": "It is breaking the forces holding the solid together, "
                     "rather than speeding particles up", "correct": True},
            {"text": "It is not going in at all until every last piece of "
                     "the ice has gone", "correct": False,
             "why": "It is going in from the first moment. If it were not, "
                    "the ice would not melt."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s03",
        "band": "standard",
        "text": "What makes a spark from a grinder harmless when it lands on "
                "your skin?",
        "options": [
            {"text": "Sparks are nowhere near as hot as the quoted figure "
                     "suggests", "correct": False,
             "why": "The temperature is real. What is small is how much "
                    "matter is at it."},
            {"text": "Skin reflects the energy away before it can be "
                     "absorbed", "correct": False,
             "why": "Skin absorbs it. There is simply very little of it to "
                    "absorb."},
            {"text": "The spark is travelling too fast to transfer anything "
                     "to the skin", "correct": False,
             "why": "Speed is not the reason. A slow spark of the same size "
                    "would be just as harmless."},
            {"text": "It has almost no mass, so it carries almost no internal "
                     "energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s04",
        "band": "standard",
        "text": "Which change raises an object's internal energy without "
                "raising its temperature?",
        "options": [
            {"text": "Melting it at its melting point", "correct": True},
            {"text": "Warming it by one degree on a hotplate",
             "correct": False,
             "why": "That raises the temperature by definition, and the "
                    "question asks for the case where it does not move."},
            {"text": "Cutting it in half and keeping one piece",
             "correct": False,
             "why": "Cutting halves the amount, so the piece you keep holds "
                    "less. Nothing has been added."},
            {"text": "Cooling it down towards freezing point",
             "correct": False,
             "why": "Cooling takes energy out, so the internal energy goes "
                    "down rather than up."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p11-03-h01",
        "band": "harder",
        "text": "One mug holds 250 g of water and another holds 500 g. Both "
                "are warmed from 20 °C to 60 °C. What is true of the energy "
                "needed?",
        "options": [
            {"text": "The same for both, because the temperature change is "
                     "the same", "correct": False,
             "why": "The change is the same per particle. Twice the particles "
                    "need twice the energy."},
            {"text": "Twice as much for the 250 g mug, because it warms "
                     "faster", "correct": False,
             "why": "Warming faster is about the rate. The total energy "
                    "needed is set by the mass and the temperature change."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Twice as much for the 500 g mug, twice the mass",
             "correct": True},
            {"text": "Four times as much for the 500 g mug", "correct": False,
             "why": "Doubling the mass doubles the energy needed. Nothing "
                    "here is squared."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h02",
        "band": "harder",
        "text": "Why is water rather than air put inside a hot water bottle?",
        "options": [
            {"text": "Water is heavier, so it presses on you more, and "
                     "pressure is what you feel as warmth",
             "correct": False,
             "why": "Pressing is not what warms you. What matters is how much "
                    "energy it can hold and give out."},
            {"text": "Air would leak out of a sealed bottle", "correct": False,
             "why": "A sealed bottle holds either one. The reason is what "
                    "each can store."},
            {"text": "Water conducts electricity and air does not",
             "correct": False,
             "why": "Nothing here is electrical."},
            {"text": "The same volume of water holds far more particles, and "
                     "each degree costs far more energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h03",
        "band": "harder",
        "text": "A storage heater's bricks are at 60 °C in the morning and "
                "25 °C by evening, and the room has stayed warm. What "
                "happened?",
        "options": [
            {"text": "Internal energy moved out of the bricks into the room, "
                     "because the bricks were hotter", "correct": True},
            {"text": "The bricks made new energy as they cooled",
             "correct": False,
             "why": "Nothing makes energy. The bricks gave out what they had "
                    "been given overnight."},
            {"text": "Cold moved from the room into the bricks",
             "correct": False,
             "why": "Cold is not a substance and does not travel. Energy "
                    "travelled, from hot to cold."},
            {"text": "The bricks lost mass overnight, and that lost mass "
                     "turned into the warmth in the room",
             "correct": False,
             "why": "The bricks weigh the same at both ends of the day. What "
                    "left them was energy, not matter."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h04",
        "band": "harder",
        "text": "Which pair could hold the same internal energy while reading "
                "very different temperatures?",
        "options": [
            {"text": "Two identical mugs of water", "correct": False,
             "why": "Same substance and same mass, so the thermometer decides "
                    "it: different temperatures mean different totals."},
            {"text": "A small amount of a very hot substance and a large "
                     "amount of a cool one", "correct": True},
            {"text": "Two objects at the same temperature", "correct": False,
             "why": "Then their temperatures are not different, which is what "
                    "the question asks for."},
            {"text": "Any two objects at all, as long as both of them are "
                     "warm to the touch", "correct": False,
             "why": "Being warm is not enough. It depends on how much of each "
                    "there is."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p11-03-e05",
        "band": "easier",
        "text": "Internal energy depends on the temperature and on…",
        "options": [
            {"text": "how much matter there is", "correct": True},
            {"text": "the colour of the object", "correct": False,
             "why": "Colour affects how well something radiates, not how much "
                    "energy its particles hold."},
            {"text": "how high above the ground it is", "correct": False,
             "why": "Height fills a gravitational store, which is a different "
                    "store altogether."},
            {"text": "how long it has been standing there", "correct": False,
             "why": "Time lets it cool, but it is not a second quantity in "
                    "the total."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e06",
        "band": "easier",
        "text": "Which quantity is measured in degrees Celsius?",
        "options": [            {"text": "Internal energy", "correct": False,
             "why": "Internal energy is a total amount of energy, measured in "
                    "joules."},
            {"text": "Mass", "correct": False,
             "why": "Mass is measured in grams or kilograms."},
            {"text": "Heating", "correct": False,
             "why": "Heating is a transfer of energy, so it is measured in "
                    "joules too."},
            {"text": "Temperature", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e07",
        "band": "easier",
        "text": "Heating is…",
        "options": [            {"text": "energy moving from a hotter object to a colder one",
             "correct": True},
            {"text": "something an object contains", "correct": False,
             "why": "What an object contains is internal energy; heating is "
                    "what moves between two objects."},
            {"text": "the same thing as temperature", "correct": False,
             "why": "Temperature is a reading in degrees; heating is a "
                    "process measured in joules."},
            {"text": "energy moving from a colder object to a hotter one",
             "correct": False,
             "why": "That is the direction energy never goes on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e08",
        "band": "easier",
        "text": "When does heating between two touching objects stop?",
        "options": [            {"text": "When the hotter one has given away all its energy",
             "correct": False,
             "why": "It never gives away all of it; the flow stops long "
                    "before that."},
            {"text": "As soon as they touch", "correct": False,
             "why": "Touching is when it starts, not when it finishes."},
            {"text": "When they have the same internal energy",
             "correct": False,
             "why": "A mug and a pool can reach the same temperature holding "
                    "wildly different amounts."},
            {"text": "When their temperatures are equal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e09",
        "band": "easier",
        "text": "What is absolute zero?",
        "options": [            {"text": "−273.15 °C", "correct": True},
            {"text": "0 °C, the freezing point of water", "correct": False,
             "why": "Water freezes at 0 °C, but things get far colder than "
                    "that."},
            {"text": "−100 °C", "correct": False,
             "why": "Plenty of things are colder than that; it is not the "
                    "limit."},
            {"text": "The temperature of empty space", "correct": False,
             "why": "Space is a little above absolute zero, not at it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e10",
        "band": "easier",
        "text": "Can anything be cooled below absolute zero?",
        "options": [
            {"text": "Yes, with a good enough refrigerator", "correct": False,
             "why": "No refrigerator can pass it; the particles already carry "
                    "the least energy allowed."},
            {"text": "Yes, in space", "correct": False,
             "why": "Space itself sits a little above it, and nothing goes "
                    "below."},
            {"text": "No, not by any means at all", "correct": True},
            {"text": "Only for a very short time", "correct": False,
             "why": "It cannot be reached even briefly, let alone passed."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e11",
        "band": "easier",
        "text": "Two identical cups of water are at 60 °C and 20 °C. Which "
                "holds more internal energy?",
        "options": [            {"text": "The 20 °C one", "correct": False,
             "why": "Same amount of water, lower temperature, so it holds "
                    "less."},
            {"text": "It cannot be told without weighing them",
             "correct": False,
             "why": "They are stated to be identical, so the amounts match."},
            {"text": "They hold the same, because the cups are identical",
             "correct": False,
             "why": "Identical cups means the same amount of water, and then "
                    "the temperature decides."},
            {"text": "The 60 °C one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e12",
        "band": "easier",
        "text": "A tiny spark at 1000 °C lands on your arm and does no harm. "
                "Why?",
        "options": [
            {"text": "Because it cools before it lands", "correct": False,
             "why": "It is still glowing when it arrives; its temperature is "
                    "genuinely high."},
            {"text": "Because skin is a good conductor and passes it on",
             "correct": False,
             "why": "Skin conducts poorly, and the reason is how little "
                    "energy the spark carries."},
            {"text": "Because it has almost no mass, so almost no internal "
                     "energy",
             "correct": True},
            {"text": "Because 1000 °C is not really very hot", "correct": False,
             "why": "It is extremely hot; what saves you is how little of it "
                    "there is."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e13",
        "band": "easier",
        "text": "Which quantity is measured in joules?",
        "options": [            {"text": "Internal energy", "correct": True},
            {"text": "Temperature", "correct": False,
             "why": "Temperature is read in degrees Celsius."},
            {"text": "The mass of an object", "correct": False,
             "why": "Mass is measured in grams or kilograms."},
            {"text": "The density of a material", "correct": False,
             "why": "Density is in g/cm³ or kg/m³."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p11-03-s05",
        "band": "standard",
        "text": "A 200 g beaker of water and a 600 g beaker are both at "
                "50 °C. Which statement is right?",
        "options": [
            {"text": "The 600 g one is at a higher temperature",
             "correct": False,
             "why": "Both were measured at 50 °C; temperature does not depend "
                    "on how much there is."},
            {"text": "Both hold the same internal energy, because both are at "
                     "50 °C",
             "correct": False,
             "why": "Temperature is the average per particle; the 600 g "
                    "beaker has three times as many."},
            {"text": "Same temperature, but the 600 g one holds more internal "
                     "energy",
             "correct": True},
            {"text": "Same internal energy, but the 200 g one is hotter",
             "correct": False,
             "why": "Both halves are wrong: the temperatures match and the "
                    "energies do not."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s06",
        "band": "standard",
        "text": "A spark at 1000 °C and a bath at 40 °C. Which has the higher "
                "temperature, and which the greater internal energy?",
        "options": [
            {"text": "The spark for both", "correct": False,
             "why": "It wins on temperature and loses badly on internal "
                    "energy, having almost no mass."},
            {"text": "The bath for both", "correct": False,
             "why": "The bath holds far more energy, but 40 °C is nowhere "
                    "near 1000 °C."},
            {"text": "The spark is hotter; the bath holds far more energy",
             "correct": True},
            {"text": "The bath is hotter; the spark holds far more energy",
             "correct": False,
             "why": "Both halves are the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s07",
        "band": "standard",
        "text": "A drink at 5 °C stands in a room at 20 °C. Which way does "
                "energy travel?",
        "options": [            {"text": "From the drink into the room", "correct": False,
             "why": "Energy travels from hotter to colder, and the room is "
                    "the warmer of the two."},
            {"text": "Neither way, because cold is not a substance",
             "correct": False,
             "why": "Cold is not a substance, and that is exactly why ENERGY "
                    "moves — into the drink."},
            {"text": "From the room into the drink", "correct": True},
            {"text": "Both ways equally, so nothing changes", "correct": False,
             "why": "Energy passes both ways, but there is a net flow into "
                    "the drink until they match."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s08",
        "band": "standard",
        "text": "Why does adding energy to something not always raise its "
                "temperature?",
        "options": [            {"text": "Because some energy always leaks away before it can be "
                     "measured",
             "correct": False,
             "why": "Even with no losses the temperature holds still during a "
                    "change of state."},
            {"text": "Because energy stops being absorbed once something is "
                     "warm",
             "correct": False,
             "why": "It keeps absorbing energy throughout; the temperature is "
                    "what pauses."},
            {"text": "Because a thermometer cannot read a rise that small",
             "correct": False,
             "why": "The reading holds steady for minutes, far longer than "
                    "any limit of the instrument."},
            {"text": "Because during a change of state it goes into the "
                     "particles' arrangement",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s09",
        "band": "standard",
        "text": "Why does a small hot object cool down much faster than a "
                "large one at the same temperature?",
        "options": [            {"text": "Because it holds far less internal energy to give away",
             "correct": True},
            {"text": "Because it is at a higher temperature to start with",
             "correct": False,
             "why": "The question says both start at the same temperature."},
            {"text": "Because small objects conduct better", "correct": False,
             "why": "Being small does not change what a material is made of "
                    "or how it conducts."},
            {"text": "Because large objects are always better insulated",
             "correct": False,
             "why": "They need not be; what matters is how much energy is "
                    "there to lose."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s10",
        "band": "standard",
        "text": "Two objects at exactly the same temperature are put in "
                "contact. What happens?",
        "options": [            {"text": "Energy flows from the larger to the smaller",
             "correct": False,
             "why": "Size does not drive a flow; a temperature difference "
                    "does, and there is none."},
            {"text": "Energy flows from the one holding more internal energy",
             "correct": False,
             "why": "Internal energy does not set the direction; temperature "
                    "does."},
            {"text": "There is no net transfer between them", "correct": True},
            {"text": "They both cool down together", "correct": False,
             "why": "Anything they lose goes to the surroundings, not between "
                    "the two."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s11",
        "band": "standard",
        "text": "A cup of tea cools from 80 °C to 20 °C in a room. Where has "
                "the energy gone?",
        "options": [            {"text": "It has been destroyed as the tea cooled",
             "correct": False,
             "why": "Nothing destroys energy; it has moved rather than "
                    "vanished."},
            {"text": "It has turned into cold, which has entered the tea",
             "correct": False,
             "why": "Cold is not a substance and nothing entered; energy "
                    "left."},
            {"text": "Into the cup, which is now storing it", "correct": False,
             "why": "The cup cools too, and passes its share on to the "
                    "room."},
            {"text": "Into the thermal store of the room around it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s12",
        "band": "standard",
        "text": "Which statement about heating is right?",
        "options": [            {"text": "It is a process, and it stops when the temperatures "
                     "match",
             "correct": True},
            {"text": "It is a quantity an object contains", "correct": False,
             "why": "What an object contains is internal energy; heating is "
                    "the transfer between two."},
            {"text": "It is another word for temperature", "correct": False,
             "why": "Temperature is a reading in degrees; heating moves "
                    "joules."},
            {"text": "It can move energy from a colder object to a hotter "
                     "one",
             "correct": False,
             "why": "That direction never happens on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s13",
        "band": "standard",
        "text": "Two kettles hold 0.5 litres and 1.5 litres of water, both at "
                "100 °C. Compare them.",
        "options": [
            {"text": "The larger one is hotter and holds more energy, since "
                     "there is more of it",
             "correct": False,
             "why": "Both read 100 °C, so neither is hotter."},
            {"text": "Same temperature and the same internal energy",
             "correct": False,
             "why": "Three times as much water means three times as many "
                    "particles to hold energy."},
            {"text": "Same temperature; the larger holds three times the "
                     "internal energy",
             "correct": True},
            {"text": "The smaller is hotter, because it heats up quicker",
             "correct": False,
             "why": "It reaches 100 °C sooner, and both are at 100 °C when "
                    "compared."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p11-03-h05",
        "band": "harder",
        "text": "Why is heat a poor word for something an object contains?",
        "options": [
            {"text": "Because objects contain no energy at all",
             "correct": False,
             "why": "They contain a great deal — that is exactly what "
                    "internal energy is."},
            {"text": "Because only really hot objects contain anything worth "
                     "naming",
             "correct": False,
             "why": "A cold object holds internal energy too, just less of "
                    "it."},
            {"text": "Because heat is measured in degrees rather than joules",
             "correct": False,
             "why": "Heating moves joules; degrees measure temperature."},
            {"text": "Because heating names a transfer, not what is contained",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h06",
        "band": "harder",
        "text": "A cup of boiling water is poured into a cold bath. What "
                "happens to the bath's temperature?",
        "options": [
            {"text": "It rises to somewhere near 100 °C", "correct": False,
             "why": "One cup cannot warm a bathful; there are far too many "
                    "particles to share it between."},
            {"text": "It rises by a very small amount", "correct": True},
            {"text": "It does not change at all", "correct": False,
             "why": "The energy really does arrive; the rise is small rather "
                    "than absent."},
            {"text": "It falls, because the cup cools the water",
             "correct": False,
             "why": "The added water is far hotter than the bath, so it can "
                    "only raise the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h07",
        "band": "harder",
        "text": "How can a pool at 25 °C hold more internal energy than a mug "
                "at 90 °C?",
        "options": [
            {"text": "Because 25 °C is hotter than 90 °C on the scale used "
                     "for pools",
             "correct": False,
             "why": "There is one Celsius scale, and 90 °C is the higher "
                    "reading."},
            {"text": "Because the pool has vastly more particles, each "
                     "holding a little",
             "correct": True},
            {"text": "Because water in a pool is a different substance",
             "correct": False,
             "why": "It is the same water; the amount of it is what "
                    "differs."},
            {"text": "Because internal energy does not depend on temperature "
                     "at all",
             "correct": False,
             "why": "It depends on both — on the temperature AND on how much "
                    "matter there is."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h08",
        "band": "harder",
        "text": "A block at 40 °C and one at 60 °C are put in contact and "
                "left. What is the final temperature?",
        "options": [
            {"text": "Exactly 50 °C, halfway between them", "correct": False,
             "why": "Halfway would need the two to be equally able to store "
                    "energy, and they need not be."},
            {"text": "60 °C, because the hotter one wins", "correct": False,
             "why": "The hotter one cools as the colder one warms; neither "
                    "keeps its own value."},
            {"text": "Somewhere between the two, depending on how much of "
                     "each there is",
             "correct": True},
            {"text": "40 °C, because energy always spreads to the coldest "
                     "value",
             "correct": False,
             "why": "The colder one warms up as well, so it does not stay at "
                    "40 °C."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h09",
        "band": "harder",
        "text": "Why is there a lowest possible temperature but no highest "
                "one?",
        "options": [
            {"text": "Because thermometers cannot read below −273.15 °C",
             "correct": False,
             "why": "The limit is in the physics, not in the instrument."},
            {"text": "Because more energy can always be added, but not less "
                     "than the least",
             "correct": True},
            {"text": "Because there IS a highest temperature, and it has "
                     "simply not been measured",
             "correct": False,
             "why": "Nothing sets an upper limit the way absolute zero sets a "
                    "lower one."},
            {"text": "Because cold is a substance that runs out",
             "correct": False,
             "why": "Cold is not a substance at all; it is simply less "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h10",
        "band": "harder",
        "text": "A storage heater's bricks fall from 60 °C to 25 °C during "
                "the day, and the room has stayed warm. What has happened?",
        "options": [
            {"text": "The bricks have lost mass as they cooled",
             "correct": False,
             "why": "They weigh the same at the end of the day; it is energy "
                    "that has left."},
            {"text": "Internal energy has moved from the bricks into the "
                     "room",
             "correct": True},
            {"text": "The room has warmed the bricks, which is why they "
                     "changed",
             "correct": False,
             "why": "The bricks were the hotter of the two, so the flow was "
                    "out of them."},
            {"text": "The bricks have turned their temperature into energy",
             "correct": False,
             "why": "Temperature is not a store that converts; it is a "
                    "reading of the energy per particle."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h11",
        "band": "harder",
        "text": "Why does twice as much water need twice the energy for the "
                "same rise in temperature?",
        "options": [
            {"text": "Because it takes twice as long to warm up",
             "correct": False,
             "why": "It does take longer, and that is a consequence rather "
                    "than the reason."},
            {"text": "Because twice as many particles each need the same "
                     "increase",
             "correct": True},
            {"text": "Because a larger volume loses more energy to the room",
             "correct": False,
             "why": "Losses matter in practice, but the doubling holds even "
                    "with none at all."},
            {"text": "Because the temperature rise is always halved when the "
                     "mass doubles",
             "correct": False,
             "why": "The rise is stated to be the same; it is the energy "
                    "needed that doubles."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h12",
        "band": "harder",
        "text": "A student says a bigger object must be hotter, because it "
                "holds more energy. Correct them.",
        "options": [
            {"text": "They are right, since more energy always means a higher "
                     "temperature",
             "correct": False,
             "why": "A swimming pool holds far more energy than a spark and "
                    "is far cooler."},
            {"text": "Temperature is the energy PER PARTICLE, so size sets "
                     "the total, not the reading",
             "correct": True},
            {"text": "A bigger object always holds less energy, so they have "
                     "it backwards",
             "correct": False,
             "why": "More matter at the same temperature really does hold "
                    "more energy; the error is about the reading."},
            {"text": "Bigger objects cannot be measured with a thermometer",
             "correct": False,
             "why": "They are measured with one all the time, which is how we "
                    "know they can be cool."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h13",
        "band": "harder",
        "text": "Why does a thermometer read the same in a teaspoon of water "
                "and a bathful at the same temperature?",
        "options": [
            {"text": "Because a thermometer is not sensitive enough to tell "
                     "them apart",
             "correct": False,
             "why": "There is nothing to tell apart: the temperatures really "
                    "are equal."},
            {"text": "Because the reading is an average per particle, not a "
                     "total",
             "correct": True},
            {"text": "Because a teaspoon of water holds as much energy as a "
                     "bath",
             "correct": False,
             "why": "It holds far less; the reading is not a measure of the "
                    "total."},
            {"text": "Because the bath has cooled to match the teaspoon",
             "correct": False,
             "why": "The question puts them at the same temperature to begin "
                    "with."},
        ],
        "figure": None,
    },
]
