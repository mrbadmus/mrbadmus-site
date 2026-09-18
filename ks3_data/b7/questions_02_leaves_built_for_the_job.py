"""B7 lesson 02 — Leaves built for the job: twelve questions (MRB-269).

These probe the one argument the lesson is built on — every feature that raises
the rate charges the plant water, so a leaf is a settlement with a place rather
than a list of improvements. The distractors come first from the lesson's two
declared misconceptions: PLANT-03 (leaves are green because chlorophyll uses
green light) drives the colour questions and their wrong options — chlorophyll
absorbing green, red and blue mixing to green, green light being harmful rather
than merely unused, and "light is light, so any lamp will do". PLANT-04 (the
bigger the leaf, the better the plant) drives the bench questions, where a
turned-up dial is read as a better leaf and a habitat verdict is read as a mark.
The rest are the ordinary Year 8 errors this lesson exists to correct: that a
leaf drinks through its surface or its stomata, that air spaces store water or
oxygen, that xylem and phloem carry the opposite things, that carbon dioxide
sinks and collects under a leaf, that stomata are placed out of the light, that
more holes could be free, and that leaves fall in autumn because the frost
killed them. The `harder` band takes the compromise somewhere the lesson never
sets a question — a cactus with no leaves, a water lily with its stomata on the
wrong side, a beech and a pine surviving the same frozen soil in opposite ways,
and a leaf with its stomata sealed shut with petroleum jelly.
"""

