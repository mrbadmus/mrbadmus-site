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
]
