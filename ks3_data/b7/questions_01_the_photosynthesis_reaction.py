"""B7 lesson 01 — The photosynthesis reaction: twelve questions (MRB-269).

The lesson has one spine — two reactants in, two products out, with light and
chlorophyll as conditions rather than raw materials — and one bench that makes
the four requirements jointly necessary: remove any one and the rate is zero,
not merely lower. The bank probes both. The easier band checks the parts a
student has to be able to name and place: what chlorophyll does without being
used up, what happens to each of the two products, where the water enters and
which element it supplies, and why a leaf is tested for starch rather than for
glucose. The standard band puts the student back at the bell jar and at van
Helmont's pot — soda lime in, the lamp dimmed rather than switched off, the
plant moved into the dark, and the 57 grams the soil actually lost. The harder
band takes the ideas somewhere the lesson did not go: a felled forest burned,
two plants each missing a different one of the four, a heatwave crop with two
reasons behind one result, and a sentence that has to be corrected in the right
place.

Both declared misconceptions supply distractors throughout. PLANT-01 ("plants
get their food from the soil") drives the "water is the plant's food" option in
e03, the soil-into-wood option in s04, and the carbon-back-into-the-soil option
in h02. PLANT-02 ("photosynthesis makes energy") drives the chlorophyll option
in e01 and both of the wrong corrections in h01, where the trap is that the
half of the sentence which is right makes the half that is wrong easy to walk
past. Three further errors the lesson exists to correct supply the rest: that
the four requirements are weighted contributors which can partly cover for one
another, so removing one costs a quarter of the rate rather than all of it
(s01, s02, s03, h03); that light being a condition rather than a reactant means
its brightness cannot matter (s02, and the mirror image in h03); and that
minerals are a raw material for the reaction (h04). e04's distractors are the
glucose-and-starch confusions in all three directions — that iodine tests any
sugar, that starch is the product and glucose comes from it, and that the
reason for testing starch is amount rather than the fact that starch stays put.

`figure` is None throughout: this lesson declares no figures.
"""

