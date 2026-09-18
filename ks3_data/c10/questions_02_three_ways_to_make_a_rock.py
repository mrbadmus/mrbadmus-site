"""C10 lesson 02 — Three ways to make a rock: twelve questions (MRB-281).

The lesson's argument is one shape: a rock's group is decided by HOW IT
FORMED, the rock still carries the evidence of which route it took, and one
clue almost never closes the decision on its own. The page teaches it with a
reference panel and six samples a student has to read and commit to.

These twelve probe the angles the mastery ladder leaves alone: what each route
actually does to the rock, why an acid fizz identifies a compound rather than a
group, why porosity follows from cementation, what a slate's sheets really are,
and what would have to be true of a rock found with fossils inside a band of
marble.

The distractors are built from the lesson's declared misconceptions.

`EARTH-05` (crystals mean igneous) drives the wrong options in e03, s01 and
h02. Each treats one observation as a decision.

`EARTH-06` (rocks are grouped by what they look like) drives e01, e04, s03 and
h04, where two rocks that look alike are in different groups, or two rocks that
look nothing alike are in the same one.

`EARTH-07` (metamorphic rock was melted and re-set) drives e02, s02, s04 and
h01. Melting is the line between metamorphic and igneous, and every one of
these turns on which side of it a rock stayed.

⚠️ **NO QUESTION ASKS FOR A ROCK NAME TO BE RECALLED.** Granite, basalt,
sandstone, limestone, marble and slate are on the page as WORKED EXAMPLES of
routes, and a bank question that rewards memorising the six names measures
whether a student read the bench rather than whether they can read a rock.
Every named rock below arrives with the evidence attached.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles through each
band — 2,0,3,1 · 1,3,0,2 · 0,2,1,3 — so this file holds three of each. The
ladder is a separate corpus and is balanced separately; see the lesson record.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "three-ways-to-make-a-rock"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-02-e01",
        "band": "easier",
        "text": "What decides which of the three groups a rock belongs to?",
        "options": [
            {"text": "Its colour, because each group has its own range of "
                     "colours",
             "correct": False,
             "why": "Granite, marble and sandstone all come in pale and dark "
                    "versions. Colour decides nothing."},
            {"text": "How hard it is, because the groups run from soft to "
                     "hard",
             "correct": False,
             "why": "Limestone is soft and sedimentary; slate is hard and "
                    "metamorphic; chalk is soft and also sedimentary."},
            {"text": "The way it formed",
             "correct": True},
            {"text": "How heavy it feels for its size",
             "correct": False,
             "why": "Density varies within every group. Two rocks of the same "
                    "weight can have taken completely different routes."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e02",
        "band": "easier",
        "text": "How does a metamorphic rock form?",
        "options": [
            {"text": "Existing rock is changed by heat and pressure without "
                     "melting",
             "correct": True},
            {"text": "Rock is melted underground and then cools into "
                     "something new",
             "correct": False,
             "why": "Melt a rock and what cools out of it is igneous. "
                    "Metamorphic rock stays solid the whole time."},
            {"text": "Grains of older rock settle in layers and are cemented "
                     "together",
             "correct": False,
             "why": "That is how a sedimentary rock forms."},
            {"text": "Crystals grow out of water as a lake dries up",
             "correct": False,
             "why": "Crystals left behind by evaporating water build a "
                    "sedimentary rock, not a metamorphic one."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e03",
        "band": "easier",
        "text": "Which observation is the strongest evidence that a rock is "
                "sedimentary?",
        "options": [
            {"text": "It is full of crystals that interlock like a jigsaw",
             "correct": False,
             "why": "Interlocking crystals point at igneous or metamorphic. "
                    "Sedimentary rock is separate grains sitting together."},
            {"text": "It is hard enough to scratch glass",
             "correct": False,
             "why": "Hardness belongs to the minerals in a rock, not to the "
                    "way the rock formed."},
            {"text": "It is dark grey almost all the way through",
             "correct": False,
             "why": "Basalt is dark grey and igneous; slate is dark grey and "
                    "metamorphic; mudstone is dark grey and sedimentary."},
            {"text": "It has a fossil shell visible on a broken surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e04",
        "band": "easier",
        "text": "An igneous rock has crystals large enough to see easily. "
                "What does that tell you about how it formed?",
        "options": [
            {"text": "The melt was much hotter than usual when it "
                     "crystallised",
             "correct": False,
             "why": "How hot the melt started does not set the crystal size. "
                    "How long it took to cool does."},
            {"text": "It cooled slowly, with time for the crystals to grow",
             "correct": True},
            {"text": "It has been buried for a very long time since it "
                     "formed",
             "correct": False,
             "why": "Crystals stop growing the moment the rock is solid. Age "
                    "afterwards changes nothing."},
            {"text": "It was squeezed hard while it was cooling down",
             "correct": False,
             "why": "Pressure is what changes a metamorphic rock. In igneous "
                    "rock the crystal size is set by cooling rate."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-02-s01",
        "band": "standard",
        "text": "A rock fizzes when a drop of dilute acid is put on it. What "
                "does the fizzing tell you?",
        "options": [
            {"text": "That it is a sedimentary rock, because only those "
                     "react",
             "correct": False,
             "why": "Marble fizzes too, and marble is metamorphic. The test "
                    "does not read the group."},
            {"text": "That it contains a carbonate",
             "correct": True},
            {"text": "That it is soft enough to be scratched with a coin",
             "correct": False,
             "why": "Marble fizzes and is far too hard to scratch with a "
                    "coin. The two properties are unrelated."},
            {"text": "That it has never been heated since it formed",
             "correct": False,
             "why": "Marble is limestone that was heated hard, and it still "
                    "fizzes. The carbonate survived."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s02",
        "band": "standard",
        "text": "Marble and limestone are both calcium carbonate, yet they "
                "are in different groups. Why?",
        "options": [
            {"text": "The marble melted and set again, which the limestone "
                     "never did",
             "correct": False,
             "why": "Nothing melted. Had the marble melted, what cooled out "
                    "of it would be an igneous rock."},
            {"text": "The marble is a purer form of the same compound than "
                     "the limestone",
             "correct": False,
             "why": "Purity is not what the groups are about. What the groups "
                    "record is how the rock was made."},
            {"text": "The limestone contains fossils and the marble contains "
                     "crystals",
             "correct": False,
             "why": "That is a symptom rather than the reason. The fossils "
                    "were destroyed and the crystals grew for the same "
                    "cause."},
            {"text": "The limestone was built up from shells; the marble is "
                     "limestone that heat and pressure changed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s03",
        "band": "standard",
        "text": "Sandstone soaks up a drop of water and granite does not. "
                "What explains the difference?",
        "options": [
            {"text": "Sandstone is made of separate grains with spaces "
                     "between them that the cement never filled",
             "correct": True},
            {"text": "Sandstone is softer, and soft rock always lets water "
                     "through",
             "correct": False,
             "why": "Marble is soft enough to carve and is not porous. It is "
                    "the spaces that matter, not the hardness."},
            {"text": "Granite is a darker rock, so water runs off it more "
                     "easily",
             "correct": False,
             "why": "Plenty of granite is pale. Colour has nothing to do with "
                    "whether water can get in."},
            {"text": "Sandstone is older, and rock becomes more absorbent "
                     "with age",
             "correct": False,
             "why": "Rock does not become porous by ageing. Sandstone was "
                    "porous from the day the grains were buried."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s04",
        "band": "standard",
        "text": "Why would you never expect to find a fossil in an igneous "
                "rock?",
        "options": [
            {"text": "Igneous rock forms too deep for any living thing to "
                     "have been there",
             "correct": False,
             "why": "Lava cools at the surface, where things live. The "
                    "problem is the temperature, not the depth."},
            {"text": "Igneous rock is too hard for a shell to have left a "
                     "mark in it",
             "correct": False,
             "why": "The rock was liquid before it was hard. Hardness is not "
                    "what destroys the remains."},
            {"text": "The rock was molten before it set, and nothing survives "
                     "that",
             "correct": True},
            {"text": "Igneous rock is far older than any living thing on "
                     "Earth",
             "correct": False,
             "why": "Igneous rock is still forming today, at every erupting "
                    "volcano."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-02-h01",
        "band": "harder",
        "text": "A student says metamorphic rock is rock that melted and set "
                "again as something different. What is wrong with that?",
        "options": [
            {"text": "Anything that melts and sets again is igneous, so a "
                     "rock that melted could not be metamorphic",
             "correct": True},
            {"text": "Rock deep enough to be changed is never hot enough to "
                     "melt, so the situation cannot arise",
             "correct": False,
             "why": "Rock does melt at depth — that is where magma comes "
                    "from. The point is what the melting would make it."},
            {"text": "Melted rock always reaches the surface as lava, so it "
                     "never stays underground to change",
             "correct": False,
             "why": "Plenty of magma cools underground; granite is what that "
                    "produces. It is still igneous."},
            {"text": "A rock that melted would lose its crystals, and "
                     "metamorphic rocks are full of them",
             "correct": False,
             "why": "Melting and re-cooling grows crystals rather than losing "
                    "them. Igneous rock is full of them too."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h02",
        "band": "harder",
        "text": "A rock is full of interlocking crystals. What have you "
                "actually learned, and what have you not?",
        "options": [
            {"text": "It must be igneous, and only the cooling rate is left "
                     "to work out",
             "correct": False,
             "why": "Marble and gneiss are full of interlocking crystals and "
                    "neither is igneous."},
            {"text": "It is metamorphic, because sedimentary and igneous "
                     "rocks are made of grains",
             "correct": False,
             "why": "Igneous rock is interlocking crystals, not grains. The "
                    "clue does not separate the two."},
            {"text": "It is not sedimentary, but igneous and metamorphic are "
                     "both still open",
             "correct": True},
            {"text": "Nothing useful, because every rock contains crystals of "
                     "some kind",
             "correct": False,
             "why": "It rules out a whole group. Sedimentary rock is separate "
                    "grains sitting side by side, not an interlocking mesh."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h03",
        "band": "harder",
        "text": "Slate splits cleanly into flat sheets. A student says the "
                "sheets are the layers of the mud it came from. Why is that "
                "probably wrong?",
        "options": [
            {"text": "Mudstone has no layers to begin with, so there is "
                     "nothing for the split to follow",
             "correct": False,
             "why": "Mudstone is sedimentary and does have layers. They are "
                    "simply not what the slate splits along."},
            {"text": "The split follows the direction the grains were "
                     "rotated into, which can cut across the old layers",
             "correct": True},
            {"text": "The layers were destroyed when the rock melted, so "
                     "nothing of them is left",
             "correct": False,
             "why": "Slate never melted. The layers can often still be seen "
                    "running across the split."},
            {"text": "Slate is igneous, so it never had sedimentary layers at "
                     "any point",
             "correct": False,
             "why": "Slate is metamorphic and started as mudstone, which is "
                    "sedimentary."},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h04",
        "band": "harder",
        "text": "A geologist walks along one rock face and finds fossils "
                "everywhere, then reaches a band where the same rock is "
                "crystalline and fossil-free. What is the best explanation?",
        "options": [
            {"text": "The animals that made the fossils only lived in part of "
                     "the sea, so that band never had any",
             "correct": False,
             "why": "The rock in the band is crystalline as well as "
                    "fossil-free. Both changes need explaining, not just "
                    "one."},
            {"text": "The two bands are unrelated rocks that happen to lie "
                     "next to each other",
             "correct": False,
             "why": "They are described as the same rock. The crystalline "
                    "band is the fossil-bearing rock, altered."},
            {"text": "The fossils in that band dissolved away later, leaving "
                     "crystals behind in the holes",
             "correct": False,
             "why": "Dissolved fossils leave moulds a geologist can see. This "
                    "band has an interlocking crystal texture throughout."},
            {"text": "The fossil-free band was heated and squeezed hard "
                     "enough for its crystals to grow and its fossils to be "
                     "destroyed",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-02-e05",
        "band": "easier",
        "text": "How does an igneous rock form?",
        "options": [
            {"text": "Fragments settle in layers on a sea floor and are "
                     "cemented together by minerals left behind as water "
                     "drains through the spaces between them",
             "correct": False,
             "why": "That is sedimentary. Nothing was ever molten"},
            {"text": "Molten rock cools and crystallises",
             "correct": True},
            {"text": "Existing rock is changed by heat and pressure",
             "correct": False,
             "why": "That is metamorphic, and the rock never melts"},
            {"text": "Shells build up and harden",
             "correct": False,
             "why": "That is one route to a sedimentary rock"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e06",
        "band": "easier",
        "text": "What does TEXTURE mean, in this lesson?",
        "options": [
            {"text": "How rough or smooth the surface of a rock feels when "
                     "you run a finger across a freshly broken face of it",
             "correct": False,
             "why": "That is the everyday sense. Here it means how the pieces "
                    "fit together"},
            {"text": "What colour the rock is",
             "correct": False,
             "why": "Colour is exactly what does NOT decide the group"},
            {"text": "How the pieces of a rock fit together — interlocking, "
                     "or separate grains side by side",
             "correct": True},
            {"text": "How heavy the rock is for its size, weighed on a balance "
                     "and set beside a block of the same size",
             "correct": False,
             "why": "That is density, and it does not decide the group "
                    "either"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e07",
        "band": "easier",
        "text": "What is cementation?",
        "options": [
            {"text": "Molten rock setting between the grains",
             "correct": False,
             "why": "Nothing melts. The minerals come out of water"},
            {"text": "Grains being pressed so hard by the weight of everything "
                     "above them that they fuse into one solid mass",
             "correct": False,
             "why": "Compaction squeezes them together and the cement is what "
                    "holds them"},
            {"text": "Grains being baked together by the heat of the rock "
                     "around them, in the same way that clay is fired into a "
                     "brick in a kiln",
             "correct": False,
             "why": "Nothing is baked. Sedimentary rock forms near the "
                    "surface, and the sticking is done by minerals"},
            {"text": "Minerals left by water in the spaces between buried "
                     "grains, sticking them into solid rock",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e08",
        "band": "easier",
        "text": "An igneous rock has crystals too small to see. What does "
                "that tell you?",
        "options": [
            {"text": "It cooled quickly, at or near the surface",
             "correct": True},
            {"text": "It cooled slowly and deep underground, and the crystals "
                     "had so long to grow that they packed tightly together "
                     "and ended up very small",
             "correct": False,
             "why": "Long growth makes crystals LARGE. Small ones mean there "
                    "was no time"},
            {"text": "It is very old",
             "correct": False,
             "why": "Crystals stop growing the moment the melt solidifies. "
                    "Age changes nothing"},
            {"text": "It is sedimentary, because only settling sediment makes "
                     "grains that fine",
             "correct": False,
             "why": "It is stated to be igneous. Fine grain size is about how "
                    "fast it cooled"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e09",
        "band": "easier",
        "text": "Which group does a rock belong to if its grains sit side by "
                "side with spaces between them, in visible layers?",
        "options": [
            {"text": "Igneous, because the layers are the different batches "
                     "of molten rock that flowed out one after another and "
                     "set on top of each other",
             "correct": False,
             "why": "Lava flows do stack up, and an igneous rock's crystals "
                    "INTERLOCK. Separate grains with gaps is sedimentary"},
            {"text": "Sedimentary",
             "correct": True},
            {"text": "Metamorphic",
             "correct": False,
             "why": "Metamorphic rock is banded or swirled and its grains do "
                    "not sit loose with gaps"},
            {"text": "It cannot be told from the texture",
             "correct": False,
             "why": "Texture is exactly what decides the group"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-02-s05",
        "band": "standard",
        "text": "Granite has crystals several millimetres across and basalt's "
                "are too small to see. Both are igneous. Where did each "
                "form?",
        "options": [
            {"text": "The granite at the surface, the basalt deep "
                     "underground, because a rock exposed to the open air has "
                     "far longer to grow its crystals than one buried under "
                     "pressure does",
             "correct": False,
             "why": "Exactly backwards. The surface is where a melt cools "
                    "FAST"},
            {"text": "The granite deep underground, the basalt at or near the "
                     "surface",
             "correct": True},
            {"text": "Both at the surface, at different times",
             "correct": False,
             "why": "Then both would be fine-grained. The crystal size is the "
                    "clue to depth"},
            {"text": "Both underground, at different depths only, with the "
                     "granite nearer the surface",
             "correct": False,
             "why": "Basalt's tiny crystals mean it cooled far too fast to "
                    "have been buried"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s06",
        "band": "standard",
        "text": "Why does texture decide the group, when colour, hardness "
                "and weight do not?",
        "options": [
            {"text": "Because texture never varies within a group, so every "
                     "igneous rock has exactly the same one",
             "correct": False,
             "why": "It varies a good deal — igneous crystals run from "
                    "invisible to centimetres. What it always records is the "
                    "process"},
            {"text": "Because texture is the only property that can be "
                     "measured accurately, and colour, hardness and weight "
                     "all depend on who is doing the looking",
             "correct": False,
             "why": "Hardness and density are measured precisely every day. "
                    "They just do not record the rock's history"},
            {"text": "Because texture is a record of HOW the rock formed, and "
                     "the others are not",
             "correct": True},
            {"text": "Because the other three are hard to see",
             "correct": False,
             "why": "Colour is the easiest thing to see about a rock, and it "
                    "is the least use"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s07",
        "band": "standard",
        "text": "A rock is full of interlocking crystals AND shows banding "
                "and swirls. Which group?",
        "options": [
            {"text": "Sedimentary",
             "correct": False,
             "why": "Sedimentary grains sit side by side with gaps. Nothing "
                    "interlocks"},
            {"text": "It cannot be told",
             "correct": False,
             "why": "Two observations together narrow it to one group, which "
                    "is how identification works"},
            {"text": "Igneous, since interlocking crystals are exactly what a "
                     "melt produces as it cools and nothing else in the three "
                     "groups makes them",
             "correct": False,
             "why": "Metamorphic rock grows interlocking crystals too, and "
                    "the banding and swirls are the giveaway"},
            {"text": "Metamorphic",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s08",
        "band": "standard",
        "text": "Coal is made from the remains of plants buried in a swamp. "
                "Which group does that put it in?",
        "options": [
            {"text": "Sedimentary",
             "correct": True},
            {"text": "Metamorphic, because the plant material was changed by "
                     "the heat and pressure of being buried under everything "
                     "that was laid down on top of it afterwards",
             "correct": False,
             "why": "Burial and compression form it, and the route is "
                    "material settling in layers — which is what sedimentary "
                     "means"},
            {"text": "Igneous",
             "correct": False,
             "why": "Nothing was ever molten. Coal would burn long before it "
                    "melted"},
            {"text": "None of the three",
             "correct": False,
             "why": "Every rock formed one of the three ways, and coal formed "
                    "by material settling and being buried"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s09",
        "band": "standard",
        "text": "Two rocks look almost identical to the eye — both grey, both "
                "hard, both heavy. What would you do next?",
        "options": [
            {"text": "Weigh both of them carefully and compare the two "
                     "figures, since two rocks of the same size that weigh "
                     "differently must have formed in different ways",
             "correct": False,
             "why": "Density varies within every group. It does not sort "
                    "them"},
            {"text": "Look at how the pieces fit together, and check for "
                     "layers or fossils",
             "correct": True},
            {"text": "Assume they are the same kind of rock, since two rocks "
                     "that look alike must have formed alike",
             "correct": False,
             "why": "That is the misconception this lesson exists to kill. "
                    "Looking alike is not being alike"},
            {"text": "Compare their colours in better light",
             "correct": False,
             "why": "Colour decides nothing at all"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-02-h05",
        "band": "harder",
        "text": "Read a cliff face from bottom to top. What are you reading, "
                "and why in that direction?",
        "options": [
            {"text": "Depth in order, because the layers nearer the bottom "
                     "were buried more deeply and are therefore more strongly "
                     "compressed than the ones above them",
             "correct": False,
             "why": "They were buried more deeply, and what the sequence "
                    "records is TIME — oldest at the bottom"},
            {"text": "Time in order, because each layer settled on top of the "
                     "one before it",
             "correct": True},
            {"text": "Nothing in order — layers can form in any sequence, so "
                     "the order tells you nothing at all",
             "correct": False,
             "why": "Sediment falls downwards, so a layer cannot arrive "
                    "beneath one that is already there"},
            {"text": "Time in order, oldest at the top",
             "correct": False,
             "why": "The right idea upside down. The bottom layer arrived "
                    "first"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h06",
        "band": "harder",
        "text": "Slate splits into flat sheets. What does the DIRECTION of "
                "the split record?",
        "options": [
            {"text": "The direction of the water that carried the mud into "
                     "place before it was ever buried",
             "correct": False,
             "why": "That is long gone by the time the rock is squeezed. The "
                    "split records the metamorphism"},
            {"text": "The direction the mud was originally laid down in, "
                     "since the sheets are the old bedding planes of the "
                     "sediment showing through the finished rock",
             "correct": False,
             "why": "The split can cut clean across the old bedding. It "
                    "follows the pressure instead"},
            {"text": "The direction the squeeze came from, which rotated the "
                     "grains into line",
             "correct": True},
            {"text": "Nothing — the split is random",
             "correct": False,
             "why": "It is highly regular, which is why slate can be split "
                    "into roofing sheets at all"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h07",
        "band": "harder",
        "text": "A band of marble runs through limestone beside an old "
                "igneous intrusion. Put the events in order.",
        "options": [
            {"text": "The marble formed first, and some of it then cooled "
                     "slowly enough that it turned back into limestone again",
             "correct": False,
             "why": "Metamorphism does not reverse on cooling. Marble stays "
                    "marble"},
            {"text": "All three formed at the same moment",
             "correct": False,
             "why": "The marble is found closest to the intrusion, which is "
                    "the mark of one event heating another"},
            {"text": "The intrusion arrived first and cooled, and the "
                     "limestone was then laid down around it and turned to "
                     "marble by the heat still left in the cooling rock",
             "correct": False,
             "why": "The marble is limestone that was ALREADY there. Heat "
                    "cannot change rock that has not formed yet"},
            {"text": "The limestone formed, then the intrusion arrived and "
                     "its heat changed the rock nearest to it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h08",
        "band": "harder",
        "text": "A rock is heated until it melts, and the melt then cools. "
                "What group is the result, and why does the answer matter?",
        "options": [
            {"text": "Igneous, because anything that cools out of a melt is "
                     "igneous whatever it was before",
             "correct": True},
            {"text": "Metamorphic, because the rock has been changed by heat "
                     "and heat is what makes a metamorphic rock out of "
                     "whatever it started as",
             "correct": False,
             "why": "Metamorphism happens WITHOUT melting. Melt it and the "
                    "history is erased"},
            {"text": "Whatever it was before, because melting changes nothing "
                     "that decides which group a rock belongs to",
             "correct": False,
             "why": "Melting erases the texture entirely, and texture is what "
                    "the group records"},
            {"text": "Sedimentary, if it was sedimentary to begin with",
             "correct": False,
             "why": "Nothing survives melting. The new texture is "
                    "interlocking crystals"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h09",
        "band": "harder",
        "text": "A sandstone's grains are all about the same size and "
                "beautifully rounded. What does that suggest about their "
                "journey?",
        "options": [
            {"text": "A short one, because grains carried a long way are "
                     "ground down into a mixture of every size from boulders "
                     "to dust before they are finally dropped",
             "correct": False,
             "why": "A long journey SORTS by size, because the heaviest are "
                    "dropped first. A short one leaves them mixed"},
            {"text": "A long one — they were knocked round and sorted by size "
                     "as they were carried",
             "correct": True},
            {"text": "That they were never carried at all",
             "correct": False,
             "why": "Fragments that stay where they fall are angular and all "
                    "sizes together — a scree slope"},
            {"text": "That they formed as crystals in a melt, and were "
                     "therefore never carried by water at all",
             "correct": False,
             "why": "Crystals from a melt interlock. These are separate "
                    "grains"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-02-e10",
        "band": "easier",
        "text": "What is compaction?",
        "options": [
            {"text": "The weight of later layers pressing buried sediment "
                     "together and forcing the water out",
             "correct": True},
            {"text": "The sticking of loose grains together by minerals that "
                     "water leaves behind in the gaps",
             "correct": False,
             "why": "That is cementation. Compaction is the squeezing that "
                    "comes before it"},
            {"text": "The melting of buried sediment into one solid mass",
             "correct": False,
             "why": "Nothing melts. Sedimentary rock forms far too near the "
                    "surface for that"},
            {"text": "The breaking of a rock into smaller pieces where it "
                     "lies",
             "correct": False,
             "why": "That happens at the surface, before anything has been "
                    "buried at all"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e11",
        "band": "easier",
        "text": "The crystals in a granite are described as INTERLOCKING. "
                "What does that mean?",
        "options": [
            {"text": "They are all exactly the same size as one another",
             "correct": False,
             "why": "Granite's pink, white and black crystals come in a range "
                    "of sizes"},
            {"text": "They grew into one another and fit together with no "
                     "gaps",
             "correct": True},
            {"text": "They are arranged in stripes that run right across the "
                     "rock",
             "correct": False,
             "why": "Stripes and bands are a metamorphic feature, and that is "
                    "not what interlocking means"},
            {"text": "They can be picked out of the rock one at a time with a "
                     "fingernail",
             "correct": False,
             "why": "Separate pieces that rub off are the grains of a "
                    "sedimentary rock"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e12",
        "band": "easier",
        "text": "Which group of rocks is most likely to soak up a drop of "
                "water?",
        "options": [
            {"text": "Igneous, because a melt cools unevenly and cracks as it "
                     "shrinks",
             "correct": False,
             "why": "An igneous rock's crystals interlock, so there are no "
                    "spaces for water to get into"},
            {"text": "Metamorphic, because squeezing opens the rock along the "
                     "direction it splits",
             "correct": False,
             "why": "Squeezing closes spaces rather than opening them, and a "
                    "slate roof keeps water out"},
            {"text": "Sedimentary, because the cement never fills every space "
                     "between the grains",
             "correct": True},
            {"text": "All three equally, since every rock has spaces of some "
                     "size in it",
             "correct": False,
             "why": "Only one of the three is built from separate grains with "
                    "gaps left between them"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e13",
        "band": "easier",
        "text": "Slate has roofed buildings for centuries. Which of its "
                "properties is the reason?",
        "options": [
            {"text": "It is the hardest rock there is",
             "correct": False,
             "why": "Slate is not especially hard, and hardness is not what a "
                    "roof tile needs"},
            {"text": "It fizzes with dilute acid",
             "correct": False,
             "why": "Slate does not fizz, and a rock that did would be "
                    "attacked by rain rather than protected from it"},
            {"text": "It is pale, so it reflects the sun",
             "correct": False,
             "why": "Slate is dark grey, and colour has nothing to do with "
                    "why it is used"},
            {"text": "It splits cleanly into thin flat sheets",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e14",
        "band": "easier",
        "text": "Polished granite is a popular material for a kitchen "
                "worktop. Which property makes it suitable?",
        "options": [
            {"text": "Its crystals interlock with no spaces, so a spill cannot "
                     "soak in",
             "correct": True},
            {"text": "It is sedimentary, and sedimentary rock takes a polish "
                     "better than any other",
             "correct": False,
             "why": "Granite is igneous, and taking a polish is a property of "
                    "a surface rather than of a group"},
            {"text": "It fizzes with acid, which keeps the surface of it "
                     "clean",
             "correct": False,
             "why": "Granite holds no carbonate and does not fizz at all"},
            {"text": "It splits into flat sheets, so the worktop can be cut to "
                     "any thickness",
             "correct": False,
             "why": "That is slate. Granite does not split along any "
                    "direction"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e15",
        "band": "easier",
        "text": "What happens to the fossils in a rock that heat and pressure "
                "change?",
        "options": [
            {"text": "They are baked hard and come out better preserved than "
                     "before",
             "correct": False,
             "why": "Heat and pressure wreck them. Nothing about metamorphism "
                    "preserves a shell"},
            {"text": "They are destroyed, or distorted until nobody can "
                     "recognise them",
             "correct": True},
            {"text": "They sink through the rock and gather in one layer",
             "correct": False,
             "why": "Nothing moves through solid rock. They stay where they "
                    "are and are wrecked in place"},
            {"text": "They turn into crystals of the same shape",
             "correct": False,
             "why": "The crystals in a marble grow at the expense of the "
                    "fossils rather than into their shapes"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e16",
        "band": "easier",
        "text": "Limestone and marble are made of the same chemical compound. "
                "Which one?",
        "options": [
            {"text": "Quartz",
             "correct": False,
             "why": "Quartz is the mineral of sand and of granite, and it does "
                    "not fizz with acid"},
            {"text": "Iron oxide",
             "correct": False,
             "why": "Iron oxide is rust, and neither rock is built from it"},
            {"text": "Calcium carbonate",
             "correct": True},
            {"text": "Calcium sulfate",
             "correct": False,
             "why": "Calcium sulfate does not fizz with acid. A fizz is the "
                    "test for a carbonate, and both rocks fizz"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e17",
        "band": "easier",
        "text": "Slate is metamorphic, so it was a different rock first. "
                "Which one?",
        "options": [
            {"text": "Granite",
             "correct": False,
             "why": "Granite is igneous and coarse. Squeezing it does not make "
                    "slate"},
            {"text": "Limestone",
             "correct": False,
             "why": "Heated and squeezed limestone becomes marble, which "
                    "fizzes. Slate does not"},
            {"text": "Basalt",
             "correct": False,
             "why": "Basalt is a fine-grained igneous rock and is not what "
                    "slate was made from"},
            {"text": "Mudstone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e18",
        "band": "easier",
        "text": "A limestone has been cooked and squeezed until its crystals "
                "grew and its fossils were wrecked. What is it now?",
        "options": [
            {"text": "Marble",
             "correct": True},
            {"text": "Limestone, unchanged",
             "correct": False,
             "why": "A rock's group records what happened to it, and heat and "
                    "pressure have happened to this one"},
            {"text": "Granite",
             "correct": False,
             "why": "Granite crystallises out of a melt, and nothing here "
                    "melted. Growing crystals is not enough on its own"},
            {"text": "Sandstone",
             "correct": False,
             "why": "Sandstone is made of separate sand grains, and this rock "
                    "never was"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e19",
        "band": "easier",
        "text": "Which of these rocks formed by cooling from molten rock?",
        "options": [
            {"text": "Sandstone",
             "correct": False,
             "why": "Sandstone is sand that was dropped, buried and cemented. "
                    "Nothing melted"},
            {"text": "Granite",
             "correct": True},
            {"text": "Slate",
             "correct": False,
             "why": "Slate is mudstone that heat and pressure changed while it "
                    "stayed solid"},
            {"text": "Limestone",
             "correct": False,
             "why": "Limestone is built up from the remains of sea creatures "
                    "on a sea floor"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e20",
        "band": "easier",
        "text": "Which of these rocks was built up from the remains of sea "
                "creatures?",
        "options": [
            {"text": "Basalt, which cooled from lava at the surface",
             "correct": False,
             "why": "A melt at over 700 °C destroys anything organic. Basalt "
                    "holds no remains"},
            {"text": "Granite, which cooled slowly a long way down",
             "correct": False,
             "why": "Granite crystallised out of a melt too, and nothing "
                    "living survives that"},
            {"text": "Limestone, which shows shell shapes on a broken surface",
             "correct": True},
            {"text": "Slate, which splits into thin flat sheets",
             "correct": False,
             "why": "Slate was mud, and the pressure that changed it wrecked "
                    "anything that had been in the mud"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e21",
        "band": "easier",
        "text": "Every rock on Earth belongs to one of three groups. What are "
                "the three?",
        "options": [
            {"text": "Hard, soft and crumbly",
             "correct": False,
             "why": "Those are properties of the rock in your hand, and every "
                    "group contains all three"},
            {"text": "Crystal, grain and layer",
             "correct": False,
             "why": "Those are things you look at to decide a group. They are "
                    "not the groups"},
            {"text": "Volcanic, ocean and mountain",
             "correct": False,
             "why": "Those are places rock is found rather than ways rock is "
                    "made"},
            {"text": "Igneous, sedimentary and metamorphic",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e22",
        "band": "easier",
        "text": "Which of these observations would NOT help you decide which "
                "group a rock belongs to?",
        "options": [
            {"text": "Whether it is pale or dark",
             "correct": True},
            {"text": "Whether its crystals interlock",
             "correct": False,
             "why": "That is texture, and texture is the observation that "
                    "decides it"},
            {"text": "Whether it has visible layers",
             "correct": False,
             "why": "Layers point at material that settled, which is the "
                    "sedimentary route"},
            {"text": "Whether it splits into sheets",
             "correct": False,
             "why": "Splitting cleanly along one direction is a metamorphic "
                    "fabric, and it is strong evidence"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e23",
        "band": "easier",
        "text": "Which group of rocks was a different rock first, and was then "
                "changed?",
        "options": [
            {"text": "Igneous",
             "correct": False,
             "why": "The melt it cooled from was rock, and an igneous rock is "
                    "defined by cooling from one however that melt arose"},
            {"text": "Metamorphic",
             "correct": True},
            {"text": "Sedimentary",
             "correct": False,
             "why": "Its grains were broken off older rock, and the rock "
                    "itself is built up rather than changed"},
            {"text": "All three of them",
             "correct": False,
             "why": "One group is defined by having been a different rock and "
                    "then changed. The other two are not"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e24",
        "band": "easier",
        "text": "The grains of a sandstone rub off on your fingers. What does "
                "that say about how they are held together?",
        "options": [
            {"text": "They were welded by heat that never quite reached the "
                     "surface of the rock",
             "correct": False,
             "why": "Nothing in a sandstone is welded or baked. It forms near "
                    "the surface"},
            {"text": "They interlock, and the outer ones have worn until they "
                     "no longer fit",
             "correct": False,
             "why": "Separate grains never interlocked. That is what makes "
                    "them separate"},
            {"text": "A cement holds them, and it is weak enough to give way",
             "correct": True},
            {"text": "Nothing holds them, so the rock is only a heap of loose "
                     "sand",
             "correct": False,
             "why": "The rock is solid and can be cut into blocks, so "
                    "something is holding it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e25",
        "band": "easier",
        "text": "What is a fossil?",
        "options": [
            {"text": "A rock that is older than the rocks lying around it",
             "correct": False,
             "why": "A fossil is a record of a living thing rather than a kind "
                    "of rock"},
            {"text": "A crystal that happened to grow into the shape of a "
                     "shell",
             "correct": False,
             "why": "The shape comes from something that was once alive, not "
                    "from a crystal growing that way"},
            {"text": "Any pattern in a rock that resembles a plant or an "
                     "animal",
             "correct": False,
             "why": "Something that merely looks like one is not a fossil. The "
                    "remains have to be genuine"},
            {"text": "The preserved remains or shape of a living thing, buried "
                     "in rock",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e26",
        "band": "easier",
        "text": "Lava reaches the surface and cools in a matter of days. Which "
                "rock is the result?",
        "options": [
            {"text": "Basalt",
             "correct": True},
            {"text": "Granite",
             "correct": False,
             "why": "Granite's crystals are millimetres across, which takes "
                    "far longer than days, and it cools well underground"},
            {"text": "Marble",
             "correct": False,
             "why": "Marble is limestone changed by heat and pressure without "
                    "melting"},
            {"text": "Sandstone",
             "correct": False,
             "why": "Sandstone is sand that was dropped, buried and cemented"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e27",
        "band": "easier",
        "text": "A body of magma stalls several kilometres down and takes an "
                "enormous time to cool. Which rock does it become?",
        "options": [
            {"text": "Basalt",
             "correct": False,
             "why": "Basalt's crystals are too small to see, which means it "
                    "cooled in days at or near the surface"},
            {"text": "Granite",
             "correct": True},
            {"text": "Slate",
             "correct": False,
             "why": "Slate is mudstone that was squeezed, and nothing about it "
                    "came out of a melt"},
            {"text": "Mudstone",
             "correct": False,
             "why": "Mudstone is mud that settled and was buried. Magma has "
                    "nothing to do with it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e28",
        "band": "easier",
        "text": "A rock breaks into flat sheets along one direction and no "
                "other. Which group does that point to?",
        "options": [
            {"text": "Igneous",
             "correct": False,
             "why": "A cooling melt can crack as it shrinks, and cracks do not "
                    "give a rock one direction it splits along"},
            {"text": "Sedimentary",
             "correct": False,
             "why": "A slate's sheets can cut clean across the old layers, "
                    "because they follow the squeeze instead"},
            {"text": "Metamorphic",
             "correct": True},
            {"text": "Any of the three",
             "correct": False,
             "why": "Splitting cleanly along one direction with no effort is a "
                    "fabric, and one group builds it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e29",
        "band": "easier",
        "text": "Which pair of rocks best shows that two rocks can look alike "
                "and still be in different groups?",
        "options": [
            {"text": "Chalk and limestone, which are both pale and soft",
             "correct": False,
             "why": "Both are sedimentary, so the pair shows two lookalikes in "
                    "the SAME group"},
            {"text": "Sandstone and mudstone, which are both made of grains",
             "correct": False,
             "why": "Both are sedimentary as well, so nothing about the groups "
                    "is being shown"},
            {"text": "Granite and basalt, which both cooled from a melt",
             "correct": False,
             "why": "Both are igneous, and a coarse pink rock and a black one "
                    "do not look alike anyway"},
            {"text": "Granite and marble, both hard, shiny and full of "
                     "crystals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-e30",
        "band": "easier",
        "text": "What does every metamorphic rock have in common?",
        "options": [
            {"text": "It was a different rock first, and it never melted while "
                     "it changed",
             "correct": True},
            {"text": "It contains crystals, which heat and pressure always "
                     "produce",
             "correct": False,
             "why": "Igneous rock is full of crystals too, so crystals cannot "
                    "be what defines the group"},
            {"text": "It formed deeper than anything else in the crust",
             "correct": False,
             "why": "Granite forms deep as well, and the heat of an intrusion "
                    "works near the surface"},
            {"text": "It fizzes with acid, because heat drives a carbonate out "
                     "of it",
             "correct": False,
             "why": "Marble fizzes and slate does not. A fizz identifies a "
                    "compound, not a group"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c10-02-s10",
        "band": "standard",
        "text": "A student uses dilute acid as their only test and puts every "
                "rock that fizzes into one group. Why will that fail?",
        "options": [
            {"text": "Because acid is too weak to react with a rock that has "
                     "been heated",
             "correct": False,
             "why": "Marble was heated hard and still fizzes. The carbonate "
                    "survives it"},
            {"text": "Because limestone and marble both fizz and they are in "
                     "different groups",
             "correct": True},
            {"text": "Because a fizz means the rock is soft, and softness "
                     "varies inside every group",
             "correct": False,
             "why": "A fizz means a carbonate is present. Marble fizzes and is "
                    "far too hard to scratch with a coin"},
            {"text": "Because the acid destroys the texture",
             "correct": False,
             "why": "A single drop marks almost nothing, and the texture is "
                    "still there to be read afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s11",
        "band": "standard",
        "text": "Limestone becomes marble. Which property does NOT change?",
        "options": [
            {"text": "Whether fossils can be seen in it",
             "correct": False,
             "why": "The fossils are destroyed, which is one of the clearest "
                    "changes there is"},
            {"text": "The size of the crystals in it",
             "correct": False,
             "why": "Growing the crystals is exactly what the heat and "
                    "pressure do"},
            {"text": "The compound it is made of",
             "correct": True},
            {"text": "Whether it has visible layers",
             "correct": False,
             "why": "The old bedding is deformed and usually destroyed, and "
                    "pale swirls replace it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s12",
        "band": "standard",
        "text": "Two rocks contain exactly the same minerals and belong to "
                "different groups. How is that possible?",
        "options": [
            {"text": "It is not possible, because the minerals in a rock "
                     "decide which group it is in",
             "correct": False,
             "why": "Marble and limestone are the same compound and sit in two "
                    "groups. Minerals do not decide it"},
            {"text": "One of them must contain a small amount of something the "
                     "other does not",
             "correct": False,
             "why": "No trace ingredient is needed. Two rocks can be identical "
                    "in composition and still differ"},
            {"text": "One must be much older, and age moves a rock from one "
                     "group to another",
             "correct": False,
             "why": "Age moves nothing. A rock stays in its group until a "
                    "process changes it"},
            {"text": "The group records how a rock formed, and the same "
                     "minerals can arrive by different routes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s13",
        "band": "standard",
        "text": "A sandstone garden wall crumbles after a few frosty winters "
                "while the granite kerb beside it does not. Explain the "
                "difference using texture.",
        "options": [
            {"text": "Water gets into the spaces between the sandstone's "
                     "grains and freezes; granite has none",
             "correct": True},
            {"text": "The sandstone is the older of the two, and any rock does "
                     "get weaker steadily as it ages",
             "correct": False,
             "why": "Age does nothing. The sandstone was full of spaces from "
                    "the day its grains were buried"},
            {"text": "The granite is darker, so the water on it never gets "
                     "cold enough to freeze",
             "correct": False,
             "why": "Plenty of granite is pale, and a kerb is at the same "
                    "temperature as the wall beside it"},
            {"text": "The sandstone fizzes with acid and the rain is slightly "
                     "acidic",
             "correct": False,
             "why": "Sandstone is quartz grains and does not fizz. What breaks "
                    "it here is water freezing in the gaps"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s14",
        "band": "standard",
        "text": "Limestone can be scratched with a coin and slate cannot. Why "
                "does that not tell you which group either belongs to?",
        "options": [
            {"text": "Because hardness can only be measured properly with "
                     "laboratory equipment",
             "correct": False,
             "why": "A coin test is a perfectly good rough measure. The "
                    "trouble is what the result tells you"},
            {"text": "Because every group contains both soft and hard rocks",
             "correct": True},
            {"text": "Because hardness changes with how wet or dry the sample "
                     "happens to be",
             "correct": False,
             "why": "Hardness is a property of the minerals and barely moves "
                    "with the weather"},
            {"text": "Because a coin is softer than any rock, so the test can "
                     "never work",
             "correct": False,
             "why": "A coin scratches limestone and chalk easily. The test "
                    "works and it answers the wrong question"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s15",
        "band": "standard",
        "text": "A rock is dark grey, hard and heavy, and a student says that "
                "makes it basalt. Why is the reasoning unsafe?",
        "options": [
            {"text": "Because basalt is always pale, so the colour rules it "
                     "out straight away",
             "correct": False,
             "why": "Basalt is dark grey. The trouble is that so are several "
                    "other rocks"},
            {"text": "Because basalt would have to be weighed against water "
                     "before anyone could name it",
             "correct": False,
             "why": "Density will not name it either, because density varies "
                    "inside every group"},
            {"text": "Because slate is dark grey, hard and heavy as well, and "
                     "slate is metamorphic",
             "correct": True},
            {"text": "Because a rock that heavy must have come from the core "
                     "of the Earth",
             "correct": False,
             "why": "Nothing at the surface came from the core, and an "
                    "ordinary rock says nothing about it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s16",
        "band": "standard",
        "text": "A stone merchant sells a dark polished stone as black "
                "granite, and a drop of acid on it fizzes. Why is the name "
                "wrong?",
        "options": [
            {"text": "Because granite is never dark, so the colour alone shows "
                     "the name is wrong",
             "correct": False,
             "why": "Some granite is genuinely dark. The fizz is what settles "
                    "it"},
            {"text": "Because granite is too hard to be polished to that kind "
                     "of finish",
             "correct": False,
             "why": "Granite takes an excellent polish, which is why it is "
                    "sold for worktops"},
            {"text": "Because a genuine granite would have crystals too small "
                     "to see",
             "correct": False,
             "why": "Granite's crystals are millimetres across and easy to "
                    "see. Tiny crystals point at basalt"},
            {"text": "Because a fizz means a carbonate, and granite contains "
                     "none",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s17",
        "band": "standard",
        "text": "Two mudstones are buried to the same depth. One ends up "
                "splitting into perfect sheets and the other does not. What "
                "was different?",
        "options": [
            {"text": "One of them was squeezed hard from one direction, lining "
                     "its flat grains up",
             "correct": True},
            {"text": "One of them was buried for very much longer than the "
                     "other was",
             "correct": False,
             "why": "Time at depth does not line grains up. A squeeze from one "
                    "direction does"},
            {"text": "One of them was heated until it partly melted and set "
                     "again as something new",
             "correct": False,
             "why": "Melting erases the fabric entirely, and what cooled out "
                    "of it would be igneous"},
            {"text": "One of them contained fossils and the other one did not",
             "correct": False,
             "why": "Fossils are wrecked by the change either way, and they "
                    "have nothing to do with how a rock splits"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s18",
        "band": "standard",
        "text": "Coal comes from swamp plants, limestone from sea shells and "
                "sandstone from grains of older rock. What do the three routes "
                "share?",
        "options": [
            {"text": "All three needed heat from a nearby intrusion to harden "
                     "them",
             "correct": False,
             "why": "None of them did. Heating limestone hard turns it into "
                    "marble and moves it out of the group"},
            {"text": "Material settled, was buried and became rock without "
                     "ever melting",
             "correct": True},
            {"text": "All three were once molten and cooled slowly enough to "
                     "build crystals",
             "correct": False,
             "why": "None of the three was ever molten. A melt would have "
                    "destroyed the shells and the plants"},
            {"text": "All three were changed from an earlier rock by heat and "
                     "pressure",
             "correct": False,
             "why": "That is the metamorphic route. These three are built up "
                    "rather than changed"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s19",
        "band": "standard",
        "text": "A rock is made of rounded pebbles the size of peas set in a "
                "finer material, and the whole thing lies in clear layers. "
                "Which group, and what settles it?",
        "options": [
            {"text": "Igneous, and the pebbles are lumps that crystallised "
                     "early in the melt",
             "correct": False,
             "why": "A melt produces crystals that interlock, never rounded "
                    "pebbles lying in layers"},
            {"text": "Metamorphic, and the pebbles were squeezed until they "
                     "became rounded",
             "correct": False,
             "why": "Squeezing flattens and stretches. Rounding happens while "
                    "a fragment is being carried"},
            {"text": "Sedimentary, and the separate rounded pieces lying in "
                     "layers settle it",
             "correct": True},
            {"text": "It cannot be decided without knowing what the pebbles "
                     "are made of",
             "correct": False,
             "why": "What the pieces are made of does not matter. How they sit "
                    "together does"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s20",
        "band": "standard",
        "text": "Chalk is soft, pale, and made from the remains of tiny sea "
                "organisms. Which group, and which of those three facts "
                "decides it?",
        "options": [
            {"text": "Metamorphic, and its softness decides it, because "
                     "heating leaves a rock easy to scratch",
             "correct": False,
             "why": "Heat and pressure leave a rock harder rather than softer, "
                    "and chalk has been through neither"},
            {"text": "Igneous, and its pale colour decides it, because a pale "
                     "melt cools to a pale rock",
             "correct": False,
             "why": "Colour decides nothing at all, and nothing about chalk "
                    "came out of a melt"},
            {"text": "Sedimentary, and its softness decides it, because only "
                     "sedimentary rock is soft",
             "correct": False,
             "why": "Right group, wrong reason. A poorly cemented mudstone is "
                    "soft and a slate is not"},
            {"text": "Sedimentary, and the remains decide it, because only "
                     "that route is gentle enough to leave them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s21",
        "band": "standard",
        "text": "Gneiss has interlocking crystals arranged in bands. Granite "
                "has interlocking crystals in no particular order. Which is "
                "metamorphic, and why?",
        "options": [
            {"text": "Gneiss, because the crystals have been lined up by "
                     "pressure",
             "correct": True},
            {"text": "Granite, because a rock with no order to its crystals "
                     "has clearly been disturbed",
             "correct": False,
             "why": "A random arrangement is what a cooling melt produces, and "
                    "it is the igneous signature"},
            {"text": "Both, because interlocking crystals can only be grown by "
                     "heat and pressure",
             "correct": False,
             "why": "A cooling melt grows interlocking crystals too. That is "
                    "what granite is"},
            {"text": "Neither, because bands in a rock are the layers the "
                     "sediment was dropped in",
             "correct": False,
             "why": "Sedimentary layers are separate grains. These bands are "
                    "crystals that have been aligned"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s22",
        "band": "standard",
        "text": "Why is it fair to say a rock's group records an event rather "
                "than a substance?",
        "options": [
            {"text": "Because the substances in rocks are far too complicated "
                     "to be listed usefully",
             "correct": False,
             "why": "They can be listed perfectly well. The list simply does "
                    "not say how the rock formed"},
            {"text": "Because one compound turns up in two groups, and one "
                     "group holds many compounds",
             "correct": True},
            {"text": "Because rocks are mixtures, and only pure substances can "
                     "be classified",
             "correct": False,
             "why": "Mixtures are classified all the time. The question is "
                    "which property carries the history"},
            {"text": "Because the substance in a rock changes every time the "
                     "rock changes group",
             "correct": False,
             "why": "Marble and limestone are one compound in two groups, so "
                    "the substance can stay put"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s23",
        "band": "standard",
        "text": "Which is the better single test that a rock is sedimentary: "
                "looking for layers, or looking for a fossil?",
        "options": [
            {"text": "Layers, because a fossil tells you nothing about how a "
                     "rock formed",
             "correct": False,
             "why": "A fossil is the strongest single clue there is about how "
                    "a rock formed"},
            {"text": "Layers, because a fossil can be carried into a rock of "
                     "any group by water",
             "correct": False,
             "why": "A fossil is buried as the rock forms. Nothing can be "
                    "carried into solid rock afterwards"},
            {"text": "A fossil, because only the sedimentary route is gentle "
                     "enough to leave one",
             "correct": True},
            {"text": "Neither, because both clues are equally likely to appear "
                     "in all three groups",
             "correct": False,
             "why": "One of them appears in essentially one group, which is "
                    "exactly what makes it useful"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s24",
        "band": "standard",
        "text": "A student sorts a tray of rocks into shiny ones and dull "
                "ones. Why is that not a classification a geologist would use?",
        "options": [
            {"text": "Because shine cannot be measured, so two people would "
                     "never agree on it",
             "correct": False,
             "why": "Two people usually would agree. The trouble is what the "
                    "sorting then tells them"},
            {"text": "Because a rock only looks shiny once a machine has cut "
                     "and polished it",
             "correct": False,
             "why": "Some rocks are shiny on a freshly broken face, and the "
                    "sorting still records nothing useful"},
            {"text": "Because the shine of a rock depends entirely on how wet "
                     "the sample happens to be when you look at it",
             "correct": False,
             "why": "Wetting a rock darkens the surface without changing which "
                    "minerals are in it"},
            {"text": "Because shine is a property of the surface and says "
                     "nothing about how the rock formed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s25",
        "band": "standard",
        "text": "Why does one observation on its own rarely decide which group "
                "a rock is in?",
        "options": [
            {"text": "Because most clues rule a group out rather than pinning "
                     "one down",
             "correct": True},
            {"text": "Because every observation has to be repeated three times "
                     "before it can be trusted",
             "correct": False,
             "why": "Repeating a reading is good practice and does not turn "
                    "one clue into an answer"},
            {"text": "Because the three groups share every property that can "
                     "be seen by eye",
             "correct": False,
             "why": "They do not. A fossil, for one, points at a single group"},
            {"text": "Because a rock has to be tested in a laboratory before "
                     "anything can be said",
             "correct": False,
             "why": "A great deal can be decided in the hand. It takes more "
                    "than one observation, not a laboratory"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s26",
        "band": "standard",
        "text": "Limestone is not made from pieces of older rock at all. Why "
                "is it still called sedimentary?",
        "options": [
            {"text": "Because it is soft, and the sedimentary group is the "
                     "group that the soft rocks go in",
             "correct": False,
             "why": "Slate is hard and metamorphic, chalk is soft and "
                    "sedimentary. Hardness places nothing"},
            {"text": "Because the material settled out of water, built up in "
                     "layers and was cemented",
             "correct": True},
            {"text": "Because it fizzes with acid, and only sedimentary rocks "
                     "hold a carbonate",
             "correct": False,
             "why": "Marble fizzes and is metamorphic. A fizz identifies a "
                    "compound rather than a group"},
            {"text": "Because it holds fossils, and the group is defined as "
                     "the one with fossils",
             "correct": False,
             "why": "Fossils are strong evidence rather than the definition. "
                    "The definition is the route"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s27",
        "band": "standard",
        "text": "Why does an igneous rock have no layers running through it?",
        "options": [
            {"text": "Because any layers in it were destroyed by the heat "
                     "before the rock set solid",
             "correct": False,
             "why": "There were never any layers, because nothing settled in "
                    "the first place"},
            {"text": "Because layers only form in rocks that contain fossils "
                     "to mark them out",
             "correct": False,
             "why": "Plenty of sedimentary rock has clear layers and no "
                    "fossils at all"},
            {"text": "Because it crystallised as one body of melt, so nothing "
                     "settled on anything",
             "correct": True},
            {"text": "Because the crystals grew too large for a layer to be "
                     "seen between them",
             "correct": False,
             "why": "Basalt's crystals are too small to see and it has no "
                    "layers either"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s28",
        "band": "standard",
        "text": "A student says a sandstone is just sand. What has been left "
                "out of that description?",
        "options": [
            {"text": "The heat that baked the grains together into one solid "
                     "piece",
             "correct": False,
             "why": "Nothing is baked. Sedimentary rock forms near the "
                    "surface"},
            {"text": "The melting that welded the grains where they touch one "
                     "another",
             "correct": False,
             "why": "Nothing melts either. A melted sandstone would cool as an "
                    "igneous rock"},
            {"text": "The fossils in it, which are what hold the grains of any "
                     "sandstone together tightly",
             "correct": False,
             "why": "Fossils are passengers in the rock. They hold nothing "
                    "together"},
            {"text": "The burial that pressed the grains together, and the "
                     "cement that now holds them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s29",
        "band": "standard",
        "text": "A builder's catalogue lists marble as a kind of granite. Why "
                "is that worth correcting?",
        "options": [
            {"text": "Because the two rocks come from opposite routes, and "
                     "acid separates them in seconds",
             "correct": True},
            {"text": "Because marble is very much harder than granite and "
                     "would blunt all of the wrong tools",
             "correct": False,
             "why": "Marble is the softer of the two. The mistake is about "
                    "history rather than hardness"},
            {"text": "Because granite is a sedimentary rock and marble is not",
             "correct": False,
             "why": "Granite is igneous, and neither of the two is "
                    "sedimentary"},
            {"text": "Because the two rocks are made of completely different "
                     "colours of crystal",
             "correct": False,
             "why": "Colour is the one thing that decides nothing. Both come "
                    "in pale and dark versions"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-s30",
        "band": "standard",
        "text": "A rock is made of separate grains you can see, and it fizzes "
                "with dilute acid. What can you conclude?",
        "options": [
            {"text": "That it is metamorphic, because a fizz means the rock "
                     "was heated at some point",
             "correct": False,
             "why": "Limestone fizzes and has never been heated, so a fizz "
                    "says nothing about heating"},
            {"text": "That it is sedimentary and contains a carbonate",
             "correct": True},
            {"text": "That it is igneous, because only a melt can leave grains "
                     "that size",
             "correct": False,
             "why": "A melt leaves interlocking crystals. Separate grains are "
                    "the sedimentary signature"},
            {"text": "That it must be marble, because marble is the rock that "
                     "fizzes",
             "correct": False,
             "why": "Marble's crystals interlock. A rock of separate grains "
                    "that fizzes is a limestone"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c10-02-h10",
        "band": "harder",
        "text": "A rock is dark, fine-grained and does not fizz. One student "
                "says basalt and another says slate. Which single observation "
                "would settle it?",
        "options": [
            {"text": "Weighing it, because basalt is denser than slate and a "
                     "balance separates them",
             "correct": False,
             "why": "Density varies within both groups and the two overlap, so "
                    "it settles nothing"},
            {"text": "Looking at it in better light, because basalt is darker",
             "correct": False,
             "why": "Both are dark grey. Colour is the observation that "
                    "decides least"},
            {"text": "Trying to split it, because one of the two breaks into "
                     "flat sheets",
             "correct": True},
            {"text": "Dropping acid on it, because slate fizzes and basalt "
                     "does not",
             "correct": False,
             "why": "Neither of them fizzes, and the stem has already said "
                    "this one does not"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h11",
        "band": "harder",
        "text": "Why is finding no fossil in a rock much weaker evidence than "
                "finding one?",
        "options": [
            {"text": "Because a fossil in a rock proves nothing about how that "
                     "rock formed",
             "correct": False,
             "why": "A fossil is the strongest single clue there is, because "
                    "only one route is gentle enough to leave one"},
            {"text": "Because igneous and metamorphic rocks are as full of "
                     "fossils as sedimentary ones",
             "correct": False,
             "why": "Igneous rock holds none at all and metamorphic rock "
                    "almost never does"},
            {"text": "Because the absence of a fossil proves a rock must have "
                     "been melted",
             "correct": False,
             "why": "Most sedimentary rock holds no fossil and has never been "
                    "anywhere near a melt"},
            {"text": "Because plenty of sedimentary rock never held a fossil "
                     "at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h12",
        "band": "harder",
        "text": "Igneous rock is said to contain fossils NEVER, and "
                "metamorphic rock RARELY. Why is the stronger word justified "
                "for one and not the other?",
        "options": [
            {"text": "Nothing survives a melt, while a solid rock changed "
                     "gently can keep a wrecked one",
             "correct": True},
            {"text": "Igneous rock is older than metamorphic rock, so nothing "
                     "was alive when it formed",
             "correct": False,
             "why": "Igneous rock is forming at every erupting volcano today, "
                    "long after life appeared"},
            {"text": "Igneous rock forms too deep for anything living to have "
                     "been buried in it",
             "correct": False,
             "why": "Lava cools at the surface, where things live. It is the "
                    "temperature that destroys them"},
            {"text": "Metamorphic rock is softer, so a fossil can be pressed "
                     "into it afterwards",
             "correct": False,
             "why": "Nothing is pressed into solid rock. A fossil is buried as "
                    "the rock forms"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h13",
        "band": "harder",
        "text": "A student proposes a fourth group for rocks made of crystals "
                "left behind when a salty lake dries up. Where do those rocks "
                "actually belong?",
        "options": [
            {"text": "Igneous, because a rock made entirely of crystals has to "
                     "have come from a melt",
             "correct": False,
             "why": "Crystals grow out of a solution as readily as out of a "
                    "melt, and nothing here was hot"},
            {"text": "Sedimentary, because the material settled out of water "
                     "and built up in place",
             "correct": True},
            {"text": "Metamorphic, because the drying counts as a change to an "
                     "existing rock",
             "correct": False,
             "why": "There was no earlier rock to change. These crystals are "
                    "the first rock the material has made"},
            {"text": "The student is right, and a fourth group is needed",
             "correct": False,
             "why": "The three groups are routes, and settling out of water is "
                    "already one of them"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h14",
        "band": "harder",
        "text": "Coal is compressed plant remains and holds no grains of older "
                "rock at all. Defend calling it sedimentary.",
        "options": [
            {"text": "Because it burns, and only a sedimentary rock contains "
                     "anything that will burn",
             "correct": False,
             "why": "What a rock does in a fire is not how it is grouped. The "
                    "route is what counts"},
            {"text": "Because it is black, and the sedimentary group is the "
                     "one that covers dark rocks",
             "correct": False,
             "why": "Colour groups nothing, and sedimentary rock runs from "
                    "white chalk to black shale"},
            {"text": "Because material settled and was buried, which is the "
                     "sedimentary route",
             "correct": True},
            {"text": "Because it is soft enough to mark paper, and softness is "
                     "the sedimentary signature",
             "correct": False,
             "why": "Slate is hard and metamorphic, chalk is soft and "
                    "sedimentary. Hardness places nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h15",
        "band": "harder",
        "text": "A rock has interlocking crystals, faint bands running through "
                "it, and it fizzes with dilute acid. Give the fullest account "
                "of its history.",
        "options": [
            {"text": "It cooled from a carbonate melt, and the bands are the "
                     "order the crystals grew in",
             "correct": False,
             "why": "Nothing here melted, and a melt would have driven the "
                    "carbonate off long before it set"},
            {"text": "It is a limestone whose shells have been packed so "
                     "tightly that they interlock",
             "correct": False,
             "why": "Shells packed together are still separate grains. "
                    "Interlocking crystals have grown into one another"},
            {"text": "It is a granite that has had a carbonate washed into the "
                     "gaps between its crystals",
             "correct": False,
             "why": "Granite's crystals leave no gaps, and washing something "
                    "in would not build bands"},
            {"text": "It was a carbonate rock that heat and pressure changed "
                     "until its crystals grew and lined up, without melting",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h16",
        "band": "harder",
        "text": "You want to know whether a region was ever buried deeply. "
                "Which is more use: a fossil, or the way a rock splits?",
        "options": [
            {"text": "The splitting, because a fabric that lines up records a "
                     "squeeze at depth",
             "correct": True},
            {"text": "The fossil, because a fossil can only survive if the "
                     "rock was buried very deeply",
             "correct": False,
             "why": "A fossil survives when the rock is NOT buried deeply. "
                    "Depth and heat wreck it"},
            {"text": "The fossil, because the deeper a rock is buried the more "
                     "fossils it will collect",
             "correct": False,
             "why": "Nothing is added to a rock once it is solid. Burial "
                    "destroys rather than collects"},
            {"text": "Neither, because deep burial leaves no mark that anybody "
                     "could read afterwards",
             "correct": False,
             "why": "It leaves the clearest mark there is — grown crystals and "
                    "an aligned fabric"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h17",
        "band": "harder",
        "text": "Evaluate this rule: if a rock fizzes with acid, it was once "
                "alive.",
        "options": [
            {"text": "It is sound, because a carbonate can only ever be built "
                     "by something once alive",
             "correct": False,
             "why": "Carbonate crystallises out of water with nothing alive "
                    "involved, in a cave or a drying sea"},
            {"text": "It is wrong, because a carbonate can also grow straight "
                     "out of water",
             "correct": True},
            {"text": "It is wrong, because a fizz shows an acid in the rock",
             "correct": False,
             "why": "The acid is the thing being dropped on. The fizz shows "
                    "the rock holds a carbonate"},
            {"text": "It is sound for limestone and wrong for marble",
             "correct": False,
             "why": "Marble's carbonate came from the shells in the limestone, "
                    "so the living origin is the same for both"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h18",
        "band": "harder",
        "text": "Explain how a rock can move from one group to another without "
                "a single atom entering it or leaving it.",
        "options": [
            {"text": "It cannot, because a change of group always means a "
                     "change in what a rock is made of",
             "correct": False,
             "why": "Limestone becomes marble with the same compound "
                    "throughout. Nothing has to be added"},
            {"text": "The atoms swap places with atoms from the rock around "
                     "it, one for one",
             "correct": False,
             "why": "No exchange is needed. The same atoms are simply "
                    "rearranged where they are"},
            {"text": "The group records the arrangement, and heat and pressure "
                     "rebuild it from what is there",
             "correct": True},
            {"text": "The rock is renamed by geologists, and nothing physical "
                     "happens to it at all",
             "correct": False,
             "why": "A great deal happens. Crystals grow, grains rotate and "
                    "fossils are destroyed"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h19",
        "band": "harder",
        "text": "The grains in a sandstone can be far older than the sandstone "
                "itself. Explain how that happens.",
        "options": [
            {"text": "The grains keep growing after the rock has formed, so "
                     "they outlive the rock",
             "correct": False,
             "why": "Grains do not grow once they have been cemented into "
                    "place"},
            {"text": "The rock is dated from its fossils, and the fossils are "
                     "younger than the grains",
             "correct": False,
             "why": "This is not a dating artefact. The grains genuinely "
                    "belonged to an older rock first"},
            {"text": "Older grains sink through the rock and gather at the "
                     "bottom of it",
             "correct": False,
             "why": "Nothing moves through solid rock. The grains were old "
                    "before they ever arrived"},
            {"text": "The grains were broken off an older rock long before it "
                     "was cemented",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h20",
        "band": "harder",
        "text": "A student argues that because all three groups can contain "
                "crystals, texture cannot really decide anything. Answer them.",
        "options": [
            {"text": "Texture is how the pieces sit together, and "
                     "interlocking, banded and separate are three answers",
             "correct": True},
            {"text": "They are right, and that is why the acid test is used "
                     "instead of texture",
             "correct": False,
             "why": "The acid test identifies a compound and places a rock in "
                    "no group at all"},
            {"text": "They are right, and the group can only be settled by "
                     "knowing where a rock was found",
             "correct": False,
             "why": "Where a rock is found can mislead badly. A band of marble "
                    "sits inside limestone"},
            {"text": "Sedimentary rock contains no crystals of any kind, so "
                     "the argument starts from a false claim",
             "correct": False,
             "why": "A limestone can be full of crystals. The claim in the "
                    "stem is correct and the conclusion is not"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h21",
        "band": "harder",
        "text": "An engineer choosing building stone could use the three rock "
                "groups, or a list of how hard each stone is. Which carries "
                "more useful information?",
        "options": [
            {"text": "The hardness list, because hardness is the only property "
                     "that really matters in a building",
             "correct": False,
             "why": "Whether water can get in matters at least as much, and "
                    "hardness does not say"},
            {"text": "The groups, because the route predicts whether water "
                     "gets in and how the stone splits",
             "correct": True},
            {"text": "The hardness list, because the three groups say nothing "
                     "at all about behaviour",
             "correct": False,
             "why": "The groups predict a great deal. A sedimentary stone "
                    "soaks up water and a slate splits"},
            {"text": "Neither, because the only way to choose is to test each "
                     "block in a machine",
             "correct": False,
             "why": "Testing is sensible, and the groups are what tell an "
                    "engineer which test to run"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h22",
        "band": "harder",
        "text": "Why does knowing a rock is metamorphic say more about where "
                "it has been than knowing it is igneous?",
        "options": [
            {"text": "Because metamorphic rock is rarer, so finding one "
                     "narrows the location down",
             "correct": False,
             "why": "How common a rock is says nothing about the conditions "
                    "that made it"},
            {"text": "Because igneous rock can form anywhere, including on the "
                     "surface of the sea",
             "correct": False,
             "why": "Igneous rock forms at the surface and at depth, and rock "
                    "does not form on the sea's surface"},
            {"text": "Because metamorphism always needs burial or a hot "
                     "intrusion nearby",
             "correct": True},
            {"text": "Because metamorphic rock carries fossils recording the "
                     "environment it formed in",
             "correct": False,
             "why": "Metamorphism is what destroys fossils. It carries a "
                    "fabric rather than a fossil"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h23",
        "band": "harder",
        "text": "One metamorphic rock splits into sheets and another breaks "
                "into blocks with no preferred direction. What differed in "
                "their histories?",
        "options": [
            {"text": "The first was heated a good deal more strongly than the "
                     "second",
             "correct": False,
             "why": "How strongly a rock is heated is not what gives it one "
                    "direction. A squeeze from one direction is"},
            {"text": "The first was buried much deeper, and depth alone lines "
                     "grains up",
             "correct": False,
             "why": "Depth brings pressure from every side equally, which "
                    "lines nothing up"},
            {"text": "The second melted slightly and set again, which "
                     "destroyed its sheets",
             "correct": False,
             "why": "Anything that melts and re-cools is igneous, so it would "
                    "not be metamorphic at all"},
            {"text": "The first was squeezed from one direction and the second "
                     "was not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h24",
        "band": "harder",
        "text": "The acid test places a rock in no group at all. Why is it "
                "still one of the most useful tests you can do?",
        "options": [
            {"text": "It is the only test that names the compound in seconds",
             "correct": True},
            {"text": "It is the only test that can be done without damaging "
                     "the sample at all",
             "correct": False,
             "why": "Looking at a rock damages nothing either, and a drop of "
                    "acid does etch the surface"},
            {"text": "It is the only test a student can do without a hand lens "
                     "or a hammer",
             "correct": False,
             "why": "Looking for layers needs neither. Usefulness is about "
                    "what a result rules out"},
            {"text": "It puts a rock into the sedimentary group faster than "
                     "any other test",
             "correct": False,
             "why": "It puts a rock into no group at all. Marble fizzes and is "
                    "metamorphic"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h25",
        "band": "harder",
        "text": "A rock is ground to a powder before it reaches you. Which of "
                "the lesson's questions can you still answer, and which can "
                "you not?",
        "options": [
            {"text": "You can still name the group, because the powder keeps "
                     "the rock's composition",
             "correct": False,
             "why": "The group is not carried by the composition. Marble and "
                    "limestone share one"},
            {"text": "You can test what it is made of, and you cannot place it "
                     "in a group",
             "correct": True},
            {"text": "You can name the group but not the compound",
             "correct": False,
             "why": "Grinding destroys no compound. A powdered marble fizzes "
                    "as readily as a lump does"},
            {"text": "You can answer neither, because a powder carries no "
                     "information",
             "correct": False,
             "why": "It carries the composition perfectly well, which is what "
                    "an acid test reads"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h26",
        "band": "harder",
        "text": "You are handed a rock whose name you have never heard. Why is "
                "working out its group more use than being told its name?",
        "options": [
            {"text": "Because a name can be wrong, and a group worked out by "
                     "hand never can be",
             "correct": False,
             "why": "A group can be got wrong as easily as a name. What counts "
                    "is what the group tells you"},
            {"text": "Because every rock has several names and only one group",
             "correct": False,
             "why": "Most rocks have one name. The point is what the group "
                    "predicts"},
            {"text": "Because the group states how it formed, and that "
                     "predicts its behaviour",
             "correct": True},
            {"text": "Because names are only used by geologists and groups are "
                     "used by everybody",
             "correct": False,
             "why": "Slate, granite and limestone are everyday words. The "
                    "group is simply the more useful information"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h27",
        "band": "harder",
        "text": "A rock is melted and the melt then cools. What exactly has "
                "been erased, and what has not?",
        "options": [
            {"text": "Everything has been erased, including what the rock was "
                     "made of",
             "correct": False,
             "why": "The atoms and the bulk composition survive. It is the "
                    "arrangement that goes"},
            {"text": "Nothing has been erased, because the same material is "
                     "present throughout",
             "correct": False,
             "why": "The texture, the layers and any fossils are destroyed "
                    "completely"},
            {"text": "The composition is erased and the texture survives the "
                     "melting completely unchanged",
             "correct": False,
             "why": "That is exactly backwards. A melt destroys texture and "
                    "keeps the atoms"},
            {"text": "The texture, the layers and any fossils are gone; the "
                     "atoms and the composition are not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h28",
        "band": "harder",
        "text": "Heat and pressure turn limestone into marble and mudstone "
                "into slate, rather than turning both into the same rock. Why?",
        "options": [
            {"text": "Because the starting rock decides the product, since "
                     "nothing is added",
             "correct": True},
            {"text": "Because limestone is heated far more strongly than "
                     "mudstone ever is",
             "correct": False,
             "why": "One event can change both. What differs is what each was "
                    "made of"},
            {"text": "Because the two rocks were buried at completely "
                     "different times in the past",
             "correct": False,
             "why": "When they were buried is irrelevant. What they were made "
                    "of is not"},
            {"text": "Because new material is added from the rock surrounding "
                     "each of them",
             "correct": False,
             "why": "Nothing needs adding. The change is a rearrangement of "
                    "what was already there"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h29",
        "band": "harder",
        "text": "A student concludes that colour is never any use at all in "
                "geology. Is that fair?",
        "options": [
            {"text": "Yes, because two rocks of the same colour are always in "
                     "the same group",
             "correct": False,
             "why": "Granite and marble can both be pale and sit in different "
                    "groups. That is the opposite of the rule"},
            {"text": "No — colour hints at the minerals but never records how "
                     "a rock formed",
             "correct": True},
            {"text": "Yes, because the colour of a rock changes every time it "
                     "is wetted or dried",
             "correct": False,
             "why": "Wetting darkens a surface without changing which minerals "
                    "are in the rock"},
            {"text": "No, because colour is the quickest way to place a rock "
                     "in one of the groups",
             "correct": False,
             "why": "Colour places a rock in no group. Dark grey covers all "
                    "three of them"},
        ],
        "figure": None,
    },
    {
        "id": "c10-02-h30",
        "band": "harder",
        "text": "Rank these three observations by how much each narrows a "
                "rock's group: a fossil, interlocking crystals, and a dark "
                "colour.",
        "options": [
            {"text": "Colour first, crystals second, fossil third, because "
                     "colour is quickest to see",
             "correct": False,
             "why": "How quickly an observation can be made has nothing to do "
                    "with how much it narrows"},
            {"text": "Crystals first, colour second, fossil third, because "
                     "crystals rule out two groups",
             "correct": False,
             "why": "Interlocking crystals rule out one group and leave two "
                    "still open"},
            {"text": "Fossil first, crystals second, colour third",
             "correct": True},
            {"text": "All three equally",
             "correct": False,
             "why": "A fossil settles it, crystals halve it and colour changes "
                    "nothing at all"},
        ],
        "figure": None,
    },
]
