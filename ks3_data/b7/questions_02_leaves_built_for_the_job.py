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
]
