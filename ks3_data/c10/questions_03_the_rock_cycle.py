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
]
