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
    # ── easier · the MRB-338 expansion ───────────────────────────
    {
        "id": "c1-03-e10",
        "band": "easier",
        "text": "A block of butter left in a warm pan stops being a solid "
                "block and becomes a pool of liquid. Name this change of "
                "state.",
        "options": [
            {"text": "Condensing, because the pan has warmed the butter "
                     "from underneath it.",
             "correct": False,
             "why": "Condensing starts with a gas and ends with a liquid. "
                    "The butter started as a solid."},
            {"text": "Evaporating, because the butter has been warmed "
                     "until it can flow across the pan.",
             "correct": False,
             "why": "Evaporating starts with a liquid and ends with a gas. "
                    "The butter has ended as a liquid, not a gas."},
            {"text": "Dissolving, because the butter has spread itself out "
                     "over the base of the pan.",
             "correct": False,
             "why": "Dissolving needs a second substance for the first to "
                    "spread through. Only butter is involved here."},
            {"text": "Melting, because one substance has been warmed past "
                     "its melting point.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e11",
        "band": "easier",
        "text": "Warm damp air touches a cold window and small drops of "
                "water appear on the glass. Name this change of state.",
        "options": [
            {"text": "Condensing, because a gas in the air has been cooled "
                     "into a liquid.",
             "correct": True},
            {"text": "Melting, because ice on the cold glass has warmed "
                     "into drops of water.",
             "correct": False,
             "why": "There was no ice on the glass to start with. The "
                    "water arrived as a gas in the air."},
            {"text": "Evaporating, because the drops have come out of the "
                     "warm damp air.",
             "correct": False,
             "why": "Evaporating goes the other way — liquid to gas. Here "
                    "a gas has become a liquid."},
            {"text": "Freezing, because the glass is colder than the air "
                     "in the room.",
             "correct": False,
             "why": "Freezing ends with a solid. The window carries liquid "
                    "drops, not ice."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e12",
        "band": "easier",
        "text": "Sublimation is a solid turning straight into a gas with "
                "no liquid in between. What is the reverse of sublimation?",
        "options": [
            {"text": "A liquid turning into a solid, which is what happens "
                     "to water in a freezer.",
             "correct": False,
             "why": "That is freezing, and it is a change every liquid can "
                    "make. The reverse of sublimation has to start as a "
                    "gas."},
            {"text": "A gas turning into a liquid, which then cools "
                     "further until it becomes a solid.",
             "correct": False,
             "why": "That is condensing followed by freezing — two changes "
                    "with a liquid stage in the middle."},
            {"text": "A gas turning straight into a solid, with no liquid "
                     "in between.",
             "correct": True},
            {"text": "A solid turning into a liquid, which is then warmed "
                     "until it becomes a gas.",
             "correct": False,
             "why": "That is melting followed by boiling, and it is the "
                    "ordinary route rather than the reverse of anything."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e13",
        "band": "easier",
        "text": "Pure ethanol boils at 78 °C. What state is ethanol in at "
                "90 °C?",
        "options": [
            {"text": "A gas, because 90 °C is above its boiling point of "
                     "78 °C.",
             "correct": True},
            {"text": "A liquid, because 90 °C is below the 100 °C at which "
                     "things boil.",
             "correct": False,
             "why": "100 °C is water's boiling point, not everything's. "
                    "Each substance has its own, and ethanol's is 78 °C."},
            {"text": "A solid, because 90 °C is nowhere near warm enough "
                     "to melt it.",
             "correct": False,
             "why": "Ethanol is a liquid at room temperature and 90 °C is "
                    "warmer than that, so it cannot have become a solid."},
            {"text": "Half liquid and half gas, because 90 °C is past the "
                     "boiling point given.",
             "correct": False,
             "why": "A liquid and its gas sit together only while it is "
                    "boiling, at 78 °C. Past that, it is all gas."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e14",
        "band": "easier",
        "text": "Aluminium melts at 660 °C. At what temperature does "
                "molten aluminium freeze?",
        "options": [
            {"text": "At 0 °C, because that is the temperature at which "
                     "any liquid freezes.",
             "correct": False,
             "why": "0 °C is water's freezing point. Every substance has "
                    "its own, and aluminium's is far higher."},
            {"text": "At some temperature below 660 °C, because freezing "
                     "always needs extra cooling.",
             "correct": False,
             "why": "It cools to 660 °C and freezes there. The energy "
                    "comes out at that temperature, not below it."},
            {"text": "At 660 °C, the same temperature used in the opposite "
                     "direction.",
             "correct": True},
            {"text": "At room temperature, because that is where you find "
                     "aluminium as a solid.",
             "correct": False,
             "why": "Aluminium is solid at room temperature, but it became "
                    "solid much earlier, on the way down, at 660 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e15",
        "band": "easier",
        "text": "Which of these changes of state takes energy IN from the "
                "surroundings?",
        "options": [
            {"text": "Freezing, because the particles have to be pushed "
                     "into their fixed positions.",
             "correct": False,
             "why": "Freezing gives energy out. That is why a freezer has "
                    "to keep removing energy to make ice."},
            {"text": "Condensing, because the gas has to be squeezed into "
                     "a smaller space.",
             "correct": False,
             "why": "Condensing gives energy out — it is what makes a "
                    "steam scald so much worse than hot water."},
            {"text": "Frost forming, because ice is colder than the air it "
                     "forms out of.",
             "correct": False,
             "why": "That change gives energy out too. Being cold is not "
                    "the same as taking energy in."},
            {"text": "Boiling, because the particles have to be separated "
                     "completely.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e16",
        "band": "easier",
        "text": "Whereabouts in a liquid does evaporation happen?",
        "options": [
            {"text": "At the surface only, which is the one place a "
                     "particle can leave from.",
             "correct": True},
            {"text": "All through the liquid, which is where the bubbles "
                     "come from.",
             "correct": False,
             "why": "That is boiling, and the bubbles are the sign of it. "
                    "Evaporation makes no bubbles."},
            {"text": "At the bottom, because that is the part nearest to "
                     "whatever is warming it.",
             "correct": False,
             "why": "A puddle evaporates on cold ground with nothing "
                    "warming it from below. Particles escape from the top."},
            {"text": "At the sides, where the liquid touches the walls of "
                     "its container.",
             "correct": False,
             "why": "Water spilt flat on a bench has no walls at all and "
                    "still evaporates, from its top surface."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e17",
        "band": "easier",
        "text": "At what temperatures can evaporation happen?",
        "options": [
            {"text": "Only at the boiling point of the liquid, which for "
                     "water is 100 °C.",
             "correct": False,
             "why": "That is boiling. Washing dries on a line at 8 °C, and "
                    "no part of it ever reaches 100 °C."},
            {"text": "Only above room temperature, because the liquid must "
                     "be warmed first.",
             "correct": False,
             "why": "A puddle in a cold garage disappears over a week with "
                    "nothing warming it at all."},
            {"text": "At any temperature at all, so long as the substance "
                     "is a liquid to begin with.",
             "correct": True},
            {"text": "Only in bright sunshine, which supplies the energy "
                     "the particles need.",
             "correct": False,
             "why": "Sunshine speeds it up. Washing still dries overnight "
                    "in the dark, more slowly."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e18",
        "band": "easier",
        "text": "A load of wet washing has to be dried. Which of these "
                "will dry it fastest?",
        "options": [
            {"text": "Left in a heap in the basket, where the warmth of "
                     "the pile is kept in.",
             "correct": False,
             "why": "A heap has hardly any surface exposed, and only the "
                    "surface can evaporate. It dries slowest of all."},
            {"text": "Hung up in a cold cupboard with the door closed, so "
                     "that nothing can blow it about.",
             "correct": False,
             "why": "Cold and still air are the two conditions that slow "
                    "evaporation down most."},
            {"text": "Spread out on a line on a warm, windy day, with all "
                     "of it exposed.",
             "correct": True},
            {"text": "Folded into a thick square on a warm radiator, so "
                     "the heat reaches it.",
             "correct": False,
             "why": "The warmth helps, but folding hides nearly all the "
                    "wet surface, and the inside stays damp for hours."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e19",
        "band": "easier",
        "text": "20 g of water in a sealed tub is put into a freezer and "
                "turns completely into ice. What is the mass of the ice?",
        "options": [
            {"text": "20 g, because freezing rearranges the particles "
                     "without removing any.",
             "correct": True},
            {"text": "More than 20 g, because ice takes up more room than "
                     "the water it froze from.",
             "correct": False,
             "why": "Ice does take up more room, but taking up more room "
                    "is not the same as having more mass."},
            {"text": "Less than 20 g, because some of the water is left "
                     "behind as vapour in the freezer.",
             "correct": False,
             "why": "The tub is sealed, so nothing can leave it. Freezing "
                    "removes no particles in any case."},
            {"text": "It cannot be said without knowing how cold the "
                     "freezer was set.",
             "correct": False,
             "why": "How cold the freezer is decides how fast it freezes, "
                    "not how much matter ends up in the tub."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e20",
        "band": "easier",
        "text": "Why is melting described as a physical change rather than "
                "a chemical one?",
        "options": [
            {"text": "Because it happens quickly, and a chemical change "
                     "always takes far longer to finish.",
             "correct": False,
             "why": "Speed decides nothing. An explosion is a chemical "
                    "change and it is over in an instant."},
            {"text": "Because it needs heat, and a chemical change is one "
                     "that happens without any heating.",
             "correct": False,
             "why": "Plenty of chemical changes need heating too, such as "
                    "baking a cake or burning a fuel."},
            {"text": "Because you can see it happening, and a chemical "
                     "change is always too small to be seen.",
             "correct": False,
             "why": "Chemical changes are often easy to see — a firework, "
                    "or a nail going rusty."},
            {"text": "Because no new substance is made — the same "
                     "particles are simply arranged differently.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e21",
        "band": "easier",
        "text": "Oxygen melts at −219 °C and boils at −183 °C. What state "
                "is oxygen in at −200 °C?",
        "options": [
            {"text": "Solid, because −200 °C is an extremely cold "
                     "temperature to be at.",
             "correct": False,
             "why": "It only becomes solid below −219 °C, and −200 °C is "
                    "warmer than that."},
            {"text": "Liquid, because −200 °C sits between its two fixed "
                     "points.",
             "correct": True},
            {"text": "Gas, because oxygen is the gas we breathe whatever "
                     "is done to it.",
             "correct": False,
             "why": "Oxygen is a gas in a warm room, but −200 °C is below "
                    "its boiling point of −183 °C, so it has condensed."},
            {"text": "Part solid and part liquid, because −200 °C lies "
                     "between the two numbers.",
             "correct": False,
             "why": "Two states sit together only at a melting or boiling "
                    "point. −200 °C is between them, not at either."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e22",
        "band": "easier",
        "text": "Which two changes of state happen at 0 °C for pure water?",
        "options": [
            {"text": "Melting and freezing, one doorway used in opposite "
                     "directions.",
             "correct": True},
            {"text": "Boiling and condensing, which are the pair that go "
                     "in opposite directions.",
             "correct": False,
             "why": "They are a pair going in opposite directions, but for "
                    "water they happen at 100 °C."},
            {"text": "Melting and boiling, which are the two changes that "
                     "need energy putting in.",
             "correct": False,
             "why": "Both do need energy in, but they happen at two "
                    "different temperatures — 0 °C and 100 °C."},
            {"text": "Freezing and evaporating, the two changes seen in "
                     "cold weather.",
             "correct": False,
             "why": "Evaporation happens at any temperature at all, so it "
                    "is not tied to 0 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e23",
        "band": "easier",
        "text": "Give one difference between boiling and evaporating.",
        "options": [
            {"text": "Boiling makes a gas and evaporating makes a liquid "
                     "that has spread out thinly.",
             "correct": False,
             "why": "Both end with a gas. That is what makes the two so "
                    "easy to muddle."},
            {"text": "Boiling happens throughout the liquid; evaporating "
                     "happens only at the surface.",
             "correct": True},
            {"text": "Boiling can be reversed by cooling and evaporating "
                     "cannot be reversed at all.",
             "correct": False,
             "why": "Both can be reversed. Cool the gas from either and it "
                    "condenses back into a liquid."},
            {"text": "Boiling changes the mass of the substance and "
                     "evaporating leaves the mass alone.",
             "correct": False,
             "why": "Neither changes the mass. The water that leaves a pan "
                    "is still water, out in the room."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e24",
        "band": "easier",
        "text": "What happens to the forces holding the particles together "
                "when a solid melts?",
        "options": [
            {"text": "They are weakened enough for the particles to slide "
                     "past one another, but not broken.",
             "correct": True},
            {"text": "They disappear altogether, which is why a liquid can "
                     "be poured out.",
             "correct": False,
             "why": "If they disappeared the particles would fly apart and "
                    "you would have a gas. They still hold, more loosely."},
            {"text": "They get stronger, which is what pulls the particles "
                     "out of their fixed rows.",
             "correct": False,
             "why": "Stronger forces would hold the particles more tightly "
                    "in place, not release them."},
            {"text": "They stay exactly as they were, and it is the "
                     "particles themselves that go soft.",
             "correct": False,
             "why": "Particles never go soft or change in any way. Only "
                    "their arrangement and their energy change."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e25",
        "band": "easier",
        "text": "What is meant by the melting point of a substance?",
        "options": [
            {"text": "The temperature at which it changes from a solid "
                     "into a liquid, and back again.",
             "correct": True},
            {"text": "The temperature at which it is safe to touch, now "
                     "that it is not solid.",
             "correct": False,
             "why": "Melting points have nothing to do with safety. Molten "
                    "iron melts at 1538 °C and is lethal."},
            {"text": "The length of time it takes for the whole of the "
                     "solid to turn into a liquid.",
             "correct": False,
             "why": "That is a time, in minutes. A melting point is a "
                    "temperature, in degrees Celsius."},
            {"text": "The amount of energy that has to be supplied before "
                     "any of the solid will melt.",
             "correct": False,
             "why": "That is an amount of energy, in joules. A melting "
                    "point is a temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e26",
        "band": "easier",
        "text": "Which of these is an example of condensation?",
        "options": [
            {"text": "A puddle on the playground drying up over a sunny "
                     "morning.",
             "correct": False,
             "why": "That is evaporation — a liquid becoming a gas. "
                    "Condensation goes the other way."},
            {"text": "An ice lolly going soft and dripping in a warm hand.",
             "correct": False,
             "why": "That is melting — a solid becoming a liquid. No gas "
                    "is involved anywhere in it."},
            {"text": "Wax running down the side of a candle that has been "
                     "burning a while.",
             "correct": False,
             "why": "That is melting too. The solid wax has been warmed "
                    "past its melting point."},
            {"text": "Mist appearing on a bathroom mirror while a hot "
                     "shower runs.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e27",
        "band": "easier",
        "text": "Changes of state are described as reversible. What does "
                "reversible mean?",
        "options": [
            {"text": "It can happen more than once to the same piece of a "
                     "substance.",
             "correct": False,
             "why": "Happening again is not the same as being undone. Rust "
                    "can form again and again and never reverses."},
            {"text": "It can be undone, so that the substance goes back to "
                     "what it was before.",
             "correct": True},
            {"text": "It happens equally easily in both directions, "
                     "needing no energy either way.",
             "correct": False,
             "why": "Energy is needed in one direction and given out in "
                    "the other. Reversible does not mean free."},
            {"text": "It goes backwards on its own, without anything "
                     "having to be done to it.",
             "correct": False,
             "why": "Water does not freeze on its own in a warm room. "
                    "Something has to change for it to reverse."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e28",
        "band": "easier",
        "text": "Steam is water in the gas state. What does steam look "
                "like?",
        "options": [
            {"text": "White and cloudy, which is how you can see it "
                     "leaving a kettle.",
             "correct": False,
             "why": "The white cloud is steam that has already condensed "
                    "into tiny drops of liquid water."},
            {"text": "Nothing at all — it is a colourless gas and cannot "
                     "be seen.",
             "correct": True},
            {"text": "Grey and smoky, in the same way as the smoke that "
                     "comes off a fire.",
             "correct": False,
             "why": "Smoke is tiny solid particles from burning. Nothing "
                    "is burning when water boils."},
            {"text": "Clear with a slight blue tint, in the way that deep "
                     "water looks blue.",
             "correct": False,
             "why": "Steam has no colour whatsoever. There is nothing "
                    "there for the eye to catch."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e29",
        "band": "easier",
        "text": "Sweat on your skin evaporates. What effect does that have "
                "on your skin?",
        "options": [
            {"text": "It cools it, because the escaping particles take "
                     "energy from the skin.",
             "correct": True},
            {"text": "It warms it, because the sweat has to be given "
                     "energy before it can leave.",
             "correct": False,
             "why": "The energy comes FROM the skin, so the skin is left "
                    "with less of it and cools."},
            {"text": "It leaves the temperature alone and simply makes the "
                     "skin feel drier.",
             "correct": False,
             "why": "The skin does dry, but energy has left with the "
                    "escaping particles, so it is genuinely cooler."},
            {"text": "It warms it, because a wet surface holds energy in "
                     "better than a dry one.",
             "correct": False,
             "why": "This has it backwards. Sweating is one of the main "
                    "ways a body gets rid of energy."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e30",
        "band": "easier",
        "text": "Which of these is NOT a change of state?",
        "options": [
            {"text": "Sublimation, in which a solid becomes a gas without "
                     "ever being a liquid.",
             "correct": False,
             "why": "Sublimation is a change of state — the one that skips "
                    "the liquid stage."},
            {"text": "Condensing, in which a gas cools until it becomes a "
                     "liquid again.",
             "correct": False,
             "why": "Condensing is a change of state, and it is the "
                    "reverse of boiling."},
            {"text": "Dissolving, in which one substance spreads out among "
                     "the particles of another.",
             "correct": True},
            {"text": "Freezing, in which a liquid is cooled until it "
                     "becomes a solid.",
             "correct": False,
             "why": "Freezing is a change of state, and it is the reverse "
                    "of melting."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e31",
        "band": "easier",
        "text": "What happens to the particles when a gas condenses into a "
                "liquid?",
        "options": [
            {"text": "They break into smaller pieces, which is why a "
                     "liquid takes up less room.",
             "correct": False,
             "why": "Particles are never broken apart by a change of "
                    "state. The same particles simply move closer "
                    "together."},
            {"text": "They shrink, so the same number of them can fit into "
                     "a much smaller space.",
             "correct": False,
             "why": "Particles do not change size. The space between them "
                    "is what closes up."},
            {"text": "They lose energy, slow down, and are pulled close "
                     "together again.",
             "correct": True},
            {"text": "They gain energy from the cold surface, which draws "
                     "them out of the air.",
             "correct": False,
             "why": "They give energy out to the cold surface. That is why "
                    "a window steams up on its coldest side."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-e32",
        "band": "easier",
        "text": "Ice is being heated steadily and is halfway through "
                "melting. What is its temperature doing?",
        "options": [
            {"text": "Rising steadily, in step with the energy going into "
                     "it all the time.",
             "correct": False,
             "why": "The energy is going into breaking the particles apart "
                    "instead, so the reading holds still."},
            {"text": "Falling, because melting is a change that takes "
                     "energy away from the ice.",
             "correct": False,
             "why": "Melting takes energy in, and in any case the "
                    "temperature holds rather than falling."},
            {"text": "Rising, but far more slowly than it did before any "
                     "of the ice had melted.",
             "correct": False,
             "why": "It does not creep up slowly. It stops dead until the "
                    "last of the ice has gone."},
            {"text": "Staying exactly where it is until all the ice has "
                     "melted.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── standard · the MRB-338 expansion ─────────────────────────
    {
        "id": "c1-03-s10",
        "band": "standard",
        "text": "A block of ice at −15 °C is taken out of a freezer and "
                "left in a room at 20 °C. Describe what happens to it, in "
                "order.",
        "options": [
            {"text": "It warms up to 0 °C, then melts at 0 °C while the "
                     "temperature holds still, and only then warms again.",
             "correct": True},
            {"text": "It melts straight away in the warm room, and the "
                     "puddle then warms up from −15 °C.",
             "correct": False,
             "why": "Ice at −15 °C is 15 degrees too cold to melt. It has "
                    "to reach 0 °C before any of it can turn to liquid."},
            {"text": "It warms all the way to 20 °C as a solid, and only "
                     "then begins to turn into water.",
             "correct": False,
             "why": "No ice can be warmed past 0 °C. It melts there, and "
                    "the water made is what warms towards 20 °C."},
            {"text": "It warms to 0 °C and keeps warming steadily all the "
                     "while, with the melting happening as it goes.",
             "correct": False,
             "why": "The climb stops at 0 °C. The reading will not move "
                    "again until the last of the ice has melted."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s11",
        "band": "standard",
        "text": "Salt melts at 801 °C and boils at 1465 °C. A technician "
                "needs a beaker of liquid salt. What must be done?",
        "options": [
            {"text": "Stir the salt into hot water until none of it can be "
                     "seen any more.",
             "correct": False,
             "why": "That gives salt dissolved in water, which is two "
                    "substances. Liquid salt is salt on its own."},
            {"text": "Cool the salt below 801 °C, which is the point at "
                     "which it stops being a solid.",
             "correct": False,
             "why": "Cooling a solid keeps it solid. 801 °C is the "
                    "temperature it has to be heated past."},
            {"text": "Heat the salt past 801 °C, which is the point at "
                     "which it melts.",
             "correct": True},
            {"text": "Heat the salt past 1465 °C, the higher of the two "
                     "temperatures given.",
             "correct": False,
             "why": "Past 1465 °C the salt has boiled and is a gas. The "
                    "liquid sits between the two numbers."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s12",
        "band": "standard",
        "text": "The same 50 cm³ of water is poured into a wide flat tray "
                "in one room and a tall narrow jar in another. Both rooms "
                "are at 20 °C. Which dries out first, and why?",
        "options": [
            {"text": "The jar, because the water in it is deeper and holds "
                     "more particles.",
             "correct": False,
             "why": "Only the particles at the surface can escape, and "
                    "depth does not add any surface."},
            {"text": "The jar, because the narrow neck funnels the "
                     "escaping particles upwards and out.",
             "correct": False,
             "why": "A narrow neck does not help. It gives a small "
                    "surface, which is what limits evaporation."},
            {"text": "Neither — the same amount of water at the same "
                     "temperature must take the same time.",
             "correct": False,
             "why": "Amount and temperature are not the only things that "
                    "matter. Surface area changes the rate a great deal."},
            {"text": "The tray, because it offers a far larger surface for "
                     "particles to escape from.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s13",
        "band": "standard",
        "text": "Washing dries faster on a breezy day than on a still day "
                "at the same temperature. Explain why the breeze helps.",
        "options": [
            {"text": "The breeze carries the escaped water particles away, "
                     "so far fewer of them return to the washing again.",
             "correct": True},
            {"text": "The breeze pushes the water particles out of the "
                     "cloth, which is work the washing cannot do alone.",
             "correct": False,
             "why": "The particles leave on their own, using their own "
                    "energy. Moving air does not push them out."},
            {"text": "The breeze warms the washing, and warmer water "
                     "always evaporates faster than cold water does.",
             "correct": False,
             "why": "The stem says the two days are at the same "
                    "temperature, and moving air does not warm anything."},
            {"text": "The breeze breaks the water into smaller drops, and "
                     "smaller drops turn into a gas more readily.",
             "correct": False,
             "why": "Water in cloth is not broken into drops by wind, and "
                    "drop size is not what the escape depends on."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s14",
        "band": "standard",
        "text": "Explain why the water left in a dish is slightly cooler "
                "after some of it has evaporated.",
        "options": [
            {"text": "The dish has been left standing, and anything left "
                     "standing cools to the temperature of the room.",
             "correct": False,
             "why": "It ends up cooler than the room, which standing alone "
                    "cannot explain."},
            {"text": "Evaporation destroys some of the energy the water "
                     "was holding, so less of it is left behind.",
             "correct": False,
             "why": "Energy is never destroyed. It leaves with the "
                    "particles that escaped, and is still theirs."},
            {"text": "The fastest particles are the ones that escape, so "
                     "the ones left behind are slower on average.",
             "correct": True},
            {"text": "There is less water than there was, and a smaller "
                     "amount of water is always at a lower temperature.",
             "correct": False,
             "why": "Temperature does not depend on how much there is. A "
                    "spoonful of boiling water is still at 100 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s15",
        "band": "standard",
        "text": "A liquid is cooled steadily in a freezer. Its temperature "
                "falls, then holds at −78 °C for several minutes while it "
                "turns solid, then falls again. What is happening during "
                "those minutes?",
        "options": [
            {"text": "The freezer has stopped removing energy for a while, "
                     "so the temperature has nothing to make it fall.",
             "correct": False,
             "why": "The freezer works steadily throughout. If it stopped, "
                    "the substance would not go on freezing."},
            {"text": "Energy is still leaving, and it is the energy "
                     "released as the particles are pulled into fixed "
                     "positions.",
             "correct": True},
            {"text": "The liquid has reached the coldest temperature it "
                     "can reach, and cannot go below it while it is solid.",
             "correct": False,
             "why": "The reading falls again afterwards, so −78 °C is "
                    "plainly not a floor."},
            {"text": "The thermometer is reading the freezer's air instead "
                     "of the substance for that part of the run.",
             "correct": False,
             "why": "The freezer's air is colder than −78 °C throughout, "
                    "so it would not give a steady reading there."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s16",
        "band": "standard",
        "text": "A substance is cooled from a gas all the way down to a "
                "solid, and its temperature is recorded throughout. At "
                "which two temperatures will the reading hold still?",
        "options": [
            {"text": "At its boiling point and then at its melting point, "
                     "in that order.",
             "correct": True},
            {"text": "At 100 °C and at 0 °C, where any substance changes "
                     "state.",
             "correct": False,
             "why": "Those are water's two fixed points. Every substance "
                    "has its own pair."},
            {"text": "At room temperature and at 0 °C, where cooling is "
                     "slowed by the surroundings.",
             "correct": False,
             "why": "The surroundings change how fast it cools, not where "
                    "the reading holds still."},
            {"text": "At its boiling point only, since freezing gives "
                     "energy out rather than taking it in.",
             "correct": False,
             "why": "Freezing does release energy, and that release is "
                    "exactly what holds the reading still a second time."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s17",
        "band": "standard",
        "text": "Boiling 1 g of water at 100 °C into steam at 100 °C takes "
                "2260 J. How much energy is given out when 1 g of steam at "
                "100 °C condenses back to water at 100 °C?",
        "options": [
            {"text": "2260 J, because condensing is boiling run backwards.",
             "correct": True},
            {"text": "None, because both start and finish sit at exactly "
                     "100 °C.",
             "correct": False,
             "why": "The temperature does not change, but the change of "
                    "state itself releases energy."},
            {"text": "More than 2260 J, because the particles have to be "
                     "pulled together as well.",
             "correct": False,
             "why": "Condensing is boiling run backwards, so it gives back "
                    "exactly what boiling cost."},
            {"text": "Less than 2260 J, because some energy stays with the "
                     "water it becomes.",
             "correct": False,
             "why": "Whatever stays with the water is what keeps it at 100 "
                    "°C. The plateau's energy comes back in full."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s18",
        "band": "standard",
        "text": "Which of these can be undone simply by cooling what is "
                "left?",
        "options": [
            {"text": "A slice of bread browning into toast under a grill.",
             "correct": False,
             "why": "Toasting is a chemical change. Cooling the toast "
                    "never gives bread back."},
            {"text": "An egg turning white and firm in a hot frying pan.",
             "correct": False,
             "why": "Cooking an egg makes new substances. A cold cooked "
                    "egg stays cooked."},
            {"text": "A steel nail going rusty after a week outdoors in "
                     "the rain.",
             "correct": False,
             "why": "Rust is a new substance made from iron and oxygen. "
                    "Cooling does not unmake it."},
            {"text": "Water boiling away into steam in an open pan on a "
                     "hob.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s19",
        "band": "standard",
        "text": "A pan of water is boiled dry on a hob in an ordinary "
                "kitchen. Where has the water gone?",
        "options": [
            {"text": "It has been destroyed by the heat of the hob, which "
                     "is why the pan is empty.",
             "correct": False,
             "why": "A hob cannot destroy matter. Boiling only changes "
                    "water's state."},
            {"text": "It has turned into air, and is now part of the air "
                     "in the kitchen.",
             "correct": False,
             "why": "It is not air. It is water in the gas state, mixed in "
                    "among the air."},
            {"text": "It is in the kitchen as water vapour, and the mass "
                     "of the room has not changed.",
             "correct": True},
            {"text": "It has soaked into the metal of the pan, which is "
                     "why a boiled-dry pan is hard to clean.",
             "correct": False,
             "why": "Water does not soak into steel. The marks left are "
                    "solids that were dissolved in the water."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s20",
        "band": "standard",
        "text": "Small bubbles cling to the sides of a pan of water long "
                "before it reaches 100 °C. What are they?",
        "options": [
            {"text": "Steam, because water starts making steam as soon as "
                     "it begins to warm up at all.",
             "correct": False,
             "why": "Steam bubbles form only once the water reaches 100 °C. "
                    "Below that, no part of it is boiling."},
            {"text": "Empty spaces opened up in the water by the pan "
                     "expanding as it is heated.",
             "correct": False,
             "why": "A bubble of nothing would be crushed instantly by the "
                    "water pressing in around it."},
            {"text": "Hydrogen and oxygen, since heating starts to break "
                     "the water apart into gases.",
             "correct": False,
             "why": "Breaking water apart is a chemical change needing far "
                    "more energy than a hob supplies."},
            {"text": "Air that was dissolved in the cold water, driven out "
                     "of it as the water warms.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s21",
        "band": "standard",
        "text": "On a cold winter day the windows of a warm house mist up "
                "on the inside, not the outside. Explain why that side.",
        "options": [
            {"text": "The warm indoor air carries water vapour, and that "
                     "vapour condenses when it meets the cold glass.",
             "correct": True},
            {"text": "The cold outdoor air is drier, and dry air pulls "
                     "moisture through the glass towards itself.",
             "correct": False,
             "why": "Nothing passes through the glass. The water was "
                    "already in the room as a gas."},
            {"text": "Water from the rain outside soaks slowly through the "
                     "window and gathers on the warmer side.",
             "correct": False,
             "why": "Glass is not porous, and windows mist up indoors on "
                    "dry days as well."},
            {"text": "The glass itself gives off water when it is cooled, "
                     "in the same way that a cold can does.",
             "correct": False,
             "why": "Neither glass nor a can gives off water. Both collect "
                    "it from the air touching them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s22",
        "band": "standard",
        "text": "Grass is often wet at dawn after a clear night, even "
                "though no rain has fallen. Explain how the water got "
                "there.",
        "options": [
            {"text": "The ground pushes water up to the surface overnight, "
                     "as fields are wettest early.",
             "correct": False,
             "why": "Dew forms on car roofs and garden tables too, which "
                    "no water can be pushed up into."},
            {"text": "Water vapour in the air condensed onto the grass as "
                     "it cooled through the night.",
             "correct": True},
            {"text": "The weight of the cold air above pressed the water "
                     "vapour down onto the blades of grass.",
             "correct": False,
             "why": "Nothing presses vapour out of the air. It turns to "
                    "liquid because the grass itself has cooled."},
            {"text": "The grass makes water while it grows, and the plant "
                     "releases it once the sun goes down.",
             "correct": False,
             "why": "Dew forms just as readily on stone and metal, which "
                    "grow nothing at all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s23",
        "band": "standard",
        "text": "Sugar melts at 186 °C and salt at 801 °C. An unlabelled "
                "white powder is heated and turns to liquid at 802 °C. "
                "What can be concluded?",
        "options": [
            {"text": "It is sugar, because 802 °C is far above the "
                     "temperature sugar melts at.",
             "correct": False,
             "why": "Sugar would have melted at 186 °C, hundreds of "
                    "degrees earlier, and never lasted to 802 °C."},
            {"text": "It could be either, because a melting point shifts "
                     "with the rate of heating.",
             "correct": False,
             "why": "A pure substance melts at its own fixed temperature, "
                    "which is why the measurement is worth making."},
            {"text": "It is neither, because a pure substance melts at "
                     "exactly the book value.",
             "correct": False,
             "why": "802 °C against 801 °C is ordinary measurement error, "
                    "not a different substance."},
            {"text": "It is likely to be the salt, whose melting point is "
                     "801 °C.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s24",
        "band": "standard",
        "text": "What has to happen to the particles of a liquid before it "
                "can boil?",
        "options": [
            {"text": "They must gain enough energy to break away from one "
                     "another completely and move far apart.",
             "correct": True},
            {"text": "They must gain enough energy to grow larger and fill "
                     "the space above.",
             "correct": False,
             "why": "Particles never grow. The space they spread into is "
                    "empty, not filled by bigger particles."},
            {"text": "They must gain enough energy to split into the two "
                     "gases the liquid is made from.",
             "correct": False,
             "why": "Splitting a substance up is a chemical change. "
                    "Boiling leaves the same particles as before."},
            {"text": "They must lose enough energy to stop being pulled "
                     "downwards by the liquid beneath them.",
             "correct": False,
             "why": "Boiling needs energy in, not out, and the pull it "
                    "overcomes is between particles."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s25",
        "band": "standard",
        "text": "A student writes: “When ice melts, each particle goes "
                "soft and squashy, and that is what lets the water flow.” "
                "What is wrong with that?",
        "options": [
            {"text": "The particles do go soft, but that is the result of "
                     "melting rather than its cause.",
             "correct": False,
             "why": "They do not go soft at all. Nothing about a particle "
                    "changes during a change of state."},
            {"text": "Only the particles at the surface go soft, and the "
                     "ones deeper in the ice stay hard.",
             "correct": False,
             "why": "No particle anywhere goes soft. Softness belongs to "
                    "materials, not to single particles."},
            {"text": "A particle never changes at all — only its "
                     "arrangement and its energy do.",
             "correct": True},
            {"text": "It should say the particles go soft when the water "
                     "boils, not when it melts.",
             "correct": False,
             "why": "Boiling changes a particle no more than melting does. "
                    "Only the spacing and the energy change."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s26",
        "band": "standard",
        "text": "A pan of water sits at 100 °C and the reading will not "
                "climb. A student says the ring must have switched itself "
                "off. What single observation shows they are wrong?",
        "options": [
            {"text": "The reading has sat at 100 °C for a few seconds "
                     "without moving at all.",
             "correct": False,
             "why": "A few seconds proves nothing. A pan taken off the heat "
                    "holds 100 °C for a while too."},
            {"text": "The pan and its handle are both still far too hot to "
                     "be touched with a bare hand.",
             "correct": False,
             "why": "A pan stays hot for many minutes after a ring is "
                    "turned off, so this settles nothing."},
            {"text": "The water is at 100 °C, which is much hotter than "
                     "the temperature of the kitchen around it.",
             "correct": False,
             "why": "Water taken off the heat is also hotter than the "
                    "kitchen. Being hot does not prove energy is arriving."},
            {"text": "The pan is still boiling hard and steadily losing "
                     "water, which takes energy to do.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s27",
        "band": "standard",
        "text": "Steam at 120 °C is cooled all the way down to −20 °C. "
                "Name the two changes of state it goes through, in order.",
        "options": [
            {"text": "Freezing at 100 °C, then condensing at 0 °C.",
             "correct": False,
             "why": "The names are the wrong way round. A gas condenses "
                    "first, and a liquid freezes second."},
            {"text": "Condensing at 100 °C, then freezing at 0 °C.",
             "correct": True},
            {"text": "Melting at 100 °C, then evaporating at 0 °C.",
             "correct": False,
             "why": "Both of those go the warming way. Cooling cannot melt "
                    "anything or drive off a gas."},
            {"text": "Condensing at 100 °C only, since ice needs to be far "
                     "colder than −20 °C to form.",
             "correct": False,
             "why": "Water freezes at 0 °C, so −20 °C is twenty degrees "
                    "colder than it needs to be."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s28",
        "band": "standard",
        "text": "A lawn is dry at dusk and the air never rises above −4 °C "
                "all night, yet by morning the grass is coated in ice "
                "crystals. Where did the ice come from?",
        "options": [
            {"text": "Dew settled on the grass first and then froze once "
                     "the air dropped below zero.",
             "correct": False,
             "why": "The air never reached 0 °C, so no liquid dew could "
                    "have settled at any point in the night."},
            {"text": "Water vapour in the air turned straight into ice on "
                     "the cold grass, with no liquid stage.",
             "correct": True},
            {"text": "Water already inside the blades of grass was pushed "
                     "out to the surface by the cold.",
             "correct": False,
             "why": "Frost forms on paving slabs and car roofs just as "
                    "readily, and neither holds any water to push out."},
            {"text": "The cold air itself froze onto the grass, which is "
                     "what the white coating is made of.",
             "correct": False,
             "why": "Air does not freeze at −4 °C. Its gases need "
                    "temperatures below −200 °C to become solid."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s29",
        "band": "standard",
        "text": "Explain what happens to a bar of chocolate that is left "
                "in a warm car, in terms of energy and forces.",
        "options": [
            {"text": "It gives energy out to the warm car, and losing that "
                     "energy is what lets its particles move about.",
             "correct": False,
             "why": "Energy flows from the warmer car into the cooler "
                    "chocolate, not the other way round."},
            {"text": "It takes energy in from the warm car, and its "
                     "particles gain enough of it to break out of their "
                     "fixed positions.",
             "correct": True},
            {"text": "It takes energy in from the warm car, and that "
                     "energy makes each of its particles expand until they "
                     "are loose enough to flow.",
             "correct": False,
             "why": "The first half is right and the second is not. "
                    "Particles do not expand — the arrangement is what "
                    "loosens."},
            {"text": "It takes energy in from the warm car, and the forces "
                     "between its particles get stronger and drag them out "
                     "of line.",
             "correct": False,
             "why": "Stronger forces would hold the particles more firmly. "
                    "Melting weakens the hold between them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s30",
        "band": "standard",
        "text": "Two identical trays go into the same freezer, one holding "
                "100 g of water and the other 400 g. Both freeze at 0 °C. "
                "Which is completely frozen first, and why?",
        "options": [
            {"text": "The 400 g tray, because a larger amount of water "
                     "freezes at a slightly higher temperature.",
             "correct": False,
             "why": "Both freeze at 0 °C, as the question says. Amount "
                    "does not shift a freezing point."},
            {"text": "The 100 g tray, because a quarter as much energy has "
                     "to be taken out of it.",
             "correct": True},
            {"text": "Neither — they finish together, because both are at "
                     "0 °C in one freezer.",
             "correct": False,
             "why": "Being at the same temperature is not the same as "
                    "holding the same energy. Four times the water needs "
                    "four times the energy removed."},
            {"text": "The 400 g tray, because the extra water spreads "
                     "across more of the cold shelf beneath it.",
             "correct": False,
             "why": "The trays are identical, so the contact is the same. "
                    "The larger mass still has more energy to lose."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s31",
        "band": "standard",
        "text": "Washing dries slowly on a warm day when the air is "
                "already very damp. Explain why the dampness of the air "
                "slows it down.",
        "options": [
            {"text": "Damp air is heavier than dry air, and its weight "
                     "presses the water down into the cloth.",
             "correct": False,
             "why": "The weight of the air is the same above wet and dry "
                    "washing, and it holds nothing in."},
            {"text": "Damp air is cooler than dry air, so the washing is "
                     "not warm enough for any water to escape.",
             "correct": False,
             "why": "The stem says the day is warm, and water evaporates "
                    "at any temperature in any case."},
            {"text": "Damp air already carries a great deal of water "
                     "vapour, so as many particles return to the cloth as "
                     "leave it.",
             "correct": True},
            {"text": "Damp air has no room left in it at all, because its "
                     "gaps between particles are already full of water.",
             "correct": False,
             "why": "Air is mostly empty space and never fills up. The "
                    "return of particles is what slows the drying."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-s32",
        "band": "standard",
        "text": "Water boils at 100 °C and ethanol at 78 °C. A mixture of "
                "the two is warmed steadily and held at 85 °C. What "
                "happens?",
        "options": [
            {"text": "Both boil together, because a mixture behaves as one "
                     "substance once stirred.",
             "correct": False,
             "why": "Each keeps its own boiling point, which is exactly "
                    "what lets a mixture be separated this way."},
            {"text": "The water boils and the ethanol stays liquid, since "
                     "water is the commoner one.",
             "correct": False,
             "why": "How common a substance is decides nothing. 85 °C is "
                    "below water's boiling point of 100 °C."},
            {"text": "Neither boils, because 85 °C is below the 100 °C at "
                     "which boiling can start.",
             "correct": False,
             "why": "100 °C is water's boiling point only. Ethanol boils "
                    "at 78 °C, which 85 °C is past."},
            {"text": "The ethanol boils off and the water stays liquid, "
                     "because 85 °C is past 78 °C only.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── harder · the MRB-338 expansion ───────────────────────────
    {
        "id": "c1-03-h10",
        "band": "harder",
        "text": "Two glasses of squash are identical. One is cooled with "
                "ice cubes at 0 °C; the other with the same mass of liquid "
                "water at 0 °C. Which keeps the squash cold for longer, "
                "and why?",
        "options": [
            {"text": "The ice, because it has to take in a great deal of "
                     "energy from the squash before it can melt.",
             "correct": True},
            {"text": "The water, because a liquid touches every part of "
                     "the squash while a cube only touches it in places.",
             "correct": False,
             "why": "Better contact makes the cooling faster, not longer. "
                    "The ice takes in far more energy in total."},
            {"text": "The ice, because ice at 0 °C is several degrees "
                     "colder than water at the same reading.",
             "correct": False,
             "why": "Both are at 0 °C, as the question says. The "
                    "difference is the energy melting costs, not the "
                    "temperature."},
            {"text": "Neither — both start at 0 °C and both have the same "
                     "mass, so both must cool it by the same amount.",
             "correct": False,
             "why": "Same mass and same temperature, but the ice has a "
                    "whole melting plateau to pay for before it warms at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h11",
        "band": "harder",
        "text": "Salt is spread on roads before a frosty night. Salty "
                "water freezes below 0 °C rather than at 0 °C. Explain how "
                "the salt keeps the road clear.",
        "options": [
            {"text": "The salt crystals are sharp enough to break any ice "
                     "that forms into pieces small enough to blow away.",
             "correct": False,
             "why": "Salt does not cut ice. It changes the temperature at "
                    "which water can freeze."},
            {"text": "The salt gives out energy as it spreads through the "
                     "water, and that energy warms the road above 0 °C.",
             "correct": False,
             "why": "Salt dissolving takes energy in rather than giving it "
                    "out — salty water is cooler, not warmer."},
            {"text": "The water on the road is now salty, so it stays "
                     "liquid at temperatures that would have frozen pure "
                     "water.",
             "correct": True},
            {"text": "The salt seals the surface of the road, so the water "
                     "underneath is never in contact with the cold air.",
             "correct": False,
             "why": "Scattered grains seal nothing. The salt works by "
                    "mixing into the water itself."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h12",
        "band": "harder",
        "text": "Instant coffee is made by freezing strong liquid coffee "
                "solid and then removing the ice from it without ever "
                "letting it melt. Which change of state does that use?",
        "options": [
            {"text": "Melting, run so slowly that the liquid is carried "
                     "off as fast as it appears.",
             "correct": False,
             "why": "The question says it never melts. Nothing liquid "
                    "appears at any stage."},
            {"text": "Condensing, which pulls the water out of the frozen "
                     "coffee and collects it elsewhere.",
             "correct": False,
             "why": "Condensing turns a gas into a liquid. It is how the "
                    "water is caught afterwards, not how it leaves."},
            {"text": "Evaporating, which happens at the surface of the "
                     "frozen coffee at any temperature.",
             "correct": False,
             "why": "Evaporation is a liquid becoming a gas. The coffee is "
                    "solid throughout."},
            {"text": "Sublimation — the ice becomes a gas without ever "
                     "becoming a liquid on the way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h13",
        "band": "harder",
        "text": "In a hot dry country a bottle of water is wrapped in a "
                "wet cloth and hung in the shade. The water inside ends up "
                "cooler than the air. Explain how.",
        "options": [
            {"text": "The wet cloth blocks the heat of the air, in the way "
                     "that a coat keeps the cold out.",
             "correct": False,
             "why": "Blocking heat could at best hold it at air "
                    "temperature. The bottle ends up colder than that."},
            {"text": "The water in the cloth is colder than the air, and "
                     "that coldness passes inwards to the bottle.",
             "correct": False,
             "why": "The cloth is wetted with ordinary water at air "
                    "temperature. The cooling comes from evaporation."},
            {"text": "The shade stops the sun reaching the bottle, so the "
                     "bottle can only get as cool as the shade is.",
             "correct": False,
             "why": "Shade is why it is not hotter than the air. It cannot "
                    "make it colder than the air."},
            {"text": "Water evaporating from the cloth takes energy with "
                     "it, and it takes that energy from the bottle.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h14",
        "band": "harder",
        "text": "Two beakers hold 100 cm³ of water each. One is left open, "
                "the other has a lid clipped on. After a week the open "
                "beaker is nearly empty and the covered one is unchanged, "
                "with drops on the underside of its lid. Explain the "
                "difference.",
        "options": [
            {"text": "The lid stops the water being warmed, and water that "
                     "is never warmed cannot evaporate at all.",
             "correct": False,
             "why": "Evaporation happens at any temperature, and the drops "
                    "on the lid prove it happened under the lid too."},
            {"text": "The lid presses down on the water, and that pressure "
                     "holds the particles in the liquid.",
             "correct": False,
             "why": "A clipped lid presses on nothing. Particles still "
                    "leave the surface underneath it."},
            {"text": "Both evaporated, but under the lid the vapour "
                     "condensed and dripped back, so nothing left the "
                     "beaker.",
             "correct": True},
            {"text": "Only the open beaker evaporated, and the drops under "
                     "the lid are water that came out of the air above it.",
             "correct": False,
             "why": "The lid is clipped on, so the air above it cannot "
                    "reach the underside. The drops came from the beaker."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h15",
        "band": "harder",
        "text": "Melting 1 g of ice at 0 °C takes 334 J. Warming 1 g of "
                "water by 1 °C takes 4.2 J. Calculate the energy needed to "
                "turn 1 g of ice at 0 °C into water at 20 °C.",
        "options": [
            {"text": "84 J",
             "correct": False,
             "why": "That is the warming alone. The ice has to be melted "
                    "first, which costs 334 J on top."},
            {"text": "418 J",
             "correct": True},
            {"text": "334 J",
             "correct": False,
             "why": "That is the melting alone, leaving the water at 0 °C. "
                    "Warming it to 20 °C costs a further 84 J."},
            {"text": "6680 J",
             "correct": False,
             "why": "That multiplies the melting energy by 20. The 20 "
                    "degrees belongs to the warming step only."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h16",
        "band": "harder",
        "text": "Boiling 1 g of water at 100 °C takes 2260 J. A kettle "
                "supplies 2000 J every second. Calculate how long it takes "
                "to boil away 10 g of water that is already at 100 °C.",
        "options": [
            {"text": "1.13 s",
             "correct": False,
             "why": "That is the time for 1 g. Ten grams need ten times as "
                    "much energy."},
            {"text": "11.3 s",
             "correct": True},
            {"text": "113 s",
             "correct": False,
             "why": "That is ten times too long — a power of ten has been "
                    "dropped in the division."},
            {"text": "22 600 s",
             "correct": False,
             "why": "That is the energy needed, in joules, not a time. It "
                    "still has to be divided by 2000 J each second."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h17",
        "band": "harder",
        "text": "Mercury melts at −39 °C and boils at 357 °C. A mercury "
                "thermometer is taken to a research station where the air "
                "is at −50 °C, and it stops working. Suggest why.",
        "options": [
            {"text": "The mercury has boiled away inside the sealed tube, "
                     "so there is nothing left to read.",
             "correct": False,
             "why": "Boiling needs 357 °C. At −50 °C the mercury is "
                    "nowhere near it."},
            {"text": "The glass has contracted so far that the tube has "
                     "closed around the mercury.",
             "correct": False,
             "why": "Glass contracts far too little for that, and the "
                    "mercury's own change of state is the real cause."},
            {"text": "The mercury has frozen solid at −39 °C, and a solid "
                     "cannot move up the tube.",
             "correct": True},
            {"text": "The mercury has become so cold that it no longer has "
                     "any energy left to respond to the air.",
             "correct": False,
             "why": "A substance at −50 °C still holds plenty of energy. "
                    "The problem is that it is now a solid."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h18",
        "band": "harder",
        "text": "Salty water is boiled and the steam is led away through a "
                "cold tube, where it collects as a liquid. What collects, "
                "and why?",
        "options": [
            {"text": "Salty water, because the salt was dissolved in the "
                     "water and travels wherever the water travels.",
             "correct": False,
             "why": "Only the water changed state. The salt stayed in the "
                    "flask, because 100 °C is nowhere near its boiling "
                    "point."},
            {"text": "Pure water, because only the water boiled, and "
                     "condensing it back changes nothing else about it.",
             "correct": True},
            {"text": "Pure salt, because the water is destroyed by the "
                     "boiling and only the solid is left to be carried "
                     "across.",
             "correct": False,
             "why": "The water is not destroyed — it is the very thing "
                    "being collected. The salt never left the flask."},
            {"text": "Nothing at all, because a gas cannot be turned back "
                     "into a liquid once it has boiled away.",
             "correct": False,
             "why": "Changes of state are reversible. Cooling steam "
                    "condenses it straight back into liquid water."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h19",
        "band": "harder",
        "text": "To find the melting point of a solid, a technician stands "
                "the sample in a beaker of warm water rather than holding "
                "it in a flame. Suggest why that gives a better "
                "measurement.",
        "options": [
            {"text": "The water warms the sample slowly and evenly, so the "
                     "thermometer and the sample are at the same "
                     "temperature.",
             "correct": True},
            {"text": "The water dissolves the outside of the sample first, "
                     "which is what makes the moment of melting easy to "
                     "spot.",
             "correct": False,
             "why": "Dissolving is a different event altogether, and it "
                    "would ruin the measurement rather than help it."},
            {"text": "A flame has no temperature of its own, so a "
                     "thermometer held in one cannot give any reading.",
             "correct": False,
             "why": "A flame has a very high temperature. The trouble is "
                    "that it is uneven and hard to control."},
            {"text": "Warming in water lowers the melting point, so the "
                     "change happens at a temperature easier to reach.",
             "correct": False,
             "why": "A pure substance melts at its own fixed temperature "
                    "however it is heated."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h20",
        "band": "harder",
        "text": "A pan of water is boiling and pasta is added. The cook "
                "turns the ring from medium up to maximum, hoping to cook "
                "the pasta faster. Will it cook faster?",
        "options": [
            {"text": "Yes, because more energy going in every second means "
                     "a higher temperature in the pan.",
             "correct": False,
             "why": "The reading holds at 100 °C however hard it is "
                    "boiled. The extra energy goes into making steam."},
            {"text": "No, because the extra energy is lost to the kitchen "
                     "before it can reach the water at all.",
             "correct": False,
             "why": "Most of it does reach the water. It is spent turning "
                    "water into steam rather than raising the temperature."},
            {"text": "Yes, because the extra energy passes straight into "
                     "the pasta and cooks it from the inside.",
             "correct": False,
             "why": "The pasta is cooked by the water around it, and that "
                    "water is at 100 °C on either setting."},
            {"text": "No — the water stays at 100 °C on either setting and "
                     "simply boils away faster.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h21",
        "band": "harder",
        "text": "Evaluate this claim: “A substance always melts at a "
                "higher temperature than it freezes at, because heating "
                "and cooling are different processes.”",
        "options": [
            {"text": "Correct, because extra energy has to be supplied to "
                     "start a melt and none is needed to start a freeze.",
             "correct": False,
             "why": "Energy is needed to melt and given out to freeze, but "
                    "both happen at the same temperature."},
            {"text": "Correct, but only for water, whose melting point is "
                     "the one exception to the rule.",
             "correct": False,
             "why": "Water is not an exception. Ice melts and water "
                    "freezes at the same 0 °C."},
            {"text": "Wrong — for a given substance the two happen at the "
                     "same temperature, in opposite directions.",
             "correct": True},
            {"text": "Wrong, because a substance actually melts at a lower "
                     "temperature than the one at which it freezes.",
             "correct": False,
             "why": "It is not the other way round either. The two "
                    "temperatures are the same."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h22",
        "band": "harder",
        "text": "Ethanol melts at −114 °C and boils at 78 °C. Oxygen melts "
                "at −219 °C and boils at −183 °C. Mercury melts at −39 °C "
                "and boils at 357 °C. Which of the three is a gas at −100 "
                "°C?",
        "options": [
            {"text": "Oxygen only, because −100 °C is above its boiling "
                     "point of −183 °C.",
             "correct": True},
            {"text": "Ethanol only, because −100 °C is above the −114 °C "
                     "at which it stops being a solid.",
             "correct": False,
             "why": "That makes it a liquid. It needs 78 °C before it "
                    "becomes a gas."},
            {"text": "Mercury only, because −100 °C is far below the 357 "
                     "°C at which it is said to boil.",
             "correct": False,
             "why": "Being below the boiling point does not make something "
                    "a gas. At −100 °C mercury is solid."},
            {"text": "All three, because −100 °C is cold enough to drive "
                     "any of them out of the liquid state.",
             "correct": False,
             "why": "Cooling drives substances towards the solid state, "
                    "not the gas state."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h23",
        "band": "harder",
        "text": "A student argues that boiling and evaporating must be the "
                "same change, since both end with a liquid becoming a gas. "
                "Evaluate that argument.",
        "options": [
            {"text": "The student is right, and the two words are simply "
                     "used in different parts of the country.",
             "correct": False,
             "why": "The two words describe genuinely different events, "
                    "and science uses both deliberately."},
            {"text": "The student is wrong, because evaporating ends with "
                     "a liquid spread thinly rather than with a gas.",
             "correct": False,
             "why": "Evaporating does end with a gas. That much of the "
                    "argument is sound."},
            {"text": "The student is wrong, because boiling makes a new "
                     "substance and evaporating leaves the substance "
                     "alone.",
             "correct": False,
             "why": "Neither makes a new substance. Both are changes of "
                    "state and both are reversible."},
            {"text": "The student is right about the ending, but the two "
                     "differ in where they happen and at what temperature.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h24",
        "band": "harder",
        "text": "Orange growers spray water over their trees when a frost "
                "is forecast, and the fruit survives inside a shell of "
                "ice. Suggest how freezing water protects the fruit.",
        "options": [
            {"text": "Ice is a warm material, so a shell of it keeps the "
                     "fruit above the temperature of the air.",
             "correct": False,
             "why": "Ice is not warm. It holds the fruit at 0 °C, which is "
                    "warmer than the air but is not warmth of its own."},
            {"text": "The ice shell is airtight, and fruit sealed away "
                     "from the air cannot be damaged by cold.",
             "correct": False,
             "why": "Cold reaches the fruit through ice perfectly well. It "
                    "is the energy released by freezing that helps."},
            {"text": "As the water freezes it gives out energy, and it "
                     "cannot fall below 0 °C while any is still freezing.",
             "correct": True},
            {"text": "The spray washes the frost off the fruit before it "
                     "can settle and cause any damage.",
             "correct": False,
             "why": "The fruit ends up encased in ice rather than clear of "
                    "it, so washing frost away is not the mechanism."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h25",
        "band": "harder",
        "text": "A 100 g block and a 300 g block of the same metal are "
                "heated in identical furnaces until each has completely "
                "melted. Compare the temperature at which each melts and "
                "the energy each needs.",
        "options": [
            {"text": "The same melting point for both; the 300 g block "
                     "needs about three times the energy.",
             "correct": True},
            {"text": "The 300 g block melts at a higher temperature and "
                     "needs about three times the energy to get there.",
             "correct": False,
             "why": "A melting point belongs to the substance, not to the "
                    "amount. Only the energy scales."},
            {"text": "The same melting point, and the same energy, since "
                     "the two blocks are made of exactly the same metal.",
             "correct": False,
             "why": "Three times the particles have to be freed, so three "
                    "times the energy is needed."},
            {"text": "The 100 g block melts at a lower temperature, "
                     "because a small block warms through much more "
                     "quickly.",
             "correct": False,
             "why": "The small block reaches the melting point sooner, but "
                    "that point is the same temperature for both."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h26",
        "band": "harder",
        "text": "Compare what happens to the hold between the particles "
                "when a substance melts and when it later boils.",
        "options": [
            {"text": "Melting weakens the hold enough for particles to "
                     "slide past one another; boiling breaks it so they "
                     "separate completely.",
             "correct": True},
            {"text": "Melting breaks the hold completely; boiling then has "
                     "to break the particles themselves into smaller "
                     "pieces.",
             "correct": False,
             "why": "If melting broke the hold completely you would have a "
                    "gas, and no change of state ever breaks a particle."},
            {"text": "Melting strengthens the hold so the particles can "
                     "flow; boiling strengthens it further still so they "
                     "can spread right out.",
             "correct": False,
             "why": "Both changes weaken the hold. A stronger hold would "
                    "keep the particles more firmly in place."},
            {"text": "Melting leaves the hold untouched and only spaces "
                     "the particles out; boiling weakens it for the first "
                     "time.",
             "correct": False,
             "why": "Melting weakens the hold too, which is why a liquid "
                    "can be poured and a solid cannot."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h27",
        "band": "harder",
        "text": "Meat left for months in a sealed bag in a freezer at −18 "
                "°C becomes dry and leathery, and ice crystals appear on "
                "the inside of the bag. Explain what has happened.",
        "options": [
            {"text": "The freezer has warmed above 0 °C at some point, so "
                     "the meat thawed and the water ran out of it.",
             "correct": False,
             "why": "A thaw would leave liquid and refrozen lumps, not dry "
                    "meat with crystals on the bag."},
            {"text": "The ice in the meat has turned straight to gas and "
                     "then back to ice on the colder bag, never melting.",
             "correct": True},
            {"text": "The cold has destroyed some of the water in the "
                     "meat, which is what leaves it dry.",
             "correct": False,
             "why": "Water is never destroyed. All of it is still in the "
                    "bag, as the crystals show."},
            {"text": "The bag has drawn water out of the meat through its "
                     "plastic and frozen it on the far side.",
             "correct": False,
             "why": "Nothing passes through the sealed plastic. The water "
                    "crossed the space inside the bag as a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h28",
        "band": "harder",
        "text": "A candle is lit. Which part of what then happens is a "
                "change of state?",
        "options": [
            {"text": "The wick blackening and crumbling as the flame works "
                     "its way down it.",
             "correct": False,
             "why": "That is burning — a chemical change that makes new "
                    "substances and cannot be undone."},
            {"text": "The flame giving out light and warming the air above "
                     "the candle.",
             "correct": False,
             "why": "Giving out light and warmth is not a change of state "
                    "at all. Nothing has changed between solid, liquid and "
                    "gas."},
            {"text": "Solid wax near the flame turning into a pool of "
                     "liquid wax around the wick.",
             "correct": True},
            {"text": "The wax burning away to make the gases that rise "
                     "from the top of the flame.",
             "correct": False,
             "why": "Burning makes new substances, so it is a chemical "
                    "change rather than a change of state."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h29",
        "band": "harder",
        "text": "Two identical ice cubes are put out in a room at 20 °C — "
                "one on a dry plate, one dropped into a glass of water "
                "that is also at 20 °C. Which melts first, and why?",
        "options": [
            {"text": "The one on the plate, because air is warmer than "
                     "water at the same reading on a thermometer.",
             "correct": False,
             "why": "Both are at 20 °C, so neither is warmer. The "
                    "difference is how quickly each delivers energy."},
            {"text": "The one in the glass, because water is a liquid and "
                     "only liquids can make a solid melt.",
             "correct": False,
             "why": "Air melts ice perfectly well, as any cube left out "
                    "will show. It simply does it more slowly."},
            {"text": "Neither — both are surrounded by something at 20 °C, "
                     "so both must take the same time to melt.",
             "correct": False,
             "why": "Same temperature, but not the same rate of transfer. "
                    "Water passes energy to the cube far faster."},
            {"text": "The one in the glass, because water carries energy "
                     "to the cube much faster than air does.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h30",
        "band": "harder",
        "text": "A drop of ethanol and a drop of water, both at room "
                "temperature, are put on the back of a hand. The ethanol "
                "feels much colder. Suggest why.",
        "options": [
            {"text": "Ethanol is colder than water when it comes out of "
                     "the bottle, whatever the room is doing.",
             "correct": False,
             "why": "Both drops are at room temperature, as the question "
                    "says, so they start out equally cold."},
            {"text": "Ethanol evaporates much faster, so it takes energy "
                     "from the skin much more quickly.",
             "correct": True},
            {"text": "Ethanol sinks into the skin, and cooling from inside "
                     "always feels stronger than cooling from outside.",
             "correct": False,
             "why": "The cooling happens at the surface, as the ethanol "
                    "leaves it. Nothing has to sink in."},
            {"text": "Ethanol takes energy in as it warms up to the "
                     "temperature of the hand around it.",
             "correct": False,
             "why": "The water on the hand would do that too. The "
                    "difference is how fast each of them evaporates."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h31",
        "band": "harder",
        "text": "Solid carbon dioxide is heated steadily from −100 °C and "
                "its temperature is recorded. How many times will the "
                "reading hold still, and why?",
        "options": [
            {"text": "Twice, because every substance has both a melting "
                     "point and a boiling point to get past.",
             "correct": False,
             "why": "Two holds need two changes of state. Solid carbon "
                    "dioxide makes only one."},
            {"text": "Once, because it makes a single change of state, "
                     "straight from solid to gas.",
             "correct": True},
            {"text": "Never, because a substance that skips the liquid "
                     "state needs no energy to change.",
             "correct": False,
             "why": "Sublimation takes energy in like any other change, so "
                    "the reading holds while it happens."},
            {"text": "Twice, because solid to gas counts as a melt and a "
                     "boil one after the other.",
             "correct": False,
             "why": "There is no melt. The solid becomes a gas in one "
                    "step, with no liquid at any point."},
        ],
        "figure": None,
    },
    {
        "id": "c1-03-h32",
        "band": "harder",
        "text": "You can see your breath outdoors on a cold morning, but "
                "never indoors in a warm room. Explain the difference.",
        "options": [
            {"text": "Outdoors your breath is white because the cold makes "
                     "the carbon dioxide in it visible.",
             "correct": False,
             "why": "Carbon dioxide has no colour at any temperature. What "
                    "you see is liquid water."},
            {"text": "Indoors your breath is thinner, because warm air has "
                     "spread the particles too far apart to be seen.",
             "correct": False,
             "why": "Breath is not seen or unseen by how spread out it is. "
                    "It is seen when its vapour condenses."},
            {"text": "Outdoors the water vapour in your breath is cooled "
                     "enough to condense into tiny drops of liquid.",
             "correct": True},
            {"text": "Outdoors your breath freezes into ice crystals, "
                     "which is why the cloud disappears as it warms.",
             "correct": False,
             "why": "The cloud forms well above 0 °C on a cool morning, so "
                    "it is liquid drops rather than ice."},
        ],
        "figure": None,
    },
]
