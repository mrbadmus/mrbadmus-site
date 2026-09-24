"""P1 lesson 04 — Heating and thermal equilibrium: twelve questions.

⊕ RUN 1's TWELVE WERE USED AS RAW MATERIAL, NOT ADOPTED (MRB-223).

Run 1's own provenance audit flags `e02` and `h01` as quoting the four
temperature pairs off a bench it invented — 80/20→50, 70/30→50, 45/15→30.
Design's `one-way-flow` bench carries three pairs and none of them is any of
those: hers are a drink at 22 °C with ice at −4 °C, a spoon at 90 °C in water
at 12 °C, and two blocks both at 30 °C. Both questions are dropped rather
than repaired, because repairing one means inventing a new number and the
whole point of the audit was that invented numbers are how this started.

The rest of the inherited set is sound on the science and largely aimed at
the right lesson, so more of it survives here than in `p1-02` or `p1-03`.

    CHANGED — five stems kept, option sets rewritten (5):
        e01  which holds more energy, spark or bath
        e03  what temperature actually measures
        s01  which way energy travels between two objects
        s03  cold is not a substance
        h02  the fridge with its door open

    NEW — her content had no question covering it (7):
        e02  thermal equilibrium as a STATE, not an ending
        e04  the particles do not change size — PART-03 re-confronted
        s02  the two blocks already at the same temperature
        s04  why a spark at 1500 °C does not hurt
        h01  the hot spoon that cools fast while the water barely warms
        h03  why "a bath has more heat in it" runs two quantities together
        h04  what stops the transfer — matching temperature, not running out

    DROPPED — invented data (2):  run 1's e02 and h01.
    DROPPED — `p1-05` material (3):  its conduction-feel questions, which
        belong with the touch test rather than here.

⚠️ Answer positions run 1,2,3,0 · 1,2,3,0 · 1,2,0,3 — three of each
index. The last pair breaks the cycle because h03's correct answer reads
naturally first; the COUNT is what MRB-278 measures, and it is 3/3/3/3.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures. ⊕ MRB-352 run 2: some questions now carry a
QUESTION figure from `figlib/catalogue_ks3.py` (the lesson page is untouched).
"""

# XU-1 (MRB-295/MRB-298, ruled 28 Aug 2026). The estate held four
# definitions of temperature and three were wrong. There is now one, and it
# is authored in ks3_data/quantities.py rather than retyped here.
from ..quantities import (TEMPERATURE_CRITERION, TEMPERATURE_OPTION,
                          TEMPERATURE_SENTENCE, TEMPERATURE_VOCAB)  # noqa: F401


