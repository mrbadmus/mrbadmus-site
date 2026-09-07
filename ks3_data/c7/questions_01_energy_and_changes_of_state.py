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
        "text": "Two blocks of the same metal are at 20 °C. One has twice "
                "the mass of the other. What can you say about the energy "
                "each one holds?",
        "options": [
            {"text": "They hold the same energy, because they are at the same "
                     "temperature", "correct": False,
             "why": "A thermometer is not an energy meter. It reports the "
                    "particles' average kinetic energy, not how many there "
                    "are."},
            {"text": "The lighter one holds more, because its particles are "
                     "less crowded and move more freely", "correct": False,
             "why": "Both are at the same temperature, so their particles "
                    "have the same average kinetic energy — same metal, so "
                    "the same average speed too. There are simply fewer of "
                    "them."},
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-01-e05",
        "band": "easier",
        "text": "What is a change of state?",
        "options": [
            {"text": "A substance going from solid to liquid, liquid to gas, "
                     "or the same journeys backwards",
             "correct": True},
            {"text": "A change in which the particles of a substance are "
                     "rearranged into a new substance with properties the old "
                     "one did not have",
             "correct": False,
             "why": "Making a new substance is a chemical change. A change of "
                    "state makes none"},
            {"text": "Any change that needs energy",
             "correct": False,
             "why": "Plenty of chemical reactions need energy too. This is "
                    "about solid, liquid and gas"},
            {"text": "A change that cannot be undone",
             "correct": False,
             "why": "Every change of state can be undone. Melt ice and freeze "
                    "it back"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e06",
        "band": "easier",
        "text": "What is the melting point of water?",
        "options": [
            {"text": "100 °C",
             "correct": False,
             "why": "That is the boiling point — where liquid becomes gas"},
            {"text": "0 °C",
             "correct": True},
            {"text": "It depends how much ice there is, because a larger "
                     "block takes longer to melt and so has to be taken "
                     "further above zero before it will start",
             "correct": False,
             "why": "More ice takes longer and melts at the same temperature. "
                    "Amount changes the time, never the point"},
            {"text": "−20 °C",
             "correct": False,
             "why": "That is a temperature ice can be at. It melts at 0 °C"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e07",
        "band": "easier",
        "text": "What is evaporating?",
        "options": [
            {"text": "A liquid changing to a gas throughout, with bubbles "
                     "forming inside it as well as at the surface, once it "
                     "has reached a high enough temperature",
             "correct": False,
             "why": "That is boiling. Evaporating happens at the surface, at "
                    "any temperature"},
            {"text": "A gas turning into a liquid",
             "correct": False,
             "why": "That is condensing, and it goes the other way"},
            {"text": "Particles escaping from the surface of a liquid and "
                     "becoming a gas",
             "correct": True},
            {"text": "A liquid soaking into a surface",
             "correct": False,
             "why": "Nothing is soaking in. The particles leave as a gas"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e08",
        "band": "easier",
        "text": "What does condensing do with energy?",
        "options": [
            {"text": "It takes energy in from the surroundings, which is why "
                     "a window feels cold where the mist is forming on it",
             "correct": False,
             "why": "The window feels cold because it IS cold, and that is "
                    "what makes the vapour condense. Condensing gives energy "
                    "OUT"},
            {"text": "It neither takes energy in nor gives it out",
             "correct": False,
             "why": "Then there would be no reason for steam to scald worse "
                    "than water at the same temperature"},
            {"text": "It destroys the energy the gas was carrying",
             "correct": False,
             "why": "Energy is never destroyed. It is transferred to whatever "
                    "the gas condenses on"},
            {"text": "It gives energy out — the same energy boiling took in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e09",
        "band": "easier",
        "text": "What does temperature measure?",
        "options": [
            {"text": "The average kinetic energy of the particles — the "
                     "energy they have because they are moving",
             "correct": True},
            {"text": "How much energy a substance contains altogether, which "
                     "is why a bathful of water at 40 °C is hotter than a cup "
                     "at the same reading",
             "correct": False,
             "why": "The bath and the cup are at the SAME temperature. The "
                    "bath holds more energy and is no hotter"},
            {"text": "How many particles are moving",
             "correct": False,
             "why": "That depends on how much substance there is. "
                    "Temperature does not"},
            {"text": "How fast a substance is heating up",
             "correct": False,
             "why": "That is a rate. Temperature is a reading at one moment"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e10",
        "band": "easier",
        "text": "Which of these gives energy OUT?",
        "options": [
            {"text": "Melting",
             "correct": False,
             "why": "Melting takes energy in — the particles have to be "
                    "pulled out of a fixed arrangement"},
            {"text": "Freezing",
             "correct": True},
            {"text": "Evaporating, because the particles that leave carry "
                     "their energy away with them and hand it to whatever "
                     "they land on next",
             "correct": False,
             "why": "They take energy FROM the liquid to escape, which is why "
                    "evaporation cools what is left behind"},
            {"text": "Boiling",
             "correct": False,
             "why": "Boiling takes in more energy than melting does"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e11",
        "band": "easier",
        "text": "Is a change of state a physical or a chemical change?",
        "options": [
            {"text": "Chemical, because a great deal of energy has to be "
                     "supplied and any change needing that much energy has "
                     "made something new",
             "correct": False,
             "why": "Energy is not the test. Melting ice takes energy and "
                    "leaves water, which is the same substance"},
            {"text": "Chemical, because the particles are rearranged",
             "correct": False,
             "why": "Rearranged in SPACE rather than joined differently. No "
                    "joins between atoms are broken"},
            {"text": "Physical, because no new substance is made",
             "correct": True},
            {"text": "Neither — it is not really a change at all",
             "correct": False,
             "why": "Ice and steam are plainly different. It is a change, and "
                    "a physical one"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e12",
        "band": "easier",
        "text": "What makes BOILING different from evaporating?",
        "options": [
            {"text": "Boiling makes a new substance out of the liquid, which "
                     "is the steam, whereas evaporating leaves the same "
                     "substance in the air above the puddle",
             "correct": False,
             "why": "Both give the same gas. Steam and water vapour are the "
                    "same substance"},
            {"text": "Boiling needs no energy",
             "correct": False,
             "why": "Boiling takes in a great deal — more than melting the "
                    "same mass"},
            {"text": "Boiling happens only in a kettle",
             "correct": False,
             "why": "Any liquid boils at its boiling point, in any container"},
            {"text": "Boiling happens throughout the liquid, with bubbles "
                     "forming inside it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e13",
        "band": "easier",
        "text": "Does the temperature of a substance depend on how much of it "
                "there is?",
        "options": [
            {"text": "No",
             "correct": True},
            {"text": "Yes, because more of it holds more energy and a "
                     "thermometer reads the energy that is there",
             "correct": False,
             "why": "More of it does hold more energy, and the thermometer "
                    "reads the AVERAGE per particle. That does not change"},
            {"text": "Only for a solid",
             "correct": False,
             "why": "It holds for all three states. Temperature is an average "
                    "however the particles are arranged"},
            {"text": "Only while it is being heated",
             "correct": False,
             "why": "Heating changes the temperature. It does not make the "
                    "reading depend on the amount"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c7-01-s05",
        "band": "standard",
        "text": "Sweating cools you down. Which change is doing it, and which "
                "way does the energy go?",
        "options": [
            {"text": "Evaporating, and the energy comes out of your skin",
             "correct": True},
            {"text": "Condensing, and the energy is given out to the air "
                     "rather than to your skin, which is why a breeze makes "
                     "the effect stronger",
             "correct": False,
             "why": "Nothing is condensing on you. Sweat EVAPORATES, and it "
                    "takes energy from your skin to do it"},
            {"text": "Evaporating, and the energy comes out of the air",
             "correct": False,
             "why": "Some comes from the air, and the reason you feel cooler "
                    "is that it is taken from your skin"},
            {"text": "Melting, and the energy comes out of your skin",
             "correct": False,
             "why": "Nothing solid is present. Sweat is already a liquid"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s06",
        "band": "standard",
        "text": "Ice at −20 °C is heated steadily. What happens before the "
                "first flat step on the curve?",
        "options": [
            {"text": "Nothing at all, because ice cannot take energy in until "
                     "it has reached the temperature at which it melts",
             "correct": False,
             "why": "It takes energy in from the first second, which is what "
                    "warms it from −20 °C to 0 °C"},
            {"text": "The ice warms up to 0 °C",
             "correct": True},
            {"text": "The ice melts slowly all the way from −20 °C",
             "correct": False,
             "why": "It melts at 0 °C and not below. Below that it simply "
                    "gets warmer"},
            {"text": "The ice gets colder before it warms",
             "correct": False,
             "why": "Nothing is taking energy out. It warms from the "
                    "start"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s07",
        "band": "standard",
        "text": "A thermometer in melting ice holds at 0 °C for six minutes. "
                "What would twice as much ice do?",
        "options": [
            {"text": "Hold at a lower temperature, because twice as much ice "
                     "in the beaker means twice as much cold in it for the "
                     "flame to work against",
             "correct": False,
             "why": "Cold is not a substance that can be doubled. The melting "
                    "point is 0 °C whatever the amount"},
            {"text": "Hold at 0 °C for the same six minutes",
             "correct": False,
             "why": "Twice as much ice needs twice as much energy to melt, "
                    "and the flame delivers it at the same rate"},
            {"text": "Hold at 0 °C for about twelve minutes",
             "correct": True},
            {"text": "Not hold at all, because the flame would be "
                     "overwhelmed",
             "correct": False,
             "why": "The plateau lasts longer rather than disappearing. The "
                    "flame is not in a race"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s08",
        "band": "standard",
        "text": "A wet towel over your shoulders feels cold on a hot day. "
                "Why?",
        "options": [
            {"text": "Because the water in it is colder than the air, so it "
                     "cools you by contact until the two reach the same "
                     "temperature",
             "correct": False,
             "why": "The towel is at air temperature within a minute and goes "
                    "on feeling cold. The cooling comes from evaporation"},
            {"text": "Because wet cloth conducts heat away faster than dry "
                     "cloth",
             "correct": False,
             "why": "It does conduct better, and that alone would stop once "
                    "you were both at the same temperature. Evaporation keeps "
                    "going"},
            {"text": "Because water holds the cold from the tap",
             "correct": False,
             "why": "Cold is not held or stored. What matters is energy being "
                    "taken away"},
            {"text": "Because water evaporating from it takes energy from you "
                     "and from the towel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s09",
        "band": "standard",
        "text": "Which takes more energy: melting 1 kg of ice at 0 °C, or "
                "warming 1 kg of water from 0 °C to 20 °C?",
        "options": [
            {"text": "Melting the ice",
             "correct": True},
            {"text": "Warming the water, because it is taken through twenty "
                     "whole degrees while the melting ice never moves off "
                     "zero at all",
             "correct": False,
             "why": "Not moving off zero is what makes melting so expensive. "
                    "The energy is separating particles instead"},
            {"text": "They take the same energy, because it is the same mass "
                     "of the same substance",
             "correct": False,
             "why": "Same mass and very different jobs. Separating particles "
                    "costs far more than speeding them up a little"},
            {"text": "It cannot be compared, because one changes state and "
                     "the other does not",
             "correct": False,
             "why": "Both can be measured in joules, which is exactly how "
                    "latent heat was discovered"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s10",
        "band": "standard",
        "text": "A drink with ice in it stays at 0 °C until the last cube has "
                "gone. Why does it not warm up gradually?",
        "options": [
            {"text": "Because ice at 0 °C is much colder than the drink, so "
                     "it holds the whole glass down until it has finished "
                     "cooling it",
             "correct": False,
             "why": "The ice is AT 0 °C, the same as the drink around it. "
                    "What holds the temperature is the melting"},
            {"text": "Because the melting ice absorbs energy while staying at "
                     "0 °C",
             "correct": True},
            {"text": "Because the drink cannot warm while there is anything "
                     "solid in it",
             "correct": False,
             "why": "A solid that is not melting would not hold it. It is the "
                    "change of state that does"},
            {"text": "Because the glass insulates the drink",
             "correct": False,
             "why": "A glass insulates poorly, and the same drink without ice "
                    "warms steadily"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s11",
        "band": "standard",
        "text": "Water boils at 100 °C, yet a puddle dries up at 8 °C. How?",
        "options": [
            {"text": "Because the ground under the puddle is warmer than the "
                     "air, so the water at the bottom of it does reach 100 °C "
                     "even on a cold day",
             "correct": False,
             "why": "Nothing outdoors reaches 100 °C. The water leaves "
                    "without boiling at all"},
            {"text": "Because the water soaks into the ground",
             "correct": False,
             "why": "A puddle on tarmac dries too, and one under a cover does "
                    "not. It is leaving as a gas"},
            {"text": "Because evaporation happens at the surface, at any "
                     "temperature",
             "correct": True},
            {"text": "Because the boiling point falls in the open air",
             "correct": False,
             "why": "It changes very little with altitude and not at all with "
                    "being outdoors"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s12",
        "band": "standard",
        "text": "During melting, what is the energy actually doing to the "
                "particles?",
        "options": [
            {"text": "Making them move faster, so they break out of the "
                     "arrangement",
             "correct": False,
             "why": "Moving faster is what raises the TEMPERATURE, and the "
                    "thermometer is not moving. The energy is separating "
                    "them"},
            {"text": "Making them larger",
             "correct": False,
             "why": "Particles never change size in any change of state"},
            {"text": "Destroying some of them, which is why the ice "
                     "disappears",
             "correct": False,
             "why": "None is destroyed. Weigh the beaker before and after and "
                    "it is unchanged"},
            {"text": "Separating them, against the forces attracting them to "
                     "each other",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s13",
        "band": "standard",
        "text": "A freezer has to keep working while water at 0 °C turns to "
                "ice at 0 °C. Why is there anything left to do?",
        "options": [
            {"text": "Because freezing gives energy out, and that energy has "
                     "to be taken away",
             "correct": True},
            {"text": "Because the water still has to be cooled below 0 °C "
                     "first",
             "correct": False,
             "why": "Water freezes AT 0 °C. What the freezer has to remove is "
                    "the energy the freezing gives out"},
            {"text": "Because the freezer is also cooling the air around the "
                     "tray",
             "correct": False,
             "why": "It is, and the tray would still need work done on it "
                    "even in a perfectly insulated box"},
            {"text": "Because water at 0 °C is not really at 0 °C",
             "correct": False,
             "why": "It is. Two things can be at the same temperature and one "
                    "of them still be giving energy out"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-01-h05",
        "band": "harder",
        "text": "Joseph Black worked out latent heat in the 1760s. Which "
                "everyday observation was he explaining?",
        "options": [
            {"text": "That ice in a warm room takes hours to melt while "
                     "staying at 0 °C the whole time",
             "correct": True},
            {"text": "That a kettle takes far longer to boil dry than it "
                     "takes to reach boiling in the first place, which is "
                     "something anybody who has burnt one out has noticed",
             "correct": False,
             "why": "That is the same idea at the other plateau, and it is "
                    "not the observation he started from. His was the ice"},
            {"text": "That a thermometer in melting ice reads 0 °C",
             "correct": False,
             "why": "That was already known. What needed explaining was why "
                    "it STAYED there for so long"},
            {"text": "That steam engines waste fuel",
             "correct": False,
             "why": "His idea went INTO the steam engine afterwards. It came "
                    "out of watching ice"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h06",
        "band": "harder",
        "text": "Latent heat means hidden heat. In what sense is it hidden?",
        "options": [
            {"text": "It is stored deep inside the substance where the "
                     "thermometer's bulb cannot reach, so a longer thermometer "
                     "would find it",
             "correct": False,
             "why": "No thermometer of any length finds it. It is not a "
                    "question of where the bulb is"},
            {"text": "A thermometer cannot see it — the energy goes in and "
                     "the reading does not move",
             "correct": True},
            {"text": "It is released only later, so it is hidden in time",
             "correct": False,
             "why": "It is released later on freezing, and hidden refers to "
                    "the thermometer not registering it as it goes in"},
            {"text": "It is too small an amount to measure",
             "correct": False,
             "why": "It is enormous — melting ice takes far more energy than "
                    "warming the water afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h07",
        "band": "harder",
        "text": "A drink with ice starts warming the moment the last cube "
                "disappears. Why the sudden change?",
        "options": [
            {"text": "Because the ice was the coldest thing in the glass, and "
                     "once it has gone there is nothing left below the "
                     "drink's temperature to cool it",
             "correct": False,
             "why": "The ice was AT the drink's temperature. What has stopped "
                    "is the melting, which was absorbing energy"},
            {"text": "Because the melted ice warms faster than the drink",
             "correct": False,
             "why": "It warms at the same rate as the rest of the liquid. It "
                    "is now just more drink"},
            {"text": "Because nothing is absorbing energy at a fixed "
                     "temperature any more",
             "correct": True},
            {"text": "Because the glass has warmed up by then",
             "correct": False,
             "why": "The glass warms gradually throughout. The change at the "
                    "last cube is sharp"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h08",
        "band": "harder",
        "text": "Identical flames heat 100 g and 200 g of ice, both at 0 °C. "
                "Compare what the two thermometers do.",
        "options": [
            {"text": "The 200 g one reads lower throughout, because there is "
                     "more ice",
             "correct": False,
             "why": "Both read 0 °C while ice remains. Amount changes how "
                    "long, never the reading"},
            {"text": "Both hold at 0 °C for the same time",
             "correct": False,
             "why": "Twice the ice needs twice the energy, so it holds for "
                    "about twice as long"},
            {"text": "Neither holds, because the flames are equal",
             "correct": False,
             "why": "Both hold. The plateau is a property of the melting, not "
                    "of the flame"},
            {"text": "Both hold at 0 °C, and the 100 g beaker starts rising "
                     "sooner",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h09",
        "band": "harder",
        "text": "A student says a thermometer tells you how much energy "
                "something has. Which single comparison settles it?",
        "options": [
            {"text": "A bathful of water and a cup of water, both at 40 °C",
             "correct": True},
            {"text": "Ice at 0 °C and water at 0 °C, which read the same and "
                     "behave completely differently when they are put next to "
                     "a plate of food",
             "correct": False,
             "why": "A good pair, and it needs the idea of latent heat to "
                    "explain. The bath and the cup settle it with nothing but "
                    "size"},
            {"text": "Boiling water and a Bunsen flame",
             "correct": False,
             "why": "Those are at different temperatures, so they do not "
                    "isolate the point"},
            {"text": "Two identical cups of water at 40 °C",
             "correct": False,
             "why": "Identical in both respects, so nothing is compared"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h10",
        "band": "harder",
        "text": "A cool box could be packed with ice at 0 °C or with dry ice "
                "at −78 °C. A student says the dry ice must always win because "
                "it is colder. What is missing?",
        "options": [
            {"text": "Whether the box is insulated well enough to hold a "
                     "temperature that far below freezing without the walls "
                     "themselves being damaged by it",
             "correct": False,
             "why": "A practical worry, and not the chemistry. The question "
                    "is what each pack absorbs while it changes state"},
            {"text": "How much energy each absorbs as it changes state, not "
                     "only how cold it starts",
             "correct": True},
            {"text": "Nothing — colder always keeps food cold for longer",
             "correct": False,
             "why": "Temperature is only half the story. A pack that absorbs "
                    "little energy warms through quickly"},
            {"text": "Whether the food would freeze",
             "correct": False,
             "why": "A real design problem, and it does not answer which pack "
                    "lasts longer"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h11",
        "band": "harder",
        "text": "During a plateau the energy is still going in and the "
                "thermometer does not move. Why is the thermometer not simply "
                "wrong?",
        "options": [
            {"text": "Because the thermometer is measuring the water rather "
                     "than the ice",
             "correct": False,
             "why": "Both are at 0 °C, and a thermometer in either reads the "
                    "same. Nothing is being missed"},
            {"text": "Because the energy is being lost to the room instead",
             "correct": False,
             "why": "Some is always lost, before and after the plateau alike. "
                    "It cannot explain a step that appears only during "
                    "melting"},
            {"text": "Because temperature measures how fast the particles "
                     "move, and the energy is going into separating them "
                     "instead",
             "correct": True},
            {"text": "Because the thermometer takes time to respond",
             "correct": False,
             "why": "A plateau lasting minutes is far longer than any lag. "
                    "The reading is genuinely constant"},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h12",
        "band": "harder",
        "text": "Equal masses of ice at 0 °C and water at 0 °C are left in "
                "identical warm rooms. Which reaches room temperature first?",
        "options": [
            {"text": "The ice, because a solid warms faster than a liquid",
             "correct": False,
             "why": "The ice has to melt first, and melting absorbs a great "
                    "deal of energy at a constant 0 °C"},
            {"text": "Both together, because they start at the same "
                     "temperature and the rooms are identical in every "
                     "respect",
             "correct": False,
             "why": "Same start and same room, and the ice has an extra job "
                    "to do before its temperature can rise at all"},
            {"text": "Neither — they never reach room temperature",
             "correct": False,
             "why": "Both do, given time. One takes far longer"},
            {"text": "The water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h13",
        "band": "harder",
        "text": "Melting a kilogram of ice takes more energy than heating a "
                "kilogram of water from 0 °C to 70 °C. Why is melting still "
                "called a PHYSICAL change?",
        "options": [
            {"text": "Because no new substance is made — how much energy it "
                     "takes is not the test",
             "correct": True},
            {"text": "Because the energy is given back when it freezes, and a "
                     "change that returns its energy has not made anything "
                     "permanent",
             "correct": False,
             "why": "A reversible energy transfer is not the test either. "
                    "Some chemical reactions reverse too"},
            {"text": "Because the temperature does not change during it",
             "correct": False,
             "why": "That is a consequence of where the energy goes, and it "
                    "is not what makes a change physical"},
            {"text": "Because water and ice are different substances",
             "correct": False,
             "why": "They are the same substance in two states, which is "
                    "exactly why it is physical"},
        ],
        "figure": None,
    },
]
