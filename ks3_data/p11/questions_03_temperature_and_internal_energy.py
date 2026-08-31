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
            {"text": "Twice as much for the 500 g mug", "correct": True},
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
]