UNIT = "B7"
LESSON = "the-photosynthesis-reaction"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-01-e01",
        "band": "easier",
        "text": "The white parts of a variegated leaf contain no chlorophyll "
                "and make no starch. What is the chlorophyll doing in the "
                "parts that are green?",
        "options": [
            {"text": "It is used up in the reaction and ends up built into "
                     "the glucose.",
             "correct": False,
             "why": "Chlorophyll is not a reactant — it is still there, "
                    "unchanged, after a day in bright light. Only carbon "
                    "dioxide and water are used up."},
            {"text": "It absorbs the light energy the reaction requires, "
                     "without being used up.",
             "correct": True},
            {"text": "It makes the energy the plant needs in order to grow.",
             "correct": False,
             "why": "Nothing makes energy. The energy is already arriving as "
                    "light, and what chlorophyll does is absorb it so the "
                    "reaction can store it in glucose."},
            {"text": "It lets carbon dioxide into the leaf from the air "
                     "outside.",
             "correct": False,
             "why": "That is what the stomata do. Chlorophyll is a green "
                    "pigment inside the leaf, and what it handles is light, "
                    "not gas."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e02",
        "band": "easier",
        "text": "Photosynthesis has two products. Which statement describes "
                "what becomes of each of them?",
        "options": [
            {"text": "The glucose is kept and used or stored, and the oxygen "
                     "diffuses out as waste.",
             "correct": True},
            {"text": "The glucose is stored as starch, and the oxygen is used "
                     "to build new cell walls.",
             "correct": False,
             "why": "Cell walls are built from glucose, not from oxygen. The "
                    "oxygen is a waste product and diffuses out through the "
                    "stomata."},
            {"text": "The oxygen is stored in the leaf, and the glucose "
                     "diffuses out into the air.",
             "correct": False,
             "why": "That is the two of them the wrong way round. Glucose is "
                    "the one the plant keeps — it is the point of the whole "
                    "reaction — and oxygen is the one it lets go."},
            {"text": "Both are waste products, and both diffuse out through "
                     "the stomata into the air.",
             "correct": False,
             "why": "Only the oxygen is waste. Glucose is respired, converted "
                    "to starch for storage, or built into cellulose for new "
                    "cell walls."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e03",
        "band": "easier",
        "text": "Where does the water used in photosynthesis come from, and "
                "what does it supply?",
        "options": [
            {"text": "From the soil through the root hair cells, and it "
                     "supplies the carbon in glucose.",
             "correct": False,
             "why": "Right route, wrong element. The carbon arrives as carbon "
                    "dioxide through the leaves; what the water supplies is "
                    "the hydrogen."},
            {"text": "From the air through the stomata, and it supplies the "
                     "hydrogen in glucose.",
             "correct": False,
             "why": "Right element, wrong route. Carbon dioxide is the one "
                    "that diffuses in through the stomata; water is taken up "
                    "by the root hair cells."},
            {"text": "From the soil through the root hair cells, and it "
                     "supplies the hydrogen in glucose.",
             "correct": True},
            {"text": "From the soil through the root hair cells, and it is "
                     "the plant's food.",
             "correct": False,
             "why": "Water is a raw material, not food. Food means something "
                    "that can be broken down to release energy — and a plant "
                    "makes its own, which is what a producer is."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e04",
        "band": "easier",
        "text": "A leaf is tested for starch rather than for glucose. Why is "
                "starch the thing to look for?",
        "options": [
            {"text": "Iodine turns blue-black with any sugar, so the two "
                     "tests come to the same thing.",
             "correct": False,
             "why": "Iodine detects starch and nothing else. A blue-black "
                    "tells you starch is present; on its own it says nothing "
                    "about sugar."},
            {"text": "Starch is what photosynthesis makes, and the glucose is "
                     "built from it afterwards.",
             "correct": False,
             "why": "The other way round. Glucose is the product of the "
                    "reaction, and the leaf converts it into starch, which is "
                    "the storage form."},
            {"text": "A leaf holds much more starch than glucose, so a faint "
                     "result is less likely.",
             "correct": False,
             "why": "It is not about how much. Glucose is used or moved on "
                    "within hours, so it may already have gone; starch stays "
                    "where it was made."},
            {"text": "Glucose is used or converted within hours, while starch "
                     "stays put in the leaf.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-01-s01",
        "band": "standard",
        "text": "Soda lime is put under the bell jar to absorb the carbon "
                "dioxide, and everything else is left exactly as it was. A "
                "day later a leaf is tested with iodine. What do you see, and "
                "why?",
        "options": [
            {"text": "Blue-black — light, water and chlorophyll are all still "
                     "there, so the reaction carries on.",
             "correct": False,
             "why": "The four are not contributors that can cover for one "
                    "another. They are all needed together, so taking any one "
                    "away stops the reaction outright."},
            {"text": "Orange-brown — no carbon dioxide arrived, so the carbon "
                     "the glucose is built from was missing.",
             "correct": True},
            {"text": "Faint blue-black — losing one of the four conditions "
                     "cuts the rate to about three quarters.",
             "correct": False,
             "why": "Removing a condition does not shave a quarter off the "
                    "rate. Remove any one of the four and nothing is made at "
                    "all — the bench reads zero."},
            {"text": "Orange-brown — the soda lime took away the oxygen the "
                     "reaction needs to get going.",
             "correct": False,
             "why": "Oxygen is a product here, not a reactant — the plant "
                    "releases it. What the soda lime absorbed was the carbon "
                    "dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s02",
        "band": "standard",
        "text": "Nothing is taken out of the bell jar, but the lamp is turned "
                "down to dim rather than switched off. What does the iodine "
                "show on a leaf tested the next day?",
        "options": [
            {"text": "Orange-brown — dim light is not enough, so the reaction "
                     "is not happening at all.",
             "correct": False,
             "why": "Dim is a reduction, not a removal. The plant is limited, "
                    "not stopped, and a low rate still builds some starch "
                    "over a whole day."},
            {"text": "Full blue-black — light is a condition and not a "
                     "reactant, so its brightness cannot matter.",
             "correct": False,
             "why": "Not being a reactant does not mean not mattering. Light "
                    "supplies the energy the reaction needs, so less light "
                    "arriving means a lower rate."},
            {"text": "Orange-brown — in dim light the plant lives off the "
                     "starch it had stored earlier.",
             "correct": False,
             "why": "A leaf does draw on its stores, but that is not what "
                    "this test shows. Dim light lowers the rate rather than "
                    "stopping it, so new starch is still being made."},
            {"text": "A faint blue-black — a little starch, because the rate "
                     "is low rather than zero.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s03",
        "band": "standard",
        "text": "With everything present, three counters run: glucose being "
                "made, oxygen released into the jar, and carbon dioxide taken "
                "from the jar. The plant is moved into a dark cupboard. What "
                "happens to the three?",
        "options": [
            {"text": "All three fall to zero, because without light energy "
                     "none of the reaction happens.",
             "correct": True},
            {"text": "Glucose and oxygen fall to zero, but carbon dioxide is "
                     "still taken from the jar.",
             "correct": False,
             "why": "Carbon dioxide is only taken in because it is being "
                    "built into glucose. Stop the reaction and all three "
                    "counters stop together."},
            {"text": "Only oxygen falls to zero, because oxygen is the one "
                     "product that light is needed for.",
             "correct": False,
             "why": "Light is not attached to one product. It supplies the "
                    "energy for the whole reaction, so nothing at all is used "
                    "up and nothing at all is made."},
            {"text": "All three keep going slowly, on the carbon dioxide "
                     "already sealed inside the jar.",
             "correct": False,
             "why": "Having the raw material is not enough. Carbon dioxide in "
                    "the jar stays carbon dioxide until there is light energy "
                    "to drive the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s04",
        "band": "standard",
        "text": "Van Helmont's soil ended up about 57 grams lighter after "
                "five years, while the willow itself gained 74 kilograms. "
                "What had those 57 grams been?",
        "options": [
            {"text": "Soil the willow took up and built into wood, which is "
                     "where the 74 kilograms came from.",
             "correct": False,
             "why": "Fifty-seven grams cannot become 74 kilograms. That gap "
                    "is exactly what weighing the soil was for: the new mass "
                    "did not come out of the pot."},
            {"text": "Water that drained out of the pot over the five years "
                     "it was left standing there.",
             "correct": False,
             "why": "The willow was watered throughout and the pot was kept "
                    "covered. What left the soil went into the plant, and 57 "
                    "grams of it was dissolved minerals."},
            {"text": "Minerals, taken up through the roots in the tiny "
                     "amounts a plant needs them in.",
             "correct": True},
            {"text": "Carbon dioxide trapped in the soil, drawn up into the "
                     "willow through its roots.",
             "correct": False,
             "why": "Carbon dioxide comes from the air, and it goes in "
                    "through the stomata on the leaves. Nothing about this "
                    "reaction takes a gas in through the roots."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-01-h01",
        "band": "harder",
        "text": "A student writes: \"Photosynthesis makes energy, and the "
                "plant keeps that energy in glucose.\" Which correction is "
                "the one that matters?",
        "options": [
            {"text": "Nothing needs correcting — glucose is an energy store, "
                     "so the sentence is already right.",
             "correct": False,
             "why": "The second half is fine, and that is what makes the "
                    "first half easy to walk past. Nothing makes energy — not "
                    "a plant, not anything."},
            {"text": "It should say the energy is stored as starch, because "
                     "starch is what a leaf stores.",
             "correct": False,
             "why": "Starch is only the glucose converted for storage, so "
                    "that swap changes almost nothing. The error is in the "
                    "words 'makes energy'."},
            {"text": "Nothing makes energy — photosynthesis stores light "
                     "energy that was already arriving.",
             "correct": True},
            {"text": "It should say the plant makes the energy out of the "
                     "sunlight that its leaves absorb.",
             "correct": False,
             "why": "That is the same claim reworded. Energy is transferred "
                    "between stores and never created; the light energy "
                    "existed before the leaf absorbed it."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h02",
        "band": "harder",
        "text": "A stretch of forest is felled and the timber burned. What "
                "happens to the carbon that was in the wood?",
        "options": [
            {"text": "It goes back into the air as carbon dioxide — exactly "
                     "the carbon the trees took out.",
             "correct": True},
            {"text": "It is destroyed by the fire, so the carbon those trees "
                     "removed is gone for good.",
             "correct": False,
             "why": "Burning changes what the carbon is joined to; it does "
                    "not destroy it. Every carbon atom in that wood leaves "
                    "the fire as carbon dioxide."},
            {"text": "It stays behind in the ash, which is why wood ash gets "
                     "spread on the soil.",
             "correct": False,
             "why": "Ash is the minerals the tree took from the soil, and it "
                    "is a tiny fraction of the mass. The carbon has gone back "
                    "into the air."},
            {"text": "It sinks into the soil, which is where the trees drew "
                     "it up from in the first place.",
             "correct": False,
             "why": "The carbon never came from the soil. It arrived as "
                    "carbon dioxide from the air, through the leaves, and "
                    "that is where burning sends it back."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h03",
        "band": "harder",
        "text": "Two identical plants sit under bell jars. Plant A is in "
                "bright light with soda lime in its jar; plant B is in normal "
                "air in a dark cupboard. Both are watered and both have green "
                "leaves. Which one makes more starch?",
        "options": [
            {"text": "Plant A, because bright light drives the reaction on "
                     "even with the soda lime in there.",
             "correct": False,
             "why": "Light on its own builds nothing. With no carbon dioxide "
                    "arriving there is no carbon to build glucose from, "
                    "however bright the lamp is."},
            {"text": "Neither of them. Each is missing one of the four, and "
                     "all four are needed.",
             "correct": True},
            {"text": "Both make some, because each of them still has three of "
                     "the four things it needs.",
             "correct": False,
             "why": "Three out of four is not three quarters of the rate. The "
                    "four are needed together, so missing any one takes the "
                    "rate to zero for both plants."},
            {"text": "Plant B, because carbon dioxide is what almost all of a "
                     "plant's new mass is built from.",
             "correct": False,
             "why": "Carbon dioxide is where the mass comes from, but it "
                    "cannot be built into anything without light energy to "
                    "drive the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h04",
        "band": "harder",
        "text": "In a heatwave a crop is left unwatered, and a leaf tested a "
                "day later shows no starch. A student says the only reason is "
                "that there was no water to supply the hydrogen. What have "
                "they missed?",
        "options": [
            {"text": "Nothing — water supplies the hydrogen in glucose, and "
                     "that is the whole of the reason.",
             "correct": False,
             "why": "It is a correct reason, but not the only one. A real "
                    "plant hands you two at once, which is why the bench "
                    "warns you it is a simplified model."},
            {"text": "That the plant runs out of minerals, which are the raw "
                     "material this reaction is built from.",
             "correct": False,
             "why": "Minerals are needed in milligram amounts to build "
                    "particular molecules, and they are not a raw material "
                    "here. Only carbon dioxide and water are."},
            {"text": "That the leaf loses its chlorophyll as it dries out, so "
                     "it goes white like a variegated edge.",
             "correct": False,
             "why": "A wilting leaf keeps its chlorophyll. The second reason "
                    "is about gas rather than pigment: a dry plant shuts its "
                    "stomata."},
            {"text": "That a dry plant closes its stomata, which shuts the "
                     "carbon dioxide out as well.",
             "correct": True},
        ],
        "figure": None,
    },
]
