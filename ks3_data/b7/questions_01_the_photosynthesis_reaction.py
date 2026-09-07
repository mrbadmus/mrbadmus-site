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
                     "food and supply the energy it lives on.",
             "correct": False,
             "why": "Minerals supply no energy at all and are not food. A "
                    "plant makes its own food, which is what being a producer "
                    "means."},
            {"text": "In milligram quantities, to build particular molecules "
                     "— they are not a raw material for photosynthesis.",
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
            {"text": "They are the two ends of one reaction: carbon dioxide "
                     "is being built into glucose and oxygen is released as "
                     "waste.",
             "correct": True},
            {"text": "The oxygen is pushing the carbon dioxide out of the "
                     "jar, so the two gases always swap over.",
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
            {"text": "Two separate reactions happen to be running in the leaf "
                     "at the same time.",
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
            {"text": "It must have found minerals in the water, so it had a "
                     "supply after all.",
             "correct": False,
             "why": "Even if there were traces, that is not the point. "
                    "Minerals are not what glucose is built from, so the "
                    "starch does not depend on them."},
            {"text": "The starch is left over from the seed, and no new "
                     "starch is being made.",
             "correct": False,
             "why": "There is nothing to stop the seedling. Light, carbon "
                    "dioxide, water and chlorophyll are all present, so it is "
                    "building new glucose every day."},
            {"text": "Iodine gives a false blue-black on a plant that is "
                     "short of minerals.",
             "correct": False,
             "why": "Iodine answers one question and answers it honestly. "
                    "Blue-black means starch, and there is nothing false "
                    "about this result."},
            {"text": "Minerals are not a raw material for photosynthesis, so "
                     "the reaction runs without them.",
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
            {"text": "It makes no starch at all, because there is no carbon "
                     "dioxide in the jar to build glucose from.",
             "correct": True},
            {"text": "It grows faster than usual, because oxygen is the gas a "
                     "plant needs most of.",
             "correct": False,
             "why": "Oxygen is what photosynthesis releases, not what it "
                    "uses. Filling the jar with it has taken away the gas the "
                    "plant actually needs."},
            {"text": "It grows at its normal rate, because it can make its "
                     "own carbon dioxide from the water.",
             "correct": False,
             "why": "A plant cannot build carbon dioxide out of anything. It "
                    "has to arrive from the air, through the stomata."},
            {"text": "It grows more slowly, because oxygen in that quantity "
                     "is poisonous to a plant.",
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
            {"text": "From the water the plant was given, which has "
                     "evaporated inside the bag.",
             "correct": False,
             "why": "Evaporating water gives water vapour, which is why the "
                    "bag mists up. The extra oxygen is a product of the "
                    "reaction going on inside the leaves."},
            {"text": "From the air that was already in the bag, which has "
                     "warmed up and expanded.",
             "correct": False,
             "why": "Warming air does not create any more oxygen in it. What "
                    "is in the bag is oxygen the leaves have released."},
            {"text": "From the soil, which gives off oxygen when it has been "
                     "watered.",
             "correct": False,
             "why": "Soil does not supply the air with oxygen. The leaves do, "
                    "as a waste product of building glucose."},
            {"text": "The leaves released it as waste while building glucose, "
                     "and it diffused out through the stomata.",
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
                     "of it just as they do in your lungs.",
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
                     "when a plant would need to take in air.",
             "correct": False,
             "why": "It is the other way round. Photosynthesis needs light "
                    "and stops in the dark, so nothing about it is a "
                    "night-time process."},
            {"text": "Photosynthesis is a reaction that builds glucose rather "
                     "than a way of moving air, and plants respire as well, "
                     "day and night.",
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
            {"text": "Yes — if the rule holds, a crop short of carbon "
                     "dioxide ought to be making nothing at all.",
             "correct": False,
             "why": "Short is not absent. The rule is about taking a "
                    "condition away completely; the glasshouse only has less "
                    "of it than the crop could use."},
            {"text": "No — the rule is about removing a condition outright, "
                     "while the glasshouse merely has less of it than the "
                     "crop could use.",
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
                     "and takes what it needs from the soil.",
             "correct": False,
             "why": "A plant is the one kind of organism that makes its own "
                    "food. What it takes from the soil is water and minerals, "
                    "and neither is food."},
            {"text": "Making food is right; out of sunlight is wrong — the "
                     "material is carbon dioxide and water, and sunlight "
                     "supplies the energy.",
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
]
