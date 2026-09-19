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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-01-e10",
        "band": "easier",
        "text": "What is the rock of the crust mostly made of?",
        "options": [
            {"text": "Compounds of silicon and oxygen",
             "correct": True},
            {"text": "Iron and nickel, the same two metals as the core",
             "correct": False,
             "why": "Those two are the core. The crust is rock"},
            {"text": "Carbon, in the form of coal, oil and limestone",
             "correct": False,
             "why": "Those are found IN the crust in small quantities. The "
                    "rock itself is silicon and oxygen compounds"},
            {"text": "Melted rock that has not finished cooling yet",
             "correct": False,
             "why": "The crust is solid rock all the way through, and has "
                    "been for billions of years"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e11",
        "band": "easier",
        "text": "Why was the deepest borehole ever drilled abandoned?",
        "options": [
            {"text": "The money ran out before the drill reached the mantle",
             "correct": False,
             "why": "What defeated it was the rock, not the budget, and the "
                    "mantle was never within reach"},
            {"text": "The drill reached the top of the outer core, and no "
                     "drill can cut through liquid metal",
             "correct": False,
             "why": "The outer core is 2900 km down. The hole stopped at "
                    "about 12 km"},
            {"text": "The rock at the bottom was hot enough to behave like "
                     "plastic, and it kept closing the hole",
             "correct": True},
            {"text": "Lava rose up the hole from the mantle and filled it",
             "correct": False,
             "why": "No melted rock reached it. Hot solid rock creeping "
                    "inwards is what closed it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e12",
        "band": "easier",
        "text": "Which of the four layers is the thickest?",
        "options": [
            {"text": "The crust",
             "correct": False,
             "why": "It is the thinnest of the four by an enormous margin"},
            {"text": "The outer core",
             "correct": False,
             "why": "Over two thousand kilometres thick, and still not the "
                    "thickest"},
            {"text": "The inner core",
             "correct": False,
             "why": "It is the smallest of the four"},
            {"text": "The mantle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e13",
        "band": "easier",
        "text": "What does a seismometer do?",
        "options": [
            {"text": "Records earthquake waves as they arrive",
             "correct": True},
            {"text": "Drills deep into rock and brings samples up",
             "correct": False,
             "why": "That is a drilling rig, and the deepest one managed 12 "
                    "km"},
            {"text": "Measures how hot the rock is at the bottom of a "
                     "borehole",
             "correct": False,
             "why": "Temperature probes do that. A seismometer listens for "
                    "waves"},
            {"text": "Sends a pulse down into the ground and waits for the "
                     "echo",
             "correct": False,
             "why": "Nothing is sent down. The wave starts at an earthquake "
                    "somewhere else in the world"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e14",
        "band": "easier",
        "text": "What keeps the inner core solid?",
        "options": [
            {"text": "Its temperature, which is lower than the outer core's",
             "correct": False,
             "why": "It is hotter than the outer core, not cooler"},
            {"text": "The pressure at the centre of the Earth",
             "correct": True},
            {"text": "The rock around it, which shields it from the heat",
             "correct": False,
             "why": "The layer around it is molten metal, and it is cooler "
                    "than the inner core is"},
            {"text": "The metal it is made of, which has a far higher "
                     "melting point",
             "correct": False,
             "why": "It is the same iron and nickel as the liquid layer "
                    "above it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e15",
        "band": "easier",
        "text": "Roughly how fast do the plates of the crust move?",
        "options": [
            {"text": "A few metres a year",
             "correct": False,
             "why": "That is about a hundred times too fast to match what is "
                    "measured"},
            {"text": "A few kilometres a year",
             "correct": False,
             "why": "Continents would cross an ocean in a human lifetime at "
                    "that speed"},
            {"text": "A few centimetres a year",
             "correct": True},
            {"text": "They do not move",
             "correct": False,
             "why": "Their movement is measured directly by satellite every "
                    "year"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e16",
        "band": "easier",
        "text": "What is magma?",
        "options": [
            {"text": "The whole of the mantle, which is a layer of liquid "
                     "rock",
             "correct": False,
             "why": "The mantle is solid rock. Melting happens in small "
                    "pockets within it"},
            {"text": "Liquid metal from the outer core, carried up by "
                     "volcanoes",
             "correct": False,
             "why": "No volcano reaches the core. What erupts is melted "
                    "rock"},
            {"text": "Rock squeezed so hard that it has been forced to turn "
                     "liquid",
             "correct": False,
             "why": "Squeezing hot rock keeps it solid. Melting follows a "
                    "DROP in pressure"},
            {"text": "Melted rock, formed in pockets near the top of the "
                     "mantle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e17",
        "band": "easier",
        "text": "What happens to a piece of iron's magnetism if it is heated "
                "strongly enough?",
        "options": [
            {"text": "It loses it",
             "correct": True},
            {"text": "It gets stronger",
             "correct": False,
             "why": "Heat destroys magnetism rather than building it"},
            {"text": "It stays exactly the same at any temperature at all",
             "correct": False,
             "why": "Above about 770 °C iron is not magnetic any more"},
            {"text": "It reverses, so that the two poles swap over",
             "correct": False,
             "why": "Heating does not flip a magnet round. It removes the "
                    "magnetism altogether"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e18",
        "band": "easier",
        "text": "What does the Earth's magnetic field do for the planet?",
        "options": [
            {"text": "It holds the atmosphere down by attracting the gases in "
                     "it, which would otherwise drift off into space",
             "correct": False,
             "why": "Gravity holds the atmosphere down. Air is not magnetic"},
            {"text": "It keeps the surface warm by soaking up sunlight",
             "correct": False,
             "why": "The field does nothing to the temperature"},
            {"text": "It stops the plates at the surface from moving about",
             "correct": False,
             "why": "The plates are dragged by currents in the mantle, which "
                    "magnetism has no part in"},
            {"text": "It deflects the stream of particles from the Sun, "
                     "which would otherwise strip the atmosphere away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e19",
        "band": "easier",
        "text": "The mantle is often described as creeping. What does that "
                "mean?",
        "options": [
            {"text": "It flows extremely slowly while staying solid",
             "correct": True},
            {"text": "It melts a little at a time and runs downhill",
             "correct": False,
             "why": "Nothing runs anywhere. It is solid rock throughout"},
            {"text": "It cracks and slides in sudden jumps",
             "correct": False,
             "why": "That describes an earthquake in the crust above it"},
            {"text": "It grows outwards as new rock is added",
             "correct": False,
             "why": "No new rock is made. The same rock changes shape"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e20",
        "band": "easier",
        "text": "Which pair of metals is the core made of?",
        "options": [
            {"text": "Iron and copper",
             "correct": False,
             "why": "Copper plays no part in it. The second metal is nickel"},
            {"text": "Iron and nickel",
             "correct": True},
            {"text": "Lead and iron",
             "correct": False,
             "why": "Lead is far too rare to build a core out of"},
            {"text": "Silicon and magnesium",
             "correct": False,
             "why": "Those two are in the rock of the mantle above the core"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e21",
        "band": "easier",
        "text": "Roughly how hot is the inner core?",
        "options": [
            {"text": "About 100 °C, the temperature water boils at",
             "correct": False,
             "why": "Even the base of the crust is hotter than that"},
            {"text": "About 550 °C, roughly the inside of a pizza oven",
             "correct": False,
             "why": "That is mantle temperature nearer the top, not the "
                    "centre"},
            {"text": "About 55 000 °C, hotter than the inside of any star",
             "correct": False,
             "why": "Ten times too hot. Nothing in the Earth comes close to "
                    "a stellar interior"},
            {"text": "About 5500 °C, close to the temperature of the Sun's "
                     "surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e22",
        "band": "easier",
        "text": "How does the thickness of the crust under an ocean compare "
                "with the thickness under a mountain range?",
        "options": [
            {"text": "Thinner under the ocean and thicker under the "
                     "mountains",
             "correct": True},
            {"text": "Thicker under the ocean and thinner under the "
                     "mountains",
             "correct": False,
             "why": "It is the other way round. Mountains have deep roots of "
                    "crust beneath them"},
            {"text": "Exactly the same, which is why it is called a shell",
             "correct": False,
             "why": "Its thickness varies by tens of kilometres from place "
                    "to place"},
            {"text": "Missing under the ocean, where the mantle is exposed",
             "correct": False,
             "why": "There is crust beneath every ocean. It is simply "
                    "thinner there"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e23",
        "band": "easier",
        "text": "The deepest borehole reached about 12 km and the centre of "
                "the Earth is 6371 km down. Roughly what fraction of the way "
                "is that?",
        "options": [
            {"text": "About two tenths of one per cent",
             "correct": True},
            {"text": "About two per cent",
             "correct": False,
             "why": "Ten times too big. Two per cent of 6371 km would be "
                    "over 100 km"},
            {"text": "About a fifth of the way",
             "correct": False,
             "why": "A fifth would be 1274 km, which is a hundred times "
                    "deeper than any hole"},
            {"text": "About half way",
             "correct": False,
             "why": "Half way is over three thousand kilometres down, inside "
                    "the mantle"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e24",
        "band": "easier",
        "text": "Which layer sits directly below the crust?",
        "options": [
            {"text": "The outer core",
             "correct": False,
             "why": "That lies below the mantle, 2900 km down"},
            {"text": "The inner core",
             "correct": False,
             "why": "That is at the very centre, with two layers between it "
                    "and the crust"},
            {"text": "The mantle",
             "correct": True},
            {"text": "A layer of magma",
             "correct": False,
             "why": "There is no such layer. Melting happens only in "
                    "pockets"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e25",
        "band": "easier",
        "text": "Where does the lava that a volcano erupts come from?",
        "options": [
            {"text": "The outer core, 2900 km below the surface",
             "correct": False,
             "why": "No volcano reaches anywhere near that depth"},
            {"text": "Pockets of melted rock near the top of the mantle",
             "correct": True},
            {"text": "A liquid layer that lies just underneath the crust",
             "correct": False,
             "why": "There is no such layer. Below the crust is solid rock"},
            {"text": "The inner core, which is the hottest part of the "
                     "planet",
             "correct": False,
             "why": "It is solid, and nothing from it ever reaches the "
                    "surface"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e26",
        "band": "easier",
        "text": "What is a plate, in the sense used when the crust is "
                "described?",
        "options": [
            {"text": "A slab of liquid rock resting on top of the mantle",
             "correct": False,
             "why": "Nothing is liquid there. The plates are solid rock on "
                    "solid rock"},
            {"text": "A layer of the mantle that has broken away from the "
                     "rest",
             "correct": False,
             "why": "The plates are pieces of crust, not pieces of mantle"},
            {"text": "A continent, and nothing but a continent",
             "correct": False,
             "why": "Plates carry ocean floor as well as continents"},
            {"text": "A piece of the cracked crust, carried slowly over the "
                     "mantle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e27",
        "band": "easier",
        "text": "In the structure of the Earth, what does the word CORE "
                "name?",
        "options": [
            {"text": "The iron and nickel centre of the Earth, in two "
                     "parts",
             "correct": True},
            {"text": "The layer of rock that lies just below the crust",
             "correct": False,
             "why": "That is the mantle, and it is rock rather than metal"},
            {"text": "The deepest part of the crust, at the base of a "
                     "mountain",
             "correct": False,
             "why": "Crust is crust however deep it goes. The core is two "
                    "layers further in"},
            {"text": "Any part of the Earth that is hot enough to melt",
             "correct": False,
             "why": "The core is a place, not a temperature, and half of it "
                    "is solid"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e28",
        "band": "easier",
        "text": "What happens to the temperature as you go deeper into the "
                "Earth?",
        "options": [
            {"text": "It falls, because the Sun cannot reach down there",
             "correct": False,
             "why": "The heat comes from inside, so depth makes it hotter "
                    "rather than colder"},
            {"text": "It rises",
             "correct": True},
            {"text": "It stays the same all the way to the centre",
             "correct": False,
             "why": "The crust reaches about 400 °C and the centre about "
                    "5500 °C"},
            {"text": "It rises to the base of the crust and then levels off",
             "correct": False,
             "why": "It goes on rising through the mantle and both parts of "
                    "the core"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e29",
        "band": "easier",
        "text": "What does MOLTEN mean?",
        "options": [
            {"text": "Melted, so that the material is now a liquid",
             "correct": True},
            {"text": "Extremely hot, whatever state the material is in",
             "correct": False,
             "why": "The inner core is extremely hot and is not molten. The "
                    "word is about the state"},
            {"text": "Made of metal rather than of rock",
             "correct": False,
             "why": "Rock can be molten too, and that is what lava is"},
            {"text": "Squeezed until the material has become solid",
             "correct": False,
             "why": "That is the opposite of melting"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-e30",
        "band": "easier",
        "text": "What is meant by a BOUNDARY between two of the Earth's "
                "layers?",
        "options": [
            {"text": "A wall of harder rock separating one layer from the "
                     "next",
             "correct": False,
             "why": "Nothing is built there. It is simply where one material "
                    "gives way to another"},
            {"text": "The gap left between two layers that do not quite "
                     "touch",
             "correct": False,
             "why": "There are no gaps inside the Earth. The layers are in "
                    "contact"},
            {"text": "The depth at which the material changes from one to "
                     "another",
             "correct": True},
            {"text": "The point at which the rock stops being hot",
             "correct": False,
             "why": "Temperature rises steadily with depth and does not stop "
                    "at any boundary"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c10-01-s10",
        "band": "standard",
        "text": "A scale drawing of the Earth's four layers has to exaggerate "
                "the crust. Why?",
        "options": [
            {"text": "Because its true share of the distance is too small to "
                     "draw or to tap",
             "correct": True},
            {"text": "Because the crust is the layer that matters most to "
                     "people",
             "correct": False,
             "why": "Importance is not a reason to distort a scale. The "
                    "reason is that a true crust would be a hairline"},
            {"text": "Because nobody knows how thick the crust really is",
             "correct": False,
             "why": "Its thickness is known well from earthquake waves, and "
                    "that is the number being exaggerated"},
            {"text": "Because the crust is thicker than the drawing can "
                     "fit",
             "correct": False,
             "why": "It is the thinnest layer. The problem is the opposite "
                    "one"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s11",
        "band": "standard",
        "text": "A wave that cannot travel through liquids passes right "
                "through the mantle. What does that establish?",
        "options": [
            {"text": "That the mantle is solid",
             "correct": True},
            {"text": "That the mantle is cooler than the crust above it, "
                     "since a cooler layer is the one that stays solid",
             "correct": False,
             "why": "The mantle is far hotter than the crust and is solid "
                    "anyway"},
            {"text": "That the mantle is liquid, because only a liquid lets "
                     "a wave through without slowing it down",
             "correct": False,
             "why": "It is the exact opposite. That wave is stopped dead by "
                    "liquid"},
            {"text": "That the mantle must be metal",
             "correct": False,
             "why": "The mantle is rock, and rock carries both kinds of wave "
                    "perfectly well"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s12",
        "band": "standard",
        "text": "What makes the plates of the crust move?",
        "options": [
            {"text": "Slow currents of solid rock creeping in the mantle "
                     "beneath them",
             "correct": True},
            {"text": "The pull of the Moon, dragging the plates as it drags "
                     "the tides",
             "correct": False,
             "why": "The Moon raises tides in water. It has no measurable "
                    "grip on the plates"},
            {"text": "The spin of the Earth, flinging the plates outwards as "
                     "it turns",
             "correct": False,
             "why": "The spin is steady and pulls every plate the same way, "
                    "yet plates move in different directions"},
            {"text": "Waves in the liquid outer core, pushing the crust "
                     "directly from below",
             "correct": False,
             "why": "There are 2865 km of mantle between the core and the "
                    "plates"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s13",
        "band": "standard",
        "text": "Something far denser than rock is inside the Earth. What "
                "makes iron the best candidate?",
        "options": [
            {"text": "It is the only dense metal that exists anywhere in the "
                     "universe, so nothing else could possibly be down there",
             "correct": False,
             "why": "Gold, lead and platinum are all denser. Iron wins on "
                    "how common it is"},
            {"text": "It is dense, it is common, and meteorites formed from "
                     "the same material are full of it",
             "correct": True},
            {"text": "It is the only metal that stays liquid at core "
                     "temperatures",
             "correct": False,
             "why": "Most metals would be liquid there, and half the core is "
                    "solid iron"},
            {"text": "It is the metal we mine the most of, so there must be "
                     "most of it",
             "correct": False,
             "why": "What is easy to mine at the surface says nothing about "
                    "6000 km down"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s14",
        "band": "standard",
        "text": "Why is a rock picked up at the surface a poor guide to what "
                "the whole planet is made of?",
        "options": [
            {"text": "Because surface rock is unusual, and most rock is not "
                     "like it",
             "correct": False,
             "why": "Surface rock is perfectly ordinary. The problem is how "
                    "little of the planet it represents"},
            {"text": "Because rock changes its composition on the way up "
                     "from below, so a surface sample is never the rock it "
                     "started as",
             "correct": False,
             "why": "It did not come up from below. It formed where it is"},
            {"text": "Because it comes from a layer that is under one per "
                     "cent of the way to the centre",
             "correct": True},
            {"text": "Because a single sample can never tell you anything "
                     "useful",
             "correct": False,
             "why": "Samples are extremely useful about the crust. They are "
                    "only silent about everything below it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s15",
        "band": "standard",
        "text": "The outer core is liquid metal. Why is being liquid not "
                "enough on its own to explain the magnetic field?",
        "options": [
            {"text": "Because a liquid that is not moving carries no "
                     "current",
             "correct": True},
            {"text": "Because liquid metal is not able to carry an electric "
                     "current at all, however fast it is stirred",
             "correct": False,
             "why": "Molten metal conducts extremely well. Motion is the "
                    "missing ingredient, not conduction"},
            {"text": "Because the field is made in the solid inner core",
             "correct": False,
             "why": "Iron that hot is not magnetic in either part of the "
                    "core"},
            {"text": "Because the liquid has to be cool before it can do "
                     "anything electrical, and the outer core is not",
             "correct": False,
             "why": "Temperature does not stop a metal conducting. What is "
                    "needed is movement"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s16",
        "band": "standard",
        "text": "One type of earthquake wave vanishes at one particular "
                "depth rather than fading away gradually. What does that "
                "tell you about the change at that depth?",
        "options": [
            {"text": "That the wave is simply too weak to be recorded any "
                     "deeper down",
             "correct": False,
             "why": "A weakening wave fades over a range of depths. This one "
                    "stops at a single depth"},
            {"text": "That the material changes sharply there rather than "
                     "gradually",
             "correct": True},
            {"text": "That the rock warms up gradually until the wave can no "
                     "longer cross it",
             "correct": False,
             "why": "A gradual change would give a gradual fade, and "
                    "temperature is not what stops that wave"},
            {"text": "That the instruments recording it lose their accuracy "
                     "at that range",
             "correct": False,
             "why": "The same instruments record other waves arriving from "
                    "deeper still"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s17",
        "band": "standard",
        "text": "A large earthquake happens in Chile. What would you expect "
                "the records from stations on the far side of the world to "
                "show?",
        "options": [
            {"text": "Every station recording both kinds of wave, exactly as "
                     "the nearby stations did",
             "correct": False,
             "why": "If that happened there would be no evidence for a "
                    "liquid layer at all"},
            {"text": "No station anywhere recording anything, because the "
                     "planet is too big to cross",
             "correct": False,
             "why": "Waves cross the whole planet routinely and are recorded "
                    "on the far side"},
            {"text": "A zone where one of the two kinds of wave never "
                     "arrives",
             "correct": True},
            {"text": "Both kinds arriving, but hours later than they do "
                     "nearby",
             "correct": False,
             "why": "The delay is minutes rather than hours, and the "
                    "important thing is which wave is missing"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s18",
        "band": "standard",
        "text": "Earthquake waves change speed as they pass from one layer "
                "into the next. Why?",
        "options": [
            {"text": "Because the material they are travelling through is "
                     "different",
             "correct": True},
            {"text": "Because they have been travelling for longer by the "
                     "time they get there, and a wave slows as it ages",
             "correct": False,
             "why": "Distance does not change a wave's speed. The material "
                    "does"},
            {"text": "Because the boundary reflects part of the wave and the "
                     "remainder is left with half of the energy",
             "correct": False,
             "why": "Some reflection happens, and the speed of what carries "
                    "on is set by the new material"},
            {"text": "Because gravity pulls harder on the wave the closer it "
                     "gets to the centre of the planet",
             "correct": False,
             "why": "Gravity does not accelerate a wave through rock"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s19",
        "band": "standard",
        "text": "The layered Earth is called a MODEL. What does that word "
                "mean here?",
        "options": [
            {"text": "A guess that will do until somebody digs deep enough "
                     "to check it",
             "correct": False,
             "why": "It rests on measurement rather than on guessing, and it "
                    "predicts new observations correctly"},
            {"text": "A small physical copy of the Earth built in a "
                     "laboratory",
             "correct": False,
             "why": "That is one meaning of the word and not this one. Here "
                    "it is an account of the real planet"},
            {"text": "An account built from evidence, which predicts what "
                     "will be measured next",
             "correct": True},
            {"text": "A drawing of the inside of the Earth used for "
                     "teaching",
             "correct": False,
             "why": "The drawing is a picture OF the model. The model is the "
                    "explanation behind it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s20",
        "band": "standard",
        "text": "Why does drilling get harder the deeper the hole goes?",
        "options": [
            {"text": "Because the rock gets hotter and softer, so it flows "
                     "back into the hole",
             "correct": True},
            {"text": "Because the rock gets colder and more brittle, so the "
                     "drill bit shatters against it",
             "correct": False,
             "why": "It gets hotter with depth, not colder"},
            {"text": "Because the air runs out and the machinery below can "
                     "no longer be cooled",
             "correct": False,
             "why": "Air is pumped down. Heat in the rock itself is the "
                    "problem"},
            {"text": "Because the magnetic field grows stronger and pulls "
                     "the steel drill sideways",
             "correct": False,
             "why": "The field is far too weak to move a drill"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s21",
        "band": "standard",
        "text": "Why can you not work out whether a layer is solid or liquid "
                "from its temperature alone?",
        "options": [
            {"text": "Because the pressure matters as well, and pressure "
                     "rises with depth",
             "correct": True},
            {"text": "Because temperature is impossible to measure at any "
                     "depth, so the number is never known",
             "correct": False,
             "why": "Temperatures at depth are estimated well from several "
                    "independent lines of evidence"},
            {"text": "Because every material melts at exactly the same "
                     "temperature, so the number tells you nothing",
             "correct": False,
             "why": "Different materials melt at very different "
                    "temperatures"},
            {"text": "Because a hotter layer is always the more solid of "
                     "two, so the reasoning runs backwards",
             "correct": False,
             "why": "There is no such rule. Pressure is what settles it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s22",
        "band": "standard",
        "text": "How can the average density of the whole Earth be worked "
                "out when nobody can weigh a planet on a balance?",
        "options": [
            {"text": "By drilling a sample from each layer and averaging "
                     "the results",
             "correct": False,
             "why": "Only the crust has ever been sampled, so there is "
                    "nothing to average"},
            {"text": "From its mass and its volume, both of which can be "
                     "measured from outside",
             "correct": True},
            {"text": "By measuring how fast earthquake waves cross it, since "
                     "speed gives density directly",
             "correct": False,
             "why": "Wave speeds help refine the picture and do not on their "
                    "own give the average density"},
            {"text": "It cannot be, which is why the figure is an educated "
                     "guess",
             "correct": False,
             "why": "It is measured to several decimal places"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s23",
        "band": "standard",
        "text": "Why does radioactive decay in the rocks matter for how hot "
                "the Earth still is?",
        "options": [
            {"text": "Because it keeps adding heat, so the planet cools far "
                     "more slowly than leftover heat alone would",
             "correct": True},
            {"text": "Because it is the only source of heat the Earth has "
                     "ever had, all the rest having escaped long ago",
             "correct": False,
             "why": "A great deal of heat is still left over from the "
                    "Earth's formation"},
            {"text": "Because it releases heat only in the core, which is "
                     "why the core is hotter than the mantle",
             "correct": False,
             "why": "The radioactive elements are concentrated in the rocky "
                    "layers, not in the metal core"},
            {"text": "Because it makes the rock radioactive, and radioactive "
                     "rock is hotter than ordinary rock of the same kind",
             "correct": False,
             "why": "Heat comes from the decay itself. Being radioactive is "
                    "not a temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s24",
        "band": "standard",
        "text": "Why are earthquakes useful to scientists who are not "
                "studying earthquakes at all?",
        "options": [
            {"text": "Because the waves they send out have crossed material "
                     "nobody can reach",
             "correct": True},
            {"text": "Because they bring rock up from the mantle each time "
                     "one happens",
             "correct": False,
             "why": "Earthquakes shake rock. They do not deliver samples "
                    "from depth"},
            {"text": "Because they open cracks that boreholes can then "
                     "follow downwards",
             "correct": False,
             "why": "No borehole follows a fault to any useful depth"},
            {"text": "Because the heat they release can be measured at the "
                     "surface",
             "correct": False,
             "why": "What is measured is the arrival of waves, not heat"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s25",
        "band": "standard",
        "text": "Why is the pressure at the centre of the Earth so "
                "enormous?",
        "options": [
            {"text": "Because the whole weight of the planet above is "
                     "pressing inwards on it",
             "correct": True},
            {"text": "Because the material there is the hottest, and heat is "
                     "what creates pressure in a solid",
             "correct": False,
             "why": "Heat alone does not build pressure in a solid. Weight "
                    "does"},
            {"text": "Because the Earth spins, and spinning squeezes "
                     "everything towards the middle",
             "correct": False,
             "why": "Spinning throws material outwards, if anything, rather "
                    "than inwards"},
            {"text": "Because the magnetic field pulls the iron at the "
                     "centre inwards on itself",
             "correct": False,
             "why": "The field is generated by the core rather than "
                    "squeezing it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s26",
        "band": "standard",
        "text": "Explain why the crust is not the same thickness "
                "everywhere.",
        "options": [
            {"text": "Ocean floor carries a thin crust and mountain ranges "
                     "have deep roots of it",
             "correct": True},
            {"text": "The crust has been worn thinner wherever people have "
                     "mined it",
             "correct": False,
             "why": "The deepest mine is a few kilometres into a layer tens "
                    "of kilometres thick"},
            {"text": "The crust is thinner wherever the mantle below it "
                     "happens to be hotter",
             "correct": False,
             "why": "Mantle temperature varies far less than crust thickness "
                    "does"},
            {"text": "The crust is thickest at the poles and thinnest at the "
                     "equator",
             "correct": False,
             "why": "Thickness follows oceans and mountains rather than "
                    "latitude"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s27",
        "band": "standard",
        "text": "The inner core gains a little more solid iron every year. "
                "What does that tell you about the planet as a whole?",
        "options": [
            {"text": "That it is slowly cooling",
             "correct": True},
            {"text": "That it is slowly heating up",
             "correct": False,
             "why": "Freezing is what happens as something cools, which is "
                    "the point"},
            {"text": "That it is gaining mass from space, which settles at "
                     "the centre and adds to the core",
             "correct": False,
             "why": "Nothing from space reaches the core. The iron was "
                    "already there as liquid"},
            {"text": "That it is spinning more slowly than it used to, which "
                     "lets the metal settle out",
             "correct": False,
             "why": "The change of state is about temperature rather than "
                    "spin"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s28",
        "band": "standard",
        "text": "The mantle runs from about 500 °C at the top to about "
                "4000 °C at the bottom. What does that range tell you?",
        "options": [
            {"text": "That the mantle is a mixture of two different "
                     "materials",
             "correct": False,
             "why": "It is one kind of rock throughout. What changes with "
                    "depth is the conditions"},
            {"text": "That the top of the mantle must be liquid and the "
                     "bottom solid",
             "correct": False,
             "why": "The whole mantle is solid, and the cooler part is "
                    "certainly not the melted one"},
            {"text": "That temperature rises steadily with depth inside a "
                     "single layer",
             "correct": True},
            {"text": "That the measurements disagree with one another by "
                     "thousands of degrees",
             "correct": False,
             "why": "They are two ends of one range rather than two rival "
                    "values"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s29",
        "band": "standard",
        "text": "The rock at the bottom of a 12 km borehole was about "
                "180 °C. What does that suggest about the rock much deeper "
                "down?",
        "options": [
            {"text": "That it is hotter still, since the temperature climbs "
                     "with depth",
             "correct": True},
            {"text": "That it is cooler, because 12 km is as warm as the "
                     "Earth ever gets",
             "correct": False,
             "why": "The base of the crust reaches about 400 °C and the "
                    "centre about 5500 °C"},
            {"text": "That it stays at about 180 °C the rest of the way to "
                     "the core",
             "correct": False,
             "why": "The rise continues right through the mantle"},
            {"text": "That it must already be molten a few kilometres "
                     "further down",
             "correct": False,
             "why": "180 °C is nowhere near the melting point of rock, and "
                    "pressure raises that melting point as you go deeper"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-s30",
        "band": "standard",
        "text": "Why is the TIME a wave arrives more useful to a "
                "seismologist than how strong the shaking is?",
        "options": [
            {"text": "Because the time depends on what the wave travelled "
                     "through on the way",
             "correct": True},
            {"text": "Because the strength of the shaking is impossible to "
                     "measure with any instrument",
             "correct": False,
             "why": "It is measured routinely. It simply says more about the "
                    "earthquake than about the planet"},
            {"text": "Because only the arrival time can be recorded at more "
                     "than one station",
             "correct": False,
             "why": "Both are recorded everywhere. The difference is what "
                    "each one is evidence of"},
            {"text": "Because the strength of a wave never changes as it "
                     "crosses the planet",
             "correct": False,
             "why": "It changes a great deal, which is part of why it is a "
                    "less clean measurement"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-01-h10",
        "band": "harder",
        "text": "Mantle rock at 4000 °C is solid, yet lava reaching the "
                "surface is liquid at about 1200 °C. How can the cooler rock "
                "be the melted one?",
        "options": [
            {"text": "Because the mantle rock is a different substance "
                     "entirely, with no melting point of its own",
             "correct": False,
             "why": "It is the same kind of rock. What differs is the "
                    "conditions it sits under"},
            {"text": "Because pressure raises the melting point, and the "
                     "pressure falls as the rock rises",
             "correct": True},
            {"text": "Because the measurement of 4000 °C is an estimate and "
                     "the real mantle is far cooler than that",
             "correct": False,
             "why": "Even the coolest estimates of the deep mantle are "
                    "thousands of degrees above 1200 °C"},
            {"text": "Because lava is heated further by friction on its way "
                     "up through the crust",
             "correct": False,
             "why": "Lava cools on the way up. The melting happened before "
                    "the journey started"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h11",
        "band": "harder",
        "text": "A laboratory squeezes a tiny piece of iron to the pressure "
                "found at the centre of the Earth and heats it. Why is that "
                "worth doing?",
        "options": [
            {"text": "It tests whether iron would still be solid under the "
                     "conditions the model claims are there",
             "correct": True},
            {"text": "It produces a sample of the inner core itself, which "
                     "can then be studied directly in a laboratory",
             "correct": False,
             "why": "Squeezing ordinary iron does not make core material. It "
                    "tests a prediction about it"},
            {"text": "It shows how quickly the inner core is growing each "
                     "year",
             "correct": False,
             "why": "Growth rates come from seismic records, not from a "
                    "pressure cell"},
            {"text": "It measures the temperature at the centre of the "
                     "Earth",
             "correct": False,
             "why": "The temperature has to be set by the experimenter. It "
                    "is an input rather than a result"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h12",
        "band": "harder",
        "text": "Which new observation would do the most damage to the "
                "four-layer model of the Earth?",
        "options": [
            {"text": "A borehole that reached 15 km instead of 12 km and "
                     "found more crust",
             "correct": False,
             "why": "That is exactly what the model predicts, so it would "
                    "support it"},
            {"text": "An earthquake whose waves took slightly longer than "
                     "expected to cross the planet on one occasion",
             "correct": False,
             "why": "Small timing differences refine a model rather than "
                    "breaking it"},
            {"text": "A volcano erupting lava that was hotter than any "
                     "measured before",
             "correct": False,
             "why": "Eruption temperatures vary, and none of them is "
                    "evidence about the core"},
            {"text": "The wave that cannot cross liquid arriving normally "
                     "right across the far side of the planet",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h13",
        "band": "harder",
        "text": "Predict the average density of a planet the same size as "
                "the Earth but made of ordinary rock all the way through.",
        "options": [
            {"text": "Around 2.7 g/cm³, close to the density of surface rock "
                     "itself",
             "correct": True},
            {"text": "Around 5.5 g/cm³, the same as the Earth, because size "
                     "is what sets a planet's density",
             "correct": False,
             "why": "Size does not set density. What a planet is made of "
                    "does"},
            {"text": "Around 11 g/cm³, because the weight of the rock above "
                     "would squeeze the inside to twice the surface value",
             "correct": False,
             "why": "Squeezing raises density a little and nowhere near "
                    "doubles it"},
            {"text": "Around 1.0 g/cm³, the same as water",
             "correct": False,
             "why": "That is the density of water. Rock is nearly three "
                    "times denser"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h14",
        "band": "harder",
        "text": "Stations in a broad band on the far side of the world "
                "record no S-waves from a given earthquake. What can be "
                "worked out from how WIDE that band is?",
        "options": [
            {"text": "How strong the earthquake was",
             "correct": False,
             "why": "A bigger earthquake makes bigger waves everywhere and "
                    "does not move the edge of the band"},
            {"text": "How deep the top of the liquid layer is",
             "correct": True},
            {"text": "How long the earthquake lasted",
             "correct": False,
             "why": "Duration changes the record at every station alike"},
            {"text": "How fast the plates above are moving",
             "correct": False,
             "why": "Plate speeds are measured at the surface and have "
                    "nothing to do with the band"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h15",
        "band": "harder",
        "text": "A student says the currents in the mantle and the currents "
                "in the outer core are the same thing. What is wrong with "
                "that?",
        "options": [
            {"text": "One is solid rock creeping and the other is liquid "
                     "metal moving, and they do different jobs",
             "correct": True},
            {"text": "There are no currents in the mantle, so only the core "
                     "has any",
             "correct": False,
             "why": "Mantle currents are what drag the plates about"},
            {"text": "There are no currents in the outer core, so only the "
                     "mantle has any",
             "correct": False,
             "why": "Moving liquid metal in the outer core is what generates "
                    "the field"},
            {"text": "They are separated by the inner core, which lies "
                     "between the two of them and blocks both",
             "correct": False,
             "why": "The inner core is at the centre, inside both"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h16",
        "band": "harder",
        "text": "A student suggests the outer core is not liquid at all, "
                "just very heavily cracked, and that the cracks are what "
                "stop the wave. Why does that not work?",
        "options": [
            {"text": "Cracked rock is still solid, so the wave would be "
                     "scattered and delayed rather than stopped completely",
             "correct": True},
            {"text": "Cracks cannot form at that depth, because the "
                     "temperature there is far too low for rock to break",
             "correct": False,
             "why": "Low temperature is not the problem at 2900 km, and "
                    "cracking is not what is being ruled out"},
            {"text": "Cracked rock would let no wave of any kind through, so "
                     "nothing would reach the far side at all",
             "correct": False,
             "why": "Waves of both kinds do reach the far side, which is "
                    "another problem for the idea"},
            {"text": "The outer core is made of rock rather than metal, so "
                     "it could not crack in the first place",
             "correct": False,
             "why": "It is metal, and metal can crack. The wave evidence is "
                    "what rules the idea out"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h17",
        "band": "harder",
        "text": "Suppose the Earth's internal heat finally ran out. Name the "
                "surface consequence that would follow.",
        "options": [
            {"text": "The oceans would freeze, because the sea is warmed "
                     "from below by the mantle",
             "correct": False,
             "why": "The Sun warms the oceans. Internal heat contributes "
                    "almost nothing at the surface"},
            {"text": "The atmosphere would be crushed, because the planet "
                     "would shrink as it cooled",
             "correct": False,
             "why": "Cooling changes the volume far too little to do "
                    "anything to the air"},
            {"text": "The plates would stop moving, because the currents "
                     "that drag them would stop",
             "correct": True},
            {"text": "Gravity would weaken, because a cold planet has less "
                     "mass than a hot one",
             "correct": False,
             "why": "Cooling changes no mass at all"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h18",
        "band": "harder",
        "text": "To find the Earth's average density you need its mass. Why "
                "is the volume needed as well?",
        "options": [
            {"text": "Because density compares mass with the space the mass "
                     "occupies",
             "correct": True},
            {"text": "Because the volume tells you how many layers the "
                     "planet must have inside it",
             "correct": False,
             "why": "Volume says nothing about layers. It is half of the "
                    "density calculation"},
            {"text": "Because mass changes with depth and volume does not, "
                     "so one corrects the other",
             "correct": False,
             "why": "Neither changes. They are two fixed properties of the "
                    "whole planet"},
            {"text": "Because the volume is what is measured and the mass is "
                     "worked out from it",
             "correct": False,
             "why": "Both are measured independently, and neither is derived "
                    "from the other"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h19",
        "band": "harder",
        "text": "Two stations sit the same distance from an earthquake, and "
                "the first wave arrives at one of them noticeably earlier "
                "than at the other. What is the best explanation?",
        "options": [
            {"text": "One station is closer to the equator, and waves travel "
                     "faster there",
             "correct": False,
             "why": "Latitude has no effect on how fast a wave crosses "
                    "rock"},
            {"text": "The wave reached one of them before the earthquake had "
                     "started",
             "correct": False,
             "why": "Nothing arrives before it is sent"},
            {"text": "One of the two clocks must be wrong, since equal "
                     "distances always give equal times",
             "correct": False,
             "why": "Equal distances give equal times only if the rock along "
                    "both paths is the same, and it need not be"},
            {"text": "The material along the two paths is different, so the "
                     "wave travelled at different speeds",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h20",
        "band": "harder",
        "text": "Is it fair to say the inside of the Earth was mapped by "
                "sound rather than by digging?",
        "options": [
            {"text": "No, because the layers were found by drilling and the "
                     "waves only confirmed it afterwards",
             "correct": False,
             "why": "No drill has ever left the crust, so drilling found "
                    "none of the layers"},
            {"text": "No, because nothing about the interior has been worked "
                     "out either way",
             "correct": False,
             "why": "The four layers and their states are all established "
                    "from wave evidence"},
            {"text": "Yes, because every boundary was found from waves "
                     "travelling through the planet",
             "correct": True},
            {"text": "Yes, because scientists listen to the noises volcanoes "
                     "make as they erupt",
             "correct": False,
             "why": "Volcano noise says nothing about the core. The waves in "
                    "question come from earthquakes"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h21",
        "band": "harder",
        "text": "Suppose a new survey showed that surface rock averaged "
                "5.5 g/cm³, the same as the whole planet. Which conclusion "
                "would have to be rethought?",
        "options": [
            {"text": "That something much denser than surface rock lies "
                     "inside",
             "correct": True},
            {"text": "That the mantle is solid rather than liquid",
             "correct": False,
             "why": "That rests on wave evidence, which the density survey "
                    "does not touch"},
            {"text": "That the crust is thinner under the oceans",
             "correct": False,
             "why": "Crust thickness is measured from waves and is "
                    "unaffected"},
            {"text": "That the Earth has a magnetic field",
             "correct": False,
             "why": "The field is measured directly with a compass anywhere "
                    "on the surface"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h22",
        "band": "harder",
        "text": "Could a planet whose mantle had stopped creeping still have "
                "a magnetic field?",
        "options": [
            {"text": "No, because the field is made by the mantle's currents "
                     "dragging the crust above them",
             "correct": False,
             "why": "The mantle is rock, and rock currents generate no "
                    "field"},
            {"text": "Yes, as long as its liquid metal core was still "
                     "moving",
             "correct": True},
            {"text": "No, because a still mantle would let the core cool and "
                     "freeze within a few years",
             "correct": False,
             "why": "Cooling a core takes billions of years, not a few"},
            {"text": "Yes, because the field comes from the solid inner core "
                     "acting as a permanent magnet",
             "correct": False,
             "why": "Iron that hot cannot be a permanent magnet in either "
                    "part of the core"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h23",
        "band": "harder",
        "text": "Wave speeds inside the Earth jump suddenly at a few "
                "particular depths instead of drifting steadily. What does "
                "that pattern establish?",
        "options": [
            {"text": "That the interior is a set of layers with sharp "
                     "boundaries between them",
             "correct": True},
            {"text": "That the interior is one material that gets steadily "
                     "denser all the way down",
             "correct": False,
             "why": "One material compressed steadily would give steadily "
                    "changing speeds, with no jumps"},
            {"text": "That the waves lose energy in steps as they travel "
                     "deeper into the planet",
             "correct": False,
             "why": "Energy loss changes how big a wave is rather than how "
                    "fast it goes"},
            {"text": "That the instruments have a limited range and jump "
                     "when they reach the end of it",
             "correct": False,
             "why": "Different instruments in different countries record the "
                    "same jumps at the same depths"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h24",
        "band": "harder",
        "text": "Waves travel faster in the mantle than in the crust. A "
                "student concludes that the mantle must therefore be cooler. "
                "Evaluate that.",
        "options": [
            {"text": "Correct, because a cooler material always carries a "
                     "wave faster than a warm one",
             "correct": False,
             "why": "There is no such rule, and the mantle is far hotter "
                    "than the crust"},
            {"text": "Correct, because the mantle is further from the Sun's "
                     "heat than the crust is",
             "correct": False,
             "why": "The Sun heats about a metre of soil. Depth makes rock "
                    "hotter, not cooler"},
            {"text": "Wrong, because the speed depends on how stiff and how "
                     "dense the material is",
             "correct": True},
            {"text": "Wrong, because waves in fact travel more slowly in the "
                     "mantle than in the crust",
             "correct": False,
             "why": "They travel faster, which is the observation being "
                    "explained"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h25",
        "band": "harder",
        "text": "The layered model said where a wave would fail to arrive "
                "before stations had been built in those places. Why does "
                "that count for more than simply fitting the records already "
                "collected?",
        "options": [
            {"text": "Because a prediction that could have failed and did "
                     "not is stronger evidence",
             "correct": True},
            {"text": "Because older records are always less accurate than "
                     "newer ones",
             "correct": False,
             "why": "Accuracy is not the issue. What matters is that the "
                    "claim was made in advance"},
            {"text": "Because a model has to be published before any data is "
                     "collected to count at all",
             "correct": False,
             "why": "Plenty of good science explains data already in hand. "
                    "A risky prediction simply counts for more"},
            {"text": "Because the new stations were built specifically to "
                     "agree with the model",
             "correct": False,
             "why": "A station records whatever arrives. It cannot be built "
                    "to produce an answer"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h26",
        "band": "harder",
        "text": "Of everything known about the outer core, which fact "
                "matters most for life at the surface, and why?",
        "options": [
            {"text": "Its temperature, because that is what keeps the "
                     "surface of the planet warm enough for liquid water",
             "correct": False,
             "why": "The Sun keeps the surface warm. Core heat barely "
                    "reaches it"},
            {"text": "Its thickness, because a thicker layer means a thicker "
                     "crust above it",
             "correct": False,
             "why": "Crust thickness has no such relationship with the core"},
            {"text": "Its depth, because that is what stops anyone drilling "
                     "into it",
             "correct": False,
             "why": "True, and nothing about life depends on whether we can "
                    "drill there"},
            {"text": "That it is liquid and moving, because that is what "
                     "generates the field protecting the atmosphere",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h27",
        "band": "harder",
        "text": "If the inner core stopped growing, what would you expect to "
                "happen to the magnetic field over a very long time?",
        "options": [
            {"text": "It would weaken, because one of the things driving the "
                     "currents would have stopped",
             "correct": True},
            {"text": "It would strengthen, because a settled core stirs more "
                     "freely than a growing one",
             "correct": False,
             "why": "The energy released by freezing is part of what keeps "
                    "the stirring going"},
            {"text": "It would reverse, so that a compass needle would point "
                     "south instead",
             "correct": False,
             "why": "Reversals happen for other reasons and are not what "
                    "stopping the growth would cause"},
            {"text": "Nothing would change, because the field comes from the "
                     "crust rather than the core",
             "correct": False,
             "why": "The crust generates no field"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h28",
        "band": "harder",
        "text": "One geologist calls the deepest borehole a triumph of "
                "engineering and a disappointment as evidence. Explain that "
                "judgement.",
        "options": [
            {"text": "It went further than anything before it and still "
                     "sampled only the crust",
             "correct": True},
            {"text": "It was easy to drill and the rock it brought up turned "
                     "out to be uninteresting",
             "correct": False,
             "why": "It took about twenty years and defeated its own "
                    "engineers. Easy is the wrong word"},
            {"text": "It reached the mantle and the samples were then lost "
                     "before anyone studied them",
             "correct": False,
             "why": "It never reached the mantle, and its samples were "
                    "studied in detail"},
            {"text": "It proved the layered model wrong and nobody has "
                     "replaced the model since",
             "correct": False,
             "why": "It found ordinary crust, exactly as the model expects"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h29",
        "band": "harder",
        "text": "Why does the accepted model of the Earth have four layers "
                "rather than forty?",
        "options": [
            {"text": "Because four is the largest number of layers a diagram "
                     "can show clearly",
             "correct": False,
             "why": "Diagrams follow the evidence. The evidence is what "
                    "limits the number"},
            {"text": "Because the evidence shows only a few depths at which "
                     "the material changes sharply",
             "correct": True},
            {"text": "Because each layer has to be at least a thousand "
                     "kilometres thick to count as one",
             "correct": False,
             "why": "The crust is about 35 km thick and is one of the four"},
            {"text": "Because instruments are not sensitive enough to detect "
                     "any more than four",
             "correct": False,
             "why": "Modern records resolve fine detail, and finer divisions "
                    "within the layers are described where they exist"},
        ],
        "figure": None,
    },
    {
        "id": "c10-01-h30",
        "band": "harder",
        "text": "A space agency wants to know whether another rocky planet "
                "has a liquid core. What measurement would settle it?",
        "options": [
            {"text": "Photographs of its whole surface taken from orbit above "
                     "it, in the finest detail available",
             "correct": False,
             "why": "No photograph shows anything below the surface"},
            {"text": "The temperature of its surface, measured from orbit",
             "correct": False,
             "why": "Surface temperature is set mostly by the Sun and the "
                    "atmosphere"},
            {"text": "Landing a seismometer and watching how its quakes "
                     "cross the planet",
             "correct": True},
            {"text": "A sample of rock returned from its surface for "
                     "analysis",
             "correct": False,
             "why": "Surface rock is the one thing that says least about the "
                    "core, as the Earth itself shows"},
        ],
        "figure": None,
    },
]
