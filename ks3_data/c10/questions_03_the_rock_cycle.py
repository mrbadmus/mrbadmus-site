"""C10 lesson 03 — The rock cycle: twelve questions (MRB-281).

The lesson's argument is one shape: any rock type can become any other, the
route is decided by WHERE THE ROCK ENDS UP rather than by which type it is
now, and the cycle has no starting point, no fixed direction and no timetable.
The page teaches it with a seven-stage sequencer and six process arrows.

These twelve probe the angles the mastery ladder leaves alone: where the cycle
begins, what a rounded pebble is evidence of, what happens to a metamorphic
rock that reaches the surface, what a rock that melts loses, why the diagram
has arrows across the middle, and how "almost none of the original crust
survives" sits beside "four-billion-year-old rocks are still found".

The distractors are built from the lesson's declared misconceptions.

`EARTH-08` (the cycle goes round one way, like a clock) drives the wrong
options in e01, s01, h01 and h04. Each treats the drawn ring as a rule.

`EARTH-09` (every rock must pass through every stage in turn) drives e03, s02,
s03 and h02. Each has a rock skipping a stage, or acting on any rock at all.

`EARTH-10` (a rock is a permanent thing) drives e02, e04, s04 and h03. Each
offers a way to keep the rock fixed and move something else instead.

⚠️ **NO QUESTION ASKS FOR A LIST OF PROCESSES TO BE RECALLED IN ORDER.** The
sequencer on the page is one grain's journey, never the order every rock
takes, and a bank question that rewards reciting seven stages would teach
back exactly the belief `#s-think` exists to break. Every question below asks
what decides a route, not what comes next.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles through each
band — 2,0,3,1 · 1,3,0,2 · 0,2,1,3 — so this file holds three of each. The
ladder is a separate corpus and is balanced separately; see the lesson record.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "the-rock-cycle"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-03-e01",
        "band": "easier",
        "text": "Where does the rock cycle begin?",
        "options": [
            {"text": "With igneous rock, because the whole Earth was molten "
                     "to start with",
             "correct": False,
             "why": "The Earth was molten once, but the cycle running today "
                    "has been turning for billions of years and has no first "
                    "step left in it."},
            {"text": "With weathering, because that is the first arrow drawn "
                     "on most diagrams",
             "correct": False,
             "why": "Where an arrow is printed on a page is a fact about the "
                    "diagram, not about the rock."},
            {"text": "Nowhere — the cycle has no beginning",
             "correct": True},
            {"text": "With sedimentary rock, because that is the type that "
                     "holds the fossils",
             "correct": False,
             "why": "Fossils tell you how a rock formed. They do not make it "
                    "the start of anything."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e02",
        "band": "easier",
        "text": "Marine fossils are found in the rock near the summit of "
                "Everest. What is the best explanation?",
        "options": [
            {"text": "Rock that formed on a sea floor was lifted to that "
                     "height",
             "correct": True},
            {"text": "The sea was once high enough to cover the mountain",
             "correct": False,
             "why": "Sea level has never been eight kilometres higher than "
                    "it is now. It is the rock that moved, not the water."},
            {"text": "The fossils were carried up there and left in the rock "
                     "later",
             "correct": False,
             "why": "The shells are inside the limestone, and the limestone "
                    "formed around them on a sea floor."},
            {"text": "Limestone can form high on a mountain as well as on a "
                     "sea floor",
             "correct": False,
             "why": "Limestone is built from the remains of sea creatures, "
                    "so it forms where they lived."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e03",
        "band": "easier",
        "text": "Which process breaks rock at the surface down into loose "
                "fragments, without carrying them anywhere?",
        "options": [
            {"text": "Deposition",
             "correct": False,
             "why": "Deposition is sediment being dropped when the water or "
                    "wind carrying it slows down."},
            {"text": "Compaction",
             "correct": False,
             "why": "Compaction squeezes sediment that has already been "
                    "dropped, turning it into solid rock."},
            {"text": "Metamorphism",
             "correct": False,
             "why": "Metamorphism changes a buried rock by heat and "
                    "pressure. It happens deep, not at the surface."},
            {"text": "Weathering",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e04",
        "band": "easier",
        "text": "A pebble on a beach is smooth and rounded. What made it "
                "that shape?",
        "options": [
            {"text": "It grew into that shape as the rock formed",
             "correct": False,
             "why": "Rock does not grow into a shape. A pebble is a broken "
                    "piece of something bigger."},
            {"text": "It was knocked about while water carried it",
             "correct": True},
            {"text": "The sea dissolved its corners away",
             "correct": False,
             "why": "Sea water dissolves some minerals slowly, but what "
                    "rounds a pebble is being tumbled against other rock."},
            {"text": "Heat and pressure smoothed it underground",
             "correct": False,
             "why": "That is metamorphism, and it changes a rock's crystals "
                    "rather than its outside shape."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-03-s01",
        "band": "standard",
        "text": "A metamorphic rock is pushed up into a mountain and ends up "
                "exposed at the surface. What can happen to it next?",
        "options": [
            {"text": "It must melt, because melting is the only way out of "
                     "the metamorphic stage",
             "correct": False,
             "why": "Nothing requires it to melt. What happens next depends "
                    "on where the rock ends up, and this one has ended up at "
                    "the surface."},
            {"text": "It is weathered and eroded into sediment, without ever "
                     "melting",
             "correct": True},
            {"text": "Nothing, because metamorphic is the last stage of the "
                     "cycle",
             "correct": False,
             "why": "There is no last stage. Every rock type has arrows "
                    "leading away from it as well as towards it."},
            {"text": "It becomes igneous, because that is the next type "
                     "round the ring",
             "correct": False,
             "why": "The ring is a way of drawing the cycle, not a rule the "
                    "rock obeys."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s02",
        "band": "standard",
        "text": "A sedimentary rock is dragged down somewhere deep and hot "
                "enough to melt, and the magma later cools. What type of "
                "rock is it now?",
        "options": [
            {"text": "Metamorphic first and then igneous, because it has to "
                     "pass through each stage",
             "correct": False,
             "why": "Melting erases everything. What cools out of a melt is "
                    "igneous, whether or not the rock was metamorphosed on "
                    "the way down."},
            {"text": "Sedimentary still, because melting does not change "
                     "what a rock is made of",
             "correct": False,
             "why": "A rock's group is decided by how it formed, not by what "
                    "it is made of, and this one formed by cooling from a "
                    "melt."},
            {"text": "Metamorphic, because heat and pressure is what "
                     "happened to it",
             "correct": False,
             "why": "Metamorphism changes a rock while it stays solid. This "
                    "one melted, which is the line between the two."},
            {"text": "Igneous, and it never had to be metamorphic on the way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s03",
        "band": "standard",
        "text": "Which statement about weathering is correct?",
        "options": [
            {"text": "It acts on any rock at the surface, whatever type that "
                     "rock is",
             "correct": True},
            {"text": "It acts only on sedimentary rock, because that is the "
                     "softest group",
             "correct": False,
             "why": "Granite is igneous and weathers perfectly well. What "
                    "matters is being at the surface, not the group."},
            {"text": "It acts only on rock that has already been "
                     "metamorphosed",
             "correct": False,
             "why": "Nothing has to be metamorphosed first. Rain does not "
                    "check what a rock has been through."},
            {"text": "It acts on rock buried deep enough for the pressure to "
                     "crack it",
             "correct": False,
             "why": "Weathering is a surface process. Deep burial brings "
                    "heat and pressure instead."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s04",
        "band": "standard",
        "text": "A sandstone cliff is worn back by about a metre every "
                "hundred years. Where does the worn-away rock go?",
        "options": [
            {"text": "It is destroyed, because weathering breaks rock down "
                     "into nothing",
             "correct": False,
             "why": "Weathering breaks rock into pieces. The pieces are "
                    "still there, and they are the sediment of somewhere "
                    "else."},
            {"text": "It stays at the foot of the cliff for good",
             "correct": False,
             "why": "Some of it rests there for a while, but rivers, waves "
                    "and wind carry it on."},
            {"text": "It is carried away and deposited as sediment somewhere "
                     "else",
             "correct": True},
            {"text": "It melts once it has been broken up small enough",
             "correct": False,
             "why": "Nothing melts at the surface. Melting needs the "
                    "conditions found deep in the crust."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-03-h01",
        "band": "harder",
        "text": "Why is a rock cycle diagram drawn with arrows across the "
                "middle as well as round the edge?",
        "options": [
            {"text": "Because a rock's route is decided by where it ends up, "
                     "not by which type it is now",
             "correct": True},
            {"text": "Because the middle arrows are the fast routes and the "
                     "outer ones are the slow routes",
             "correct": False,
             "why": "The arrows are routes, not speeds. Any of them can take "
                    "days or millions of years depending on the "
                    "conditions."},
            {"text": "Because the middle arrows are rare exceptions to the "
                     "real cycle",
             "correct": False,
             "why": "They are not exceptions. A metamorphic rock weathering "
                    "into sediment is one of the commonest things that "
                    "happens."},
            {"text": "Because the three rock types have to be fitted into a "
                     "circle somehow",
             "correct": False,
             "why": "The arrows are drawn where they are because those "
                    "routes exist, not to fill a shape."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h02",
        "band": "harder",
        "text": "Two grains of quartz sit side by side in the same "
                "sandstone. One came from a granite and the other from a "
                "quartzite. What does that tell you?",
        "options": [
            {"text": "One of the two grains must be far older than the "
                     "other",
             "correct": False,
             "why": "Nothing here dates either grain, and both arrived in "
                    "the same layer at the same time."},
            {"text": "The sandstone must have formed twice, once for each "
                     "grain",
             "correct": False,
             "why": "One sandstone is built from fragments of many different "
                    "rocks at once — that is what a river delivers."},
            {"text": "Two rocks that took different routes can end up in the "
                     "same new rock",
             "correct": True},
            {"text": "The quartzite grain must have melted somewhere along "
                     "the way",
             "correct": False,
             "why": "A grain that melted would not still be a grain. Both "
                    "were weathered and carried, and neither was melted."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h03",
        "band": "harder",
        "text": "Almost none of the Earth's original crust still exists, yet "
                "rocks around four billion years old are still found. How "
                "can both of those be true?",
        "options": [
            {"text": "The very old rocks are not really that old, so the "
                     "dating must be wrong",
             "correct": False,
             "why": "Several independent dating methods agree on those ages. "
                    "The problem is not the measurement."},
            {"text": "The cycle destroys rock continually, and a few pieces "
                     "happened never to be caught by it",
             "correct": True},
            {"text": "The oldest rocks are made of something the cycle "
                     "cannot break down",
             "correct": False,
             "why": "The cycle acts on every kind of rock. Survival is about "
                    "where a rock sat, not what it was made of."},
            {"text": "The original crust is all still there, buried under "
                     "everything younger",
             "correct": False,
             "why": "Burial does not protect rock from the cycle — burial is "
                    "what delivers it to heat, pressure and melting."},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h04",
        "band": "harder",
        "text": "A student says one trip round the rock cycle takes a fixed "
                "length of time. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong; a complete circuit takes hundreds of "
                     "millions of years",
             "correct": False,
             "why": "That is a rough figure for a typical circuit, not a "
                    "length of time any particular grain has to take."},
            {"text": "Nothing is wrong, as long as you start counting from "
                     "the igneous stage",
             "correct": False,
             "why": "There is no stage to start counting from, because the "
                    "cycle has no beginning."},
            {"text": "It is wrong only because the cycle runs one way round "
                     "rather than two",
             "correct": False,
             "why": "It does not run one way round either, and a fixed "
                    "direction would still not give it a fixed length."},
            {"text": "The processes take anything from days to millions of "
                     "years, and a rock can skip stages",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-03-e05",
        "band": "easier",
        "text": "What is erosion?",
        "options": [
            {"text": "The dropping of sediment when water slows down",
             "correct": False,
             "why": "That is deposition, which comes after erosion"},
            {"text": "The breaking down of rock where it stands, by frost or "
                     "by water freezing in the cracks in it and forcing them "
                     "further apart each winter",
             "correct": False,
             "why": "That is weathering, and nothing is carried anywhere. "
                    "Erosion is the transport"},
            {"text": "The picking up and carrying away of fragments, by "
                     "water, wind or ice",
             "correct": True},
            {"text": "The squeezing of layers into solid rock",
             "correct": False,
             "why": "That is compaction, which happens after the sediment "
                    "has been dropped"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e06",
        "band": "easier",
        "text": "What is deposition?",
        "options": [
            {"text": "The breaking down of rock by frost",
             "correct": False,
             "why": "That is weathering, and it happens before anything is "
                    "carried or dropped"},
            {"text": "The melting of rock deep underground",
             "correct": False,
             "why": "That is the route to an igneous rock and is nothing to "
                    "do with sediment"},
            {"text": "The laying down of new rock by a volcano, which spreads "
                     "molten material over the surface where it cools into "
                     "solid layers one on top of another",
             "correct": False,
             "why": "That is how an igneous rock forms. Deposition is about "
                    "sediment being dropped"},
            {"text": "The dropping of sediment when the water or wind "
                     "carrying it slows down",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e07",
        "band": "easier",
        "text": "What is metamorphism?",
        "options": [
            {"text": "The changing of a rock by heat and pressure while it "
                     "stays solid",
             "correct": True},
            {"text": "The melting of a rock deep underground, followed by the "
                     "cooling of the melt into a new rock with a different "
                     "set of minerals in it",
             "correct": False,
             "why": "Melt it and what cools out is IGNEOUS. Metamorphism "
                    "never melts the rock"},
            {"text": "The breaking of a rock into fragments",
             "correct": False,
             "why": "That is weathering, and it happens at the surface"},
            {"text": "The cementing of grains into rock",
             "correct": False,
             "why": "That makes a sedimentary rock near the surface"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e08",
        "band": "easier",
        "text": "Which order do the sedimentary processes come in?",
        "options": [
            {"text": "Deposition, weathering, erosion, compaction, "
                     "cementation, which is the order that a grain would meet "
                     "them going round the cycle starting from a sea floor",
             "correct": False,
             "why": "A grain cannot be dropped before it has been broken off "
                    "and carried. Weathering comes first"},
            {"text": "Weathering, erosion and transport, deposition, "
                     "compaction and cementation",
             "correct": True},
            {"text": "Erosion, weathering, deposition, cementation",
             "correct": False,
             "why": "Nothing can be carried away until it has been broken "
                    "loose. Weathering is first"},
            {"text": "Compaction, cementation, weathering, erosion",
             "correct": False,
             "why": "That is the sequence backwards. Rock has to be broken "
                    "down before it can be built up again"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e09",
        "band": "easier",
        "text": "What turns a metamorphic rock into an igneous one?",
        "options": [
            {"text": "Being lifted to the surface and weathered",
             "correct": False,
             "why": "That is the route to sediment and eventually to a "
                    "sedimentary rock"},
            {"text": "Being squeezed harder still, so that its grains rotate "
                     "further into line and its bands become sharper than "
                     "they were before",
             "correct": False,
             "why": "More squeezing gives more metamorphism. Only melting "
                    "makes it igneous"},
            {"text": "Being buried deeper and hotter until it melts, and then "
                     "cooling",
             "correct": True},
            {"text": "Nothing — a metamorphic rock stays metamorphic",
             "correct": False,
             "why": "Any rock type can become any other. That is what makes "
                    "it a cycle"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-03-s05",
        "band": "standard",
        "text": "The cycle is described as having no fixed direction. Which "
                "statement follows?",
        "options": [
            {"text": "Rocks change type at random",
             "correct": False,
             "why": "Nothing is random — the route follows the conditions the "
                    "rock finds itself in"},
            {"text": "A rock has to pass through all three types in turn "
                     "before it can come back round to the one it started as, "
                     "which is what makes the diagram a circle",
             "correct": False,
             "why": "Arrows cross the middle for exactly this reason. Stages "
                    "can be skipped"},
            {"text": "Where a rock ends up is what decides its route, not "
                     "what type it is now",
             "correct": True},
            {"text": "Sedimentary rock always becomes metamorphic next",
             "correct": False,
             "why": "It may be lifted and weathered back into sediment "
                    "instead"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s06",
        "band": "standard",
        "text": "Fragments are rounded and sorted by size on their journey. "
                "Which process does that?",
        "options": [
            {"text": "Compaction, as the weight of later layers presses them "
                     "together",
             "correct": False,
             "why": "Compaction happens after they have been dropped. They "
                    "arrive already rounded"},
            {"text": "Cementation",
             "correct": False,
             "why": "Cement fills the gaps between grains. It does not shape "
                    "them"},
            {"text": "Weathering, which breaks each fragment down evenly on "
                     "every side and so leaves it rounder and smaller than it "
                     "was before",
             "correct": False,
             "why": "Weathering breaks rock where it stands, and it leaves "
                    "angular pieces. The rounding happens on the way"},
            {"text": "Erosion and transport, as the fragments are knocked "
                     "about and carried",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s07",
        "band": "standard",
        "text": "A granite outcrop on a moor slowly crumbles into sand. What "
                "is happening, and what could that sand become?",
        "options": [
            {"text": "It is being weathered, and the sand could become "
                     "sandstone",
             "correct": True},
            {"text": "It is being metamorphosed, and the sand could become "
                     "another granite once it has been buried deeply enough "
                     "for the heat to reach it",
             "correct": False,
             "why": "Nothing at the surface is metamorphism, and buried sand "
                    "becomes sandstone rather than granite"},
            {"text": "It is melting, and the sand could become an igneous "
                     "rock",
             "correct": False,
             "why": "Nothing melts on a moor. Crumbling in the weather is "
                    "weathering"},
            {"text": "Nothing much — granite is too hard to weather",
             "correct": False,
             "why": "Granite weathers perfectly well. Much of the sand on "
                    "British beaches is what is left of it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s08",
        "band": "standard",
        "text": "What is the difference between WEATHERING and EROSION?",
        "options": [
            {"text": "Weathering is caused by the weather and erosion by "
                     "moving water, so the two words name the two different "
                     "forces that wear a landscape down over time",
             "correct": False,
             "why": "Water does both. The difference is whether anything is "
                    "carried away"},
            {"text": "Weathering breaks rock down where it is; erosion "
                     "carries the pieces away",
             "correct": True},
            {"text": "Weathering is fast and erosion is slow",
             "correct": False,
             "why": "Both run over long periods. Speed is not what separates "
                    "them"},
            {"text": "They are two words for the same process",
             "correct": False,
             "why": "One breaks rock down and the other moves the pieces. "
                    "Keeping them apart is the point"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s09",
        "band": "standard",
        "text": "Rain is slightly acidic even in clean country air. What does "
                "that do to a limestone wall over centuries?",
        "options": [
            {"text": "Erodes it, by carrying pieces away",
             "correct": False,
             "why": "Rain does wash the products off, and the attack itself "
                    "is chemical weathering"},
            {"text": "Nothing measurable, because rain that far from any "
                     "industry is not acidic enough to react with a rock as "
                     "hard as limestone is",
             "correct": False,
             "why": "It is the reason old gravestones go unreadable. Slightly "
                    "acidic is enough over centuries"},
            {"text": "Weathers it chemically, reacting with the carbonate and "
                     "dissolving it away",
             "correct": True},
            {"text": "Metamorphoses it into marble",
             "correct": False,
             "why": "That needs heat and pressure deep underground, not rain "
                    "on a wall"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-03-h05",
        "band": "harder",
        "text": "The stone in a cathedral wall was once sand, and before that "
                "a mountain, and before that molten. What is the ONE thing "
                "that has stayed the same?",
        "options": [
            {"text": "The texture",
             "correct": False,
             "why": "Texture is the first thing every stage destroys, and it "
                    "is why texture records the LAST stage"},
            {"text": "The minerals, which are rearranged into new textures at "
                     "each stage but are never actually broken up into the "
                     "elements they are built from",
             "correct": False,
             "why": "Melting and metamorphism both make new minerals. What "
                    "survives every stage is the atoms"},
            {"text": "The atoms",
             "correct": True},
            {"text": "Nothing at all",
             "correct": False,
             "why": "The atoms go round unchanged. That is the point of the "
                    "big question"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h06",
        "band": "harder",
        "text": "A pebble on a beach is rounded and a scree slope below a "
                "cliff is full of sharp angular pieces. What separates them?",
        "options": [
            {"text": "How old each is",
             "correct": False,
             "why": "A scree can be older than a beach pebble and still be "
                    "sharp. It is the journey that counts"},
            {"text": "The pebble has been weathered and the scree has not",
             "correct": False,
             "why": "The scree is the PRODUCT of weathering. What it has not "
                    "had is transport"},
            {"text": "What each is made of, since a rock made of hard "
                     "minerals keeps its edges and one made of softer "
                     "minerals wears round wherever it happens to lie",
             "correct": False,
             "why": "The same rock does both, depending on where it ends up. "
                    "Travel is what rounds it"},
            {"text": "How far each has travelled — the pebble has been "
                     "knocked about and the scree has not moved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h07",
        "band": "harder",
        "text": "A rock is buried deep enough to melt, and the magma later "
                "cools. What has happened to the record of what it used to "
                "be?",
        "options": [
            {"text": "It is erased — the new rock records only the cooling of "
                     "the melt",
             "correct": True},
            {"text": "It is preserved in the minerals, which survive the "
                     "melting unchanged and can still be read afterwards to "
                     "show what the rock was before it went down",
             "correct": False,
             "why": "Melting rearranges everything. New minerals crystallise "
                    "as the melt cools"},
            {"text": "It is preserved in the fossils",
             "correct": False,
             "why": "Nothing survives molten rock. Fossils go first"},
            {"text": "It is preserved in the layers",
             "correct": False,
             "why": "Layers are the first structure a melt destroys"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h08",
        "band": "harder",
        "text": "Why is the rock cycle drawn with arrows across the middle "
                "rather than only round the rim?",
        "options": [
            {"text": "Because the diagram would be too large to fit on a page "
                     "if every possible route had to be drawn round the "
                     "outside of it in order",
             "correct": False,
             "why": "It is not a drafting convenience. The middle arrows are "
                    "real routes"},
            {"text": "Because a rock can skip stages — where it ends up "
                     "decides its route",
             "correct": True},
            {"text": "Because some routes run faster than others",
             "correct": False,
             "why": "They do, and speed is not what the arrows record. They "
                    "record what is possible"},
            {"text": "Because the middle of the diagram would otherwise be "
                     "empty",
             "correct": False,
             "why": "The arrows are there because those changes happen, not "
                    "to fill space"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h09",
        "band": "harder",
        "text": "The mountains around us have not always been what they are "
                "now. Which everyday observation supports that best?",
        "options": [
            {"text": "Mountains are cold at the top",
             "correct": False,
             "why": "Altitude explains that and says nothing about change "
                    "over time"},
            {"text": "Mountains are made of hard rock, and hard rock lasts "
                     "far longer than any of the softer kinds, so a mountain "
                     "will still be there long after a hill has gone",
             "correct": False,
             "why": "That argues the OTHER way — for permanence. What shows "
                    "change is the material leaving them"},
            {"text": "Rivers carry sediment to the sea continually, and it "
                     "has to be coming from somewhere",
             "correct": True},
            {"text": "Volcanoes build new mountains",
             "correct": False,
             "why": "True and it is about building rather than wearing away. "
                    "The sediment in rivers shows the other half"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-03-e10",
        "band": "easier",
        "text": "Weathering can be physical or chemical. What does PHYSICAL "
                "weathering do to a rock?",
        "options": [
            {"text": "It breaks the rock into pieces without changing what it "
                     "is made of",
             "correct": True},
            {"text": "It reacts with the minerals and changes them into "
                     "different substances",
             "correct": False,
             "why": "That is chemical weathering. The physical kind changes "
                    "the size of the pieces only"},
            {"text": "It carries the loose pieces away and drops them "
                     "somewhere else",
             "correct": False,
             "why": "Carrying is erosion and transport. Weathering leaves "
                    "everything where it was"},
            {"text": "It presses the pieces together until they make a new "
                     "solid rock",
             "correct": False,
             "why": "That is compaction, and it happens long afterwards and a "
                    "long way down"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e11",
        "band": "easier",
        "text": "Which of these is an example of CHEMICAL weathering?",
        "options": [
            {"text": "Water freezing in a crack and levering it wider open",
             "correct": False,
             "why": "Nothing reacts there. Ice simply takes up more room than "
                    "the water did"},
            {"text": "Slightly acidic rain reacting with the minerals in a "
                     "rock",
             "correct": True},
            {"text": "A river rolling a boulder along and knocking its corners "
                     "off",
             "correct": False,
             "why": "That is erosion and transport, and it happens on the "
                    "journey rather than where the rock sat"},
            {"text": "A tree root growing into a crack and forcing it apart",
             "correct": False,
             "why": "That is physical. The rock is prised apart rather than "
                    "reacted with"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e12",
        "band": "easier",
        "text": "Water gets into a crack in a rock and then freezes. What "
                "happens next?",
        "options": [
            {"text": "The ice dissolves the rock around the crack",
             "correct": False,
             "why": "Ice dissolves nothing. What it does is push"},
            {"text": "The rock shrinks around the ice and seals the crack up",
             "correct": False,
             "why": "The crack is forced wider rather than closed. That is why "
                    "a frost damages a wall"},
            {"text": "The ice takes up more room than the water did and levers "
                     "the crack open",
             "correct": True},
            {"text": "The water is squeezed out again before it can freeze",
             "correct": False,
             "why": "Water trapped in a narrow crack freezes where it is, "
                    "which is what makes this work"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e13",
        "band": "easier",
        "text": "What carries away the fragments that weathering has broken "
                "loose?",
        "options": [
            {"text": "Nothing carries them; they stay where they fall for "
                     "good",
             "correct": False,
             "why": "Some rest at the foot of a cliff for a while, and rivers, "
                    "waves and wind take them on"},
            {"text": "The rock beneath them, which creeps downhill and drags "
                     "them along with it",
             "correct": False,
             "why": "Solid rock does not creep downhill at the surface. Water, "
                    "wind and ice do the carrying"},
            {"text": "Heat rising from below, which pushes them out of the "
                     "ground",
             "correct": False,
             "why": "Heat from below drives the plates about. It does not move "
                    "loose fragments across a landscape"},
            {"text": "Rivers, glaciers, wind and waves",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e14",
        "band": "easier",
        "text": "Where does a river drop the sediment it has been carrying?",
        "options": [
            {"text": "Where it slows down",
             "correct": True},
            {"text": "Where it runs fastest, because fast water shakes its "
                     "load loose",
             "correct": False,
             "why": "Fast water carries MORE, not less. Slowing is what makes "
                    "a river let go"},
            {"text": "Where the water is deepest, because depth holds sediment "
                     "down",
             "correct": False,
             "why": "Depth on its own decides nothing. It is the speed of the "
                    "water that matters"},
            {"text": "Where the river is narrowest, because the banks squeeze "
                     "the load out",
             "correct": False,
             "why": "A narrow channel usually runs faster, so it carries its "
                    "load further rather than dropping it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e15",
        "band": "easier",
        "text": "What part does a glacier play in the rock cycle?",
        "options": [
            {"text": "It melts rock, because ice at that pressure is hot "
                     "underneath",
             "correct": False,
             "why": "Nothing near a glacier is anywhere close to a melting "
                    "point. Ice is cold"},
            {"text": "It carries fragments, which is erosion and transport",
             "correct": True},
            {"text": "It cements grains together into a new sedimentary rock",
             "correct": False,
             "why": "Cementing is done by minerals left behind by water in "
                    "buried sediment"},
            {"text": "It metamorphoses the rock it sits on by pressing down on "
                     "it",
             "correct": False,
             "why": "A glacier's weight is tiny beside the burial that "
                    "metamorphism needs"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e16",
        "band": "easier",
        "text": "What is the rock cycle?",
        "options": [
            {"text": "The order in which the three rock types were first made "
                     "on Earth",
             "correct": False,
             "why": "It is not an order and not a history. It is a set of "
                    "routes that are open at any time"},
            {"text": "The regular period of time in which a rock changes from "
                     "one type to another",
             "correct": False,
             "why": "There is no regular period. The processes run at wildly "
                    "different rates"},
            {"text": "The whole set of routes by which any rock type can "
                     "become any other",
             "correct": True},
            {"text": "The journey a single grain makes from a mountain to the "
                     "sea and back",
             "correct": False,
             "why": "That is one journey a grain can take. The cycle is every "
                    "route there is"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e17",
        "band": "easier",
        "text": "How does a rock that formed several kilometres underground end "
                "up at the surface?",
        "options": [
            {"text": "It floats upwards, because rock is less dense than the "
                     "material around it",
             "correct": False,
             "why": "Rock does not float through rock. It is lifted, and what "
                    "lay above it is worn away"},
            {"text": "It is erupted by a volcano along with the lava",
             "correct": False,
             "why": "A volcano brings up melt. Solid rock arrives by being "
                    "lifted and uncovered"},
            {"text": "It stays where it is, and the sea level drops until it "
                     "is exposed",
             "correct": False,
             "why": "Sea level has never fallen by kilometres. The rock itself "
                    "moves"},
            {"text": "It is pushed up, and the rock above it is worn away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e18",
        "band": "easier",
        "text": "Roughly how much rock does weathering remove from an exposed "
                "surface in a human lifetime?",
        "options": [
            {"text": "A few millimetres",
             "correct": True},
            {"text": "A few metres",
             "correct": False,
             "why": "Metres in a lifetime would strip a hillside bare within a "
                    "century. It is far slower than that"},
            {"text": "A few centimetres",
             "correct": False,
             "why": "Nearer, and still about ten times too much for an "
                    "ordinary exposed surface"},
            {"text": "Nothing measurable at all",
             "correct": False,
             "why": "It is slow and it is measurable, which is how the figure "
                    "is known"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e19",
        "band": "easier",
        "text": "About how long does one complete circuit of the rock cycle "
                "take?",
        "options": [
            {"text": "A few thousand years",
             "correct": False,
             "why": "Compaction alone can take that long. A whole circuit is "
                    "very much slower"},
            {"text": "Hundreds of millions of years",
             "correct": True},
            {"text": "A few million years",
             "correct": False,
             "why": "Nearer, and still roughly a hundred times short of a full "
                    "circuit"},
            {"text": "About a hundred thousand years",
             "correct": False,
             "why": "That is not long enough for burial, heating and cooling "
                    "at depth, let alone all of it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e20",
        "band": "easier",
        "text": "How old are the oldest crustal rocks found so far?",
        "options": [
            {"text": "About four hundred million years old",
             "correct": False,
             "why": "Plenty of rock is older than that. The oldest is about "
                    "ten times older"},
            {"text": "About forty million years old",
             "correct": False,
             "why": "That is younger than the Himalayas. The oldest crust is "
                    "far older"},
            {"text": "About four billion years old",
             "correct": True},
            {"text": "About four hundred thousand years old",
             "correct": False,
             "why": "That is younger than our own species is old. Rock goes "
                    "back very much further"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e21",
        "band": "easier",
        "text": "What drives the rock cycle — where does the energy come from?",
        "options": [
            {"text": "Heat from inside the Earth",
             "correct": True},
            {"text": "The pull of the Moon on the solid rock of the crust",
             "correct": False,
             "why": "The Moon raises tides in the sea. It does not drag plates "
                    "around or bury rock"},
            {"text": "The weight of the atmosphere pressing on the surface",
             "correct": False,
             "why": "The air presses evenly and changes nothing. The engine is "
                    "below, not above"},
            {"text": "Heat from the Sun warming the rocks at the surface",
             "correct": False,
             "why": "The Sun drives the weather, and what lifts and buries "
                    "rock is the heat inside"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e22",
        "band": "easier",
        "text": "What happens to rock where two continents collide?",
        "options": [
            {"text": "It is forced downwards or pushed up into mountains",
             "correct": True},
            {"text": "It is thrown clear of the collision and left as loose "
                     "rubble",
             "correct": False,
             "why": "Continents meet far too slowly for anything to be thrown. "
                    "The rock is driven down or up"},
            {"text": "It shatters into sand along the whole length of the "
                     "join",
             "correct": False,
             "why": "Rock is deformed rather than shattered into sand. Sand is "
                    "made at the surface by weathering"},
            {"text": "It is left completely unchanged, because rock is far too "
                     "strong",
             "correct": False,
             "why": "Whole mountain ranges are built this way, and the rock in "
                    "them is deformed and cooked"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e23",
        "band": "easier",
        "text": "A sandstone is buried deep in a mountain range and cooked "
                "without melting. What does it become?",
        "options": [
            {"text": "Granite",
             "correct": False,
             "why": "Granite crystallises out of a melt, and this rock has not "
                    "melted"},
            {"text": "Quartzite",
             "correct": True},
            {"text": "Marble",
             "correct": False,
             "why": "Marble is what cooked limestone becomes. A sandstone is "
                    "not a carbonate"},
            {"text": "Mudstone",
             "correct": False,
             "why": "Mudstone is mud that settled and was buried. Burying a "
                    "sandstone does not make one"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e24",
        "band": "easier",
        "text": "Where does the sediment that settles on a sea floor come "
                "from?",
        "options": [
            {"text": "From rock at the surface that has been worn away and "
                     "carried there",
             "correct": True},
            {"text": "From the mantle, which pushes fresh material up through "
                     "the sea floor",
             "correct": False,
             "why": "Material from the mantle arrives as melt at a volcano, "
                    "not as loose sediment"},
            {"text": "From the sea water itself, which turns slowly into solid "
                     "grains",
             "correct": False,
             "why": "Some minerals do crystallise out of sea water, and the "
                    "bulk of sediment is worn off the land"},
            {"text": "From dust that falls onto the sea from space each year",
             "correct": False,
             "why": "A little dust does arrive from space, and it is nothing "
                    "beside what the rivers deliver"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e25",
        "band": "easier",
        "text": "What has to be true of a rock before it can melt and become "
                "magma?",
        "options": [
            {"text": "It has to be buried, since depth on its own is enough to "
                     "melt anything",
             "correct": False,
             "why": "The mantle is deeper and hotter than any of this and is "
                    "solid rock. Depth alone does not do it"},
            {"text": "It has to have been metamorphosed first",
             "correct": False,
             "why": "Nothing requires that. A rock can go straight from "
                    "sedimentary to melted"},
            {"text": "It has to be hot enough, and wet enough, to pass its "
                     "melting point",
             "correct": True},
            {"text": "It has to be an igneous rock to begin with",
             "correct": False,
             "why": "Any rock can melt if the conditions are right. What comes "
                    "out is igneous whatever went in"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e26",
        "band": "easier",
        "text": "Which process turns magma into an igneous rock?",
        "options": [
            {"text": "Compaction, as the weight above squeezes the melt solid",
             "correct": False,
             "why": "Compaction acts on loose sediment. A melt solidifies by "
                    "losing heat"},
            {"text": "Cooling and crystallising",
             "correct": True},
            {"text": "Cementation, as minerals fill the gaps in the melt",
             "correct": False,
             "why": "There are no gaps in a melt, and cementation belongs to "
                    "the sedimentary route"},
            {"text": "Weathering, which hardens the surface of the melt",
             "correct": False,
             "why": "Weathering breaks rock down. It builds nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e27",
        "band": "easier",
        "text": "Which of these is NOT one of the processes of the rock cycle?",
        "options": [
            {"text": "Weathering",
             "correct": False,
             "why": "It is the process that breaks rock down where it sits"},
            {"text": "Deposition",
             "correct": False,
             "why": "It is the dropping of sediment when the water slows"},
            {"text": "Respiration",
             "correct": True},
            {"text": "Metamorphism",
             "correct": False,
             "why": "It is the changing of a rock by heat and pressure while "
                    "it stays solid"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e28",
        "band": "easier",
        "text": "What is sediment?",
        "options": [
            {"text": "Loose fragments and grains that have been dropped and "
                     "are not yet rock",
             "correct": True},
            {"text": "The cement that fills the gaps between the grains of a "
                     "buried rock",
             "correct": False,
             "why": "That is the cement itself. Sediment is the loose material "
                    "it later sticks together"},
            {"text": "Any rock that has been broken by heat and pressure deep "
                     "underground",
             "correct": False,
             "why": "Deep heat and pressure give a metamorphic rock. Sediment "
                    "sits at the surface"},
            {"text": "The layer of soil that covers most of the land surface "
                     "of the Earth",
             "correct": False,
             "why": "Soil holds sediment and a good deal of living material. "
                    "Sediment is the mineral fragments"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e29",
        "band": "easier",
        "text": "Weathering happens at the surface. Where does metamorphism "
                "happen?",
        "options": [
            {"text": "At the surface as well, wherever the weather is hot "
                     "enough",
             "correct": False,
             "why": "Nowhere at the surface is remotely hot enough, and there "
                    "is no burial pressure there"},
            {"text": "In buried rock, or beside an intrusion of magma",
             "correct": True},
            {"text": "Only in the mantle, below every part of the crust",
             "correct": False,
             "why": "It happens inside the crust, where burial and intrusions "
                    "supply the heat and pressure"},
            {"text": "On the sea floor, where the water pressure is greatest",
             "correct": False,
             "why": "Water pressure at the deepest sea floor is nothing beside "
                    "the pressure of deep burial"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-e30",
        "band": "easier",
        "text": "Which of these is a SURFACE process?",
        "options": [
            {"text": "Melting",
             "correct": False,
             "why": "Melting needs the conditions found deep in the crust"},
            {"text": "Metamorphism",
             "correct": False,
             "why": "It needs deep burial or the heat of a nearby intrusion"},
            {"text": "Compaction",
             "correct": False,
             "why": "It needs the weight of later layers on top, which means "
                    "burial"},
            {"text": "Weathering",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c10-03-s10",
        "band": "standard",
        "text": "As a river slows down it drops the heaviest particles first. "
                "Why?",
        "options": [
            {"text": "Because the heaviest particles dissolve first and are "
                     "lost from the water",
             "correct": False,
             "why": "Nothing dissolves here. The heavy grains are dropped "
                    "because the water can no longer hold them up"},
            {"text": "Because the heaviest particles are pushed to the front "
                     "and arrive earliest",
             "correct": False,
             "why": "The load is mixed through the water. What decides is how "
                    "much weight the flow can carry"},
            {"text": "Because heavy particles are rounder, so they roll out of "
                     "the river bed",
             "correct": False,
             "why": "Rounding comes from the journey and has nothing to do "
                    "with the order of dropping"},
            {"text": "Because a river can only carry the heaviest particles "
                     "while it is moving fast",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s11",
        "band": "standard",
        "text": "Sand on a beach and the granite cliff behind it contain the "
                "same mineral. What does that suggest?",
        "options": [
            {"text": "The sand is what is left of the granite after weathering "
                     "and erosion",
             "correct": True},
            {"text": "The granite is forming out of the sand as the beach is "
                     "buried by the tide",
             "correct": False,
             "why": "Granite crystallises from a melt deep underground. A "
                    "beach makes sandstone at best"},
            {"text": "The two are unrelated, and the match between the "
                     "minerals is a coincidence",
             "correct": False,
             "why": "A beach directly below a cliff of the same mineral is not "
                    "a coincidence"},
            {"text": "The sand blew in from elsewhere",
             "correct": False,
             "why": "Sand does blow about, and the simplest account of a match "
                    "with the cliff above is that the cliff supplied it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s12",
        "band": "standard",
        "text": "Why does physical weathering make chemical weathering work "
                "faster?",
        "options": [
            {"text": "Because the pieces are warmer once they have been broken "
                     "off the rock",
             "correct": False,
             "why": "Breaking rock warms nothing measurably. What changes is "
                    "how much surface is exposed"},
            {"text": "Because breaking the rock up gives the rain far more "
                     "surface to attack",
             "correct": True},
            {"text": "Because broken rock holds more water, and water is what "
                     "reacts with rock",
             "correct": False,
             "why": "What reacts is the acid dissolved in the rain, and the "
                    "gain comes from the extra surface"},
            {"text": "Because small pieces contain different minerals from the "
                     "rock they came off",
             "correct": False,
             "why": "A fragment holds the same minerals as its parent. Only "
                    "the size has changed"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s13",
        "band": "standard",
        "text": "A limestone block and a granite block sit side by side on a "
                "moor, and the limestone is far more worn. Why?",
        "options": [
            {"text": "The limestone is softer, and softness is the only thing "
                     "that decides how fast rock wears",
             "correct": False,
             "why": "Softness plays a part, and what is doing most of the work "
                    "here is a chemical reaction"},
            {"text": "The granite is much younger, and a younger rock has had "
                     "less time to be worn away",
             "correct": False,
             "why": "Nothing says the granite is younger, and the two have sat "
                    "side by side under the same rain"},
            {"text": "Slightly acidic rain reacts with the carbonate in the "
                     "limestone and not with quartz",
             "correct": True},
            {"text": "The limestone is nearer the path",
             "correct": False,
             "why": "Where a block sits on a moor does not change what the "
                    "rain does to it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s14",
        "band": "standard",
        "text": "A rock is buried deep under a mountain range and becomes "
                "metamorphic rather than igneous. Why?",
        "options": [
            {"text": "Because igneous rock can only form at the surface",
             "correct": False,
             "why": "Granite forms deep underground and is igneous. Where a "
                    "melt cools does not decide the group"},
            {"text": "Because burial cools a rock rather than heating it",
             "correct": False,
             "why": "Burial heats it. That is why deep rock is hot"},
            {"text": "Because only a rock that was sedimentary first can ever "
                     "melt",
             "correct": False,
             "why": "Any rock can melt given the right conditions, whatever it "
                    "was before"},
            {"text": "Because heat and pressure change it while it stays "
                     "solid, and it never reaches its melting point",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s15",
        "band": "standard",
        "text": "The Himalayas took fifty million years to rise and are still "
                "rising. Which part of the cycle does that belong to?",
        "options": [
            {"text": "Uplift, driven by the heat inside the Earth, which lifts "
                     "rock and exposes it",
             "correct": True},
            {"text": "Deposition, because a rising mountain is sediment being "
                     "piled up on itself",
             "correct": False,
             "why": "Deposition drops loose sediment. A mountain range is "
                    "solid rock being pushed upwards"},
            {"text": "Cementation, because rising rock is being glued together "
                     "as it goes up",
             "correct": False,
             "why": "Cementation sticks buried grains together near the "
                    "surface and lifts nothing"},
            {"text": "Melting, because a mountain can only rise if the rock "
                     "below it has melted",
             "correct": False,
             "why": "The Himalayas were pushed up by a collision of "
                    "continents, not floated up on a melt"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s16",
        "band": "standard",
        "text": "Suppose the heat inside the Earth stopped. What would happen "
                "to the continents over a very long time?",
        "options": [
            {"text": "They would be built higher, because weathering would "
                     "stop along with everything else",
             "correct": False,
             "why": "Weathering is driven by the weather, which the Sun runs. "
                    "It would carry on"},
            {"text": "They would be worn flat by rain, because nothing would "
                     "ever lift them again",
             "correct": True},
            {"text": "They would stay exactly as they are now, because the "
                     "surface would be frozen in place",
             "correct": False,
             "why": "The surface is not held in place by heat from below. Rain "
                    "would keep wearing it down"},
            {"text": "They would sink",
             "correct": False,
             "why": "Nothing would push them down either. What stops is the "
                    "lifting, not the land"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s17",
        "band": "standard",
        "text": "Where two plates pull apart, new igneous rock forms. What "
                "makes the rock there melt?",
        "options": [
            {"text": "The two plates rub together and the friction melts the "
                     "rock between them",
             "correct": False,
             "why": "The plates are moving apart rather than rubbing, so there "
                    "is nothing to make friction"},
            {"text": "Sea water pours into the gap and is heated until it "
                     "turns the rock to melt",
             "correct": False,
             "why": "Water cools the rock it meets. It does not supply the "
                    "heat"},
            {"text": "The pressure drops, so rock that was solid at that depth "
                     "passes its melting point",
             "correct": True},
            {"text": "The gap fills with sediment, which is compressed until "
                     "it becomes igneous",
             "correct": False,
             "why": "Compressed sediment becomes sedimentary rock. Igneous "
                    "rock needs a melt"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s18",
        "band": "standard",
        "text": "A granite forms several kilometres underground. What has to "
                "happen before weathering can touch it?",
        "options": [
            {"text": "The granite has to melt again first, because only a melt "
                     "can move upwards through rock",
             "correct": False,
             "why": "A melted granite would cool as a new igneous rock. Solid "
                    "rock is lifted rather than melted"},
            {"text": "The sea level has to fall by several kilometres before "
                     "the granite can be uncovered",
             "correct": False,
             "why": "Sea level has never moved by kilometres. It is the rock "
                    "that moves"},
            {"text": "The rock lying above it has to be removed and the "
                     "granite has to reach the surface",
             "correct": True},
            {"text": "Nothing has to happen",
             "correct": False,
             "why": "Weathering is a surface process. A rock kilometres down "
                    "is out of its reach"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s19",
        "band": "standard",
        "text": "A river slows as it enters a lake and drops its load. What "
                "becomes of that sediment over the next million years?",
        "options": [
            {"text": "It is buried by later layers, compacted and cemented "
                     "into a sedimentary rock",
             "correct": True},
            {"text": "It is dissolved away, because still water breaks "
                     "sediment down over time",
             "correct": False,
             "why": "Still water dissolves very little. Burial is what happens "
                    "to sediment on a lake bed"},
            {"text": "It melts, because the weight of the water above heats "
                     "the lake bed",
             "correct": False,
             "why": "Water does not heat what it lies on, and a lake bed is "
                    "nowhere near a melting point"},
            {"text": "It stays loose for ever, because a lake has no way of "
                     "turning it to rock",
             "correct": False,
             "why": "Later layers supply the weight, and water moving through "
                    "leaves the cement"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s20",
        "band": "standard",
        "text": "One sandstone holds grains of granite and another holds "
                "grains of slate. What does that say about where each came "
                "from?",
        "options": [
            {"text": "The two sandstones must have been laid down at "
                     "completely different times in the past",
             "correct": False,
             "why": "Nothing here dates either of them. What differs is the "
                    "land each river drained"},
            {"text": "Each river drained a different kind of country — one "
                     "granite, one slate",
             "correct": True},
            {"text": "One of them has been metamorphosed and the other one has "
                     "not been touched",
             "correct": False,
             "why": "Both are sandstones made of separate grains, so neither "
                    "has been metamorphosed"},
            {"text": "One of the two is not really a sandstone",
             "correct": False,
             "why": "A sandstone is defined by its grains sitting separately, "
                    "not by what those grains came from"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s21",
        "band": "standard",
        "text": "A sea cliff is worn back by about 1 metre every 100 years. "
                "How far back would it move in 10 000 years?",
        "options": [
            {"text": "10 metres",
             "correct": False,
             "why": "That is the answer for 1000 years. Ten thousand years is "
                    "ten times as long"},
            {"text": "1000 metres",
             "correct": False,
             "why": "That would need 1 metre every 10 years. The rate given is "
                    "ten times slower"},
            {"text": "100 metres",
             "correct": True},
            {"text": "10 000 metres",
             "correct": False,
             "why": "That is 1 metre a year, which is a hundred times the rate "
                    "given"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s22",
        "band": "standard",
        "text": "Weathering removes about 2 mm of rock from an exposed surface "
                "every 100 years. How much would it remove in 10 000 years?",
        "options": [
            {"text": "20 mm",
             "correct": False,
             "why": "That is the answer for 1000 years rather than for ten "
                    "thousand"},
            {"text": "200 mm",
             "correct": True},
            {"text": "2000 mm",
             "correct": False,
             "why": "That would be 2 mm every 10 years, ten times the rate "
                    "given"},
            {"text": "2 mm",
             "correct": False,
             "why": "That is what one hundred years removes, not ten thousand"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s23",
        "band": "standard",
        "text": "One circuit of the rock cycle takes roughly 300 million "
                "years. Roughly how many circuits could have run since the "
                "Earth formed 4500 million years ago?",
        "options": [
            {"text": "About 150",
             "correct": False,
             "why": "That would need a circuit of about 30 million years, ten "
                    "times faster than the figure given"},
            {"text": "About 15",
             "correct": True},
            {"text": "About 1500",
             "correct": False,
             "why": "That would be a circuit every three million years, which "
                    "is a hundred times too fast"},
            {"text": "About 1",
             "correct": False,
             "why": "4500 divided by 300 is 15, so there has been time for "
                    "many circuits"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s24",
        "band": "standard",
        "text": "A student writes that erosion makes rock and weathering "
                "destroys it. Correct them.",
        "options": [
            {"text": "Both of them break rock down; what makes new rock is "
                     "deposition and burial",
             "correct": True},
            {"text": "They have the two the right way round, since erosion "
                     "does build the new layers up",
             "correct": False,
             "why": "Erosion carries fragments away. Building the layers is "
                    "deposition"},
            {"text": "Weathering makes rock and erosion destroys it, so the "
                     "two words are simply swapped",
             "correct": False,
             "why": "Neither of them makes rock. Both take it apart or move "
                    "the pieces"},
            {"text": "Both are right, because the cycle destroys and rebuilds "
                     "rock at every single stage",
             "correct": False,
             "why": "Rock is rebuilt at particular stages, and neither of "
                    "these two is one of them"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s25",
        "band": "standard",
        "text": "A slab of sea floor is being dragged downwards where two "
                "plates meet. Which processes will act on it?",
        "options": [
            {"text": "Weathering and erosion, because it is still in contact "
                     "with sea water all the way down",
             "correct": False,
             "why": "Both are surface processes. Once the rock is going down "
                    "it is out of their reach"},
            {"text": "Deposition and cementation, because sediment keeps "
                     "settling onto it as it descends",
             "correct": False,
             "why": "Sediment settles on the sea floor above. What acts on the "
                    "descending slab is heat and pressure"},
            {"text": "Heat and pressure, and eventually melting",
             "correct": True},
            {"text": "None of them, because rock that is moving is not being "
                     "changed by anything",
             "correct": False,
             "why": "Moving rock is changed constantly, and this is the route "
                    "by which magma is made"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s26",
        "band": "standard",
        "text": "A geologist finds a rounded pebble of basalt sitting inside a "
                "sandstone. What order did the two rocks form in?",
        "options": [
            {"text": "The sandstone first, because the basalt grew inside it "
                     "afterwards from material in the water",
             "correct": False,
             "why": "A basalt pebble cannot grow inside solid rock. It was a "
                    "fragment before it was buried"},
            {"text": "Both at the same moment, because the pebble and the sand "
                     "were laid down together",
             "correct": False,
             "why": "The pebble was laid down with the sand, and the basalt "
                    "itself had to exist first"},
            {"text": "The basalt first, because it had to exist before a piece "
                     "of it could be buried",
             "correct": True},
            {"text": "It cannot be worked out",
             "correct": False,
             "why": "It can, and it is one of the most useful things a "
                    "sedimentary rock will tell you"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s27",
        "band": "standard",
        "text": "Cooling takes days at the surface and up to millions of years "
                "at depth. Why does the same process take so much longer down "
                "there?",
        "options": [
            {"text": "Because rock cools more slowly the older it is, and deep "
                     "rock is older",
             "correct": False,
             "why": "Age does not change how fast anything cools. The "
                    "surroundings do"},
            {"text": "Because pressure at depth stops a melt from cooling at "
                     "all until it rises",
             "correct": False,
             "why": "Pressure raises a melting point and does not stop heat "
                    "escaping"},
            {"text": "Because a melt at depth is much hotter to begin with "
                     "than lava at the surface",
             "correct": False,
             "why": "The starting temperature is similar. What differs is how "
                    "fast the heat can leave"},
            {"text": "Because the rock around it is nearly as hot, so the heat "
                     "has almost nowhere to go",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s28",
        "band": "standard",
        "text": "Why is uplift necessary if the cycle is to keep turning?",
        "options": [
            {"text": "Because without it everything buried would stay buried "
                     "and never return to the surface",
             "correct": True},
            {"text": "Because uplift is what supplies the heat that melting "
                     "and metamorphism both need",
             "correct": False,
             "why": "The heat comes from inside the Earth. Uplift moves rock "
                    "rather than heating it"},
            {"text": "Because a rock cannot be weathered until it has been "
                     "lifted well above sea level",
             "correct": False,
             "why": "Rock is weathered wherever it meets the weather, and a "
                    "low coast weathers perfectly well"},
            {"text": "Because uplift is what breaks buried rock into the "
                     "fragments a river can carry",
             "correct": False,
             "why": "Weathering makes the fragments. Uplift simply delivers "
                    "the rock to where weathering can reach it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s29",
        "band": "standard",
        "text": "The stone of a cathedral wall was once sand on a beach. What "
                "had to happen in between?",
        "options": [
            {"text": "It had to be melted and cooled, which is what turns "
                     "loose sand into a solid block",
             "correct": False,
             "why": "A melted sand would cool as an igneous rock. Building "
                    "sandstone was never melted"},
            {"text": "It had to be metamorphosed, because only a metamorphic "
                     "rock is strong enough to build with",
             "correct": False,
             "why": "A great many buildings are sandstone and limestone, "
                    "neither of which is metamorphic"},
            {"text": "It had to be buried, compacted and cemented, and then "
                     "lifted and quarried",
             "correct": True},
            {"text": "Nothing had to happen at all",
             "correct": False,
             "why": "Loose sand cannot be cut into blocks. It had to become "
                    "rock first"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-s30",
        "band": "standard",
        "text": "Why is there sediment on the floor of every ocean?",
        "options": [
            {"text": "Because the sea floor itself is slowly crumbling into "
                     "sediment where the water touches it",
             "correct": False,
             "why": "Most of what lies there was worn off the land and carried "
                    "out, not made on the spot"},
            {"text": "Because sea water turns to solid grains once it has been "
                     "still for long enough",
             "correct": False,
             "why": "Sea water does not turn into sediment by standing still"},
            {"text": "Because volcanoes on the sea floor cover it in loose "
                     "fragments every year",
             "correct": False,
             "why": "Sea-floor volcanoes build igneous rock in places. The "
                    "sediment blanket comes from the land"},
            {"text": "Because rock at the surface everywhere is being worn "
                     "away and the pieces end up in the sea",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-03-h10",
        "band": "harder",
        "text": "Two rocks formed at the same moment and are in completely "
                "different groups a hundred million years later. How?",
        "options": [
            {"text": "One of them was made of harder minerals, and hard "
                     "minerals resist change",
             "correct": False,
             "why": "What a rock is made of does not fix its group. Marble and "
                    "limestone share a compound"},
            {"text": "One of them must have been misidentified, since rocks of "
                     "one age share a group",
             "correct": False,
             "why": "Age and group have nothing to do with one another. Rocks "
                    "of every age sit in all three groups"},
            {"text": "One of them stopped taking part in the cycle when it "
                     "reached its final form",
             "correct": False,
             "why": "No rock reaches a final form. Every one of them has "
                    "routes leading away from it"},
            {"text": "What happened to each afterwards depended on where each "
                     "one ended up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h11",
        "band": "harder",
        "text": "Which single fact about the rock cycle best explains why the "
                "Earth has mountains at all?",
        "options": [
            {"text": "Heat inside the Earth lifts rock faster than weathering "
                     "can take it away",
             "correct": True},
            {"text": "Sediment piles up on the land until the pile is high "
                     "enough to be called a mountain range",
             "correct": False,
             "why": "Sediment settles into low ground and into the sea. It "
                    "does not build upwards into ranges"},
            {"text": "Rock expands as it is weathered, so a weathered "
                     "landscape ends up higher than it started",
             "correct": False,
             "why": "Weathering removes material. A weathered landscape ends "
                    "up lower"},
            {"text": "Mountains never wear away",
             "correct": False,
             "why": "They wear away constantly, which is why rivers carry "
                    "sediment out of every range on Earth"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h12",
        "band": "harder",
        "text": "Weathering removes only millimetres in a human lifetime, yet "
                "whole mountain ranges disappear. Reconcile the two.",
        "options": [
            {"text": "The figure applies to hard rock, and mountains are made "
                     "of softer material",
             "correct": False,
             "why": "Ranges are built of hard rock. What removes them is time "
                    "rather than softness"},
            {"text": "Mountains are removed by a different and much faster "
                     "process than weathering",
             "correct": False,
             "why": "It is the same slow process, helped by erosion carrying "
                    "the pieces away"},
            {"text": "The figure is an underestimate, and modern measurements "
                     "give a much larger one",
             "correct": False,
             "why": "The figure is well measured. It is the timescale that is "
                    "hard to picture"},
            {"text": "A few millimetres each lifetime adds up over tens of "
                     "millions of years",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h13",
        "band": "harder",
        "text": "Compare what happens to rock buried a few kilometres down "
                "with what happens to rock driven far deeper under a "
                "collision.",
        "options": [
            {"text": "The shallower rock melts and the deeper rock is only "
                     "metamorphosed, because heat rises",
             "correct": False,
             "why": "That is the wrong way round. It gets hotter with depth, "
                    "not cooler"},
            {"text": "The shallower rock is metamorphosed; the deeper rock can "
                     "pass its melting point",
             "correct": True},
            {"text": "Both are metamorphosed, because nothing in the crust "
                     "ever passes its melting point",
             "correct": False,
             "why": "Magma is made in the crust, which is exactly rock passing "
                    "its melting point"},
            {"text": "Neither is changed",
             "correct": False,
             "why": "Both are changed. Burial is how the cycle delivers rock "
                    "to heat and pressure"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h14",
        "band": "harder",
        "text": "Depth on its own does not melt rock. What else has to be true "
                "before a buried rock becomes magma?",
        "options": [
            {"text": "It has to have been sedimentary first, because only "
                     "sediment can be melted",
             "correct": False,
             "why": "Any rock will melt in the right conditions, whatever it "
                    "was before"},
            {"text": "It has to be squeezed from one direction rather than "
                     "from every side at once",
             "correct": False,
             "why": "A squeeze from one direction makes a slate. It does not "
                    "melt anything"},
            {"text": "It has to have reached the very bottom of the crust, "
                     "where the mantle begins",
             "correct": False,
             "why": "The mantle is hotter still and is solid rock, so reaching "
                    "it settles nothing"},
            {"text": "It has to be hot enough, and wet enough, to pass its "
                     "melting point",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h15",
        "band": "harder",
        "text": "A rock is weathered, carried, deposited, buried and cemented, "
                "then lifted and weathered again, without ever being "
                "metamorphosed or melted. Is that a complete trip round the "
                "cycle?",
        "options": [
            {"text": "No, because a trip is only complete once the rock has "
                     "been through all three groups on the way",
             "correct": False,
             "why": "Nothing requires that. Arrows run across the middle of "
                    "the diagram for exactly this reason"},
            {"text": "Yes — the cycle is a set of routes, and that is one of "
                     "them",
             "correct": True},
            {"text": "No, because melting is the step that starts the cycle "
                     "off again",
             "correct": False,
             "why": "There is no step that starts the cycle. It has no "
                    "beginning to start from"},
            {"text": "Yes, but only because the rock ended up where it began",
             "correct": False,
             "why": "Ending where it began is not the test either. The route "
                    "is valid whether or not it returns"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h16",
        "band": "harder",
        "text": "Why does a sea floor collect sediment while a mountain top "
                "loses it?",
        "options": [
            {"text": "Because the sea is colder, and cold water holds sediment "
                     "better",
             "correct": False,
             "why": "Temperature is not what decides it. Moving water carries "
                    "and slow water drops"},
            {"text": "Because a mountain has no rock left to lose, so nothing "
                     "can settle on it",
             "correct": False,
             "why": "A mountain is solid rock and is losing it continually"},
            {"text": "Because sediment is made in the sea and is carried "
                     "uphill only by a flood",
             "correct": False,
             "why": "Most sediment is made on land by weathering and is "
                    "carried downhill from there"},
            {"text": "Because gravity moves loose material downhill, and it is "
                     "dropped where the water finally slows",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h17",
        "band": "harder",
        "text": "A geologist reads a sandstone and says a river once drained a "
                "granite highland here. What chain of reasoning gets from the "
                "rock to that claim?",
        "options": [
            {"text": "The sandstone must have been a granite itself before it "
                     "was buried and squeezed into grains",
             "correct": False,
             "why": "Squeezing a granite does not make separate grains. "
                    "Weathering broke the granite up first"},
            {"text": "The sandstone lies near a granite today, so the two must "
                     "have been made together at the same moment",
             "correct": False,
             "why": "The grains are the evidence, not the modern map. A river "
                    "can carry sand a very long way"},
            {"text": "The grains match the minerals of granite, so they were "
                     "broken off granite, carried and cemented",
             "correct": True},
            {"text": "Sandstone is always made from granite",
             "correct": False,
             "why": "Sand can come from any rock that weathers into grains of "
                    "that size"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h18",
        "band": "harder",
        "text": "Some steps of the cycle take days. Why does a complete "
                "circuit still take hundreds of millions of years?",
        "options": [
            {"text": "Because the slowest steps — burial, heating and cooling "
                     "at depth — set the pace of the whole thing",
             "correct": True},
            {"text": "Because every step has to wait for the one before it to "
                     "finish everywhere on Earth first",
             "correct": False,
             "why": "The processes run all over the planet at once. Nothing "
                    "waits for anything else"},
            {"text": "Because a rock can only move round the cycle when a "
                     "collision between continents pushes it",
             "correct": False,
             "why": "Weathering, erosion and deposition run constantly with no "
                    "collision needed"},
            {"text": "Because the cycle is paused for most of that time and "
                     "runs only in short bursts",
             "correct": False,
             "why": "It never pauses. Some of its steps are simply very slow"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h19",
        "band": "harder",
        "text": "A rock has been round the cycle several times. Which of its "
                "features records the EARLIEST of those trips?",
        "options": [
            {"text": "Its layers, which survive every trip and stack up one "
                     "set for each circuit it has made",
             "correct": False,
             "why": "Layers are among the first things a later process "
                    "destroys, and no stack of them survives"},
            {"text": "Its fossils, which are added to on each pass and so "
                     "record every trip it has ever made",
             "correct": False,
             "why": "Nothing is added to solid rock. Fossils are destroyed by "
                    "metamorphism and by melting"},
            {"text": "Its crystals, which keep the shape they were given the "
                     "very first time the rock formed",
             "correct": False,
             "why": "Crystals are regrown or remelted on later trips, so they "
                    "record the most recent one"},
            {"text": "None of them — each trip rebuilds the rock, so only the "
                     "latest is recorded",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h20",
        "band": "harder",
        "text": "Why is the rock cycle a more useful model than a simple list "
                "of the three rock types?",
        "options": [
            {"text": "Because a list cannot be drawn on a page, and a cycle "
                     "can be drawn as a diagram with arrows on it",
             "correct": False,
             "why": "Being drawable is not what makes a model useful. What it "
                    "explains is"},
            {"text": "Because the cycle names more rocks than a list of three "
                     "types ever could manage to name",
             "correct": False,
             "why": "The cycle names no extra rocks. It names the routes "
                    "between the three"},
            {"text": "Because it says how each type becomes the others and "
                     "what decides the route",
             "correct": True},
            {"text": "Because a list is wrong",
             "correct": False,
             "why": "The three types are correct. The list is simply less "
                    "informative than the cycle"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h21",
        "band": "harder",
        "text": "A sedimentary rock and an igneous rock turn out to be exactly "
                "the same age. Explain how that can happen.",
        "options": [
            {"text": "Lava erupted onto a sea floor while sediment was "
                     "settling close by",
             "correct": True},
            {"text": "One of the two must have been dated wrongly, because "
                     "each group belongs to a different period of time",
             "correct": False,
             "why": "The groups are routes rather than periods. All three have "
                    "formed throughout the Earth's history"},
            {"text": "The igneous rock turned into the sedimentary rock at the "
                     "moment it was dated",
             "correct": False,
             "why": "That change needs weathering, transport and burial, which "
                    "take an enormous time"},
            {"text": "They cannot be the same age",
             "correct": False,
             "why": "They can. The three routes are all running everywhere, "
                    "all of the time"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h22",
        "band": "harder",
        "text": "The cycle has run for over four billion years. Why has the "
                "sea not simply filled up with sediment and stopped?",
        "options": [
            {"text": "Because sediment dissolves back into the sea water once "
                     "it has been lying there for long enough",
             "correct": False,
             "why": "Sediment does not dissolve away. It is buried and turned "
                    "into rock"},
            {"text": "Because the amount of rock at the surface of the land "
                     "has not fallen since the Earth first formed",
             "correct": False,
             "why": "Land is being worn down constantly. What keeps it there "
                    "is uplift"},
            {"text": "Because the rate at which rivers deliver sediment has "
                     "fallen to almost nothing over that time",
             "correct": False,
             "why": "Rivers carry as much as they ever did. The sea floor is "
                    "emptied rather than the rivers slowing"},
            {"text": "Because it is buried, lifted and returned to the land, "
                     "or dragged down where plates meet",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h23",
        "band": "harder",
        "text": "Which is the stronger evidence that ROCK ITSELF moves: marine "
                "fossils near the top of a mountain, or sand on a beach?",
        "options": [
            {"text": "The sand, because a beach is made entirely of material "
                     "that has been carried there from somewhere else",
             "correct": False,
             "why": "Sand shows that FRAGMENTS move. The fossils show a whole "
                    "body of rock was lifted"},
            {"text": "The fossils, because they show solid rock was lifted "
                     "kilometres above where it formed",
             "correct": True},
            {"text": "The sand, because the grains in it are rounded and rock "
                     "that has not moved is angular",
             "correct": False,
             "why": "Rounding is good evidence that fragments travelled, and "
                    "it says nothing about solid rock"},
            {"text": "Neither is any use as evidence about whether rock moves",
             "correct": False,
             "why": "Both are evidence, and one of the two is a great deal "
                    "stronger than the other"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h24",
        "band": "harder",
        "text": "Why does a geologist care how LONG each process takes, and "
                "not only what order they come in?",
        "options": [
            {"text": "Because the order of the processes changes depending on "
                     "how long each one of them happens to take",
             "correct": False,
             "why": "A grain cannot be dropped before it is carried, however "
                    "long either step takes"},
            {"text": "Because the times are what make the cycle a timetable "
                     "that every rock has to keep to",
             "correct": False,
             "why": "The times are the evidence that it is NOT a timetable. "
                    "They differ enormously"},
            {"text": "Because the rates decide what a landscape looks like "
                     "now, and the cycle is not a schedule",
             "correct": True},
            {"text": "Because a faster process is more important",
             "correct": False,
             "why": "Speed does not rank importance. Compaction is slow and "
                    "indispensable"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h25",
        "band": "harder",
        "text": "A student claims that because rock is recycled, nothing on "
                "Earth is ever lost. Evaluate that.",
        "options": [
            {"text": "The material is not lost, and the record of what the "
                     "rock used to be is destroyed every time it melts",
             "correct": True},
            {"text": "It is correct, because melting and metamorphism leave "
                     "the rock unchanged",
             "correct": False,
             "why": "Both change it, and melting erases everything about its "
                    "previous form"},
            {"text": "It is wrong, because material really is destroyed at "
                     "every stage",
             "correct": False,
             "why": "The atoms survive the whole cycle. What is lost is the "
                    "record"},
            {"text": "It is wrong, because rock is not recycled at all",
             "correct": False,
             "why": "Recycling rock is exactly what the cycle does"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h26",
        "band": "harder",
        "text": "Suppose weathering stopped everywhere tomorrow. Which parts "
                "of the cycle would stop with it, and which would not?",
        "options": [
            {"text": "Everything would stop, because weathering is the first "
                     "step and every other step follows it in turn",
             "correct": False,
             "why": "There is no first step, and what is already buried would "
                    "carry on being heated and melted"},
            {"text": "Nothing would stop, because the other processes can all "
                     "make their own material without weathering",
             "correct": False,
             "why": "Erosion and deposition have nothing to move once no new "
                    "fragments are being made"},
            {"text": "Only melting would stop, because a melt is made out of "
                     "freshly weathered material",
             "correct": False,
             "why": "A melt is made from buried rock of any kind. Melting is "
                    "the part least affected"},
            {"text": "Erosion, transport and deposition would run out of "
                     "material; burial and melting would carry on",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h27",
        "band": "harder",
        "text": "Why is it fair to call weathering a chemical process as well "
                "as a physical one?",
        "options": [
            {"text": "Because breaking a rock into smaller pieces is itself a "
                     "chemical change to the material in it",
             "correct": False,
             "why": "Breaking something up changes its size and not its "
                    "chemistry. That part is purely physical"},
            {"text": "Because the rain freezing in a crack is a chemical "
                     "reaction between water and rock",
             "correct": False,
             "why": "Freezing is a change of state. Nothing reacts with "
                    "anything"},
            {"text": "Because slightly acidic rain reacts with the minerals "
                     "and changes what the rock is made of",
             "correct": True},
            {"text": "Because rock gives off gas as it weathers",
             "correct": False,
             "why": "Weathering limestone does release carbon dioxide, and the "
                    "reason it counts as chemical is the reaction itself"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h28",
        "band": "harder",
        "text": "Compare what the rock cycle is doing to a mountain range with "
                "what it is doing to a sea floor.",
        "options": [
            {"text": "Both are being taken apart, because weathering reaches "
                     "the sea floor just as it reaches the land above it",
             "correct": False,
             "why": "Weathering is a surface process on land. A sea floor is "
                    "collecting material rather than losing it"},
            {"text": "One is being taken apart and the other built up, and the "
                     "material moves from the first to the second",
             "correct": True},
            {"text": "Both are being built up, because sediment settles onto a "
                     "mountain top as readily as onto a sea floor",
             "correct": False,
             "why": "Loose material moves downhill off a mountain. Nothing "
                    "settles and stays on a summit"},
            {"text": "One is being melted and the other frozen",
             "correct": False,
             "why": "Neither is happening at the surface. The exchange is "
                    "between wearing away and settling"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h29",
        "band": "harder",
        "text": "An igneous, a sedimentary and a metamorphic rock all lie at "
                "the surface of one hillside. What does that say about its "
                "history?",
        "options": [
            {"text": "That the hillside is where all three types were "
                     "originally made, side by side at the same moment",
             "correct": False,
             "why": "The three form in different conditions, and none of them "
                    "forms at the surface of a hill"},
            {"text": "That rock from different parts of the cycle has been "
                     "brought together by uplift and erosion",
             "correct": True},
            {"text": "That the rocks are all the same age and were simply "
                     "given three different names by geologists",
             "correct": False,
             "why": "The three names record three different routes. They are "
                    "not labels for one thing"},
            {"text": "That the hillside cannot be real, because a rock can "
                     "only be one of the three types at a time",
             "correct": False,
             "why": "There are three separate rocks here, each in one group. "
                    "Nothing is in two at once"},
        ],
        "figure": None,
    },
    {
        "id": "c10-03-h30",
        "band": "harder",
        "text": "Which single observation would do the most damage to the "
                "claim that the cycle has no fixed direction?",
        "options": [
            {"text": "Finding a metamorphic rock that had never been melted at "
                     "any point in its history",
             "correct": False,
             "why": "That is what metamorphism means. It supports the claim "
                    "rather than damaging it"},
            {"text": "Finding a sedimentary rock made of grains that came off "
                     "several completely different rocks",
             "correct": False,
             "why": "That is what a river delivers every day, and it shows "
                    "many routes meeting rather than one"},
            {"text": "Finding an igneous rock lying at the surface of a "
                     "continent thousands of miles from a volcano",
             "correct": False,
             "why": "Granite forms underground and is uncovered later, so this "
                    "is expected"},
            {"text": "Finding that every metamorphic rock in the world had "
                     "been sedimentary first",
             "correct": True},
        ],
        "figure": None,
    },
]
