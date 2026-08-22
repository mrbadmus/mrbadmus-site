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
]
