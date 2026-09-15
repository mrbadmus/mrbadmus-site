"""P1 lesson 06 — Radiation: twelve questions.

⊕ THE LOWEST SURVIVAL RATE IN THE UNIT, AND FOR A STRUCTURAL REASON.

Run 1 flagged this set itself, and was right to: *"L6 radiation is the worst
and I would not carry ANY of it forward unchecked."* Measured against
Design's page, FIVE of the twelve depend on a Leslie's cube — matt black
100, matt white 92, dull silver 34, polished silver 12 — and a ruling that
for infrared it is SHINE rather than colour that decides emissivity.

**Design's `p1-06` has no Leslie's cube and no emissivity bench of any
kind.** Her instruments are a three-routes bench (`SCENARIOS`) and a
six-card harmless/risky word sort (`WORD_CARDS`). Her only emissivity
content in the entire lesson is one key-fact line: *"more from matt black
ones than from shiny silver ones"* — which contrasts matt black with SHINY
SILVER and never raises matt white at all.

So those five are not questions with wrong numbers. They are questions about
an instrument that is not on the page, testing a distinction the lesson does
not draw. `DEPARTURES-P1.md` row A records the ruling as considered and not
applied, for the same reason.

    CHANGED — six stems kept, option sets rewritten (6):
        e01  what radiation needs in order to travel
        e03  what infrared is
        s02  the hot object in an evacuated jar — her `sc3` exactly
        s03  the vacuum flask
        h02  the runner in a foil blanket
        h04  "radiation is dangerous, so a radiator must be dangerous"

    NEW — her instruments had no question covering them (6):
        e02  everything above absolute zero emits infrared
        e04  the detector beside the fire — her `sc2`, radiation only
        s01  which routes survive a vacuum — her `sc3` versus `sc4`
        s04  where the harmless/risky boundary actually sits
        h01  why "heat rises" is a fact about air, not a law about energy
        h03  conduction works in a vacuum IF the objects touch — her `sc4`

    DROPPED — depend on an instrument that is not on her page (5):
        run 1's e02, e04, s01, h01, h03 — all Leslie's-cube emissivity.
    DROPPED — quotes bench readings that do not exist (1):
        run 1's s04.

⚠️ Answer positions are 0,1,2,3 · 0,1,2,3 · 0,1,2,3 — three of each index.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "radiation"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-06-e01",
        "band": "easier",
        "text": "What does radiation need in order to travel?",
        "options": [
            {"text": "Nothing at all — it crosses empty space perfectly well",
             "correct": True},
            {"text": "Particles that are touching, so it can be passed along",
             "correct": False,
             "why": "That is conduction. Radiation crosses a vacuum, where "
                    "there are no particles to touch."},
            {"text": "A fluid that is free to move and carry it upwards",
             "correct": False,
             "why": "That is convection. Radiation reaches us from the Sun "
                    "across empty space."},
            {"text": "A warm surface for it to travel along on its way",
             "correct": False,
             "why": "It travels in straight lines through nothing. No "
                    "surface is involved."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e02",
        "band": "easier",
        "text": "Which of these objects is emitting infrared radiation right "
                "now?",
        "options": [
            {"text": "Only the ones that are hotter than the room they are "
                     "standing in",
             "correct": False,
             "why": "Everything above absolute zero emits. Being cooler than "
                    "the room only means emitting less."},
            {"text": "Every one of them, including you and a block of ice",
             "correct": True},
            {"text": "Only the ones that are glowing brightly enough to be "
                     "seen in the dark",
             "correct": False,
             "why": "Glowing visibly needs a very high temperature. "
                    "Infrared is emitted long before that."},
            {"text": "Only the ones that have been switched on and are "
                     "using electricity",
             "correct": False,
             "why": "Nothing needs to be powered. A cold stone in a field "
                    "emits infrared."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e03",
        "band": "easier",
        "text": "What is infrared?",
        "options": [
            {"text": "A stream of hot particles given off by a warm surface",
             "correct": False,
             "why": "No particles are given off. It is a wave, and it "
                    "travels where there are no particles at all."},
            {"text": "A kind of heat that only exists inside hot objects",
             "correct": False,
             "why": "There is no substance called heat, and infrared travels "
                    "away from the object."},
            {"text": "An electromagnetic wave, just beyond red in the family "
                     "of light",
             "correct": True},
            {"text": "The name for the temperature of a surface you cannot "
                     "touch",
             "correct": False,
             "why": "It is a wave, not a temperature. A thermal camera "
                    "detects the wave and infers the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e04",
        "band": "easier",
        "text": "You stand to the side of a campfire, level with the flames, "
                "and feel warmth. Which route reaches you?",
        "options": [
            {"text": "Convection, because the warm air spreads out in all "
                     "directions",
             "correct": False,
             "why": "Warm air goes UP, not sideways. That is why standing "
                    "beside a fire tests this so well."},
            {"text": "Conduction, because the air between carries it to your "
                     "skin",
             "correct": False,
             "why": "Air is a very poor conductor, and you are not touching "
                    "the fire."},
            {"text": "All three at once, because a fire is hot enough to use "
                     "each of them",
             "correct": False,
             "why": "Only one is available sideways. The other two need "
                    "either contact or upward-moving air."},
            {"text": "Radiation, which travels sideways as easily as it "
                     "travels upwards",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-06-s01",
        "band": "standard",
        "text": "A warm object and a detector sit in a sealed jar, not "
                "touching. The air is pumped out. What happens?",
        "options": [
            {"text": "The detector still registers, at full strength",
             "correct": True},
            {"text": "The detector stops registering, because there is "
                     "nothing left to carry it",
             "correct": False,
             "why": "That would be true of conduction and convection. "
                    "Radiation needs no carrier."},
            {"text": "The detector registers, but much more weakly than it "
                     "did before",
             "correct": False,
             "why": "Removing the air removes two routes that were not "
                    "working sideways anyway. Radiation is unaffected."},
            {"text": "The detector registers only while some air still "
                     "remains in the jar",
             "correct": False,
             "why": "It keeps registering with the jar fully evacuated — "
                    "which is the whole point of the test."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s02",
        "band": "standard",
        "text": "A vacuum flask has a vacuum between its walls and both "
                "facing surfaces are silvered. Why both features?",
        "options": [
            {"text": "The vacuum stops all three routes on its own, and the "
                     "silvering is decorative",
             "correct": False,
             "why": "A vacuum stops two of them. Radiation crosses it "
                    "perfectly well, which is what the silvering is for."},
            {"text": "The vacuum stops conduction and convection; the "
                     "silvering reflects radiation back",
             "correct": True},
            {"text": "The vacuum stops radiation, and the silvering stops "
                     "conduction across the gap",
             "correct": False,
             "why": "The two are the wrong way round. Radiation is the one "
                    "that crosses a vacuum."},
            {"text": "Both features do the same job, so that the flask still "
                     "works if one fails",
             "correct": False,
             "why": "They block different routes. Losing either one leaves a "
                    "way out that the other cannot cover."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s03",
        "band": "standard",
        "text": "Two objects touch inside a vacuum. Which routes can deliver "
                "energy between them?",
        "options": [
            {"text": "None of them, because a vacuum has no particles in it "
                     "at all",
             "correct": False,
             "why": "The vacuum is around them; they are touching each "
                    "other, so their own particles are in contact."},
            {"text": "Convection and radiation, because the two are in "
                     "contact with each other",
             "correct": False,
             "why": "Convection needs a fluid to move and there is none. "
                    "Contact enables conduction, not convection."},
            {"text": "Conduction and radiation, because contact restores the "
                     "particle route",
             "correct": True},
            {"text": "Conduction only, because a vacuum blocks radiation "
                     "between two solids",
             "correct": False,
             "why": "A vacuum never blocks radiation. That is the one thing "
                    "it cannot do."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s04",
        "band": "standard",
        "text": "Where does the boundary between harmless and risky "
                "radiation actually sit?",
        "options": [
            {"text": "Between radio waves and infrared, where warming "
                     "effects first begin",
             "correct": False,
             "why": "Warming is not damage. Infrared warms you all day and "
                    "cannot break a molecule."},
            {"text": "Between infrared and visible light, where radiation "
                     "becomes visible",
             "correct": False,
             "why": "Being visible has nothing to do with it. Light is "
                    "harmless and you are reading by it."},
            {"text": "Between X-rays and gamma rays, at the very top of the "
                     "whole family",
             "correct": False,
             "why": "Too far up. X-rays are already risky, which is why "
                    "radiographers leave the room."},
            {"text": "Between visible light and ultraviolet, where waves can "
                     "damage a molecule",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-06-h01",
        "band": "harder",
        "text": "A student says “heat rises, so heating always "
                "travels upwards”. What is wrong with the reasoning?",
        "options": [
            {"text": "Warm air rises, which is one route of three; the other "
                     "two ignore direction",
             "correct": True},
            {"text": "Nothing is wrong — warmth really does always travel "
                     "upwards from its source",
             "correct": False,
             "why": "Stand beside a bonfire, or under a patio heater, and "
                    "the claim fails immediately."},
            {"text": "Heat actually sinks, and it is the cold air that rises "
                     "above it instead",
             "correct": False,
             "why": "Neither. Warm air rises because it is less dense; "
                    "nothing about cold rises."},
            {"text": "It is true indoors but not outdoors, where the wind "
                     "moves the air around",
             "correct": False,
             "why": "Wind is not the issue. Radiation goes in every "
                    "direction indoors too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h02",
        "band": "harder",
        "text": "A marathon runner is wrapped in a shiny foil blanket at the "
                "finish. Which explanation is right?",
        "options": [
            {"text": "The foil is warm to begin with and passes that warmth "
                     "into the runner",
             "correct": False,
             "why": "The foil has no warmth of its own. It comes out of a "
                    "packet at air temperature."},
            {"text": "The shiny surface reflects the runner's own radiation "
                     "back towards them",
             "correct": True},
            {"text": "The foil conducts energy away from the runner faster "
                     "than skin alone would",
             "correct": False,
             "why": "That would cool them down. Metal foil conducts well, "
                    "which is why it is used so thin."},
            {"text": "The foil generates warmth from the friction of the "
                     "runner moving inside it",
             "correct": False,
             "why": "No useful energy comes from that. The runner's own "
                    "body is the source."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h03",
        "band": "harder",
        "text": "Why does the Moon's surface get so extremely cold at night "
                "despite being fiercely hot by day?",
        "options": [
            {"text": "Because the Moon moves further from the Sun during its "
                     "own night-time",
             "correct": False,
             "why": "Its distance barely changes. The difference is about "
                    "what happens to the energy it has."},
            {"text": "Because the cold of space flows into the surface once "
                     "the Sun has set",
             "correct": False,
             "why": "Cold is not a substance and cannot flow. Energy leaves; "
                    "nothing arrives."},
            {"text": "Because it radiates its energy away and has no "
                     "atmosphere to hold any of it",
             "correct": True},
            {"text": "Because rock conducts energy so badly that the surface "
                     "never warms up properly",
             "correct": False,
             "why": "The surface does warm up — to well above boiling by "
                    "day. The question is where it goes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h04",
        "band": "harder",
        "text": "A student says “radiation is dangerous, so a hot "
                "radiator must be dangerous”. Correct them.",
        "options": [
            {"text": "Radiators emit no radiation at all, so the premise is "
                     "simply mistaken",
             "correct": False,
             "why": "They very much do — infrared, which is exactly what "
                    "warms you across the room."},
            {"text": "Radiation is only dangerous in very large amounts, "
                     "whatever kind it happens to be",
             "correct": False,
             "why": "Amount is not the distinction. No amount of radio waves "
                    "will break a molecule."},
            {"text": "Radiators emit radiation but it is far too weak to be "
                     "detected by anything",
             "correct": False,
             "why": "It is easily detected — a thermal camera sees it, and "
                    "so does your face."},
            {"text": "The word covers a whole family, and only the "
                     "high-energy end can damage anything",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-06-e05",
        "band": "easier",
        "text": "Which of these transfers CANNOT happen across a vacuum?",
        "options": [
            {"text": "Conduction between the two surfaces", "correct": True},
            {"text": "Radiation from a hot object", "correct": False,
             "why": "Radiation is the one route that crosses a vacuum, which "
                    "is how the Sun's energy reaches us."},
            {"text": "Infrared leaving a warm surface", "correct": False,
             "why": "Infrared is radiation, so it crosses a vacuum "
                    "perfectly well."},
            {"text": "Light passing through a window", "correct": False,
             "why": "Light is radiation as well, and needs no particles to "
                    "travel through."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e06",
        "band": "easier",
        "text": "Which objects emit infrared radiation?",
        "options": [
            {"text": "Only objects that are glowing red or white hot",
             "correct": False,
             "why": "Glowing means visible light as well. Infrared comes off "
                    "long before anything glows."},
            {"text": "Only objects hotter than the room they are in",
             "correct": False,
             "why": "Cold objects emit too — just less than warm ones do."},
            {"text": "Every object, however warm or cool it is",
             "correct": True},
            {"text": "Only objects that have been heated by electricity",
             "correct": False,
             "why": "How something was warmed makes no difference to whether "
                    "it emits."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-06-s05",
        "band": "standard",
        "text": "On a thermal camera a person appears bright and the wall "
                "behind them appears dark. What does that show?",
        "options": [
            {"text": "Only the person is emitting infrared", "correct": False,
             "why": "The wall emits too. It is cooler, so it emits less and "
                    "shows up darker."},
            {"text": "Both emit infrared, and the warmer one emits more",
             "correct": True},
            {"text": "The wall is absorbing all the infrared that reaches it",
             "correct": False,
             "why": "The camera shows what is emitted, and a wall that "
                    "absorbed everything would then emit strongly."},
            {"text": "The camera is detecting visible light from the person",
             "correct": False,
             "why": "A thermal camera sees infrared. The picture works in a "
                    "completely dark room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s06",
        "band": "standard",
        "text": "You sit behind a closed window in sunlight and still feel "
                "warm. Which route is reaching you?",
        "options": [
            {"text": "Conduction through the glass and then through the air",
             "correct": False,
             "why": "Conduction through glass and still air is far too slow "
                    "to be what you feel."},
            {"text": "Convection carrying warm air through the closed window",
             "correct": False,
             "why": "The window is shut, so no air is coming through it at "
                    "all."},
            {"text": "Radiation, which passes straight through the glass",
             "correct": True},
            {"text": "Nothing is reaching you; the room is simply warm "
                     "already",
             "correct": False,
             "why": "Step out of the sunbeam and the feeling stops at once, "
                    "so something is arriving along it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-06-h05",
        "band": "harder",
        "text": "Space is extremely cold, yet a spacecraft needs radiators to "
                "get rid of unwanted energy. Why?",
        "options": [
            {"text": "Because there are no particles outside, so only "
                     "radiation can carry energy away",
             "correct": True},
            {"text": "Because space is not really cold, so nothing can cool "
                     "at all",
             "correct": False,
             "why": "It is genuinely cold. The difficulty is that there is "
                    "nothing to conduct into."},
            {"text": "Because the spacecraft makes so much energy that no "
                     "route could keep up",
             "correct": False,
             "why": "It is not the amount. Two of the three routes are simply "
                    "unavailable out there."},
            {"text": "Because energy can only leave a spacecraft through "
                     "metal fins",
             "correct": False,
             "why": "The fins are shaped to radiate well; the whole hull "
                    "radiates too, just less."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h06",
        "band": "harder",
        "text": "Two identical cans of hot water are left side by side, one "
                "painted matt black and one polished silver. Which cools "
                "faster, and why?",
        "options": [
            {"text": "The silver one, because shiny metal conducts energy "
                     "away quickly",
             "correct": False,
             "why": "Both cans are metal, so conduction through the wall is "
                    "the same. The surfaces differ in what they emit."},
            {"text": "Neither — the paint changes the colour, not the "
                     "physics",
             "correct": False,
             "why": "The surface is exactly what decides how well infrared "
                    "leaves it."},
            {"text": "The black one, because a matt dark surface emits "
                     "infrared better",
             "correct": True},
            {"text": "The black one, because dark surfaces hold less energy "
                     "to start with",
             "correct": False,
             "why": "Both start with the same water at the same temperature; "
                    "the difference is the rate of emission."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-06-e07",
        "band": "easier",
        "text": "Roughly how long does radiation from the Sun take to reach "
                "the Earth?",
        "options": [
            {"text": "About eight minutes", "correct": True},
            {"text": "No time at all, because it arrives instantly",
             "correct": False,
             "why": "It travels very fast but not instantly. There is a "
                    "measurable delay of several minutes."},
            {"text": "About eight hours, because space is so wide",
             "correct": False,
             "why": "Space is wide, but radiation crosses it far faster than "
                    "that. Minutes, not hours."},
            {"text": "About a year, one for each orbit of the Earth",
             "correct": False,
             "why": "The orbit has nothing to do with it. Sunlight is only "
                    "minutes old when it reaches you."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e08",
        "band": "easier",
        "text": "In which directions does radiation leave a hot object?",
        "options": [
            {"text": "Upwards only, because warmth rises",
             "correct": False,
             "why": "That is warm air rising, which is convection. Radiation "
                    "ignores which way is up."},
            {"text": "Sideways only, because it cannot climb against gravity",
             "correct": False,
             "why": "Gravity does not act on radiation in any way you would "
                    "notice. It goes up as easily as sideways."},
            {"text": "Downwards only, being heavy",
             "correct": False,
             "why": "Radiation is a wave and has no weight. A patio heater "
                    "sends it down and a bonfire sends it up."},
            {"text": "In straight lines in every direction at once",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e09",
        "band": "easier",
        "text": "Is infrared the same kind of thing as visible light?",
        "options": [
            {"text": "No, because infrared is a stream of hot particles "
                     "rather than a wave of any kind",
             "correct": False,
             "why": "No particles are given off. Infrared is a wave, exactly "
                    "as light is."},
            {"text": "Yes — the same family of wave, at a wavelength your "
                     "eyes cannot see",
             "correct": True},
            {"text": "No, because infrared can only travel through air",
             "correct": False,
             "why": "Infrared crosses a vacuum as easily as light does. Most "
                    "of the Sun's warmth arrives that way."},
            {"text": "Yes, but only when the object is glowing red",
             "correct": False,
             "why": "Infrared is the same family whatever the temperature. "
                    "A cold object emits it too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e10",
        "band": "easier",
        "text": "Which of these carries the least energy per wave?",
        "options": [
            {"text": "Ultraviolet from the Sun", "correct": False,
             "why": "Ultraviolet is past visible light and carries enough "
                    "energy per wave to damage skin cells."},
            {"text": "Radio waves from a mast", "correct": True},
            {"text": "Visible light from a lamp", "correct": False,
             "why": "Light carries more per wave than infrared, which in turn "
                    "carries more than radio."},
            {"text": "Infrared from a radiator", "correct": False,
             "why": "Infrared sits between radio and visible light, so radio "
                    "is lower still."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e11",
        "band": "easier",
        "text": "Which of these carries the most energy per wave?",
        "options": [
            {"text": "Infrared", "correct": False,
             "why": "Infrared sits below visible light, near the harmless end "
                    "of the family."},
            {"text": "Visible light", "correct": False,
             "why": "Light is harmless and sits well below ultraviolet, "
                    "X-rays and gamma rays."},
            {"text": "Gamma rays", "correct": True},
            {"text": "Ultraviolet", "correct": False,
             "why": "Ultraviolet is the first risky one, but X-rays and gamma "
                    "rays are higher still."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e12",
        "band": "easier",
        "text": "Which three kinds of radiation on the word sort are the "
                "harmless ones?",
        "options": [
            {"text": "Radio waves, infrared and visible light",
             "correct": True},
            {"text": "Infrared, visible light and ultraviolet",
             "correct": False,
             "why": "Ultraviolet is the first risky one. The boundary sits "
                    "just above visible light."},
            {"text": "Ultraviolet, X-rays and gamma rays",
             "correct": False,
             "why": "Those are the three risky ones. Each carries enough "
                    "energy per wave to break a molecule."},
            {"text": "Radio waves, X-rays and gamma rays",
             "correct": False,
             "why": "Radio is harmless but X-rays and gamma rays are the two "
                    "most dangerous of the six."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e13",
        "band": "easier",
        "text": "What does a thermal camera actually detect?",
        "options": [
            {"text": "The infrared radiation an object is emitting",
             "correct": True},
            {"text": "The visible light reflecting off the object",
             "correct": False,
             "why": "A thermal camera works in a completely dark room, so it "
                    "cannot be using visible light."},
            {"text": "The temperature of the air between",
             "correct": False,
             "why": "It reads the object, not the air. The air between makes "
                    "very little difference."},
            {"text": "The warm air rising off the object as it is heated up",
             "correct": False,
             "why": "Rising air is convection. A thermal camera works fine "
                    "with no air there at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e14",
        "band": "easier",
        "text": "Does a block of ice emit infrared radiation?",
        "options": [
            {"text": "No, because ice is far too cold to emit any infrared at "
                     "all",
             "correct": False,
             "why": "Everything above absolute zero emits, and ice is far "
                    "above it."},
            {"text": "No, because only warm objects are able to emit",
             "correct": False,
             "why": "Cold objects emit as well. Being cold means emitting "
                    "less, not emitting nothing."},
            {"text": "Yes, but only while it is melting",
             "correct": False,
             "why": "Melting has nothing to do with it. A block of ice in a "
                    "freezer emits too."},
            {"text": "Yes — everything above absolute zero always does",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e15",
        "band": "easier",
        "text": "What happens to the infrared a surface emits as that surface "
                "gets hotter?",
        "options": [
            {"text": "It emits more", "correct": True},
            {"text": "It emits less, as the energy stays inside",
             "correct": False,
             "why": "A hotter surface emits more, not less. That is how a "
                    "thermal camera tells hot from cold."},
            {"text": "It emits the same at any temperature",
             "correct": False,
             "why": "If that were true a thermal camera could not tell one "
                    "object from another."},
            {"text": "It stops emitting once it glows",
             "correct": False,
             "why": "Glowing means it has begun emitting visible light as "
                    "well. The infrared is stronger than ever."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e16",
        "band": "easier",
        "text": "Which surface emits infrared radiation best?",
        "options": [
            {"text": "A polished silver one, which shines", "correct": False,
             "why": "A shiny silver surface is the worst emitter of the two. "
                    "That is why a flask is silvered."},
            {"text": "A matt black one", "correct": True},
            {"text": "Neither — the surface makes no difference",
             "correct": False,
             "why": "The surface makes a large difference, which is why cans "
                    "with different finishes cool at different rates."},
            {"text": "Whichever one is smoother",
             "correct": False,
             "why": "Smooth and shiny emits worst. A matt finish is the "
                    "better emitter."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e17",
        "band": "easier",
        "text": "Which surface absorbs the most radiation falling on it?",
        "options": [
            {"text": "A shiny silver surface, because it holds on to "
                     "everything",
             "correct": False,
             "why": "A shiny surface reflects most of what arrives rather "
                    "than taking it in."},
            {"text": "A matt black surface, because it reflects very little "
                     "of what arrives",
             "correct": True},
            {"text": "A clear glass surface, which radiation passes into",
             "correct": False,
             "why": "Passing through is not absorbing. Glass lets most of it "
                    "go on its way."},
            {"text": "All surfaces absorb equally, whatever they look like",
             "correct": False,
             "why": "They differ a great deal, which is why a black car gets "
                    "hotter than a white one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e18",
        "band": "easier",
        "text": "Which surface reflects the most radiation?",
        "options": [
            {"text": "A matt black one, because dark turns it back",
             "correct": False,
             "why": "Matt black is the best absorber there is, which is the "
                    "opposite of a good reflector."},
            {"text": "A rough grey one, which scatters",
             "correct": False,
             "why": "Roughness scatters some but absorbs a great deal. Shine "
                    "is what reflects."},
            {"text": "They all reflect the same",
             "correct": False,
             "why": "Shiny and matt surfaces behave very differently, which "
                    "is why survival blankets are shiny."},
            {"text": "A shiny silver one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e19",
        "band": "easier",
        "text": "What is a vacuum?",
        "options": [
            {"text": "A space that is very cold but has some air in it",
             "correct": False,
             "why": "A vacuum is defined by having no particles, not by being "
                    "cold or by having a little air."},
            {"text": "A space with no particles in it at all",
             "correct": True},
            {"text": "A space no energy crosses",
             "correct": False,
             "why": "Radiation crosses a vacuum perfectly well. It is the "
                    "only route that can."},
            {"text": "A space full of gas",
             "correct": False,
             "why": "Any gas at all means particles, and particles mean it is "
                    "not a vacuum."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e20",
        "band": "easier",
        "text": "You can feel a fire's warmth on your face from across a "
                "room. Which route delivers it?",
        "options": [
            {"text": "Radiation, straight across the room in a line",
             "correct": True},
            {"text": "Conduction, along the air between",
             "correct": False,
             "why": "Air is one of the worst conductors there is, and it "
                    "could not deliver warmth that quickly."},
            {"text": "Convection, in the air of the room",
             "correct": False,
             "why": "Warm air rises to the ceiling. It does not cross the "
                    "room to your face."},
            {"text": "None of them — nothing arrives",
             "correct": False,
             "why": "Step behind a screen and it stops at once, so something "
                    "is certainly arriving."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e21",
        "band": "easier",
        "text": "Which objects in a room are emitting infrared radiation "
                "right now?",
        "options": [
            {"text": "Only the ones plugged in and switched on at the wall",
             "correct": False,
             "why": "Nothing needs to be powered. A cold stone in a field "
                    "emits infrared."},
            {"text": "Only the ones warmer than the person in the room",
             "correct": False,
             "why": "Cooler objects emit too. Being cooler means emitting "
                    "less, never none."},
            {"text": "Every single one of them, including you",
             "correct": True},
            {"text": "Only the dark or matt ones",
             "correct": False,
             "why": "A matt surface emits better, but a shiny one still "
                    "emits. Every object does."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e22",
        "band": "easier",
        "text": "Can radiation pass through a closed glass window?",
        "options": [
            {"text": "No, because glass has no gaps in it for radiation to use",
             "correct": False,
             "why": "You can see through a window, and light is radiation. It "
                    "passes easily."},
            {"text": "No, because a window is airtight and seals it",
             "correct": False,
             "why": "Radiation needs no air at all. It crosses an entire "
                    "vacuum without difficulty."},
            {"text": "Yes, but only the visible light",
             "correct": False,
             "why": "Plenty of infrared comes through too, which is why a "
                    "sunlit room warms up."},
            {"text": "Yes — which is why sunlight warms a closed room",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e23",
        "band": "easier",
        "text": "Does infrared radiation carry enough energy per wave to "
                "damage a molecule?",
        "options": [
            {"text": "Yes, which is why radiators are thought to be unsafe",
             "correct": False,
             "why": "Radiators are entirely safe. Infrared warms things and "
                    "cannot break them."},
            {"text": "No — it can only warm something and nothing more",
             "correct": True},
            {"text": "Yes, if the surface is hot enough",
             "correct": False,
             "why": "A hotter surface emits more waves, not more energetic "
                    "ones of a damaging kind."},
            {"text": "No, infrared is not radiation",
             "correct": False,
             "why": "It is radiation, and part of the same family. It simply "
                    "sits at the harmless end of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e24",
        "band": "easier",
        "text": "Where does infrared sit relative to visible light?",
        "options": [
            {"text": "Just beyond red, at a longer wavelength",
             "correct": True},
            {"text": "Just beyond violet, at a much shorter wavelength than "
                     "red",
             "correct": False,
             "why": "Just beyond violet is ultraviolet, which is the first "
                    "risky one."},
            {"text": "In the middle of the visible range",
             "correct": False,
             "why": "If it were there you would see it. Infrared is outside "
                    "the visible range altogether."},
            {"text": "Far above gamma rays",
             "correct": False,
             "why": "Gamma rays are the top. Infrared is near the bottom, "
                    "below visible light."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e25",
        "band": "easier",
        "text": "A patio heater warms people sitting under it even on a cold "
                "evening. Why does the cold air not stop it?",
        "options": [
            {"text": "Because the heater warms all the air in the garden first",
             "correct": False,
             "why": "Outdoor air is impossible to warm. The people feel the "
                    "radiation directly."},
            {"text": "Because the radiation travels straight to them without "
                     "needing the air at all",
             "correct": True},
            {"text": "Because the cold air is pushed aside by warm air rising",
             "correct": False,
             "why": "Warm air does rise, but it rises away from the people "
                    "rather than towards them."},
            {"text": "Because a heater makes the air around it heavier",
             "correct": False,
             "why": "Warm air is lighter, not heavier, and the warmth arrives "
                    "by radiation in any case."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e26",
        "band": "easier",
        "text": "What does it mean to say an object emits radiation?",
        "options": [
            {"text": "That it takes radiation in from around it",
             "correct": False,
             "why": "Taking it in is absorbing. Emitting is the other "
                    "direction entirely."},
            {"text": "That it bounces radiation back the way it came",
             "correct": False,
             "why": "That is reflecting. A shiny surface does it well and a "
                    "matt one badly."},
            {"text": "That it gives radiation out", "correct": True},
            {"text": "That it lets radiation pass through",
             "correct": False,
             "why": "That is transmitting, which is what a window does. "
                    "Emitting means giving out."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e27",
        "band": "easier",
        "text": "Which one of these is NOT radiation?",
        "options": [
            {"text": "Conduction along a metal bar", "correct": True},
            {"text": "Infrared from a warm radiator", "correct": False,
             "why": "Infrared is radiation, and it is the kind this lesson is "
                    "mostly about."},
            {"text": "Visible light from a desk lamp", "correct": False,
             "why": "Light is radiation. You are being irradiated by your "
                    "lamp as you read."},
            {"text": "Radio from a mast", "correct": False,
             "why": "Radio waves are radiation, at the lowest-energy end of "
                    "the family."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e28",
        "band": "easier",
        "text": "Which end of the family of waves can do harm?",
        "options": [
            {"text": "The low-energy end, where radio waves and infrared sit",
             "correct": False,
             "why": "That end is harmless. Radio and infrared cannot break a "
                    "molecule at any strength."},
            {"text": "Both ends equally, since all radiation is risky",
             "correct": False,
             "why": "No amount of radio waves will break a molecule. Amount "
                    "is not the distinction."},
            {"text": "Neither end — none of it is harmful",
             "correct": False,
             "why": "Ultraviolet, X-rays and gamma rays are genuinely risky, "
                    "which is why doses are controlled."},
            {"text": "The high-energy end, from ultraviolet upwards",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e29",
        "band": "easier",
        "text": "Why does a radiographer step out of the room before taking "
                "an X-ray?",
        "options": [
            {"text": "Because X-rays carry enough energy to damage cells, and "
                     "the doses add up over a working day",
             "correct": True},
            {"text": "Because the machine makes a very loud noise to stand "
                     "beside",
             "correct": False,
             "why": "Noise is not the reason. The hazard is the radiation "
                    "itself."},
            {"text": "Because standing close would spoil the picture being "
                     "taken",
             "correct": False,
             "why": "A person standing nearby does not blur the image. The "
                    "reason is the dose they would receive."},
            {"text": "Because X-rays cannot pass through a closed door",
             "correct": False,
             "why": "The shielding in the wall is what stops them, and it is "
                    "there because they are hazardous."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e30",
        "band": "easier",
        "text": "Which kind of radiation from the Sun causes sunburn?",
        "options": [
            {"text": "Infrared, the part you feel as warmth",
             "correct": False,
             "why": "Infrared warms you and nothing more. You can burn on a "
                    "cool but bright day."},
            {"text": "Visible light, the brightest part of it",
             "correct": False,
             "why": "Light is harmless. Reading by it would be a hazard if it "
                    "were not."},
            {"text": "Radio waves, the most plentiful",
             "correct": False,
             "why": "Radio waves are the lowest-energy of the family and "
                    "cannot damage skin at all."},
            {"text": "Ultraviolet", "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-06-s07",
        "band": "standard",
        "text": "Why can the Sun's energy not reach the Earth by conduction?",
        "options": [
            {"text": "Because conduction needs particles in contact, and "
                     "space between has none",
             "correct": True},
            {"text": "Because the distance involved is far too great for any "
                     "conduction to be able to cover it",
             "correct": False,
             "why": "Distance slows conduction but does not forbid it. The "
                    "missing particles do."},
            {"text": "Because conduction only ever works downwards, and the "
                     "Sun is above the Earth",
             "correct": False,
             "why": "Conduction ignores direction entirely. A rod pointing "
                    "down conducts as well as one pointing up."},
            {"text": "Because the Sun is too hot for it",
             "correct": False,
             "why": "A higher temperature makes conduction faster, not "
                    "impossible. The vacuum is the obstacle."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s08",
        "band": "standard",
        "text": "A detector is placed level with a hot object rather than "
                "above it, in air. Why does convection deliver nothing?",
        "options": [
            {"text": "Because convection only works over very short distances "
                     "and the detector is too far away",
             "correct": False,
             "why": "Convection carries energy right up to a ceiling. "
                    "Direction, not distance, is the problem."},
            {"text": "Because convection needs a solid to travel through",
             "correct": False,
             "why": "Convection needs a fluid, which air is. It is the "
                    "direction of the flow that rules it out."},
            {"text": "Because the air beside a hot object is always colder "
                     "than the air above it can be",
             "correct": False,
             "why": "Air beside a hot object does warm. It simply rises as "
                    "soon as it does."},
            {"text": "Because warm air always rises, so the moving air goes "
                     "up rather than sideways",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s09",
        "band": "standard",
        "text": "You sit under a patio heater and feel warm on the top of "
                "your head. Which route is delivering that?",
        "options": [
            {"text": "Convection, because the warm air from the heater falls "
                     "down on to you from above",
             "correct": False,
             "why": "Warm air rises away from the heater. Nothing warm comes "
                    "down by convection."},
            {"text": "Conduction, along the column of air between the heater "
                     "and the top of your head",
             "correct": False,
             "why": "Air conducts extremely badly and could not deliver "
                    "warmth that quickly over that distance."},
            {"text": "Radiation, which travels downwards as easily as it "
                     "travels up",
             "correct": True},
            {"text": "All three at once, since the heater is hot enough to "
                     "use every route available to it",
             "correct": False,
             "why": "Only one route works downwards. The other two need "
                    "contact or rising air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s10",
        "band": "standard",
        "text": "At a camp fire, one person holds their hands above the "
                "flames and another holds theirs beside. Compare the routes.",
        "options": [
            {"text": "Above gets convection and radiation; beside gets "
                     "radiation only",
             "correct": True},
            {"text": "Above gets radiation only, and beside gets both "
                     "convection and radiation together",
             "correct": False,
             "why": "That is the two positions swapped. Rising air goes up, "
                    "not sideways."},
            {"text": "Both positions get exactly the same two routes as each "
                     "other, in the same amounts",
             "correct": False,
             "why": "Only the position above is in the rising air, so the two "
                    "cannot be the same."},
            {"text": "Both positions get conduction only, through the air "
                     "between them and the fire",
             "correct": False,
             "why": "Air is a very poor conductor, so almost nothing arrives "
                    "by that route at either position."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s11",
        "band": "standard",
        "text": "Two identical kettles of boiling water are left on a bench, "
                "one polished silver and one matt black. Which stays hot "
                "longer?",
        "options": [
            {"text": "The matt black one, because a dark surface holds its "
                     "energy in rather than letting it go",
             "correct": False,
             "why": "A matt black surface is the best emitter of the two, so "
                    "it loses energy fastest."},
            {"text": "Neither, because the water inside them is identical and "
                     "the outside cannot matter",
             "correct": False,
             "why": "The surface decides how fast infrared leaves, so it "
                    "matters a great deal."},
            {"text": "The matt black one, because black paint is a thicker "
                     "layer than polish is",
             "correct": False,
             "why": "Thickness of paint is not the mechanism. How well the "
                    "surface emits infrared is."},
            {"text": "The polished silver one, because a shiny surface emits "
                     "infrared poorly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s12",
        "band": "standard",
        "text": "Houses in hot countries are often painted white. What does "
                "that achieve?",
        "options": [
            {"text": "The white surface reflects much of the Sun's radiation "
                     "instead of absorbing it",
             "correct": True},
            {"text": "The white paint stops the walls from emitting any "
                     "infrared",
             "correct": False,
             "why": "All surfaces emit. The saving comes from taking less in, "
                    "not from giving none out."},
            {"text": "The white paint keeps the cold of the night inside the "
                     "walls until the following evening",
             "correct": False,
             "why": "Cold is not a thing that can be kept anywhere. Only "
                    "energy moves."},
            {"text": "The white surface conducts the Sun's energy away",
             "correct": False,
             "why": "Paint colour does not change conduction. It changes how "
                    "much radiation is absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s13",
        "band": "standard",
        "text": "A solar cooker is a curved shiny dish with a black pot at "
                "its centre. Explain the two choices of surface.",
        "options": [
            {"text": "The dish reflects the Sun's radiation on to the pot, "
                     "and the black pot absorbs it well",
             "correct": True},
            {"text": "The dish absorbs the Sun's radiation and then conducts "
                     "it along to the pot at the centre",
             "correct": False,
             "why": "A shiny dish absorbs badly, and there is a gap between "
                    "dish and pot in any case."},
            {"text": "The dish emits its own radiation towards the pot, which "
                     "is why it has to be shiny",
             "correct": False,
             "why": "A shiny surface is the worst emitter there is. The dish "
                    "reflects rather than emits."},
            {"text": "The black pot reflects the radiation back up",
             "correct": False,
             "why": "Black absorbs and reflects very little, which is exactly "
                    "why the pot is black."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s14",
        "band": "standard",
        "text": "A car parked in the sun with its windows shut becomes far "
                "hotter inside than the air outside. Why?",
        "options": [
            {"text": "Because the closed windows trap the outside air, which "
                     "then has nowhere else to go",
             "correct": False,
             "why": "The trapped air starts at the outside temperature. "
                    "Something has to warm it."},
            {"text": "Because the metal body conducts the warmth of the road "
                     "up into the inside of the car",
             "correct": False,
             "why": "A car parked on cool tarmac still bakes. The energy "
                    "arrives as radiation through the glass."},
            {"text": "Because radiation passes in through the glass and is "
                     "absorbed by the seats and dashboard",
             "correct": True},
            {"text": "Because a car makes warmth of its own while parked",
             "correct": False,
             "why": "The engine is off and nothing inside is making energy. "
                    "All of it comes from the Sun."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s15",
        "band": "standard",
        "text": "Frost is far more likely on a clear night than on a cloudy "
                "one. What explains that?",
        "options": [
            {"text": "Clouds hold the cold of the upper air away from the "
                     "ground until the morning comes",
             "correct": False,
             "why": "There is no cold to hold. Clouds return radiation the "
                    "ground has emitted."},
            {"text": "Clear skies let the ground radiate away into space, "
                     "while cloud sends some back down",
             "correct": True},
            {"text": "Clouds conduct energy down to the ground all night, "
                     "which is what keeps it above freezing",
             "correct": False,
             "why": "Clouds are not touching the ground, so conduction is "
                    "impossible. They radiate."},
            {"text": "Clear nights are always windier than cloudy ones",
             "correct": False,
             "why": "Wind is not the difference. What the sky does with the "
                    "ground's radiation is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s16",
        "band": "standard",
        "text": "A thermal camera produces a clear picture in a room with the "
                "lights off and the curtains shut. Why?",
        "options": [
            {"text": "Because the camera uses a very sensitive kind of "
                     "visible-light sensor to see in the dark",
             "correct": False,
             "why": "There is no visible light to be sensitive to. It detects "
                    "infrared instead."},
            {"text": "Because the camera sends out its own beam of light and "
                     "then measures what comes back",
             "correct": False,
             "why": "It sends out nothing. It reads the infrared the objects "
                    "are already emitting."},
            {"text": "Because the objects in the room are emitting infrared "
                     "whether the lights are on or not",
             "correct": True},
            {"text": "Because dark rooms are warmer than lit ones",
             "correct": False,
             "why": "Room temperature is not the point. The objects emit "
                    "infrared at any temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s17",
        "band": "standard",
        "text": "A survival blanket is shiny on both sides. Which property is "
                "doing the work when one is wrapped round a casualty?",
        "options": [
            {"text": "The shine reflects the casualty's own radiation back "
                     "towards them",
             "correct": True},
            {"text": "The shine makes the blanket a much better conductor, so "
                     "warmth spreads evenly over the body",
             "correct": False,
             "why": "Spreading energy through the blanket would move it away "
                    "from the casualty, not towards them."},
            {"text": "The shine lets the blanket emit a great deal of its own "
                     "infrared on to the casualty",
             "correct": False,
             "why": "A shiny surface is the worst emitter, and the blanket "
                    "has no energy of its own anyway."},
            {"text": "The shine attracts warmth out of the air nearby and "
                     "holds it against you",
             "correct": False,
             "why": "Nothing attracts warmth. The blanket returns what the "
                    "casualty is already emitting."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s18",
        "band": "standard",
        "text": "Two identical cans of cold water, one matt black and one "
                "polished silver, are left in bright sunshine. Which warms "
                "faster?",
        "options": [
            {"text": "The silver one, because shiny metal takes in radiation "
                     "faster than paint does",
             "correct": False,
             "why": "Shiny surfaces reflect most of what arrives. They are "
                    "the worst absorbers."},
            {"text": "Neither, because both cans are standing in exactly the "
                     "same sunshine as each other",
             "correct": False,
             "why": "The same radiation arrives at both, but they take in "
                    "very different amounts of it."},
            {"text": "The black one, because a matt dark surface absorbs "
                     "radiation well",
             "correct": True},
            {"text": "The silver one, because silver conducts energy better "
                     "than black paint does",
             "correct": False,
             "why": "Both cans are metal, so conduction through the wall is "
                    "the same. The surface is what differs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s19",
        "band": "standard",
        "text": "Why is the harmless-or-risky boundary about energy per wave "
                "rather than about how bright or strong the source is?",
        "options": [
            {"text": "Because a very bright source of radio waves would be "
                     "just as dangerous as a weak X-ray source",
             "correct": False,
             "why": "It would not. No quantity of radio waves can break a "
                    "molecule."},
            {"text": "Because strong sources are always high-energy ones",
             "correct": False,
             "why": "A powerful radio transmitter is strong and low-energy. "
                    "The two are independent."},
            {"text": "Because brightness cannot be measured, so energy per "
                     "wave is used",
             "correct": False,
             "why": "Brightness is easily measured. It is simply not what "
                    "decides whether damage is possible."},
            {"text": "Because one wave either carries enough energy to break "
                     "a molecule or it does not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s20",
        "band": "standard",
        "text": "Put these in order of increasing energy per wave: visible "
                "light, radio waves, gamma rays, infrared.",
        "options": [
            {"text": "Radio, infrared, visible, gamma", "correct": True},
            {"text": "Gamma, visible, infrared, radio", "correct": False,
             "why": "That is the correct order reversed. Gamma rays are the "
                    "highest, not the lowest."},
            {"text": "Infrared, radio, gamma, visible", "correct": False,
             "why": "Radio sits below infrared, and visible light below "
                    "gamma rays."},
            {"text": "Visible, gamma, radio, infrared", "correct": False,
             "why": "Visible light is above infrared and radio, and gamma "
                    "rays are above everything."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s21",
        "band": "standard",
        "text": "A room with a newly lit fire feels warm near the fire long "
                "before the air in the room has warmed up. Why?",
        "options": [
            {"text": "Because the fire's radiation arrives at once, while "
                     "warming the air takes much longer",
             "correct": True},
            {"text": "Because a fire always warms solid objects first and "
                     "only warms the air in a room afterwards",
             "correct": False,
             "why": "The order is not about solids and gases. It is about "
                    "radiation arriving immediately."},
            {"text": "Because the air near a fire is pushed away, leaving "
                     "nothing between you and the flames",
             "correct": False,
             "why": "The air stays where it is. Radiation would reach you "
                    "through it regardless."},
            {"text": "Because a new fire is hotter than an old one",
             "correct": False,
             "why": "A new fire is usually cooler. The speed of arrival is "
                    "what is being asked about."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s22",
        "band": "standard",
        "text": "A greenhouse stays warm on a cold but sunny day. Which "
                "account of that is right?",
        "options": [
            {"text": "The glass creates warmth of its own whenever sunlight "
                     "falls on to the outside of it",
             "correct": False,
             "why": "Glass creates nothing. Every joule inside arrived from "
                    "the Sun."},
            {"text": "Radiation passes in through the glass and warms the "
                     "soil and plants, and the warm air is kept in",
             "correct": True},
            {"text": "The cold outside air is blocked by the glass, which is "
                     "the only reason the inside stays warm",
             "correct": False,
             "why": "Blocking the wind helps, but an unlit greenhouse at "
                    "night gets cold. The Sun's radiation is the source."},
            {"text": "The glass conducts warmth inwards from the cold air",
             "correct": False,
             "why": "Energy never conducts from colder to warmer. The source "
                    "is the sunlight passing through."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s23",
        "band": "standard",
        "text": "X-rays are known to be risky and are still used in "
                "hospitals. What makes that a reasonable decision?",
        "options": [
            {"text": "They are only risky for the radiographer, and never for "
                     "the patient being photographed",
             "correct": False,
             "why": "The dose reaches the patient too. It is kept small "
                    "rather than being absent."},
            {"text": "The dose from one scan is small, and knowing what is "
                     "broken is worth that small risk",
             "correct": True},
            {"text": "X-rays stop being risky as soon as a machine is "
                     "properly maintained and correctly set up",
             "correct": False,
             "why": "A well-maintained machine still delivers a dose. "
                    "Maintenance controls it; it does not remove it."},
            {"text": "X-rays are not really risky at all",
             "correct": False,
             "why": "They carry enough energy per wave to ionise atoms, which "
                    "is why doses are controlled."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s24",
        "band": "standard",
        "text": "Why is ultraviolet the first of the six to be risky, when "
                "visible light just below it is harmless?",
        "options": [
            {"text": "Because ultraviolet is invisible and anything you "
                     "cannot see is more dangerous than anything you can",
             "correct": False,
             "why": "Infrared and radio are invisible and harmless. Being "
                    "invisible decides nothing."},
            {"text": "Because ultraviolet arrives in far greater quantity "
                     "from the Sun than visible light does",
             "correct": False,
             "why": "Far less UV arrives than light. It is the energy per "
                    "wave that makes the difference."},
            {"text": "Because ultraviolet is the point at which one wave "
                     "first carries enough energy to damage a molecule",
             "correct": True},
            {"text": "Because ultraviolet travels faster than light does",
             "correct": False,
             "why": "Every member of the family travels at the same speed. "
                    "Only the energy per wave differs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s25",
        "band": "standard",
        "text": "The water pipes on a solar water heater are painted matt "
                "black. Why is that the right choice?",
        "options": [
            {"text": "Because a matt black surface takes in a large share of "
                     "the radiation falling on it",
             "correct": True},
            {"text": "Because a matt black surface reflects the Sun's "
                     "radiation on to the water inside the pipes",
             "correct": False,
             "why": "Black reflects very little. Shiny surfaces are the "
                    "reflectors."},
            {"text": "Because black paint conducts energy into the water far "
                     "better than any other colour does",
             "correct": False,
             "why": "Paint colour does not change conduction. It changes how "
                    "much radiation is absorbed."},
            {"text": "Because black paint makes warmth of its own in sunshine",
             "correct": False,
             "why": "No paint makes warmth. All of it arrives from the Sun as "
                    "radiation."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s26",
        "band": "standard",
        "text": "The sunward side of a spacecraft is often covered in shiny "
                "gold or silver foil. What is that for?",
        "options": [
            {"text": "To conduct the Sun's energy round to the cooler shaded "
                     "side",
             "correct": False,
             "why": "A thin foil conducts very little round a whole "
                    "spacecraft. It reflects instead."},
            {"text": "To reflect most of the Sun's radiation away instead of "
                     "absorbing it",
             "correct": True},
            {"text": "To emit as much infrared as possible from that side",
             "correct": False,
             "why": "A shiny surface is the worst emitter. Radiator panels "
                    "elsewhere do that job."},
            {"text": "To stop the vacuum of space touching the hull",
             "correct": False,
             "why": "A vacuum is nothing and cannot touch anything. The foil "
                    "is there for the radiation."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s27",
        "band": "standard",
        "text": "On a sunny day a dark tarmac road is painfully hot but the "
                "white line painted on it is not. Explain.",
        "options": [
            {"text": "The white line is a better conductor, so it moves the "
                     "energy away into the ground beneath",
             "correct": False,
             "why": "The paint layer is far too thin to matter for "
                    "conduction. It is absorbing less to begin with."},
            {"text": "The dark surface absorbs far more of the Sun's "
                     "radiation than the white paint does",
             "correct": True},
            {"text": "The white line is shaded by the cars driving over it "
                     "for most of the daylight hours",
             "correct": False,
             "why": "The line is in full sun like the rest of the road. "
                    "Colour, not shade, is the difference."},
            {"text": "The white line emits its own cold upwards",
             "correct": False,
             "why": "Nothing emits cold. Cold is not a substance and has "
                    "nothing to emit."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s28",
        "band": "standard",
        "text": "A student says a radiator “only sends its radiation "
                "sideways into the room”. What is wrong with that?",
        "options": [
            {"text": "Nothing — radiation really does travel horizontally "
                     "and in no other direction",
             "correct": False,
             "why": "It travels in every direction. Standing above a radiator "
                    "shows it at once."},
            {"text": "Radiation from a radiator only ever travels upwards",
             "correct": False,
             "why": "Upward travel is the warm AIR. The radiation goes every "
                    "way at once."},
            {"text": "A radiator gives out no radiation at all, so the "
                     "direction does not come into it",
             "correct": False,
             "why": "It gives out plenty of infrared, which is how it warms "
                    "you across a room."},
            {"text": "Radiation always leaves in every direction, up to the "
                     "ceiling and down to the floor",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s29",
        "band": "standard",
        "text": "Standing closer to a bonfire feels hotter straight away, "
                "before the air around you has changed at all. Why?",
        "options": [
            {"text": "Because the air nearer a fire is always at a much "
                     "higher temperature than the air further away",
             "correct": False,
             "why": "The stem says the air has not changed. The extra warmth "
                    "arrives without it."},
            {"text": "Because more of the fire's radiation lands on you when "
                     "you are closer to it",
             "correct": True},
            {"text": "Because radiation travels more quickly over a short "
                     "distance than it does over a long one",
             "correct": False,
             "why": "Its speed is the same at any distance. What changes is "
                    "how much of it reaches you."},
            {"text": "Because conduction through the air improves when you "
                     "stand nearer to the source of the warmth",
             "correct": False,
             "why": "Air conducts very badly at any distance, and the effect "
                    "is felt far too quickly for conduction."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s30",
        "band": "standard",
        "text": "An object and a detector are put in a jar and the air is "
                "pumped out. What happens to the reading if the object is "
                "then made hotter?",
        "options": [
            {"text": "It falls, because a hotter object emits less infrared "
                     "than a cooler one does",
             "correct": False,
             "why": "A hotter surface emits more, which is exactly how a "
                    "thermal camera works."},
            {"text": "It does not change, because the jar has no air left in "
                     "it to carry anything across",
             "correct": False,
             "why": "Radiation needs no air, so the reading responds exactly "
                    "as it would with air present."},
            {"text": "It rises, because a hotter surface emits more infrared "
                     "and radiation crosses the vacuum",
             "correct": True},
            {"text": "It drops to zero, since a vacuum blocks radiation",
             "correct": False,
             "why": "A vacuum is the one thing that never blocks radiation. "
                    "It blocks the other two routes."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-06-h07",
        "band": "harder",
        "text": "If every object emits radiation, why is the night sky dark "
                "rather than blazing in every direction?",
        "options": [
            {"text": "Because light from the most distant parts has not had "
                     "time to reach us, and what does arrive is stretched",
             "correct": True},
            {"text": "Because space is a vacuum, and a vacuum blocks the "
                     "radiation coming from the far side of it",
             "correct": False,
             "why": "A vacuum is the one thing that never blocks radiation. "
                    "That is why sunlight reaches us at all."},
            {"text": "Because the stars in between absorb everything before "
                     "any of it can arrive here",
             "correct": False,
             "why": "Stars emit far more than they absorb. Adding stars would "
                    "make the sky brighter."},
            {"text": "Because only hot objects emit, and space is cold",
             "correct": False,
             "why": "Everything above absolute zero emits, and the stars in "
                    "question are extremely hot."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h08",
        "band": "harder",
        "text": "A thermal camera pointed at a snowy field still shows a "
                "picture. What does that prove?",
        "options": [
            {"text": "That the camera must be detecting the visible light "
                     "reflecting off the snow instead",
             "correct": False,
             "why": "It works in the dark, so visible light cannot be what it "
                    "is reading."},
            {"text": "That the snow is emitting infrared too, just less than "
                     "the things around it",
             "correct": True},
            {"text": "That snow is warmer than it looks and is well above the "
                     "freezing point of water",
             "correct": False,
             "why": "The snow is genuinely at or below freezing and still "
                    "emits. Emission does not need warmth."},
            {"text": "That the camera is producing its own infrared",
             "correct": False,
             "why": "It emits nothing. It reads what the field is already "
                    "giving out."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h09",
        "band": "harder",
        "text": "Evaluate the claim: “only hot things give out "
                "infrared radiation.”",
        "options": [
            {"text": "Correct, because an object has to be above room "
                     "temperature before it can begin to emit",
             "correct": False,
             "why": "Room temperature is not a threshold. Everything above "
                    "absolute zero emits."},
            {"text": "Correct, but only for solids — every liquid and gas "
                     "emits at any temperature at all",
             "correct": False,
             "why": "The state of matter makes no difference. Solids, liquids "
                    "and gases all emit."},
            {"text": "Wrong — everything above absolute zero emits, and "
                     "temperature decides only how much",
             "correct": True},
            {"text": "Wrong, because in fact only cold things are able to emit "
                     "any infrared radiation at all",
             "correct": False,
             "why": "That inverts the claim rather than correcting it. Hot "
                    "things emit the most."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h10",
        "band": "harder",
        "text": "A desert is fiercely hot by day and can be near freezing by "
                "night. Explain both, in terms of radiation.",
        "options": [
            {"text": "Cold air from higher up sinks into the desert at night, "
                     "and warmer air comes back to replace it by day",
             "correct": False,
             "why": "Moving air is convection and does not explain the size "
                    "of the swing. Radiation does."},
            {"text": "The sand absorbs strongly by day and, with dry cloudless "
                     "skies, radiates away freely by night",
             "correct": True},
            {"text": "The desert is closer to the Sun at midday and much "
                     "further from it at midnight",
             "correct": False,
             "why": "The distance to the Sun barely changes. What changes is "
                    "whether radiation is arriving."},
            {"text": "Sand conducts energy up by day and down by night",
             "correct": False,
             "why": "Sand conducts badly, and conduction has no preferred "
                    "direction. The route is radiation."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h11",
        "band": "harder",
        "text": "In a vacuum flask the silvering is on the two surfaces that "
                "face the vacuum gap. Why there, rather than outside?",
        "options": [
            {"text": "Because those are the surfaces the radiation has to "
                     "cross the gap between",
             "correct": True},
            {"text": "Because silver on the outside of a flask would be "
                     "scratched by ordinary handling and use",
             "correct": False,
             "why": "Wear is a practical matter. The physical reason is that "
                    "the gap is where radiation crosses."},
            {"text": "Because silver has to be kept away from the air to go "
                     "on reflecting anything at all",
             "correct": False,
             "why": "Silver reflects in air perfectly well. Mirrors do it "
                    "every day."},
            {"text": "Because silver conducts energy well, and it must never "
                     "be allowed to touch the tea",
             "correct": False,
             "why": "The inner wall already touches the drink. Its job on the "
                    "gap side is reflection."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h12",
        "band": "harder",
        "text": "Spacesuits and probes are wrapped in reflective layers. What "
                "problem does that solve that insulation alone could not?",
        "options": [
            {"text": "The layers stop conduction into the vacuum, which is "
                     "the main way energy would be lost out there",
             "correct": False,
             "why": "There is no conduction into a vacuum at all, so nothing "
                    "is needed to stop it."},
            {"text": "The layers stop convection currents forming in the "
                     "vacuum around the suit while it is in sunlight",
             "correct": False,
             "why": "Convection is impossible in a vacuum too. Radiation is "
                    "the only route left."},
            {"text": "The layers make the suit a great deal heavier, which "
                     "slows any energy trying to pass through",
             "correct": False,
             "why": "Weight does not slow energy transfer. Reflection does."},
            {"text": "Radiation is the only route in or out in a vacuum, and "
                     "reflection is what controls it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h13",
        "band": "harder",
        "text": "Why is radiation the only one of the three routes that works "
                "upwards, downwards and sideways equally?",
        "options": [
            {"text": "Because it travels in straight lines from the source "
                     "and gravity has no hold on it at all",
             "correct": True},
            {"text": "Because it travels so fast that gravity does not get "
                     "the chance to pull it down before it arrives",
             "correct": False,
             "why": "Speed is not the reason. Gravity has no useful hold on "
                    "radiation at any speed."},
            {"text": "Because it is the only route that can carry energy in "
                     "more than one direction at once",
             "correct": False,
             "why": "Conduction carries energy along a bar in any direction "
                    "too. What it needs is contact."},
            {"text": "Because it is very much lighter than warm air is and so "
                     "is never pulled downwards",
             "correct": False,
             "why": "Radiation is a wave and has no weight to compare. Warm "
                    "air rising is a separate route."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h14",
        "band": "harder",
        "text": "A matt black surface is the best absorber and also the best "
                "emitter. Why is that not a contradiction?",
        "options": [
            {"text": "Because absorbing and emitting are two entirely separate "
                     "properties that simply agree by coincidence",
             "correct": False,
             "why": "It is not a coincidence. The same surface property "
                    "controls both directions."},
            {"text": "Because a surface can only emit the radiation it has "
                     "already absorbed from somewhere else",
             "correct": False,
             "why": "A surface emits because of its own temperature, whether "
                    "or not anything is shining on it."},
            {"text": "Because black surfaces are always hotter than others",
             "correct": False,
             "why": "A black surface in the shade is at room temperature like "
                    "everything else."},
            {"text": "Because the same surface property controls how easily "
                     "radiation crosses it in either direction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h15",
        "band": "harder",
        "text": "A phone mast is safe to live near and a sunbed is not. "
                "Explain the difference, given that both emit radiation.",
        "options": [
            {"text": "A mast is far away and a sunbed is close, and distance "
                     "is the only thing that matters here",
             "correct": False,
             "why": "Distance changes how much arrives, not whether a wave "
                    "can break a molecule. It cannot."},
            {"text": "A mast emits radio waves, which cannot damage a "
                     "molecule; a sunbed emits ultraviolet, which can",
             "correct": True},
            {"text": "A mast emits far less radiation in total than a sunbed "
                     "does over the same length of time",
             "correct": False,
             "why": "A mast is a powerful transmitter. Quantity is not what "
                    "decides the risk."},
            {"text": "A sunbed is hotter than a mast, and heat is the hazard",
             "correct": False,
             "why": "Temperature is not the hazard. A sunbed's UV would burn "
                    "you even if the lamp felt cool."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h16",
        "band": "harder",
        "text": "Infrared from a fire feels far hotter than sunlight, yet "
                "sunlight causes sunburn and the fire does not. Why?",
        "options": [
            {"text": "The fire's infrared cannot reach your skin cells, "
                     "because it stops at the surface of your body",
             "correct": False,
             "why": "Ultraviolet is absorbed at the surface too. The "
                    "difference is what one wave can do there."},
            {"text": "The feeling of heat comes from infrared, but damage "
                     "needs the energy per wave that ultraviolet carries",
             "correct": True},
            {"text": "Sunlight is brighter than a fire, and brightness is "
                     "what decides whether a burn happens",
             "correct": False,
             "why": "Brightness is quantity. Only the energy per wave decides "
                    "whether a molecule can be broken."},
            {"text": "Fires emit no ultraviolet and the Sun emits no infrared",
             "correct": False,
             "why": "Both emit both. The Sun's ultraviolet is what does the "
                    "damage."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h17",
        "band": "harder",
        "text": "The Sun has been shining on the Earth for billions of years. "
                "Why is the Earth not steadily getting hotter and hotter?",
        "options": [
            {"text": "Because the Sun's radiation is mostly reflected back "
                     "into space by the clouds before it lands",
             "correct": False,
             "why": "Clouds reflect a share, not all of it. The Earth's own "
                    "emission is what balances the books."},
            {"text": "Because the energy arriving each day is destroyed by "
                     "the atmosphere before it can build up",
             "correct": False,
             "why": "Nothing destroys energy. It leaves again as radiation."},
            {"text": "Because the Earth is also radiating, and it settles at "
                     "the temperature where out matches in",
             "correct": True},
            {"text": "Because night lasts as long as day everywhere on Earth",
             "correct": False,
             "why": "Darkness stops the arrival, but the Earth would still "
                    "warm without something leaving too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h18",
        "band": "harder",
        "text": "Design a fair test of whether surface finish changes how "
                "fast an object cools. Which plan is best?",
        "options": [
            {"text": "Identical cans, same volume of water at the same start "
                     "temperature, different finishes, timed together",
             "correct": True},
            {"text": "One matt black can of hot water and one polished can of "
                     "cold water, each timed on a different day",
             "correct": False,
             "why": "Two things have been changed at once and the conditions "
                    "differ, so nothing can be concluded."},
            {"text": "Cans of different sizes with different finishes, all "
                     "filled to the brim and timed in one room",
             "correct": False,
             "why": "Size changes the cooling rate on its own, which would "
                    "swamp the effect of the finish."},
            {"text": "One can, painted black, timed and then repainted silver",
             "correct": False,
             "why": "The room and the water would have changed between the "
                    "two runs, so they are not comparable."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h19",
        "band": "harder",
        "text": "Solar panels are tilted to face the Sun rather than laid "
                "flat. Why does the angle matter so much?",
        "options": [
            {"text": "Because a tilted panel is closer to the Sun than a flat "
                     "one is, so more energy reaches it",
             "correct": False,
             "why": "The difference in distance is nothing at all compared "
                    "with 150 million kilometres."},
            {"text": "Because radiation travels in straight lines, so a panel "
                     "square-on catches the most of it",
             "correct": True},
            {"text": "Because a tilted panel stays cooler, and a cool panel "
                     "absorbs radiation far better than a warm one",
             "correct": False,
             "why": "Absorption barely depends on the panel's temperature. "
                    "The angle is about how much lands on it."},
            {"text": "Because a flat panel reflects everything that lands",
             "correct": False,
             "why": "A flat panel absorbs plenty. It simply presents a "
                    "smaller face to the incoming radiation."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h20",
        "band": "harder",
        "text": "Traditional teapots are often shiny, and some come with a "
                "thick cosy. Which does which job?",
        "options": [
            {"text": "The shine reduces the radiation leaving, and the cosy "
                     "slows conduction and convection",
             "correct": True},
            {"text": "The shine reduces conduction through the pot wall, and "
                     "the cosy blocks the radiation from leaving",
             "correct": False,
             "why": "The two jobs are swapped. Shine works on radiation and "
                    "trapped air works on the other routes."},
            {"text": "Both of them work only on radiation, which is why a pot "
                     "needs the two of them together",
             "correct": False,
             "why": "A cosy's trapped air does very little about radiation. "
                    "It slows conduction and convection."},
            {"text": "Both work by adding warmth of their own to the tea",
             "correct": False,
             "why": "Neither has an energy supply. Both only slow the tea's "
                    "own energy leaving."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h21",
        "band": "harder",
        "text": "A vacuum flask keeps a cold drink cold as well as keeping "
                "tea hot. Explain using the same physics.",
        "options": [
            {"text": "The flask reverses its silvering when it is filled with "
                     "something cold rather than something hot",
             "correct": False,
             "why": "Nothing about the flask changes. The same surfaces do "
                    "the same job in both directions."},
            {"text": "The flask keeps the cold in by stopping it escaping "
                     "through the walls and out of the top",
             "correct": False,
             "why": "There is no cold to keep in. Energy flowing INWARDS is "
                    "what is being slowed."},
            {"text": "The same barriers slow the flow whichever way it is "
                     "going, and here it is inwards",
             "correct": True},
            {"text": "Cold drinks emit no radiation at all, so the silvering "
                     "can do nothing for them in there",
             "correct": False,
             "why": "A cold drink emits too, and the silvering works on "
                    "radiation arriving as well as leaving."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h22",
        "band": "harder",
        "text": "You feel a grill's warmth the instant it is switched on, but "
                "a metal handle takes minutes to warm. Why the difference?",
        "options": [
            {"text": "Because a grill is far hotter than a handle ever gets, "
                     "and hotter things always act faster",
             "correct": False,
             "why": "Temperature is not the point. The two routes work at "
                    "completely different speeds."},
            {"text": "Because a grill emits particles and a handle does not",
             "correct": False,
             "why": "A grill emits no particles. It emits a wave, which is "
                    "why it arrives immediately."},
            {"text": "Because the handle is a poor conductor and the air "
                     "between you and the grill is a very good one",
             "correct": False,
             "why": "Air is one of the worst conductors there is. The warmth "
                    "you feel is not arriving by conduction."},
            {"text": "Because radiation crosses the gap at once, while "
                     "conduction has to pass along particle by particle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h23",
        "band": "harder",
        "text": "A student says the vacuum in a flask is what stops the "
                "radiation. What evidence shows that is wrong?",
        "options": [
            {"text": "An unsilvered vacuum flask still loses energy steadily, "
                     "and silvering it fixes that",
             "correct": True},
            {"text": "A flask with no vacuum at all keeps tea just as hot as "
                     "one with a proper vacuum in it",
             "correct": False,
             "why": "The vacuum does a great deal of work, against conduction "
                    "and convection. It is simply not the radiation."},
            {"text": "A vacuum flask works better on cold drinks than on hot "
                     "ones, which shows the vacuum is not involved",
             "correct": False,
             "why": "It works the same in both directions, and that says "
                    "nothing about which barrier stops which route."},
            {"text": "Radiation cannot cross a vacuum, so the vacuum must "
                     "already be stopping it",
             "correct": False,
             "why": "Radiation crosses a vacuum perfectly well — that is how "
                    "sunlight reaches us. The premise is false."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h24",
        "band": "harder",
        "text": "Two identical cars, one black and one white, are parked in "
                "the same sunshine. Compare them at midday and at midnight.",
        "options": [
            {"text": "The black one is hotter at midday and the white one is "
                     "hotter at midnight, by the same amount",
             "correct": False,
             "why": "A better absorber is also a better emitter, so the black "
                    "one does not end up the warmer at night."},
            {"text": "Both are the same at midday, and the black one is "
                     "cooler by midnight because dark things cool faster",
             "correct": False,
             "why": "They differ at midday too. The black surface takes in "
                    "far more of the Sun's radiation."},
            {"text": "The black one is hotter at midday, and by midnight both "
                     "have settled near the air temperature",
             "correct": True},
            {"text": "The white one is hotter at midday, because white "
                     "surfaces hold on to the radiation they receive",
             "correct": False,
             "why": "White reflects most of what arrives, so it takes in less "
                    "and stays cooler."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h25",
        "band": "harder",
        "text": "Step behind a low wall beside a bonfire and the warmth stops "
                "at once, though the air is unchanged. What does that show?",
        "options": [
            {"text": "That the fire must have stopped burning at the exact "
                     "moment you stepped behind the wall",
             "correct": False,
             "why": "The fire is unchanged. Step back out and the warmth "
                    "returns instantly."},
            {"text": "That the air just behind a wall is very much colder than "
                     "the air in front of it",
             "correct": False,
             "why": "The stem says the air is unchanged, and the effect is "
                    "instant, which air cannot be."},
            {"text": "That the wall is absorbing the warm air before it can "
                     "reach you",
             "correct": False,
             "why": "Warm air rises over a wall rather than being absorbed, "
                    "and it was never what you were feeling."},
            {"text": "That the warmth was arriving as radiation in straight "
                     "lines, which the wall blocks",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h26",
        "band": "harder",
        "text": "A solar oven can cook food on a cold, bright winter's day. "
                "Why does the cold air not prevent it?",
        "options": [
            {"text": "Because the cold air is kept out by the glass lid, "
                     "which is the only reason the oven works at all",
             "correct": False,
             "why": "Keeping air out helps, but the energy has to arrive from "
                    "somewhere, and it arrives as radiation."},
            {"text": "Because the Sun's radiation arrives regardless of the "
                     "air temperature, and the black pot absorbs it",
             "correct": True},
            {"text": "Because cold air conducts the Sun's energy into the "
                     "oven better than warm air would",
             "correct": False,
             "why": "Air conducts badly at any temperature, and the energy "
                    "does not arrive by conduction."},
            {"text": "Because the oven makes warmth from the cold outside it",
             "correct": False,
             "why": "Cold is not a supply of anything. All of the energy "
                    "comes from the Sun."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h27",
        "band": "harder",
        "text": "On a clear night, dew forms on a car roof in the open but "
                "not on one parked under a tree. Explain.",
        "options": [
            {"text": "The tree drips extra water on to the car, which stops "
                     "dew being able to form on the roof",
             "correct": False,
             "why": "More water would make it wetter, not drier. The "
                    "difference is the roof's temperature."},
            {"text": "The open car radiates to the clear sky and cools below "
                     "the sheltered one, so dew forms on it",
             "correct": True},
            {"text": "The sheltered car is the colder of the two, and a colder "
                     "surface cannot collect any dew",
             "correct": False,
             "why": "Colder surfaces collect dew more readily. The sheltered "
                    "car is in fact the warmer of the two."},
            {"text": "The tree emits warmth, which dries the car underneath",
             "correct": False,
             "why": "The tree is at air temperature. What it does is return "
                    "radiation rather than let it escape to the sky."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h28",
        "band": "harder",
        "text": "Evaluate the claim: “space is cold, so a spacecraft "
                "in space cools down quickly.”",
        "options": [
            {"text": "Correct, because a spacecraft is surrounded by "
                     "something far colder than it is at all times",
             "correct": False,
             "why": "Being surrounded by cold only matters if there is "
                    "something there to carry the energy away."},
            {"text": "Correct, but only on the shaded side, where the "
                     "spacecraft is not in direct sunlight",
             "correct": False,
             "why": "The shaded side still has no particles to conduct into, "
                    "so it can only radiate."},
            {"text": "Wrong — with no particles to conduct or convect into, "
                     "the only way to cool is by radiating",
             "correct": True},
            {"text": "Wrong, because space is not cold at all",
             "correct": False,
             "why": "Space genuinely is cold. The claim fails because of the "
                    "missing particles, not the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h29",
        "band": "harder",
        "text": "A thermal camera can see a person in a dark room but cannot "
                "see them through a brick wall. Why not?",
        "options": [
            {"text": "Because a wall is far too cold for any infrared to make "
                     "its way out of the far side",
             "correct": False,
             "why": "The wall emits its own infrared. What it will not do is "
                    "let the person's through."},
            {"text": "Because infrared travels only in the dark and a wall "
                     "has light on at least one of its sides",
             "correct": False,
             "why": "Infrared travels in daylight too. A thermal camera works "
                    "outdoors at noon."},
            {"text": "Because brick absorbs infrared, so what the camera sees "
                     "is the wall's own emission instead",
             "correct": True},
            {"text": "Because infrared cannot pass through any solid at all",
             "correct": False,
             "why": "Some materials do let it through. Brick simply is not "
                    "one of them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h30",
        "band": "harder",
        "text": "A probe in sunlight has its sunward face at 120 °C and its "
                "shaded face at −100 °C. Explain how one object holds both.",
        "options": [
            {"text": "Because the sunward face is closer to the Sun than the "
                     "shaded face is, by the width of the probe",
             "correct": False,
             "why": "That width is nothing against 150 million kilometres. "
                    "The shadow is what matters."},
            {"text": "Because the shaded side of the probe is being cooled by "
                     "the cold of space pressing against it",
             "correct": False,
             "why": "There is no cold to press. The shaded side simply "
                    "radiates away and receives nothing."},
            {"text": "Because the metal of the probe conducts the difference "
                     "from one face to the other",
             "correct": False,
             "why": "Conduction would even the two out. It is what stops the "
                    "gap being larger still."},
            {"text": "Because one face absorbs the Sun's radiation while the "
                     "other only radiates away into empty space",
             "correct": True},
        ],
        "figure": None,
    },
]
