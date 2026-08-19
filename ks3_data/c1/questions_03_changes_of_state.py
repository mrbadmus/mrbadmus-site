"""C1 lesson 03 — Changes of state: twelve questions (MRB-269).

These probe the two claims the lesson is built on — that a change of state
moves particles about and never removes one, and that a held thermometer is
the sign of energy buying separation rather than speed. The distractors come
from all three declared misconceptions: PART-05 (something is lost when a
substance melts or evaporates — a balance too blunt to see it, a gas with no
mass, water "turning into air"), PART-06 (melting and dissolving are the same
event, so cooling should undo both), and PART-07 (the bubbles in a boiling pan
are dissolved air, an empty space, or water split into hydrogen and oxygen).
Two more distractor families are the ones the lesson's own feedback names: the
last lesson's particles-change-size error wearing a new hat, and the belief
that a plateau is heat leaking away. The `harder` band takes the lesson
somewhere it never goes — a scalding by steam at the same temperature as the
water beside it, frost that leaves a dry windscreen, and two trays of solid
that have to be recovered in opposite ways.
"""

UNIT = "C1"
LESSON = "changes-of-state"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-03-e01",
        "band": "easier",
        "text": "Solid carbon dioxide — dry ice — turns straight into a gas "
                "without ever becoming a liquid. What is this change called?",
        "options": [
            {"text": "Evaporating",
             "correct": False,
             "why": "Evaporating starts with a liquid. Dry ice never becomes "
                    "a liquid — it skips that step entirely."},
            {"text": "Sublimation",
             "correct": True},
            {"text": "Melting",
             "correct": False,
             "why": "Melting ends with a liquid, and there is never a puddle "
                    "under a block of dry ice."},
            {"text": "Condensing",
             "correct": False,
             "why": "Condensing is a gas turning into a liquid — the opposite "
                    "direction, and it ends in the state dry ice skips."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e02",
        "band": "easier",
        "text": "Through the whole heating run — ice at −20 °C, melting, "
                "water, boiling, steam at 120 °C — the readout on the sealed "
                "flask never moves off 50.0 g. What does that tell you?",
        "options": [
            {"text": "A change of state only rearranges the particles; it "
                     "never creates or destroys a single one.",
             "correct": True},
            {"text": "The seal traps what was lost during boiling, so the "
                     "balance cannot show the loss.",
             "correct": False,
             "why": "There is nothing lost to trap. Unseal it and the steam "
                    "that leaves is the same particles, still with mass — "
                    "gone from the flask, not gone from existence."},
            {"text": "A gas has no mass, so the reading cannot change once "
                     "the water has boiled.",
             "correct": False,
             "why": "Steam is the same particles as the water, so it has the "
                    "same mass. If a gas weighed nothing the reading would "
                    "fall as the water boiled — and it does not."},
            {"text": "The balance is not sensitive enough to notice the small "
                     "amount lost while it boils.",
             "correct": False,
             "why": "There is nothing there to notice. 50.0 g of ice becomes "
                    "50.0 g of steam, particle for particle."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e03",
        "band": "easier",
        "text": "Watch the thermometer through the whole run on the heating "
                "bench and it stops climbing twice. At which two temperatures "
                "does it stop?",
        "options": [
            {"text": "−20 °C and 0 °C",
             "correct": False,
             "why": "−20 °C is where the run starts, and the ice is warming "
                    "there — the thermometer is climbing, not held."},
            {"text": "0 °C and 120 °C",
             "correct": False,
             "why": "0 °C is right. 120 °C is the end of the run, where the "
                    "steam is warming fast; the second stop is at the boiling "
                    "point, 100 °C."},
            {"text": "0 °C and 100 °C",
             "correct": True},
            {"text": "100 °C only — there is one stop, when the water boils",
             "correct": False,
             "why": "There are two. Melting holds the thermometer at 0 °C "
                    "long before the water gets anywhere near boiling."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e04",
        "band": "easier",
        "text": "A student writes: “Salt melts when you stir it into cold "
                "water.” What is wrong with that sentence?",
        "options": [
            {"text": "Nothing is wrong — melting and dissolving are two words "
                     "for the same event.",
             "correct": False,
             "why": "They are different events. Melting is one substance "
                    "heated past its melting point; dissolving is a solid "
                    "spreading out among the particles of a liquid."},
            {"text": "Salt cannot melt at any temperature, so the word can "
                     "never be used of it.",
             "correct": False,
             "why": "Salt does melt — at 801 °C. Cold water is nowhere near "
                    "that, which is why this one is dissolving."},
            {"text": "It should say the salt evaporated into the water it was "
                     "stirred into.",
             "correct": False,
             "why": "Evaporating is a liquid turning into a gas. Nothing here "
                    "has become a gas; the salt has dissolved."},
            {"text": "The water is cold, so nothing was heated to a melting "
                     "point — the salt is dissolving.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-03-s01",
        "band": "standard",
        "text": "A pan of water is kept at a rolling boil for twenty minutes "
                "and never runs out of bubbles. What does that on its own "
                "tell you?",
        "options": [
            {"text": "The bubbles are dissolved air, topped up all the while "
                     "by fresh air from above the water.",
             "correct": False,
             "why": "Air would have to travel down through boiling water "
                    "against the rising bubbles. The little that is dissolved "
                    "in a pan is gone in the first minute."},
            {"text": "The bubbles cannot be dissolved air — a pan holds very "
                     "little of it and it would have run out.",
             "correct": True},
            {"text": "The bubbles are empty spaces that the heat keeps making "
                     "at the bottom of the pan.",
             "correct": False,
             "why": "An empty space would be crushed instantly by the "
                    "pressure of the water above it. The bubbles are full — "
                    "of water that has turned into a gas."},
            {"text": "The bubbles are hydrogen and oxygen, and they last "
                     "because there is plenty of water to split.",
             "correct": False,
             "why": "Splitting water into hydrogen and oxygen is a chemical "
                    "change and takes far more energy than a hob has. Boiling "
                    "is a change of state and the water is still water."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s02",
        "band": "standard",
        "text": "A white cloud hangs a few centimetres above a boiling "
                "kettle, but the gap right at the spout looks completely "
                "clear. What is going on in that clear gap?",
        "options": [
            {"text": "The steam is moving too fast to see there, and it slows "
                     "down enough to be seen further up.",
             "correct": False,
             "why": "Speed has nothing to do with it — steam is invisible "
                    "however slowly it drifts. The gap is clear because the "
                    "water there is still a gas."},
            {"text": "Hot air is being pushed out of the kettle first, ahead "
                     "of the steam that follows it.",
             "correct": False,
             "why": "What leaves a boiling kettle is water, not air. The "
                    "cloud further up is that water, condensed back to "
                    "liquid."},
            {"text": "Steam is invisible; the cloud is steam that has already "
                     "condensed into tiny drops of liquid water.",
             "correct": True},
            {"text": "The water is splitting into hydrogen and oxygen, and "
                     "those gases cannot be seen.",
             "correct": False,
             "why": "That would be a chemical change, and a kettle is "
                    "nowhere near having the energy for it. Nothing has "
                    "split — it is water all the way out."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s03",
        "band": "standard",
        "text": "The ring delivers the same energy every second from start to "
                "finish. The thermometer holds at 0 °C for a while, then "
                "later holds at 100 °C for far longer. Why is the second hold "
                "the longer one?",
        "options": [
            {"text": "Melting only loosens the particles; separating them "
                     "completely costs about seven times as much.",
             "correct": True},
            {"text": "The water is much hotter by then, so every further "
                     "degree takes longer to gain.",
             "correct": False,
             "why": "Nothing is gaining a degree during a hold — that is what "
                    "a hold is. The extra energy is buying separation, not "
                    "temperature."},
            {"text": "More heat escapes to the room at 100 °C, so less of it "
                     "is left to go into the water.",
             "correct": False,
             "why": "The flask is sealed and the energy is going in at the "
                    "same steady rate as before. The hold is longer because "
                    "the job is bigger, not because energy is leaking."},
            {"text": "The particles are bigger and heavier by then, so they "
                     "take more energy to shift.",
             "correct": False,
             "why": "Particles never change size or mass — that is the last "
                    "lesson's misconception in a new hat. What changes is how "
                    "far apart they are."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s04",
        "band": "standard",
        "text": "A tray of water is left in a freezer and turns to ice at "
                "0 °C. What is happening to energy while it freezes?",
        "options": [
            {"text": "The water takes energy in from the freezer, and that is "
                     "what makes it set solid.",
             "correct": False,
             "why": "Freezing is melting run backwards. Melting costs energy, "
                    "so freezing must hand the same energy back — the "
                    "freezer's job is to carry it away."},
            {"text": "No energy moves at all, because the temperature stays "
                     "at 0 °C the whole time.",
             "correct": False,
             "why": "A held temperature is exactly when energy is moving in "
                    "or out fastest. It is buying separation, not speed, so "
                    "the thermometer cannot see it."},
            {"text": "The energy is destroyed as the particles stop moving "
                     "and lock into place.",
             "correct": False,
             "why": "The particles do not stop, and energy is never "
                    "destroyed. It is passed out to the surroundings, and it "
                    "goes back in when the ice melts again."},
            {"text": "The water gives energy out — the same energy that "
                     "melting the ice again would cost.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-03-h01",
        "band": "harder",
        "text": "Water at 100 °C and steam at 100 °C give a thermometer the "
                "same reading, yet a splash of the steam does far more damage "
                "to skin. Why?",
        "options": [
            {"text": "The steam is really hotter than 100 °C; the "
                     "thermometer is reading the pan and not the gas.",
             "correct": False,
             "why": "Both are at 100 °C, and that is the whole point. The "
                    "reading tells you nothing about the energy a change of "
                    "state gives back."},
            {"text": "Steam moves much faster than water, so it strikes the "
                     "skin harder when it lands.",
             "correct": False,
             "why": "The damage is energy transferred into your skin, not "
                    "force. Steam drifting slowly at 100 °C does the same "
                    "harm."},
            {"text": "Condensing on your skin gives back a whole boiling "
                     "plateau's worth of energy first.",
             "correct": True},
            {"text": "Steam is a gas, so it soaks into the skin where hot "
                     "water can only sit on the surface.",
             "correct": False,
             "why": "It does not soak in — it condenses on the surface, and "
                    "it is the energy released by that change of state that "
                    "burns."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h02",
        "band": "harder",
        "text": "The sealed bag from the start of the lesson is left on a "
                "warm radiator for a week. The puddle has gone and the inside "
                "of the bag is misted with droplets. What does the balance "
                "read now?",
        "options": [
            {"text": "Less than 50 g — the water evaporated, so some of it "
                     "has gone.",
             "correct": False,
             "why": "Evaporating moves particles into the gas state; it does "
                    "not remove them. The bag is sealed, so every particle is "
                    "still sitting on the balance."},
            {"text": "50 g, exactly as it read as an ice cube and as a "
                     "puddle.",
             "correct": True},
            {"text": "More than 50 g — a gas spreads out and takes up far "
                     "more room than a liquid.",
             "correct": False,
             "why": "Room is volume, not mass. Spreading the same particles "
                    "further apart adds nothing at all to the reading."},
            {"text": "There is no way to say, because some has evaporated and "
                     "some has condensed back.",
             "correct": False,
             "why": "The mixture makes no difference. Liquid or gas, every "
                    "particle is still inside the sealed bag, so the total is "
                    "50 g."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h03",
        "band": "harder",
        "text": "Tray A holds melted candle wax. Tray B holds salt dissolved "
                "in water. A student wants the solid back from each tray. "
                "What should they do?",
        "options": [
            {"text": "Cool tray A until the wax sets; leave tray B until the "
                     "water has gone.",
             "correct": True},
            {"text": "Cool both trays — cooling undoes melting and dissolving "
                     "alike.",
             "correct": False,
             "why": "Cool salt water and you get cold salt water, then salty "
                    "ice. Dissolving is undone by taking the liquid away, not "
                    "by dropping the temperature."},
            {"text": "Warm both trays — heat is what separates a solid back "
                     "out of a liquid.",
             "correct": False,
             "why": "Warming melted wax only keeps it liquid. Wax comes back "
                    "by cooling; the salt comes back only once the water has "
                    "gone."},
            {"text": "Neither can be recovered — once a solid is in a liquid "
                     "it is gone for good.",
             "correct": False,
             "why": "Both come back. Changes of state are reversible, and so "
                    "is dissolving — the salt was there the whole time, "
                    "spread out among the water particles."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h04",
        "band": "harder",
        "text": "Frost on a car windscreen slowly disappears over a morning "
                "when the air never rises above −3 °C, and the glass is left "
                "dry. What has happened to the frost?",
        "options": [
            {"text": "It melted, and the water ran off the sloping glass "
                     "before anyone looked at it.",
             "correct": False,
             "why": "Melting needs 0 °C and the air never got there — and "
                    "melted frost would leave the glass wet, which it is "
                    "not."},
            {"text": "Some of the water was destroyed by the cold, dry wind "
                     "blowing across the glass.",
             "correct": False,
             "why": "No change of state destroys anything. Every particle of "
                    "that frost is still there, spread out into the air as a "
                    "gas."},
            {"text": "The frost turned into air, which is why the glass is "
                     "clear and dry.",
             "correct": False,
             "why": "Water never becomes air. It has become water vapour — "
                    "the same water, invisible, mixed in among the air."},
            {"text": "It went straight from solid to gas without melting "
                     "first — sublimation, like dry ice.",
             "correct": True},
        ],
        "figure": None,
    },
]
