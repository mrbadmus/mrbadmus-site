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
]
