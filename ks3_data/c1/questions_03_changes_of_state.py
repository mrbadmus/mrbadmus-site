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
            {"text": "Salt cannot melt at any temperature, since it breaks "
                     "apart before it ever gets that hot.",
             "correct": False,
             "why": "Salt does melt — at 801 °C. Cold water is nowhere near "
                    "that, which is why this one is dissolving."},
            {"text": "It should say the salt evaporated into the water it was "
                     "stirred into.",
             "correct": False,
             "why": "Evaporating is a liquid turning into a gas. Nothing here "
                    "has become a gas; the salt has dissolved."},
            {"text": "The water is cold, so nothing reached a melting point — "
                     "the salt is dissolving.",
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
                     "costs about seven times as much.",
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-03-e05",
        "band": "easier",
        "text": "What is the name of the change from a liquid to a solid?",
        "options": [
            {"text": "Melting",
             "correct": False,
             "why": "That is the other direction — solid to liquid. Melting "
                    "and freezing use the same doorway opposite ways."},
            {"text": "Condensing",
             "correct": False,
             "why": "Condensing is gas to liquid — what happens on a cold "
                    "window, not in a freezer."},
            {"text": "Freezing",
             "correct": True},
            {"text": "Evaporating",
             "correct": False,
             "why": "Evaporating goes the other way again, from liquid to "
                    "gas."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e06",
        "band": "easier",
        "text": "The lesson says mass is conserved through a change of state. "
                "What does conserved mean?",
        "options": [
            {"text": "Kept somewhere safe until it is needed.",
             "correct": False,
             "why": "That is the everyday meaning. In science, conserved "
                    "means the total does not change."},
            {"text": "Reduced slowly, a little at a time.",
             "correct": False,
             "why": "The opposite. Conserved means nothing is lost at all, "
                    "quickly or slowly."},
            {"text": "Changed into energy rather than being destroyed.",
             "correct": False,
             "why": "Nothing here turns into anything. The particles are "
                    "rearranged, and every one of them is still present."},
            {"text": "Stays the same in total — nothing is gained or lost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e07",
        "band": "easier",
        "text": "Pure water freezes at 0 °C. At what temperature does pure "
                "ice melt?",
        "options": [
            {"text": "0 °C — the same temperature, used in the opposite "
                     "direction.",
             "correct": True},
            {"text": "A few degrees above 0 °C, because melting needs extra "
                     "energy.",
             "correct": False,
             "why": "Melting does need energy, but it is spent at 0 °C. The "
                    "energy goes in without the temperature moving."},
            {"text": "100 °C, the same temperature at which water boils.",
             "correct": False,
             "why": "100 °C is the boiling point, the second plateau. Melting "
                    "happens at the first one."},
            {"text": "It depends on how much ice there is.",
             "correct": False,
             "why": "More ice takes longer to melt, but it melts at the same "
                    "temperature. The amount changes the time, not the "
                    "reading."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e08",
        "band": "easier",
        "text": "A wet playground dries out during the morning. Which change "
                "of state has happened to the water?",
        "options": [
            {"text": "Condensing",
             "correct": False,
             "why": "Condensing makes a liquid appear, not disappear. That is "
                    "what happens on a cold window."},
            {"text": "Evaporating",
             "correct": True},
            {"text": "Melting",
             "correct": False,
             "why": "Melting turns a solid into a liquid. The playground "
                    "started wet, so no solid was involved."},
            {"text": "Freezing",
             "correct": False,
             "why": "Freezing would leave ice behind. The playground is dry, "
                    "so the water has left as a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e09",
        "band": "easier",
        "text": "Solid carbon dioxide is called dry ice. Why dry?",
        "options": [
            {"text": "Because it is much colder than ordinary ice.",
             "correct": False,
             "why": "It is far colder, but that is not where the name comes "
                    "from. The name is about what it leaves behind."},
            {"text": "Because it has had all the water taken out of it.",
             "correct": False,
             "why": "There was never any water in it — it is carbon dioxide, "
                    "a different substance altogether."},
            {"text": "Because it turns straight into a gas and leaves no "
                     "puddle.",
             "correct": True},
            {"text": "Because it does not melt until it is warmed a great "
                     "deal.",
             "correct": False,
             "why": "It does not melt at all under normal conditions. It "
                    "sublimes, going solid straight to gas."},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-03-s05",
        "band": "standard",
        "text": "A student sorts “a chocolate bar left on a sunny "
                "windowsill” into the dissolving column. Which test shows it "
                "belongs in the melting one?",
        "options": [
            {"text": "The chocolate goes runny, and only a liquid can "
                     "dissolve in a liquid.",
             "correct": False,
             "why": "Both processes end with something runny. Going runny "
                    "does not tell the two apart."},
            {"text": "It happened outdoors rather than in a cup.",
             "correct": False,
             "why": "Where it happens does not decide it. Butter melts in a "
                    "pan and salt dissolves in a beaker."},
            {"text": "Only one substance is involved, and it was warmed past "
                     "its melting point.",
             "correct": True},
            {"text": "It cannot be reversed, and dissolving can.",
             "correct": False,
             "why": "Cool the chocolate and it sets again — melting reverses "
                    "perfectly well. The test is how many substances are "
                    "involved."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s06",
        "band": "standard",
        "text": "On the heating bench, between the two plateaus, the "
                "thermometer climbs steadily. What is the energy doing during "
                "that climb?",
        "options": [
            {"text": "Breaking particles out of their fixed positions.",
             "correct": False,
             "why": "That happens during a plateau, when the temperature "
                    "refuses to move. Between the plateaus the reading is "
                    "rising."},
            {"text": "Being lost to the room instead of heating the flask.",
             "correct": False,
             "why": "Some energy is always lost to the room, before and after "
                    "the plateaus alike. It cannot explain why the climb "
                    "happens here and not there."},
            {"text": "Making the particles larger, so the substance takes up "
                     "more room.",
             "correct": False,
             "why": "Particles never change size. What heating changes is how "
                    "fast they move."},
            {"text": "Making the particles move faster, which the thermometer "
                     "reports.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s07",
        "band": "standard",
        "text": "A student says the water in a drying puddle has been "
                "destroyed. What is the strongest single piece of evidence "
                "against that?",
        "options": [
            {"text": "Cool the air above it and the same water comes back as "
                     "droplets.",
             "correct": True},
            {"text": "The puddle takes hours to dry, so nothing sudden "
                     "happened to it.",
             "correct": False,
             "why": "How long it takes says nothing about where the water "
                    "went. Slow destruction would still be destruction."},
            {"text": "The ground underneath is still damp, so some water is "
                     "left.",
             "correct": False,
             "why": "That only shows the drying is unfinished. It says "
                    "nothing about the water that has already gone."},
            {"text": "Water is a liquid, and liquids cannot be destroyed.",
             "correct": False,
             "why": "This states the conclusion instead of giving evidence "
                    "for it. The evidence is that the water can be got back."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s08",
        "band": "standard",
        "text": "A student says the bubbles in boiling water are hydrogen and "
                "oxygen, split apart by the heat. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — that is exactly what boiling does.",
             "correct": False,
             "why": "Boiling is a change of state. The water is still water "
                    "throughout, only in a different state."},
            {"text": "Splitting water is a chemical change and needs far more "
                     "energy than a kettle has.",
             "correct": True},
            {"text": "Hydrogen and oxygen would be invisible, and the bubbles "
                     "can be seen.",
             "correct": False,
             "why": "Steam is invisible too — what you see is the bubble's "
                    "edge. The real problem is that boiling does not split "
                    "water at all."},
            {"text": "Hydrogen and oxygen are both liquids at 100 °C, so they "
                     "could not form bubbles.",
             "correct": False,
             "why": "Both are gases at 100 °C. The objection is that boiling "
                    "never produces them in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s09",
        "band": "standard",
        "text": "A cold can of drink taken out on a warm day soon has water "
                "running down its outside. Where has that water come from?",
        "options": [
            {"text": "It has leaked out through the metal of the can.",
             "correct": False,
             "why": "The can is sealed and its level does not drop. The water "
                    "arrives from outside it."},
            {"text": "The can is sweating, the way your skin does when it is "
                     "warm.",
             "correct": False,
             "why": "A can produces nothing of its own. The water is already "
                    "in the air as a gas before it touches the can."},
            {"text": "It is water vapour from the air, condensing on the cold "
                     "surface.",
             "correct": True},
            {"text": "Ice inside the can has melted and soaked through.",
             "correct": False,
             "why": "Nothing passes through the metal, and it happens to cans "
                    "with no ice in them at all."},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-03-h05",
        "band": "harder",
        "text": "On the bench, ice warms from −20 °C to 0 °C much faster than "
                "the water then warms from 0 °C to 100 °C — and the ring "
                "delivers the same energy every second throughout. Ignoring "
                "the size of each temperature rise, what does that comparison "
                "suggest?",
        "options": [
            {"text": "The ring gets weaker as the run goes on.",
             "correct": False,
             "why": "The ring is stated to deliver the same energy every "
                    "second from start to finish. The difference is in the "
                    "substance."},
            {"text": "Some of the water has already escaped from the flask as "
                     "steam.",
             "correct": False,
             "why": "The flask is sealed and the mass never moves. Nothing "
                    "has left."},
            {"text": "Water takes more energy per degree than the same mass "
                     "of ice does.",
             "correct": True},
            {"text": "Water particles are heavier than ice particles.",
             "correct": False,
             "why": "They are the same particles. A change of state never "
                    "alters them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h06",
        "band": "harder",
        "text": "A town on the coast has milder winters and cooler summers "
                "than a town the same distance north but far inland. Which "
                "idea from this lesson helps explain that?",
        "options": [
            {"text": "Sea water is salty, and salt water cannot freeze.",
             "correct": False,
             "why": "Salt lowers the freezing point but does not abolish it — "
                    "and this is about air temperature all year, not about "
                    "freezing."},
            {"text": "The sea is always at the same temperature everywhere.",
             "correct": False,
             "why": "It is not — the sea warms and cools with the seasons. It "
                    "simply does so far less than the land does."},
            {"text": "Water evaporates all through the summer, and "
                     "evaporation always warms the air lying above the sea.",
             "correct": False,
             "why": "Evaporation cools what is left behind rather than "
                    "warming the air. And it would not explain the milder "
                    "winter."},
            {"text": "Water takes a great deal of energy to warm and gives it "
                     "back slowly, so its temperature swings less.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h07",
        "band": "harder",
        "text": "On the bench the melting plateau lasts about 6 minutes. "
                "Separating the particles completely costs roughly seven times "
                "what loosening them costs. About how long should the boiling "
                "plateau last?",
        "options": [
            {"text": "About 40 minutes.",
             "correct": True},
            {"text": "About 6 minutes — the ring's power has not changed.",
             "correct": False,
             "why": "The power is the same, which is exactly why the times "
                    "can be compared. Seven times the energy at the same "
                    "power takes seven times as long."},
            {"text": "About 12 minutes.",
             "correct": False,
             "why": "That is doubling. The comparison in the lesson is about "
                    "seven times, not twice."},
            {"text": "About 90 minutes.",
             "correct": False,
             "why": "That is nearer fifteen times as long. Seven lots of six "
                    "minutes comes to a little over forty."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h08",
        "band": "harder",
        "text": "100 g of water is frozen in a sealed bottle and the ice "
                "takes up noticeably more room than the water did. Has matter "
                "been created?",
        "options": [
            {"text": "Yes — the extra volume has to be made of something.",
             "correct": False,
             "why": "Volume is not matter. The extra room is empty space "
                    "between the particles, and it weighs nothing."},
            {"text": "No — the same particles are held further apart, and the "
                     "mass is still 100 g.",
             "correct": True},
            {"text": "Yes — freezing adds particles from the air around the "
                     "bottle.",
             "correct": False,
             "why": "The bottle is sealed, so nothing can get in. Sealed or "
                    "not, freezing does not draw in air."},
            {"text": "No — the volume has not really changed, it only looks "
                     "as though it has.",
             "correct": False,
             "why": "The volume genuinely does increase, which is why bottles "
                    "of water crack in a freezer. What stays fixed is the "
                    "mass."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h09",
        "band": "harder",
        "text": "A fridge lets a liquid evaporate in a pipe inside the cold "
                "compartment, then condense in a pipe on the back. Why does "
                "that move energy out of the fridge?",
        "options": [
            {"text": "Because the gas inside the pipe is far colder than "
                     "everything else inside the fridge compartment.",
             "correct": False,
             "why": "The temperature of the pipe is a result, not the cause. "
                    "What matters is the energy taken in by evaporating and "
                    "given out by condensing."},
            {"text": "Because the pipes carry the warm air out through the "
                     "back of the fridge.",
             "correct": False,
             "why": "Nothing inside the fridge is carried outside. What "
                    "travels is the liquid in a sealed loop, and what it "
                    "carries is energy."},
            {"text": "Because evaporating takes energy in inside, and "
                     "condensing gives the same energy out at the back.",
             "correct": True},
            {"text": "Because a fridge destroys the energy of the food it "
                     "cools.",
             "correct": False,
             "why": "Energy is not destroyed. It is moved from inside the "
                    "fridge to the room, which is why the back of a fridge is "
                    "warm."},
        ],
        "figure": None,
    },
]
