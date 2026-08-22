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
]
