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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-01-e05",
        "band": "easier",
        "text": "Photosynthesis uses up two substances and builds two new "
                "ones. Which pair is used up?",
        "options": [
            {"text": "Glucose and oxygen, which the plant makes and then "
                     "breaks down again.",
             "correct": False,
             "why": "Those two are the products — what the reaction makes. "
                    "Read the summary from left to right and what goes in is "
                    "carbon dioxide and water."},
            {"text": "Light energy and chlorophyll, which are both spent as "
                     "the reaction runs.",
             "correct": False,
             "why": "Neither of them is spent. Light supplies the energy and "
                    "chlorophyll absorbs it, and the chlorophyll is still "
                    "there, unchanged, at the end of the day."},
            {"text": "Carbon dioxide and water, one taken from the air and "
                     "one from the soil.",
             "correct": True},
            {"text": "Carbon dioxide and minerals, both taken in through the "
                     "plant's roots.",
             "correct": False,
             "why": "Minerals are not a raw material for this reaction, and "
                    "carbon dioxide does not arrive through the roots — it "
                    "diffuses in through the stomata."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e06",
        "band": "easier",
        "text": "Light is needed for photosynthesis, but it is not called a "
                "reactant. What does the word reactant mean?",
        "options": [
            {"text": "A substance that is used up in the reaction, written on "
                     "the left of the summary.",
             "correct": True},
            {"text": "Anything the reaction needs in order to happen, whether "
                     "or not it is used up.",
             "correct": False,
             "why": "That would make light and chlorophyll reactants, and "
                    "neither of them is used up. A reactant is a substance "
                    "the reaction consumes."},
            {"text": "A substance the reaction makes, written on the right of "
                     "the summary.",
             "correct": False,
             "why": "That is a product. Glucose and oxygen are the products "
                    "here; carbon dioxide and water are the reactants."},
            {"text": "The green pigment that absorbs the light energy the "
                     "reaction runs on.",
             "correct": False,
             "why": "That is chlorophyll, and it is a condition rather than a "
                    "reactant — no part of it ends up in the glucose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e07",
        "band": "easier",
        "text": "Carbon dioxide is one of the two reactants. How does it get "
                "into a leaf?",
        "options": [
            {"text": "It is taken up from the soil by the root hair cells and "
                     "carried up to the leaves.",
             "correct": False,
             "why": "That is the route water takes. Carbon dioxide comes from "
                    "the air, and nothing about this reaction takes a gas in "
                    "through the roots."},
            {"text": "It is built inside the leaf from the minerals the plant "
                     "has taken out of the soil.",
             "correct": False,
             "why": "A plant cannot build carbon dioxide out of minerals. It "
                    "arrives ready-made from the air outside the leaf."},
            {"text": "It soaks in through the waxy upper surface, where the "
                     "light falling on the leaf is strongest.",
             "correct": False,
             "why": "The waxy layer is there to keep water in, and gases do "
                    "not cross it. Carbon dioxide goes in through the "
                    "stomata."},
            {"text": "It diffuses in from the air through the stomata on the "
                     "underside of the leaf.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e08",
        "band": "easier",
        "text": "A leaf keeps the glucose it makes. Which list gives three "
                "things a plant does with it?",
        "options": [
            {"text": "It is stored as starch, turned straight back into "
                     "carbon dioxide, or released into the air.",
             "correct": False,
             "why": "Nothing releases glucose into the air, and turning it "
                    "straight back into carbon dioxide is not a use. Glucose "
                    "is respired, stored, or built into new structures."},
            {"text": "It is respired, converted to starch for storage, or "
                     "built into cellulose for new cell walls.",
             "correct": True},
            {"text": "It is respired, sent down to the roots as minerals, or "
                     "evaporated out through the stomata.",
             "correct": False,
             "why": "Minerals come from the soil and glucose never becomes "
                    "one, and no sugar evaporates out of a leaf. The third "
                    "use is building cellulose."},
            {"text": "It is burnt for warmth, stored as starch, or passed out "
                     "through the roots into the soil.",
             "correct": False,
             "why": "A plant burns nothing and passes no sugar into the soil. "
                    "The three uses are respiration, storage as starch, and "
                    "building cellulose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e09",
        "band": "easier",
        "text": "Photosynthesis needs light, carbon dioxide, water and "
                "chlorophyll. What happens to the rate if exactly one of "
                "those four is taken away?",
        "options": [
            {"text": "It falls by about a quarter, because one of the four "
                     "contributions has been lost.",
             "correct": False,
             "why": "The four are not contributions that add up to a rate. "
                    "They are all needed together, so losing one is not "
                    "losing a share."},
            {"text": "It carries on unchanged, because the other three can "
                     "cover for the missing one.",
             "correct": False,
             "why": "Nothing covers for a missing one. Take the carbon "
                    "dioxide away and there is no carbon to build glucose "
                    "from, however much light and water there is."},
            {"text": "It falls to zero, because all four are needed together "
                     "for the reaction to run.",
             "correct": True},
            {"text": "It falls to zero only if the missing one is light, "
                     "which is the reaction's energy supply.",
             "correct": False,
             "why": "Light is not the special one. Remove the water, the "
                    "carbon dioxide or the chlorophyll instead and the rate "
                    "is zero just the same."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e10",
        "band": "easier",
        "text": "A plant takes minerals from the soil. In what quantities "
                "does it need them, and what are they for?",
        "options": [
            {"text": "In large quantities, because minerals are the plant's "
                     "food and supply all the energy it lives and grows on.",
             "correct": False,
             "why": "Minerals supply no energy at all and are not food. A "
                    "plant makes its own food, which is what being a producer "
                    "means."},
            {"text": "In milligram quantities, to build particular "
                     "molecules, not glucose.",
             "correct": True},
            {"text": "In milligram quantities, as the raw material the plant "
                     "builds its glucose out of.",
             "correct": False,
             "why": "The quantity is right and the job is wrong. Glucose is "
                    "built from carbon dioxide and water; minerals go into "
                    "other particular molecules."},
            {"text": "In large quantities, because most of a plant's mass is "
                     "soil drawn up through the roots.",
             "correct": False,
             "why": "Van Helmont settled that. His willow gained 74 "
                    "kilograms while the soil lost about 57 grams, so the new "
                    "mass did not come out of the pot."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e11",
        "band": "easier",
        "text": "Carbon dioxide makes up about 0.04% of the air. What does "
                "that figure mean?",
        "options": [
            {"text": "About four molecules in every hundred in the air are "
                     "carbon dioxide.",
             "correct": False,
             "why": "That would be 4%, a hundred times too much. A figure of "
                    "0.04% is four hundredths of one per cent — four "
                    "molecules in every ten thousand."},
            {"text": "About four litres out of every hundred litres of air "
                     "are carbon dioxide.",
             "correct": False,
             "why": "Again that is 4% rather than 0.04%. The real supply is "
                    "far thinner: four molecules in every ten thousand."},
            {"text": "There is so little of it that a plant cannot use the "
                     "air as its carbon supply.",
             "correct": False,
             "why": "It is a thin supply and it is still the supply. Every "
                    "gram of an oak beam was assembled out of it, one "
                    "molecule at a time."},
            {"text": "About four molecules in every ten thousand in the air "
                     "are carbon dioxide.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e12",
        "band": "easier",
        "text": "In the word summary, light energy and chlorophyll are "
                "written above and below the arrow rather than on the left "
                "with the reactants. What does that show?",
        "options": [
            {"text": "That both are needed for the reaction but neither is a "
                     "raw material it is built from.",
             "correct": True},
            {"text": "That both are optional, and a healthy plant will "
                     "manage the reaction without them.",
             "correct": False,
             "why": "Needed is not optional. Take the light away, or test the "
                    "white part of a leaf that has no chlorophyll in it, and "
                    "nothing at all is made."},
            {"text": "That both are used up more slowly than the carbon "
                     "dioxide and the water are.",
             "correct": False,
             "why": "Neither of them is used up at any speed. The chlorophyll "
                    "is unchanged at the end of the day, and no part of the "
                    "light ends up in the glucose."},
            {"text": "That both are made by the reaction rather than being "
                     "needed before it starts.",
             "correct": False,
             "why": "The products are glucose and oxygen. Light and "
                    "chlorophyll are conditions the reaction requires, which "
                    "is why they sit above and below the arrow."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e13",
        "band": "easier",
        "text": "Photosynthesis builds glucose. What is glucose?",
        "options": [
            {"text": "A mineral the plant takes from the soil and "
                     "concentrates in its leaves.",
             "correct": False,
             "why": "Minerals come from the soil and glucose does not. The "
                    "plant builds it in the leaf out of carbon dioxide and "
                    "water."},
            {"text": "The green pigment that absorbs light energy inside the "
                     "leaf.",
             "correct": False,
             "why": "That is chlorophyll. Glucose is the sugar the reaction "
                    "builds using the energy chlorophyll absorbs."},
            {"text": "A sugar, and an energy store — it holds more energy "
                     "than the substances it was built from.",
             "correct": True},
            {"text": "The insoluble store a leaf keeps in its cells, which "
                     "is what a leaf is tested for.",
             "correct": False,
             "why": "That describes starch. Glucose is the soluble sugar the "
                    "reaction makes, and the leaf converts some of it into "
                    "starch to store it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-01-s05",
        "band": "standard",
        "text": "Van Helmont weighed the dried soil at the start and again "
                "five years later. What did weighing it settle, and where did "
                "he still go wrong?",
        "options": [
            {"text": "It settled that the mass had come from the water, and "
                     "on that he turned out to be right.",
             "correct": False,
             "why": "Water supplies the hydrogen and it is not where the mass "
                    "came from. Nearly all of that new willow was carbon "
                    "dioxide taken from the air."},
            {"text": "It settled that the mass had not come from the soil, "
                     "and he then concluded wrongly that it was all water.",
             "correct": True},
            {"text": "It settled that minerals are a plant's food, though he "
                     "underestimated how much of them a willow uses.",
             "correct": False,
             "why": "The soil lost about 57 grams in five years, which is "
                    "nowhere near a food supply for 74 kilograms of willow — "
                    "and minerals release no energy anyway."},
            {"text": "It settled nothing at all, because he had no way of "
                     "weighing the air the plant was taking in.",
             "correct": False,
             "why": "He could not weigh the air and the experiment was still "
                    "decisive. The soil was almost unchanged, so whatever the "
                    "willow was built from, it was not the pot."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s06",
        "band": "standard",
        "text": "Growers of glasshouse crops often pipe extra carbon dioxide "
                "into the air around the plants. Why does that raise the "
                "yield when there is carbon dioxide in ordinary air already?",
        "options": [
            {"text": "Because carbon dioxide is the gas a plant breathes in, "
                     "and more of it keeps the crop alive for longer.",
             "correct": False,
             "why": "Photosynthesis is not breathing, and carbon dioxide here "
                    "is a raw material rather than something a plant takes in "
                    "to stay alive."},
            {"text": "Because extra carbon dioxide makes the light the plants "
                     "are already receiving work harder for them.",
             "correct": False,
             "why": "The daylight and the lamps are unchanged. What the extra "
                    "gas changes is the supply of the material the glucose is "
                    "built from."},
            {"text": "Because the supply in ordinary air is so thin that it "
                     "is often the condition holding the rate back.",
             "correct": True},
            {"text": "Because carbon dioxide keeps a glasshouse warmer, and a "
                     "warm plant photosynthesises faster.",
             "correct": False,
             "why": "Warmth does matter to a real plant, but that is not what "
                    "this is. Growers add the gas because it is the raw "
                    "material in shortest supply."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s07",
        "band": "standard",
        "text": "A plant is sealed under a bell jar in bright light. The "
                "carbon dioxide in the jar falls while the oxygen in it "
                "rises. Why do both happen at once?",
        "options": [
            {"text": "One reaction is using up the carbon dioxide and "
                     "releasing the oxygen as waste.",
             "correct": True},
            {"text": "The oxygen is pushing the carbon dioxide out of the "
                     "jar as it builds up, so the two gases swap over one "
                     "for one.",
             "correct": False,
             "why": "Nothing is pushed out of a sealed jar. One reaction is "
                    "using up the one gas and releasing the other, which is "
                    "why the two change together."},
            {"text": "The carbon dioxide is dissolving into the wet soil, and "
                     "the oxygen is leaking out of the leaf.",
             "correct": False,
             "why": "Both changes are the reaction's doing. The carbon "
                    "dioxide is being used up as glucose is built, and the "
                    "oxygen is the waste that comes with it."},
            {"text": "Two separate reactions happen to be running in the "
                     "leaf at once.",
             "correct": False,
             "why": "It is one reaction. Two reactants go in and two products "
                    "come out, so a change in one is always matched by a "
                    "change in the other."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s08",
        "band": "standard",
        "text": "A seedling is grown in washed sand with no minerals in it at "
                "all, watered with pure water and left in bright light. For "
                "the first few weeks its leaves still test blue-black for "
                "starch. Explain that result.",
        "options": [
            {"text": "It must have found minerals dissolved in the water it "
                     "was given, so it had a small supply of them after all.",
             "correct": False,
             "why": "Even if there were traces, that is not the point. "
                    "Minerals are not what glucose is built from, so the "
                    "starch does not depend on them."},
            {"text": "The starch is left over from the food store in the "
                     "seed, and no new starch is being made at all.",
             "correct": False,
             "why": "There is nothing to stop the seedling. Light, carbon "
                    "dioxide, water and chlorophyll are all present, so it is "
                    "building new glucose every day."},
            {"text": "Iodine gives a false blue-black on a plant short of "
                     "minerals.",
             "correct": False,
             "why": "Iodine answers one question and answers it honestly. "
                    "Blue-black means starch, and there is nothing false "
                    "about this result."},
            {"text": "Photosynthesis does not use minerals as a raw "
                     "material, so it runs without them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s09",
        "band": "standard",
        "text": "Photosynthesis stops the moment it goes dark, and yet a "
                "plant is still alive in the morning. What has it been living "
                "on all night?",
        "options": [
            {"text": "The minerals it goes on taking up through its roots "
                     "after dark.",
             "correct": False,
             "why": "Minerals supply no energy. What a plant lives on "
                    "overnight is the food it made for itself while it was "
                    "light."},
            {"text": "The glucose it built during the day, some of it held in "
                     "the leaf as starch.",
             "correct": True},
            {"text": "Nothing at all, because a plant needs no energy while "
                     "it is dark.",
             "correct": False,
             "why": "A plant is alive all night, and everything alive uses "
                    "energy. It spends the store it built while the light was "
                    "on."},
            {"text": "The water it took up during the day, broken down for "
                     "energy after dark.",
             "correct": False,
             "why": "Water is a raw material, not a fuel. The store a plant "
                    "draws on is the glucose it built, kept in the leaf as "
                    "starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s10",
        "band": "standard",
        "text": "A student seals a healthy pot plant in a jar of pure oxygen "
                "and leaves it in bright light, expecting it to grow faster. "
                "What actually happens?",
        "options": [
            {"text": "It makes no starch at all: there is no carbon dioxide "
                     "in the jar to build glucose from.",
             "correct": True},
            {"text": "It grows faster than usual, because oxygen is the gas "
                     "a plant takes in through its stomata and needs most "
                     "of.",
             "correct": False,
             "why": "Oxygen is what photosynthesis releases, not what it "
                    "uses. Filling the jar with it has taken away the gas the "
                    "plant actually needs."},
            {"text": "It grows at its normal rate, because it can make its "
                     "own carbon dioxide from the water it is given.",
             "correct": False,
             "why": "A plant cannot build carbon dioxide out of anything. It "
                    "has to arrive from the air, through the stomata."},
            {"text": "It grows more slowly, because oxygen at that strength "
                     "poisons a plant.",
             "correct": False,
             "why": "The plant is not being poisoned. It has simply been "
                    "sealed away from the one raw material it cannot make for "
                    "itself."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s11",
        "band": "standard",
        "text": "Two identical seedlings are watered the same and kept at the "
                "same temperature. One is on a bright windowsill and the "
                "other two metres back into the room. After a fortnight the "
                "windowsill one is much the bigger. Explain why.",
        "options": [
            {"text": "The one at the back had no light at all, so it made "
                     "nothing and lived off its store.",
             "correct": False,
             "why": "Two metres into a room is dim rather than dark. That "
                    "seedling has been photosynthesising the whole fortnight, "
                    "only slowly."},
            {"text": "The windowsill one was warmer, and warmth is what makes "
                     "a plant grow.",
             "correct": False,
             "why": "You are told the temperature was the same for both. What "
                    "differed is the light, and light is what supplies the "
                    "energy."},
            {"text": "More light means a higher rate, so more glucose was "
                     "built and there was more to grow with.",
             "correct": True},
            {"text": "The windowsill one was nearer the glass, so more carbon "
                     "dioxide reached its leaves.",
             "correct": False,
             "why": "The air in a room is the same on both sides of it. The "
                    "difference between these two plants is the light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s12",
        "band": "standard",
        "text": "A healthy pot plant is sealed inside a clear plastic bag and "
                "left in bright light. An hour later there is more oxygen "
                "inside the bag than there was at the start. Where has it "
                "come from?",
        "options": [
            {"text": "From the water the plant was given at the start, which "
                     "has evaporated off its leaves and collected inside the "
                     "bag.",
             "correct": False,
             "why": "Evaporating water gives water vapour, which is why the "
                    "bag mists up. The extra oxygen is a product of the "
                    "reaction going on inside the leaves."},
            {"text": "From the air that was already sealed inside the bag, "
                     "which has warmed up in the light and expanded.",
             "correct": False,
             "why": "Warming air does not create any more oxygen in it. What "
                    "is in the bag is oxygen the leaves have released."},
            {"text": "From the soil, which gives off oxygen when it has been "
                     "watered.",
             "correct": False,
             "why": "Soil does not supply the air with oxygen. The leaves do, "
                    "as a waste product of building glucose."},
            {"text": "The leaves released it as waste while building "
                     "glucose, and it left through the stomata.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s13",
        "band": "standard",
        "text": "A bottle sold in a garden centre is labelled plant food, and "
                "what is in it is a mixture of dissolved minerals. Why is "
                "that name misleading?",
        "options": [
            {"text": "Because the bottle is mostly water, and water is not a "
                     "food either.",
             "correct": False,
             "why": "There are real minerals dissolved in it. The problem is "
                    "not what is in the bottle — it is calling minerals "
                    "food."},
            {"text": "Because food means something that can be broken down to "
                     "release energy, and minerals cannot.",
             "correct": True},
            {"text": "Because minerals enter through the leaves rather than "
                     "the roots, so they are never eaten.",
             "correct": False,
             "why": "Minerals do go in through the roots. What makes the word "
                    "wrong is that they release no energy, so they are not "
                    "food."},
            {"text": "Because a plant needs no food of any kind, living on "
                     "light energy alone.",
             "correct": False,
             "why": "A plant certainly needs food — it simply makes its own, "
                    "which is what a producer is. Light is the energy that "
                    "lets it build that food."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-01-h05",
        "band": "harder",
        "text": "In bright light a pot plant builds glucose at 100 units an "
                "hour. The lamp is then dimmed and its rate falls to 35% of "
                "that. How much glucose does it build in the next four "
                "hours?",
        "options": [
            {"text": "35 units, because the 35% figure already covers the "
                     "whole four hours.",
             "correct": False,
             "why": "Both figures are rates — units an hour. Thirty-five "
                    "units is one hour's worth at 35%, so four hours give "
                    "four times that."},
            {"text": "400 units, because four hours at 100 units an hour "
                     "comes to 400.",
             "correct": False,
             "why": "That is the full-rate answer. The lamp is dimmed, so "
                    "only 35% of it is built: 140 units."},
            {"text": "140 units, because 35% of 100 units an hour is 35 units "
                     "an hour, for four hours.",
             "correct": True},
            {"text": "8.75 units, because 35 divided by four gives the amount "
                     "made in each of the four hours.",
             "correct": False,
             "why": "You have divided where you should have multiplied. Four "
                    "hours at 35 units an hour is 140 units, not less than a "
                    "single hour's worth."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h06",
        "band": "harder",
        "text": "A gardener lights a tray of lettuce for eighteen hours a day "
                "instead of twelve and it grows faster. Another gardener does "
                "the same to lettuce inside a sealed glass case and sees "
                "almost no extra growth. Explain the difference.",
        "options": [
            {"text": "In the sealed case the carbon dioxide is soon used up, "
                     "and no amount of light builds glucose without it.",
             "correct": True},
            {"text": "In the sealed case the extra light warms the air, and "
                     "warmth stops photosynthesis happening at all.",
             "correct": False,
             "why": "A sealed case does warm up, but that is not what has "
                    "stopped the growth. The reaction has run out of one of "
                    "its raw materials."},
            {"text": "The sealed plants have all the light they can hold, so "
                     "the extra hours are stored up for later.",
             "correct": False,
             "why": "Light is not stored. It supplies energy while it is "
                    "arriving, and the reaction still needs carbon dioxide to "
                    "spend that energy on."},
            {"text": "The glass blocks the light that plants can use, so the "
                     "extra hours make no difference to them.",
             "correct": False,
             "why": "The plants under glass do receive the light — a case is "
                    "glass, not a shutter. What they run short of is carbon "
                    "dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h07",
        "band": "harder",
        "text": "A student writes that photosynthesis is how plants breathe. "
                "What is wrong with that sentence?",
        "options": [
            {"text": "Nothing is wrong, since gases move into a leaf and out "
                     "of it again just as they do in your lungs.",
             "correct": False,
             "why": "Gases do move in and out, and that is gas exchange "
                    "rather than photosynthesis. Photosynthesis is the "
                    "reaction that builds glucose."},
            {"text": "Plants have no need of gases at all, so nothing that "
                     "happens in a leaf resembles breathing.",
             "correct": False,
             "why": "A leaf takes carbon dioxide in and lets oxygen out all "
                    "day, so gases certainly matter. The error is in the word "
                    "used for the reaction."},
            {"text": "Photosynthesis happens only at night, which is exactly "
                     "when a plant would need to take air in through its "
                     "leaves.",
             "correct": False,
             "why": "It is the other way round. Photosynthesis needs light "
                    "and stops in the dark, so nothing about it is a "
                    "night-time process."},
            {"text": "Photosynthesis builds glucose rather than moving air, "
                     "and plants also respire.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h08",
        "band": "harder",
        "text": "Over five years van Helmont's willow gained about 74 "
                "kilograms while the soil lost about 57 grams. Roughly how "
                "many times greater was the plant's gain than the soil's "
                "loss?",
        "options": [
            {"text": "About 1.3 times greater, since 74 divided by 57 is a "
                     "little over one.",
             "correct": False,
             "why": "You have divided kilograms by grams. Convert first: 74 "
                    "kilograms is 74 000 grams, which is about 1300 times 57 "
                    "grams."},
            {"text": "About 1300 times greater, since 74 kilograms is 74 000 "
                     "grams.",
             "correct": True},
            {"text": "About 130 times greater, since 74 kilograms is 7400 "
                     "grams.",
             "correct": False,
             "why": "A kilogram is a thousand grams, not a hundred. That "
                    "makes 74 000 grams against 57 grams, or about 1300 "
                    "times."},
            {"text": "About 13 times greater, since a gram is a tenth of a "
                     "kilogram.",
             "correct": False,
             "why": "A gram is a thousandth of a kilogram. Converting "
                    "properly gives 74 000 grams against 57 grams, about 1300 "
                    "times."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h09",
        "band": "harder",
        "text": "One book says almost all of a plant's mass comes from carbon "
                "dioxide; another says a living plant is mostly water. Which "
                "of them is right?",
        "options": [
            {"text": "The first only, because a living plant holds very "
                     "little water and what there is drains away as it grows.",
             "correct": False,
             "why": "A living plant is mostly water and you can feel it in a "
                    "fresh leaf. The carbon dioxide claim is about the "
                    "material left once the water has gone."},
            {"text": "The second only, because a trace gas could never supply "
                     "the mass of something as large as a tree.",
             "correct": False,
             "why": "Thin as the supply is, it is where the mass comes from. "
                    "The willow gained 74 kilograms while the soil lost 57 "
                    "grams."},
            {"text": "Both, because a living plant is mostly water and the "
                     "material left after drying was built from carbon "
                     "dioxide.",
             "correct": True},
            {"text": "Neither, because almost all of a plant's mass is taken "
                     "up from the soil through the roots.",
             "correct": False,
             "why": "Weighing the soil is what settled that. It barely "
                    "changes, however much new plant appears above it."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h10",
        "band": "harder",
        "text": "A plant sits under a bell jar in bright light for a day and "
                "its leaves make starch. Of the four things the reaction "
                "needed, which is present at the end in the same amount as at "
                "the start?",
        "options": [
            {"text": "The chlorophyll, which absorbs the light energy without "
                     "being used up.",
             "correct": True},
            {"text": "The water, since only the hydrogen in it is needed and "
                     "the rest is handed straight back.",
             "correct": False,
             "why": "Water is a reactant and is used up. Nothing about this "
                    "reaction returns most of it unchanged."},
            {"text": "The carbon dioxide, since the carbon is used and the "
                     "gas itself is returned to the jar.",
             "correct": False,
             "why": "The carbon dioxide is used up, which is exactly why the "
                    "amount of it in the jar falls all day."},
            {"text": "The glucose, since the leaf stores it rather than "
                     "spending it.",
             "correct": False,
             "why": "There was no glucose at the start. It is a product, so "
                    "there is more of it at the end rather than the same "
                    "amount."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h11",
        "band": "harder",
        "text": "Two pots of cress are set up. Pot A has a mineral feed and "
                "plenty of water in a dark cupboard; pot B has plain water on "
                "a bright windowsill. Which one grows, and why?",
        "options": [
            {"text": "Pot A, because the mineral feed is the food the "
                     "seedlings need in order to grow.",
             "correct": False,
             "why": "Minerals are not food and release no energy. With no "
                    "light there is nothing to build glucose with, feed or no "
                    "feed."},
            {"text": "Both about equally, because each of them has three of "
                     "the four things the reaction needs.",
             "correct": False,
             "why": "Three out of four is not three quarters of a rate. Pot A "
                    "has no light at all, so it builds nothing."},
            {"text": "Neither, because cress needs a mineral feed and bright "
                     "light together before it will grow.",
             "correct": False,
             "why": "Pot B has everything the reaction needs. Minerals are "
                    "used for other jobs, in milligram quantities, and are "
                    "not a raw material here."},
            {"text": "Pot B, because light is what the reaction runs on and "
                     "minerals supply no energy at all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h12",
        "band": "harder",
        "text": "Removing any one of the four things photosynthesis needs "
                "takes the rate to zero. A grower's glasshouse is short of "
                "carbon dioxide and the crop still grows. Are those two "
                "statements in conflict?",
        "options": [
            {"text": "Yes — if the rule holds, a crop that is short of "
                     "carbon dioxide ought to be making no glucose and no "
                     "starch at all.",
             "correct": False,
             "why": "Short is not absent. The rule is about taking a "
                    "condition away completely; the glasshouse only has less "
                    "of it than the crop could use."},
            {"text": "No — the rule is about removing a condition outright, "
                     "not about having less of it.",
             "correct": True},
            {"text": "No — the rule is about starch and the glasshouse is "
                     "about growth, so the two are not the same subject.",
             "correct": False,
             "why": "Growth is what the starch is evidence of, so they are "
                    "not different subjects. The real difference is between "
                    "removing something and reducing it."},
            {"text": "Yes — the glasshouse shows a crop can manage without "
                     "carbon dioxide if the light is bright enough.",
             "correct": False,
             "why": "No amount of light builds glucose with no carbon to "
                    "build it from. That crop has carbon dioxide; it simply "
                    "has less than it could use."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h13",
        "band": "harder",
        "text": "A student writes that a plant makes food out of sunlight. "
                "Which part of that sentence is right and which part is "
                "wrong?",
        "options": [
            {"text": "It is right throughout, because sunlight is the "
                     "material a plant builds its glucose from.",
             "correct": False,
             "why": "Light carries energy, not matter. Nothing about a beam "
                    "of light has any mass to give to a stem."},
            {"text": "It is wrong throughout, because a plant makes no food "
                     "of its own and simply takes everything it needs from "
                     "the soil around its roots.",
             "correct": False,
             "why": "A plant is the one kind of organism that makes its own "
                    "food. What it takes from the soil is water and minerals, "
                    "and neither is food."},
            {"text": "Making food is right; the material is carbon dioxide "
                     "and water, not sunlight.",
             "correct": True},
            {"text": "Out of sunlight is right; making food is wrong — a "
                     "plant stores energy but never builds anything of its "
                     "own.",
             "correct": False,
             "why": "A plant builds a great deal: glucose, and then starch "
                    "and cellulose out of it. The half that is wrong is where "
                    "the material comes from."},
        ],
        "figure": None,
    },
    # ── easier (MRB-338) ────────────────────────────────────────────────
    {
        "id": "b7-01-e14",
        "band": "easier",
        "text": "In which part of a plant cell does photosynthesis happen?",
        "options": [
            {"text": "In the cell wall, which is the part built from "
                     "cellulose.",
             "correct": False,
             "why": "The cell wall is built out of glucose once the reaction "
                    "has finished. It holds no chlorophyll, so it absorbs no "
                    "light."},
            {"text": "In the vacuole, which is the store of cell sap.",
             "correct": False,
             "why": "The vacuole keeps a plant cell firm. It holds no "
                    "pigment, so nothing is built there."},
            {"text": "In the chloroplast, which holds the pigment "
                     "chlorophyll.",
             "correct": True},
            {"text": "In the nucleus, which controls what the cell does.",
             "correct": False,
             "why": "The nucleus controls the cell but carries out no "
                    "photosynthesis. The reaction happens where the "
                    "chlorophyll is."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e15",
        "band": "easier",
        "text": "Almost all the oxygen in the atmosphere was put there by "
                "living organisms. Which process released it?",
        "options": [
            {"text": "Respiration, which is how animals return oxygen to the "
                     "air after they have finished with it.",
             "correct": False,
             "why": "Respiration takes oxygen out of the air and gives carbon "
                    "dioxide back. It spends oxygen rather than making it."},
            {"text": "Evaporation, which lifts oxygen out of the oceans and "
                     "carries it up into the atmosphere.",
             "correct": False,
             "why": "Evaporation lifts water vapour, not oxygen. The oxygen "
                    "dissolved in sea water was photosynthesised there in the "
                    "first place."},
            {"text": "Volcanic eruptions, which supplied the gases that the "
                     "early atmosphere was made of.",
             "correct": False,
             "why": "Volcanoes gave off mostly carbon dioxide and water "
                    "vapour. Oxygen appeared later, once photosynthesising "
                    "organisms had begun."},
            {"text": "Photosynthesis, which releases oxygen as a waste "
                     "product every time it builds glucose.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e16",
        "band": "easier",
        "text": "A plant grows a new shoot and needs new cell walls for it. "
                "What are those walls built from?",
        "options": [
            {"text": "Cellulose, built from the glucose the leaves made.",
             "correct": True},
            {"text": "Starch, built from minerals taken up by the roots.",
             "correct": False,
             "why": "Starch is a store rather than a wall, and minerals build "
                    "neither. A cell wall is cellulose, and cellulose is "
                    "built from glucose."},
            {"text": "Cellulose, built from the water taken up by the roots.",
             "correct": False,
             "why": "Water supplies only the hydrogen. Almost all the "
                    "material in a cell wall arrived as carbon dioxide and "
                    "was built into glucose first."},
            {"text": "Protein, built from the oxygen the leaves released.",
             "correct": False,
             "why": "Oxygen is a waste product and diffuses out of the leaf. "
                    "A plant cell wall is made of cellulose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e17",
        "band": "easier",
        "text": "A leaf turns some of its glucose into starch. What makes "
                "starch suited to being a store?",
        "options": [
            {"text": "Starch holds more energy than the glucose it was built "
                     "from, so a store of it lasts longer.",
             "correct": False,
             "why": "Converting glucose to starch adds no energy. What starch "
                    "does is stay where it is put."},
            {"text": "Starch is insoluble, so it stays in the cell that made "
                     "it instead of dissolving away.",
             "correct": True},
            {"text": "Starch dissolves easily, so it can be moved to "
                     "wherever the plant needs it.",
             "correct": False,
             "why": "Starch is insoluble, and that is exactly why it stays "
                    "put. Glucose is the soluble one that travels."},
            {"text": "Starch can be taken back in through the roots when the "
                     "plant needs it again.",
             "correct": False,
             "why": "Starch never goes near the roots. It is stored in the "
                    "cell that made it and converted back to glucose there."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e18",
        "band": "easier",
        "text": "Biologists call a plant a producer. What does that word "
                "mean?",
        "options": [
            {"text": "It produces the oxygen that every other organism "
                     "depends on for respiration.",
             "correct": False,
             "why": "A plant does release oxygen, but that is not what the "
                    "word means. Producer is about food."},
            {"text": "It produces minerals and passes them into the soil.",
             "correct": False,
             "why": "Minerals travel the other way — a plant takes them out "
                    "of the soil — and minerals are not food."},
            {"text": "It produces more offspring than an animal of its size.",
             "correct": False,
             "why": "Producer says nothing about offspring. It is about where "
                    "an organism's food comes from."},
            {"text": "It makes its own food rather than taking it from "
                     "another organism.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e19",
        "band": "easier",
        "text": "A leaf is tested with iodine solution and stays "
                "orange-brown. What does that tell you?",
        "options": [
            {"text": "There is no starch in that leaf, whatever glucose it "
                     "may still be holding.",
             "correct": True},
            {"text": "There is starch, because iodine keeps its own colour "
                     "wherever it finds starch present.",
             "correct": False,
             "why": "Iodine turns blue-black where starch is present. "
                    "Orange-brown is the colour it started as."},
            {"text": "There is plenty of glucose, none of it converted "
                     "into starch yet.",
             "correct": False,
             "why": "The test says nothing about glucose. Orange-brown tells "
                    "you starch is absent and stops there."},
            {"text": "The chlorophyll has been destroyed, so the leaf cannot "
                     "be tested a second time.",
             "correct": False,
             "why": "The colour of the iodine is about starch, not about "
                    "pigment. Nothing in the test destroys chlorophyll."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e20",
        "band": "easier",
        "text": "Before a starch test, a plant is left in the dark for two "
                "days. Why is that done first?",
        "options": [
            {"text": "To let the leaves take in extra carbon dioxide while "
                     "the light is off them.",
             "correct": False,
             "why": "Darkness does not load a leaf with carbon dioxide. What "
                    "it does is stop the plant making any more starch."},
            {"text": "To use up the starch already in the leaves, so any "
                     "found afterwards must have been made during the test.",
             "correct": True},
            {"text": "To break down the chlorophyll so the iodine colour "
                     "shows up clearly.",
             "correct": False,
             "why": "The chlorophyll is dealt with later, when the leaf is "
                    "decolourised. The two dark days are about the starch "
                    "that is already there."},
            {"text": "To make sure the plant is fully watered before the "
                     "test.",
             "correct": False,
             "why": "Watering has nothing to do with the darkness. The point "
                    "of the two days is to empty the leaves of starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e21",
        "band": "easier",
        "text": "A student says a plant takes in its food through its roots. "
                "What does a plant really take in through its roots?",
        "options": [
            {"text": "Sugars dissolved in the soil water.",
             "correct": False,
             "why": "Soil water holds no sugar for a plant to take up. A "
                    "plant builds its own sugar, in its leaves."},
            {"text": "Starch, which the soil supplies and the leaves store.",
             "correct": False,
             "why": "There is no starch in soil. The starch in a leaf was "
                    "made there, out of glucose the leaf built."},
            {"text": "Water, and dissolved minerals in milligram amounts.",
             "correct": True},
            {"text": "Carbon dioxide, which dissolves in soil water and is "
                     "drawn up the stem to the leaves.",
             "correct": False,
             "why": "Carbon dioxide reaches a leaf from the air through the "
                    "stomata, not up the stem from the soil."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e22",
        "band": "easier",
        "text": "The oxygen made in a leaf does not stay there. How does it "
                "leave the plant?",
        "options": [
            {"text": "It is carried down the stem and released into the "
                     "soil.",
             "correct": False,
             "why": "Oxygen leaves through the leaf that made it. Nothing "
                    "carries it down to the roots."},
            {"text": "It is stored in the vacuole until the plant needs it.",
             "correct": False,
             "why": "Oxygen is the waste product of this reaction, not a "
                    "store. The surplus diffuses out of the leaf."},
            {"text": "It is turned back into carbon dioxide in the leaf.",
             "correct": False,
             "why": "Nothing in the leaf turns the oxygen back. It leaves as "
                    "oxygen gas."},
            {"text": "It diffuses out through the stomata into the air "
                     "around the leaf that made it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e23",
        "band": "easier",
        "text": "Glucose is an energy store. Where was that energy before "
                "the plant built the glucose?",
        "options": [
            {"text": "In the minerals from the soil, which give up their "
                     "energy as the plant uses them.",
             "correct": False,
             "why": "Minerals supply no energy at all. They are needed in "
                    "tiny amounts to build particular molecules."},
            {"text": "In the light arriving at the leaf.",
             "correct": True},
            {"text": "In the carbon dioxide and the water, and the reaction "
                     "simply moved it across into the glucose.",
             "correct": False,
             "why": "Carbon dioxide and water hold less energy than glucose "
                    "does. The difference came from the light."},
            {"text": "Nowhere — the plant made the energy during the "
                     "reaction itself.",
             "correct": False,
             "why": "Nothing makes energy. Photosynthesis stores energy that "
                    "was already arriving as light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e24",
        "band": "easier",
        "text": "When does a plant respire?",
        "options": [
            {"text": "Only at night, because in the day photosynthesis takes "
                     "the place of respiration.",
             "correct": False,
             "why": "Respiration never stops. It runs through the day as "
                    "well, alongside photosynthesis, which is a different "
                    "reaction doing a different job."},
            {"text": "Only in the day, because that is when it has glucose "
                     "available to release energy from.",
             "correct": False,
             "why": "A plant has glucose available at night too, some of it "
                    "converted back from its starch store."},
            {"text": "Day and night, without stopping.",
             "correct": True},
            {"text": "Never, because it makes its own food and so has no "
                     "need to release energy from it.",
             "correct": False,
             "why": "Making food and using it are two different things. Every "
                    "living cell releases energy by respiring, plant cells "
                    "included."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e25",
        "band": "easier",
        "text": "Most of a plant's photosynthesis happens in its leaves. "
                "Give the reason.",
        "options": [
            {"text": "They are the only part that can reach the carbon "
                     "dioxide in the air.",
             "correct": False,
             "why": "A green stem reaches the air too and photosynthesises. "
                    "What makes leaves the main site is their shape and their "
                    "chloroplasts."},
            {"text": "They are the part furthest from the roots, so the water "
                     "reaches them last.",
             "correct": False,
             "why": "Being far from the roots is no advantage. Leaves are the "
                    "main site because they are broad, flat and full of "
                    "chloroplasts."},
            {"text": "They are the thinnest part, so light passes straight "
                     "through them.",
             "correct": False,
             "why": "Light passing straight through is light that was not "
                    "absorbed. A leaf is thin so that gases and light reach "
                    "its inner cells quickly."},
            {"text": "They are broad and flat, and packed with "
                     "chloroplasts that catch the light.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e26",
        "band": "easier",
        "text": "A student lists what photosynthesis needs: light, carbon "
                "dioxide, water, chlorophyll and minerals. Which item does "
                "not belong on the list?",
        "options": [
            {"text": "Chlorophyll, because it is not used up by the "
                     "reaction.",
             "correct": False,
             "why": "Chlorophyll is not used up, but it is genuinely needed — "
                    "without it no light energy is absorbed and nothing is "
                    "built."},
            {"text": "Minerals, because they are not a raw material for this "
                     "reaction.",
             "correct": True},
            {"text": "Water, because a plant short of it wilts rather than "
                     "stopping.",
             "correct": False,
             "why": "Water is one of the two raw materials, and it supplies "
                    "the hydrogen in glucose. Without it nothing is built."},
            {"text": "Light, because it is written above the arrow rather "
                     "than on the left.",
             "correct": False,
             "why": "Light is needed even though it is not a reactant. The "
                    "summary shows that by writing it above the arrow, not by "
                    "leaving it out."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e27",
        "band": "easier",
        "text": "A potato plant's roots are underground in the dark. How do "
                "they get the glucose they need?",
        "options": [
            {"text": "They absorb it from the soil, which is where a plant's "
                     "supply of sugar comes from.",
             "correct": False,
             "why": "There is no sugar in the soil to absorb. Every bit of a "
                    "plant's glucose was built in its own leaves."},
            {"text": "They photosynthesise in the dark, more slowly than a "
                     "leaf does in the light.",
             "correct": False,
             "why": "No light means no photosynthesis, however slow. Roots "
                    "have no chlorophyll either."},
            {"text": "They receive it from the leaves, carried down "
                     "through the stem.",
             "correct": True},
            {"text": "They do not need any, because only the green parts of "
                     "a plant use glucose.",
             "correct": False,
             "why": "Every living cell in a plant respires, and respiration "
                    "needs glucose. Root cells are no exception."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e28",
        "band": "easier",
        "text": "The word photosynthesis is built from photo, meaning light, "
                "and synthesis. What does synthesis mean?",
        "options": [
            {"text": "Breaking down, which is what respiration does.",
             "correct": False,
             "why": "Respiration breaks glucose down. Photosynthesis goes the "
                    "other way, which is why the word is not the same."},
            {"text": "Absorbing, which is what chlorophyll does to light.",
             "correct": False,
             "why": "Chlorophyll does absorb, but the second half of the word "
                    "names what is then made, not how the energy arrives."},
            {"text": "Storing, which is what a leaf does with starch.",
             "correct": False,
             "why": "The glucose is stored afterwards, but synthesis names "
                    "the building rather than the keeping."},
            {"text": "Building something up out of simpler substances.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e29",
        "band": "easier",
        "text": "A grower raises seedlings indoors under electric lamps, "
                "with no daylight on them at all. Will they photosynthesise?",
        "options": [
            {"text": "Yes, because the reaction needs light energy and does "
                     "not mind what the light came from.",
             "correct": True},
            {"text": "No, because only sunlight carries the energy this "
                     "reaction runs on.",
             "correct": False,
             "why": "Light from a lamp carries energy just as sunlight does. "
                    "What matters to the leaf is how much light arrives."},
            {"text": "No, because a plant also needs the warmth of the sun "
                     "before the reaction can start at all.",
             "correct": False,
             "why": "Warmth affects the rate, but it is not one of the four "
                    "things the reaction needs, and lamps give off heat "
                    "anyway."},
            {"text": "Yes, but only if the lamps are left on for the whole "
                     "twenty-four hours of every day.",
             "correct": False,
             "why": "A plant photosynthesises whenever there is light. It "
                    "does not need light around the clock to begin."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e30",
        "band": "easier",
        "text": "Glucose molecules contain carbon. Which raw material "
                "supplies that carbon?",
        "options": [
            {"text": "The water, which the roots take up out of the soil.",
             "correct": False,
             "why": "Water supplies the hydrogen. There is no carbon in water "
                    "at all."},
            {"text": "The minerals, dissolved in the water in the soil.",
             "correct": False,
             "why": "Minerals are taken up in milligram amounts to build "
                    "particular molecules. Nowhere near enough of them enters "
                    "to build a plant's glucose."},
            {"text": "The carbon dioxide, which diffuses in through the "
                     "stomata.",
             "correct": True},
            {"text": "The light, which the chlorophyll in the leaf absorbs.",
             "correct": False,
             "why": "Light carries energy, not matter. No part of a beam of "
                    "light ends up inside a molecule."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e31",
        "band": "easier",
        "text": "A rabbit eats grass and a fox eats the rabbit. Where did "
                "the energy in the fox's food enter the food chain?",
        "options": [
            {"text": "At the grass, which stored light energy by "
                     "photosynthesising.",
             "correct": True},
            {"text": "At the rabbit, which made the energy it needed out of "
                     "the grass it had eaten.",
             "correct": False,
             "why": "Nothing makes energy. The rabbit passed on energy the "
                    "grass had already stored."},
            {"text": "At the soil, which supplied the food the grass grew "
                     "on.",
             "correct": False,
             "why": "The soil supplies water and minerals, and neither is "
                    "food. The grass makes its own."},
            {"text": "At the fox, which is the largest animal in the chain "
                     "and so holds the most energy.",
             "correct": False,
             "why": "Being large is not the same as being where the energy "
                    "came in. It entered at the producer."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-e32",
        "band": "easier",
        "text": "Photosynthesis is called a chemical reaction rather than a "
                "physical change. What makes it one?",
        "options": [
            {"text": "It happens slowly, and physical changes are always "
                     "fast.",
             "correct": False,
             "why": "Speed does not decide it. Rusting is slow and melting "
                    "can be quick, and both are still what they are."},
            {"text": "New substances are made, and they are not the ones the "
                     "plant started with.",
             "correct": True},
            {"text": "It needs energy, and physical changes never do.",
             "correct": False,
             "why": "Melting ice needs energy and is a physical change. What "
                    "matters is whether new substances appear."},
            {"text": "It can be reversed, and only chemical changes can be.",
             "correct": False,
             "why": "Physical changes are the easy ones to reverse. Melting "
                    "and freezing are the obvious pair."},
        ],
        "figure": None,
    },

    # ── standard (MRB-338) ──────────────────────────────────────────────
    {
        "id": "b7-01-s14",
        "band": "standard",
        "text": "A destarched plant has a strip of foil clipped across one "
                "leaf and is left in bright light for a day. The leaf is "
                "then tested with iodine. Predict the result and say why.",
        "options": [
            {"text": "The whole leaf goes blue-black, because carbon "
                     "dioxide, water and chlorophyll reached every part of "
                     "it.",
             "correct": False,
             "why": "Three out of four is not enough. The strip under the "
                    "foil had no light, and all four are needed together."},
            {"text": "Blue-black except under the strip of foil, which "
                     "stays orange-brown because no light reached it.",
             "correct": True},
            {"text": "The whole leaf stays orange-brown, because covering "
                     "any part of a leaf stops the whole leaf working.",
             "correct": False,
             "why": "Each part of a leaf photosynthesises for itself. The lit "
                    "parts carried on making starch as usual."},
            {"text": "Blue-black under the foil only, because the foil kept "
                     "in the warmth the reaction needs.",
             "correct": False,
             "why": "The foil kept out the light, which is the condition that "
                    "matters here. Warmth is not one of the four."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s15",
        "band": "standard",
        "text": "A leaf builds glucose at 12 mg per hour while it is lit. "
                "The plant is in bright light for 9 hours. How much glucose "
                "does that leaf build?",
        "options": [
            {"text": "108 mg",
             "correct": True},
            {"text": "21 mg, from 12 + 9",
             "correct": False,
             "why": "That is 12 added to 9. A rate multiplied by a time gives "
                    "the total, so the two numbers multiply."},
            {"text": "1.3 mg",
             "correct": False,
             "why": "That is 12 divided by 9. Dividing would give you a rate "
                    "again, not a total."},
            {"text": "288 mg, at 12 mg an hour for a whole 24 hours",
             "correct": False,
             "why": "That is 12 for the whole 24 hours. The plant was lit for "
                    "9 of them, and no glucose is built in the dark."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s16",
        "band": "standard",
        "text": "Over a summer day a healthy plant takes in far more carbon "
                "dioxide than it gives out, and at night it gives out carbon "
                "dioxide and takes in none. Explain the difference.",
        "options": [
            {"text": "Photosynthesis stops in the dark while respiration "
                     "carries on, so at night only respiration's gases move.",
             "correct": True},
            {"text": "Respiration only happens at night, so in the day the "
                     "plant runs one reaction and after dark the other.",
             "correct": False,
             "why": "Respiration runs day and night. In daylight it is simply "
                    "hidden, because photosynthesis is using carbon dioxide "
                    "faster than respiration releases it."},
            {"text": "The plant reverses photosynthesis after dark, running "
                     "the same reaction backwards to get its energy.",
             "correct": False,
             "why": "Respiration is its own reaction with its own steps, not "
                    "photosynthesis run in reverse."},
            {"text": "The stomata close at night, which traps the carbon "
                     "dioxide the plant made during the day inside the leaf.",
             "correct": False,
             "why": "The carbon dioxide measured at night has just been "
                    "released by respiration, and it is leaving the plant "
                    "rather than being trapped."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s17",
        "band": "standard",
        "text": "A potato tuber grows underground in complete darkness, yet "
                "it is full of starch. Explain how the starch got there.",
        "options": [
            {"text": "The tuber photosynthesised underground, slowly, using "
                     "the small amount of light that reaches the soil.",
             "correct": False,
             "why": "No light reaches a buried tuber, and a tuber has no "
                    "chlorophyll to absorb it with."},
            {"text": "The tuber absorbed starch from the soil around it "
                     "through its skin, in the way a root absorbs water.",
             "correct": False,
             "why": "Soil contains no starch to absorb. Roots take up water "
                    "and dissolved minerals only."},
            {"text": "Glucose made in the leaves was carried down to the "
                     "tuber and stored there as starch.",
             "correct": True},
            {"text": "The tuber built starch out of the minerals the roots "
                     "took up, which is what a mineral feed is for.",
             "correct": False,
             "why": "Minerals are not the raw material for starch. Starch is "
                    "built from glucose, and glucose is built in the leaves."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s18",
        "band": "standard",
        "text": "The underside of one leaf on a destarched plant is coated "
                "with petroleum jelly. After a day in bright light that leaf "
                "makes almost no starch. Explain the result.",
        "options": [
            {"text": "The jelly blocked the stomata on the underside, so "
                     "almost no carbon dioxide could diffuse into the leaf.",
             "correct": True},
            {"text": "The jelly blocked the light, so the chlorophyll in "
                     "that leaf absorbed none of the energy the reaction "
                     "needs.",
             "correct": False,
             "why": "The coating is on the underside, away from the light, "
                    "and the leaf stayed green. What it stopped was the gas."},
            {"text": "The jelly stopped water reaching the leaf from the "
                     "stem, so there was no hydrogen for the glucose.",
             "correct": False,
             "why": "Water arrives inside the leaf through the stem, and a "
                    "coating on the surface cannot interrupt that."},
            {"text": "The jelly is poisonous to a leaf and destroyed its "
                     "chloroplasts, which is why nothing was built.",
             "correct": False,
             "why": "Petroleum jelly does not poison a leaf. It is used in "
                    "this investigation precisely because all it does is seal "
                    "the surface."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s19",
        "band": "standard",
        "text": "Carbon dioxide is about 0.04% of the air. A greenhouse "
                "holds 10 000 litres of air. What volume of that is carbon "
                "dioxide?",
        "options": [
            {"text": "400 litres",
             "correct": False,
             "why": "That is 4%, a hundred times too much. 0.04% is four "
                    "hundredths of one per cent."},
            {"text": "0.4 litres",
             "correct": False,
             "why": "That is ten times too little — a power of ten has been "
                    "dropped somewhere in the working."},
            {"text": "40 litres",
             "correct": False,
             "why": "That is 0.4%, ten times too much. Divide by 100 to turn "
                    "a percentage into a fraction, then multiply."},
            {"text": "4 litres",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s20",
        "band": "standard",
        "text": "Van Helmont covered his pot to keep dust off the soil for "
                "the whole five years. Why did covering it matter to his "
                "conclusion?",
        "options": [
            {"text": "It stopped the plant taking in carbon dioxide, which "
                     "is what made the experiment a fair one.",
             "correct": False,
             "why": "The leaves were above the cover and in open air "
                    "throughout. A pot cover does not seal off a tree."},
            {"text": "It kept the soil dry, so that only the water he added "
                     "himself could reach the willow's roots.",
             "correct": False,
             "why": "He watered the pot for five years, so the soil was not "
                    "kept dry. The cover was about dust."},
            {"text": "Without it, blown dust could have added mass to the "
                     "soil and hidden how much the soil had really lost.",
             "correct": True},
            {"text": "It kept the light off the soil, so that nothing could "
                     "photosynthesise except the willow itself.",
             "correct": False,
             "why": "Soil does not photosynthesise, and any weed could have "
                    "been pulled out. The measurement at risk was the mass of "
                    "the soil."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s21",
        "band": "standard",
        "text": "In the 1770s Joseph Priestley found that a candle burning "
                "in a sealed jar soon went out, but that it burned for "
                "longer if a sprig of mint had been left growing in the jar "
                "first. Explain the mint's effect.",
        "options": [
            {"text": "The mint used up the carbon dioxide in the jar, and "
                     "carbon dioxide is what puts a candle flame out.",
             "correct": False,
             "why": "The mint did take carbon dioxide in, but a candle needs "
                    "oxygen to burn. It was the oxygen the mint added that "
                    "kept the flame going."},
            {"text": "The mint released oxygen into the jar as it "
                     "photosynthesised, and a candle needs oxygen in order to "
                     "burn.",
             "correct": True},
            {"text": "The mint gave out water vapour, which cooled the jar "
                     "and slowed the candle down so that it lasted longer.",
             "correct": False,
             "why": "A cooler jar does not make a candle burn for longer. "
                    "What the flame ran out of was oxygen."},
            {"text": "The mint made the air in the jar heavier, so more air "
                     "was packed in for the candle to burn through.",
             "correct": False,
             "why": "A sealed jar holds the air it holds. The change was in "
                    "what the air was made of, not in how much there was."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s22",
        "band": "standard",
        "text": "A newly planted woodland puts on tonnes of wood over "
                "thirty years. What has happened to the carbon in that wood "
                "over those years?",
        "options": [
            {"text": "It was taken out of the soil by the roots and built "
                     "into the trunks, which is why forest soil is poor.",
             "correct": False,
             "why": "Roots take up water and dissolved minerals only. The "
                    "soil under a growing wood loses nothing like the mass of "
                    "the trees."},
            {"text": "It was made by the trees out of the light energy their "
                     "leaves absorbed over the thirty years.",
             "correct": False,
             "why": "Light carries energy, not matter, and carbon atoms are "
                    "not made by anything. They were already in the air."},
            {"text": "It was taken from the water the trees were given, "
                     "which is the only raw material a tree gets in "
                     "quantity.",
             "correct": False,
             "why": "Water supplies the hydrogen. The carbon arrived as "
                    "carbon dioxide, through the leaves."},
            {"text": "It was taken out of the air as carbon dioxide and is "
                     "now locked up in the wood the trees have grown.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s23",
        "band": "standard",
        "text": "Two identical winter glasshouses are kept at the same "
                "temperature, one by an electric heater and one by a "
                "paraffin burner. The crop under the paraffin burner yields "
                "more. Suggest why.",
        "options": [
            {"text": "Paraffin flames give out light as well as heat, and "
                     "that light is what raised the rate.",
             "correct": False,
             "why": "A burner's flame is far too dim to matter beside "
                    "daylight. What it adds in useful quantity is a gas."},
            {"text": "Electric heaters dry the air, and a dry plant closes "
                     "its stomata whatever the temperature is.",
             "correct": False,
             "why": "The plants were watered in both houses. The difference "
                    "between the two is what the paraffin puts into the air."},
            {"text": "Burning paraffin releases carbon dioxide, and a "
                     "glasshouse crop is often short of it.",
             "correct": True},
            {"text": "Burning paraffin uses up oxygen, and less oxygen in "
                     "the air lets photosynthesis run faster.",
             "correct": False,
             "why": "Oxygen is a product of this reaction, and the amount in "
                    "the air is not what holds the rate back."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s24",
        "band": "standard",
        "text": "A gardener gives her houseplant twice the recommended dose "
                "of mineral feed, expecting it to grow twice as fast. It "
                "does not. Explain why not.",
        "options": [
            {"text": "The feed has to be given at night, when the plant is "
                     "not busy photosynthesising and can take it up "
                     "properly.",
             "correct": False,
             "why": "Uptake is not the issue and there is no right time of "
                    "day for it. Minerals are simply not what growth is built "
                    "from."},
            {"text": "Minerals are needed in milligram amounts to build "
                     "particular molecules, so extra does not build extra "
                     "plant.",
             "correct": True},
            {"text": "The extra minerals were used up by the plant in one "
                     "day, so there was none left for the rest of the week.",
             "correct": False,
             "why": "A plant uses minerals so slowly that a normal dose lasts "
                    "for weeks. Running out is not what happened."},
            {"text": "Mineral feed only works on plants grown outdoors, "
                     "where there is soil for it to soak into.",
             "correct": False,
             "why": "The same minerals work in a pot. The reason the double "
                    "dose changed nothing is that minerals are not the raw "
                    "material for photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s25",
        "band": "standard",
        "text": "A fish tank with a bright lamp and plenty of water plants "
                "needs less air pumped into it than a bare tank does. "
                "Explain why.",
        "options": [
            {"text": "The plants take in the oxygen the fish give out, which "
                     "keeps the water from becoming too rich in it.",
             "correct": False,
             "why": "Fish take oxygen in and give carbon dioxide out. It is "
                    "the plants that add oxygen to the water."},
            {"text": "The lamp warms the water, and warm water holds much "
                     "more dissolved oxygen than cold.",
             "correct": False,
             "why": "Warm water actually holds less dissolved oxygen. The "
                    "oxygen here is coming from the plants."},
            {"text": "The plants filter the water, and clean water needs "
                     "less air pumped through it than dirty water does.",
             "correct": False,
             "why": "The pump is there to supply oxygen rather than to clean. "
                    "What the plants add is the gas itself."},
            {"text": "The plants release oxygen into the water while they "
                     "photosynthesise, and the fish can use it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s26",
        "band": "standard",
        "text": "Two leaves are taken from one plant on a windowsill at "
                "sunset: one after a bright clear day, one after a day of "
                "thick cloud. Both are tested with iodine. Compare the "
                "results.",
        "options": [
            {"text": "Both go the same deep blue-black, because the plant "
                     "was in daylight on both days and light is a condition "
                     "rather than a reactant.",
             "correct": False,
             "why": "Being a condition does not make brightness irrelevant. "
                    "Less light gives a lower rate and so less starch."},
            {"text": "The cloudy-day leaf goes darker, because a plant works "
                     "harder to make up for the light it has lost.",
             "correct": False,
             "why": "A plant cannot work harder to compensate. Less light "
                    "simply means a lower rate."},
            {"text": "The clear-day leaf gives the deeper blue-black, "
                     "because a higher rate made more glucose and so more "
                     "starch.",
             "correct": True},
            {"text": "Both stay orange-brown, because a leaf only stores "
                     "starch overnight and there is none in it at sunset.",
             "correct": False,
             "why": "Sunset is when a leaf's starch is at its highest, after "
                    "a day of building it. It is used up overnight, not "
                    "made."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s27",
        "band": "standard",
        "text": "Plant A builds 480 units of glucose in 8 hours of light. "
                "Plant B builds 350 units in 5 hours. Which plant is "
                "photosynthesising at the higher rate?",
        "options": [
            {"text": "Plant A, because 480 units is the larger total of the "
                     "two.",
             "correct": False,
             "why": "A rate is an amount per hour. Plant A had three more "
                    "hours to build its total in, so the totals cannot be "
                    "compared directly."},
            {"text": "Plant B, at 70 units per hour against plant A's 60.",
             "correct": True},
            {"text": "Neither — they are the same, because 480 is to 8 as "
                     "350 is to 5.",
             "correct": False,
             "why": "480 divided by 8 is 60 and 350 divided by 5 is 70, so "
                    "the two rates are not equal."},
            {"text": "Plant A, at 60 units per hour against plant B's 58.",
             "correct": False,
             "why": "350 divided by 5 is 70, not 58. Divide the total by the "
                    "hours it took."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s28",
        "band": "standard",
        "text": "A pot plant left in a cupboard for three weeks comes out "
                "pale, thin and much lighter than it went in. Explain what "
                "has happened to it.",
        "options": [
            {"text": "It made no new glucose in the dark and respired the "
                     "store it had, so it lost mass steadily.",
             "correct": True},
            {"text": "It photosynthesised as usual but had no minerals in "
                     "the cupboard air, so it could not build any new "
                     "tissue.",
             "correct": False,
             "why": "There is no photosynthesis without light, and minerals "
                    "come from the soil in the pot rather than from the air."},
            {"text": "It stopped respiring in the dark, so its cells had no "
                     "energy and began to break down.",
             "correct": False,
             "why": "Respiration carried on the whole time. That is exactly "
                    "why the plant lost mass with nothing coming in."},
            {"text": "It used up all its water, because water is what a "
                     "plant lives on when it cannot photosynthesise.",
             "correct": False,
             "why": "A watered plant does not run out of water in a cupboard, "
                    "and water is not food. What it lived on was its glucose "
                    "and starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s29",
        "band": "standard",
        "text": "A student says photosynthesis is simply respiration "
                "backwards. How far is that fair?",
        "options": [
            {"text": "It is completely fair: the two are the same reaction, "
                     "run forwards in the light and backwards in the dark by "
                     "the same cells.",
             "correct": False,
             "why": "They are two separate reactions with separate steps, and "
                    "one is not the other run in reverse."},
            {"text": "It is not fair at all, because the two reactions have "
                     "no substances in common with one another.",
             "correct": False,
             "why": "They have all four in common, which is where the idea "
                    "comes from. What is wrong is calling them one reaction."},
            {"text": "It is not fair, because respiration only happens at "
                     "night while photosynthesis only happens in the day.",
             "correct": False,
             "why": "Respiration runs day and night, so that is not the "
                    "difference between them."},
            {"text": "The substances match up, but they are two different "
                     "reactions rather than one run in reverse.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s30",
        "band": "standard",
        "text": "About half of all the photosynthesis on Earth happens in "
                "the oceans rather than on land. What does that tell you "
                "about the oxygen in the air?",
        "options": [
            {"text": "That a large share of it was released by organisms "
                     "living in the sea.",
             "correct": True},
            {"text": "That the oxygen in the air came out of the sea water "
                     "itself as it evaporated over millions of years.",
             "correct": False,
             "why": "Evaporating sea water gives water vapour. The oxygen was "
                    "released by photosynthesising organisms in the water."},
            {"text": "That the oxygen in the sea is a different gas from the "
                     "oxygen in the air, and the two never mix together.",
             "correct": False,
             "why": "Oxygen is oxygen wherever it is, and gases dissolve out "
                    "of water into the air above it."},
            {"text": "That forests make no difference to the oxygen in the "
                     "air, so cutting them down cannot change it at all.",
             "correct": False,
             "why": "Half on land is still an enormous share. Losing forests "
                    "matters, and it matters most for the carbon they hold."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s31",
        "band": "standard",
        "text": "A class wants to show that carbon dioxide is needed for "
                "photosynthesis. Two destarched plants are used, one with "
                "soda lime beside it under a sealed jar. What must be kept "
                "the same for both?",
        "options": [
            {"text": "The light, the water and the temperature, so that "
                     "the carbon dioxide is the only thing that differs "
                     "between them.",
             "correct": True},
            {"text": "Only the temperature, because heat is what changes the "
                     "rate most, and the rest can be left to look after "
                     "themselves.",
             "correct": False,
             "why": "Any condition left to differ could explain the result "
                    "instead. All of them but the one being tested are held "
                    "the same."},
            {"text": "Nothing needs to match, as long as both plants are "
                     "destarched at the start and tested at the same time "
                     "afterwards.",
             "correct": False,
             "why": "Destarching is a good start but it is not enough. A "
                    "plant left in poorer light would give the same result "
                    "for the wrong reason."},
            {"text": "Everything, including the amount of carbon dioxide, so "
                     "that the two plants are treated identically "
                     "throughout.",
             "correct": False,
             "why": "The carbon dioxide is the one thing that must differ. It "
                    "is the variable being tested."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-s32",
        "band": "standard",
        "text": "A destarched plant is put into bright light for twenty "
                "minutes and a leaf is tested at once. The iodine stays "
                "orange-brown. What is the best explanation?",
        "options": [
            {"text": "Too little glucose was built in twenty minutes for any "
                     "starch to show.",
             "correct": True},
            {"text": "Twenty minutes of light destroys the chlorophyll, so "
                     "nothing could be built after the first few minutes.",
             "correct": False,
             "why": "Bright light does not destroy chlorophyll. The leaf was "
                    "green and working throughout."},
            {"text": "The destarching had failed, which is why no starch "
                     "could be found in the leaf afterwards.",
             "correct": False,
             "why": "Destarching removes starch, so a successful destarch is "
                    "part of why the leaf began with none."},
            {"text": "Photosynthesis cannot begin until a plant has been in "
                     "the light for a full day after being kept in the "
                     "dark.",
             "correct": False,
             "why": "The reaction starts as soon as light arrives. What takes "
                    "time is building enough starch for iodine to find."},
        ],
        "figure": None,
    },

    # ── harder (MRB-338) ────────────────────────────────────────────────
    {
        "id": "b7-01-h14",
        "band": "harder",
        "text": "A wheat crop builds about 20 g of glucose per square metre "
                "each day. One hectare is 10 000 square metres. How much "
                "glucose does a hectare of that crop build in a day?",
        "options": [
            {"text": "20 kg, because a hectare is a thousand square metres "
                     "and 20 g becomes 20 kg.",
             "correct": False,
             "why": "A hectare is ten thousand square metres, not a thousand. "
                    "A power of ten has been lost."},
            {"text": "2000 kg",
             "correct": False,
             "why": "That is ten times too much. 20 × 10 000 g is 200 000 g, "
                    "and 200 000 g is 200 kg."},
            {"text": "200 g",
             "correct": False,
             "why": "That is the mass for ten square metres. The area is a "
                    "thousand times larger than that."},
            {"text": "200 kg, because 20 g × 10 000 is 200 000 g.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h15",
        "band": "harder",
        "text": "A freshly cut plant has a mass of 500 g, and 80% of that "
                "is water. Almost all of what is left was built from carbon "
                "dioxide. What mass was built from carbon dioxide?",
        "options": [
            {"text": "400 g, the mass of the water in it",
             "correct": False,
             "why": "400 g is the water — 80% of 500 g. The material built "
                    "from carbon dioxide is what remains after the water has "
                    "gone."},
            {"text": "20 g",
             "correct": False,
             "why": "20 is the percentage that is not water, not the mass. "
                    "20% of 500 g is 100 g."},
            {"text": "100 g",
             "correct": True},
            {"text": "80 g",
             "correct": False,
             "why": "80 is the percentage that is water. It is not a mass, "
                    "and it belongs to the wrong part of the plant."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h16",
        "band": "harder",
        "text": "Chlorophyll absorbs red and blue light strongly and "
                "reflects green, which is why a leaf looks green. Predict "
                "how a plant grown under pure green light would do.",
        "options": [
            {"text": "It would grow better than in white light, because "
                     "green light is the colour a green plant is built to "
                     "use.",
             "correct": False,
             "why": "A leaf looks green because green is the light it "
                    "reflects — the light it is not absorbing."},
            {"text": "Poorly, because chlorophyll reflects most of the "
                     "green light instead of absorbing it, so little energy "
                     "is taken in.",
             "correct": True},
            {"text": "Exactly as well as in white light, because light is a "
                     "condition and its colour cannot matter to the rate.",
             "correct": False,
             "why": "Only light that is absorbed can supply energy, so which "
                    "colours a pigment absorbs matters a great deal."},
            {"text": "It would not grow at all, because a plant needs red "
                     "and blue light together and green light is no use to "
                     "any organism.",
             "correct": False,
             "why": "Some green light is absorbed, so the rate is low rather "
                    "than zero. Other pigments in other organisms absorb "
                    "green well."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h17",
        "band": "harder",
        "text": "A student covers one leaf of a plant with foil, leaves the "
                "plant in the light, finds no starch in the covered leaf, "
                "and concludes that light is needed. Evaluate that "
                "conclusion.",
        "options": [
            {"text": "It is sound as it stands, because the covered leaf "
                     "made no starch and the covering is what kept the light "
                     "off it.",
             "correct": False,
             "why": "The result fits, but without a lit leaf tested from the "
                    "same plant there is nothing to show the plant was making "
                    "starch at all."},
            {"text": "It is unsafe until an uncovered leaf from the same "
                     "plant has been tested as a control and found to have "
                     "starch.",
             "correct": True},
            {"text": "It is unsafe, because a covered leaf is short of "
                     "carbon dioxide as well and either shortage would give "
                     "the same result.",
             "correct": False,
             "why": "Foil clipped over a leaf does not seal its stomata, and "
                    "the air moves around it freely. The missing piece is the "
                    "comparison."},
            {"text": "It is unsafe, because starch tests cannot be trusted "
                     "on a leaf that has been covered up for a day.",
             "correct": False,
             "why": "The iodine test works the same on any leaf. What the "
                    "investigation lacks is a control to compare against."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h18",
        "band": "harder",
        "text": "At dusk the light fades, and for a short while a plant "
                "takes in no carbon dioxide from the air and gives out none "
                "either. Explain what is happening at that moment.",
        "options": [
            {"text": "Both reactions have stopped, so no gas is moving in "
                     "either direction at all.",
             "correct": False,
             "why": "Respiration does not stop at dusk. Both reactions are "
                    "running, and their gas exchange happens to cancel."},
            {"text": "The stomata have closed for the night, so no gas can "
                     "get in or out of the leaf whatever the reactions are "
                     "doing.",
             "correct": False,
             "why": "If the stomata simply shut, the carbon dioxide from "
                    "respiration would build up inside the leaf. The two "
                    "reactions are balancing."},
            {"text": "Photosynthesis has slowed until it uses carbon dioxide "
                     "at exactly the rate respiration releases it.",
             "correct": True},
            {"text": "Photosynthesis has stopped and respiration has not yet "
                     "started, because a plant only begins to respire once it "
                     "is fully dark.",
             "correct": False,
             "why": "Respiration runs day and night without pausing. It does "
                    "not wait for darkness to begin."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h19",
        "band": "harder",
        "text": "A campaigner says planting a forest removes carbon dioxide "
                "from the air permanently. Evaluate that claim.",
        "options": [
            {"text": "It is right: once carbon has been built into wood it "
                     "can never return to the air in any form.",
             "correct": False,
             "why": "Burning the wood, or letting it rot, returns exactly the "
                    "carbon the trees took out."},
            {"text": "The carbon is held while the wood is, but burning or "
                     "rotting returns all of it to the air.",
             "correct": True},
            {"text": "It is wrong, because trees give out as much carbon "
                     "dioxide as they take in and so remove none of it.",
             "correct": False,
             "why": "A growing tree takes in far more than it respires. The "
                    "extra is what the trunk is built from."},
            {"text": "It is wrong, because the carbon in wood came out of "
                     "the soil rather than out of the air in the first "
                     "place.",
             "correct": False,
             "why": "Almost all of a tree's dry mass came from carbon dioxide "
                    "in the air, which is what van Helmont's soil showed."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h20",
        "band": "harder",
        "text": "About half the dry mass of wood is carbon. A tree adds 25 "
                "kg of dry mass in a year. Roughly what mass of carbon did "
                "it take out of the air over that year?",
        "options": [
            {"text": "About 12.5 kg",
             "correct": True},
            {"text": "About 50 kg",
             "correct": False,
             "why": "That doubles the dry mass instead of halving it. The "
                    "carbon is part of the wood, so it must be less than the "
                    "wood."},
            {"text": "About 25 kg, the whole of the dry mass",
             "correct": False,
             "why": "That is all of the dry mass. The other half is mostly "
                    "hydrogen and oxygen, and the hydrogen came from water."},
            {"text": "About 2.5 kg",
             "correct": False,
             "why": "That is a tenth rather than a half — a power of ten has "
                    "slipped into the working."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h21",
        "band": "harder",
        "text": "A class measures the oxygen a plant releases in an hour "
                "and calls it the amount photosynthesis produced. Why is "
                "their figure an underestimate?",
        "options": [
            {"text": "Because some oxygen dissolves back into the water in "
                     "the soil before it can be collected.",
             "correct": False,
             "why": "A little may dissolve, but there is a much larger and "
                    "more certain loss inside the plant itself."},
            {"text": "Because the plant respires at the same time and uses "
                     "up some of the oxygen it has just made.",
             "correct": True},
            {"text": "Because oxygen escapes through the stomata, so a "
                     "sealed apparatus can never collect all of it.",
             "correct": False,
             "why": "The stomata are how the oxygen reaches the apparatus in "
                    "the first place. Sealed apparatus collects what leaves "
                    "the leaf."},
            {"text": "Because an hour is too short a time for a plant to "
                     "reach the rate it eventually settles at.",
             "correct": False,
             "why": "A lit plant is photosynthesising throughout the hour. "
                    "The gap is respiration, which never stops."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h22",
        "band": "harder",
        "text": "Plant A is in bright light for 6 hours at 100 units of "
                "glucose an hour. Plant B is in dim light for 12 hours at "
                "half that rate. Compare the amounts they build.",
        "options": [
            {"text": "Plant B builds twice as much, because it had twice as "
                     "long in the light as plant A did.",
             "correct": False,
             "why": "Twice the time at half the rate is the same total. Both "
                    "the rate and the time have to be used."},
            {"text": "They build the same amount, 600 units each, because "
                     "twice the time at half the rate cancels out.",
             "correct": True},
            {"text": "Plant A builds twice as much, because bright light "
                     "always beats dim light whatever the timings are.",
             "correct": False,
             "why": "Bright light gives a higher rate, but plant B ran for "
                    "twice as long, and here the two exactly cancel."},
            {"text": "Plant B builds nothing at all, because dim light is "
                     "not enough to drive the reaction in the first place.",
             "correct": False,
             "why": "Dim light gives a low rate rather than no rate. Only "
                    "removing the light altogether takes it to zero."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h23",
        "band": "harder",
        "text": "A leaf builds 210 units of glucose over 3.5 hours of "
                "steady light. Determine its rate, with the unit.",
        "options": [
            {"text": "60 units per hour",
             "correct": True},
            {"text": "735 units per hour",
             "correct": False,
             "why": "That multiplies the total by the time. A rate is a total "
                    "divided by the time it took."},
            {"text": "105 units per hour",
             "correct": False,
             "why": "That divides by 2 rather than by 3.5. The light was on "
                    "for three and a half hours."},
            {"text": "6 units per hour",
             "correct": False,
             "why": "That is ten times too small — a power of ten has been "
                    "dropped from the division."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h24",
        "band": "harder",
        "text": "A variegated plant and an all-green plant of the same size "
                "are grown side by side in identical conditions. Predict "
                "which grows faster, and why.",
        "options": [
            {"text": "The variegated one, because the white tissue lets "
                     "light through to the cells underneath it.",
             "correct": False,
             "why": "Light reaching a cell with no chlorophyll is light that "
                    "is not absorbed. The white tissue photosynthesises "
                    "nothing."},
            {"text": "Neither — they grow at the same rate, because both "
                     "plants have the same leaf area exposed to the light.",
             "correct": False,
             "why": "Area is not the point. Only the green part of that area "
                    "has any chlorophyll in it."},
            {"text": "The variegated one, because it spends nothing on "
                     "making chlorophyll for its white parts and can put that "
                     "into growth.",
             "correct": False,
             "why": "Any small saving is dwarfed by the glucose the white "
                    "tissue fails to make."},
            {"text": "The all-green one, because more of its leaf area holds "
                     "chlorophyll and so more of it photosynthesises.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h25",
        "band": "harder",
        "text": "A student says that because a fox eats only meat, "
                "photosynthesis has nothing to do with how a fox gets its "
                "energy. Evaluate that.",
        "options": [
            {"text": "It is right, because a fox eats no plants and so takes "
                     "in none of the glucose a plant has built.",
             "correct": False,
             "why": "The energy is passed along, not the plant. Whatever the "
                    "fox eats was fed by something that ate a producer."},
            {"text": "It is right, because the energy a fox uses comes from "
                     "its own respiration rather than from anything a plant "
                     "did.",
             "correct": False,
             "why": "Respiration releases energy from food. It does not "
                    "create it, and the food came from a producer."},
            {"text": "It is wrong: the energy entered at the producer and "
                     "was passed along the chain to the fox.",
             "correct": True},
            {"text": "It is wrong, because a fox photosynthesises a little "
                     "itself when the sun is on its back.",
             "correct": False,
             "why": "No animal photosynthesises. A fox has no chlorophyll and "
                    "no chloroplasts."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h26",
        "band": "harder",
        "text": "In a clear lake, rooted plants grow only in the top few "
                "metres, although the water is just as rich in carbon "
                "dioxide lower down. Suggest why.",
        "options": [
            {"text": "The water is colder deeper down, and cold stops "
                     "photosynthesis happening at all whatever the light "
                     "is.",
             "correct": False,
             "why": "Cold lowers the rate rather than stopping the reaction. "
                    "The condition that runs out with depth is light."},
            {"text": "There are no minerals in the deep sediment, so a plant "
                     "rooted there would have no raw materials to build "
                     "with.",
             "correct": False,
             "why": "Lake sediment is rich in minerals, and minerals are not "
                    "raw materials for this reaction anyway."},
            {"text": "The pressure lower down closes the stomata, so no "
                     "carbon dioxide can reach the cells inside the leaf.",
             "correct": False,
             "why": "Pressure at a few metres does not shut a plant down, and "
                    "the question already says the carbon dioxide is there."},
            {"text": "Too little light reaches the deeper water for "
                     "photosynthesis to build enough glucose to keep a plant "
                     "alive.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h27",
        "band": "harder",
        "text": "A leaf of area 4 cm² builds 0.8 mg of glucose an hour in "
                "bright light. Predict the rate for a 12 cm² leaf on the "
                "same plant in the same light.",
        "options": [
            {"text": "9.6 mg per hour",
             "correct": False,
             "why": "That multiplies by 12 rather than by 3. The new leaf is "
                    "three times the area, not twelve times."},
            {"text": "0.27 mg per hour",
             "correct": False,
             "why": "That divides by 3. A larger leaf catches more light and "
                    "builds more, not less."},
            {"text": "1.6 mg per hour",
             "correct": False,
             "why": "That doubles the rate. Going from 4 cm² to 12 cm² is a "
                    "trebling."},
            {"text": "2.4 mg per hour, since 12 cm² is three times 4 cm².",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h28",
        "band": "harder",
        "text": "A class raises the light on a plant step by step. The rate "
                "climbs at first, then levels off and will not rise further "
                "however bright the lamp. Explain the levelling off.",
        "options": [
            {"text": "The chlorophyll has been used up by then, so there is "
                     "none left to absorb the extra light with.",
             "correct": False,
             "why": "Chlorophyll is not used up by the reaction. It is still "
                    "there, absorbing, however long the lamp is on."},
            {"text": "The leaf has absorbed all the light it can hold, and "
                     "stores the rest for later use in the dark.",
             "correct": False,
             "why": "Light is not stored for later. Once something else is "
                    "in short supply, extra light simply goes unused."},
            {"text": "Light has stopped being the condition in shortest "
                     "supply, and something else is now holding the rate "
                     "back.",
             "correct": True},
            {"text": "The plant has made as much glucose as it needs, so it "
                     "shuts the reaction down until the store runs low.",
             "correct": False,
             "why": "A plant does not switch off once it has enough. The "
                    "ceiling comes from a condition running short."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h29",
        "band": "harder",
        "text": "Over a week a plant takes in 44 g of carbon dioxide and 18 "
                "g of water for photosynthesis, and releases 32 g of "
                "oxygen. By how much does its mass rise from the reaction?",
        "options": [
            {"text": "62 g, the whole of what it took in.",
             "correct": False,
             "why": "The oxygen leaves the plant, so its mass is not kept. "
                    "Only the glucose stays behind."},
            {"text": "30 g, because the plant keeps what came in and loses "
                     "what went out.",
             "correct": True},
            {"text": "94 g, adding everything the reaction involved "
                     "together.",
             "correct": False,
             "why": "The oxygen released is a product leaving the plant, so "
                    "it is subtracted rather than added."},
            {"text": "12 g, the difference between the carbon dioxide taken "
                     "in and the oxygen released.",
             "correct": False,
             "why": "The water taken in belongs in the sum too. It supplies "
                    "the hydrogen in the glucose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h30",
        "band": "harder",
        "text": "A class collects gas from a jar holding a lit plant and "
                "shows it relights a glowing splint. A second jar is set up "
                "in the same light with no plant in it. What is that second "
                "jar for?",
        "options": [
            {"text": "To warm up alongside the first, so that both jars end "
                     "the experiment at the same temperature.",
             "correct": False,
             "why": "Matching the temperature is worth doing, but that is not "
                    "what an empty jar demonstrates."},
            {"text": "To supply the plant in the first jar with extra air "
                     "once it has used up what it started with.",
             "correct": False,
             "why": "The two jars are separate. Nothing passes from one to "
                    "the other."},
            {"text": "To show that no oxygen collects without a plant, so "
                     "the gas in the first jar must have come from the "
                     "plant.",
             "correct": True},
            {"text": "To give a second set of readings, so that the mean of "
                     "the two is more reliable than one alone.",
             "correct": False,
             "why": "A jar with no plant is not a repeat of the same "
                    "measurement. It is a control."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h31",
        "band": "harder",
        "text": "Priestley's mint sometimes freshened the air in a jar and "
                "sometimes did not, and he could not say why. Jan "
                "Ingenhousz later found the missing condition. What was it?",
        "options": [
            {"text": "The sprigs had to be in the light, because a plant "
                     "only releases oxygen while its leaves are being lit.",
             "correct": True},
            {"text": "The sprigs had to be freshly cut, because a wilting "
                     "plant releases carbon dioxide instead of oxygen.",
             "correct": False,
             "why": "A plant releases carbon dioxide by respiring whatever "
                    "its condition. The difference Ingenhousz found was "
                    "light."},
            {"text": "The jar had to be sealed tightly, because any leak let "
                     "the oxygen escape before it could be tested.",
             "correct": False,
             "why": "Priestley's jars were sealed. What varied between his "
                    "successes and his failures was whether they were lit."},
            {"text": "The sprigs had to be given a mineral feed, because "
                     "without minerals no plant can release oxygen into the "
                     "air around it.",
             "correct": False,
             "why": "Minerals are not needed for this reaction. A cutting in "
                    "plain water releases oxygen perfectly well in the "
                    "light."},
        ],
        "figure": None,
    },
    {
        "id": "b7-01-h32",
        "band": "harder",
        "text": "A glasshouse holds 250 tomato plants, each building about "
                "3.2 g of glucose a day. Calculate the total glucose built "
                "over 14 days, in kilograms.",
        "options": [
            {"text": "1.12 kg",
             "correct": False,
             "why": "That is ten times too small. 3.2 × 250 × 14 is 11 200 g, "
                    "and 11 200 g is 11.2 kg."},
            {"text": "112 kg",
             "correct": False,
             "why": "That is ten times too large — a power of ten has been "
                    "gained in the conversion from grams."},
            {"text": "11.2 kg, since 3.2 g × 250 × 14 is 11 200 g.",
             "correct": True},
            {"text": "0.8 kg",
             "correct": False,
             "why": "That is one day's total for the whole glasshouse. The "
                    "question asks for fourteen days."},
        ],
        "figure": None,
    },
]
