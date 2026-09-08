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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-01-e05",
        "band": "easier",
        "text": "What is density?",
        "options": [
            {"text": "How much mass a material has for its size",
             "correct": True},
            {"text": "How hard a material is to break apart, measured by "
                     "pressing on a sample of it until it finally gives way "
                     "under the load",
             "correct": False,
             "why": "That is strength. Density is mass compared with volume"},
            {"text": "How hot a material is, and how quickly it warms up in "
                     "sunlight",
             "correct": False,
             "why": "Temperature is a separate property. A hot rock and a "
                    "cold one have almost the same density"},
            {"text": "How deep a layer is",
             "correct": False,
             "why": "Depth is a distance. Density is about the material "
                    "itself"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e06",
        "band": "easier",
        "text": "Which of the Earth's four layers is by far the THINNEST?",
        "options": [
            {"text": "The mantle",
             "correct": False,
             "why": "The mantle is the thickest layer of the four, running "
                    "most of the way to the core"},
            {"text": "The crust",
             "correct": True},
            {"text": "The outer core",
             "correct": False,
             "why": "It is over two thousand kilometres thick — hundreds of "
                    "times the crust"},
            {"text": "The inner core, which is the smallest of the four "
                     "because it sits right at the middle where there is "
                     "least room for anything to fit",
             "correct": False,
             "why": "It is a ball over a thousand kilometres across. The "
                    "crust is a skin a few tens of kilometres thick"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e07",
        "band": "easier",
        "text": "What is the inner core made of, and what state is it in?",
        "options": [
            {"text": "Iron and nickel, and liquid, since it is the hottest "
                     "part of the whole planet and nothing that hot could "
                     "still be holding together as a solid",
             "correct": False,
             "why": "It is the hottest part and it is solid, because the "
                    "pressure at the centre will not let the atoms move "
                    "apart"},
            {"text": "Rock, and solid",
             "correct": False,
             "why": "Rock is the mantle and the crust. The core is metal"},
            {"text": "Iron and nickel, and solid",
             "correct": True},
            {"text": "Rock, and molten, like the lava that reaches the surface",
             "correct": False,
             "why": "Neither half is right. The core is iron and nickel, and "
                    "the inner part is solid"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e08",
        "band": "easier",
        "text": "Which layer is solid rock that flows very slowly?",
        "options": [
            {"text": "The crust, which is carried about on the surface and "
                     "must therefore be the layer that is doing the moving",
             "correct": False,
             "why": "The crust is carried BY something. What creeps "
                    "underneath it is the mantle"},
            {"text": "The outer core",
             "correct": False,
             "why": "That is a genuine liquid — molten iron — rather than a "
                    "solid that creeps"},
            {"text": "The inner core",
             "correct": False,
             "why": "Solid, and not flowing at all. The pressure holds it "
                    "rigid"},
            {"text": "The mantle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e09",
        "band": "easier",
        "text": "How is the structure of the Earth's inside known?",
        "options": [
            {"text": "From the way earthquake waves travel through the "
                     "planet",
             "correct": True},
            {"text": "From samples brought up by the deepest boreholes ever "
                     "drilled, which have now reached down as far as the top "
                     "of the mantle",
             "correct": False,
             "why": "The deepest hole reached about a third of the way "
                    "through the crust. Nothing has sampled the mantle"},
            {"text": "From what comes out of volcanoes when they erupt, "
                     "sampled at the surface",
             "correct": False,
             "why": "Volcanoes bring up material from small pockets near the "
                    "top of the mantle. They say nothing about the core"},
            {"text": "It is a guess",
             "correct": False,
             "why": "It rests on measurement — waves recorded at stations all "
                    "over the world"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-01-s05",
        "band": "standard",
        "text": "Why does the Earth have a magnetic field at all?",
        "options": [
            {"text": "Because liquid metal is moving in the outer core, and "
                     "moving metal carries electric currents",
             "correct": True},
            {"text": "Because there is a very large permanent magnet at the "
                     "centre of the planet, made of the iron that sank there "
                     "while the Earth was forming",
             "correct": False,
             "why": "Iron loses its magnetism long before core temperatures. "
                    "No permanent magnet could survive down there"},
            {"text": "Because the Earth spins",
             "correct": False,
             "why": "Spinning helps stir the core and is not enough on its "
                    "own. Venus spins and has no field"},
            {"text": "Because the Sun magnetises the planet, in the same way "
                     "that stroking a nail with a magnet magnetises the nail",
             "correct": False,
             "why": "The Sun's particles are DEFLECTED by the field rather "
                    "than causing it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s06",
        "band": "standard",
        "text": "A student pictures the mantle as a sea of molten lava under "
                "the crust. What is the correction?",
        "options": [
            {"text": "It is molten near the top and solid further down, which "
                     "is why volcanoes can reach the melted part and "
                     "earthquake waves can cross the solid part below it",
             "correct": False,
             "why": "It is solid essentially throughout. The pockets that "
                    "melt are local and small"},
            {"text": "It is solid rock that creeps, and melting happens only "
                     "in small pockets",
             "correct": True},
            {"text": "It is liquid iron rather than liquid rock, which is why "
                     "a compass needle lines up with it",
             "correct": False,
             "why": "That describes the outer core. The mantle is rock"},
            {"text": "Nothing — the picture is right",
             "correct": False,
             "why": "Earthquake waves cross the mantle in a way that only a "
                    "solid allows"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s07",
        "band": "standard",
        "text": "The crust is under one per cent of the way to the centre. "
                "What does that mean in practice?",
        "options": [
            {"text": "The crust holds under one per cent of the Earth's "
                     "material, so almost none of the planet's mass is in the "
                     "part that anybody has ever been able to reach",
             "correct": False,
             "why": "True about the mass, and the phrase is about DEPTH. It "
                    "is a statement about how far down anyone has got"},
            {"text": "The crust is unimportant",
             "correct": False,
             "why": "Everything alive and everything ever mined is in it. "
                    "Thin is not unimportant"},
            {"text": "Everything anyone has ever dug, mined or drilled has "
                     "stayed in a very thin skin",
             "correct": True},
            {"text": "The crust is thinner than the atmosphere, so there is "
                     "more air above us than there is rock below",
             "correct": False,
             "why": "The crust is tens of kilometres thick and most of the "
                    "atmosphere is in the first ten"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s08",
        "band": "standard",
        "text": "Which TWO layers are made of iron and nickel?",
        "options": [
            {"text": "The crust and the mantle, which are the two rocky "
                     "layers and hold most of the iron that has ever been "
                     "mined anywhere in the world",
             "correct": False,
             "why": "Mined iron comes from the crust, and the crust and "
                    "mantle are rock. The metal layers are the two cores"},
            {"text": "The mantle and the outer core",
             "correct": False,
             "why": "The mantle is rock. Only the two core layers are metal"},
            {"text": "The crust and the inner core",
             "correct": False,
             "why": "The crust is rock, and the two metal layers are next to "
                    "each other at the centre"},
            {"text": "The outer core and the inner core",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s09",
        "band": "standard",
        "text": "Earthquake waves are recorded at stations all over the "
                "world. Why does having MANY stations matter?",
        "options": [
            {"text": "Because where a wave arrives and where it fails to "
                     "arrive is what maps the inside",
             "correct": True},
            {"text": "Because a single station could miss an earthquake "
                     "altogether, and having many of them means no event "
                     "anywhere in the world goes unrecorded",
             "correct": False,
             "why": "Catching every event matters and is not the point here. "
                    "The pattern of where waves DO NOT arrive is the "
                    "evidence"},
            {"text": "Because any one station's instrument might be faulty, "
                     "and a second reading is needed to check it",
             "correct": False,
             "why": "Checking instruments is good practice. The layers are "
                    "found from the geography of the arrivals"},
            {"text": "Because earthquakes are rare",
             "correct": False,
             "why": "They are recorded constantly. The number of stations is "
                    "about coverage rather than frequency"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-01-h05",
        "band": "harder",
        "text": "The inner core is growing a little every year. Where does "
                "the added material come from?",
        "options": [
            {"text": "From the outer core, which freezes onto it",
             "correct": True},
            {"text": "From the mantle above, which sinks through the liquid "
                     "outer core and settles at the centre because rock is "
                     "denser than molten iron",
             "correct": False,
             "why": "Iron is far denser than rock, so rock does not sink "
                    "through it. The growth is the liquid iron freezing"},
            {"text": "From iron falling in from space",
             "correct": False,
             "why": "Meteorites land on the surface. Nothing reaches the "
                    "core"},
            {"text": "It does not grow — it is the same size as when the "
                     "Earth formed",
             "correct": False,
             "why": "It has been growing as the planet slowly cools, and the "
                    "energy released helps drive the field"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h06",
        "band": "harder",
        "text": "Why does the inner core's growth matter for anything at the "
                "surface?",
        "options": [
            {"text": "Because the planet gets slightly denser each year as "
                     "liquid becomes solid, and that gradual change alters "
                     "the strength of gravity at the surface over time",
             "correct": False,
             "why": "Freezing rearranges material without adding any. The "
                    "mass and the gravity are unchanged"},
            {"text": "Because the energy released as it freezes helps drive "
                     "the currents that make the magnetic field",
             "correct": True},
            {"text": "Because it makes the Earth spin faster, in the same way "
                     "that a spinning skater speeds up by pulling their arms "
                     "in",
             "correct": False,
             "why": "Nothing at the surface would notice. What matters is the "
                    "energy driving the core's currents"},
            {"text": "It does not matter at all",
             "correct": False,
             "why": "The magnetic field it helps sustain is what deflects the "
                    "solar wind and keeps the atmosphere"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h07",
        "band": "harder",
        "text": "A student says the Earth's interior is only a guess, because "
                "nobody has ever been there. What is the best reply?",
        "options": [
            {"text": "It IS a guess for now, and it will stay one until "
                     "somebody manages to drill deep enough to bring a sample "
                     "of the mantle back to the surface",
             "correct": False,
             "why": "The evidence is already strong, and a great deal of "
                    "established science rests on things nobody has "
                    "visited"},
            {"text": "Volcanoes have brought up samples of the core, so the "
                     "deepest layers have been examined in a laboratory",
             "correct": False,
             "why": "They bring up material from near the top of the mantle. "
                    "Nothing from the core reaches the surface"},
            {"text": "The layers were found by measurement and inference, "
                     "which is how most of science works",
             "correct": True},
            {"text": "Boreholes have reached the mantle",
             "correct": False,
             "why": "The deepest reached about a third of the way through the "
                    "crust"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h08",
        "band": "harder",
        "text": "Suppose the whole core were solid. What would the earthquake "
                "records look like?",
        "options": [
            {"text": "No waves would reach the far side of the planet at all, "
                     "because a solid core would absorb everything that "
                     "entered it rather than letting it pass",
             "correct": False,
             "why": "A solid carries BOTH kinds of wave. Solid material is "
                    "what lets that wave through"},
            {"text": "Nothing would change",
             "correct": False,
             "why": "Then the liquid layer could never have been detected, "
                    "and it was"},
            {"text": "The waves would arrive sooner everywhere, because waves "
                     "travel faster through a solid",
             "correct": False,
             "why": "Speeds would shift a little, and the decisive change is "
                    "that a wave which currently vanishes would not"},
            {"text": "The wave that stops at 2900 km would carry straight on "
                     "through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h09",
        "band": "harder",
        "text": "The Earth formed about 4.5 billion years ago. Why is it "
                "still hot inside?",
        "options": [
            {"text": "Heat left over from its formation, plus heat still "
                     "being released by radioactive decay in the rocks",
             "correct": True},
            {"text": "The Sun heats the ground, and over billions of years "
                     "that heat has worked its way down through the crust to "
                     "the layers below it",
             "correct": False,
             "why": "The Sun warms about a metre of soil. Nothing solar "
                    "reaches any depth that matters"},
            {"text": "Friction from the planet spinning",
             "correct": False,
             "why": "The spin is smooth and generates almost nothing. The "
                    "heat is left over and radioactive"},
            {"text": "The pressure at the centre creates heat continuously, in "
                     "the way a bicycle pump warms up as the air inside it is "
                     "squeezed",
             "correct": False,
             "why": "Pressure keeps the inner core solid and does not go on "
                    "making new heat"},
        ],
        "figure": None,
    },
]
