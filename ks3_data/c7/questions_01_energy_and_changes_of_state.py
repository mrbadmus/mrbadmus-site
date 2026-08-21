"""C7 lesson 01 — Energy and changes of state: twelve questions (MRB-272).

The lesson's argument is one shape: energy goes in or comes out at every change
of state, and while the change is happening the thermometer does not move
because the energy is separating particles rather than speeding them up. The
page teaches it by stepping a heating curve one minute at a time, so these
twelve probe the angles the mastery ladder leaves alone — the flat step read as
a pause, the thermometer read as an energy meter, and the two directions of
transfer applied to things that are not beakers.

The distractors are built from the lesson's two declared misconceptions.

`ENER-01` (while ice is melting it has stopped absorbing heat) drives the wrong
options in e02, s01, s03 and h01. Each treats the flat step as an interruption —
the flame stopped, the ice stopped taking energy, the thermometer is broken.
s03 is the one that matters: it asks what would happen if the flame were turned
UP, where the belief predicts something the apparatus flatly refuses to do.

`ENER-02` (a thermometer measures how much energy something has) drives e03,
s02, h02 and h04, where two things at the same temperature are treated as
carrying the same energy. h02 is the register's own case put as a burn, which
is where a student actually meets it.

A third strand, everywhere on the page and in neither register entry, is that
freezing must take energy in because ice is cold. e04, s04 and h03 are built on
it: h03 uses the orange growers, where the belief predicts that spraying water
on a crop in a frost would make things worse.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each and C7's four banks hold
twelve of each. Authored level from the start rather than rebalanced
afterwards.

Every question here is new prose — a question bank is the one place in these
files where that is true — and the bar is §13's: each distractor is a WRONG
RULE in the correct answer's own shape, at the correct answer's own length, and
each is a mistake a real student actually makes.
"""