UNIT = "B7"
LESSON = "leaves-built-for-the-job"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-e01",
        "band": "easier",
        "text": "Cut a leaf open and the middle layer is loose and open, with "
                "air spaces running between the cells. What are those spaces "
                "doing?",
        "options": [
            {"text": "Storing water, so the leaf has its own supply to draw "
                     "on when the soil dries out.",
             "correct": False,
             "why": "Water arrives through the xylem in the veins and is used, "
                    "not stockpiled in the leaf. The spaces hold air, which is "
                    "the whole point of them."},
            {"text": "Letting carbon dioxide reach every photosynthesising "
                     "cell, and giving the oxygen made a way out.",
             "correct": True},
            {"text": "Holding the blade of the leaf out flat and rigid so "
                     "that it does not fold over on itself.",
             "correct": False,
             "why": "Holding the blade flat is the veins' job. The spongy "
                    "layer is deliberately loose so that gases can move "
                    "through it."},
            {"text": "Storing the oxygen the leaf makes, until the plant "
                     "needs to use it later in the day.",
             "correct": False,
             "why": "Oxygen is not put away for later — it diffuses straight "
                    "out through the stomata. The spaces are a route for "
                    "gases, not a container."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e02",
        "band": "easier",
        "text": "The veins running through a leaf carry two different things, "
                "travelling in opposite directions. Which two?",
        "options": [
            {"text": "Xylem carries sugar up into the leaf, and phloem "
                     "carries the water it makes back down.",
             "correct": False,
             "why": "You have the two swapped, and sugar is made in the leaf "
                    "rather than delivered to it. Xylem brings water up; "
                    "phloem takes sugar away."},
            {"text": "One set of veins carries carbon dioxide in, and the "
                     "other carries the oxygen back out again.",
             "correct": False,
             "why": "Gases do not travel in the veins at all. They move in "
                    "and out through the stomata and spread through the air "
                    "spaces inside."},
            {"text": "Xylem carries water up from the roots, and phloem "
                     "carries dissolved sugar away from the leaf.",
             "correct": True},
            {"text": "Both of them carry water: one set feeds the top of the "
                     "leaf and the other feeds the underside.",
             "correct": False,
             "why": "Only the xylem carries water. The phloem carries the "
                    "dissolved sugar the leaf has made, out to the rest of "
                    "the plant."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e03",
        "band": "easier",
        "text": "Almost every stoma in a leaf is on the underside rather than "
                "the upper surface. What does the plant gain by putting them "
                "there?",
        "options": [
            {"text": "Less water evaporates from a hole in the shade than "
                     "from one in the sun on the upper surface.",
             "correct": True},
            {"text": "Carbon dioxide is heavier than air, so it sinks and "
                     "collects underneath the leaf where the holes are.",
             "correct": False,
             "why": "Gases do not settle into layers like that. Carbon "
                    "dioxide reaches the leaf from every side and diffuses in "
                    "through any open stoma."},
            {"text": "The upper surface is covered by the waxy cuticle, so no "
                     "hole could ever be opened through it there.",
             "correct": False,
             "why": "The cuticle is a layer the leaf builds, not a wall it "
                    "cannot get through, and the underside has one too. The "
                    "reason is water."},
            {"text": "Stomata have to be kept out of the light, because light "
                     "stops them opening and closing properly.",
             "correct": False,
             "why": "Light does not stop a stoma working. They sit "
                    "underneath because a shaded hole loses less water than a "
                    "sunlit one."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e04",
        "band": "easier",
        "text": "A leaf looks green to you. Which colours of light is the "
                "chlorophyll inside it actually absorbing?",
        "options": [
            {"text": "The green, which is exactly why the leaf looks that "
                     "colour when you look at it.",
             "correct": False,
             "why": "It is the other way round. You see the light a thing "
                    "sends back, so a green leaf is a leaf throwing green "
                    "light away."},
            {"text": "Every colour about equally, since light is light as far "
                     "as a plant is concerned.",
             "correct": False,
             "why": "Chlorophyll is fussy about colour. It absorbs strongly "
                    "in the red and the blue and barely touches the green in "
                    "the middle."},
            {"text": "Only the green and the yellow, which are the brightest "
                     "part of ordinary daylight.",
             "correct": False,
             "why": "Green is the part chlorophyll uses least of all — it "
                    "reflects it, which is the reason the leaf looks green to "
                    "you."},
            {"text": "The red and the blue strongly, and hardly any of the "
                     "green in the middle.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-02-s01",
        "band": "standard",
        "text": "On the bench you leave every other dial alone and turn the "
                "stomata up from Normal to Many. Predict what the two "
                "readouts do.",
        "options": [
            {"text": "The rate rises and the water loss stays put, because "
                     "the extra holes only let gas in.",
             "correct": False,
             "why": "Every hole that lets carbon dioxide in lets water out. "
                    "That trade is the thing the whole bench was built to "
                    "show you."},
            {"text": "The water loss rises and the rate stays put, because "
                     "the leaf already had all the gas it needed.",
             "correct": False,
             "why": "More stomata do raise the rate — carbon dioxide gets in "
                    "faster. They simply raise the water loss faster still."},
            {"text": "Both rise, and the water loss climbs the more steeply "
                     "of the two readouts.",
             "correct": True},
            {"text": "Both readouts fall, because the extra holes weaken the "
                     "leaf and it works less well.",
             "correct": False,
             "why": "Extra holes do not weaken anything. Both readouts go up; "
                    "the lesson is in which of them goes up faster."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s02",
        "band": "standard",
        "text": "A leaf on the bench is broad, thick and fleshy, with many "
                "stomata and no waxy cuticle, and the verdict reads \"The "
                "worst of both\". Which single change buys back the most "
                "water for the least rate?",
        "options": [
            {"text": "Give it a waxy cuticle: the water loss drops sharply "
                     "and the rate barely moves.",
             "correct": True},
            {"text": "Turn the stomata down to Few: the water drops further "
                     "still, and the rate can be spared.",
             "correct": False,
             "why": "Few stomata do cut the water more, but they halve the "
                    "rate as well. You would be paying for water with the "
                    "very thing you came for."},
            {"text": "Make it thin instead of thick and fleshy: a thin leaf "
                     "loses less through its surface.",
             "correct": False,
             "why": "Watch the readout — going thin raises the water loss as "
                    "well as the rate. Thickness was buying water back, not "
                    "costing it."},
            {"text": "Shrink it to a needle: less surface means less water, "
                     "and the rate holds where it is.",
             "correct": False,
             "why": "A needle does lose far less water, but the rate falls "
                    "with it. Change the area and both readouts move "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s03",
        "band": "standard",
        "text": "The bench opens on a leaf that is enormous, thick and "
                "fleshy, with many stomata and no cuticle. The verdict reads "
                "\"A swamp, and nowhere drier\". What is it telling you about "
                "that leaf?",
        "options": [
            {"text": "It is the best leaf on the bench, because every dial "
                     "has been turned up as far as it goes.",
             "correct": False,
             "why": "Turned up is not the same as better. This leaf spends "
                    "more than three times an oak leaf's water, and on a "
                    "hillside in July it wilts by lunchtime."},
            {"text": "It is badly built, and there is nowhere at all that it "
                     "could actually live and survive.",
             "correct": False,
             "why": "There is somewhere — a rainforest or a marsh, where "
                    "water is never short. The verdict names a habitat rather "
                    "than marking your leaf."},
            {"text": "It suits a swamp because a leaf in damp air can take "
                     "water back in through its own surface.",
             "correct": False,
             "why": "Leaves do not drink from the air. It suits a swamp "
                    "because the roots there can always replace what the leaf "
                    "is losing."},
            {"text": "It photosynthesises a little faster than an oak leaf, "
                     "for more than three times the water.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s04",
        "band": "standard",
        "text": "The growing lamps in a commercial glasshouse are an odd "
                "purple-pink rather than white. What is the grower paying "
                "for?",
        "options": [
            {"text": "Green light, the colour plants use most — red and blue "
                     "lamps together give off a green glow.",
             "correct": False,
             "why": "Green is the colour chlorophyll uses least, which is why "
                    "the leaf reflects it at you. Red and blue light together "
                    "look pink, not green."},
            {"text": "The red and blue that chlorophyll absorbs, not the green "
                     "the leaf throws away.",
             "correct": True},
            {"text": "Protection from green light, which damages a leaf that "
                     "is left under it for too long.",
             "correct": False,
             "why": "Green light does a leaf no harm at all. The plant simply "
                    "cannot use it, so the grower is avoiding waste rather "
                    "than avoiding damage."},
            {"text": "Whichever lamp came cheapest, since chlorophyll absorbs "
                     "every colour about equally anyway.",
             "correct": False,
             "why": "Chlorophyll does not treat the colours equally. It "
                    "absorbs strongly in the red and the blue and hardly "
                    "touches the green."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-h01",
        "band": "harder",
        "text": "A cactus has done away with leaves altogether: its stem "
                "photosynthesises and its spines are leaves that gave up the "
                "job. Read that against the two readouts. What has a cactus "
                "traded?",
        "options": [
            {"text": "It photosynthesises without losing any water at all, "
                     "which wins on both readouts at once.",
             "correct": False,
             "why": "There is no such setting on the bench and none in a "
                    "desert. Every route that lets carbon dioxide in lets "
                    "some water out; a cactus has made that route as small as "
                    "it can."},
            {"text": "It has given up photosynthesis, and lives instead on "
                     "the water stored in its thick stem.",
             "correct": False,
             "why": "Water is not food. A cactus photosynthesises perfectly "
                    "well — the stem does the job the leaves used to do, only "
                    "slowly."},
            {"text": "It photosynthesises faster than a leafy plant, because "
                     "a thick stem packs in far more chloroplasts.",
             "correct": False,
             "why": "Thick does not mean fast. Light cannot reach the "
                    "chloroplasts deep inside, which is the same reason a "
                    "leaf is thin rather than fleshy."},
            {"text": "A very low rate, accepted in exchange for losing almost "
                     "no water — so it grows slowly and lasts.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h02",
        "band": "harder",
        "text": "A water lily's leaf floats flat on a pond, and its stomata "
                "are on the top surface instead of the underside. Why is that "
                "the right way round for this plant?",
        "options": [
            {"text": "It is simply a worse-built leaf than an oak's — not "
                     "every plant gets its adaptations right.",
             "correct": False,
             "why": "Better does not exist on its own in biology. The lily's "
                    "leaf is the compromise that works on a pond, exactly as "
                    "an oak's works in a hedgerow."},
            {"text": "The underside is against the water, where gases cannot "
                     "pass, and a floating leaf cannot dry out.",
             "correct": True},
            {"text": "The holes are on top so that the leaf can take in the "
                     "pond water it is floating on.",
             "correct": False,
             "why": "Stomata are for gases, not for drinking. Water still "
                    "comes up through the roots and the xylem, as it does in "
                    "any other plant."},
            {"text": "Stomata underneath would be in the shade, and a stoma "
                     "needs light on it to work at all.",
             "correct": False,
             "why": "Shade is the reason a land plant puts them underneath — "
                    "a shaded hole loses less water. The lily's problem is "
                    "the water itself, not the light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h03",
        "band": "harder",
        "text": "In winter the water in the soil is frozen. A beech has "
                "dropped every broad leaf; a pine beside it keeps its "
                "needles. Both survive. What is each one doing?",
        "options": [
            {"text": "The beech's leaves were killed by the first frost, and "
                     "the pine's needles are tough enough to survive it.",
             "correct": False,
             "why": "A beech drops its leaves on purpose, and starts before "
                    "the frost. It sheds them because a broad leaf goes on "
                    "losing water that frozen soil cannot replace."},
            {"text": "The pine keeps its needles to catch what little winter "
                     "light there is, and the beech has given up on light.",
             "correct": False,
             "why": "Light is not what settles it. The winter question is "
                    "water: a beech cannot pay for a broad leaf, and a small "
                    "waxy needle costs very little."},
            {"text": "The beech has removed the surface that leaks water; the "
                     "pine keeps a small waxy one it can still afford.",
             "correct": True},
            {"text": "The beech has stored enough sugar to stop "
                     "photosynthesising, and the pine has not stored any.",
             "correct": False,
             "why": "Neither bet is about the store. A broad leaf keeps "
                    "losing water all winter; a needle loses little enough to "
                    "be worth keeping."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h04",
        "band": "harder",
        "text": "A student smears petroleum jelly over the whole underside of "
                "a living leaf, sealing every stoma, and leaves the plant in "
                "the light. Predict what the two readouts do.",
        "options": [
            {"text": "The water loss falls a long way, and the rate falls "
                     "with it, because no carbon dioxide can get in.",
             "correct": True},
            {"text": "The water loss falls and the rate is unchanged, because "
                     "light still reaches the palisade cells.",
             "correct": False,
             "why": "Light is not the only thing a leaf needs. With every "
                    "stoma sealed, no carbon dioxide reaches those cells, so "
                    "the rate falls too."},
            {"text": "The rate falls but the water loss carries on, because "
                     "water leaves through the whole leaf surface.",
             "correct": False,
             "why": "Very little escapes through the surface — the waxy "
                    "cuticle sees to that. Almost all of it leaves through "
                    "the holes you have just sealed."},
            {"text": "Both readouts rise, because a sealed leaf traps carbon "
                     "dioxide inside where the cells can use it.",
             "correct": False,
             "why": "There is nothing to trap. The cells use up the carbon "
                    "dioxide already inside within minutes, and sealing the "
                    "holes stops any more arriving."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-e05",
        "band": "easier",
        "text": "Which cells stand in a layer directly under the upper "
                "surface of a leaf, packed with chloroplasts?",
        "options": [
            {"text": "The guard cells, which sit in pairs around each pore.",
             "correct": False,
             "why": "Guard cells are on the underside, around the stomata. "
                    "The tall cells packed with chloroplasts near the top are "
                    "the palisade cells."},
            {"text": "The palisade cells, standing tall and side by side near "
                     "the top.",
             "correct": True},
            {"text": "The spongy layer cells, rounded with air spaces between "
                     "them.",
             "correct": False,
             "why": "Those are in the middle of the leaf and carry far fewer "
                    "chloroplasts each. The tall packed cells at the top are "
                    "the palisade cells."},
            {"text": "The epidermis cells, forming the transparent skin over "
                     "the leaf.",
             "correct": False,
             "why": "The epidermis is the single transparent row above the "
                    "palisade layer. It is the light's way in rather than the "
                    "place the light is used."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e06",
        "band": "easier",
        "text": "Photosynthesis happens inside one particular part of a plant "
                "cell. Which part?",
        "options": [
            {"text": "The cell wall, which is built out of the glucose the "
                     "plant makes.",
             "correct": False,
             "why": "The wall is built from cellulose made out of glucose, so "
                    "it is a product rather than a place. The reaction "
                    "happens in the chloroplasts."},
            {"text": "The vacuole, the large space filled with liquid.",
             "correct": False,
             "why": "The vacuole holds cell sap. The reaction happens in the "
                    "chloroplasts, which are the parts that hold the "
                    "chlorophyll."},
            {"text": "The stoma, since that is where the carbon dioxide "
                     "arrives.",
             "correct": False,
             "why": "A stoma is a pore in the leaf's surface, not a part of a "
                    "cell. The gas travels on to the chloroplasts, where the "
                    "reaction happens."},
            {"text": "The chloroplast, which is the part that holds the green "
                     "chlorophyll.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e07",
        "band": "easier",
        "text": "The outer surface of a leaf is covered by a waxy cuticle. "
                "What does it do?",
        "options": [
            {"text": "It slows water loss: water evaporates only slowly "
                     "through wax.",
             "correct": True},
            {"text": "It absorbs the light and passes the energy on to the "
                     "palisade cells underneath.",
             "correct": False,
             "why": "Light is absorbed by chlorophyll, inside the "
                    "chloroplasts. The cuticle is a transparent waxy layer "
                    "and its subject is water."},
            {"text": "It lets carbon dioxide in through the wax while "
                     "holding the water in, so both problems are solved at "
                     "once.",
             "correct": False,
             "why": "Gases do not cross the cuticle. Carbon dioxide goes in "
                    "through the stomata, which is exactly why those holes "
                    "cost the plant water."},
            {"text": "It keeps the whole blade rigid and flat, so that the "
                     "leaf holds itself out towards the light.",
             "correct": False,
             "why": "That is the vein network's doing. The cuticle is a thin "
                    "waxy layer whose job is limiting water loss."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e08",
        "band": "easier",
        "text": "What is a stoma, and what passes through it?",
        "options": [
            {"text": "A vein running through the leaf, carrying water in and "
                     "sugar out.",
             "correct": False,
             "why": "Those are the xylem and the phloem inside a vein. A "
                    "stoma is a hole in the surface of the leaf."},
            {"text": "A pore in the leaf's surface, through which water is "
                     "drawn in from the air.",
             "correct": False,
             "why": "A leaf does not drink through its holes. Water arrives "
                    "up the xylem from the roots, and what moves through a "
                    "stoma is gas."},
            {"text": "A pore in the leaf's surface, through which gases move "
                     "in and out.",
             "correct": True},
            {"text": "A packet of chlorophyll inside a palisade cell, where "
                     "the reaction happens.",
             "correct": False,
             "why": "That is a chloroplast. A stoma is a hole, and more than "
                    "one of them is stomata."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e09",
        "band": "easier",
        "text": "Besides carrying water and sugar, the vein network does a "
                "third job in a leaf. What is it?",
        "options": [
            {"text": "It stores starch for the leaf to draw on overnight.",
             "correct": False,
             "why": "Starch is stored in the cells where it was made, not in "
                    "the veins. The third job the veins do is a mechanical "
                    "one."},
            {"text": "It holds the blade rigid and flat, so the leaf stays "
                     "spread out.",
             "correct": True},
            {"text": "It carries carbon dioxide from the stomata to the "
                     "palisade cells.",
             "correct": False,
             "why": "Gases travel through the air spaces in the spongy layer, "
                    "not along the veins. The third job is holding the blade "
                    "out flat."},
            {"text": "It lets water evaporate away, which is how a leaf keeps "
                     "cool.",
             "correct": False,
             "why": "Water leaves mainly through the stomata. What the vein "
                    "network adds, besides delivery and collection, is "
                    "support."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e10",
        "band": "easier",
        "text": "Carbon dioxide reaches a cell in the middle of a leaf by "
                "diffusion. What does diffusion mean?",
        "options": [
            {"text": "A substance spreading from where there is more of it to "
                     "where there is less.",
             "correct": True},
            {"text": "A substance being pushed along a tube by a pump, the "
                     "way blood is moved.",
             "correct": False,
             "why": "Nothing pumps gas around a leaf. It spreads out on its "
                    "own, from where there is more of it to where there is "
                    "less."},
            {"text": "A substance dissolving in water and being carried along "
                     "by it.",
             "correct": False,
             "why": "That is how sugar travels in the phloem. Carbon dioxide "
                    "reaches the cells by spreading through the air spaces."},
            {"text": "A substance being absorbed by a surface and held there.",
             "correct": False,
             "why": "Diffusion is movement rather than capture — a spreading "
                    "out from where there is more of something to where there "
                    "is less."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e11",
        "band": "easier",
        "text": "Why is a leaf broad and flat?",
        "options": [
            {"text": "So that rain runs off it quickly and the whole surface "
                     "dries out again before the leaf can begin to rot in "
                     "wet weather.",
             "correct": False,
             "why": "Shedding rain is not what shapes a leaf. Broad and flat "
                    "is about catching light and keeping every cell near a "
                    "surface."},
            {"text": "So that it can hold as many layers of "
                     "photosynthesising cells stacked inside the blade as it "
                     "possibly can.",
             "correct": False,
             "why": "A leaf is deliberately thin rather than deep. Broad is "
                    "about area; thin is about how far light and gases have "
                    "to travel."},
            {"text": "So that it can store the water the plant will need in "
                     "dry weather.",
             "correct": False,
             "why": "Leaves lose water rather than stockpiling it. The broad "
                    "flat shape is about intercepting light."},
            {"text": "So that it intercepts as much light as possible and "
                     "keeps every cell close to a surface.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e12",
        "band": "easier",
        "text": "In October a beech wood turns yellow and orange. Where have "
                "those colours come from?",
        "options": [
            {"text": "The tree makes fresh yellow and orange pigments in "
                     "autumn to replace the green one it has taken back out "
                     "of its leaves.",
             "correct": False,
             "why": "Nothing new has to be made. The yellows and oranges were "
                    "in the leaf all summer, masked by so much chlorophyll "
                    "that you could not see them."},
            {"text": "The first hard frost of the autumn turns the green "
                     "pigment yellow and orange wherever it touches a leaf.",
             "correct": False,
             "why": "The colour usually changes before the first frost. What "
                    "has happened is that the tree has dismantled its "
                    "chlorophyll and stopped hiding the other pigments."},
            {"text": "They were in the leaves all summer, hidden by the "
                     "chlorophyll.",
             "correct": True},
            {"text": "The leaves have filled with the sugar the tree could "
                     "not carry away in time.",
             "correct": False,
             "why": "Sugar is colourless and is moved out through the "
                    "phloem. The yellows and oranges are pigments that were "
                    "there all along."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e13",
        "band": "easier",
        "text": "What does it mean to call a feature of an organism an "
                "adaptation?",
        "options": [
            {"text": "It is a feature that works well in the conditions where "
                     "that organism lives.",
             "correct": True},
            {"text": "It is a feature that is better than the same feature in "
                     "any other organism.",
             "correct": False,
             "why": "Better does not exist on its own in biology. A needle "
                    "beats a broad leaf on a frozen hillside and loses to it "
                    "on a shaded forest floor."},
            {"text": "It is a change an organism makes to itself during its "
                     "life to suit the weather.",
             "correct": False,
             "why": "An adaptation is a feature the organism has, not "
                    "something it decides on. What makes it an adaptation is "
                    "that it suits the place."},
            {"text": "It is a feature that costs the organism nothing, since "
                     "it already suits its home.",
             "correct": False,
             "why": "Almost every adaptation is a compromise with a price. A "
                    "broad leaf catches more light and loses more water for "
                    "it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-02-s05",
        "band": "standard",
        "text": "A pine needle has far less surface area than a broad oak "
                "leaf. Compared with that oak leaf, what are a needle's rate "
                "of photosynthesis and its water loss?",
        "options": [
            {"text": "The rate is the same and the water loss is lower, "
                     "since a needle is only a leaf made narrower.",
             "correct": False,
             "why": "Surface area moves both together. A needle intercepts "
                    "far less light, so its rate is lower as well."},
            {"text": "Both are higher, because a narrow leaf concentrates "
                     "the light that falls on it.",
             "correct": False,
             "why": "Nothing concentrates light here. A smaller surface "
                    "intercepts less of it, so both are lower."},
            {"text": "Both are lower — a needle intercepts far less light "
                     "and loses far less water.",
             "correct": True},
            {"text": "The rate is lower and the water loss is higher, "
                     "because a narrow leaf dries out faster.",
             "correct": False,
             "why": "Less surface means less water lost, not more. Both drop "
                    "together when the area drops."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s06",
        "band": "standard",
        "text": "Two leaves photosynthesise at the same rate, but one of them "
                "loses twice as much water a day as the other. Which would "
                "you expect on a dry hillside in July, and why?",
        "options": [
            {"text": "The drier one, because on a hillside the roots cannot "
                     "replace water at that speed.",
             "correct": True},
            {"text": "The thirstier one, because more water moving through a "
                     "leaf means faster growth.",
             "correct": False,
             "why": "Water lost is a cost, not a driver. Both leaves "
                    "photosynthesise at the same rate, and one of them is "
                    "paying twice as much for it."},
            {"text": "Either would do equally well, since the two "
                     "photosynthesise at the same rate.",
             "correct": False,
             "why": "The rate is only half the account. On a dry hillside the "
                    "water bill is what decides whether the plant sees out "
                    "the summer."},
            {"text": "The thirstier one, because losing water is how a leaf "
                     "keeps itself cool in July.",
             "correct": False,
             "why": "Evaporation does cool a leaf, but a plant that cannot "
                    "replace the water wilts — and a wilted leaf "
                    "photosynthesises at nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s07",
        "band": "standard",
        "text": "Carbon dioxide enters through a stoma on the underside of a "
                "leaf and is used in a palisade cell near the top. How does "
                "it get from one to the other?",
        "options": [
            {"text": "It is carried up in the xylem, along with the water "
                     "arriving from the roots.",
             "correct": False,
             "why": "The xylem carries water, and gases do not travel in the "
                    "veins at all. Carbon dioxide moves through the air "
                    "spaces."},
            {"text": "It is pumped upwards by the guard cells as they open "
                     "and close.",
             "correct": False,
             "why": "Guard cells open and close a hole; they do not drive gas "
                    "along. It spreads through the air spaces on its own."},
            {"text": "It dissolves in the water inside the leaf and is "
                     "carried to the top by the phloem.",
             "correct": False,
             "why": "Phloem carries dissolved sugar away from the leaf. "
                    "Carbon dioxide reaches the cells by diffusing through "
                    "the air spaces."},
            {"text": "It diffuses through the air spaces of the spongy layer, "
                     "which run up between the cells.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s08",
        "band": "standard",
        "text": "A gardener polishes a thin layer of wax over the whole upper "
                "surface of a leaf, to protect it. What happens to its rate "
                "of photosynthesis and to the water it loses?",
        "options": [
            {"text": "Both fall sharply, because the leaf can no longer take "
                     "in any carbon dioxide.",
             "correct": False,
             "why": "Almost all the gas goes in underneath, where the stomata "
                    "are. Sealing the top surface blocks very little of it."},
            {"text": "Very little changes, because almost all the gas "
                     "exchange and the water loss happen underneath.",
             "correct": True},
            {"text": "The rate falls and the water loss is unchanged, because "
                     "the wax blocks the light.",
             "correct": False,
             "why": "A thin layer of wax is not a blackout, and the upper "
                    "surface already carries a waxy cuticle of its own."},
            {"text": "The water loss falls sharply and the rate is unchanged, "
                     "because the top is where the water goes.",
             "correct": False,
             "why": "The top surface already has a cuticle and loses little. "
                    "Water leaves through the stomata, and those are "
                    "underneath."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s09",
        "band": "standard",
        "text": "Leaves low down and deep inside a large tree are often "
                "broader and thinner than the leaves at the very top of the "
                "same tree. Explain that difference.",
        "options": [
            {"text": "The lower leaves are younger, and a leaf grows narrower "
                     "and thicker as it ages.",
             "correct": False,
             "why": "Age is not what differs here. The two positions receive "
                    "very different amounts of light, and each leaf is built "
                    "for the light it gets."},
            {"text": "The lower leaves are further from the roots, so less "
                     "water reaches them.",
             "correct": False,
             "why": "If anything the lower leaves are nearer the roots. What "
                    "actually differs between the two positions is the "
                    "light."},
            {"text": "Light is scarce lower down, so a broader, thinner blade "
                     "is worth the extra water it costs.",
             "correct": True},
            {"text": "The top leaves curl in the afternoon sun, so they only "
                     "look thicker than the ones below.",
             "correct": False,
             "why": "The difference is a settled one rather than a trick of "
                    "the light. It comes from how much light each position "
                    "receives."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s10",
        "band": "standard",
        "text": "A simple computer model of a leaf predicts a rate of "
                "photosynthesis and a water loss for any leaf shape, but it "
                "has nothing in it for temperature or wind. What does that "
                "mean for the habitat it suggests?",
        "options": [
            {"text": "It shows the direction of a trade rather than what "
                     "would really happen in that habitat.",
             "correct": True},
            {"text": "It is worthless, since a model with anything left out "
                     "can teach you nothing.",
             "correct": False,
             "why": "A model with something left out is still useful as long "
                    "as you know what is missing. This one shows the trade "
                    "between rate and water well."},
            {"text": "It is exact, because temperature and wind have no "
                     "effect on a real leaf.",
             "correct": False,
             "why": "Both matter a great deal to a real leaf, which is "
                    "precisely why leaving them out limits what the model "
                    "can tell you."},
            {"text": "It applies to oak trees only, because its figures are "
                     "percentages of an oak leaf.",
             "correct": False,
             "why": "The oak is only the baseline the percentages are "
                    "measured against. What is missing is temperature, wind "
                    "and several other real costs."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s11",
        "band": "standard",
        "text": "Why does the vein network branch out through the whole blade "
                "rather than running down the middle of the leaf only?",
        "options": [
            {"text": "Because water can travel only a few millimetres inside "
                     "a leaf before it evaporates away through the surface.",
             "correct": False,
             "why": "Water travels the height of a tree in the xylem. The "
                    "veins branch so that every part of the blade is served."},
            {"text": "Because branching veins catch more light than a single "
                     "thick one would.",
             "correct": False,
             "why": "Veins do not photosynthesise; the cells around them do. "
                    "The branching is about delivery, collection and "
                    "support."},
            {"text": "Because the branches are where the stomata open, and "
                     "those are spread right across the whole leaf.",
             "correct": False,
             "why": "Stomata are in the leaf's outer skin, not in the veins. "
                    "The branching is there so no cell is far from water or "
                    "from the phloem."},
            {"text": "Because every part of the blade needs water brought "
                     "in, sugar taken out and support.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s12",
        "band": "standard",
        "text": "Building a bigger leaf costs the plant water. Name another "
                "cost of a bigger leaf.",
        "options": [
            {"text": "It would need a thicker cuticle, and wax is the most "
                     "expensive thing a plant makes.",
             "correct": False,
             "why": "There is no rule that a bigger leaf needs more wax per "
                    "square centimetre. The real extra costs are tissue, "
                    "weight and shading."},
            {"text": "There is more tissue to build and keep alive, and more "
                     "weight for the stem to hold out.",
             "correct": True},
            {"text": "It would run out of chlorophyll, since a plant can only "
                     "make a fixed amount of it.",
             "correct": False,
             "why": "A plant builds chlorophyll as it builds leaf. The costs "
                    "that count are the tissue, the weight and the shade the "
                    "leaf casts."},
            {"text": "It would use up the carbon dioxide around it faster "
                     "than the air outside could replace it.",
             "correct": False,
             "why": "Air moves and replaces itself around a leaf. The costs "
                    "that really weigh are building the tissue and holding it "
                    "out."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s13",
        "band": "standard",
        "text": "Palisade cells are packed with chloroplasts while the "
                "rounded cells of the spongy layer carry only one or two "
                "each. Suggest why the spongy layer is not packed as well.",
        "options": [
            {"text": "Chloroplasts cannot survive in the middle of a leaf, "
                     "where it is too warm for them.",
             "correct": False,
             "why": "There is nothing hostile about the middle of a leaf — "
                    "the spongy cells do carry chloroplasts, just far fewer "
                    "of them."},
            {"text": "The spongy cells are too small to hold more than one "
                     "chloroplast each.",
             "correct": False,
             "why": "Spongy cells are rounded and roomy. What limits them is "
                    "the light reaching that depth and the space the air "
                    "spaces need."},
            {"text": "Less light reaches that depth, and the layer has to "
                     "stay open so gases can move through it.",
             "correct": True},
            {"text": "The spongy layer is where the leaf stores its starch, "
                     "so there is no room for anything else.",
             "correct": False,
             "why": "Starch is stored where it is made, inside the "
                    "chloroplasts. The spongy layer's job is to let gases "
                    "through."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-h05",
        "band": "harder",
        "text": "A leaf is measured photosynthesising at 110% of an oak "
                "leaf's rate while losing 363% of an oak leaf's water. How "
                "much water is it spending for each unit of photosynthesis, "
                "compared with the oak leaf?",
        "options": [
            {"text": "About 3.6 times as much, since it loses 363% of the "
                     "water an oak leaf loses.",
             "correct": False,
             "why": "That is how much more water it spends altogether. Per "
                    "unit of photosynthesis you divide by the rate — 363 by "
                    "110, not by 100."},
            {"text": "About 3.3 times as much, since 363 divided by 110 is "
                     "about 3.3.",
             "correct": True},
            {"text": "About 1.1 times as much, since it photosynthesises at "
                     "110% of the oak leaf's rate.",
             "correct": False,
             "why": "That is the rate comparison rather than the water one. "
                    "Dividing the water by the rate, 363 by 110, gives about "
                    "3.3."},
            {"text": "About 0.3 times as much, since 110 divided by 363 is "
                     "about 0.3.",
             "correct": False,
             "why": "You have divided the wrong way round. Water per unit of "
                    "photosynthesis is the water reading divided by the rate "
                    "reading."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h06",
        "band": "harder",
        "text": "Marram grass on a sand dune rolls each leaf into a tube, "
                "with the stomata on the inside of the roll. What does that "
                "buy the plant, and what does it cost?",
        "options": [
            {"text": "It buys more light, since a rolled leaf catches the sun "
                     "from every side, and it costs nothing.",
             "correct": False,
             "why": "A rolled leaf presents less area to the sun, not more, "
                    "and there are no free moves on a dune. What it buys is "
                    "water."},
            {"text": "It buys extra carbon dioxide, which collects inside the "
                     "tube, and it costs the plant water.",
             "correct": False,
             "why": "Carbon dioxide does not collect in the roll — it is "
                    "being used up in there. What is held inside is damp air, "
                    "and the cost is a lower rate."},
            {"text": "It buys nothing at all, since a stoma works the same "
                     "wherever it sits on a leaf.",
             "correct": False,
             "why": "Placement matters a great deal. A stoma opening into "
                    "still damp air inside a roll loses far less water than "
                    "one facing a dry wind."},
            {"text": "It buys a large saving in water, since the air inside "
                     "the roll stays damp, and it costs light and rate.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h07",
        "band": "harder",
        "text": "Before a beech drops its leaves in autumn it dismantles the "
                "chlorophyll in them. Why not simply drop them green?",
        "options": [
            {"text": "Chlorophyll is built around nitrogen and magnesium, "
                     "which the tree pulls back into its twigs.",
             "correct": True},
            {"text": "A green leaf would go on photosynthesising where it "
                     "lay on the ground and rob the tree of the store it had "
                     "built up.",
             "correct": False,
             "why": "A fallen leaf is cut off from the tree entirely. What "
                    "the tree is recovering is the material its chlorophyll "
                    "was built from."},
            {"text": "The green pigment would poison the soil under the tree "
                     "as the leaves rotted.",
             "correct": False,
             "why": "Leaf litter feeds the soil rather than poisoning it. The "
                    "dismantling happens because the atoms in chlorophyll are "
                    "worth keeping."},
            {"text": "A leaf has to lose all its colour before the layer "
                     "holding it to the twig will let the wind pull it off.",
             "correct": False,
             "why": "Colour has nothing to do with how a leaf is shed. The "
                    "tree takes the chlorophyll apart to recover the nitrogen "
                    "and magnesium in it."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h08",
        "band": "harder",
        "text": "On the same woodland floor a holly leaf is thick, waxy and "
                "lasts for years, while a bluebell leaf is thin and soft and "
                "has gone by June. Explain how both can be well adapted.",
        "options": [
            {"text": "The bluebell is poorly adapted, and survives only "
                     "because the holly shades it from the worst of the "
                     "summer.",
             "correct": False,
             "why": "The bluebell is doing very well. It uses the bright "
                    "weeks before the canopy closes over, and then it is "
                    "finished with leaves for the year."},
            {"text": "The holly is poorly adapted, since a thick waxy leaf "
                     "photosynthesises slowly all the year round.",
             "correct": False,
             "why": "Slow and lasting is a settlement rather than a fault. A "
                    "holly leaf still works in winter, when the bluebell has "
                    "nothing above ground at all."},
            {"text": "The bluebell buys a high rate for a few bright weeks; "
                     "the holly buys a leaf tough enough to last through "
                     "winters.",
             "correct": True},
            {"text": "They are adapted to different amounts of water, since "
                     "the holly's waxy surface belongs in a dry habitat.",
             "correct": False,
             "why": "Both are growing in the same damp wood. What differs is "
                    "how long each leaf has to last and when its light "
                    "arrives."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h09",
        "band": "harder",
        "text": "The leaves of a pondweed growing entirely under water have "
                "almost no waxy cuticle and no stomata at all. Explain how "
                "they manage without either.",
        "options": [
            {"text": "They take their carbon dioxide up through their roots "
                     "and along the veins, instead of through the surface "
                     "of the leaf.",
             "correct": False,
             "why": "Pondweed roots anchor it rather than feed it, and gases "
                    "do not travel in the veins. The gas crosses the leaf "
                    "surface itself."},
            {"text": "Under water there is nothing to dry out, so dissolved "
                     "gases cross the surface directly and no holes are "
                     "needed.",
             "correct": True},
            {"text": "They do not photosynthesise at all, and live on "
                     "material drifting down from the surface.",
             "correct": False,
             "why": "Pondweed is green and photosynthesises briskly — bubbles "
                    "stream off it in bright light. What it does not need is "
                    "protection from drying."},
            {"text": "The water washes carbon dioxide in through the stomata "
                     "faster than air ever could.",
             "correct": False,
             "why": "There are no stomata for it to be washed through. The "
                    "dissolved gas crosses the surface of the leaf itself."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h10",
        "band": "harder",
        "text": "Two identical potted plants are watered the same. Half the "
                "leaves are cut off one of them. Compared with the untouched "
                "plant, what happens to that one's water loss and its growth?",
        "options": [
            {"text": "Both fall, because leaf area is what raises the rate "
                     "and what spends the water.",
             "correct": True},
            {"text": "Its water loss falls and its growth is unchanged, "
                     "because the leaves left on it work harder.",
             "correct": False,
             "why": "Leaves do not take on extra work when their neighbours "
                    "go. Less area means less light intercepted, so the "
                    "growth falls too."},
            {"text": "Its water loss is unchanged and its growth falls, "
                     "because water leaves through the stem as well.",
             "correct": False,
             "why": "Almost all of it leaves through the stomata on the "
                    "leaves, so removing leaves cuts the loss sharply."},
            {"text": "Both rise, because the remaining leaves now receive "
                     "light that was being shaded from them.",
             "correct": False,
             "why": "A little more light may reach them, nowhere near enough "
                    "to replace the leaves that have gone. Both readings "
                    "fall."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h11",
        "band": "harder",
        "text": "A grower runs fans and vents to keep the air in a glasshouse "
                "drier, to stop mould, and the crop then grows more slowly. "
                "Suggest why.",
        "options": [
            {"text": "Drier air holds less carbon dioxide than damp air does, "
                     "so the plants are left with less of the raw material "
                     "they build glucose from.",
             "correct": False,
             "why": "How dry the air is does not change how much carbon "
                    "dioxide is in it. The connection here runs through the "
                    "plant's water."},
            {"text": "The fans blow the oxygen away from the leaves before "
                     "the plants can use it.",
             "correct": False,
             "why": "Oxygen is what plants release rather than what they use. "
                    "What the drier air changes is how fast water leaves the "
                    "leaves."},
            {"text": "Drier air is colder air, and a cold plant cannot "
                     "photosynthesise at all.",
             "correct": False,
             "why": "Drying air does not have to cool it, and the grower "
                    "controls the heating anyway. The problem is the water "
                    "leaving the leaves."},
            {"text": "Leaves lose water faster into dry moving air, so the "
                     "plants close their stomata and shut the carbon dioxide "
                     "out with it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h12",
        "band": "harder",
        "text": "A student suggests putting stomata on the upper surface as "
                "well as the lower one, so that twice as much carbon dioxide "
                "can get in. What would happen to the rate of photosynthesis "
                "and to the water lost?",
        "options": [
            {"text": "Both would stay as they are, because the leaf already "
                     "takes in all the gas that it can use.",
             "correct": False,
             "why": "More holes do raise the rate — every extra stoma is "
                    "another way in for the gas. The question is what the "
                    "extra rate would cost."},
            {"text": "The rate would double and the water loss would hold "
                     "steady, since the upper surface is already covered by "
                     "a waxy cuticle that keeps water in.",
             "correct": False,
             "why": "Every hole that lets carbon dioxide in lets water out, "
                    "wherever it is. A hole in the cuticle is a hole."},
            {"text": "The rate would rise and the water loss would rise "
                     "faster still, and worse than usual, since a hole in the "
                     "sun loses more than one in the shade.",
             "correct": True},
            {"text": "The rate would fall, because gas coming in from both "
                     "sides would meet in the middle and stop.",
             "correct": False,
             "why": "Gases do not block one another like that; they spread "
                    "out through the air spaces. The rate would rise, and the "
                    "water loss faster."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h13",
        "band": "harder",
        "text": "You are handed two leaves, one from a Devon hedgerow and one "
                "from a hot dry hillside in Spain, and told nothing else. "
                "Which features would tell them apart, and what would that "
                "not tell you?",
        "options": [
            {"text": "The Spanish one will be smaller, thicker or waxier to "
                     "cut water loss; neither is better.",
             "correct": True},
            {"text": "The Spanish one will be the larger of the two, because "
                     "there is more sunlight in Spain and a bigger blade "
                     "catches more of it each day.",
             "correct": False,
             "why": "More light means the leaf can afford to be small. What "
                    "limits it there is water, and area is what spends "
                    "water."},
            {"text": "The Devon one will be the waxier of the two, because a "
                     "damp climate demands more protection from rain.",
             "correct": False,
             "why": "Rain on a leaf is not a problem worth building for. Wax "
                    "keeps water in, so the dry-country leaf is the one that "
                    "carries most."},
            {"text": "Neither can be told from the other, because leaf shape "
                     "depends only on the species and never on the place it "
                     "grew.",
             "correct": False,
             "why": "Species matters and so does habitat. Look across a whole "
                    "hillside and the local compromise is readable off the "
                    "plants."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-e14",
        "band": "easier",
        "text": "A single row of transparent cells covers the top of a leaf, "
                "lying above the palisade layer. What is that row called, and "
                "what does being transparent achieve?",
        "options": [
            {"text": "The spongy layer, and being clear lets carbon dioxide "
                     "through it from the air above.",
             "correct": False,
             "why": "The spongy layer is in the middle of the leaf, below the "
                    "palisade cells, and gas comes in underneath. The clear "
                    "row on top is the upper epidermis."},
            {"text": "The waxy cuticle, and being clear stops the leaf "
                     "overheating in strong sun.",
             "correct": False,
             "why": "The cuticle is a wax layer rather than a row of cells, "
                    "and it is about water rather than heat. The cells "
                    "underneath it are the upper epidermis."},
            {"text": "The palisade layer, and being clear lets you see the "
                     "veins running underneath.",
             "correct": False,
             "why": "Palisade cells are packed with green chloroplasts and "
                    "are anything but clear. The transparent row is the skin "
                    "above them."},
            {"text": "The upper epidermis, and being clear lets light through "
                     "to the cells below.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e15",
        "band": "easier",
        "text": "Each stoma sits between a pair of cells that can open it and "
                "close it again. What are that pair called?",
        "options": [
            {"text": "Palisade cells, the tall ones near the top of the leaf.",
             "correct": False,
             "why": "Palisade cells are working cells packed with "
                    "chloroplasts, and they are nowhere near a pore. The pair "
                    "either side of a stoma are the guard cells."},
            {"text": "Spongy cells, the round ones in the leaf's middle.",
             "correct": False,
             "why": "Spongy cells sit inside the leaf with air spaces between "
                    "them. The pore in the surface is opened and closed by "
                    "guard cells."},
            {"text": "Guard cells, the pair either side of every pore.",
             "correct": True},
            {"text": "Xylem cells, the ones that bring the water up.",
             "correct": False,
             "why": "Xylem runs inside the veins and carries water. A stoma "
                    "is a hole in the leaf's skin, worked by a pair of guard "
                    "cells."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e16",
        "band": "easier",
        "text": "Nearly all the water a plant loses goes from its leaves. "
                "What does it travel out through?",
        "options": [
            {"text": "The veins, which run it back out the way it came in.",
             "correct": False,
             "why": "Veins deliver water and do not return it to the air. It "
                    "escapes through the stomata, the same holes the carbon "
                    "dioxide comes in by."},
            {"text": "The waxy cuticle, which passes water and holds gas in.",
             "correct": False,
             "why": "Wax is what water crosses most slowly of all, which is "
                    "the whole reason a leaf has a cuticle. The water leaves "
                    "through the stomata."},
            {"text": "The stomata, the same holes that let carbon dioxide in.",
             "correct": True},
            {"text": "The palisade cells, which push it out of the top "
                     "surface.",
             "correct": False,
             "why": "Palisade cells do no pushing; they photosynthesise. "
                    "Water evaporates and leaves through the holes in the "
                    "underside."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e17",
        "band": "easier",
        "text": "What is chlorophyll?",
        "options": [
            {"text": "The green liquid that fills a plant cell and moves "
                     "sugar about.",
             "correct": False,
             "why": "Nothing green fills a plant cell. Chlorophyll is the "
                    "pigment held inside the chloroplasts, and it is what "
                    "absorbs the light."},
            {"text": "The tough green layer around a plant cell, made of "
                     "cellulose.",
             "correct": False,
             "why": "A cell wall is made of cellulose and is not green. "
                    "Chlorophyll is the pigment inside the chloroplast."},
            {"text": "The green sugar a leaf builds and sends off in the "
                     "phloem.",
             "correct": False,
             "why": "The sugar a leaf builds is glucose, and it is "
                    "colourless. Chlorophyll is the pigment that absorbed the "
                    "light to make it."},
            {"text": "The green pigment inside a chloroplast that absorbs "
                     "light.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e18",
        "band": "easier",
        "text": "A plant lives on a hot dry hillside where rain is rare. "
                "Which set of leaf features would you expect it to have?",
        "options": [
            {"text": "A large area, many stomata and no cuticle at all.",
             "correct": False,
             "why": "That is the leaf for a swamp, where the roots can always "
                    "replace what is lost. On a dry hillside it would wilt by "
                    "lunchtime."},
            {"text": "A large area, few stomata and a very thin cuticle.",
             "correct": False,
             "why": "The area is the dial that spends the most water of all, "
                    "and a thin cuticle spends more again. Dry-country leaves "
                    "are small and waxy."},
            {"text": "A small area, many stomata and a thin waxy cuticle.",
             "correct": False,
             "why": "Every extra hole is another leak, so a dry-country plant "
                    "has few of them and a thick wax layer as well as a small "
                    "blade."},
            {"text": "A small area, few stomata and a thick waxy cuticle.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e19",
        "band": "easier",
        "text": "On a rainforest floor light is very scarce and water never "
                "is. Which leaf suits that place?",
        "options": [
            {"text": "A needle, which holds on to water through a long dry "
                     "season.",
             "correct": False,
             "why": "Water is not the problem in a rainforest; light is. A "
                    "needle intercepts far too little of it to pay on a "
                    "shaded floor."},
            {"text": "A thick fleshy leaf, which stores water for the plant "
                     "to draw on later in the year.",
             "correct": False,
             "why": "Leaves do not store water, and a thick leaf slows the "
                    "rate down because light cannot reach the cells at the "
                    "bottom of it."},
            {"text": "A broad thin blade, which catches as much as it can of "
                     "the little light there is.",
             "correct": True},
            {"text": "A small waxy leaf, which keeps the rain off the cells "
                     "underneath.",
             "correct": False,
             "why": "Rain on a leaf is not a problem worth building for. On a "
                    "dark forest floor the leaf that pays is the one with the "
                    "most area."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e20",
        "band": "easier",
        "text": "A pine carries needles instead of broad leaves. What is a "
                "needle?",
        "options": [
            {"text": "A woody spine, grown to stop deer eating the tree.",
             "correct": False,
             "why": "A needle is green and photosynthesises. It is a leaf, "
                    "built narrow and tough so that it loses very little "
                    "water."},
            {"text": "A stem that has taken the leaves' job over, as a "
                     "cactus's does.",
             "correct": False,
             "why": "A pine has ordinary stems as well as needles. The needle "
                    "itself is a leaf, made narrow and tough."},
            {"text": "A young leaf that would open out flat in a warmer "
                     "summer.",
             "correct": False,
             "why": "A needle stays a needle for years. It is a leaf built "
                    "that shape from the start, because narrow costs little "
                    "water."},
            {"text": "A leaf, made narrow and tough so that it loses very "
                     "little water.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e21",
        "band": "easier",
        "text": "Palisade cells are tall and narrow, and stand on end rather "
                "than lying flat. What does that shape achieve?",
        "options": [
            {"text": "More of them fit side by side in the layer where the "
                     "light is strongest.",
             "correct": True},
            {"text": "Wide air spaces are left between them, so that gases "
                     "can move freely through the top of the leaf.",
             "correct": False,
             "why": "That is the spongy layer below, which is loose on "
                    "purpose. Palisade cells are packed together tightly."},
            {"text": "Water can run down between them and out of the leaf "
                     "again.",
             "correct": False,
             "why": "Water is delivered by the veins and leaves as vapour "
                    "through the stomata. The palisade cells' shape is about "
                    "how many will fit."},
            {"text": "The top of the leaf is stiffened, so the blade is held "
                     "out flat.",
             "correct": False,
             "why": "Holding the blade out is the vein network's doing. "
                    "Palisade cells stand on end so that more of them sit in "
                    "the brightest layer."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e22",
        "band": "easier",
        "text": "The leaves on a stem are usually spaced so that one does not "
                "sit directly above another. What does that gain the plant?",
        "options": [
            {"text": "Rain runs off the whole plant rather than collecting on "
                     "one leaf.",
             "correct": False,
             "why": "Shedding rain is not what shapes a plant. The spacing is "
                    "there so that leaves do not stand in each other's "
                    "light."},
            {"text": "Each leaf has its own share of the carbon dioxide in "
                     "the air.",
             "correct": False,
             "why": "Air moves and carbon dioxide reaches a leaf from every "
                    "side, so no leaf takes another's share. Light is what "
                    "one leaf can take from another."},
            {"text": "Fewer leaves are shaded by the ones above them, so more "
                     "are lit.",
             "correct": True},
            {"text": "The stem carries less weight on one side, so it does "
                     "not bend.",
             "correct": False,
             "why": "Balance matters to a tall plant and is not why leaves "
                    "are spread out. They are spread so that each one "
                    "receives light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e23",
        "band": "easier",
        "text": "Where on a leaf is the waxy cuticle found?",
        "options": [
            {"text": "On the outside of both surfaces, over the epidermis.",
             "correct": True},
            {"text": "On the upper surface alone, where the sunlight falls.",
             "correct": False,
             "why": "Both surfaces carry one. The upper layer is often "
                    "thicker, but the underside is waxed as well."},
            {"text": "Around each stoma, sealing the pore when it shuts.",
             "correct": False,
             "why": "A stoma is closed by its guard cells rather than by wax. "
                    "The cuticle is a layer over the whole outer surface."},
            {"text": "Between the palisade layer and the spongy layer inside.",
             "correct": False,
             "why": "There is no wax inside a leaf — it would block the gases "
                    "moving about in there. The cuticle is on the outside."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e24",
        "band": "easier",
        "text": "A plant that has run short of water wilts and its leaves "
                "droop. What does that do to its photosynthesis?",
        "options": [
            {"text": "It speeds up, because a drooping leaf is out of the "
                     "worst of the sun.",
             "correct": False,
             "why": "A wilted leaf is in trouble rather than in shade. Its "
                    "rate falls to almost nothing, which is why running dry "
                    "is so expensive."},
            {"text": "It carries on unchanged, since there is still light and "
                     "carbon dioxide.",
             "correct": False,
             "why": "Water is one of the raw materials, and a wilted leaf "
                    "closes up as well. The rate drops to almost nothing."},
            {"text": "It nearly stops — a wilted leaf photosynthesises at "
                     "almost nothing.",
             "correct": True},
            {"text": "It speeds up, because the stomata open wider to let "
                     "more gas in.",
             "correct": False,
             "why": "A plant short of water shuts its stomata rather than "
                    "opening them. Either way a wilted leaf photosynthesises "
                    "at almost nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e25",
        "band": "easier",
        "text": "Between the upper skin of a leaf and the lower one lie two "
                "layers of photosynthesising tissue. Which two?",
        "options": [
            {"text": "The cuticle above and the epidermis below it.",
             "correct": False,
             "why": "Neither of those photosynthesises: one is wax and the "
                    "other is a clear skin. The two working layers are the "
                    "palisade and the spongy."},
            {"text": "The xylem above and the phloem below it.",
             "correct": False,
             "why": "Those are the two tissues inside a vein, and they carry "
                    "things rather than photosynthesise. The working layers "
                    "are the palisade and the spongy."},
            {"text": "The guard cells on the outside and the stomata between "
                     "them.",
             "correct": False,
             "why": "Guard cells and stomata are in the skin, mostly "
                    "underneath, and they handle gases. The two layers in "
                    "between are the palisade and the spongy."},
            {"text": "The palisade layer above and the spongy layer below it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e26",
        "band": "easier",
        "text": "What is the difference between a chloroplast and "
                "chlorophyll?",
        "options": [
            {"text": "A chloroplast is a part of the cell; chlorophyll is the "
                     "pigment inside it.",
             "correct": True},
            {"text": "Chlorophyll is a part of the cell; a chloroplast is the "
                     "pigment inside it.",
             "correct": False,
             "why": "You have them the other way round. The chloroplast is "
                    "the structure, and the chlorophyll is the green pigment "
                    "packed inside it."},
            {"text": "They are two names for one green part of a cell.",
             "correct": False,
             "why": "They are two different things. One is a part of the "
                    "cell; the other is the pigment that part holds."},
            {"text": "A chloroplast is found in a leaf; chlorophyll is found "
                     "down in the root.",
             "correct": False,
             "why": "Roots are underground and hold neither. Both are in the "
                    "green parts, and the chlorophyll is inside the "
                    "chloroplast."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e27",
        "band": "easier",
        "text": "A leaf is usually less than half a millimetre from its top "
                "surface to its bottom one. What does being that thin mean "
                "for the gases moving about inside it?",
        "options": [
            {"text": "They are squeezed flat, and a gas moves faster the "
                     "narrower the space it is in.",
             "correct": False,
             "why": "Being squeezed does not speed a gas up. What thinness "
                    "buys is distance: there is very little of it to cross."},
            {"text": "They are held under pressure, which forces them into "
                     "the cells more quickly.",
             "correct": False,
             "why": "There is no pressure inside a leaf driving gas anywhere. "
                    "The gases spread out on their own, and thinness means a "
                    "short way to spread."},
            {"text": "They cannot get out again, since a thin leaf leaves no "
                     "gap to go by.",
             "correct": False,
             "why": "The leaf is riddled with air spaces and open to the air "
                    "through its stomata. What thinness gives is a short "
                    "journey for the gas."},
            {"text": "They have only a very short way to travel to reach any "
                     "cell.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e28",
        "band": "easier",
        "text": "The upper surface of an oak leaf is a darker green than its "
                "underside. Why?",
        "options": [
            {"text": "The veins lie nearer the top, and it is the veins that "
                     "are green.",
             "correct": False,
             "why": "Veins carry water and sugar and are the palest part of a "
                    "leaf. The colour comes from the chloroplasts packed into "
                    "the palisade cells at the top."},
            {"text": "The palisade cells just below it are packed with "
                     "chloroplasts.",
             "correct": True},
            {"text": "Sunlight has bleached the underside, which spends its "
                     "life in shade.",
             "correct": False,
             "why": "Sunlight does not reach the underside to bleach it, and "
                    "shade does not remove colour. The top is darker because "
                    "of what is packed beneath it."},
            {"text": "The cuticle on top is green; the underside has none.",
             "correct": False,
             "why": "The cuticle is clear, and both surfaces have one. The "
                    "green is in the chloroplasts inside the cells."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e29",
        "band": "easier",
        "text": "Chlorophyll reflects the green light that falls on a leaf. "
                "What does reflects mean here?",
        "options": [
            {"text": "It sends the green light back out rather than absorbing "
                     "it.",
             "correct": True},
            {"text": "It lets the green light pass straight through and out "
                     "the far side.",
             "correct": False,
             "why": "Light that goes straight through has been transmitted, "
                    "not reflected. Reflected light comes back out the way it "
                    "arrived, which is why you see it."},
            {"text": "It stores the green light for later.",
             "correct": False,
             "why": "Light is not stored anywhere. Green is the colour "
                    "chlorophyll cannot use, so it is sent straight back "
                    "out."},
            {"text": "It turns the green light into the red and blue the leaf "
                     "can use.",
             "correct": False,
             "why": "Nothing changes one colour of light into another here. "
                    "The green is simply thrown back, which is the colour you "
                    "end up seeing."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-e30",
        "band": "easier",
        "text": "Every leaf feature that pushes the rate of photosynthesis up "
                "charges the plant the same price. What is that price?",
        "options": [
            {"text": "Warmth lost to the soil.",
             "correct": False,
             "why": "A leaf is not heated from the soil. What every "
                    "rate-raising feature spends is water."},
            {"text": "Water lost from the leaf.",
             "correct": True},
            {"text": "Oxygen taken from the air.",
             "correct": False,
             "why": "A lit leaf releases oxygen rather than taking it in. The "
                    "price of a higher rate is water."},
            {"text": "Chlorophyll used up for good.",
             "correct": False,
             "why": "Chlorophyll is not consumed by the reaction. The cost "
                    "every feature carries is water lost."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-02-s14",
        "band": "standard",
        "text": "Some plants carry a thick felt of tiny hairs over the "
                "underside of each leaf. Suggest what that does for the "
                "plant.",
        "options": [
            {"text": "The hairs catch the light that the palisade cells have "
                     "missed, and pass it back up to them.",
             "correct": False,
             "why": "Hairs are not green and photosynthesise nothing, and "
                    "they are on the shaded side anyway. Their subject is the "
                    "air next to the leaf."},
            {"text": "The hairs soak up rain and dew, which is how the leaf "
                     "takes in the water that it needs.",
             "correct": False,
             "why": "A leaf does not drink through its surface; water comes "
                    "up the xylem from the roots. Hairs slow the water going "
                    "the other way."},
            {"text": "The hairs hold the stomata open, so that carbon dioxide "
                     "can get in more easily.",
             "correct": False,
             "why": "Stomata are opened and closed by their guard cells, not "
                    "propped by hairs. The hairs cut water loss by keeping "
                    "the air next to the leaf still."},
            {"text": "The hairs hold a layer of still damp air against the "
                     "surface, so less water escapes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s15",
        "band": "standard",
        "text": "On most leaves the waxy cuticle is noticeably thicker on the "
                "upper surface than on the lower one. Explain why.",
        "options": [
            {"text": "The upper surface has to be tough enough to take the "
                     "weight of rain falling on it.",
             "correct": False,
             "why": "Raindrops do a leaf no damage worth building against. "
                    "The top is waxed more heavily because it is the hotter, "
                    "sunnier side."},
            {"text": "The upper surface carries the stomata, and each needs a "
                     "wax seal.",
             "correct": False,
             "why": "The stomata are mostly on the underside, and a pore is "
                    "closed by guard cells rather than sealed with wax. The "
                    "top is waxier because it is in the sun."},
            {"text": "The upper surface is the sunlit one, so water would "
                     "evaporate from it fastest.",
             "correct": True},
            {"text": "The upper surface must be waterproofed so that rain "
                     "cannot soak in and swell the cells.",
             "correct": False,
             "why": "Leaves do not take water in through their surfaces "
                    "either way. The wax is there to stop water getting out, "
                    "and it goes out fastest in the sun."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s16",
        "band": "standard",
        "text": "At midday on a hot dry afternoon many plants close their "
                "stomata. Predict what that does to the water lost and to the "
                "rate of photosynthesis.",
        "options": [
            {"text": "The water loss drops sharply and the rate holds up, "
                     "since light is still falling on the leaf.",
             "correct": False,
             "why": "Light alone is not enough. With the holes shut the "
                    "carbon dioxide stops arriving, so the rate falls as "
                    "well."},
            {"text": "The water loss holds up and the rate drops, since water "
                     "still goes out through the cuticle.",
             "correct": False,
             "why": "Very little crosses the wax; that is the point of it. "
                    "Closing the holes is what cuts the water loss right "
                    "down."},
            {"text": "Both rise, since a closed leaf keeps its carbon dioxide "
                     "in where the cells can use it.",
             "correct": False,
             "why": "The cells use up the gas already inside within minutes, "
                    "and shutting the holes stops any more arriving. Both "
                    "readings fall."},
            {"text": "Both drop — the plant is buying water at the price of "
                     "the carbon dioxide it shuts out.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s17",
        "band": "standard",
        "text": "A bedding plant with damp soil around its roots still wilts "
                "on a hot bright afternoon and recovers by the evening. "
                "Explain that.",
        "options": [
            {"text": "The soil water is too cold to be taken up until the "
                     "afternoon has warmed it through.",
             "correct": False,
             "why": "Roots take up cool water perfectly well. What happens at "
                    "midday is that the leaves lose it faster than the roots "
                    "can supply it."},
            {"text": "The plant loses water faster than its roots can supply "
                     "it, and catches up once the afternoon cools.",
             "correct": True},
            {"text": "The plant has stopped photosynthesising, so it no "
                     "longer needs water.",
             "correct": False,
             "why": "It is the other way round: wilting is what stops the "
                    "photosynthesis. The wilt comes from losing water faster "
                    "than it arrives."},
            {"text": "The heat has damaged the roots, and they grow back "
                     "again during the cool of the night.",
             "correct": False,
             "why": "Roots in damp soil are not harmed by a warm afternoon, "
                    "and they do not regrow overnight. The leaves were simply "
                    "outrunning the supply."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s18",
        "band": "standard",
        "text": "A thick fleshy leaf holds far more chloroplasts per square "
                "centimetre than a thin one, and yet it photosynthesises more "
                "slowly. Explain that.",
        "options": [
            {"text": "Light is absorbed on its way down, and carbon dioxide "
                     "arrives slowly, so the deep chloroplasts add little.",
             "correct": True},
            {"text": "A thick leaf has no stomata, so no carbon dioxide "
                     "reaches any of the chloroplasts inside it.",
             "correct": False,
             "why": "Thick leaves have stomata like any other. The trouble is "
                    "how far the gas has to travel once it is in, and how "
                    "little light gets down there."},
            {"text": "Chloroplasts crowded together get in each other's way "
                     "and each works more slowly.",
             "correct": False,
             "why": "Chloroplasts do not interfere with one another. What "
                    "limits the deep ones is the light reaching them and the "
                    "gas arriving."},
            {"text": "A fleshy leaf is full of stored water, and water "
                     "between the cells slows the reaction inside them down.",
             "correct": False,
             "why": "Water is a raw material rather than an obstacle. The "
                    "reason is that light and carbon dioxide both run short "
                    "deep inside a thick leaf."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s19",
        "band": "standard",
        "text": "The air spaces in a leaf are in the middle layer rather than "
                "in the layer just under the top surface. Suggest why they "
                "are put there.",
        "options": [
            {"text": "Air spaces at the top would let the rain in, and the "
                     "cells beneath would be soaked every time it fell.",
             "correct": False,
             "why": "The spaces are inside the leaf and open only at the "
                    "stomata, so rain does not enter them. The reason is "
                    "about light."},
            {"text": "Air spaces at the top would freeze in winter, and the "
                     "ice would split the cells around them open.",
             "correct": False,
             "why": "A broad leaf is dropped before winter in any case. The "
                    "spaces are lower down because the top is where the light "
                    "is."},
            {"text": "The top layer is the brightest, so it is worth filling "
                     "with packed cells rather than with gaps.",
             "correct": True},
            {"text": "Air spaces at the top would blow away in the wind, and "
                     "the leaf would collapse flat as they went.",
             "correct": False,
             "why": "The spaces are enclosed inside the blade and cannot blow "
                    "anywhere. They sit below the layer that is worth packing "
                    "with cells."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s20",
        "band": "standard",
        "text": "A leaf's veins hold two separate sets of tubes rather than "
                "one set doing both jobs. Suggest why the plant needs two.",
        "options": [
            {"text": "Two sets can be repaired one at a time, so a damaged "
                     "leaf is never cut off from the rest of the plant.",
             "correct": False,
             "why": "Plants do not repair veins like that. Two sets are "
                    "needed because two different things are travelling, in "
                    "opposite directions."},
            {"text": "One set is for daytime and the other takes over at "
                     "night, when the leaf is working the other way round.",
             "correct": False,
             "why": "Both run at any hour. They are separate because water "
                    "comes up and dissolved sugar goes out, which is two "
                    "journeys."},
            {"text": "The two sets carry different things in opposite "
                     "directions — water up, dissolved sugar away.",
             "correct": True},
            {"text": "One set carries the water and the other carries the "
                     "gases, which are kept well apart.",
             "correct": False,
             "why": "Gases travel through the air spaces and never enter a "
                    "vein. The second set of tubes is carrying dissolved "
                    "sugar out of the leaf."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s21",
        "band": "standard",
        "text": "A pot plant left on a windowsill turns its leaves until they "
                "face the glass. What does the plant gain, and what does it "
                "cost?",
        "options": [
            {"text": "It gains warmth from the glass, and it costs the plant "
                     "nothing to turn a leaf.",
             "correct": False,
             "why": "The gain is light rather than heat. And a leaf facing "
                    "the light squarely also loses water fastest, so the move "
                    "has a price."},
            {"text": "It gains carbon dioxide, which is thicker near a cold "
                     "window, and it costs the plant some of its light.",
             "correct": False,
             "why": "Carbon dioxide does not gather at a window. Turning to "
                    "the glass is about light, and it is paid for in water."},
            {"text": "It gains nothing measurable, since a leaf intercepts "
                     "just the same light whichever way round it happens "
                     "to be facing.",
             "correct": False,
             "why": "A blade facing the light squarely intercepts far more "
                    "than one edge-on to it. That is why the plant bothers to "
                    "turn."},
            {"text": "It gains more light on each blade, and pays for it in "
                     "water, since a lit leaf loses fastest.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s22",
        "band": "standard",
        "text": "Salt marsh plants stand in water all day, but the salt in it "
                "makes that water hard to take up. Which leaf would you "
                "expect on one, and why?",
        "options": [
            {"text": "A broad thin leaf, because there is water all around it "
                     "and no reason to be careful with any of it.",
             "correct": False,
             "why": "Water being present is not the same as water being "
                    "available. A salt marsh plant can take up very little, "
                    "so it must spend very little."},
            {"text": "A thick waxy leaf, because water is hard to replace "
                     "even though there is plenty of it about.",
             "correct": True},
            {"text": "A leaf with extra stomata, because the salt has to be "
                     "let out through the holes somewhere.",
             "correct": False,
             "why": "Stomata handle gases, and extra holes would spend more "
                    "water than the plant can replace. The leaf to expect is "
                    "a thick waxy one."},
            {"text": "A leaf with no cuticle, because the wax would stop the "
                     "salt water reaching the cells inside.",
             "correct": False,
             "why": "Water reaches the cells through the roots and the xylem, "
                    "not through the leaf's surface. Losing the wax would "
                    "only spend water faster."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s23",
        "band": "standard",
        "text": "A gardener takes a cutting with six large leaves on it and "
                "cuts three of them off before planting it. Explain that.",
        "options": [
            {"text": "Three fewer leaves means less shade on the soil, so the "
                     "cutting's new roots are warmer while they grow.",
             "correct": False,
             "why": "Soil temperature is not what is at stake. A cutting has "
                    "no roots yet, so what matters is how fast the leaves are "
                    "spending its water."},
            {"text": "Cut leaves release a substance into the soil that makes "
                     "roots grow out of the bottom of the stem faster.",
             "correct": False,
             "why": "Nothing useful is released by cutting a leaf off. The "
                    "reason is that fewer leaves lose less water while the "
                    "cutting has no roots."},
            {"text": "A cutting has no roots yet, so the leaf area left on it "
                     "has to be small enough not to dry it out.",
             "correct": True},
            {"text": "Leaves would use up the cutting's store of food.",
             "correct": False,
             "why": "Photosynthesis adds to a plant's store rather than "
                    "spending it. Leaves are removed because of the water "
                    "they lose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s24",
        "band": "standard",
        "text": "The air spaces inside a leaf take up room that could have "
                "held more photosynthesising cells. Explain why the plant "
                "gives that room up.",
        "options": [
            {"text": "Extra cells could not be fed, but the spaces let carbon "
                     "dioxide reach the cells that are already there.",
             "correct": True},
            {"text": "The spaces make the leaf lighter, so the stem can hold "
                     "more blade out.",
             "correct": False,
             "why": "Weight is a small matter beside gas supply. The spaces "
                    "are the route carbon dioxide takes to cells nowhere near "
                    "a hole."},
            {"text": "The spaces hold a store of oxygen, which the leaf falls "
                     "back on whenever the light fails.",
             "correct": False,
             "why": "Oxygen is what the leaf gives out rather than stockpiles. "
                    "The spaces are a route for gas, not a container."},
            {"text": "The spaces stop the leaf overheating, since air carries "
                     "heat away much faster than packed cells can.",
             "correct": False,
             "why": "Still air is a poor carrier of heat, and cooling is not "
                    "the job here. The spaces exist so gas can reach every "
                    "cell."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s25",
        "band": "standard",
        "text": "Leaves grown in deep shade carry fewer stomata per square "
                "millimetre than leaves of the same species grown in full "
                "sun. Suggest why.",
        "options": [
            {"text": "A shaded leaf cannot photosynthesise as fast anyway, so "
                     "it needs less gas and can afford fewer leaks.",
             "correct": True},
            {"text": "A shaded leaf is colder, and cold leaves grow no "
                     "stomata.",
             "correct": False,
             "why": "Temperature does not decide where holes are built. A "
                    "shaded leaf simply cannot use as much gas, so it needs "
                    "fewer ways in."},
            {"text": "A shaded leaf loses no water at all, so there would be "
                     "nothing for extra stomata to do on it.",
             "correct": False,
             "why": "A shaded leaf still loses water, only more slowly. What "
                    "settles the number of holes is how much gas the leaf can "
                    "actually use."},
            {"text": "A shaded leaf takes its carbon dioxide in through its "
                     "upper surface instead, so fewer holes are wanted "
                     "underneath.",
             "correct": False,
             "why": "Gas comes in through the stomata wherever a leaf grows. "
                    "The count is lower because a shaded leaf works more "
                    "slowly."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s26",
        "band": "standard",
        "text": "A student suggests that a plant in a dry place should simply "
                "keep all its stomata shut and carry on photosynthesising. "
                "What is wrong with that?",
        "options": [
            {"text": "Shut stomata let no carbon dioxide in, and the "
                     "reaction stops without it however bright the light is.",
             "correct": True},
            {"text": "Shut stomata would starve the leaf of the oxygen it "
                     "needs for photosynthesis, so the reaction would stop.",
             "correct": False,
             "why": "Oxygen is what photosynthesis releases, not what it "
                    "uses. The gas that stops arriving is carbon dioxide."},
            {"text": "Shut stomata would trap water inside the leaf until the "
                     "pressure split the cells open from within.",
             "correct": False,
             "why": "A plant closes its stomata routinely and comes to no "
                    "harm. The cost of closing them is that the gas supply is "
                    "cut off."},
            {"text": "Shut stomata would keep the light out as well, since a "
                     "closed pore darkens the whole surface of the leaf.",
             "correct": False,
             "why": "Stomata are tiny holes and let in no measurable light. "
                    "Closing them cuts off the carbon dioxide, which is what "
                    "stops the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s27",
        "band": "standard",
        "text": "A leaf whose waxy surface has been rubbed away with a cloth "
                "wilts much sooner than an untouched one beside it. Explain "
                "the difference.",
        "options": [
            {"text": "Without the wax the leaf can no longer take up the "
                     "water its roots are sending, so it dries from the top "
                     "down.",
             "correct": False,
             "why": "The wax has nothing to do with taking water up; the "
                    "xylem does that. Without it, water evaporates straight "
                    "off the leaf's surface."},
            {"text": "Without the wax, water evaporates straight from the "
                     "leaf's surface as well as through the stomata.",
             "correct": True},
            {"text": "Without the wax the stomata are stuck open, so the leaf "
                     "cannot close them however dry it becomes.",
             "correct": False,
             "why": "Guard cells work whether the surface is waxed or not. "
                    "The loss is coming through the bare surface itself."},
            {"text": "Without the wax the leaf absorbs far more sunlight, and "
                     "the heat is what dries the cells out from inside.",
             "correct": False,
             "why": "A clear wax layer changes the light very little. What it "
                    "changes is how fast water crosses the surface."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s28",
        "band": "standard",
        "text": "A houseplant moved from a dim corner to a bright windowsill "
                "grows new leaves that are smaller and thicker than the old "
                "ones. Explain that change.",
        "options": [
            {"text": "Bright light damages a large blade, so the plant builds "
                     "smaller ones that the sun cannot reach all of.",
             "correct": False,
             "why": "The sun reaches all of a small leaf just as easily. The "
                    "change is about what the plant needs and what it can "
                    "afford to spend."},
            {"text": "Light is plentiful now, so a large thin blade is no "
                     "longer worth the water it would cost.",
             "correct": True},
            {"text": "The windowsill is warmer, and a warm leaf grows thicker "
                     "because its cells expand as they are built.",
             "correct": False,
             "why": "Cells are not swollen into shape by warmth. The plant is "
                    "building the leaf that suits plenty of light and a "
                    "higher water bill."},
            {"text": "A bright windowsill holds less carbon dioxide than a "
                     "dim corner.",
             "correct": False,
             "why": "There is as much carbon dioxide at a window as anywhere "
                    "else in the room. What has changed is the light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s29",
        "band": "standard",
        "text": "A leaf's blade is usually held out at right angles to the "
                "light rather than edge-on to it. Explain what that gains.",
        "options": [
            {"text": "It keeps both surfaces at the same temperature, so the "
                     "cells inside work at one steady rate all day.",
             "correct": False,
             "why": "The two surfaces are at different temperatures whatever "
                    "the angle. Facing the light is about how much of it the "
                    "blade catches."},
            {"text": "It points the stomata straight down, which is where "
                     "they work.",
             "correct": False,
             "why": "A stoma opens whichever way it is pointing — think of a "
                    "water lily's, which face upwards. The angle is about "
                    "light."},
            {"text": "It lets rain run off the middle of the blade instead of "
                     "collecting in it and weighing the leaf down.",
             "correct": False,
             "why": "A leaf held flat is the one that collects rain, so this "
                    "is backwards. The blade faces the light because that is "
                    "what it is for."},
            {"text": "It intercepts the most light for the tissue the plant "
                     "spent on building it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-s30",
        "band": "standard",
        "text": "To measure how much water a potted plant loses through its "
                "leaves, a student seals the pot and its soil inside a "
                "plastic bag before weighing it. Why seal the soil?",
        "options": [
            {"text": "So that water evaporating from the soil is not counted "
                     "as water lost by the leaves.",
             "correct": True},
            {"text": "So that the roots cannot take up any more water while "
                     "the measurement is being made.",
             "correct": False,
             "why": "The roots must go on supplying the leaves, or there is "
                    "nothing to measure. The bag is there to keep the soil's "
                    "own losses out of the reading."},
            {"text": "So that the carbon dioxide around the pot is kept away "
                     "from the leaves during the run.",
             "correct": False,
             "why": "The leaves are outside the bag and take in gas as usual. "
                    "The bag stops the soil's evaporation being counted."},
            {"text": "So that the soil stays at one temperature for the whole "
                     "of the measurement.",
             "correct": False,
             "why": "A bag does very little to the temperature. It stops "
                    "water evaporating from the soil and spoiling the "
                    "reading."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-02-h14",
        "band": "harder",
        "text": "Some desert plants keep their stomata shut through the whole "
                "day and open them only at night, storing the carbon dioxide "
                "they take in until morning. Evaluate that strategy against "
                "the rate of photosynthesis and the water lost.",
        "options": [
            {"text": "It saves an enormous amount of water, because a hole "
                     "open at night in cool air loses far less than one open "
                     "at midday.",
             "correct": True},
            {"text": "It saves water and costs nothing, because carbon "
                     "dioxide is more plentiful in the cool air of the night "
                     "than it is by day.",
             "correct": False,
             "why": "The air holds the same carbon dioxide at any hour, and "
                     "there are no free moves in a desert. What this plant "
                     "buys with its water saving is a slower rate."},
            {"text": "It raises the rate, because the plant can then "
                     "photosynthesise right through the night as well as "
                     "through the day.",
             "correct": False,
             "why": "Photosynthesis needs light and stops when it is dark. "
                    "Only the gas collection happens at night; the reaction "
                    "still waits for the morning."},
            {"text": "It makes no difference to either figure, because a "
                     "stoma loses the same water whenever in the day it "
                     "happens to be opened.",
             "correct": False,
             "why": "Cool damp night air draws water out of an open hole far "
                    "more slowly than hot dry afternoon air does. The saving "
                    "is real and large."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h15",
        "band": "harder",
        "text": "Plants grown in air with extra carbon dioxide in it develop "
                "fewer stomata per square millimetre than the same species "
                "grown in ordinary air. Explain that result.",
        "options": [
            {"text": "Extra carbon dioxide blocks some of the pores as they "
                     "form, so fewer of them ever open.",
             "correct": False,
             "why": "Nothing is blocked. With more gas outside, fewer holes "
                    "bring in as much, so the plant can build fewer and spend "
                    "less water."},
            {"text": "Extra carbon dioxide makes the leaves grow larger, and "
                     "the same number of holes then sits in more space.",
             "correct": False,
             "why": "A count per square millimetre already allows for the "
                    "size of the leaf. The plant really is building fewer "
                    "holes."},
            {"text": "Extra carbon dioxide raises the rate so far that the "
                     "leaf runs short of water and stops building holes.",
             "correct": False,
             "why": "A plant short of water still builds leaves with stomata. "
                    "This is a settlement rather than a failure: fewer holes "
                    "are needed, so fewer are made."},
            {"text": "Fewer holes will bring in as much gas when there is "
                     "more of it outside, so the plant saves water by "
                     "building fewer.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h16",
        "band": "harder",
        "text": "Leaf A photosynthesises at 50% of an oak leaf's rate while "
                "losing 40% of an oak leaf's water; leaf B is at 100% of "
                "both. Which spends less water for each unit of "
                "photosynthesis, and by how much?",
        "options": [
            {"text": "Leaf B, because 100% is the bigger rate, and the faster "
                     "leaf is the better one.",
             "correct": False,
             "why": "Speed and efficiency are different questions. Divide "
                    "water by rate: A spends 0.8 and B spends 1.0, so A is "
                    "the thriftier."},
            {"text": "Leaf A, because 40 divided by 50 is 0.8 against leaf "
                     "B's 1.0.",
             "correct": True},
            {"text": "Leaf B, because 100 minus 100 is nothing, while "
                     "leaf A is 10 percentage points behind on its water.",
             "correct": False,
             "why": "Subtracting the two figures compares nothing useful. The "
                    "measure wanted is water divided by rate, which comes out "
                    "at 0.8 for A and 1.0 for B."},
            {"text": "Neither — they spend the same, since leaf A is behind "
                     "on both figures by roughly the same sort of amount.",
             "correct": False,
             "why": "Roughly is not enough here. A's water falls further than "
                    "its rate does, so A gets more photosynthesis per unit of "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h17",
        "band": "harder",
        "text": "Two leaves off the same plant have the same mass, but one "
                "has twice the surface area of the other. Which is the "
                "thinner, and which would do better in dim light?",
        "options": [
            {"text": "The wider one is thinner, and the narrower one does "
                     "better in dim light because it holds more chloroplasts "
                     "in each square centimetre of blade.",
             "correct": False,
             "why": "Chloroplasts deep in a thick leaf sit in dim light "
                    "already. In poor light the leaf that wins is the one "
                    "catching the most of it."},
            {"text": "The wider one is thicker, since spreading the same mass "
                     "further means piling it up rather than flattening it "
                     "out.",
             "correct": False,
             "why": "Spreading the same mass over twice the area makes it "
                    "half as deep. The wider leaf is the thinner of the two."},
            {"text": "They are the same thickness, since two leaves off one "
                     "plant are built to one pattern.",
             "correct": False,
             "why": "Equal mass over unequal area means unequal thickness. "
                    "The wider leaf must be thinner."},
            {"text": "The wider one is thinner, and it does better in dim "
                     "light because it intercepts more of what there is.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h18",
        "band": "harder",
        "text": "A sealed glass terrarium with a plant in it is watered once "
                "and then closed, and the plant lives for years. Explain how "
                "the plant manages its water.",
        "options": [
            {"text": "The plant has stopped losing water, because a sealed jar "
                     "holds its stomata shut.",
             "correct": False,
             "why": "Nothing holds a stoma shut, and the plant goes on losing "
                    "water. What it loses condenses on the glass and returns "
                    "to the soil."},
            {"text": "The plant makes its own water, since water is one of "
                     "the two things photosynthesis produces from carbon "
                     "dioxide.",
             "correct": False,
             "why": "Photosynthesis uses water up; its products are glucose "
                    "and oxygen. Inside the jar the water is being recycled "
                    "rather than made."},
            {"text": "Water lost from the leaves condenses on the glass and "
                     "runs back to the soil, so the same water is used again "
                     "and again.",
             "correct": True},
            {"text": "The glass stops water evaporating out of the leaves at "
                     "all, because the air inside cannot move about.",
             "correct": False,
             "why": "Evaporation carries on in still air, only more slowly. "
                    "What keeps the jar going is that the water cannot "
                    "escape."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h19",
        "band": "harder",
        "text": "Plant breeders have bred wheat with narrow leaves held "
                "nearly upright instead of broad ones held flat, and a dense "
                "field of it yields more. Suggest why.",
        "options": [
            {"text": "Upright leaves catch the wind better, and moving air "
                     "brings each plant more of the carbon dioxide it "
                     "needs.",
             "correct": False,
             "why": "Carbon dioxide is not what limits a wheat field on a "
                    "bright day. Upright blades let light down to the leaves "
                    "below instead of stopping it at the top."},
            {"text": "Upright leaves let light down to the leaves lower in "
                     "the crop, so more of the field's leaf area is working.",
             "correct": True},
            {"text": "Upright leaves lose less water, and a crop that is "
                     "never short of water grows at the fastest rate it "
                     "possibly can.",
             "correct": False,
             "why": "They do lose somewhat less, and that is not where the "
                    "extra yield comes from. It comes from lighting the lower "
                    "leaves rather than shading them."},
            {"text": "Upright leaves are stronger, so the crop stands up in "
                     "the rain and none of the grain is lost into the mud.",
             "correct": False,
             "why": "Standing up is worth having and is a separate matter. "
                    "The yield rises because the light reaches further down "
                    "into the crop."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h20",
        "band": "harder",
        "text": "A moss growing in a damp wall crevice has leaves one cell "
                "thick, with no cuticle, no stomata and no veins. Explain how "
                "it manages, and what it gives up.",
        "options": [
            {"text": "It gives up nothing, since a leaf one cell thick has "
                     "every cell in the light.",
             "correct": False,
             "why": "There are no designs that win everywhere. A moss cannot "
                    "leave its damp crevice, and it cannot grow tall without "
                    "veins."},
            {"text": "It manages because a moss photosynthesises without "
                     "needing carbon dioxide, and it gives up the ability to "
                     "make its own sugars.",
             "correct": False,
             "why": "A moss is green and photosynthesises exactly as a leaf "
                    "does, gas and all. What it lacks is the plumbing and the "
                    "waterproofing."},
            {"text": "It manages because the damp wall supplies both its "
                     "water and its food through the crevice, and so it gives "
                     "up the need to photosynthesise.",
             "correct": False,
             "why": "A wall supplies no food, and moss is green for a reason. "
                    "It takes water in over its whole surface and must stay "
                    "damp to do it."},
            {"text": "It manages because water and gas cross every cell "
                     "directly in a damp place, and it gives up being able to "
                     "live anywhere dry or grow tall.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h21",
        "band": "harder",
        "text": "A houseplant owner mists the leaves with a water spray every "
                "morning. What does that actually do, and what does it not "
                "do?",
        "options": [
            {"text": "It feeds the plant through the leaves, and it does "
                     "nothing to the water the plant is losing.",
             "correct": False,
             "why": "Water is a raw material rather than food, and a leaf "
                    "does not drink. What the mist does is make the air round "
                    "the leaf damp for a while."},
            {"text": "It damps the air round the leaf for a while, so water "
                     "leaves more slowly; it does not water the plant, which "
                     "still drinks through its roots.",
             "correct": True},
            {"text": "It washes the stomata clean so gas moves in and out of "
                     "them freely.",
             "correct": False,
             "why": "Stomata are not blocked by dust in any ordinary room. "
                    "The effect of the mist is on the damp of the air next to "
                    "the leaf."},
            {"text": "It fills the leaf through its surface, so the roots can "
                     "be left dry; it does not affect the rate of "
                     "photosynthesis.",
             "correct": False,
             "why": "Leaves do not take water in through their surfaces, and "
                    "a plant with dry roots will die. Misting only slows the "
                    "loss for a while."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h22",
        "band": "harder",
        "text": "A leaf carries about 300 stomata per square millimetre on "
                "its underside, and its blade is 40 cm2. About how many "
                "stomata does the underside carry altogether?",
        "options": [
            {"text": "About 12 000, since 40 multiplied by 300 gives 12 000.",
             "correct": False,
             "why": "You have used square centimetres as though they were "
                    "square millimetres. One square centimetre is 100 square "
                    "millimetres, so the blade is 4000 mm2."},
            {"text": "About 120 000, since 40 cm2 is 400 mm2 and 400 "
                     "multiplied by 300 gives 120 000.",
             "correct": False,
             "why": "There are 100 square millimetres in a square centimetre, "
                    "not 10. Forty square centimetres is 4000 mm2."},
            {"text": "About 1 200 000, since 40 cm2 is 4000 mm2 and 4000 "
                     "times 300 is 1 200 000.",
             "correct": True},
            {"text": "About 7.5, since 300 divided by 40 gives 7.5 stomata "
                     "for each square centimetre of blade.",
             "correct": False,
             "why": "Dividing gives a rate, not a total. To find how many "
                    "there are, multiply the number in each square millimetre "
                    "by the number of square millimetres."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h23",
        "band": "harder",
        "text": "A student designs the perfect leaf: enormous area, many "
                "stomata, a thick waxy cuticle and thin as paper. Which pair "
                "of those pull against each other hardest, and why?",
        "options": [
            {"text": "Thin and waxy, because wax cannot be laid over a "
                     "surface a fraction of a millimetre "
                     "through.",
             "correct": False,
             "why": "Every thin leaf carries a cuticle, so those two sit "
                    "together happily. The fight is between the features that "
                    "raise the rate and the water they spend."},
            {"text": "Enormous area and many stomata, because each of them "
                     "raises the rate and each of them pours water away.",
             "correct": True},
            {"text": "Enormous area and thin, because a very large blade "
                     "cannot be held out flat unless it is built thick enough "
                     "to be stiff.",
             "correct": False,
             "why": "The veins hold a broad thin blade out, which is one of "
                    "their jobs. The real conflict is between the rate and "
                    "the water bill."},
            {"text": "Many stomata and waxy, because the wax would have to be "
                     "broken to let a hole through it in the first place.",
             "correct": False,
             "why": "A waxed leaf with holes in it is the ordinary "
                    "arrangement — that is what every oak leaf is. The clash "
                    "is over water."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h24",
        "band": "harder",
        "text": "A leaf is altered in two ways at once: its thickness is "
                "doubled and its surface area is halved. Predict what happens "
                "to its rate of photosynthesis and to its water loss.",
        "options": [
            {"text": "Both of them fall, since each change on its own cuts "
                     "the rate and each cuts the water as well.",
             "correct": True},
            {"text": "The rate falls and the water rises, since a thick leaf "
                     "holds more water in it and therefore has more to lose.",
             "correct": False,
             "why": "Thickness buys water back rather than spending it, and "
                    "halving the area saves more again. Both readings go "
                    "down."},
            {"text": "The rate rises and the water falls, since doubling the "
                     "thickness doubles the chloroplasts while halving the "
                     "area halves the loss.",
             "correct": False,
             "why": "Extra chloroplasts deep in a thick leaf sit in dim light "
                    "and add little, so the rate falls. The area cut takes it "
                    "down further."},
            {"text": "Neither moves, since the two changes are opposites and "
                     "cancel each other out exactly.",
             "correct": False,
             "why": "They are not opposites — both a thicker leaf and a "
                    "smaller one cut the rate. They pull the same way, not "
                    "against each other."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h25",
        "band": "harder",
        "text": "A crop raised in a still, very humid glasshouse grows thin "
                "leaves with a light cuticle and plenty of stomata. Predict "
                "what happens when it is planted out into an open field.",
        "options": [
            {"text": "It grows faster outdoors, because there is more light "
                     "in a field than under glass and light is what sets the "
                     "rate.",
             "correct": False,
             "why": "Light does rise, and so does the water bill. Leaves "
                    "built for still damp air wilt in moving dry air before "
                    "the extra light can pay."},
            {"text": "It does much the same outdoors, since a grown leaf "
                     "ignores the air around it.",
             "correct": False,
             "why": "How fast water leaves a leaf depends a great deal on the "
                    "air outside it. Dry moving air pulls water out far "
                    "faster than still damp air."},
            {"text": "It suffers, because leaves built for still damp air "
                     "lose water far too fast in dry moving air.",
             "correct": True},
            {"text": "It suffers, because a field holds much less carbon "
                     "dioxide than a sealed glasshouse does and the leaves go "
                     "short of it.",
             "correct": False,
             "why": "Outdoor air holds carbon dioxide and is constantly "
                    "replaced. The problem is the water leaving those thin "
                    "unwaxed leaves."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h26",
        "band": "harder",
        "text": "A student proposes a desert leaf with no stomata at all, "
                "reasoning that it would lose no water whatever. Evaluate "
                "that proposal.",
        "options": [
            {"text": "It would work, because a leaf can take its carbon "
                     "dioxide straight through the cuticle once it has no "
                     "holes to use.",
             "correct": False,
             "why": "Gases do not cross the waxy cuticle, which is why the "
                    "holes exist at all. A leaf without them is sealed to the "
                    "gas as well as to the water."},
            {"text": "It would work, because a leaf without stomata makes its "
                     "carbon dioxide from the water arriving up the xylem "
                     "from the roots.",
             "correct": False,
             "why": "Nothing makes carbon dioxide inside a leaf; it has to "
                    "come in from the air. Without stomata there is no way in "
                    "for it."},
            {"text": "It fails: no holes means no carbon dioxide, and a leaf "
                     "with no gas coming in cannot photosynthesise at all.",
             "correct": True},
            {"text": "It fails, because the water arriving from the roots "
                     "would then have no way out of the leaf, and the "
                     "cells would swell.",
             "correct": False,
             "why": "A plant can slow its uptake and comes to no such harm. "
                    "What kills the idea is that the carbon dioxide has no "
                    "way in."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h27",
        "band": "harder",
        "text": "A newly transplanted shrub has lost about half its roots. It "
                "wilts badly on a bright breezy day and looks fine on a dull "
                "still one. Explain the difference between the two days.",
        "options": [
            {"text": "On the bright day the leaves photosynthesise fast, and "
                     "the sugar they make draws all the water out of the "
                     "cells and into the phloem.",
             "correct": False,
             "why": "Sugar leaving in the phloem does not empty the leaf of "
                    "water. The wilt comes from water leaving through the "
                    "stomata faster than it arrives."},
            {"text": "On the dull day the roots have grown back, and by the "
                     "next bright day they will have been lost again.",
             "correct": False,
             "why": "Roots do not come and go between one day and the next. "
                    "What changes is how fast the leaves are spending water."},
            {"text": "On the bright day the soil is warmer, and warm soil "
                     "holds its water tightly enough that no root can pull "
                     "any of it free.",
             "correct": False,
             "why": "Warm soil gives up water perfectly well. The problem is "
                    "the rate of loss from the leaves against a root system "
                    "half the size it should be."},
            {"text": "On the bright day the leaves lose water fast, and half "
                     "a root system cannot supply it that quickly.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h28",
        "band": "harder",
        "text": "Adding a thick waxy cuticle to a leaf takes it from 100% "
                "rate and 100% water loss to 90% rate and 60% water loss. Is "
                "that a good trade on a dry hillside, and why?",
        "options": [
            {"text": "No, because any fall in the rate is a loss, and a plant "
                     "that photosynthesises more slowly must always grow more "
                     "slowly than its neighbours.",
             "correct": False,
             "why": "On a dry hillside the water bill decides who survives "
                    "the summer. A tenth off the rate for two fifths off the "
                    "water is a good bargain there."},
            {"text": "Yes: the water falls by 40 while the rate falls by 10, "
                     "so each unit of photosynthesis now costs 0.67 instead "
                     "of 1.0.",
             "correct": True},
            {"text": "Yes, because a thick cuticle raises the rate as well, "
                     "and a leaf that keeps its water in is a leaf that can "
                     "run its reaction faster.",
             "correct": False,
             "why": "The rate falls to 90, as the figures say. The trade is "
                    "worth it despite that, not because the rate went up."},
            {"text": "No, because 60 is still more than half of the water the "
                     "leaf was losing before the wax went on.",
             "correct": False,
             "why": "Compare the two falls rather than judging one of them "
                    "alone. Water per unit of photosynthesis drops from 1.0 "
                    "to about 0.67, which is a large gain."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h29",
        "band": "harder",
        "text": "A student writes that a leaf is thin so that light can pass "
                "through it to the leaves below. Evaluate that explanation.",
        "options": [
            {"text": "It is right, and it is the main reason a plant builds "
                     "thin leaves.",
             "correct": False,
             "why": "A leaf absorbs most of the light that hits it, which is "
                    "why the ground under a tree is dark. Thinness is about "
                    "the distances inside the leaf."},
            {"text": "It is wrong: a leaf absorbs most of the light it "
                     "receives, and thinness is about how far gases and light "
                     "must travel inside it.",
             "correct": True},
            {"text": "It is wrong, because a leaf is not really thin — half a "
                     "millimetre is a considerable depth for a single cell to "
                     "look through.",
             "correct": False,
             "why": "Half a millimetre is genuinely thin, and the thinness is "
                    "real and deliberate. What is wrong is the reason given "
                    "for it."},
            {"text": "It is right, because the leaves lower on a plant have "
                     "no stomata of their own and are fed entirely by the "
                     "light coming through from above.",
             "correct": False,
             "why": "Lower leaves carry stomata and photosynthesise for "
                    "themselves. And a leaf lets very little light through, "
                    "which is why a wood floor is shaded."},
        ],
        "figure": None,
    },
    {
        "id": "b7-02-h30",
        "band": "harder",
        "text": "A leaf is traced onto paper ruled in 1 cm squares. It covers "
                "46 whole squares, and 22 squares are part covered. Estimate "
                "its area, and say why the figure is an estimate.",
        "options": [
            {"text": "About 57 cm2, counting each part square as half a "
                     "square — and how much of each is covered is a "
                     "judgement.",
             "correct": True},
            {"text": "About 68 cm2, counting every part square as a whole one "
                     "— and tracing round a curved edge is a rough job.",
             "correct": False,
             "why": "Counting every part square whole overestimates every "
                    "time, since most are less than full. Half of each is the "
                    "usual compromise, giving about 57 cm2."},
            {"text": "About 46 cm2, counting just the squares that are fully "
                     "covered — and the leaf may have curled while it was "
                     "being drawn round.",
             "correct": False,
             "why": "Ignoring the part squares throws away real leaf area. "
                    "Counting each of them as half gives about 57 cm2."},
            {"text": "About 1012 cm2, multiplying the 46 whole squares by the "
                     "22 part ones — and the pencil line adds a little to "
                     "every edge.",
             "correct": False,
             "why": "Multiplying two counts of squares gives no area at all. "
                    "Add them, with the part squares counted as half: about "
                    "57 cm2."},
        ],
        "figure": None,
    },
]
