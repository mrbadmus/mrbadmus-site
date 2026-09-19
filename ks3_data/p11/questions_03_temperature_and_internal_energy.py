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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p11-03-e14",
        "band": "easier",
        "text": "Aluminium has a specific heat capacity of about 900 J/kg°C. "
                "What does that number tell you?",
        "options": [
            {"text": "How much energy is needed to warm 1 kg of it by 1 °C",
             "correct": True},
            {"text": "How hot aluminium gets before it melts", "correct": False,
             "why": "That is a melting point, a completely different "
                    "quantity measured in degrees, not joules per kilogram "
                    "per degree."},
            {"text": "How much aluminium is needed to fill 1 kg",
             "correct": False,
             "why": "That mixes up mass with the quantity itself; a specific "
                    "heat capacity says nothing about how much substance "
                    "there is."},
            {"text": "How fast aluminium heats up compared with other "
                     "metals", "correct": False,
             "why": "Speed of heating depends on more than this one number; "
                    "it tells you an energy requirement, not a rate."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e15",
        "band": "easier",
        "text": "Water's specific heat capacity is about 4200 J/kg°C. Lead's "
                "is about 130 J/kg°C. Which one needs LESS energy to warm "
                "1 kg by 1 °C?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "Water's figure is the far bigger of the two, so it "
                    "needs more energy, not less."},
            {"text": "Lead", "correct": True},
            {"text": "Both need the same energy", "correct": False,
             "why": "The two figures given are very different, so the "
                    "energy needed is very different too."},
            {"text": "It cannot be told from these numbers", "correct": False,
             "why": "It can — the smaller specific heat capacity is exactly "
                    "the one that needs less energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e16",
        "band": "easier",
        "text": "Why do scientists often measure temperature in kelvin rather "
                "than in degrees Celsius?",
        "options": [
            {"text": "Kelvin is a bigger unit, so the numbers are smaller",
             "correct": False,
             "why": "A kelvin is exactly the same size as a degree Celsius; "
                    "only where the scale starts is different."},
            {"text": "Kelvin was invented more recently", "correct": False,
             "why": "How old a scale is has nothing to do with why it is "
                    "used."},
            {"text": "The kelvin scale starts at absolute zero", "correct": True},
            {"text": "Kelvin is easier to convert into joules", "correct": False,
             "why": "Neither scale converts directly into joules; that "
                    "conversion needs more than a temperature reading "
                    "alone."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e17",
        "band": "easier",
        "text": "How close have laboratories come to reaching absolute zero?",
        "options": [
            {"text": "They have reached it exactly", "correct": False,
             "why": "Absolute zero has never been reached; the laws of "
                    "physics do not allow it."},
            {"text": "Nowhere close — within a few degrees at best",
             "correct": False,
             "why": "Laboratories have done vastly better than that — "
                    "within billionths of a degree."},
            {"text": "It is impossible to get anywhere near it", "correct": False,
             "why": "It is impossible to REACH it, but laboratories have got "
                    "extremely close, within billionths of a degree."},
            {"text": "Within a few billionths of a degree", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e18",
        "band": "easier",
        "text": "A hot water bottle stays warm for hours. What property of "
                "water makes it useful for this?",
        "options": [
            {"text": "It has a high specific heat capacity, so it stores a "
                     "lot of energy per degree", "correct": True},
            {"text": "It has a low density, so it floats comfortably against "
                     "the skin without feeling too heavy", "correct": False,
             "why": "Floating plays no part here; what matters is how much "
                    "energy the water can store as it cools."},
            {"text": "It boils at a high temperature", "correct": False,
             "why": "Boiling point is unrelated; a hot water bottle is used "
                    "well below boiling."},
            {"text": "It conducts electricity well", "correct": False,
             "why": "Electrical conduction has nothing to do with storing "
                    "warmth."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e19",
        "band": "easier",
        "text": "Coastal towns tend to have milder winters than inland towns "
                "at the same latitude. What is this linked to?",
        "options": [
            {"text": "The sea being saltier in winter, which changes how "
                     "quickly it evaporates into the air", "correct": False,
             "why": "Saltiness is not what changes the sea's ability to "
                    "store energy."},
            {"text": "The sea's high specific heat capacity, which releases "
                     "stored energy slowly", "correct": True},
            {"text": "Coastal air containing less oxygen than inland air",
             "correct": False,
             "why": "The amount of oxygen in the air has no bearing on "
                    "winter temperatures."},
            {"text": "Coastal towns generally being built on lower ground",
             "correct": False,
             "why": "Height above sea level is not what is being described "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e20",
        "band": "easier",
        "text": "Radiators and car cooling systems commonly use water rather "
                "than air. Why?",
        "options": [
            {"text": "Water is generally cheaper to manufacture and pipe "
                     "around than air is", "correct": False,
             "why": "Air costs nothing at all to obtain; cost is not the "
                    "reason water is chosen."},
            {"text": "Water is easier to see moving through pipes",
             "correct": False,
             "why": "Visibility plays no part in why a coolant is chosen."},
            {"text": "Water can carry far more energy for the same rise in "
                     "temperature", "correct": True},
            {"text": "Water boils at a lower temperature than air",
             "correct": False,
             "why": "Air does not have a boiling point in this context, and "
                    "this is not why water is chosen anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e21",
        "band": "easier",
        "text": "A bowl of soup cools from 70 °C down to 20 °C. What happens "
                "to the average kinetic energy of its particles?",
        "options": [
            {"text": "It stays the same, since the number of particles has "
                     "not changed", "correct": False,
             "why": "The number of particles is indeed unchanged, but each "
                    "one is moving more slowly, so the average per particle "
                    "falls."},
            {"text": "It rises, because cooling packs the particles closer "
                     "together", "correct": False,
             "why": "How closely particles are packed is not what the reading "
                    "measures; slower particles carry less kinetic energy."},
            {"text": "It cannot be said without knowing how much soup is in "
                     "the bowl", "correct": False,
             "why": "The average per particle is set by the temperature "
                    "alone, whatever amount of soup there is."},
            {"text": "It falls, because temperature is the average kinetic "
                     "energy per particle", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e22",
        "band": "easier",
        "text": "Which of these is the unit of specific heat capacity?",
        "options": [
            {"text": "J/kg°C", "correct": True},
            {"text": "J/°C", "correct": False,
             "why": "That leaves the mass out, and a specific heat capacity "
                    "is always quoted per kilogram."},
            {"text": "J/kg", "correct": False,
             "why": "That leaves the temperature out, and the figure is "
                    "always quoted per degree."},
            {"text": "kg/J°C", "correct": False,
             "why": "That turns the unit upside down; the joules go on top, "
                    "because it is an amount of energy that is being "
                    "quoted."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e23",
        "band": "easier",
        "text": "A bath and a kettle of water are both at 60 °C. Which "
                "quantity is the SAME for both?",
        "options": [
            {"text": "Internal energy", "correct": False,
             "why": "The bath has far more water, so its internal energy is "
                    "far greater even at a matching temperature."},
            {"text": "Average kinetic energy of one particle", "correct": True},
            {"text": "Total mass of water", "correct": False,
             "why": "A bath and a kettle hold very different amounts of "
                    "water."},
            {"text": "Total number of particles", "correct": False,
             "why": "Far more particles are in a bathful than in a "
                    "kettleful."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e24",
        "band": "easier",
        "text": "In the name 'specific heat capacity', what is the word "
                "SPECIFIC there to tell you?",
        "options": [
            {"text": "That the figure applies to one particular object and "
                     "to nothing else", "correct": False,
             "why": "The figure belongs to the material, so every sample of "
                    "that substance shares the same value."},
            {"text": "That it is an unusually precise measurement",
             "correct": False,
             "why": "Precision is not what the word means here; it means the "
                    "figure is quoted for each kilogram."},
            {"text": "That the figure is quoted for each kilogram of the "
                     "substance", "correct": True},
            {"text": "That it holds good at one temperature only",
             "correct": False,
             "why": "The figure is quoted per degree and is used right across "
                    "a range of temperatures, not at one alone."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e25",
        "band": "easier",
        "text": "A block of ice sits at 0 °C, slowly melting on a hotplate. "
                "While it melts, what happens to the thermometer reading?",
        "options": [
            {"text": "It rises steadily", "correct": False,
             "why": "While the ice is melting, the reading holds steady "
                    "rather than rising."},
            {"text": "It falls steadily", "correct": False,
             "why": "Energy is going in, not out, so nothing here is cooling "
                    "the beaker."},
            {"text": "It rises then falls", "correct": False,
             "why": "The reading does not move in either direction while "
                    "the ice is still melting."},
            {"text": "It stays at 0 °C", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e26",
        "band": "easier",
        "text": "Which pair correctly matches a unit to what it measures?",
        "options": [
            {"text": "Joules — internal energy", "correct": True},
            {"text": "Degrees Celsius — internal energy", "correct": False,
             "why": "Degrees Celsius measures temperature, not internal "
                    "energy."},
            {"text": "Joules — temperature", "correct": False,
             "why": "Joules measure energy; temperature is measured in "
                    "degrees."},
            {"text": "Kilograms — temperature", "correct": False,
             "why": "Kilograms measure mass, and temperature has its own "
                    "separate unit."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e27",
        "band": "easier",
        "text": "A brick at 60 °C is placed in a cold room. Which way does "
                "energy travel, and when does it stop?",
        "options": [
            {"text": "From the room into the brick, until the brick is at "
                     "room temperature", "correct": False,
             "why": "The brick is hotter than the room, so energy leaves the "
                    "brick rather than entering it."},
            {"text": "From the brick into the room, until both are at the "
                     "same temperature", "correct": True},
            {"text": "From the brick into the room, forever, without ever "
                     "stopping", "correct": False,
             "why": "The flow stops once the two temperatures become equal; "
                    "it does not continue indefinitely."},
            {"text": "Both ways at once, with no overall change",
             "correct": False,
             "why": "There is a clear net direction here, from the hotter "
                    "brick to the colder room."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e28",
        "band": "easier",
        "text": "Two identical mugs of tea are made, one with twice as much "
                "water as the other, both at the same temperature. Which one "
                "took more energy to heat up from cold?",
        "options": [
            {"text": "The smaller one", "correct": False,
             "why": "A smaller amount of water needs less energy to reach "
                    "the same temperature, not more."},
            {"text": "Neither — both took the same energy", "correct": False,
             "why": "Twice the water needs twice the energy for the same "
                    "temperature rise."},
            {"text": "The bigger one", "correct": True},
            {"text": "It cannot be told without knowing the room "
                     "temperature", "correct": False,
             "why": "The room's temperature does not change which mug "
                    "needed more energy to reach the same final temperature "
                    "from cold."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e29",
        "band": "easier",
        "text": "Which of these correctly separates temperature from internal "
                "energy?",
        "options": [
            {"text": "Temperature is measured in joules; internal energy in "
                     "degrees", "correct": False,
             "why": "This is the two units swapped round the wrong way."},
            {"text": "They are two names for exactly the same quantity",
             "correct": False,
             "why": "They are different quantities with different units; an "
                    "object can be hot and still hold little internal "
                    "energy."},
            {"text": "Temperature depends on mass; internal energy does not",
             "correct": False,
             "why": "It is the other way round — internal energy depends on "
                    "mass, and temperature does not."},
            {"text": "Temperature is an average per particle; internal "
                     "energy is a total", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-e30",
        "band": "easier",
        "text": "A spark and a bathful of water can both be described with a "
                "temperature. Which of them can also be usefully described "
                "with an internal energy?",
        "options": [
            {"text": "Both of them", "correct": True},
            {"text": "Only the spark", "correct": False,
             "why": "Internal energy can be found for anything with "
                    "particles and a temperature, including the bath."},
            {"text": "Only the bath", "correct": False,
             "why": "The spark also has particles with kinetic energy, "
                    "however few of them there are."},
            {"text": "Neither of them", "correct": False,
             "why": "Both a spark and a bath of water are made of particles, "
                    "and both have an internal energy, however different the "
                    "two amounts are."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p11-03-s14",
        "band": "standard",
        "text": "Copper has a specific heat capacity of about 390 J/kg°C. "
                "How much energy is needed to warm 2 kg of copper by 1 °C?",
        "options": [
            {"text": "195 J", "correct": False,
             "why": "That divides the specific heat capacity by the mass "
                    "instead of multiplying."},
            {"text": "780 J", "correct": True},
            {"text": "392 J", "correct": False,
             "why": "That adds the mass onto the specific heat capacity "
                    "instead of multiplying the two."},
            {"text": "1560 J", "correct": False,
             "why": "That treats the mass as 4 kg rather than the 2 kg "
                    "given."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s15",
        "band": "standard",
        "text": "Which needs MORE energy: warming 1 kg of water by 1 °C "
                "(4200 J/kg°C), or warming 1 kg of aluminium by 10 °C "
                "(900 J/kg°C)?",
        "options": [
            {"text": "Water, since 4200 is the bigger number", "correct": False,
             "why": "The specific heat capacity alone is not the answer; the "
                    "temperature rise matters too."},
            {"text": "Neither — they need exactly the same energy",
             "correct": False,
             "why": "900 × 10 and 4200 × 1 are not equal; one comes out "
                    "well above the other."},
            {"text": "Aluminium, since 900 × 10 beats 4200 × 1", "correct": True},
            {"text": "It cannot be told from the numbers given",
             "correct": False,
             "why": "It can — both energies can be worked out directly from "
                    "the figures given."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s16",
        "band": "standard",
        "text": "A 500 g block of lead (specific heat capacity about "
                "130 J/kg°C) is warmed from 20 °C to 25 °C. How much energy "
                "went in?",
        "options": [
            {"text": "65 J", "correct": False,
             "why": "That leaves out the temperature rise, using only the "
                    "mass and the specific heat capacity."},
            {"text": "650 J", "correct": False,
             "why": "That leaves out the mass, using only the specific heat "
                    "capacity and the temperature rise."},
            {"text": "162.5 J", "correct": False,
             "why": "That is half of the correct value; the mass should be "
                    "used as 0.5 kg, not halved again."},
            {"text": "325 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s17",
        "band": "standard",
        "text": "Two identical bricks are warmed from 20 °C to 60 °C. Brick A "
                "is heated over 10 minutes; brick B over 30 minutes. Compare "
                "the FINAL internal energy of the two bricks.",
        "options": [
            {"text": "They end up the same, since both reach the same "
                     "temperature and mass", "correct": True},
            {"text": "Brick A ends up higher, since it was heated faster",
             "correct": False,
             "why": "How quickly the energy arrived does not change how much "
                    "internal energy the finished brick holds."},
            {"text": "Brick B ends up higher, since it took longer to "
                     "absorb the energy", "correct": False,
             "why": "Taking longer does not add any extra energy; both "
                    "bricks finish at the same temperature and mass."},
            {"text": "It cannot be compared without knowing the exact "
                     "heaters used", "correct": False,
             "why": "The heaters used do not matter here; the final "
                    "temperature and mass are what decide the final internal "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s18",
        "band": "standard",
        "text": "A 1 kg block of water and a 1 kg block of aluminium both "
                "start at 20 °C and are given exactly 9000 J each. Which "
                "ends up hotter, given water needs 4200 J/kg°C and aluminium "
                "needs 900 J/kg°C?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "Water's bigger specific heat capacity means the same "
                    "energy raises its temperature LESS, not more."},
            {"text": "Aluminium", "correct": True},
            {"text": "They end up at the same temperature", "correct": False,
             "why": "Their specific heat capacities are very different, so "
                    "the same energy raises them by different amounts."},
            {"text": "It cannot be told without knowing their masses more "
                     "precisely", "correct": False,
             "why": "Both masses are already given as 1 kg each, which is "
                    "enough to compare the two."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s19",
        "band": "standard",
        "text": "A storage heater holds 200 kg of brick, which needs far less "
                "energy per kilogram per degree than water does. How does "
                "its stored energy compare with a 200 kg tank of water "
                "heated over the same temperature range?",
        "options": [
            {"text": "The brick stores far more energy", "correct": False,
             "why": "A lower specific heat capacity means LESS energy is "
                    "stored for the same temperature rise, not more."},
            {"text": "They store exactly the same energy", "correct": False,
             "why": "Different specific heat capacities, at the same mass "
                    "and temperature rise, give different stored energies."},
            {"text": "The water stores far more energy", "correct": True},
            {"text": "Neither stores any energy at all", "correct": False,
             "why": "Both materials store real energy once warmed; the "
                    "question is only about which stores more."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s20",
        "band": "standard",
        "text": "A 2 kg lump of aluminium (900 J/kg°C) and a 2 kg lump of "
                "copper (390 J/kg°C) are both given 3600 J from cold. Which "
                "one warms up more?",
        "options": [
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium's bigger specific heat capacity means the "
                    "same energy warms it up LESS, not more."},
            {"text": "Neither — they warm by the same amount",
             "correct": False,
             "why": "Their specific heat capacities are different, so the "
                    "same energy gives them different temperature rises."},
            {"text": "It cannot be told without knowing their starting "
                     "temperature", "correct": False,
             "why": "The starting temperature does not change which one "
                    "warms up MORE for the same energy."},
            {"text": "Copper", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s21",
        "band": "standard",
        "text": "A car's cooling system is refilled with a liquid whose "
                "specific heat capacity is half that of water. To carry away "
                "the same energy over the same temperature rise, what has to "
                "change?",
        "options": [
            {"text": "Twice the mass of liquid has to circulate",
             "correct": True},
            {"text": "Half the mass of liquid has to circulate",
             "correct": False,
             "why": "A smaller specific heat capacity carries less energy per "
                    "kilogram, so more liquid is needed, not less."},
            {"text": "Nothing has to change, since both are liquids",
             "correct": False,
             "why": "Being liquid is not the point; the two store very "
                    "different amounts of energy per kilogram per degree."},
            {"text": "The engine has to be run at twice the temperature",
             "correct": False,
             "why": "The temperature rise is fixed by the question; it is the "
                    "amount of liquid that has to change."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s22",
        "band": "standard",
        "text": "A 1 kg block of ice at 0 °C and a 1 kg block of water at "
                "0 °C sit side by side. Do they hold the same internal "
                "energy?",
        "options": [
            {"text": "Yes, since both read 0 °C on a thermometer",
             "correct": False,
             "why": "Matching thermometer readings only mean the average "
                    "energy per particle matches, not the total."},
            {"text": "No — melting the ice needs extra energy that the "
                     "water has already received", "correct": True},
            {"text": "No — the ice has more internal energy than the "
                     "water", "correct": False,
             "why": "It is the other way round: the water has already been "
                    "given the extra energy needed to melt the ice."},
            {"text": "Yes, since both are made of the same substance in the "
                     "same amount", "correct": False,
             "why": "Being the same substance and amount is not enough; "
                    "melting the ice takes extra energy the water already "
                    "holds."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s23",
        "band": "standard",
        "text": "A brick at 80 °C and an identical brick at 40 °C are pushed "
                "together. Which way does energy travel, and does the final "
                "temperature end up exactly halfway?",
        "options": [
            {"text": "From the cooler brick to the hotter one, because energy "
                     "flows towards whichever object is already carrying more "
                     "of it, ending up halfway at 60 °C", "correct": False,
             "why": "Energy never travels from a cooler object into a "
                    "hotter one on its own."},
            {"text": "From the hotter brick to the cooler one; but ending "
                     "above 60 °C", "correct": False,
             "why": "Since the two bricks are identical, the final "
                    "temperature lands exactly halfway, not above it."},
            {"text": "From the hotter brick to the cooler one; ending "
                     "exactly halfway at 60 °C, since the two bricks are "
                     "identical", "correct": True},
            {"text": "Both ways at once, with neither brick's temperature "
                     "changing", "correct": False,
             "why": "Both temperatures do change here, moving together "
                    "towards the same final value."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s24",
        "band": "standard",
        "text": "A 3 kg block of aluminium (900 J/kg°C) is warmed by 8 °C. "
                "How much energy was needed?",
        "options": [
            {"text": "2700 J", "correct": False,
             "why": "That leaves out the temperature rise from the "
                    "calculation."},
            {"text": "7200 J", "correct": False,
             "why": "That leaves out the mass from the calculation."},
            {"text": "10800 J", "correct": False,
             "why": "That is half of the correct value."},
            {"text": "21600 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s25",
        "band": "standard",
        "text": "A kettle uses 1 kg of water and needs about 336 000 J to "
                "heat it from 20 °C to 100 °C, a rise of 80 °C. Roughly how "
                "much energy would the SAME rise need for 1 kg of aluminium, "
                "given aluminium needs about 900 J/kg°C against water's "
                "4200?",
        "options": [
            {"text": "About 72 000 J — far less than water needed",
             "correct": True},
            {"text": "About 336 000 J — the same as water", "correct": False,
             "why": "Aluminium's far smaller specific heat capacity means "
                    "the same rise takes far less energy, not the same."},
            {"text": "About 672 000 J — twice what water needed",
             "correct": False,
             "why": "Aluminium's smaller specific heat capacity means LESS "
                    "energy is needed for the same rise, not more."},
            {"text": "About 33 600 J — a hundredth of what water needed",
             "correct": False,
             "why": "900 J/kg°C over 80 °C comes out to about 72 000 J, not "
                    "a hundredth of water's figure."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s26",
        "band": "standard",
        "text": "A thermos flask is designed to slow down heat loss from hot "
                "coffee. Which property of the coffee itself, not the "
                "flask, means it holds a great deal of energy even as it "
                "cools?",
        "options": [
            {"text": "Its high density", "correct": False,
             "why": "Density is not what decides how much energy a liquid "
                    "stores per degree."},
            {"text": "Water's high specific heat capacity", "correct": True},
            {"text": "Its dark colour", "correct": False,
             "why": "Colour affects how visibly it radiates energy away, not "
                    "how much it stores in the first place."},
            {"text": "Its ability to dissolve sugar", "correct": False,
             "why": "Dissolving sugar has no bearing on how much energy the "
                    "coffee itself can store."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s27",
        "band": "standard",
        "text": "A 4 kg block of lead (130 J/kg°C) and a 1 kg block of water "
                "(4200 J/kg°C) both receive 2600 J. Which one shows the "
                "bigger temperature rise?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "Water's far bigger specific heat capacity gives it the "
                    "SMALLER rise for the same energy, not the bigger one."},
            {"text": "Neither — they rise by the same amount",
             "correct": False,
             "why": "Their specific heat capacities and masses are quite "
                    "different, so the temperature rises differ too."},
            {"text": "Lead", "correct": True},
            {"text": "It cannot be told without knowing their starting "
                     "temperatures", "correct": False,
             "why": "The starting temperature does not change which one "
                    "rises MORE for the same energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s28",
        "band": "standard",
        "text": "Why does a swimming pool cool down much more slowly "
                "overnight than a shallow puddle on a patio?",
        "options": [
            {"text": "The pool is deeper, so cold cannot reach the bottom",
             "correct": False,
             "why": "Cold is not a substance that travels; what matters is "
                    "how much internal energy each holds."},
            {"text": "The patio absorbs energy from the puddle",
             "correct": False,
             "why": "The puddle loses energy to the cold night air, not to "
                    "the patio underneath it."},
            {"text": "The puddle has a lower specific heat capacity than the "
                     "pool, because a smaller amount of a substance stores "
                     "less energy per kilogram", "correct": False,
             "why": "Both are water, so they share exactly the same "
                    "specific heat capacity."},
            {"text": "The pool holds vastly more water, and so vastly more "
                     "internal energy to lose", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s29",
        "band": "standard",
        "text": "A 0.2 kg block of copper (390 J/kg°C) cools from 100 °C to "
                "20 °C. How much energy left the block?",
        "options": [
            {"text": "6240 J", "correct": True},
            {"text": "3120 J", "correct": False,
             "why": "That is half of the correct value."},
            {"text": "624 J", "correct": False,
             "why": "That is a tenth of the correct value."},
            {"text": "62400 J", "correct": False,
             "why": "That is ten times too big for the correct value."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-s30",
        "band": "standard",
        "text": "A designer needs a strip whose temperature climbs a long way "
                "from only a modest amount of energy, so that it warms up "
                "quickly as a warning indicator. Which is the better choice: "
                "a material at 130 J/kg°C or one at 900 J/kg°C?",
        "options": [
            {"text": "The one at 900 J/kg°C, since a bigger specific heat "
                     "capacity drives the temperature up faster for the same "
                     "energy put in", "correct": False,
             "why": "A bigger specific heat capacity needs MORE energy for "
                    "the same rise, the opposite of what is wanted here."},
            {"text": "The one at 130 J/kg°C, since less energy is needed "
                     "for the same temperature rise", "correct": True},
            {"text": "Neither — the specific heat capacity makes no "
                     "difference here", "correct": False,
             "why": "It makes exactly the difference being asked about: how "
                    "much energy is needed for a given temperature rise."},
            {"text": "It cannot be judged without knowing the exact mass "
                     "used", "correct": False,
             "why": "Whatever the mass, the smaller specific heat capacity "
                    "always needs less energy per degree of rise."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p11-03-h14",
        "band": "harder",
        "text": "A 1.5 kg block of aluminium (900 J/kg°C) is warmed from "
                "15 °C using 54 000 J. What is its final temperature?",
        "options": [
            {"text": "40 °C", "correct": False,
             "why": "That is the temperature RISE; the starting 15 °C still "
                    "needs to be added on."},
            {"text": "15 °C", "correct": False,
             "why": "That ignores the energy supplied entirely; the "
                    "temperature must have risen."},
            {"text": "55 °C", "correct": True},
            {"text": "95 °C", "correct": False,
             "why": "That doubles the temperature rise before adding the "
                    "starting value."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h15",
        "band": "harder",
        "text": "Two blocks of the same aluminium, masses 1 kg and 3 kg, are "
                "both warmed from 20 °C to 40 °C. Compare the energy needed "
                "for each.",
        "options": [
            {"text": "Equal energy, since the temperature rise is the same "
                     "for both", "correct": False,
             "why": "The temperature rise is the same, but three times the "
                    "mass still needs three times the energy."},
            {"text": "The 1 kg block needs three times as much",
             "correct": False,
             "why": "It is the other way round: the bigger mass needs more "
                    "energy, not less."},
            {"text": "Both need the same energy per kilogram, but the "
                     "totals are still equal", "correct": False,
             "why": "Needing the same energy per kilogram is exactly why "
                    "the TOTALS differ, since the masses differ."},
            {"text": "The 3 kg block needs three times as much energy",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h16",
        "band": "harder",
        "text": "A 2 kg lump of an unknown metal needs 1800 J to warm by "
                "10 °C. What is its specific heat capacity?",
        "options": [
            {"text": "90 J/kg°C", "correct": True},
            {"text": "180 J/kg°C", "correct": False,
             "why": "That leaves out dividing by the mass."},
            {"text": "900 J/kg°C", "correct": False,
             "why": "That leaves out dividing by the temperature rise."},
            {"text": "9 J/kg°C", "correct": False,
             "why": "That divides by the temperature rise twice over."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h17",
        "band": "harder",
        "text": "A thermal engineer wants a material that stores the MOST "
                "energy for the smallest rise in temperature, for a fixed "
                "mass. Should they pick a HIGH or a LOW specific heat "
                "capacity?",
        "options": [
            {"text": "Low, since less energy is then needed overall",
             "correct": False,
             "why": "A low specific heat capacity stores LESS energy for a "
                    "given rise, not more."},
            {"text": "High, since more energy is absorbed for each degree "
                     "it rises", "correct": True},
            {"text": "It makes no difference to how much is stored",
             "correct": False,
             "why": "It makes exactly the difference; specific heat capacity "
                    "is precisely the energy stored per degree."},
            {"text": "Neither — mass is the only thing that matters here",
             "correct": False,
             "why": "Mass is fixed in this question; the specific heat "
                    "capacity is what is being chosen."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h18",
        "band": "harder",
        "text": "A 500 g sample of an unknown liquid absorbs 40 000 J and "
                "rises from 20 °C to 60 °C. Is this liquid more likely to be "
                "water (4200 J/kg°C) or an oil (about 2000 J/kg°C)?",
        "options": [
            {"text": "Water, since 4200 is closer to a round number",
             "correct": False,
             "why": "How round a number looks has no bearing on which "
                    "specific heat capacity the calculation actually gives."},
            {"text": "Neither value matches at all", "correct": False,
             "why": "The calculated value does match one of the two values "
                    "closely."},
            {"text": "Oil, since the calculated value of 2000 J/kg°C "
                     "matches it closely", "correct": True},
            {"text": "Water, since liquids always match water's specific "
                     "heat capacity", "correct": False,
             "why": "Different liquids have different specific heat "
                    "capacities; oil's is roughly half of water's."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h19",
        "band": "harder",
        "text": "A 1 kg block of ice at 0 °C takes in energy without "
                "changing temperature, then becomes water at 0 °C, which "
                "then needs 4200 J to rise by 1 °C. What does this show "
                "about the melting process itself?",
        "options": [
            {"text": "It needs no energy of its own compared with warming the "
                     "liquid afterwards, because the particles only begin "
                     "taking energy in once the thermometer starts to climb",
             "correct": False,
             "why": "Melting genuinely needs a substantial amount of energy "
                    "of its own, taken in while the temperature holds "
                    "still."},
            {"text": "It happens at a lower temperature than 0 °C",
             "correct": False,
             "why": "The melting happens exactly at 0 °C, which is the "
                    "reading the thermometer holds throughout."},
            {"text": "It only happens once all the surrounding water has "
                     "warmed up", "correct": False,
             "why": "The melting happens first, while the temperature is "
                    "still at 0 °C, before any warming of the liquid can "
                    "begin."},
            {"text": "It needs its own separate store of energy, on top of "
                     "the energy needed to warm the resulting water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h20",
        "band": "harder",
        "text": "A 250 g mug of tea at 90 °C is placed in a room at 20 °C. "
                "Which of these is TRUE as the tea cools towards room "
                "temperature?",
        "options": [
            {"text": "The tea's internal energy falls as the room's rises, "
                     "until both stop changing", "correct": True},
            {"text": "The room's temperature falls as the tea's rises",
             "correct": False,
             "why": "The flow of energy runs the opposite way: from the "
                    "hotter tea into the cooler room."},
            {"text": "Both temperatures rise together until they match",
             "correct": False,
             "why": "The tea's temperature falls rather than rises as it "
                    "cools towards the room."},
            {"text": "The tea keeps losing energy forever, even after "
                     "reaching room temperature", "correct": False,
             "why": "The net flow of energy stops once the tea and the room "
                    "reach the same temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h21",
        "band": "harder",
        "text": "A 2 kg block of copper (390 J/kg°C) and a 1 kg block of "
                "aluminium (900 J/kg°C) are both warmed by 10 °C. Which "
                "needed more energy?",
        "options": [
            {"text": "Copper, since it has the bigger mass", "correct": False,
             "why": "A bigger mass alone does not settle it; the actual "
                    "figures give aluminium the larger total."},
            {"text": "Aluminium, since 9000 J beats copper's 7800 J",
             "correct": True},
            {"text": "Neither — they needed exactly the same energy",
             "correct": False,
             "why": "The two totals worked out from the figures are not "
                    "equal."},
            {"text": "It cannot be told without knowing their starting "
                     "temperatures", "correct": False,
             "why": "The starting temperature does not change which one "
                    "needed MORE energy for the same rise."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h22",
        "band": "harder",
        "text": "A storage heater's bricks and an equal mass of water both "
                "start at 20 °C. Which one reaches a higher final "
                "temperature after receiving the same amount of energy?",
        "options": [
            {"text": "Water, since it has the higher specific heat "
                     "capacity", "correct": False,
             "why": "A higher specific heat capacity means a SMALLER "
                    "temperature rise for the same energy, not a bigger "
                    "one."},
            {"text": "Neither — the final temperatures must be identical",
             "correct": False,
             "why": "Their specific heat capacities are different, so the "
                    "same energy gives them different final temperatures."},
            {"text": "The bricks, since a lower specific heat capacity "
                     "means a bigger temperature rise for the same energy",
             "correct": True},
            {"text": "It cannot be told without knowing the exact masses used, "
                     "since a temperature rise depends on the mass before it "
                     "depends on anything else", "correct": False,
             "why": "The masses are already stated to be equal, which is "
                    "enough to compare the two — and the specific heat "
                    "capacity matters quite as much as the mass does."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h23",
        "band": "harder",
        "text": "Why might a desert have very hot days and very cold nights, "
                "while a nearby coastal region stays milder both day and "
                "night?",
        "options": [
            {"text": "Sand contains more moisture than seawater, and "
                     "moisture absorbs energy", "correct": False,
             "why": "Dry sand contains far LESS moisture than seawater, not "
                    "more."},
            {"text": "The desert is further from the equator",
             "correct": False,
             "why": "Distance from the equator is not what this contrast is "
                    "about; deserts and coasts occur at similar latitudes."},
            {"text": "Coastal air is thinner and holds less energy",
             "correct": False,
             "why": "The key difference is the SEA's stored energy, not the "
                    "thinness of the air above it."},
            {"text": "Sand has a low specific heat capacity, so it heats "
                     "and cools quickly, unlike the sea", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h24",
        "band": "harder",
        "text": "A 3 kg lump of an unknown solid absorbs 7020 J and its "
                "temperature rises by 6 °C. Which material's specific heat "
                "capacity does this match: copper (390 J/kg°C) or lead "
                "(130 J/kg°C)?",
        "options": [
            {"text": "Copper, since the calculated value of 390 J/kg°C "
                     "matches it exactly", "correct": True},
            {"text": "Lead, since 130 is a smaller, more believable number",
             "correct": False,
             "why": "How believable a number looks is not the test; the "
                    "calculated value itself is what has to match."},
            {"text": "Neither — the value calculated does not match either "
                     "metal", "correct": False,
             "why": "The calculated value matches one of the two metals "
                    "exactly."},
            {"text": "Both equally, since the value sits exactly between "
                     "them", "correct": False,
             "why": "The calculated value matches one metal exactly rather "
                    "than sitting between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h25",
        "band": "harder",
        "text": "A 1 kg block of lead (130 J/kg°C) and a 1 kg block of "
                "copper (390 J/kg°C) are both given exactly 1300 J. Which "
                "ends up with the bigger temperature rise?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper's bigger specific heat capacity gives it the "
                    "SMALLER rise for the same energy, not the bigger one."},
            {"text": "Lead", "correct": True},
            {"text": "Neither — they rise by the same amount",
             "correct": False,
             "why": "Their specific heat capacities are different, so equal "
                    "energy gives them different rises."},
            {"text": "It cannot be told without knowing their starting "
                     "temperatures", "correct": False,
             "why": "The starting temperature does not change which one "
                    "rises MORE for the same energy."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h26",
        "band": "harder",
        "text": "Two identical mugs of water are warmed from 20 °C to "
                "80 °C, one over 2 minutes and one over 20 minutes, using "
                "the same total energy in each case. Compare the FINAL "
                "internal energy of the two.",
        "options": [
            {"text": "The 2-minute mug ends up with more internal energy",
             "correct": False,
             "why": "How quickly the energy arrived does not add anything "
                    "extra to the final total."},
            {"text": "The 20-minute mug ends up with more internal energy",
             "correct": False,
             "why": "Taking longer does not add any extra energy beyond "
                    "what was actually supplied."},
            {"text": "They end up with the same internal energy",
             "correct": True},
            {"text": "Neither has gained any internal energy at all",
             "correct": False,
             "why": "Both mugs have clearly gained energy, shown by their "
                    "rise from 20 °C to 80 °C."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h27",
        "band": "harder",
        "text": "A 4 kg block of water and a 4 kg block of lead both cool "
                "from 60 °C to 20 °C, releasing energy to a room. Which one "
                "releases MORE energy, given water's specific heat capacity "
                "is far higher than lead's?",
        "options": [
            {"text": "Lead", "correct": False,
             "why": "Lead's much smaller specific heat capacity means it "
                    "releases far LESS energy for the same fall, not more."},
            {"text": "Neither — they release the same energy",
             "correct": False,
             "why": "Their very different specific heat capacities give "
                    "very different amounts of energy released."},
            {"text": "It cannot be told without knowing the room's "
                     "temperature", "correct": False,
             "why": "The room's temperature does not change which block "
                    "released MORE energy for the same fall."},
            {"text": "Water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h28",
        "band": "harder",
        "text": "A 1 kg block of an unknown metal absorbs 45 000 J and warms "
                "from 25 °C to 75 °C. What is its specific heat capacity, "
                "and which of these two metals does it match: aluminium "
                "(900 J/kg°C) or copper (390 J/kg°C)?",
        "options": [
            {"text": "900 J/kg°C, matching aluminium", "correct": True},
            {"text": "450 J/kg°C, matching neither metal closely",
             "correct": False,
             "why": "That halves the correct value; the temperature rise "
                    "used should be 50 °C, not 100 °C."},
            {"text": "390 J/kg°C, matching copper", "correct": False,
             "why": "The calculated value matches aluminium far more "
                    "closely than it matches copper."},
            {"text": "9000 J/kg°C, ten times too big for either metal",
             "correct": False,
             "why": "That drops a power of ten from the temperature rise, "
                    "dividing by 5 °C rather than by 50 °C."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h29",
        "band": "harder",
        "text": "A brick at 60 °C and a much smaller pebble, also at 60 °C "
                "and made of the same material, are both left in a cold "
                "room. Which cools to room temperature FIRST?",
        "options": [
            {"text": "The brick, since it started with more internal "
                     "energy", "correct": False,
             "why": "Starting with MORE internal energy to lose is exactly "
                    "why the brick takes longer to finish cooling, not "
                    "less."},
            {"text": "The pebble, since it has far less internal energy to "
                     "lose", "correct": True},
            {"text": "Neither — both cool at exactly the same rate",
             "correct": False,
             "why": "The much smaller pebble has far less internal energy "
                    "to shed, so it reaches room temperature sooner."},
            {"text": "It cannot be told without knowing the room's "
                     "temperature", "correct": False,
             "why": "Whatever the room's temperature, the pebble still has "
                    "far less internal energy to lose than the brick."},
        ],
        "figure": None,
    },
    {
        "id": "p11-03-h30",
        "band": "harder",
        "text": "An engineer needs to know how much energy a 2 kg aluminium "
                "casting (900 J/kg°C) gives out as it cools in air from "
                "100 °C down to 60 °C. What figure should they use?",
        "options": [
            {"text": "1800 J", "correct": False,
             "why": "That leaves out the temperature fall from the "
                    "calculation."},
            {"text": "36 000 J", "correct": False,
             "why": "That is half of the correct value."},
            {"text": "72 000 J", "correct": True},
            {"text": "144 000 J", "correct": False,
             "why": "That is double the correct value."},
        ],
        "figure": None,
    },
]