UNIT = "P1"
LESSON = "heating-and-thermal-equilibrium"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-04-e01",
        "band": "easier",
        "text": "A spark from a sparkler is at 1500 °C. A bath is at 40 °C. "
                "Which holds more energy in its thermal store?",
        "options": [
            {"text": "The spark, because it is very much hotter than the "
                     "bath is",
             "correct": False,
             "why": "Hotter means faster particles, not more of them. The "
                    "spark is a handful of particles."},
            {"text": "The bath, because it has vastly more particles than "
                     "the spark",
             "correct": True},
            {"text": "They hold the same, because energy depends only on the "
                     "temperature",
             "correct": False,
             "why": "Energy depends on temperature AND on how much there is. "
                    "That is the whole lesson."},
            {"text": "The spark, because all of its energy is concentrated "
                     "in one place",
             "correct": False,
             "why": "Concentrated is not the same as large. There is very "
                    "little there to concentrate."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e02",
        "band": "easier",
        "text": "Two metal blocks are both at 30 °C and are touching. What "
                "is happening between them?",
        "options": [
            {"text": "Energy is flowing from the first block into the second "
                     "one steadily",
             "correct": False,
             "why": "There is no temperature difference, so there is nothing "
                    "to drive a net flow either way."},
            {"text": "Nothing at all is happening, because both blocks are "
                     "completely inert",
             "correct": False,
             "why": "Their particles are still colliding and still "
                    "exchanging energy — the two flows are simply equal."},
            {"text": "There is no NET flow — they are in thermal equilibrium",
             "correct": True},
            {"text": "Energy is flowing from whichever block is physically "
                     "the larger one",
             "correct": False,
             "why": "Size does not set the direction. Only a temperature "
                    "difference does, and there is none."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e03",
        "band": "easier",
        "text": "What does temperature measure?",
        "options": [
            {"text": "The total amount of energy held in a substance's "
                     "thermal store",
             "correct": False,
             "why": "That is the store itself. Temperature ignores how much "
                    "of the substance there is."},
            {"text": "How much heat a substance contains at the moment you "
                     "measure it",
             "correct": False,
             "why": "There is no substance called heat to contain. "
                    "Temperature is about the movement energy of one "
                    "particle, on average."},
            {"text": "How quickly a substance will warm something else that "
                     "it touches",
             "correct": False,
             "why": "That is a rate, and it depends on the material as well. "
                    "Temperature is simpler than that."},
            # XU-1 — this option used to read "The average speed of the
            # particles in a substance" and was marked CORRECT, so a child
            # who knew the right answer was marked down. Two gases at the
            # same temperature have the same average kinetic energy and
            # different average speeds; speed is not the quantity.
            {"text": TEMPERATURE_OPTION, "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e04",
        "band": "easier",
        "text": "When a metal block is heated, what happens to its "
                "particles?",
        "options": [
            {"text": "They vibrate faster, and stay exactly the same size",
             "correct": True},
            {"text": "They get bigger, which is why the block expands when "
                     "it is heated",
             "correct": False,
             "why": "The block expands because the particles move further "
                    "apart, not because any particle grows."},
            {"text": "They melt slightly and then re-form when the block "
                     "cools again",
             "correct": False,
             "why": "Nothing melts below the melting point, and a particle "
                    "does not melt at all."},
            {"text": "They gain extra particles from the flame that is doing "
                     "the heating",
             "correct": False,
             "why": "Heating adds energy, never matter. The same particles "
                    "are there throughout."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-04-s01",
        "band": "standard",
        "text": "A hot spoon is put into cold water. Which way does energy "
                "travel, and when does it stop?",
        "options": [
            {"text": "Both ways at once, stopping when the spoon has given "
                     "out all it has",
             "correct": False,
             "why": "There is one NET flow, and it stops at matching "
                    "temperatures rather than at empty."},
            {"text": "Spoon to water, stopping when they reach the same "
                     "temperature",
             "correct": True},
            {"text": "Water to spoon, stopping when the water has cooled "
                     "right down to zero",
             "correct": False,
             "why": "Energy travels from hotter to colder, so it leaves the "
                    "spoon. The direction is the wrong way round."},
            {"text": "Spoon to water, stopping only when the spoon has run "
                     "out of heat entirely",
             "correct": False,
             "why": "Right direction, wrong ending. It stops when the two "
                    "match, with plenty left in both."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s02",
        "band": "standard",
        "text": "Ice is dropped into a warm drink. What is the correct "
                "description of what happens?",
        "options": [
            {"text": "Cold moves out of the ice and spreads through the "
                     "whole of the drink",
             "correct": False,
             "why": "There is no such thing as cold to move. Only energy "
                    "travels, and it goes the other way."},
            {"text": "The cold and the warmth swap places until the two have "
                     "evened out",
             "correct": False,
             "why": "Only one quantity is moving. Describing two makes the "
                    "account twice as complicated and wrong."},
            {"text": "Energy leaves the drink and enters the ice, so the "
                     "drink is left with less",
             "correct": True},
            {"text": "The ice absorbs the drink's temperature until both "
                     "readings are the same",
             "correct": False,
             "why": "Temperature is not a thing that can be absorbed. What "
                    "moves is energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s03",
        "band": "standard",
        "text": "Why does a spark at 1500 °C landing on your hand do so "
                "little damage?",
        "options": [
            {"text": "Because it cools down before it has time to reach your "
                     "skin at all",
             "correct": False,
             "why": "It lands on you still glowing. The reason is how "
                    "little energy it holds, not timing."},
            {"text": "Because skin is a poor conductor and refuses to accept "
                     "energy that hot",
             "correct": False,
             "why": "Skin accepts it readily. There is simply almost none of "
                    "it to accept."},
            {"text": "Because your hand is already at a temperature close "
                     "enough to the spark's",
             "correct": False,
             "why": "The difference is enormous — about 1470 degrees. That "
                    "is not what saves you."},
            {"text": "Because it has so few particles that its thermal store "
                     "is tiny",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s04",
        "band": "standard",
        "text": "A hot spoon in cold water loses temperature fast while the "
                "water barely warms. Why?",
        "options": [
            {"text": "The spoon is small, so the same energy makes a much "
                     "bigger difference to it",
             "correct": True},
            {"text": "Metal loses temperature quickly whatever it is placed "
                     "into or next to",
             "correct": False,
             "why": "Its material affects the RATE, not how far its own "
                    "temperature falls for the energy it loses."},
            {"text": "The water is receiving only a small part of what the "
                     "spoon is giving out",
             "correct": False,
             "why": "The water receives all of it. It simply has far more "
                    "particles to share it among."},
            {"text": "Water is very difficult to heat because it is a liquid "
                     "rather than a solid",
             "correct": False,
             "why": "Being liquid is not the reason. The reason is how much "
                    "of it there is."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-04-h01",
        "band": "harder",
        "text": "A student leaves the fridge door open to cool the kitchen. "
                "What actually happens, and why?",
        "options": [
            {"text": "The kitchen cools slowly, because the fridge is "
                     "releasing the cold it has made",
             "correct": False,
             "why": "A fridge does not make cold. There is no such substance "
                    "for it to release."},
            {"text": "The kitchen gets warmer, because the fridge returns "
                     "that energy plus the motor's",
             "correct": True},
            {"text": "Nothing changes at all, because the energy taken out "
                     "is exactly the energy put back",
             "correct": False,
             "why": "Close, but the motor adds more on top, so the room ends "
                    "up warmer rather than level."},
            {"text": "The kitchen cools quickly, because the fridge is much "
                     "colder than the room is",
             "correct": False,
             "why": "The inside is colder, but the back is warmer, and the "
                    "motor makes the total positive."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h02",
        "band": "harder",
        "text": "A bath at 40 °C and a cup of tea at 80 °C. Which statement "
                "is correct?",
        "options": [
            {"text": "The bath is hotter, because it holds far more energy "
                     "than the cup does",
             "correct": False,
             "why": "Hotter means higher temperature, and the tea's is "
                    "higher. More energy is not hotter."},
            {"text": "The tea holds more energy, because its particles are "
                     "moving much faster",
             "correct": False,
             "why": "Faster particles, far fewer of them. The bath holds "
                    "vastly more energy in total."},
            {"text": "The tea is hotter, and the bath holds far more energy "
                     "in its thermal store",
             "correct": True},
            {"text": "The bath is hotter and holds more energy, since it is "
                     "very much larger",
             "correct": False,
             "why": "Larger, and holding more energy — but at a lower "
                    "temperature. Size does not make it hotter."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h03",
        "band": "harder",
        "text": "Put the tea from the last question into the bath. Which way "
                "does energy travel?",
        "options": [
            {"text": "From the tea to the bath, because temperature decides "
                     "the direction",
             "correct": True},
            {"text": "From the bath to the tea, because the bath holds far "
                     "more total energy",
             "correct": False,
             "why": "Total energy does not set the direction. If it did, a "
                    "spark could never heat a room."},
            {"text": "Neither way, because the two effects cancel each other "
                     "out exactly",
             "correct": False,
             "why": "Nothing cancels. There is a temperature difference, so "
                    "there is a flow."},
            {"text": "Both ways equally, because each one has more of a "
                     "different quantity",
             "correct": False,
             "why": "Only temperature difference drives the net flow, and it "
                    "runs one way only."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h04",
        "band": "harder",
        "text": "Two objects are left touching for a long time. What finally "
                "stops the transfer between them?",
        "options": [
            {"text": "The hotter one runs out of the energy it had to "
                     "give away to the colder one",
             "correct": False,
             "why": "It never runs out. Both objects still hold plenty when "
                    "the transfer stops."},
            {"text": "The colder one becomes completely full and can "
                     "accept no more energy at all",
             "correct": False,
             "why": "There is no upper limit to fill. A store is not a "
                    "container with a brim."},
            {"text": "The surrounding air removes the difference in "
                     "temperature between the two",
             "correct": False,
             "why": "The air affects both, but the transfer between them "
                    "stops for a reason of its own."},
            {"text": "They reach the same temperature, so there is no longer "
                     "a difference to drive it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-04-e05",
        "band": "easier",
        "text": "What is thermal equilibrium?",
        "options": [
            {"text": "When two objects reach the same temperature and the "
                     "net flow stops",
             "correct": True},
            {"text": "When two objects hold exactly the same amount of energy",
             "correct": False,
             "why": "They can hold very different amounts — a pool and a mug "
                    "reach it while holding wildly different energies."},
            {"text": "When one object has given away all of its energy",
             "correct": False,
             "why": "Nothing ever gives away all of it; the flow stops when "
                    "the temperatures match."},
            {"text": "When an object stops conducting energy altogether",
             "correct": False,
             "why": "Energy still passes both ways. What stops is any net "
                    "flow one way."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e06",
        "band": "easier",
        "text": "The energy in an object's thermal store depends on its "
                "temperature and on what else?",
        "options": [
            {"text": "Its colour", "correct": False,
             "why": "Colour affects how well it radiates, not how much its "
                    "thermal store holds."},
            {"text": "How many particles it has", "correct": True},
            {"text": "How long it has been standing there", "correct": False,
             "why": "Time changes the temperature by letting it cool; it is "
                    "not a second quantity in the store."},
            {"text": "How high above the ground it is", "correct": False,
             "why": "Height fills a gravitational store, which is a different "
                    "store altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e07",
        "band": "easier",
        "text": "Is cold a substance that travels from one object to "
                "another?",
        "options": [
            {"text": "Yes — cold moves out of ice and into a drink",
             "correct": False,
             "why": "Energy moves the other way: out of the drink and into "
                    "the ice. Nothing cold travels."},
            {"text": "Yes, but only when the two objects touch",
             "correct": False,
             "why": "Touching lets energy pass. It does not create a "
                    "substance called cold."},
            {"text": "No — cold is simply less energy, and only energy moves",
             "correct": True},
            {"text": "No — nothing moves at all between a cold object and a "
                     "warm one",
             "correct": False,
             "why": "Energy certainly moves, from the warmer one to the "
                    "colder one, until they match."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-04-s05",
        "band": "standard",
        "text": "A 1 kg block and a 4 kg block of the same metal are both at "
                "60 °C. Which statement is right?",
        "options": [
            {"text": "The 4 kg block is at a higher temperature because there "
                     "is more of it",
             "correct": False,
             "why": "Both were measured at 60 °C. Temperature does not depend "
                    "on how much there is."},
            {"text": "They hold the same energy, because they are at the same "
                     "temperature",
             "correct": False,
             "why": "Temperature is the average per particle; the 4 kg block "
                    "has four times as many particles."},
            {"text": "The 1 kg block holds more, because its particles are "
                     "more crowded",
             "correct": False,
             "why": "The same metal has the same crowding. What differs is "
                    "simply how much of it there is."},
            {"text": "Both are at 60 °C, but the 4 kg block holds more in its "
                     "thermal store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s06",
        "band": "standard",
        "text": "200 g of water at 80 °C is mixed with 800 g of water at "
                "30 °C. What can you say about the final temperature?",
        "options": [
            {"text": "It will be 40 °C, pulled down by the extra cool "
                     "water",
             "correct": True},
            {"text": "It will be 55 °C, halfway between the two",
             "correct": False,
             "why": "Halfway would need equal masses. The 800 g pulls the "
                    "result strongly towards 30 °C."},
            {"text": "It will be 110 °C, because the two temperatures add",
             "correct": False,
             "why": "Temperatures never add on mixing — the result always "
                    "lies between the two."},
            {"text": "It will be 30 °C, because cold always wins",
             "correct": False,
             "why": "The hot water raises it above 30 °C; nothing 'wins', the "
                    "two settle in between."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s07",
        "band": "standard",
        "text": "Why does a thermometer left in a drink eventually read the "
                "drink's temperature?",
        "options": [
            {"text": "Because glass always takes the temperature of whatever "
                     "it touches instantly",
             "correct": False,
             "why": "It is not instant — that is why you wait for the reading "
                    "to settle."},
            {"text": "Because the thermometer adds its own temperature to the "
                     "drink",
             "correct": False,
             "why": "It does change the drink very slightly, but the reading "
                    "settles because the two match."},
            {"text": "Because energy flows between them until they reach "
                     "thermal equilibrium",
             "correct": True},
            {"text": "Because the liquid inside the thermometer is the same "
                     "as the drink",
             "correct": False,
             "why": "The two liquids are quite different; what matters is the "
                    "temperature difference between them."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-04-h05",
        "band": "harder",
        "text": "A small cup of tea at 90 °C is poured into a heavy metal "
                "teapot at 20 °C. What happens to the two temperatures?",
        "options": [
            {"text": "The tea cools a lot and the pot warms a little, until "
                     "both match",
             "correct": True},
            {"text": "The pot warms to 90 °C, because that is the tea's "
                     "temperature",
             "correct": False,
             "why": "The pot has far more particles to warm, so the shared "
                    "temperature ends up near 20 °C."},
            {"text": "They meet at 55 °C, halfway between the two",
             "correct": False,
             "why": "Halfway would need the two to have equal thermal "
                    "capacities, and the pot is far heavier."},
            {"text": "Nothing happens until the tea is stirred",
             "correct": False,
             "why": "Stirring speeds it up but the flow begins the moment "
                    "they touch."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h06",
        "band": "harder",
        "text": "Why does a room stop getting colder once it has reached the "
                "temperature outside?",
        "options": [
            {"text": "Because the walls stop conducting energy once they are "
                     "cold",
             "correct": False,
             "why": "The walls conduct just as well as before. What has gone "
                    "is the temperature difference."},
            {"text": "Because the cold outside has all been used up",
             "correct": False,
             "why": "Cold is not a substance and cannot be used up; only "
                    "energy moves."},
            {"text": "Because there is no temperature difference left to "
                     "drive a net flow",
             "correct": True},
            {"text": "Because energy can only flow for a limited time",
             "correct": False,
             "why": "It flows for as long as a difference lasts, which can be "
                    "hours or days."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h07",
        "band": "harder",
        "text": "You can hold your hand in a 200 °C oven for a moment, but "
                "not in water at 100 °C. Explain.",
        "options": [
            {"text": "Water is at a higher temperature than the oven air, "
                     "despite what the numbers say",
             "correct": False,
             "why": "The numbers are the temperatures: 200 °C really is "
                    "hotter than 100 °C."},
            {"text": "Air has far fewer particles per litre, so it delivers "
                     "less energy",
             "correct": True},
            {"text": "Air is a gas, and gases cannot transfer energy at all",
             "correct": False,
             "why": "They can — it is how an oven cooks. They simply deliver "
                    "much less, much more slowly."},
            {"text": "Skin is a good conductor, so the oven's energy passes "
                     "straight through",
             "correct": False,
             "why": "Skin conducts poorly, and passing through would still "
                    "mean being burnt."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-04-e08",
        "band": "easier",
        "text": "Two objects at different temperatures are placed in "
                "contact. Which way does energy travel between them?",
        "options": [
            {"text": "From the hotter object to the colder one",
             "correct": True},
            {"text": "From the colder object to the hotter one",
             "correct": False,
             "why": "Energy never travels that way on its own — only "
                    "from hotter to colder."},
            {"text": "Both ways equally, so neither object changes "
                     "temperature",
             "correct": False,
             "why": "If nothing changed, the colder object would never "
                    "warm up — and it does."},
            {"text": "In whichever direction the larger object is",
             "correct": False,
             "why": "Size does not set the direction. Only which one is "
                    "hotter does."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e09",
        "band": "easier",
        "text": "A cup of coffee is left on a table until it reaches the "
                "temperature of the room. What is true about the energy "
                "transfer at that point?",
        "options": [
            {"text": "The coffee is still losing energy quickly, but the "
                     "room is not gaining any",
             "correct": False,
             "why": "Whatever the coffee loses, the room around it "
                    "gains — nothing simply vanishes."},
            {"text": "There is no longer a net flow of energy between "
                     "the coffee and the room",
             "correct": True},
            {"text": "The coffee has run out of energy completely",
             "correct": False,
             "why": "The coffee still holds plenty of energy in its "
                    "thermal store; it has simply stopped losing more of "
                    "it."},
            {"text": "Energy is now flowing from the room back into the "
                     "coffee only",
             "correct": False,
             "why": "With no temperature difference left, there is "
                    "nothing to drive a flow either way."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e10",
        "band": "easier",
        "text": "A metal spoon left standing in a freshly poured cup of "
                "hot tea eventually reaches the tea's own temperature. "
                "What has happened?",
        "options": [
            {"text": "The spoon has created extra energy of its own to "
                     "match the tea",
             "correct": False,
             "why": "A spoon creates nothing; every joule in it arrived "
                    "from the tea."},
            {"text": "The tea's temperature has dropped to absolute zero",
             "correct": False,
             "why": "The tea only falls to about room temperature, "
                    "nowhere near that."},
            {"text": "The spoon and the tea have reached thermal "
                     "equilibrium",
             "correct": True},
            {"text": "The spoon has stopped being able to hold any "
                     "energy",
             "correct": False,
             "why": "The spoon holds plenty of energy; it is simply no "
                    "longer gaining more."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e11",
        "band": "easier",
        "text": "A block of ice sits in a warm room. In which direction "
                "is energy actually moving?",
        "options": [
            {"text": "Cold is moving out of the ice and into the room",
             "correct": False,
             "why": "There is no substance called cold to move out of "
                    "anything."},
            {"text": "Energy moves back and forth in exactly equal "
                     "amounts",
             "correct": False,
             "why": "Equal amounts would mean no net change, yet the ice "
                    "melts."},
            {"text": "The ice blocks any movement, since it is a solid",
             "correct": False,
             "why": "Being a solid does not stop energy moving through "
                    "or into it."},
            {"text": "Energy is moving from the room into the ice",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e12",
        "band": "easier",
        "text": "A hot-air balloon's burner heats the air inside the "
                "balloon envelope. Which way is energy travelling?",
        "options": [
            {"text": "From the burner's flame into the air inside the "
                     "balloon",
             "correct": True},
            {"text": "From the air inside the balloon into the burner's "
                     "flame",
             "correct": False,
             "why": "Energy leaves the hotter flame; it does not flow "
                    "back into it."},
            {"text": "Equally in both directions, so the air inside "
                     "never warms",
             "correct": False,
             "why": "The air does warm up, which shows the flow is not "
                    "balanced both ways."},
            {"text": "From the cold sky outside into the balloon",
             "correct": False,
             "why": "The sky is colder than the balloon, so nothing "
                    "flows from it inward."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e13",
        "band": "easier",
        "text": "An ice lolly left in direct sunshine on a warm day "
                "eventually melts completely. What has happened to the "
                "energy involved?",
        "options": [
            {"text": "The lolly has destroyed some of its own coldness",
             "correct": False,
             "why": "There is no coldness to destroy; only energy has "
                    "entered the lolly."},
            {"text": "Energy from the sunshine and the warm air has "
                     "entered the lolly",
             "correct": True},
            {"text": "The lolly's own energy escaped into the ground "
                     "beneath it",
             "correct": False,
             "why": "The ground plays no special part; the surrounding "
                    "air and sunshine are the source."},
            {"text": "Nothing has transferred; the lolly simply changed "
                     "on its own",
             "correct": False,
             "why": "A change like this needs energy arriving from "
                    "somewhere; it does not happen unprompted."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e14",
        "band": "easier",
        "text": "A can of fizzy drink is put into a bowl of ice to cool "
                "it. Which statement is correct?",
        "options": [
            {"text": "The ice releases cold into the drink until the two "
                     "match",
             "correct": False,
             "why": "There is no cold to release; only energy leaves the "
                    "drink."},
            {"text": "The drink stays the same temperature because cans "
                     "are sealed",
             "correct": False,
             "why": "Being sealed does not stop energy passing through "
                    "the metal can."},
            {"text": "Energy passes from the drink into the ice until "
                     "they are at the same temperature",
             "correct": True},
            {"text": "The drink's temperature falls only once all the ice has melted, since ice must vanish before it can cool anything",
             "correct": False,
             "why": "The drink starts cooling immediately, well before "
                    "the ice has finished melting."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e15",
        "band": "easier",
        "text": "A greenhouse stays warmer inside than the garden outside "
                "on a sunny day. What does that tell you about the "
                "energy passing through the glass?",
        "options": [
            {"text": "None is passing through the glass at all",
             "correct": False,
             "why": "If none passed through, the inside could never be "
                    "warmer than the garden."},
            {"text": "It is passing from the cooler garden into the "
                     "warmer greenhouse",
             "correct": False,
             "why": "Energy does not travel from colder to hotter on "
                    "its own."},
            {"text": "The glass is creating fresh energy inside the "
                     "greenhouse",
             "correct": False,
             "why": "Glass creates no energy; it simply lets sunlight in "
                    "more easily than it lets warmth back out."},
            {"text": "More energy is arriving from outside than is "
                     "escaping back out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e16",
        "band": "easier",
        "text": "A student says a radiator “gives off heat” into a cold "
                "room. What is really being described?",
        "options": [
            {"text": "Energy passing from the radiator, which is "
                     "hotter, into the room, which is colder",
             "correct": True},
            {"text": "Heat, a substance stored inside the radiator, "
                     "leaking out into the air",
             "correct": False,
             "why": "There is no substance called heat stored anywhere; "
                    "only energy moves."},
            {"text": "The room's own coldness entering the radiator and cancelling its warmth",
             "correct": False,
             "why": "Coldness cannot enter anything; only energy leaves "
                    "the radiator."},
            {"text": "Energy passing equally in both directions until "
                     "nothing changes",
             "correct": False,
             "why": "If it passed equally both ways, the room would "
                    "never warm up, and it does."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e17",
        "band": "easier",
        "text": "A frozen chicken is left on the kitchen worktop to "
                "thaw. What is happening to its temperature?",
        "options": [
            {"text": "It stays the same until the chicken is completely "
                     "thawed",
             "correct": False,
             "why": "Its temperature rises steadily well before it is "
                    "fully thawed."},
            {"text": "It rises as energy moves from the warmer kitchen "
                     "into the colder chicken",
             "correct": True},
            {"text": "It falls further as the room's coldness spreads "
                     "into it",
             "correct": False,
             "why": "There is no coldness to spread; energy is entering "
                    "the chicken, not leaving it."},
            {"text": "It rises because the chicken makes its own warmth as it defrosts",
             "correct": False,
             "why": "A chicken makes no energy; everything it gains "
                    "comes from the kitchen around it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e18",
        "band": "easier",
        "text": "A hot iron is switched off and left to stand. "
                "Eventually it feels the same temperature as the room. "
                "What has happened to the flow of energy between the "
                "iron and the room?",
        "options": [
            {"text": "It has reversed, so energy now flows from the room "
                     "into the iron",
             "correct": False,
             "why": "There is no longer any net flow at all, in either "
                    "direction."},
            {"text": "It has grown stronger, because the iron is "
                     "releasing everything at once",
             "correct": False,
             "why": "The flow has stopped altogether, not sped up."},
            {"text": "It has stopped, because there is no longer a "
                     "temperature difference",
             "correct": True},
            {"text": "It cannot happen, because an iron stays hotter "
                     "than a room",
             "correct": False,
             "why": "Left long enough, any iron settles to the "
                    "temperature of the room around it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e19",
        "band": "easier",
        "text": "A student pours hot water at 80 °C and cold water at "
                "20 °C into the same jug. Could the mixture end up at "
                "85 °C?",
        "options": [
            {"text": "Yes, if the hot water was poured in first",
             "correct": False,
             "why": "The order of pouring makes no difference to where "
                    "the mixture settles."},
            {"text": "Yes, because the two temperatures add together",
             "correct": False,
             "why": "Temperatures do not add when liquids mix; the "
                    "result lies between the two."},
            {"text": "Only if the jug is well insulated",
             "correct": False,
             "why": "Insulation affects how fast heat is lost "
                    "afterwards, not where the mixture first settles."},
            {"text": "No — the result must lie somewhere between 20 °C "
                     "and 80 °C",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e20",
        "band": "easier",
        "text": "A pack of frozen peas at −18 °C is taken out of a "
                "freezer and put into a cool box that is at −5 °C. Which "
                "way does energy move between them?",
        "options": [
            {"text": "From the cool box into the peas, because the box is "
                     "at the higher temperature",
             "correct": True},
            {"text": "From the peas into the box, because the peas are "
                     "the colder of the two",
             "correct": False,
             "why": "Energy leaves the hotter object, and at −5 °C the "
                    "box is the hotter of the two."},
            {"text": "Neither way, because both are below 0 °C and so "
                     "count as cold rather than hot",
             "correct": False,
             "why": "Only the temperature difference matters; the rule "
                    "works just the same below 0 °C."},
            {"text": "Both ways at once, because two frozen objects "
                     "cannot warm one another",
             "correct": False,
             "why": "The warmer box does warm the peas; being frozen "
                    "does not stop energy moving into them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e21",
        "band": "easier",
        "text": "A bath of water at 38 °C and a mug of tea at 38 °C are "
                "compared. What can you say about the two?",
        "options": [
            {"text": "The bath is hotter, because there is more of it",
             "correct": False,
             "why": "Equal readings mean equal temperature, however "
                    "different the amounts are."},
            {"text": "They are at the same temperature, whatever their "
                     "sizes",
             "correct": True},
            {"text": "The mug is hotter, because it cools down faster",
             "correct": False,
             "why": "Cooling speed does not change the reading right "
                    "now — both are 38 °C."},
            {"text": "Neither has a temperature until they are placed "
                     "beside each other",
             "correct": False,
             "why": "Each already has its own temperature; standing "
                    "them together does not create one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e22",
        "band": "easier",
        "text": "A student leaves a warm can of soup on a cold windowsill "
                "overnight. By morning, what is true?",
        "options": [
            {"text": "The can is colder than the windowsill, because it "
                     "started warmer",
             "correct": False,
             "why": "By morning both have settled to the same "
                    "temperature; neither stays behind."},
            {"text": "The can still holds all the energy it started "
                     "with",
             "correct": False,
             "why": "A good deal of that energy has left the can and "
                    "warmed the windowsill and the air around it."},
            {"text": "The can and its surroundings are at the same "
                     "temperature",
             "correct": True},
            {"text": "The windowsill has become warmer than the can",
             "correct": False,
             "why": "Both settle to the same point; the windowsill does "
                    "not overtake it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e23",
        "band": "easier",
        "text": "A hot metal casting is lowered into a bucket of cold "
                "water and left. What eventually happens to the flow of "
                "energy between them?",
        "options": [
            {"text": "It keeps going for ever, because metal keeps "
                     "giving off energy",
             "correct": False,
             "why": "The flow stops once the casting and the water "
                    "reach the same temperature."},
            {"text": "It reverses once the water has warmed up a little",
             "correct": False,
             "why": "The flow never reverses; it simply weakens and then "
                    "stops as the temperatures meet."},
            {"text": "It carries on until the casting has used up all "
                     "its energy",
             "correct": False,
             "why": "The casting keeps plenty of energy; the flow stops "
                    "at matching temperatures, not at empty."},
            {"text": "It stops once the casting and the water reach the "
                     "same temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e24",
        "band": "easier",
        "text": "Why is it wrong to say a fridge “pumps cold air” into "
                "the food compartment?",
        "options": [
            {"text": "Because a fridge only moves energy; cold is not a "
                     "substance to pump",
             "correct": True},
            {"text": "Because fridges work using warm air, not cold air",
             "correct": False,
             "why": "A fridge does contain cold air; the mistake is "
                    "calling it a pumped substance."},
            {"text": "Because the compartment is sealed, so nothing can "
                     "be pumped in",
             "correct": False,
             "why": "The compartment is not perfectly sealed, and that "
                    "is not why the sentence is wrong."},
            {"text": "Because the food inside produces its own cooling",
             "correct": False,
             "why": "Food produces no cooling of its own; the fridge "
                    "removes energy from it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e25",
        "band": "easier",
        "text": "A hot cup of tea and a cold glass of milk are left in "
                "the same room. Which one has more energy transferred "
                "out of it before both settle at room temperature?",
        "options": [
            {"text": "It depends on which drink is picked up first",
             "correct": False,
             "why": "The order they are picked up makes no difference to "
                    "the transfer already happening."},
            {"text": "The tea, because it starts further from the "
                     "room's temperature",
             "correct": True},
            {"text": "The milk, because cold liquids lose energy faster",
             "correct": False,
             "why": "Cold liquids do not lose energy faster; the milk is "
                    "actually gaining energy, not losing it."},
            {"text": "Neither, because both are liquids and behave identically",
             "correct": False,
             "why": "Being liquids does not make their starting "
                    "temperatures the same, and one is above room "
                    "temperature while the other is below it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e26",
        "band": "easier",
        "text": "A large boulder and a small pebble sit outside all "
                "night, both made of the same rock. By morning, what is "
                "true of their temperatures?",
        "options": [
            {"text": "The pebble is colder, because it is much smaller",
             "correct": False,
             "why": "Size decides how much energy is held, not what "
                    "temperature is finally reached."},
            {"text": "The boulder is colder, because it holds far more "
                     "energy",
             "correct": False,
             "why": "Holding more energy is not the same as being "
                    "colder; both settle to the air's temperature."},
            {"text": "Both are at the same temperature as the air "
                     "around them",
             "correct": True},
            {"text": "Neither has a fixed temperature until it is "
                     "touched",
             "correct": False,
             "why": "Both already have a temperature, whether or not "
                    "anyone touches them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e27",
        "band": "easier",
        "text": "A parent tells a child that opening the freezer for a "
                "few seconds will not warm up the kitchen. Is the parent "
                "right?",
        "options": [
            {"text": "No — the freezer's motor adds a burst of extra "
                     "energy the moment the door opens",
             "correct": False,
             "why": "The kitchen warming from an open freezer comes "
                    "from ongoing running, not a burst tied to opening."},
            {"text": "Yes — freezers are too well insulated for any "
                     "energy to escape",
             "correct": False,
             "why": "Some energy does escape through the open door and "
                    "the running motor while it is open."},
            {"text": "No — freezing food destroys some of the room's "
                     "energy",
             "correct": False,
             "why": "Freezing destroys no energy; it only moves it "
                    "about."},
            {"text": "Roughly, for a few seconds — but leaving it open "
                     "a long time would warm the room",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e28",
        "band": "easier",
        "text": "A camper says their sleeping bag “keeps the cold "
                "out.” What is actually happening?",
        "options": [
            {"text": "The bag slows the loss of the camper's own energy "
                     "to the cold air outside",
             "correct": True},
            {"text": "The bag stops the outside air's coldness reaching the camper",
             "correct": False,
             "why": "There is no coldness travelling in; the issue is "
                    "the camper's own energy leaving."},
            {"text": "The bag makes warmth of its own to fight off the "
                     "cold",
             "correct": False,
             "why": "A sleeping bag makes no energy; it only slows the "
                    "camper's own energy escaping."},
            {"text": "The bag reflects the outside air's coldness back "
                     "outside",
             "correct": False,
             "why": "Coldness cannot be reflected, because it is not a "
                    "substance or a wave."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e29",
        "band": "easier",
        "text": "A jug of water at 20 °C is left in a warm kitchen at "
                "25 °C for a long time. What is true once nothing more "
                "changes?",
        "options": [
            {"text": "The water stays at 20 °C for ever, since water "
                     "resists warming",
             "correct": False,
             "why": "Water is not resistant this way; left long enough "
                    "it settles to the kitchen's temperature."},
            {"text": "The water has warmed to 25 °C, matching the "
                     "kitchen",
             "correct": True},
            {"text": "The water has cooled the kitchen down to 20 °C "
                     "instead",
             "correct": False,
             "why": "The kitchen is far larger, so the tiny jug cannot "
                    "pull its temperature down noticeably."},
            {"text": "The water and the kitchen swap temperatures with "
                     "each other",
             "correct": False,
             "why": "Nothing swaps; energy simply moves from the warmer "
                    "kitchen into the cooler water until they match."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e30",
        "band": "easier",
        "text": "Two identical mugs of tea are poured at the same "
                "moment, one placed on a warm radiator and one placed on "
                "a cold windowsill. After an hour, which is at a lower "
                "temperature?",
        "options": [
            {"text": "The one on the radiator, because radiators feel "
                     "cold to touch at first",
             "correct": False,
             "why": "A radiator is warmer than room temperature, so it "
                    "adds energy to the tea rather than removing it."},
            {"text": "Neither — both mugs stay exactly at the temperature they were poured at",
             "correct": False,
             "why": "Both mugs exchange energy with whatever they are "
                    "standing on, so neither one stays unchanged."},
            {"text": "The one on the windowsill, because it is losing "
                     "energy to a colder surrounding",
             "correct": True},
            {"text": "It cannot be known without knowing how much tea is "
                     "in each mug",
             "correct": False,
             "why": "The amount affects how far each temperature has "
                    "moved by then, not which one ends up lower."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-04-s08",
        "band": "standard",
        "text": "500 g of water at 60 °C is mixed with 500 g of water at "
                "20 °C. What is the best estimate of the final "
                "temperature?",
        "options": [
            {"text": "20 °C, because cold always dominates a mixture",
             "correct": False,
             "why": "Cold has no special dominance; with equal masses "
                    "the result sits exactly between the two."},
            {"text": "80 °C, because the two temperatures add together",
             "correct": False,
             "why": "Temperatures never add when liquids mix; the "
                    "result lies between them."},
            {"text": "40 °C, exactly halfway between the two, since the "
                     "masses are equal",
             "correct": True},
            {"text": "60 °C, because hot water always wins out",
             "correct": False,
             "why": "Neither temperature wins; with equal masses the "
                    "mixture settles exactly in the middle."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s09",
        "band": "standard",
        "text": "1 kg of water at 90 °C is added to 9 kg of water at "
                "10 °C. Which estimate for the final temperature is most "
                "sensible?",
        "options": [
            {"text": "50 °C, halfway between the two starting values",
             "correct": False,
             "why": "Halfway only applies with equal masses; here the "
                    "9 kg is far larger and pulls the result close to "
                    "its own value."},
            {"text": "100 °C, because the two temperatures add together",
             "correct": False,
             "why": "Mixing liquids never adds their temperatures; the "
                    "answer must lie between 10 °C and 90 °C."},
            {"text": "90 °C, because the smaller amount is much hotter",
             "correct": False,
             "why": "Being hotter is not enough; the 9 kg vastly "
                    "outweighs the 1 kg and pulls the result down."},
            {"text": "18 °C, close to the larger mass's starting "
                     "temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s10",
        "band": "standard",
        "text": "A student says an air conditioning unit cools a room "
                "“the same way” a fridge with its door open does. Is "
                "that correct?",
        "options": [
            {"text": "Yes — both simply release cold air stored inside "
                     "them",
             "correct": False,
             "why": "Neither stores cold air as a substance; both only "
                    "move energy."},
            {"text": "No — an air conditioner moves energy out of the "
                     "building, while an open fridge keeps it inside",
             "correct": True},
            {"text": "Yes — both work by destroying a little of the "
                     "room's energy",
             "correct": False,
             "why": "Neither device destroys energy; both only "
                    "relocate it."},
            {"text": "No — fridges cannot move energy at all, only air conditioners can, because a fridge merely holds its cold air still",
             "correct": False,
             "why": "A fridge does move energy, from inside its "
                    "compartment to the coils at the back; the "
                    "difference is where that energy ends up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s11",
        "band": "standard",
        "text": "A welder's spark at over 1000 °C lands briefly on a "
                "workbench without setting it alight, but a cooking fire "
                "at 400 °C easily does. What explains this?",
        "options": [
            {"text": "The spark is not really that hot; its true temperature is much lower than stated",
             "correct": False,
             "why": "Its temperature genuinely is that high; the issue "
                    "is how little energy the tiny spark carries."},
            {"text": "The bench resists a spark better than it resists a "
                     "fire",
             "correct": False,
             "why": "The bench material does not change between the two "
                    "events; the difference is the size of what is "
                    "touching it."},
            {"text": "The spark carries very little total energy, while "
                     "the fire delivers energy continuously",
             "correct": True},
            {"text": "A single spark cannot transfer any energy, unlike "
                     "a flame",
             "correct": False,
             "why": "The spark does transfer some energy; it is simply "
                    "far too little and far too brief to matter."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s12",
        "band": "standard",
        "text": "A 2 kg block of metal at 100 °C is placed in a large "
                "lake at 15 °C. Which statement about the final state is "
                "correct?",
        "options": [
            {"text": "The lake's temperature barely changes, and the "
                     "block cools to close to 15 °C",
             "correct": True},
            {"text": "The block and the lake meet exactly halfway, at about 57 °C, as any two objects left in contact always do",
             "correct": False,
             "why": "Halfway only happens with roughly equal masses; "
                    "the lake vastly outweighs the block."},
            {"text": "The lake warms to 100 °C because the block was "
                     "hotter",
             "correct": False,
             "why": "The lake has far too much water for a single block "
                    "to raise it to the block's own temperature."},
            {"text": "Nothing changes, because the lake is too big to "
                     "be affected",
             "correct": False,
             "why": "The lake does gain a tiny amount of energy — it is "
                    "simply too small to notice in such a vast amount of "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s13",
        "band": "standard",
        "text": "A hot metal ingot and a small pool of oil are used to "
                "explain thermal equilibrium. Which statement correctly "
                "uses the idea?",
        "options": [
            {"text": "The ingot keeps its own temperature no matter what "
                     "it touches",
             "correct": False,
             "why": "An object's temperature does change once it is in "
                    "contact with something at a different temperature."},
            {"text": "Each object simply keeps whichever particular temperature happens to be more natural to its own material",
             "correct": False,
             "why": "No material has a natural temperature it defends; "
                    "contact between them decides the outcome."},
            {"text": "Left together, the ingot and the oil settle at "
                     "one shared temperature between their starting "
                     "values",
             "correct": True},
            {"text": "The colder of the two eventually becomes the "
                     "hotter one",
             "correct": False,
             "why": "The colder one warms and the hotter one cools, but "
                    "neither swaps roles entirely; they meet in between."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s14",
        "band": "standard",
        "text": "A pan of soup at 90 °C is left in a fridge at 4 °C. "
                "Explain what happens to the net flow of energy as time "
                "passes.",
        "options": [
            {"text": "It stays exactly constant throughout the whole process, because the soup starts out so much hotter",
             "correct": False,
             "why": "The net flow shrinks as the temperature gap between "
                    "soup and fridge narrows."},
            {"text": "It increases as the soup gets closer to the "
                     "fridge's temperature",
             "correct": False,
             "why": "A smaller temperature difference drives a smaller "
                    "flow, not a larger one."},
            {"text": "It reverses partway through, once the soup has "
                     "cooled a little",
             "correct": False,
             "why": "The flow never reverses; it simply weakens and then "
                    "stops as the temperatures meet."},
            {"text": "It gradually decreases as the soup cools, reaching "
                     "zero once the soup matches the fridge",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s15",
        "band": "standard",
        "text": "Explain why a large tank of warm water cools far more "
                "slowly overnight than a small cup of the same warm "
                "water.",
        "options": [
            {"text": "The tank contains far more particles, so the same "
                     "energy loss changes its temperature by much less",
             "correct": True},
            {"text": "The tank is simply a better insulator overall, since tanks like this are usually built from much thicker material",
             "correct": False,
             "why": "Wall thickness is not the reason here; both are "
                    "simply water losing energy to the room."},
            {"text": "The cup loses energy faster because liquids in "
                     "small containers boil more easily",
             "correct": False,
             "why": "Nothing here is boiling; the cup is simply cooling "
                    "towards room temperature."},
            {"text": "The tank keeps making its own warmth to replace "
                     "what it loses",
             "correct": False,
             "why": "A tank of water makes no energy of its own; it can "
                    "only lose what it started with."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s16",
        "band": "standard",
        "text": "A thermometer reads 21 °C in a bowl of water, and reads "
                "21 °C again when moved into a separate bowl of oil "
                "standing in the same room. What can be concluded about "
                "the water and the oil?",
        "options": [
            {"text": "Nothing can be concluded until the two liquids are "
                     "poured into one container together",
             "correct": False,
             "why": "The thermometer has settled with each liquid in "
                    "turn, and that is enough to compare the two."},
            {"text": "They are at the same temperature, so no net energy "
                     "would flow if they were put in contact",
             "correct": True},
            {"text": "The oil must be hotter, because oil holds more "
                     "energy than water for the same reading",
             "correct": False,
             "why": "Total energy and temperature are different "
                    "quantities; an equal reading means an equal "
                    "temperature."},
            {"text": "The water must be hotter, because water passes "
                     "energy to a thermometer more readily than oil",
             "correct": False,
             "why": "How quickly a thermometer settles does not change "
                    "the reading it finally settles at."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s17",
        "band": "standard",
        "text": "A metal casting cools from 800 °C to 750 °C in the "
                "first ten minutes, then only from 750 °C to 745 °C in "
                "the next ten minutes. Why does the drop get smaller?",
        "options": [
            {"text": "The temperature difference between the casting "
                     "and the room has shrunk, so the flow is weaker",
             "correct": True},
            {"text": "The casting has less total energy left to lose as "
                     "time passes",
             "correct": False,
             "why": "It still holds a huge amount of energy at 745 °C; "
                    "the flow has simply slowed."},
            {"text": "The room has warmed up to match the casting's "
                     "early temperature",
             "correct": False,
             "why": "The room barely changes; it is the casting's own "
                    "temperature that has moved."},
            {"text": "Metal always cools down in exactly equal steps, no matter what starting temperature it begins at",
             "correct": False,
             "why": "Real cooling slows as the gap narrows, rather than "
                    "dropping by a fixed amount each time."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s18",
        "band": "standard",
        "text": "A camping stove boils water in an open pan on a windy "
                "day, and the water takes far longer to boil than "
                "usual. What can you conclude about the energy account?",
        "options": [
            {"text": "The stove is somehow creating less of its own energy than usual, purely because of the wind blowing past it",
             "correct": False,
             "why": "The stove supplies roughly the same energy; the "
                    "wind is carrying more of it away before it reaches "
                    "the water."},
            {"text": "The water has begun losing its own ability to "
                     "hold energy",
             "correct": False,
             "why": "Water's ability to hold energy has not changed; "
                    "the surroundings are simply taking more of the "
                    "supply."},
            {"text": "More of the stove's energy is being carried away "
                     "by the moving air before it reaches the water",
             "correct": True},
            {"text": "The wind destroys some of the energy that the "
                     "stove supplies",
             "correct": False,
             "why": "Wind carries energy away into the surroundings; it "
                    "destroys none of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s19",
        "band": "standard",
        "text": "A hot water bottle at 60 °C is placed against a "
                "person's back at 37 °C under a thick duvet. Which "
                "correctly describes what follows?",
        "options": [
            {"text": "The two separate temperatures average out immediately to exactly 48.5 °C the instant they first touch",
             "correct": False,
             "why": "The settling happens gradually, and the final "
                    "value depends on how much of each there is, not a "
                    "simple average of two numbers."},
            {"text": "Nothing changes, because the duvet blocks any "
                     "transfer completely",
             "correct": False,
             "why": "The duvet slows the loss of energy to the room; it "
                    "does not stop the bottle and the person exchanging "
                    "energy with each other."},
            {"text": "The person's own coldness travels into the bottle "
                     "and cancels its heat",
             "correct": False,
             "why": "There is no coldness to travel; only energy leaves "
                    "the hotter bottle."},
            {"text": "Energy flows from the bottle into the person until "
                     "the temperature difference disappears",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s20",
        "band": "standard",
        "text": "A large saucepan of stew and a small ramekin of the "
                "same stew are both taken out of a hot oven at the same "
                "moment. Which cools to room temperature first?",
        "options": [
            {"text": "The ramekin, because it holds far less energy for "
                     "the same starting temperature",
             "correct": True},
            {"text": "The saucepan, because a larger amount of stew always loses its own energy much faster",
             "correct": False,
             "why": "Larger amounts generally take longer to cool, "
                    "because they hold more energy to lose."},
            {"text": "Neither — both cool at the same rate regardless of "
                     "size",
             "correct": False,
             "why": "The much smaller ramekin has far less energy to "
                    "lose to reach room temperature, so it gets there "
                    "sooner."},
            {"text": "It depends only on which container is a darker "
                     "colour",
             "correct": False,
             "why": "Colour is not the deciding factor here; the amount "
                    "of stew is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s21",
        "band": "standard",
        "text": "A tank holds 40 kg of water at 45 °C. A jug of 2 kg at "
                "15 °C is poured in. Which is closest to the final "
                "temperature?",
        "options": [
            {"text": "30 °C, halfway between the two",
             "correct": False,
             "why": "Halfway only applies when the two masses are close "
                    "in size; here the tank is twenty times larger."},
            {"text": "About 44 °C, close to the tank's own temperature",
             "correct": True},
            {"text": "15 °C, because the smaller amount always sets the "
                     "final value",
             "correct": False,
             "why": "The much larger tank dominates the outcome, not the "
                    "small jug."},
            {"text": "60 °C, because the two temperatures are added",
             "correct": False,
             "why": "Mixing never adds the two temperatures; the result "
                    "must lie between 15 °C and 45 °C."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s22",
        "band": "standard",
        "text": "Explain why blowing on a hot spoonful of soup cools it "
                "faster than simply leaving it to stand.",
        "options": [
            {"text": "Blowing destroys some of the soup's energy on contact, leaving the spoonful holding less than it started with",
             "correct": False,
             "why": "Blowing destroys nothing; it only moves the warmed "
                    "air away and brings in cooler air."},
            {"text": "Blowing physically and directly adds the cold air's own coldness straight into the hot soup itself",
             "correct": False,
             "why": "No coldness is added; only the surrounding air's "
                    "temperature and how often it is refreshed matter."},
            {"text": "Blowing sweeps away the air the soup has already "
                     "warmed, so cooler air keeps arriving",
             "correct": True},
            {"text": "Blowing lowers the soup's own temperature setting",
             "correct": False,
             "why": "A spoonful of soup has no such setting; only actual "
                    "energy transfer changes its temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s23",
        "band": "standard",
        "text": "Two identical metal blocks start at 20 °C. One is "
                "placed on a hotplate at 20 °C and one on a hotplate at "
                "80 °C. After a long time, compare their temperatures.",
        "options": [
            {"text": "Both are still at 20 °C, since that is where they "
                     "started",
             "correct": False,
             "why": "The block on the 80 °C hotplate rises to match it; "
                    "only the other one stays at 20 °C."},
            {"text": "Both settle at 50 °C, halfway between the two "
                     "hotplate settings",
             "correct": False,
             "why": "Each block reaches equilibrium with its own "
                    "hotplate independently; they never interact with "
                    "each other."},
            {"text": "Both rise to 80 °C, because contact with any "
                     "hotplate raises temperature",
             "correct": False,
             "why": "Contact with a hotplate at the same temperature "
                    "causes no net change at all."},
            {"text": "The first stays at 20 °C, and the second rises to "
                     "80 °C",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s24",
        "band": "standard",
        "text": "A student argues that a large iceberg must be “more "
                "cold” than a small ice cube because it is so much "
                "bigger. What is the correct response?",
        "options": [
            {"text": "They are right — bigger cold objects are colder",
             "correct": False,
             "why": "Temperature does not scale with size; an iceberg "
                    "and a cube of the same ice are at the same "
                    "temperature."},
            {"text": "They are wrong — size always affects the amount of energy involved, not the temperature reading",
             "correct": True},
            {"text": "They are right, but only because icebergs always happen to float around in much colder water than cubes do",
             "correct": False,
             "why": "Floating in colder water is not the reason given, "
                    "and an iceberg on land would be no different."},
            {"text": "They are wrong, because ice cubes are colder than icebergs, since a smaller piece of ice chills down further",
             "correct": False,
             "why": "Neither is automatically colder; both can be at "
                    "the same temperature regardless of size."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s25",
        "band": "standard",
        "text": "A 100 g mug of tea at 70 °C is left beside a separate "
                "100 g mug of tea at 70 °C, not touching. Ten minutes "
                "later, are they still at the same temperature as each "
                "other?",
        "options": [
            {"text": "Yes, provided they have been losing energy to the "
                     "same surroundings in the same way",
             "correct": True},
            {"text": "No, because two separate mugs can never match exactly, since each cools at a rate set by its own handle and rim",
             "correct": False,
             "why": "Identical starting mugs losing energy under the "
                    "same conditions do reach matching readings."},
            {"text": "No, because tea cools unevenly from mug to mug",
             "correct": False,
             "why": "Under the same conditions, two identical mugs cool "
                    "the same way."},
            {"text": "Yes, but only because the two separate mugs are somehow secretly touching underneath the table",
             "correct": False,
             "why": "Touching is not required; each simply loses energy "
                    "to the same room at the same rate."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s26",
        "band": "standard",
        "text": "A block of copper and a block of wood, both starting at "
                "90 °C, are left in a cold room. A student claims the "
                "wood will end up at a lower final temperature. Assess "
                "the claim.",
        "options": [
            {"text": "Correct — wood settles below the surrounding air's temperature, because wood keeps drawing energy out of itself",
             "correct": False,
             "why": "No material settles below the surrounding "
                    "temperature; both blocks end up matching the room."},
            {"text": "Correct — wood holds onto its own particular coldness once it first starts cooling down",
             "correct": False,
             "why": "Wood holds no coldness of its own; cooling is "
                    "simply energy leaving it."},
            {"text": "Incorrect — both blocks always end up at the same final temperature as the room",
             "correct": True},
            {"text": "It depends on which block is heavier",
             "correct": False,
             "why": "Weight changes how long it takes to reach the "
                    "room's temperature, not what that final temperature "
                    "is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s27",
        "band": "standard",
        "text": "A vacuum flask keeps coffee hot for hours far better "
                "than an open mug does. Does this mean the flask breaks "
                "the rule that objects move towards the temperature of "
                "their surroundings?",
        "options": [
            {"text": "Yes — a genuinely good flask keeps its coffee permanently fixed at its original starting temperature",
             "correct": False,
             "why": "Even the best flask lets a little energy escape "
                    "eventually; given enough time the coffee still "
                    "cools."},
            {"text": "No — because flasks actually raise the coffee's temperature slightly, by trapping its energy and concentrating it",
             "correct": False,
             "why": "A flask cannot raise the coffee's temperature; it "
                    "can only reduce how quickly it falls."},
            {"text": "Yes — flasks work by adding fresh energy to "
                     "replace what is lost",
             "correct": False,
             "why": "A flask adds no energy of its own; it can only slow "
                    "the loss of what is already there."},
            {"text": "No — it only slows the rate of energy loss; the coffee still moves towards room temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s28",
        "band": "standard",
        "text": "300 g of water at 50 °C is mixed with 100 g of water at "
                "10 °C. Which is the best estimate for the final "
                "temperature?",
        "options": [
            {"text": "30 °C, exactly halfway between the two",
             "correct": False,
             "why": "Halfway would need equal masses; here the 50 °C "
                    "water is three times as much."},
            {"text": "About 40 °C, closer to the larger mass's starting "
                     "value",
             "correct": True},
            {"text": "60 °C, because the two temperatures add",
             "correct": False,
             "why": "Mixing liquids never adds the two temperatures "
                    "together."},
            {"text": "10 °C, because the smaller amount always decides "
                     "the outcome",
             "correct": False,
             "why": "The larger 300 g mass dominates the result, not the "
                    "smaller 100 g."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s29",
        "band": "standard",
        "text": "The end of a metal fork standing in a bowl of hot "
                "custard becomes too hot to touch within seconds, while "
                "the handle sticking out of the bowl is still only "
                "slightly warm a minute later. Explain why the fork's "
                "end heats up so much faster than its handle does.",
        "options": [
            {"text": "The end is in direct contact with the custard, "
                     "and each part only warms as energy reaches it",
             "correct": True},
            {"text": "The whole fork changes temperature at the same speed everywhere, because metal spreads energy through itself at once",
             "correct": False,
             "why": "The end in the custard clearly changes far faster "
                    "than the handle further away."},
            {"text": "The custard sends its coldness through the handle "
                     "first",
             "correct": False,
             "why": "There is no coldness in the custard to send "
                    "anywhere; only energy from it is moving."},
            {"text": "The handle must actually be made from a completely different material from the rest of the metal fork itself",
             "correct": False,
             "why": "A fork is normally one material throughout; the "
                    "delay is about distance from the custard."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s30",
        "band": "standard",
        "text": "A student measures a mug of tea at 65 °C and, twenty "
                "minutes later, at 40 °C, in a room that stayed at "
                "20 °C throughout. Which statement best explains why the "
                "tea did not reach 20 °C in that time?",
        "options": [
            {"text": "Twenty minutes was too short for the temperature "
                     "difference to disappear completely",
             "correct": True},
            {"text": "The tea somehow created a little more of its own fresh energy in order to resist cooling",
             "correct": False,
             "why": "Tea makes no energy of its own; it can only lose "
                    "what it started with."},
            {"text": "The room must have been warmer than 20 °C for part of the time, since a thermometer in a warm room drifts upward",
             "correct": False,
             "why": "The room stayed at 20 °C throughout, as stated; the "
                    "tea's temperature is simply still falling towards "
                    "it."},
            {"text": "The mug stopped losing energy once it reached "
                     "40 °C",
             "correct": False,
             "why": "It is still losing energy at 40 °C; it will keep "
                    "cooling until it matches the room."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-04-h08",
        "band": "harder",
        "text": "A 5 kg block of iron at 200 °C is dropped into 45 kg "
                "of water at 15 °C. Which range must the final shared "
                "temperature fall inside?",
        "options": [
            {"text": "Between 100 °C and 200 °C, since the block started out by far the hottest object anywhere in the whole set-up",
             "correct": False,
             "why": "The final value lies between the two STARTING "
                    "values, and it ends up far closer to 15 °C than "
                    "to 200 °C given the water's much larger mass."},
            {"text": "Exactly 200 °C, because the block controls the "
                     "outcome",
             "correct": False,
             "why": "The water vastly outweighs the block, so the "
                    "outcome sits far closer to the water's own starting "
                    "value."},
            {"text": "Between 15 °C and 200 °C, much closer to 15 °C "
                     "because the water's mass is far larger",
             "correct": True},
            {"text": "Below 15 °C, because adding a much hotter block somehow cools the water down even further before it settles",
             "correct": False,
             "why": "The water can only rise from 15 °C once a hotter "
                    "object joins it, never fall below its own starting "
                    "value."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h09",
        "band": "harder",
        "text": "A scientist wants to warm 1000 kg of water in a tank by "
                "dropping in hot metal blocks, one at a time. Why does "
                "the number of blocks required depend on more than just "
                "how hot each block is?",
        "options": [
            {"text": "Because the total energy each block can hand over "
                     "also depends on how much metal it contains",
             "correct": True},
            {"text": "Because only the very last block that gets added into the tank actually transfers any energy at all",
             "correct": False,
             "why": "Every block transfers energy on contact, not only "
                    "the final one."},
            {"text": "Because water refuses to accept energy above a certain temperature, and turns any further supply away unchanged",
             "correct": False,
             "why": "Water accepts energy from anything hotter than it, "
                    "right up to boiling; there is no such refusal here."},
            {"text": "Because hotter blocks contain fewer particles than "
                     "cooler ones",
             "correct": False,
             "why": "Temperature says nothing about how many particles a "
                    "block contains; that depends on its mass alone."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h10",
        "band": "harder",
        "text": "A student wrongly claims that stirring a mixture of hot "
                "and cold water changes the FINAL temperature it "
                "settles at, compared with leaving it unstirred. What is "
                "the strongest objection?",
        "options": [
            {"text": "Stirring drives the mixture to settle well above the hotter portion's own starting temperature, through the spoon's movement alone",
             "correct": False,
             "why": "A spoon adds a negligible amount; the mixture still "
                    "settles between the two starting temperatures, never "
                    "above the hotter one."},
            {"text": "Stirring can only ever raise the final temperature, "
                     "never lower it",
             "correct": False,
             "why": "Stirring changes how quickly the mixture settles, "
                    "not which value it settles at."},
            {"text": "Stirring physically and permanently destroys some of the hot water's own energy before it ever gets the chance to be transferred across",
             "correct": False,
             "why": "Stirring destroys nothing; it only helps the two "
                    "portions mix and settle more quickly."},
            {"text": "The final temperature is set by the total energy "
                     "and amount of the two starting portions, which "
                     "stirring does not change",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h11",
        "band": "harder",
        "text": "A camper has a 2 litre flask of hot water and wants the "
                "warmest possible drink by mixing in some cold stream "
                "water. Explain why adding a little cold water barely "
                "changes the final temperature, but adding a lot does.",
        "options": [
            {"text": "The final temperature depends on the ratio of the "
                     "two amounts, so a small addition shifts it only "
                     "slightly",
             "correct": True},
            {"text": "A little cold water is completely destroyed the instant it makes contact with the hot flask, before it can ever have an effect",
             "correct": False,
             "why": "Nothing is destroyed; even a small amount of cold "
                    "water does transfer some energy."},
            {"text": "Cold water only starts affecting the temperature once a certain amount has been added, and does nothing at all below that",
             "correct": False,
             "why": "Any amount added has some effect; there is no "
                    "threshold before which nothing happens."},
            {"text": "The flask's hot water resists small additions of "
                     "cold water",
             "correct": False,
             "why": "Hot water has no such resistance; the small shift "
                    "is simply because the addition is a small share of "
                    "the total."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h12",
        "band": "harder",
        "text": "A 1 kg copper block at 90 °C, a 1 kg copper block at "
                "30 °C and a 1 kg copper block at 60 °C are sealed "
                "together inside an insulated box and left. Predict the "
                "final temperature of all three.",
        "options": [
            {"text": "90 °C, because the hottest block sets the temperature the other two must rise to meet",
             "correct": False,
             "why": "The hot block cools as it warms the other two; "
                    "nothing lifts all three to the highest starting "
                    "value."},
            {"text": "60 °C, the average of the three starting values, "
                     "since the masses and the material are identical",
             "correct": True},
            {"text": "180 °C, which is what the three starting temperatures come to when they are added together",
             "correct": False,
             "why": "Temperatures are never added; the shared value must "
                    "lie between the lowest and the highest starting "
                    "value."},
            {"text": "30 °C, because energy always drains downwards to whichever object in the box is the coldest one",
             "correct": False,
             "why": "The cold block warms while the hot one cools, so "
                    "they meet in between rather than all falling to the "
                    "lowest value."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h13",
        "band": "harder",
        "text": "A factory cools molten metal by pouring it into 200 "
                "identical moulds, each surrounded by a fixed amount of "
                "water. An engineer wants to predict the final "
                "temperature of the water in one mould without weighing "
                "the metal in it. What must they know?",
        "options": [
            {"text": "The mass and starting temperature of both the "
                     "metal poured into that mould and the water "
                     "surrounding it",
             "correct": True},
            {"text": "Only the temperature the metal started at, since the mass involved makes very little real difference to the outcome",
             "correct": False,
             "why": "Mass is essential; the same hot metal in a larger "
                    "or smaller amount of water settles at very "
                    "different final temperatures."},
            {"text": "Only how many moulds there are in total",
             "correct": False,
             "why": "The number of other moulds says nothing about this "
                    "particular mould's own mix of metal and water."},
            {"text": "Only the colour the molten metal glows, since glow colour fixes both the temperature and the mass of metal present",
             "correct": False,
             "why": "Glow colour hints at temperature, but the final "
                    "settled temperature also needs how much metal and "
                    "water are involved."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h14",
        "band": "harder",
        "text": "The graph shows the temperature of a beaker of hot water as "
                "it cools in a room at 20 °C. Why does the line level off?",
        "options": [
            {"text": "The water is running out of energy to give out to the "
                     "room",
             "correct": False,
             "why": "The water still holds plenty of energy as the line "
                    "levels off. It is the rate of transfer that has fallen, "
                    "not the supply."},
            {"text": "The temperature difference between the water and the "
                     "room is shrinking, so the transfer slows",
             "correct": True},
            {"text": "The thermometer develops a fault as its reading gets "
                     "close to room temperature, so it stops changing",
             "correct": False,
             "why": "A thermometer reads correctly all the way down. The "
                    "levelling off is real physics, not a fault."},
            {"text": "The room slowly warms up until it matches the water's "
                     "falling temperature",
             "correct": False,
             "why": "A room is far bigger than a beaker, so its temperature "
                    "hardly changes. It is the water's temperature that does "
                    "almost all the moving."},
        ],
        "figure": "p1-cooling-curve",
    },
    {
        "id": "p1-04-h15",
        "band": "harder",
        "text": "A student says that because a swimming pool holds far "
                "more energy than a kettle of boiling water, putting "
                "the kettle into the pool would make the pool's "
                "temperature rise a lot. Evaluate this.",
        "options": [
            {"text": "Correct — the kettle's water is so much hotter that it must completely dominate the eventual outcome of the mix",
             "correct": False,
             "why": "Being hotter does not mean dominating; the pool "
                    "vastly outweighs the kettle in amount."},
            {"text": "Correct — total energy alone decides the final shared temperature, and the pool already holds far more of it",
             "correct": False,
             "why": "Already having more total energy is exactly why "
                    "the pool's temperature moves so little; the claim "
                    "gets the conclusion backwards."},
            {"text": "Incorrect — the pool's temperature would barely "
                     "change, because its mass vastly outweighs the "
                     "kettle's",
             "correct": True},
            {"text": "Incorrect — the two amounts of water cannot mix "
                     "their temperatures at all",
             "correct": False,
             "why": "They can and do mix towards a shared temperature; "
                    "it simply ends up very close to the pool's own "
                    "value."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h16",
        "band": "harder",
        "text": "A physicist wants to explain why the ash left after a "
                "bonfire is still warm the next morning, hours after "
                "the flames have died. Which account is correct?",
        "options": [
            {"text": "The ash is genuinely producing entirely fresh energy of its own all through the night as it keeps on reacting chemically",
             "correct": False,
             "why": "Cold ash produces no new energy; any warmth left "
                    "is simply what has not yet left it."},
            {"text": "The night air is somehow warmer around the ash than everywhere else, and that warm pocket keeps the ash warm",
             "correct": False,
             "why": "The air is the same temperature nearby; the "
                    "difference is the ash's own remaining store of "
                    "energy."},
            {"text": "The ash is protected from losing energy by the fire's leftover flames, which shield it right through the night",
             "correct": False,
             "why": "The flames are out; nothing is protecting the ash "
                    "from losing energy, it is simply doing so slowly."},
            {"text": "The ash's large mass of particles is releasing "
                     "its remaining thermal energy slowly to the cooler "
                     "night air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h17",
        "band": "harder",
        "text": "A tank contains 1000 litres of water at 25 °C. A "
                "student adds a single ice cube at 0 °C and claims the "
                "whole tank's reading will drop noticeably on the "
                "thermometer. Evaluate the claim using what you know "
                "about mixing different amounts.",
        "options": [
            {"text": "Correct — absolutely any object placed below the water's own temperature pulls the thermometer's reading down noticeably",
             "correct": False,
             "why": "A single small ice cube against a huge tank changes "
                    "the average by an amount too small to read on an "
                    "ordinary thermometer."},
            {"text": "Incorrect — the ice cube's mass is genuinely negligible next to 1000 litres, so the final reading barely moves",
             "correct": True},
            {"text": "Correct — ice always cools down whatever liquid it is placed into by several whole degrees, whatever the amount",
             "correct": False,
             "why": "How much cooling happens depends on the relative "
                    "masses; against 1000 litres a single cube is "
                    "negligible."},
            {"text": "Incorrect — the ice would need to be much hotter to have no effect, because only warm objects can be left out",
             "correct": False,
             "why": "Being colder is exactly why it would have a tiny "
                    "effect; the size of that effect is what is actually "
                    "in question."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h18",
        "band": "harder",
        "text": "A tank of 200 kg of water at 30 °C is warmed by dropping "
                "in a 5 kg metal block heated to 500 °C, then removing "
                "the cooled block before adding a fresh one heated the "
                "same way. A colleague says this can never make the "
                "water boil however many fresh blocks are added. Is the "
                "colleague right?",
        "options": [
            {"text": "No — a single 500 °C block already carries far more than enough energy on its own to boil the whole 200 kg tank of water completely outright",
             "correct": False,
             "why": "A 5 kg block, however hot, cannot supply enough "
                    "energy to raise 200 kg of water anywhere near "
                    "boiling in one go."},
            {"text": "Yes — water can genuinely never actually be heated at all by dropping any number of blocks of hot metal into it, however many are used at all",
             "correct": False,
             "why": "Adding a hotter object to water does raise the "
                    "water's temperature; this happens every time a "
                    "block is dropped in."},
            {"text": "No — repeated additions keep adding energy to the "
                     "water, so with enough blocks its temperature can "
                     "be pushed up towards boiling",
             "correct": True},
            {"text": "Yes — each fresh block leaves the water at exactly the temperature the block before it left the water at",
             "correct": False,
             "why": "Every block hands over more energy, so the water is "
                    "a little warmer after each one than it was before "
                    "that block went in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h19",
        "band": "harder",
        "text": "A student is asked to design an observation proving "
                "that thermal equilibrium means no NET flow, rather "
                "than no flow at all. Which observation would provide "
                "the best evidence?",
        "options": [
            {"text": "Showing that the two objects have become exactly the same colour all over once they have reached the very same shared temperature as each other",
             "correct": False,
             "why": "Colour has nothing to do with net versus total "
                    "flow; it does not test the claim at all."},
            {"text": "Showing that one of the two objects always ends up settling at a slightly warmer final temperature than the other one ever really does in the end",
             "correct": False,
             "why": "At true equilibrium neither ends up warmer; this "
                    "describes a mixture that has not yet finished "
                    "settling."},
            {"text": "Showing that the two objects physically stop touching each other completely, the very moment true equilibrium is finally reached between them",
             "correct": False,
             "why": "Objects at equilibrium can remain in contact "
                    "indefinitely; nothing forces them apart."},
            {"text": "Showing that particles at the boundary are still "
                     "colliding and exchanging energy even though "
                     "neither object's temperature is changing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h20",
        "band": "harder",
        "text": "A student argues: “Because energy only flows from hot "
                "to cold, a radiator can never make a room warmer than "
                "the radiator's own surface temperature.” Is this "
                "argument sound?",
        "options": [
            {"text": "No — energy sometimes flows from a colder radiator into a hotter room instead, whenever the radiator is switched on",
             "correct": False,
             "why": "It never does; the flow is always from the hotter "
                    "radiator into the cooler room, not the reverse."},
            {"text": "Yes — the room settles somewhere below the "
                     "radiator's surface temperature, never above it, "
                     "which agrees with the rule",
             "correct": True},
            {"text": "No — the radiator can somehow create additional energy entirely of its own, pushing the room hotter than the radiator itself",
             "correct": False,
             "why": "A radiator creates no energy of its own; it can "
                    "only pass on what it is supplied with."},
            {"text": "No — rooms genuinely have no fixed temperature of their own for the radiator to ever compare itself against, in the first place at all",
             "correct": False,
             "why": "A room does have a temperature at every moment; "
                    "the radiator warms it towards, but never past, its "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h21",
        "band": "harder",
        "text": "A cold, half-full swimming pool at 10 °C is compared "
                "with a single saucepan of boiling water at 100 °C. "
                "Which genuinely holds more total energy in its thermal "
                "store?",
        "options": [
            {"text": "The saucepan, because its own temperature of 100 °C is so much higher than the pool's 10 °C reading",
             "correct": False,
             "why": "A higher temperature alone does not decide the "
                    "total; the pool's vastly greater number of "
                    "particles matters far more."},
            {"text": "They hold the same amount, because both are made of water, and one substance holds one fixed amount of energy",
             "correct": False,
             "why": "Being the same substance does not make the totals "
                    "equal; the amount and temperature of each still "
                    "differ hugely."},
            {"text": "The pool, despite its lower temperature, because "
                     "it contains far more particles",
             "correct": True},
            {"text": "It genuinely cannot be worked out at all without first knowing the exact shape of the pool",
             "correct": False,
             "why": "Shape does not change how much energy is in the "
                    "water; its mass and temperature do."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h22",
        "band": "harder",
        "text": "A student wrongly believes that because a giant iceberg "
                "is at a lower TEMPERATURE than a cup of hot tea, the "
                "iceberg must also have a smaller total energy than the "
                "tea. What is the flaw?",
        "options": [
            {"text": "There is genuinely no flaw here at all — the iceberg truly does hold much less total energy than the small cup of hot tea",
             "correct": False,
             "why": "The iceberg's enormous mass of particles gives it a "
                    "far larger total energy than the tea, despite its "
                    "lower temperature."},
            {"text": "The flaw is that icebergs are not really all that cold in the first place, only unusually large compared with an ordinary ice cube",
             "correct": False,
             "why": "Icebergs genuinely are cold; the issue is comparing "
                    "total energy using temperature alone."},
            {"text": "The flaw is that ice genuinely cannot hold any energy whatsoever in its thermal store until it has completely and fully melted",
             "correct": False,
             "why": "Ice well below its melting point still holds "
                    "energy in its thermal store; melting is not "
                    "required for that."},
            {"text": "The flaw is confusing temperature, an average, "
                     "with total energy, which also depends on the "
                     "amount of matter involved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h23",
        "band": "harder",
        "text": "A tank of water and a small metal ball, both starting "
                "at exactly the same temperature, are placed in an "
                "oven. After the oven has been running for a long time, "
                "is either one warmer than the other?",
        "options": [
            {"text": "Yes — metal ends up hotter than water in an oven",
             "correct": False,
             "why": "Given enough time both simply match the oven's own "
                    "temperature; the material does not decide a "
                    "different final value."},
            {"text": "Yes — the ball, because it is smaller and heats up "
                     "more easily",
             "correct": False,
             "why": "Being smaller changes how quickly it reaches the "
                    "oven's temperature, not what that final temperature "
                    "is."},
            {"text": "No — given enough time, both settle at the oven's "
                     "own temperature",
             "correct": True},
            {"text": "It cannot be answered without measuring both "
                     "objects' masses",
             "correct": False,
             "why": "Mass affects only how long each takes to get "
                    "there, not the temperature they both eventually "
                    "reach."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h24",
        "band": "harder",
        "text": "A physicist wants to warm a large greenhouse using "
                "several identical small heaters rather than one huge "
                "one. A colleague argues this must fail because each "
                "small heater only carries a small amount of energy at "
                "any moment. Assess this argument.",
        "options": [
            {"text": "Correct — a whole group of small heaters can never possibly together supply as much total energy as one single big heater would manage",
             "correct": False,
             "why": "Their combined output can match or exceed one "
                    "large heater; there is no rule against multiple "
                    "sources adding up."},
            {"text": "Flawed — the total energy delivered adds up across "
                     "all the heaters and across time, not just from a "
                     "single heater at a single moment",
             "correct": True},
            {"text": "Correct — energy arriving from several separate small sources simply and completely cancels itself out entirely once it is all combined together",
             "correct": False,
             "why": "Energy from separate sources does not cancel; it "
                    "adds together in the greenhouse."},
            {"text": "Flawed — only the largest single heater in the group actually contributes anything, the smaller ones being too weak",
             "correct": False,
             "why": "Every heater contributes, however small "
                    "individually; none of the smaller ones contributes "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h25",
        "band": "harder",
        "text": "Two sealed flasks of water, A at 80 °C and B at 20 °C, "
                "are connected by a metal rod so that energy can pass "
                "between them but nothing can escape to the room. "
                "Eventually, what is true?",
        "options": [
            {"text": "Flask A stays at 80 °C for ever, because it started hottest and a sealed flask locks that reading in",
             "correct": False,
             "why": "A cools as B warms, because energy passes from A "
                    "into B through the rod until they match."},
            {"text": "Flask B cools further below 20 °C as its own coldness is drawn out and gathered at the far end of the rod",
             "correct": False,
             "why": "There is no coldness to draw out of B; only energy "
                    "passes into it from A."},
            {"text": "Both flasks always settle at the same shared final temperature, somewhere between 20 °C and 80 °C",
             "correct": True},
            {"text": "Energy actually stops moving completely as soon as the rod is first connected, so nothing changes at all",
             "correct": False,
             "why": "Connecting the rod is exactly what allows energy to "
                    "start moving between the two flasks."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h26",
        "band": "harder",
        "text": "A student calculates that mixing 4 kg of water at "
                "60 °C with 1 kg of water at 0 °C should give exactly "
                "48 °C. Check whether this is sensible, using the fact "
                "that the larger mass should dominate the result.",
        "options": [
            {"text": "Sensible — 48 °C is close to 60 °C, reflecting the "
                     "4 kg's larger share",
             "correct": True},
            {"text": "Not sensible — the answer should be exactly "
                     "halfway, at 30 °C",
             "correct": False,
             "why": "Halfway is only right when the two masses are "
                    "equal; here one is four times the other."},
            {"text": "Not sensible — the answer must be lower than "
                     "0 °C, since the smaller amount was colder",
             "correct": False,
             "why": "Mixing with a hotter, much larger amount can only "
                    "raise the final temperature above the cold "
                    "portion's own value, never below it."},
            {"text": "Not sensible — the two temperatures should simply "
                     "add up to 60 °C",
             "correct": False,
             "why": "Mixing temperatures never works by simple addition; "
                    "the result must lie between the two starting "
                    "values."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h27",
        "band": "harder",
        "text": "A hot metal block is dropped into a large tank of "
                "water and, after settling, both read 22 °C. A student "
                "says: “this proves the block and the water started at "
                "the same temperature.” Is that conclusion justified?",
        "options": [
            {"text": "Yes — a shared final temperature always means they started the same, since equal readings need equal starts",
             "correct": False,
             "why": "A shared final temperature only shows that "
                    "equilibrium has been reached; the starting "
                    "temperatures could have been very different."},
            {"text": "No — the block and the water can never possibly settle down and reach exactly the very same reading as each other",
             "correct": False,
             "why": "They plainly do reach the same reading, 22 °C, as "
                    "stated in the question."},
            {"text": "Yes — genuine thermal equilibrium is completely impossible unless the two objects started off perfectly identical",
             "correct": False,
             "why": "Thermal equilibrium is exactly what happens when "
                    "two different starting temperatures meet in the "
                    "middle; that is the whole point of this lesson."},
            {"text": "No — a shared final temperature only shows "
                     "equilibrium has been reached, not what either one "
                     "started at",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h28",
        "band": "harder",
        "text": "A scientist argues: “A thermometer left in a beaker of "
                "water for one second gives an unreliable reading, but "
                "the same thermometer left in the same beaker for ten "
                "minutes gives a reliable one, because in ten minutes "
                "thermal equilibrium has been reached between the "
                "thermometer and the water.” Evaluate this reasoning.",
        "options": [
            {"text": "Sound — a brief dip genuinely has not let the thermometer and the water reach a shared temperature yet",
             "correct": True},
            {"text": "Flawed — thermometers read correctly the instant they touch a liquid, with no settling time needed at all",
             "correct": False,
             "why": "A thermometer needs time in contact with the liquid "
                    "before it settles at the liquid's own temperature."},
            {"text": "Flawed — ten minutes is never enough time to reach equilibrium in any liquid, however small the thermometer is",
             "correct": False,
             "why": "Ten minutes is easily enough time for a small "
                    "thermometer and a beaker of water to settle to the "
                    "same reading."},
            {"text": "Flawed — a thermometer's own reading genuinely has nothing whatsoever to do with the water's actual temperature",
             "correct": False,
             "why": "A thermometer works precisely by reaching the same "
                    "temperature as whatever it is placed in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h29",
        "band": "harder",
        "text": "A student claims that because energy is conserved, a "
                "room with a heater running non-stop must eventually "
                "reach an infinitely high temperature. Where does this "
                "argument go wrong?",
        "options": [
            {"text": "It ignores that the room also loses energy to its "
                     "surroundings, so it settles once the loss matches "
                     "the heater's supply",
             "correct": True},
            {"text": "It goes wrong because energy stops being conserved once a heater is switched on, so extra energy appears from nowhere",
             "correct": False,
             "why": "Energy is conserved throughout; the flaw lies "
                    "elsewhere, in ignoring the room's own losses."},
            {"text": "It goes wrong because a room genuinely cannot gain any energy whatsoever at all from a heater that is merely switched on inside it",
             "correct": False,
             "why": "A room certainly does gain energy from a running "
                    "heater; the flaw is somewhere else."},
            {"text": "It goes wrong because every single mains heater eventually runs out of the ability to keep on supplying fresh energy for ever",
             "correct": False,
             "why": "A mains heater does not run out this way; the room "
                    "settling is about losses balancing gains, not the "
                    "heater failing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h30",
        "band": "harder",
        "text": "A tank at 20 °C has a 50 °C heating coil switched on "
                "inside it, and at the same time the tank is losing "
                "energy to a cold room outside. A technician predicts "
                "the tank's temperature will keep rising for ever while "
                "the coil is on. Assess this prediction.",
        "options": [
            {"text": "Correct, since a hotter heating coil always drives the tank's own temperature up continuously and without any real limit at all whatsoever",
             "correct": False,
             "why": "As the tank warms, the flow from the coil weakens "
                    "and the loss to the room grows, so the rise cannot "
                    "continue for ever."},
            {"text": "Likely wrong — as the tank approaches the coil's "
                     "own temperature, the net gain shrinks and a steady "
                     "temperature is reached",
             "correct": True},
            {"text": "Correct, because energy genuinely cannot ever be lost from a tank at all once the heating coil has been switched on inside it",
             "correct": False,
             "why": "The tank loses energy to the cold room throughout, "
                    "whether or not the coil is on."},
            {"text": "Wrong, because the heating coil completely and permanently stops working the very instant the tank's own temperature actually passes 20 °C",
             "correct": False,
             "why": "Nothing about the coil stops it working at 20 °C; "
                    "it keeps supplying energy as long as it is switched "
                    "on."},
        ],
        "figure": None,
    },
]
