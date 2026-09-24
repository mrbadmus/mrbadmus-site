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
            {"text": "A change that cannot be undone once it has happened, "
                     "whatever you do to the substance afterwards",
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
            {"text": "A liquid soaking into the surface it is resting on and "
                     "disappearing down inside it",
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
            {"text": "It neither takes energy in nor gives any of it out at "
                     "any point in the change",
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
            {"text": "How fast a substance is heating up, so a reading that is "
                     "climbing quickly must mean a high temperature",
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
            {"text": "Boiling happens only in a kettle, and never in any other "
                     "container in a laboratory",
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
            {"text": "Because wet cloth conducts heat away from your skin a "
                     "great deal faster than dry cloth",
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
            {"text": "Because the boiling point of water falls once it is out "
                     "in the open air like that",
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
            {"text": "That a thermometer standing in a beaker of melting ice "
                     "reads exactly 0 °C and not some other value",
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
            {"text": "It is released only later on, so it is hidden in time "
                     "rather than hidden from the thermometer",
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
            {"text": "Because the melted ice warms up faster than the rest of "
                     "the drink around it does",
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
            {"text": "Two identical cups of water, both of them at 40 °C, side "
                     "by side",
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
            {"text": "Nothing at all — a colder pack always keeps food cold "
                     "for longer than any warmer one does",
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
            {"text": "Because the temperature does not change at any point "
                     "during the whole of the melting itself",
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

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "c7-01-e14",
        "band": "easier",
        "text": "While a substance is changing state, what does its "
                "temperature do?",
        "options": [
            {"text": "It stays constant until the change is finished",
             "correct": True},
            {"text": "It rises more slowly than it did before",
             "correct": False,
             "why": "It does not rise at all. A slower rise would still be a "
                    "rise, and the thermometer does not move."},
            {"text": "It falls while the particles are being separated",
             "correct": False,
             "why": "Nothing is taken away from the substance during melting "
                    "or boiling, so there is no reason for it to fall."},
            {"text": "It rises in small steps, one for each state",
             "correct": False,
             "why": "The flat parts of a heating curve are level, not "
                    "stepped. The reading holds at one value."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e15",
        "band": "easier",
        "text": "Water in a beaker is boiling and bubbles are forming inside "
                "the liquid. What is inside those bubbles?",
        "options": [
            {"text": "Air that was dissolved in the water", "correct": False,
             "why": "Dissolved air comes out in small bubbles long before "
                    "boiling, and it runs out. Boiling does not."},
            {"text": "Water that has turned into a gas", "correct": True},
            {"text": "Nothing — they are empty spaces",
             "correct": False,
             "why": "A bubble is a pocket of gas. Boiling is the liquid "
                    "turning to gas throughout, and that gas fills them."},
            {"text": "Oxygen and hydrogen split out of the water",
             "correct": False,
             "why": "Splitting water into its elements is a chemical change. "
                    "Boiling makes no new substance at all."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e16",
        "band": "easier",
        "text": "Steam that has been heated above 100 °C is given a special "
                "name. What is it?",
        "options": [
            {"text": "Saturated steam", "correct": False,
             "why": "Saturated describes steam sitting at its boiling point, "
                    "not steam that has been taken past it."},
            {"text": "Condensed steam", "correct": False,
             "why": "Condensing is the gas turning back into a liquid, which "
                    "is the opposite journey."},
            {"text": "Superheated steam", "correct": True},
            {"text": "Latent steam", "correct": False,
             "why": "Latent describes the energy a change of state hides from "
                    "a thermometer. It is not a kind of steam."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e17",
        "band": "easier",
        "text": "About how many times more energy does it take to boil a "
                "kilogram of water than to melt a kilogram of ice?",
        "options": [
            {"text": "About twice as much", "correct": False,
             "why": "Far too small. Twice would make the boiling step only "
                    "twice as long, and it is much longer than that."},
            {"text": "About the same amount", "correct": False,
             "why": "Then both flat steps would last the same time, and the "
                    "boiling one is plainly the longer of the two."},
            {"text": "About a hundred times as much", "correct": False,
             "why": "Far too large. A hundredfold gap would make boiling a "
                    "pan dry take most of a day on a hob."},
            {"text": "About seven times as much", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "c7-01-s14",
        "band": "standard",
        "text": "A pan of water takes about four minutes to reach 100 °C on "
                "a hob, and about half an hour to boil dry. Why is the second "
                "stage so much slower?",
        "options": [
            {"text": "Because turning the water into steam takes far more "
                     "energy than warming it did", "correct": True},
            {"text": "Because the hob delivers energy more slowly once the "
                     "water has reached 100 °C", "correct": False,
             "why": "The hob setting has not changed, so it is delivering "
                    "energy at the same rate throughout."},
            {"text": "Because a hot pan loses heat to the kitchen faster "
                     "than the hob can supply it", "correct": False,
             "why": "If that were true the water would cool rather than boil "
                    "away. Some heat is lost, but the pan keeps boiling."},
            {"text": "Because water cannot get hotter than 100 °C, so the "
                     "heating has nothing left to do", "correct": False,
             "why": "The heating still has a great deal to do — it is "
                    "separating the particles into a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s15",
        "band": "standard",
        "text": "Water vapour in a steamy bathroom condenses on a cold "
                "mirror. What happens to the energy as it condenses?",
        "options": [
            {"text": "It is taken in from the mirror, which is what makes "
                     "the mirror cold", "correct": False,
             "why": "The mirror was already cold before anything condensed "
                    "on it, and condensing gives energy out rather than "
                    "taking it in."},
            {"text": "It is given out to the mirror and the air touching it",
             "correct": True},
            {"text": "It is held in the droplets until they dry off again",
             "correct": False,
             "why": "Drying takes MORE energy in. The energy that condensing "
                    "released has already gone into the surroundings."},
            {"text": "It is destroyed, because the vapour stops existing",
             "correct": False,
             "why": "The vapour has not stopped existing — it is the water "
                    "now sitting on the glass — and energy is never "
                    "destroyed."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s16",
        "band": "standard",
        "text": "A heating curve printed in a revision guide is labelled "
                "“schematic — not to scale”. What is that label "
                "warning you about?",
        "options": [
            {"text": "That the temperatures marked on it are guesses rather "
                     "than real values", "correct": False,
             "why": "The temperatures are real: water does melt at 0 °C and "
                    "boil at 100 °C. It is the lengths that are not to "
                    "scale."},
            {"text": "That the shape is wrong, so nothing on it can be "
                     "trusted at all", "correct": False,
             "why": "The shape is the whole point of the drawing, and it is "
                    "right — two flat steps with rises between them."},
            {"text": "That the lengths of the steps show the pattern rather "
                     "than measured times", "correct": True},
            {"text": "That it describes one particular substance and cannot "
                     "apply to another", "correct": False,
             "why": "Every substance gives a curve of this shape; only the "
                    "two temperatures change. A scale warning is not about "
                    "that."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s17",
        "band": "standard",
        "text": "A sample of water is heated steadily all the way from solid "
                "at −20 °C to gas at 120 °C. How many flat steps and how "
                "many rising sections does the graph of its temperature "
                "have?",
        "options": [
            {"text": "One flat step and two rising sections", "correct": False,
             "why": "That misses one of the two changes of state. Melting "
                    "and boiling each give a flat step of their own."},
            {"text": "Three flat steps and two rising sections",
             "correct": False,
             "why": "There are only two changes of state on this journey, so "
                    "there can only be two flat steps."},
            {"text": "Two flat steps and two rising sections",
             "correct": False,
             "why": "That forgets one rise. The solid warms, the liquid "
                    "warms, and the gas warms — three rises in all."},
            {"text": "Two flat steps and three rising sections",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ────────────────────────────────────────
    {
        "id": "c7-01-h14",
        "band": "harder",
        "text": "A power station boils water and sends steam to its turbine "
                "rather than pumping very hot liquid water there. Why is "
                "steam so much better at carrying the energy?",
        "options": [
            {"text": "Because boiling put a great deal of extra energy into "
                     "it that water at 100 °C does not carry",
             "correct": True},
            {"text": "Because a gas cannot lose any energy to its "
                     "surroundings while it is travelling along a pipe",
             "correct": False,
             "why": "Steam pipes are lagged precisely because a gas does "
                    "lose energy on the way. That is a problem, not a "
                    "reason."},
            {"text": "Because steam weighs far less than water does, so it "
                     "arrives at the turbine much sooner", "correct": False,
             "why": "Arriving sooner is not the same as carrying more "
                    "energy, and a lighter substance does not carry more."},
            {"text": "Because the energy is created inside the boiler at the "
                     "moment the water turns into steam", "correct": False,
             "why": "Nothing creates energy. The boiler transfers it from "
                    "the fuel into the water."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h15",
        "band": "harder",
        "text": "The melting point of water and the freezing point of water "
                "are the same temperature. Why must that be so?",
        "options": [
            {"text": "Because a thermometer is not sensitive enough to "
                     "separate two values that close together",
             "correct": False,
             "why": "They are not two close values that an instrument "
                    "confuses. They are one temperature."},
            {"text": "Because they are one change run in opposite "
                     "directions, so they turn at the same point",
             "correct": True},
            {"text": "Because 0 °C is the coldest that liquid water is "
                     "physically able to become", "correct": False,
             "why": "How cold water can get is a different question "
                    "altogether, and it is not what fixes the two points "
                    "together."},
            {"text": "Because pure water always holds a little ice in it, "
                     "whatever its temperature", "correct": False,
             "why": "Water well above 0 °C holds no ice at all, and the two "
                    "points would still match if it did."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h16",
        "band": "harder",
        "text": "A beaker of water is boiled until the last of the liquid "
                "has gone. Where is the energy the flame supplied during the "
                "flat step at 100 °C?",
        "options": [
            {"text": "Used up, because boiling spends energy rather than "
                     "passing it on to anything", "correct": False,
             "why": "Energy is never used up. It is transferred, and here it "
                    "left the beaker inside the steam."},
            {"text": "In the empty beaker, which is the hottest thing in "
                     "the room", "correct": False,
             "why": "The beaker holds very little of it, and a beaker at "
                    "100 °C is not where a whole flat step's energy went."},
            {"text": "In the steam that has left the beaker, which carried "
                     "it away", "correct": True},
            {"text": "Back in the flame, which is why the flame keeps "
                     "burning after the water has gone", "correct": False,
             "why": "The flame is the source of the energy, not a store for "
                    "it, and it burns because of its own fuel."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h17",
        "band": "harder",
        "text": "A technician checks a thermometer by standing it in a "
                "beaker of melting ice rather than in a beaker of cooling "
                "water. Why is melting ice the better check?",
        "options": [
            {"text": "Because ice is colder than any water the technician "
                     "would be able to pour out", "correct": False,
             "why": "Melting ice and the water around it are both at 0 °C. "
                    "Being colder is not what makes it useful."},
            {"text": "Because a thermometer is more reliable at low "
                     "temperatures than at high ones", "correct": False,
             "why": "A thermometer is no more reliable at one end of its "
                    "range than the other, and that would not fix a value "
                    "to check against."},
            {"text": "Because the ice keeps getting colder as it melts, so "
                     "every value can be checked", "correct": False,
             "why": "Melting ice does not get colder. It holds at 0 °C for "
                    "the whole of the melting."},
            {"text": "Because melting ice holds at one known temperature "
                     "for as long as ice is left", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier, second pass ───────────────────────────
    {
        "id": "c7-01-e18",
        "band": "easier",
        "text": "What is the boiling point of water?",
        "options": [
            {"text": "100 °C", "correct": True},
            {"text": "0 °C", "correct": False,
             "why": "0 °C is where water melts and freezes, at the other end "
                    "of the liquid range."},
            {"text": "50 °C", "correct": False,
             "why": "Water at 50 °C is hot to the touch but nowhere near "
                    "bubbling throughout."},
            {"text": "212 °C", "correct": False,
             "why": "212 is the boiling point on the Fahrenheit scale, not "
                    "the Celsius one."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e19",
        "band": "easier",
        "text": "In which state are the particles held in a fixed "
                "arrangement?",
        "options": [
            {"text": "A liquid", "correct": False,
             "why": "Liquid particles touch each other but slide past, which "
                    "is why a liquid takes the shape of its container."},
            {"text": "A solid", "correct": True},
            {"text": "A gas", "correct": False,
             "why": "Gas particles are far apart and move freely in all "
                    "directions."},
            {"text": "A gas that has been squeezed into a small space",
             "correct": False,
             "why": "Squeezing pushes gas particles closer together but does "
                    "not lock them into any arrangement."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e20",
        "band": "easier",
        "text": "Particles in a solid cannot move around. What can they do?",
        "options": [
            {"text": "Nothing, until the solid starts to melt",
             "correct": False,
             "why": "They are moving the whole time. Melting is not what "
                    "starts them off."},
            {"text": "Swap places with each other",
             "correct": False,
             "why": "That is a liquid, where particles slide past one "
                    "another."},
            {"text": "Vibrate where they are", "correct": True},
            {"text": "Spread out until they fill the space around them",
             "correct": False,
             "why": "Only a gas does that. A solid keeps its own shape."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e21",
        "band": "easier",
        "text": "What holds the particles of a solid in their fixed "
                "arrangement?",
        "options": [
            {"text": "The air pressing in on the outside of the solid",
             "correct": False,
             "why": "A solid keeps its arrangement in a vacuum, where there "
                    "is no air to press on it."},
            {"text": "The fact that they are too cold to move anywhere",
             "correct": False,
             "why": "They are vibrating even in a very cold solid. Being "
                    "cold is not what holds them."},
            {"text": "The container the solid is sitting in",
             "correct": False,
             "why": "A solid holds its own shape with no container at all, "
                    "which is what makes it a solid."},
            {"text": "Forces of attraction between the particles",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e22",
        "band": "easier",
        "text": "Which change of state turns a gas into a liquid?",
        "options": [
            {"text": "Condensing", "correct": True},
            {"text": "Evaporating", "correct": False,
             "why": "Evaporating goes the other way — liquid to gas, from "
                    "the surface."},
            {"text": "Melting", "correct": False,
             "why": "Melting starts with a solid, and no gas is involved in "
                    "it at all."},
            {"text": "Freezing", "correct": False,
             "why": "Freezing turns a liquid into a solid, one step further "
                    "on."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e23",
        "band": "easier",
        "text": "At what temperatures can evaporation happen?",
        "options": [
            {"text": "Only at 100 °C", "correct": False,
             "why": "At 100 °C the liquid changes throughout. Evaporation is going on well below that."},
            {"text": "At any temperature at all", "correct": True},
            {"text": "Only above room temperature", "correct": False,
             "why": "Washing dries outside on a cold day, and a puddle "
                    "shrinks at 8 °C."},
            {"text": "Only while the liquid is being heated by something",
             "correct": False,
             "why": "A glass of water left alone on a bench loses some over "
                    "a week with nothing heating it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e24",
        "band": "easier",
        "text": "What do the particles of a liquid do as it freezes?",
        "options": [
            {"text": "They stop moving completely and lock still",
             "correct": False,
             "why": "They keep vibrating in the solid. Only the moving "
                    "around stops."},
            {"text": "They get smaller, which is why ice takes up less room",
             "correct": False,
             "why": "Particles do not change size, and ice in fact takes up "
                    "more room than the water it came from."},
            {"text": "They settle into a fixed arrangement", "correct": True},
            {"text": "They spread further apart and slow down",
             "correct": False,
             "why": "They come closer together as a solid forms, not "
                    "further apart."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e25",
        "band": "easier",
        "text": "What is latent heat?",
        "options": [
            {"text": "The heat a substance holds on to once it has been "
                     "taken off the flame", "correct": False,
             "why": "That is just the substance being hot, which a "
                    "thermometer shows perfectly well."},
            {"text": "The heat that escapes from a beaker into the room "
                     "during an experiment", "correct": False,
             "why": "Escaping heat is a loss to the surroundings, and it is "
                    "not hidden from anything."},
            {"text": "The extra heat needed to take a substance above its "
                     "boiling point", "correct": False,
             "why": "Heating steam above 100 °C raises its temperature, and "
                    "a thermometer reports every degree of it."},
            {"text": "The energy taken in or given out during a change of "
                     "state", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e26",
        "band": "easier",
        "text": "Who worked out the idea of latent heat, and roughly when?",
        "options": [
            {"text": "Joseph Black, in the 1760s", "correct": True},
            {"text": "James Watt, in the 1860s", "correct": False,
             "why": "Watt built the idea into his steam engines, and he was "
                    "working a century before the 1860s."},
            {"text": "Isaac Newton, in the 1660s", "correct": False,
             "why": "Newton worked on forces and light. Latent heat was a "
                    "hundred years after him."},
            {"text": "Anders Celsius, in the 1740s", "correct": False,
             "why": "Celsius gave us the temperature scale, which is a "
                    "different piece of work altogether."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e27",
        "band": "easier",
        "text": "A block of ice is weighed, allowed to melt into a sealed "
                "dish, and weighed again. What does the balance read?",
        "options": [
            {"text": "Less, because melting uses some of the ice up",
             "correct": False,
             "why": "Nothing is used up. The same particles are there, "
                    "arranged differently."},
            {"text": "Exactly the same", "correct": True},
            {"text": "More, because the ice has taken energy in",
             "correct": False,
             "why": "Taking energy in does not add mass to anything you "
                    "could weigh on a school balance."},
            {"text": "Less, because water is lighter than ice",
             "correct": False,
             "why": "A kilogram of ice makes a kilogram of water. Ice floats "
                    "because it is less dense, not because it weighs less."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e28",
        "band": "easier",
        "text": "Which of these is NOT a change of state?",
        "options": [
            {"text": "Wax melting in a warm room", "correct": False,
             "why": "Melting is a change of state, and the wax could be set "
                    "solid again by cooling it."},
            {"text": "Water freezing in a pipe", "correct": False,
             "why": "Freezing is a change of state, and the same water comes "
                    "back when it thaws."},
            {"text": "Wood burning on a fire", "correct": True},
            {"text": "Steam condensing on a window", "correct": False,
             "why": "Condensing is a change of state — gas back to liquid, "
                    "with nothing new made."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e29",
        "band": "easier",
        "text": "Why is a boiling beaker watched from the side rather than "
                "from directly above it?",
        "options": [
            {"text": "Because the glass is more likely to crack upwards than "
                     "sideways", "correct": False,
             "why": "Glass does not crack in a chosen direction, and a "
                    "cracked beaker is not what the rule is about."},
            {"text": "Because the bubbles are easier to count from that "
                     "angle", "correct": False,
             "why": "Nobody is counting bubbles, and the rule would not be a "
                    "safety one if they were."},
            {"text": "Because a thermometer cannot be read properly from "
                     "above", "correct": False,
             "why": "A thermometer can be read from any angle that shows the "
                    "scale."},
            {"text": "Because the plume of steam above it burns",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-e30",
        "band": "easier",
        "text": "In which state can particles slide past one another while "
                "still touching?",
        "options": [
            {"text": "A liquid", "correct": True},
            {"text": "A solid", "correct": False,
             "why": "Solid particles are held in one arrangement and can "
                    "only vibrate on the spot."},
            {"text": "A gas", "correct": False,
             "why": "Gas particles are far apart and are not touching for "
                    "most of the time."},
            {"text": "A solid that has been warmed close to its melting "
                     "point", "correct": False,
             "why": "A warm solid vibrates harder, but nothing slides until "
                    "it actually melts."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard, second pass ─────────────────────────
    {
        "id": "c7-01-s18",
        "band": "standard",
        "text": "Sweating cools you much less well on a humid day, when the "
                "air already holds a great deal of water vapour. Why?",
        "options": [
            {"text": "Because humid air is warmer, so there is nothing for "
                     "the sweat to cool you down to", "correct": False,
             "why": "A humid day can be cool and still feel unpleasant. It "
                    "is the water in the air that does it."},
            {"text": "Because the sweat cannot evaporate, so the cooling "
                     "never happens", "correct": True},
            {"text": "Because humid air stops the body making sweat in the "
                     "first place", "correct": False,
             "why": "You sweat more on a humid day, not less. It simply sits "
                    "on the skin."},
            {"text": "Because water in the air condenses onto the skin and "
                     "warms it up again", "correct": False,
             "why": "Skin is warmer than the air around it, so nothing "
                    "condenses onto it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s19",
        "band": "standard",
        "text": "Spraying trees with water protects fruit in a light frost. "
                "Why would it not save a crop on a night at −15 °C?",
        "options": [
            {"text": "Because water sprayed at −15 °C would not freeze at "
                     "all", "correct": False,
             "why": "It would freeze quickly. The problem is what happens "
                    "afterwards, not whether it freezes."},
            {"text": "Because the spray would blow away before it could "
                     "reach the fruit", "correct": False,
             "why": "Wind is not the point. The question is how cold the "
                    "night is."},
            {"text": "Because freezing can only hold the fruit at 0 °C, and "
                     "the ice then cools further", "correct": True},
            {"text": "Because ice gives out energy only while the air is "
                     "above freezing", "correct": False,
             "why": "Freezing gives energy out whatever the air temperature "
                    "is. There is simply not enough of it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s20",
        "band": "standard",
        "text": "Ice taken straight out of a freezer at −18 °C sits in a "
                "warm kitchen for several minutes before the first drip "
                "appears. Why the delay?",
        "options": [
            {"text": "Because the outside has to melt before the inside can "
                     "start", "correct": False,
             "why": "The surface is where melting starts, and it would drip "
                    "as soon as it did. Nothing is waiting for the middle."},
            {"text": "Because a freezer coats ice in a layer that has to "
                     "come off first", "correct": False,
             "why": "There is no such coating. The ice is the same substance "
                    "all the way through."},
            {"text": "Because the room has to warm the ice up to 0 °C before "
                     "any melting can begin", "correct": True},
            {"text": "Because melting always starts slowly and then speeds "
                     "up on its own", "correct": False,
             "why": "Once it is at 0 °C the melting runs steadily. The delay "
                    "happens before melting starts at all."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s21",
        "band": "standard",
        "text": "Wet clothes on a washing line dry on a cold, breezy day. "
                "Which change is happening, and what supplies the energy?",
        "options": [
            {"text": "Evaporation, with the energy coming from the air and "
                     "the clothes themselves", "correct": True},
            {"text": "Boiling, with the energy coming from the wind moving "
                     "over the fabric", "correct": False,
             "why": "Boiling needs 100 °C. Nothing on a washing line is "
                    "anywhere near that."},
            {"text": "Condensing, with the energy given out into the air as "
                     "the water leaves", "correct": False,
             "why": "Condensing turns gas into liquid, which would make the "
                    "clothes wetter rather than drier."},
            {"text": "Melting, with the energy coming from the sunlight "
                     "falling on the line", "correct": False,
             "why": "The water is already liquid, so there is nothing there "
                    "to melt."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s22",
        "band": "standard",
        "text": "A student heats a solid steadily and plots this graph. What "
                "did they most likely do?",
        "options": [
            {"text": "They heated a substance that has no boiling point", "correct": False,
             "why": "Every substance boils if it is taken hot enough. The "
                    "run simply stopped before that."},
            {"text": "They stopped heating before the substance reached its "
                     "boiling point", "correct": True},
            {"text": "They started the run after the substance had already "
                     "melted", "correct": False,
             "why": "Then there would be no flat step at all, and their "
                    "graph has one."},
            {"text": "They used a thermometer that stopped working part way "
                     "through", "correct": False,
             "why": "A broken thermometer would not give a steady climb "
                    "afterwards."},
        ],
        "figure": "c7-heating-one-step",
    },
    {
        "id": "c7-01-s23",
        "band": "standard",
        "text": "Steam at 120 °C is cooled steadily all the way down to ice. "
                "What does a graph of its temperature against time look "
                "like?",
        "options": [
            {"text": "A steady fall with no flat steps, because energy is "
                     "leaving the whole time", "correct": False,
             "why": "Energy leaving is exactly what the flat steps are made "
                    "of. They appear while the state changes."},
            {"text": "A steady fall with two flat steps, where the changes "
                     "of state happen", "correct": True},
            {"text": "A steady fall with one flat step, at 0 °C only",
             "correct": False,
             "why": "Condensing at 100 °C gives a flat step too, and it is "
                    "the longer of the two."},
            {"text": "A fall that gets steeper and steeper as the substance "
                     "gets colder", "correct": False,
             "why": "Nothing in the cooling makes it accelerate, and it "
                    "would still have to hold at the two change points."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s24",
        "band": "standard",
        "text": "A pan of water is left boiling on a hob. Once the last of "
                "the water has gone, the pan's temperature climbs fast. "
                "Why?",
        "options": [
            {"text": "Because a dry pan conducts heat better than a wet one "
                     "does", "correct": False,
             "why": "The metal conducts the same either way. What has "
                    "changed is what the energy has to do."},
            {"text": "Because the hob turns itself up once the water has "
                     "gone", "correct": False,
             "why": "The hob is doing exactly what it was doing before. "
                    "Nothing about it has changed."},
            {"text": "Because the energy has nothing left to boil, so it "
                     "goes into heating the metal", "correct": True},
            {"text": "Because steam was keeping the pan cool and there is "
                     "none left", "correct": False,
             "why": "The steam was leaving at 100 °C, carrying energy away "
                    "rather than cooling anything down."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s25",
        "band": "standard",
        "text": "A student says boiling and evaporating are two words for "
                "the same thing. Give the two differences.",
        "options": [
            {"text": "Boiling happens throughout the liquid and only at its "
                     "boiling point", "correct": True},
            {"text": "Boiling gives energy out while evaporating takes it "
                     "in", "correct": False,
             "why": "Both take energy in. Both are a liquid becoming a gas."},
            {"text": "Boiling needs a flame while evaporating needs only "
                     "sunlight", "correct": False,
             "why": "Neither one cares what the energy source is. A kettle "
                    "and the sun both do either."},
            {"text": "Boiling makes a gas while evaporating makes only tiny "
                     "droplets", "correct": False,
             "why": "Evaporation makes the same gas boiling does. The "
                    "droplets you see are that gas condensing again."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s26",
        "band": "standard",
        "text": "A candle burns: the wax near the wick turns liquid, and "
                "further up the wick it burns. Which part is a change of "
                "state?",
        "options": [
            {"text": "Both are, because the wax changes form in each of "
                     "them", "correct": False,
             "why": "Burning makes new substances, which is what a change of "
                    "state never does."},
            {"text": "The burning, because the solid wax disappears "
                     "completely", "correct": False,
             "why": "It disappears because it has reacted into gases, not "
                    "because it has changed state."},
            {"text": "Neither, because a candle is a chemical reaction from "
                     "start to finish", "correct": False,
             "why": "The melting at the top of the candle is a change of "
                    "state, with the same wax left afterwards."},
            {"text": "The melting, because the wax is the same substance "
                     "afterwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s27",
        "band": "standard",
        "text": "A beaker holds ice and water together and the thermometer "
                "reads 0 °C. More ice is added. What does the reading do?",
        "options": [
            {"text": "It falls, because more ice makes the mixture colder",
             "correct": False,
             "why": "The ice being added is at 0 °C too. There is nothing "
                    "colder in the beaker to pull the reading down."},
            {"text": "It dips briefly",
             "correct": False,
             "why": "Nothing dips. Ice and water together hold at the "
                    "melting point."},
            {"text": "It holds at 0 °C", "correct": True},
            {"text": "It rises, because there is now less liquid water to "
                     "cool", "correct": False,
             "why": "How much liquid there is does not set the temperature "
                    "while ice is still present."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s28",
        "band": "standard",
        "text": "A student heating ice reads the thermometer every minute "
                "but never stirs the beaker. Why might their flat step at "
                "0 °C look less clear than it should?",
        "options": [
            {"text": "Because the thermometer drifts upwards when it is left "
                     "still for too long", "correct": False,
             "why": "A thermometer reads what it is in. It does not drift "
                    "because nothing is moving."},
            {"text": "Because unstirred ice melts more slowly, so the step "
                     "is shorter", "correct": False,
             "why": "The step would still be flat, just longer or shorter. "
                    "Stirring changes how clear the reading is."},
            {"text": "Because a flat step only appears on a graph if "
                     "readings are taken more often than once a minute",
             "correct": False,
             "why": "A minute is plenty. The lesson's own run is plotted "
                    "exactly that way."},
            {"text": "Because the water near the thermometer can warm past "
                     "0 °C while ice is still there", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s29",
        "band": "standard",
        "text": "Why is the flame kept at exactly the same setting for the "
                "whole of a heating-curve run?",
        "options": [
            {"text": "So that every minute delivers the same energy and the "
                     "flat steps can be compared", "correct": True},
            {"text": "So that the beaker does not crack from being heated "
                     "unevenly", "correct": False,
             "why": "Cracking is worth avoiding, but it is not what the "
                    "steady flame is there to do."},
            {"text": "So that the water never goes above its boiling point "
                     "on the way", "correct": False,
             "why": "Boiling water holds at 100 °C however big the flame "
                    "is."},
            {"text": "So that the two changes of state happen at their "
                     "proper temperatures", "correct": False,
             "why": "Ice melts at 0 °C and water boils at 100 °C whatever "
                    "the flame is doing."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-s30",
        "band": "standard",
        "text": "Two students heat ice with identical flames, one using "
                "50 g and one using 200 g. Compare the TEMPERATURES their "
                "thermometers show at the flat steps.",
        "options": [
            {"text": "The larger sample holds at a lower temperature, "
                     "because there is more of it to warm", "correct": False,
             "why": "How much there is does not change the temperature a "
                    "substance melts or boils at."},
            {"text": "Both hold at 0 °C and then at 100 °C", "correct": True},
            {"text": "The larger sample holds at a higher temperature, "
                     "because it stores more energy", "correct": False,
             "why": "It does hold more energy, and that is exactly why "
                    "temperature is not the same thing as energy."},
            {"text": "Neither holds steady at all", "correct": False,
             "why": "A smaller flame makes the steps longer. It does not "
                    "stop them being flat."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder, second pass ───────────────────────────
    {
        "id": "c7-01-h18",
        "band": "harder",
        "text": "Water melts and freezes at the same temperature. A student "
                "says that means water sitting at 0 °C cannot be doing "
                "either. What is the right answer?",
        "options": [
            {"text": "They are right, because the two changes would cancel "
                     "each other out exactly", "correct": False,
             "why": "Nothing cancels. Only one of them runs, and which one "
                    "depends on the energy."},
            {"text": "They are right, because a substance at its melting "
                     "point is between states rather than changing",
             "correct": False,
             "why": "There is no in-between state. Ice and water sit "
                    "together and one turns into the other."},
            {"text": "They are wrong — which one happens depends only on whether energy is going in or out", "correct": True},
            {"text": "They are wrong, because freezing happens a little below 0 °C", "correct": False,
             "why": "Water freezes at the same 0 °C it melts at. That is "
                    "what makes it one fixed point."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h19",
        "band": "harder",
        "text": "A heating curve is redrawn with ENERGY SUPPLIED along the "
                "bottom instead of time. The flame was steady throughout. "
                "How does the new graph compare?",
        "options": [
            {"text": "The flat steps swap places, because energy and time "
                     "run opposite ways", "correct": False,
             "why": "They run together, not opposite. More time at a steady "
                    "flame simply means more energy."},
            {"text": "The flat steps disappear, because energy is going in "
                     "the whole time", "correct": False,
             "why": "Energy going in with no temperature change is exactly "
                    "what a flat step is."},
            {"text": "The second flat step becomes the shorter one, because "
                     "boiling is quicker per joule", "correct": False,
             "why": "Boiling takes about seven times the energy of melting, "
                    "so its step is longer on either axis."},
            {"text": "It has the same shape, because at a steady flame "
                     "energy and time go together", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h20",
        "band": "harder",
        "text": "In a power station, used steam is turned back into water in "
                "a condenser, which has cold water running through it. "
                "Predict what that cooling water does.",
        "options": [
            {"text": "It warms up, because condensing gives out the energy "
                     "boiling put in", "correct": True},
            {"text": "It cools down, because the steam takes energy from it "
                     "as it condenses", "correct": False,
             "why": "Condensing is the giving-out direction. The steam is "
                    "handing energy over, not taking it."},
            {"text": "It stays at the same temperature, because the steam is "
                     "already at 100 °C", "correct": False,
             "why": "Equal temperatures would still leave all the energy of "
                    "condensing to go somewhere."},
            {"text": "It freezes, because the steam has given up all of its "
                     "energy by then", "correct": False,
             "why": "The cooling water is receiving energy. Nothing there is "
                    "being taken towards 0 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h21",
        "band": "harder",
        "text": "Joseph Black's work on latent heat went straight into James "
                "Watt's steam engines. Which is the best reason it mattered "
                "so much to an engine designer?",
        "options": [
            {"text": "Because an engine runs better the hotter its steam is "
                     "allowed to become", "correct": False,
             "why": "That is about temperature. Black's discovery was about "
                    "energy that a temperature does not show."},
            {"text": "Because making the steam is where most of the fuel "
                     "goes, so wasting steam wastes fuel", "correct": True},
            {"text": "Because it showed that steam is hotter than the water "
                     "it was boiled from", "correct": False,
             "why": "Steam leaving a boiler is at the same temperature as "
                    "the water. That is the whole surprise."},
            {"text": "Because it let engineers boil water at a lower "
                     "temperature than before", "correct": False,
             "why": "Nothing about latent heat changes the temperature water "
                    "boils at."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h22",
        "band": "harder",
        "text": "While a beaker boils, a balance under it shows the mass "
                "falling steadily and the thermometer in it does not move at "
                "all. Explain how those two observations fit together.",
        "options": [
            {"text": "The mass leaving as steam is carrying the energy away, "
                     "so the reading holds", "correct": True},
            {"text": "The mass is falling because the energy itself has "
                     "weight and is escaping", "correct": False,
             "why": "Energy is not something a balance weighs. What is "
                    "leaving the beaker is water."},
            {"text": "The thermometer is holding because there is less water "
                     "left to heat each minute", "correct": False,
             "why": "Less water would heat faster, not hold still. The "
                    "holding is the change of state."},
            {"text": "The two cannot both be right, so one instrument must "
                     "be faulty", "correct": False,
             "why": "Both are correct, and together they are the best "
                    "evidence on the bench for where the energy goes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h23",
        "band": "harder",
        "text": "A lake freezes over in winter and thaws in spring. Compare "
                "what the energy does in the two events.",
        "options": [
            {"text": "Freezing takes energy from the air, and thawing gives "
                     "the same energy back to it", "correct": False,
             "why": "That is the right pair of events with the directions "
                    "swapped over."},
            {"text": "Both take energy in, because ice is involved in each "
                     "of them", "correct": False,
             "why": "The substance does not fix the direction. Opposite "
                    "changes transfer opposite ways."},
            {"text": "Freezing releases energy to the surroundings, and "
                     "thawing takes the same amount back", "correct": True},
            {"text": "Neither moves much energy, because the temperature "
                     "stays near 0 °C throughout", "correct": False,
             "why": "A steady temperature is the sign of a large transfer, "
                    "not of a small one."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h24",
        "band": "harder",
        "text": "A change of state is described as reversible. Explain why "
                "reversible does not mean that reversing it costs nothing.",
        "options": [
            {"text": "Because reversing it always means supplying or removing the same energy again", "correct": True},
            {"text": "Because a substance is never quite the same after it "
                     "has been changed and changed back", "correct": False,
             "why": "It is exactly the same substance. That is what makes "
                    "the change physical."},
            {"text": "Because a little of the substance is lost every time "
                     "the change is run", "correct": False,
             "why": "In a sealed container the mass is unchanged. Nothing is "
                    "lost by changing state."},
            {"text": "Because the change can only be reversed a limited "
                     "number of times", "correct": False,
             "why": "Water can be frozen and melted endlessly, and it is the "
                    "same water each time."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h25",
        "band": "harder",
        "text": "Chocolate burns easily on a hob, so cooks melt it in a bowl "
                "over a pan of boiling water. Explain why that protects it.",
        "options": [
            {"text": "Because water carries heat more gently than metal "
                     "does, whatever temperature it is at", "correct": False,
             "why": "How gently it carries heat is not the protection. The "
                    "temperature it cannot pass is."},
            {"text": "Because boiling water never goes above 100 °C, however hard the hob is driven", "correct": True},
            {"text": "Because the steam coming off keeps the bowl below 100 °C throughout", "correct": False,
             "why": "The steam is at 100 °C itself and warms the bowl rather "
                    "than holding it lower."},
            {"text": "Because the bowl does not touch anything that is being heated", "correct": False,
             "why": "It is being heated — by the water and steam under it. "
                    "The limit is their temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h26",
        "band": "harder",
        "text": "A student wants to show that a thermometer is not an energy "
                "meter, using a beaker, a flame, ice and a thermometer. "
                "Which demonstration makes the point best?",
        "options": [
            {"text": "Heat the flame itself and show that it reads far "
                     "higher than the water does", "correct": False,
             "why": "That compares two temperatures, which is exactly what a "
                    "thermometer is for."},
            {"text": "Heat two beakers to the same temperature and show the "
                     "readings match", "correct": False,
             "why": "Matching readings with nothing else measured say "
                    "nothing about energy at all."},
            {"text": "Heat melting ice and show the reading holds while the "
                     "flame keeps running", "correct": True},
            {"text": "Heat the water quickly and then slowly and show the "
                     "readings end up the same", "correct": False,
             "why": "Two routes to one temperature is a fair point about "
                    "heating rate, not about what the reading means."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h27",
        "band": "harder",
        "text": "One student's flat step at 0 °C lasts four minutes; "
                "another, with the same flame and twice the ice, gets eight. "
                "What quantity is the same for both of them?",
        "options": [
            {"text": "The total energy each flame delivered during the flat "
                     "step", "correct": False,
             "why": "The second flame ran for twice as long at the same "
                    "rate, so it delivered twice as much."},
            {"text": "The length of the flat step, once the graphs are drawn "
                     "to the same scale", "correct": False,
             "why": "Drawing them differently does not change the fact that "
                    "one took twice the time."},
            {"text": "The temperature and nothing else about the two runs",
             "correct": False,
             "why": "The temperature does match, but something about the "
                    "energy matches too, which is the useful part."},
            {"text": "The energy needed to melt each kilogram of ice",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h28",
        "band": "harder",
        "text": "Steam at 100 °C is bubbled into cold water, and the water "
                "warms far more than the same mass of boiling water would "
                "have warmed it. Explain why.",
        "options": [
            {"text": "Because the steam gives out the energy of condensing "
                     "as well as cooling down", "correct": True},
            {"text": "Because steam is hotter than boiling water, so it has "
                     "more to give", "correct": False,
             "why": "Both are at 100 °C. A thermometer cannot tell them "
                    "apart, which is the point of the comparison."},
            {"text": "Because bubbling stirs the water and stirring warms "
                     "it", "correct": False,
             "why": "Stirring spreads energy around a beaker. It does not "
                    "add any."},
            {"text": "Because a gas carries energy more quickly than a "
                     "liquid can", "correct": False,
             "why": "How quickly it arrives is a separate question from how "
                    "much arrives, and it is the amount that differs here."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h29",
        "band": "harder",
        "text": "Two students describe the flat step. One says energy is "
                "being stored; the other says it is being used up. Which is "
                "the better description, and how would you show it?",
        "options": [
            {"text": "Used up — the ice absorbs it and nothing can get it "
                     "back afterwards", "correct": False,
             "why": "It can be got back. Freeze the water again and the same "
                    "energy comes out."},
            {"text": "Stored — freezing the water again gives the same "
                     "energy back out", "correct": True},
            {"text": "Used up — the proof is that the thermometer records "
                     "none of it", "correct": False,
             "why": "A thermometer not showing something is not evidence "
                    "that it has gone."},
            {"text": "Stored — the proof is that the beaker is warmer "
                     "afterwards than before", "correct": False,
             "why": "The beaker is not warmer. It sat at 0 °C for the whole "
                    "of the flat step."},
        ],
        "figure": None,
    },
    {
        "id": "c7-01-h30",
        "band": "harder",
        "text": "A pan is boiling hard on full power. The hob is turned down "
                "to the lowest setting that still keeps it boiling. Compare "
                "the temperature and the rate steam is made.",
        "options": [
            {"text": "The temperature drops a little and the steam is made "
                     "more slowly", "correct": False,
             "why": "Boiling water is at 100 °C on any setting that keeps it "
                    "boiling."},
            {"text": "Both stay the same, because the water is boiling in "
                     "each case", "correct": False,
             "why": "Less energy every minute means less water turned to "
                    "steam every minute."},
            {"text": "The temperature stays the same and the steam is made "
                     "more slowly", "correct": True},
            {"text": "The temperature stays the same and the steam is made "
                     "at the same rate", "correct": False,
             "why": "The rate follows the energy going in, and much less is "
                    "going in now."},
        ],
        "figure": None,
    },
]