UNIT = "C7"
LESSON = "energy-and-changes-of-state"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-01-e01",
        "band": "easier",
        "text": "Which of these changes of state takes energy IN from the "
                "surroundings?",
        "options": [
            {"text": "Melting, because the particles have to be pulled out of "
                     "a fixed arrangement", "correct": True},
            {"text": "Freezing, because the particles have to be forced into "
                     "a fixed arrangement", "correct": False,
             "why": "Freezing gives energy out. The particles fall together "
                    "under the forces attracting them and release what was "
                    "holding them apart."},
            {"text": "Condensing, because the gas has to be squeezed back "
                     "into a smaller space", "correct": False,
             "why": "Condensing gives energy out too. Nothing is squeezing "
                    "the gas — the particles slow enough for the attractions "
                    "to pull them together."},
            {"text": "Cooling a liquid, because taking heat away is still a "
                     "kind of energy change", "correct": False,
             "why": "Cooling takes energy out, not in — and cooling a liquid "
                    "is not a change of state at all until it reaches its "
                    "freezing point."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e02",
        "band": "easier",
        "text": "A beaker of ice and water is heated with a steady flame. For "
                "several minutes the thermometer stays at 0 °C. What is the "
                "flame doing during those minutes?",
        "options": [
            {"text": "Nothing, because a substance cannot take in heat at its "
                     "melting point", "correct": False,
             "why": "It can, and it is taking in more than at any other point "
                    "in the run. Melting is the most energy-hungry part of "
                    "heating a beaker of ice."},
            {"text": "Still delivering energy at exactly the same rate as "
                     "before", "correct": True},
            {"text": "Delivering less energy, which is why the reading has "
                     "stopped climbing", "correct": False,
             "why": "Nothing was done to the flame. The reading stopped for a "
                    "reason inside the beaker, not a reason inside the "
                    "Bunsen."},
            {"text": "Delivering energy that is being destroyed as the ice "
                     "melts", "correct": False,
             "why": "Energy is never destroyed. It is stored in the "
                    "separated particles, where a thermometer cannot read "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e03",
        "band": "easier",
        "text": "Steam at 100 °C and water at 100 °C are both put in contact "
                "with your skin. Which statement is true?",
        "options": [
            {"text": "They are at the same temperature and carry the same "
                     "energy", "correct": False,
             "why": "Same temperature, very different energy. The steam also "
                    "carries everything that went into boiling it."},
            {"text": "The steam is at a higher temperature, which is why it "
                     "burns worse", "correct": False,
             "why": "Both are at 100 °C — a thermometer cannot tell them "
                    "apart. Temperature is not what separates them."},
            {"text": "They are at the same temperature but the steam carries "
                     "far more energy", "correct": True},
            {"text": "The water carries more energy, because a liquid is "
                     "denser than a gas", "correct": False,
             "why": "Density is not energy. The steam holds all the energy "
                    "that boiling put into it and releases it into your skin "
                    "as it condenses."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e04",
        "band": "easier",
        "text": "What happens to the energy when a puddle of water freezes "
                "overnight?",
        "options": [
            {"text": "It is taken in from the air, which is why freezing "
                     "needs a cold night", "correct": False,
             "why": "Freezing gives energy out. A cold night is what lets "
                    "that energy escape, not what supplies it."},
            {"text": "It is destroyed, because the water stops moving once it "
                     "is solid", "correct": False,
             "why": "Energy is never destroyed, and the particles in ice have "
                    "not stopped — they vibrate in fixed positions."},
            {"text": "It stays exactly where it is, because nothing was "
                     "heated or cooled", "correct": False,
             "why": "Something was cooled: the puddle. Energy left it, which "
                    "is why it could freeze at all."},
            {"text": "It is given out to the surroundings as the particles "
                     "fall into a fixed arrangement", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-01-s01",
        "band": "standard",
        "text": "On a heating curve for ice, why is there a flat step at 0 °C "
                "and a much longer flat step at 100 °C?",
        "options": [
            {"text": "Because the flame is turned down for the changes of "
                     "state and up again afterwards", "correct": False,
             "why": "The flame is never touched. The flat steps are produced "
                    "by what the energy is being spent on inside the beaker."},
            {"text": "Because the energy is separating particles, and pulling "
                     "them fully apart takes far more than loosening them",
             "correct": True},
            {"text": "Because water can only absorb heat at certain "
                     "temperatures, and 0 °C and 100 °C are two of them",
             "correct": False,
             "why": "Water absorbs energy at every temperature in the run. "
                    "What changes at 0 °C and 100 °C is what the energy is "
                    "spent on."},
            {"text": "Because the thermometer cannot respond quickly enough "
                     "while a change of state is happening", "correct": False,
             "why": "The thermometer is working perfectly. Leave it there for "
                    "an hour and it still reads 0 °C while ice remains."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s02",
        "band": "standard",
        "text": "A cool box is packed with 1 kg of ice at 0 °C. The same box "
                "could have been packed with 1 kg of water at 0 °C. Why does "
                "the ice keep the food cold for longer?",
        "options": [
            {"text": "Because ice is colder than water, so it starts the job "
                     "with an advantage", "correct": False,
             "why": "Both start at 0 °C. Temperature alone cannot explain the "
                    "difference, which is exactly what makes this "
                    "interesting."},
            {"text": "Because solid ice is denser, so there is more of it in "
                     "the same space", "correct": False,
             "why": "Ice is actually less dense than water, and in any case "
                    "both are 1 kg. Mass is the thing being compared."},
            {"text": "Because the ice must absorb a great deal of energy "
                     "before it can melt, and it takes that from the food",
             "correct": True},
            {"text": "Because water conducts heat into the food faster than "
                     "ice does", "correct": False,
             "why": "Conduction is not the point here. The ice is a store "
                    "that has to be paid for in energy before it can warm "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s03",
        "band": "standard",
        "text": "A student turns the Bunsen up while ice is melting in the "
                "beaker. What happens to the reading on the thermometer?",
        "options": [
            {"text": "It climbs above 0 °C, because more energy means a "
                     "higher temperature", "correct": False,
             "why": "It cannot, while ice is still there. The extra energy "
                    "melts the ice faster; it does not raise the "
                    "temperature."},
            {"text": "It falls, because the ice is now melting faster and "
                     "melting is a cooling process", "correct": False,
             "why": "Nothing falls. The mixture stays at its melting point "
                    "for as long as both solid and liquid are present."},
            {"text": "It stays at 0 °C and the ice takes exactly as long as "
                     "before to melt", "correct": False,
             "why": "The reading holds, but a bigger flame delivers more "
                    "energy per minute, so the melting finishes sooner."},
            {"text": "It stays at 0 °C, but the ice disappears sooner",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s04",
        "band": "standard",
        "text": "Why does the water coming out of a fridge freezer feel cold "
                "while the grille at the back feels warm?",
        "options": [
            {"text": "Because energy taken out of the food has to go "
                     "somewhere, and the grille is where it is released",
             "correct": True},
            {"text": "Because the fridge makes cold at the front and heat at "
                     "the back, from two separate systems", "correct": False,
             "why": "There is no such thing as making cold. A fridge moves "
                    "energy out of the food and dumps it at the back."},
            {"text": "Because the motor at the back is hot and the cold "
                     "inside has nothing to do with it", "correct": False,
             "why": "The motor does warm, but most of the heat at the grille "
                    "is the energy that came out of the food."},
            {"text": "Because cold air is heavier, so it sinks to the front "
                     "and the heat rises behind", "correct": False,
             "why": "This is about energy being transferred, not about air "
                    "moving. Nothing cold has been produced anywhere."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-01-h01",
        "band": "harder",
        "text": "A pan of water is left boiling on a hob for ten minutes. A "
                "student says the water must be getting hotter and hotter "
                "because the hob has been on the whole time. What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong — boiling water does keep climbing "
                     "above 100 °C in a pan", "correct": False,
             "why": "It does not, while liquid water remains. The reading "
                    "holds at the boiling point for the whole ten minutes."},
            {"text": "The hob stops delivering energy once the water reaches "
                     "boiling point", "correct": False,
             "why": "The hob does nothing different. Energy goes in at the "
                    "same rate for the whole ten minutes."},
            {"text": "The energy is turning liquid into steam rather than "
                     "raising the temperature, so the reading holds",
             "correct": True},
            {"text": "The steam leaving the pan carries the heat away so "
                     "fast that the water cannot warm up", "correct": False,
             "why": "The steam does carry the energy away, but the reason the "
                    "reading holds is that the energy is being spent making "
                    "steam in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h02",
        "band": "harder",
        "text": "Two identical blocks of metal are at 20 °C. One has twice "
                "the mass of the other. What can you say about the energy "
                "each one holds?",
        "options": [
            {"text": "They hold the same energy, because they are at the same "
                     "temperature", "correct": False,
             "why": "A thermometer is not an energy meter. It reports how "
                    "fast the particles move, not how many there are."},
            {"text": "The lighter one holds more, because its particles are "
                     "less crowded and move more freely", "correct": False,
             "why": "Both are at the same temperature, so their particles "
                    "move at the same average speed. There are simply fewer "
                    "of them."},
            {"text": "Nothing can be said, because energy cannot be compared "
                     "between two separate objects", "correct": False,
             "why": "It can be compared, and the comparison is "
                    "straightforward: twice the particles at the same speed "
                    "is twice the energy."},
            {"text": "The heavier one holds more, because there are twice as "
                     "many particles moving at that speed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h03",
        "band": "harder",
        "text": "Orange growers spray their trees with water when a frost is "
                "forecast, and it protects the fruit. Which explanation is "
                "correct?",
        "options": [
            {"text": "As the sprayed water freezes it releases energy, "
                     "holding the fruit at 0 °C rather than colder",
             "correct": True},
            {"text": "The layer of water freezes and seals the fruit away "
                     "from the cold air completely", "correct": False,
             "why": "A shell of ice is not an insulator against a hard frost. "
                    "What protects the fruit is the energy freezing releases "
                    "while it forms."},
            {"text": "Wet fruit freezes at a lower temperature than dry "
                     "fruit, so the frost cannot reach it", "correct": False,
             "why": "Wetting the fruit does not change what temperature its "
                    "own contents freeze at."},
            {"text": "The water absorbs the cold from the air before the cold "
                     "can reach the fruit", "correct": False,
             "why": "Cold is not a substance and cannot be absorbed. Energy "
                    "moves; nothing else does."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h04",
        "band": "harder",
        "text": "Two beakers of water are heated by identical flames. Beaker "
                "A goes from 20 °C to 40 °C in two minutes. Beaker B is "
                "already boiling and stays at 100 °C for those two minutes. "
                "Which beaker received more energy?",
        "options": [
            {"text": "Beaker A, because its temperature rose and beaker B's "
                     "did not", "correct": False,
             "why": "A rising reading is not a measure of energy received. "
                    "Both beakers sat under identical flames for the same "
                    "time."},
            {"text": "They received the same energy, because the flames and "
                     "the times were identical", "correct": True},
            {"text": "Beaker B, because boiling water is hotter than water at "
                     "40 °C", "correct": False,
             "why": "How hot the water already was does not change how much "
                    "the flame delivered in two minutes."},
            {"text": "It cannot be worked out without knowing how much water "
                     "is in each beaker", "correct": False,
             "why": "The volumes would matter for the temperature RISE. The "
                    "energy DELIVERED is set by the flame and the time, and "
                    "both are the same."},
        ],
        "figure": None,
    },
]
