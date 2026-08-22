"""C10 lesson 01 — Inside the Earth: twelve questions (MRB-281).

The lesson's argument is one shape: the Earth is four layers with sharp
boundaries, nobody has been to any of them, and the whole structure was worked
out from the way earthquake waves cross the planet. The page teaches it with a
bar drawn from four real thicknesses and three inferences a student commits to
before reading the answer.

These twelve probe the angles the mastery ladder leaves alone: what each layer
is made of, what a seismic wave is, why the deepest hole ever drilled proves
almost nothing, why density is evidence, and what would have to change on a
planet whose core had frozen solid.

The distractors are built from the lesson's declared misconceptions.

`EARTH-01` (the mantle is a sea of molten lava) drives the wrong options in
e02, e03, s01, h02 and h03. Each treats melted rock as a layer rather than as
something that happens in pockets.

`EARTH-02` (nobody has been down there, so it is a guess) drives s02 and s04,
where a real chain of evidence is offered beside three that sound like
guesswork, and h01, where a familiar mental picture has to be given up because
the temperature rules it out.

`EARTH-03` (anything that hot must be melted) drives e02 and h02, where the
inner core is hotter than the liquid layer above it and solid anyway.

`EARTH-04` (the crust is a thick shell) drives e01 and s04, where every hole
ever drilled is still inside the top third of the crust.

⚠️ **NO QUESTION ASKS FOR A DEPTH TO BE RECALLED.** The boundaries are on the
page as a bar a student can read, and a bank question that rewards memorising
2900 km measures the wrong thing entirely — what the depth is FOR is that a
wave stops there, and that is what s02 and h02 ask about.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles through each
band — 1,3,0,2 · 3,0,2,1 · 0,2,1,3 — so this file holds three of each. The
ladder is a separate corpus and is balanced separately; see the lesson record.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "inside-the-earth"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-01-e01",
        "band": "easier",
        "text": "Every mine and every borehole ever dug has stayed inside "
                "one layer of the Earth. Which one?",
        "options": [
            {"text": "The mantle, which begins only a few kilometres down",
             "correct": False,
             "why": "The mantle begins about 35 km down, and no hole has "
                    "ever got anywhere near it."},
            {"text": "The crust, the thin rocky layer at the surface",
             "correct": True},
            {"text": "The outer core, where the rock becomes liquid metal",
             "correct": False,
             "why": "The outer core starts 2900 km down. It is liquid iron "
                    "and nickel, not rock."},
            {"text": "The inner core, right at the centre of the planet",
             "correct": False,
             "why": "The centre is 6371 km down. The deepest hole reached "
                    "12.3 km."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e02",
        "band": "easier",
        "text": "Which layer of the Earth is liquid?",
        "options": [
            {"text": "The crust, because it is cracked into moving plates",
             "correct": False,
             "why": "The plates move, but the crust itself is solid rock all "
                    "the way through."},
            {"text": "The mantle, because volcanoes bring lava out of it",
             "correct": False,
             "why": "The mantle is solid rock. Lava comes from small pockets "
                    "of melted rock, not from a liquid layer."},
            {"text": "The inner core, because it is the hottest part",
             "correct": False,
             "why": "It is the hottest part of the planet and it is solid. "
                    "The pressure at the centre keeps it that way."},
            {"text": "The outer core, which is molten iron and nickel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e03",
        "band": "easier",
        "text": "What is the mantle made of?",
        "options": [
            {"text": "Rock containing silicon, oxygen, iron and magnesium",
             "correct": True},
            {"text": "Iron and nickel, the same as the two core layers",
             "correct": False,
             "why": "That is the core. The mantle is rock, not metal."},
            {"text": "Melted rock, which volcanoes bring to the surface",
             "correct": False,
             "why": "The mantle is solid rock. Only small pockets of it are "
                    "melted at any one time."},
            {"text": "Water and gas trapped underneath the solid crust",
             "correct": False,
             "why": "There is no such layer. Below the crust is 2865 km of "
                    "solid rock."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e04",
        "band": "easier",
        "text": "What is a seismic wave?",
        "options": [
            {"text": "A wave that travels round the surface of the sea",
             "correct": False,
             "why": "That is a water wave. Seismic waves travel through rock "
                    "and metal."},
            {"text": "A current of hot rock creeping through the mantle",
             "correct": False,
             "why": "That is a convection current. It carries matter along "
                    "rather than passing through it."},
            {"text": "A wave sent through the Earth by an earthquake",
             "correct": True},
            {"text": "A radio pulse sent down a borehole to listen with",
             "correct": False,
             "why": "Nothing is sent down. The wave starts at an earthquake "
                    "and is recorded at the surface."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-01-s01",
        "band": "standard",
        "text": "Why can the mantle be described as solid when it also "
                "flows?",
        "options": [
            {"text": "Because it is solid at the top and liquid further "
                     "down",
             "correct": False,
             "why": "It is solid all the way through. What changes with "
                    "depth is temperature and pressure, not the state."},
            {"text": "Because it is a liquid that has been squeezed until "
                     "it set",
             "correct": False,
             "why": "It was never a liquid that set. It is rock, and at "
                    "these pressures it stays solid."},
            {"text": "Because only the parts near a volcano are truly "
                     "solid",
             "correct": False,
             "why": "It is the other way round. Melting happens in pockets, "
                    "usually near the top of the mantle."},
            {"text": "Because hot solid rock under pressure can creep very "
                     "slowly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s02",
        "band": "standard",
        "text": "One type of earthquake wave stops dead at a depth of "
                "2900 km and never gets any further. What is the best "
                "explanation?",
        "options": [
            {"text": "A liquid layer starts there, and that wave cannot "
                     "cross liquid",
             "correct": True},
            {"text": "The wave has run out of energy after travelling that "
                     "far",
             "correct": False,
             "why": "Other waves from the same earthquake carry on well past "
                    "2900 km and arrive on the far side."},
            {"text": "The rock at that depth is too hot for any wave to "
                     "cross",
             "correct": False,
             "why": "Waves cross the mantle at 4000 °C. Temperature is not "
                    "what stops them."},
            {"text": "There is nothing below that depth for the wave to "
                     "travel through",
             "correct": False,
             "why": "There are 3471 km of core below it, and other waves do "
                    "cross it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s03",
        "band": "standard",
        "text": "The Earth as a whole is about twice as dense as the rock "
                "at its surface. What does that tell you?",
        "options": [
            {"text": "The surface rocks are unusually light for ordinary "
                     "rock",
             "correct": False,
             "why": "Surface rock is ordinary rock. The difference comes "
                    "from what is underneath it."},
            {"text": "The Earth must be hollow somewhere near the middle",
             "correct": False,
             "why": "A hollow would make the average density lower, not "
                    "higher."},
            {"text": "The material deep inside must be far denser than "
                     "rock",
             "correct": True},
            {"text": "The rock is squashed into a smaller space as you go "
                     "deeper",
             "correct": False,
             "why": "Squeezing does raise the density a little, but nowhere "
                    "near enough. The inside is a different material."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s04",
        "band": "standard",
        "text": "Why does the deepest borehole ever drilled tell us almost "
                "nothing about the mantle?",
        "options": [
            {"text": "It was drilled through ocean floor instead of "
                     "continent",
             "correct": False,
             "why": "It was drilled on land. Where it was drilled is not the "
                    "problem; how far it got is."},
            {"text": "It reached only about a third of the way through the "
                     "crust",
             "correct": True},
            {"text": "Its rock samples were destroyed before anyone could "
                     "study them",
             "correct": False,
             "why": "The samples were studied in detail. The trouble is that "
                    "every one of them is crust."},
            {"text": "It measured temperature but brought no rock to the "
                     "surface",
             "correct": False,
             "why": "Rock was brought up from it. It is still crust, from "
                    "12 km down."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-01-h01",
        "band": "harder",
        "text": "A student says there must be a huge bar magnet inside the "
                "Earth, because a compass works anywhere on the surface. "
                "Why can that not be right?",
        "options": [
            {"text": "Iron loses its magnetism far below core temperatures, "
                     "so a permanent magnet could not survive down there",
             "correct": True},
            {"text": "A magnet that size would pull every iron object on "
                     "the surface of the planet straight downwards",
             "correct": False,
             "why": "The field at the surface is very weak. Its strength is "
                    "not what rules a permanent magnet out; the temperature "
                    "is."},
            {"text": "The magnetic poles would then have to sit exactly on "
                     "the geographic poles, and they do not",
             "correct": False,
             "why": "A permanent magnet could be tilted just as easily. Heat "
                    "is the reason, not the angle."},
            {"text": "A magnet cannot work through 6371 kilometres of solid "
                     "rock and liquid metal in the way",
             "correct": False,
             "why": "Magnetic fields pass through rock perfectly well. The "
                    "problem is that iron that hot is not magnetic."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h02",
        "band": "harder",
        "text": "The mantle above it is solid and the inner core below it "
                "is solid. How is the outer core known to be liquid?",
        "options": [
            {"text": "It is the hottest layer in the Earth, so it is the "
                     "one that melts",
             "correct": False,
             "why": "The inner core is hotter still and is solid. "
                    "Temperature on its own does not decide the state."},
            {"text": "It is made of metal, and metal melts more easily than "
                     "rock does",
             "correct": False,
             "why": "The inner core is the same metal and is solid. The "
                    "pressure is what differs between them."},
            {"text": "One type of earthquake wave stops dead at its top and "
                     "never crosses it",
             "correct": True},
            {"text": "Molten metal from it has been brought up by the "
                     "deepest volcanoes",
             "correct": False,
             "why": "No volcano reaches anywhere near 2900 km. Lava comes "
                    "from the top of the mantle."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h03",
        "band": "harder",
        "text": "Volcanoes bring molten rock to the surface. Why is that "
                "not evidence that the mantle is a liquid layer?",
        "options": [
            {"text": "Molten rock does not come from the mantle at all, but "
                     "from inside the crust",
             "correct": False,
             "why": "Most of it does form in the top of the mantle. The "
                    "point is that the melting is local."},
            {"text": "Melting happens only in small pockets, where the "
                     "pressure drops enough",
             "correct": True},
            {"text": "Volcanoes are fed by seawater that has been heated "
                     "under the ocean floor",
             "correct": False,
             "why": "Water changes how rock melts, but what erupts is melted "
                    "rock, not heated water."},
            {"text": "The lava is made inside the volcano itself as the rock "
                     "is squeezed together",
             "correct": False,
             "why": "Squeezing hot rock keeps it solid. It is a DROP in "
                    "pressure that lets it melt."},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h04",
        "band": "harder",
        "text": "Imagine a planet the same size as the Earth, made of the "
                "same materials, but whose core has frozen solid all the "
                "way through. Which observation would be different?",
        "options": [
            {"text": "Earthquake waves would no longer cross the planet at "
                     "all",
             "correct": False,
             "why": "They would cross it better, not worse. Solid material "
                    "carries every type of wave."},
            {"text": "The planet would be noticeably less dense than the "
                     "Earth",
             "correct": False,
             "why": "Solid iron is slightly denser than liquid iron, so the "
                    "density would barely move."},
            {"text": "The surface would be far too cold for rock ever to "
                     "melt",
             "correct": False,
             "why": "A frozen core says nothing about the temperature at the "
                    "surface."},
            {"text": "There would be no magnetic field, because no liquid "
                     "metal is moving",
             "correct": True},
        ],
        "figure": None,
    },
]
