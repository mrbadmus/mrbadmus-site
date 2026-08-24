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

The lesson carries no figures, so every question is figure=None.
"""

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
                    "Temperature is about particle speed."},
            {"text": "How quickly a substance will warm something else that "
                     "it touches",
             "correct": False,
             "why": "That is a rate, and it depends on the material as well. "
                    "Temperature is simpler than that."},
            {"text": "The average speed of the particles in a substance",
             "correct": True},
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
            {"text": "The hotter one runs out of the energy it had to give "
                     "away to the other",
             "correct": False,
             "why": "It never runs out. Both objects still hold plenty when "
                    "the transfer stops."},
            {"text": "The colder one becomes completely full and can accept "
                     "no more energy",
             "correct": False,
             "why": "There is no upper limit to fill. A store is not a "
                    "container with a brim."},
            {"text": "The surrounding air removes the difference between the "
                     "two of them",
             "correct": False,
             "why": "The air affects both, but the transfer between them "
                    "stops for a reason of its own."},
            {"text": "They reach the same temperature, so there is no longer "
                     "a difference to drive it",
             "correct": True},
        ],
        "figure": None,
    },
]
