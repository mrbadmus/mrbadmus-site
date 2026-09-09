"""B8 lesson 01 — Aerobic respiration: twelve questions (MRB-269).

These probe the three things this lesson exists to fix and the one thing it is
easiest to half-learn: that respiration is a chemical reaction in cells and not
the muscular job of breathing, that no mass is lost when fuel is respired, and
that energy is transferred rather than made and so is never a product. The
distractors are built from the lesson's two declared misconceptions — RESP-01
(respiration is just slow burning) and RESP-02 (the fat is converted into
energy, so the mass disappears) — together with five errors the page's own
ledger, exits panel and fact cards are drawn to catch: that the reaction
happens in the lungs or the blood where the oxygen is, that heat is a third
product listed beside carbon dioxide and water, that the two totals match only
by luck at one amount, that a cell can respire starch without digesting it
first, and that the carbon in exhaled carbon dioxide came from the oxygen
breathed in. The lesson carries no figures, so every question is figure=None.
"""

UNIT = "B8"
LESSON = "aerobic-respiration"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-01-e01",
        "band": "easier",
        "text": "Where in the body does aerobic respiration actually happen?",
        "options": [
            {"text": "In the lungs, where the oxygen you breathe in arrives.",
             "correct": False,
             "why": "The lungs deliver oxygen; they do not use it. Breathing "
                    "is the muscular job that supplies the reaction, and the "
                    "reaction itself is somewhere else entirely."},
            {"text": "In the mitochondria, inside almost every one of your "
                     "cells.",
             "correct": True},
            {"text": "In the blood, which is carrying the oxygen and the "
                     "glucose around.",
             "correct": False,
             "why": "The blood is the delivery service. It brings both "
                    "reactants to the cells and carries the carbon dioxide "
                    "away, but nothing is respired inside it."},
            {"text": "In the digestive system, where the glucose is released "
                     "from food.",
             "correct": False,
             "why": "Digestion supplies the glucose, it does not respire it. "
                    "The glucose is absorbed into the blood and used inside "
                    "the cells themselves."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e02",
        "band": "easier",
        "text": "What does the word aerobic tell you about this reaction?",
        "options": [
            {"text": "That it happens in the air around you rather than "
                     "inside your body.",
             "correct": False,
             "why": "Aerobic names a reactant, not a place. The reaction runs "
                    "inside cells — a fish does the same thing using oxygen "
                    "dissolved in water."},
            {"text": "That it happens in the lungs, which is where the air "
                     "actually is.",
             "correct": False,
             "why": "That is breathing again. Aerobic tells you what the "
                    "reaction uses, and the reaction runs in the cells, a long "
                    "way from the lungs."},
            {"text": "That the reaction gives out a gas which you then "
                     "breathe out.",
             "correct": False,
             "why": "It does give out carbon dioxide, but that is not what the "
                    "word means. Aerobic points at what goes in, not at what "
                    "comes out."},
            {"text": "That the reaction needs oxygen in order to happen at "
                     "all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e03",
        "band": "easier",
        "text": "A student writes: “I respire about fifteen times a "
                "minute.” What is wrong with that sentence?",
        "options": [
            {"text": "That is breathing. Respiration is a chemical reaction "
                     "inside cells, and it never stops.",
             "correct": True},
            {"text": "Nothing is wrong — respire is simply the scientific "
                     "word for breathe.",
             "correct": False,
             "why": "This is the commonest mix-up in the topic. Breathing is "
                    "the muscular job of moving air in and out; respiration is "
                    "the reaction that the air supplies."},
            {"text": "The number is too low — at rest you respire nearer "
                     "thirty times a minute.",
             "correct": False,
             "why": "The number is not the problem. Respiration has no rate "
                    "you can count in breaths, because a breath is not what it "
                    "is made of."},
            {"text": "It is only true during exercise, since respiration "
                     "starts when energy is needed.",
             "correct": False,
             "why": "There is no off switch. A cell that stops respiring for "
                    "more than a few minutes dies, so it is running while you "
                    "sleep as well."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e04",
        "band": "easier",
        "text": "Which pair names the two products of aerobic respiration — "
                "the two substances the reaction makes?",
        "options": [
            {"text": "Glucose and oxygen",
             "correct": False,
             "why": "Those are the two reactants, the substances that go in. "
                    "Turn the summary round and you have written "
                    "photosynthesis instead."},
            {"text": "Carbon dioxide and energy",
             "correct": False,
             "why": "Energy is not a substance and so cannot be a product. "
                    "Two products have mass, and the energy is transferred as "
                    "they form."},
            {"text": "Carbon dioxide and water",
             "correct": True},
            {"text": "Oxygen and water",
             "correct": False,
             "why": "Oxygen is used up rather than made. Water is right; the "
                    "other product is the carbon dioxide you breathe out "
                    "without noticing."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-01-s01",
        "band": "standard",
        "text": "A red blood cell spends its whole life carrying oxygen and "
                "cannot use a single molecule of it. Why not?",
        "options": [
            {"text": "Haemoglobin holds the oxygen so tightly that the cell "
                     "can never get any of it back.",
             "correct": False,
             "why": "It releases oxygen perfectly well — handing it over is "
                    "its job. What it lacks is anywhere to use the oxygen "
                    "itself."},
            {"text": "It has no need of energy, because the heart pushes it "
                     "around the body for it.",
             "correct": False,
             "why": "Every living cell needs energy transferred to it, moving "
                    "under its own power or not. This cell is unusual for what "
                    "it lacks, not for what it needs."},
            {"text": "It has no mitochondria, and mitochondria are where "
                     "aerobic respiration happens.",
             "correct": True},
            {"text": "It is already full of oxygen, so there is no room left "
                     "inside it for glucose.",
             "correct": False,
             "why": "Space is not the problem. Deliver glucose to it and "
                    "nothing changes, because it has nowhere to run the "
                    "reaction."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s02",
        "band": "standard",
        "text": "A hall fills with two hundred students and the temperature "
                "climbs, with the heating off. What explains it?",
        "options": [
            {"text": "Their cells are respiring, and the energy not used "
                     "usefully warms the room.",
             "correct": True},
            {"text": "Their bodies are burning the food they ate, and burning "
                     "always gives off heat.",
             "correct": False,
             "why": "Respiration is not burning. There is no flame and no "
                    "spark — the glucose comes apart in a long series of small "
                    "enzyme-controlled steps at 37 °C."},
            {"text": "Heat is respiration's third product, made alongside the "
                     "carbon dioxide and water.",
             "correct": False,
             "why": "There are two products and heat is not one of them. "
                    "Energy is transferred rather than made, which is why the "
                    "ledger prints it outside both totals."},
            {"text": "The carbon dioxide they breathe out traps the heat "
                     "inside the closed room.",
             "correct": False,
             "why": "The students are what warms the hall, not the gas. The "
                    "energy came from respiration in their cells before any of "
                    "it reached the air."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s03",
        "band": "standard",
        "text": "The ledger is set to a banana — 25 g of glucose. Total in "
                "reads 51.7 g and the energy panel reads 390 kJ. What does "
                "Total out read?",
        "options": [
            {"text": "Less than 51.7 g, because some of the mass was "
                     "transferred away as the 390 kJ.",
             "correct": False,
             "why": "Mass does not turn into energy in a chemical reaction. "
                    "The energy comes from a store in the glucose, not from "
                    "the atoms, and every atom is still there afterwards."},
            {"text": "More than 51.7 g, because the energy released has to be "
                     "added on to the products.",
             "correct": False,
             "why": "Energy has no mass, so it cannot be added to a total "
                    "measured in grams. That is exactly why it is printed in a "
                    "column of its own."},
            {"text": "It depends on the amount — the two totals only happen "
                     "to match for a banana.",
             "correct": False,
             "why": "They match at every amount, and not by luck. The figures "
                    "come straight from the balanced equation, so the two "
                    "totals are equal by construction."},
            {"text": "51.7 g, because every atom that went in comes out again "
                     "in the products.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s04",
        "band": "standard",
        "text": "A plate of pasta is mostly starch, not glucose. So why does "
                "the ledger count it as 90 g of glucose going in?",
        "options": [
            {"text": "Cells respire starch directly — glucose is only the "
                     "name it goes by in the blood.",
             "correct": False,
             "why": "Glucose in the blood is glucose. Starch is a far larger "
                    "molecule, and a cell cannot respire it until it has been "
                    "digested down."},
            {"text": "The starch is digested to glucose first, and glucose is "
                     "what reaches the cell.",
             "correct": True},
            {"text": "The mitochondria break the starch down into glucose and "
                     "then respire that.",
             "correct": False,
             "why": "The breakdown happens in the digestive system, not in the "
                    "cell. What travels in the blood and arrives at a "
                    "mitochondrion is already glucose."},
            {"text": "The starch is respired to carbon dioxide and water, and "
                     "the glucose is what is left.",
             "correct": False,
             "why": "Glucose is not a leftover, it is the fuel. Carbon dioxide "
                    "and water are the only two products, and nothing else is "
                    "sitting there at the end."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-01-h01",
        "band": "harder",
        "text": "You finish a run and breathe out. Trace the carbon in that "
                "carbon dioxide back to where it came from.",
        "options": [
            {"text": "From the oxygen you breathed in, which the lungs turn "
                     "into carbon dioxide.",
             "correct": False,
             "why": "There is no carbon in oxygen at all. The lungs make "
                    "nothing — they only get rid of what the cells have "
                    "already made."},
            {"text": "From the glucose in your food, joined to oxygen inside "
                     "your cells.",
             "correct": True},
            {"text": "From the carbon dioxide already in the air you breathed "
                     "in, on its way back out.",
             "correct": False,
             "why": "Air does carry a little carbon dioxide, but you breathe "
                    "out far more than you take in. The extra was made in your "
                    "cells from the glucose."},
            {"text": "It was made as the energy was released, so those atoms "
                     "did not exist before.",
             "correct": False,
             "why": "Atoms are never made or destroyed in a reaction. Every "
                    "carbon atom you exhale was in your food first, and in a "
                    "plant before that."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h02",
        "band": "harder",
        "text": "A gas heater warms a tent, and so do the four people asleep "
                "in it. Both are getting energy out of a fuel. What is the "
                "real difference between them?",
        "options": [
            {"text": "There is no real difference — respiration is burning, "
                     "just running more slowly inside a body.",
             "correct": False,
             "why": "This is the belief the lesson exists to correct. The "
                    "overall equation is the same and everything else differs: "
                    "no flame, no spark, and 37 °C rather than several hundred "
                    "degrees."},
            {"text": "The heater makes carbon dioxide and water, whereas the "
                     "people's cells make only carbon dioxide.",
             "correct": False,
             "why": "The people make both, and you can see the water — breathe "
                    "on a cold window. The products are identical; it is the "
                    "way they are released that differs."},
            {"text": "The heater needs a supply of oxygen and the people's "
                     "cells manage without one.",
             "correct": False,
             "why": "Aerobic means with oxygen. Their cells need it as much as "
                    "the flame does, which is why the people breathe harder if "
                    "the tent gets stuffy."},
            {"text": "The flame releases it all in one rush; the cells "
                     "release it in small enzyme-controlled steps.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h03",
        "band": "harder",
        "text": "A cell from the muscle a bird uses to fly is crammed with "
                "mitochondria. A cell from the skin of its foot has very few. "
                "What does that tell you?",
        "options": [
            {"text": "The flight muscle cell respires far faster — "
                     "contracting constantly needs energy.",
             "correct": True},
            {"text": "The flight muscle cell is simply larger, so it holds "
                     "more of everything a cell has.",
             "correct": False,
             "why": "It is the proportion that differs, not the size — in a "
                    "hard-working cell the mitochondria can take up a third of "
                    "the volume."},
            {"text": "The skin cell gets the energy it needs from somewhere "
                     "other than respiration.",
             "correct": False,
             "why": "There is nowhere else to get it. Every cell respires, "
                    "continuously; the skin cell just has less work to do and "
                    "so needs fewer mitochondria."},
            {"text": "The flight muscle cell sits nearer the blood, so more "
                     "oxygen reaches it.",
             "correct": False,
             "why": "Mitochondria are built where the work is, not where the "
                    "oxygen arrives. The demand comes first and the supply "
                    "follows it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h04",
        "band": "harder",
        "text": "A cell has plenty of glucose and plenty of oxygen. Why can "
                "it not respire the whole day's worth each morning and coast "
                "until evening?",
        "options": [
            {"text": "Because a mitochondrion can only handle a small amount "
                     "of glucose at a time.",
             "correct": False,
             "why": "This is not a capacity limit. Even if the reaction could "
                    "be run that fast, the energy transferred would not still "
                    "be waiting there in the afternoon."},
            {"text": "Because the energy released in the morning would be "
                     "stored as fat until it was wanted.",
             "correct": False,
             "why": "Fat is a store of fuel, not a store of energy respiration "
                    "has already transferred. Once that energy has been spent "
                    "on work it is gone."},
            {"text": "Because the energy is spent as it is transferred, never "
                     "stored up for later.",
             "correct": True},
            {"text": "Because releasing it all at once would be burning "
                     "rather than respiring, and the cell would cook.",
             "correct": False,
             "why": "That is true of a flame and it is not the reason here. "
                    "Even fast respiration is still small enzyme-controlled "
                    "steps; the reason is that the energy cannot be kept."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-01-e05",
        "band": "easier",
        "text": "Your food supplies the fuel that most cells respire. Which "
                "substance is that fuel?",
        "options": [
            {"text": "Oxygen, which arrives at the cell at the same moment.",
             "correct": False,
             "why": "Oxygen is a reactant, but it is not the fuel — there is "
                    "no store of energy in it. The store is in the glucose, "
                    "and the oxygen is what lets the cell get at it."},
            {"text": "Glucose, a sugar that reaches the cell in the blood.",
             "correct": True},
            {"text": "Water, which the blood carries to every cell in you.",
             "correct": False,
             "why": "Water comes out of respiration rather than going into "
                    "it. A cell given nothing but water has nothing to "
                    "release any energy from."},
            {"text": "Carbon dioxide, which the cell then has to get rid of.",
             "correct": False,
             "why": "Carbon dioxide is what is left once the glucose has been "
                    "broken down. It leaves the cell, and nothing can be "
                    "respired out of it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e06",
        "band": "easier",
        "text": "Which sentence describes what happens to energy during "
                "aerobic respiration?",
        "options": [
            {"text": "The cell makes it out of the glucose and the oxygen.",
             "correct": False,
             "why": "Energy is never made. It is already there, stored in the "
                    "glucose, and respiration transfers it to the cell that "
                    "needs it."},
            {"text": "It is created in the mitochondria and put away for "
                     "later.",
             "correct": False,
             "why": "Two errors in one sentence. Energy is not created, and "
                    "none of it is stored up — it is transferred and then "
                    "spent."},
            {"text": "It is destroyed as the carbon dioxide and water form.",
             "correct": False,
             "why": "Nothing destroys it either. The store in the glucose is "
                    "transferred to the cell, and what is not used usefully "
                    "ends up warming you."},
            {"text": "It is released from the glucose and transferred to the "
                     "cell.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e07",
        "band": "easier",
        "text": "Which gas does a cell use up when it respires aerobically?",
        "options": [
            {"text": "Oxygen", "correct": True},
            {"text": "Carbon dioxide", "correct": False,
             "why": "Carbon dioxide is made rather than used. You breathe it "
                    "out because the cell has finished with it."},
            {"text": "Nitrogen", "correct": False,
             "why": "Nitrogen is most of the air you breathe in and most of "
                    "the air you breathe out, because respiration does "
                    "nothing with it at all."},
            {"text": "Hydrogen", "correct": False,
             "why": "There is almost no hydrogen gas in air, and no cell "
                    "takes any in. The gas respiration uses is oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e08",
        "band": "easier",
        "text": "Are your cells respiring while you are fast asleep?",
        "options": [
            {"text": "No — it stops at rest and starts again when you move.",
             "correct": False,
             "why": "There is no off switch. A cell that stops respiring for "
                    "more than a few minutes dies, so you would not wake "
                    "up."},
            {"text": "Only in the heart and lungs, which work through the "
                     "night.",
             "correct": False,
             "why": "Those are working, and so is everything else — your "
                    "brain, your liver, your skin. Every living cell respires "
                    "all night."},
            {"text": "Yes — every living cell respires continuously, day and "
                     "night.",
             "correct": True},
            {"text": "Only until the food you ate during the day runs out.",
             "correct": False,
             "why": "Your cells never wait for a meal. Glucose is released "
                    "from stores between meals, and the reaction carries on "
                    "without a pause."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e09",
        "band": "easier",
        "text": "In the word summary glucose + oxygen gives carbon dioxide + "
                "water, what name is given to glucose and oxygen?",
        "options": [
            {"text": "The products, because they are what the reaction "
                     "produces.",
             "correct": False,
             "why": "Products are what comes out. Glucose and oxygen are what "
                    "goes in, and swapping the two names round turns the "
                    "reaction into photosynthesis."},
            {"text": "The reactants, because they are the substances that go "
                     "in.",
             "correct": True},
            {"text": "The catalysts, because they make the reaction go "
                     "faster.",
             "correct": False,
             "why": "A catalyst is not used up. Both of these are, which is "
                    "why a cell needs a continuous supply of each of them."},
            {"text": "The waste, because the cell is finished with them by "
                     "the end.",
             "correct": False,
             "why": "They are used, not discarded. What is left at the end is "
                    "carbon dioxide and water, and it is the carbon dioxide "
                    "that is treated as waste."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e10",
        "band": "easier",
        "text": "Breathe on a cold window and it mists over. Which of "
                "these best explains where that water comes from?",
        "options": [
            {"text": "From saliva in your mouth, sprayed out as you breathe.",
             "correct": False,
             "why": "It leaves as vapour, not as a spray. Water is carried "
                    "out of the lungs as a gas in every breath you take."},
            {"text": "From the glass, which sweats when something warm "
                     "touches it.",
             "correct": False,
             "why": "Glass releases no water of its own. What condenses on it "
                    "arrived as vapour in your breath."},
            {"text": "From carbon dioxide, which turns into water on the cold "
                     "glass.",
             "correct": False,
             "why": "One gas does not turn into another on a cold surface. "
                    "Carbon dioxide and water are two separate products, and "
                    "it is the water you can see."},
            {"text": "From water vapour in your breath, some of it made by "
                     "respiration.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e11",
        "band": "easier",
        "text": "At roughly what temperature does aerobic respiration happen "
                "inside your cells?",
        "options": [
            {"text": "At about 37 °C, which is your body temperature.",
             "correct": True},
            {"text": "At several hundred degrees, as a flame burns fuel.",
             "correct": False,
             "why": "That is burning, and a cell at that temperature is a "
                    "dead one. Respiration takes the same molecule apart in "
                    "small enzyme-controlled steps instead."},
            {"text": "At about 100 °C, the temperature at which water boils.",
             "correct": False,
             "why": "Nothing inside you is anywhere near boiling. The "
                    "reaction runs at body temperature, which is exactly why "
                    "it needs enzymes rather than heat."},
            {"text": "At whatever temperature the room around you happens to "
                     "be.",
             "correct": False,
             "why": "That would be true of a lizard, not of you. A mammal "
                    "holds itself at about 37 °C, and its cells respire at "
                    "that temperature whatever the room is doing."},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-01-s05",
        "band": "standard",
        "text": "When the masses going into aerobic respiration are added "
                "up and compared with the masses coming out, the energy "
                "transferred is listed on its own. Why is it in neither "
                "total?",
        "options": [
            {"text": "Because energy is not a substance and has no mass to "
                     "add.",
             "correct": True},
            {"text": "Because the energy is released later, once the products "
                     "have formed.",
             "correct": False,
             "why": "It is transferred as the products form, not afterwards. "
                    "It sits outside the totals because it has no mass, not "
                    "because of when it appears."},
            {"text": "Because only some of the energy leaves the body, so it "
                     "cannot be totalled.",
             "correct": False,
             "why": "How much of it leaves is not the issue. Energy is "
                    "measured in kilojoules and mass in grams, and the two "
                    "cannot be added together at all."},
            {"text": "Because the energy is already counted on the goes-in "
                     "side instead.",
             "correct": False,
             "why": "It is on neither side. The store of energy arrives inside "
                    "the glucose, but the energy itself is not something a "
                    "balance could weigh."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s06",
        "band": "standard",
        "text": "The masses in aerobic respiration are worked out first "
                "for the 4 g of glucose in a teaspoon of sugar, then for the "
                "300 g a person respires in a day. What happens to the mass "
                "going in and the mass coming out?",
        "options": [
            {"text": "The mass going in grows faster than the mass coming "
                     "out, because more energy is released.",
             "correct": False,
             "why": "More energy is released, but energy is in neither total. "
                    "Both columns scale with the glucose and stay equal to "
                    "each other."},
            {"text": "Both stay exactly as they were, because it is the same "
                     "reaction either way.",
             "correct": False,
             "why": "It is the same reaction, but there is seventy-five times "
                    "as much glucose going into it. Every figure in both "
                    "columns grows with it."},
            {"text": "Both totals grow, and they still match each other "
                     "exactly at 300 g.",
             "correct": True},
            {"text": "They match at 4 g but drift apart at 300 g, where the "
                     "error is larger.",
             "correct": False,
             "why": "They match at every amount. The figures come from the "
                    "balanced equation rather than from a measurement, so "
                    "there is no error to grow."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s07",
        "band": "standard",
        "text": "A student writes the summary as glucose + oxygen gives "
                "carbon dioxide + water + energy. What is wrong with writing "
                "it that way?",
        "options": [
            {"text": "Nothing is wrong — energy is the third product of the "
                     "reaction.",
             "correct": False,
             "why": "There are two products and energy is not one of them. "
                    "Only something with mass can be a product, and energy "
                    "has none."},
            {"text": "Energy is not a substance, so it cannot be listed as a "
                     "product.",
             "correct": True},
            {"text": "Energy belongs on the left, because it is put into the "
                     "reaction.",
             "correct": False,
             "why": "It is not put in either. The store of energy arrives "
                    "inside the glucose, which is already on the left, and "
                    "respiration transfers it out."},
            {"text": "Energy should be written as heat, because that is how "
                     "it leaves.",
             "correct": False,
             "why": "Some of it does end up warming you, but that is not the "
                    "fault here. Neither word belongs on either side of a "
                    "word summary."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s08",
        "band": "standard",
        "text": "A cell has plenty of glucose, but its oxygen supply is cut "
                "off completely. What happens to its aerobic respiration?",
        "options": [
            {"text": "It carries on at the same rate, using the glucose on "
                     "its own.",
             "correct": False,
             "why": "Glucose alone releases nothing aerobically. Both "
                    "reactants have to be present, which is why a few minutes "
                    "without oxygen does permanent damage."},
            {"text": "It carries on more slowly, on the oxygen the cell had "
                     "stored.",
             "correct": False,
             "why": "There is no store of oxygen inside a cell to fall back "
                    "on. What the blood is delivering at that moment is all "
                    "there is."},
            {"text": "It speeds up, because a cell short of energy respires "
                     "faster to make it up.",
             "correct": False,
             "why": "Needing energy does not supply oxygen. Demand cannot "
                    "drive a reaction one of whose reactants has stopped "
                    "arriving."},
            {"text": "It stops, because aerobic respiration needs both "
                     "reactants.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s09",
        "band": "standard",
        "text": "A muscle cell working hard needs more glucose and more "
                "oxygen. Which parts of the body supply them?",
        "options": [
            {"text": "The lungs supply both, since the air breathed in "
                     "carries oxygen and dissolved glucose.",
             "correct": False,
             "why": "There is no glucose in air. It comes from food, digested "
                    "down to glucose and absorbed into the blood."},
            {"text": "The blood makes both of them and then delivers them to "
                     "the cell.",
             "correct": False,
             "why": "Blood makes neither. It is the delivery service, "
                    "carrying what the digestive system and the lungs have "
                    "supplied."},
            {"text": "Glucose comes from digestion, oxygen from the lungs, "
                     "blood carries both.",
             "correct": True},
            {"text": "The mitochondria make the glucose and the lungs supply "
                     "the oxygen for it.",
             "correct": False,
             "why": "Mitochondria use glucose; they never make it. Building "
                    "glucose is what a plant does in photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s10",
        "band": "standard",
        "text": "Two people are in one room: one is asleep, the other is "
                "sitting reading. What is true of respiration in the two of "
                "them?",
        "options": [
            {"text": "It has stopped in the sleeper and is running in the "
                     "reader.",
             "correct": False,
             "why": "It has not stopped in either. The sleeper's rate is "
                    "lower, not zero — a cell that stops respiring is a dead "
                    "one."},
            {"text": "It is running in both, more slowly in the sleeper than "
                     "in the reader.",
             "correct": True},
            {"text": "It is running at exactly the same rate, since both of "
                     "them are resting.",
             "correct": False,
             "why": "Both are resting, but reading is not sleeping. Awake "
                    "muscles, a faster heart and a busier brain all cost "
                    "more, so the rate is higher."},
            {"text": "It is running in the sleeper's brain only, and "
                     "everywhere in the reader.",
             "correct": False,
             "why": "Every living cell in both of them is respiring. What "
                    "differs is the rate, not which cells are taking part."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s11",
        "band": "standard",
        "text": "A student who has done no exercise all day says they have "
                "hardly respired at all. What is the best reply?",
        "options": [
            {"text": "Every cell has respired all day — about 300 g of "
                     "carbohydrate, run or not.",
             "correct": True},
            {"text": "They are right: a body that has not exercised has "
                     "barely respired.",
             "correct": False,
             "why": "Exercise raises the rate, but it is not what switches "
                    "respiration on. A day of sitting still still costs "
                    "hundreds of grams of carbohydrate."},
            {"text": "They are right about the muscles, but the brain has "
                     "been respiring instead.",
             "correct": False,
             "why": "The brain certainly has, and so have the muscles. "
                    "Resting muscle respires continuously; it simply does "
                    "less work."},
            {"text": "They are right, because a cell respires only when it "
                     "runs short of energy.",
             "correct": False,
             "why": "Respiration is not a response to running short. It runs "
                    "continuously in every living cell, paying for repairs, "
                    "transport and keeping you warm."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-01-h05",
        "band": "harder",
        "text": "Respiring 180 g of glucose uses 192 g of oxygen. What mass "
                "of oxygen is needed to respire 45 g of glucose?",
        "options": [
            {"text": "45 g", "correct": False,
             "why": "That assumes the two masses must be equal. The ratio is "
                    "192 g of oxygen for every 180 g of glucose, so the "
                    "oxygen mass is a little larger, not the same."},
            {"text": "42.2 g", "correct": False,
             "why": "That is 45 × 180 ÷ 192 — the ratio used upside down. "
                    "Multiply by 192/180, because more oxygen is needed than "
                    "glucose, not less."},
            {"text": "48 g", "correct": True},
            {"text": "192 g", "correct": False,
             "why": "That is the oxygen for the full 180 g of glucose. Only a "
                    "quarter of that is being respired here, so the oxygen "
                    "scales down with it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h06",
        "band": "harder",
        "text": "Respiring glucose transfers about 15.6 kJ of energy per gram "
                "of glucose. How much is transferred by respiring the 4 g of "
                "glucose in a teaspoon of sugar?",
        "options": [
            {"text": "3.9 kJ", "correct": False,
             "why": "That is 15.6 ÷ 4 — divided where it should be "
                    "multiplied. Each gram transfers 15.6 kJ, so four grams "
                    "transfer four times as much."},
            {"text": "15.6 kJ", "correct": False,
             "why": "That is the energy from one gram, not from four. The "
                    "figure has to be multiplied by the mass of glucose "
                    "actually respired."},
            {"text": "19.6 kJ", "correct": False,
             "why": "That is 15.6 + 4, adding a mass in grams to an energy in "
                    "kilojoules. The two cannot be added; 15.6 kJ per gram "
                    "has to be multiplied by 4 g."},
            {"text": "62.4 kJ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h07",
        "band": "harder",
        "text": "In one worked example, 90 g of glucose and 96 g of oxygen "
                "go in, and 132 g of carbon dioxide comes out. What mass of "
                "water comes out with it?",
        "options": [
            {"text": "54 g", "correct": True},
            {"text": "42 g", "correct": False,
             "why": "That is 132 − 90, which counts only one of the two "
                    "reactants. Both go in: 90 + 96 = 186 g, and 186 − 132 "
                    "leaves 54 g as water."},
            {"text": "96 g", "correct": False,
             "why": "The oxygen going in is not the water coming out; the "
                    "atoms are rearranged between the two. Add both "
                    "reactants and subtract the carbon dioxide."},
            {"text": "222 g", "correct": False,
             "why": "Adding the carbon dioxide gives more coming out than "
                    "went in, and no reaction can do that. The two totals are "
                    "equal, so the water is 186 − 132 = 54 g."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h08",
        "band": "harder",
        "text": "A hibernating dormouse cools to about 5 °C and its heart "
                "slows to a few beats a minute. Why has respiration in its "
                "cells not stopped altogether?",
        "options": [
            {"text": "It has stopped, and that is what hibernation is — "
                     "switched off until spring.",
             "correct": False,
             "why": "A cell that stops respiring dies within minutes, so an "
                    "animal that switched it off would never wake up. What "
                    "falls in hibernation is the rate."},
            {"text": "Because it is still breathing, and breathing is what "
                     "keeps respiration going.",
             "correct": False,
             "why": "Breathing supplies the oxygen; it is not the reaction. "
                    "Respiration continues because the cells would die "
                    "without it, not because the chest is still moving."},
            {"text": "Because a cell that stopped respiring would die — the "
                     "rate falls, never to zero.",
             "correct": True},
            {"text": "Because respiration warms the animal, so it must run "
                     "flat out to hold it at 5 °C.",
             "correct": False,
             "why": "Respiration does warm a mammal, and hibernation lets the "
                    "temperature fall precisely to cut that bill. The rate "
                    "drops a long way; it simply cannot reach zero."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h09",
        "band": "harder",
        "text": "The air inside a sealed spacecraft has to be treated "
                "continuously: one gas is added and another taken out. Using "
                "aerobic respiration, which is which?",
        "options": [
            {"text": "Carbon dioxide is added, and oxygen is taken out.",
             "correct": False,
             "why": "That is respiration backwards. Oxygen is what the crew's "
                    "cells use up, and carbon dioxide is what those cells "
                    "produce."},
            {"text": "Oxygen is added, and water vapour taken out so the "
                     "carbon dioxide can be re-breathed.",
             "correct": False,
             "why": "Water vapour does build up and is removed as well, but "
                    "carbon dioxide cannot be re-used. Nothing respires it, "
                    "and it becomes dangerous as it accumulates."},
            {"text": "Nitrogen is added, and oxygen taken out, since nitrogen "
                     "is most of the air.",
             "correct": False,
             "why": "Nitrogen is most of the air and takes no part in "
                    "respiration, so none of it is used up. The gas the crew "
                    "consume is oxygen."},
            {"text": "Oxygen is added, and carbon dioxide is taken out.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h10",
        "band": "harder",
        "text": "A student finds that the total mass going into aerobic "
                "respiration equals the total mass coming out, and says the "
                "reaction has therefore achieved nothing. What is wrong?",
        "options": [
            {"text": "The totals only match on paper — a real body loses a "
                     "little mass each time.",
             "correct": False,
             "why": "No mass is lost in a real body either. Every atom that "
                    "goes in comes out, and that is measured, not assumed."},
            {"text": "The atoms are rearranged, and the energy stored in the "
                     "glucose is transferred.",
             "correct": True},
            {"text": "The totals match, so the value must lie in the "
                     "breathing rather than the reaction.",
             "correct": False,
             "why": "Breathing supplies the reaction and achieves nothing on "
                    "its own. What the reaction achieves is energy "
                    "transferred to the cell."},
            {"text": "The totals would not match if the reaction were doing "
                     "anything, so one is wrong.",
             "correct": False,
             "why": "Both are right, and matching totals are what every "
                    "chemical reaction gives. What was achieved is measured "
                    "in kilojoules, not in grams."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h11",
        "band": "harder",
        "text": "Carbon monoxide from a faulty heater sticks to haemoglobin "
                "so that it can no longer carry oxygen. The person goes on "
                "breathing normally, yet their cells begin to fail. Why?",
        "options": [
            {"text": "Because their cells respire the carbon monoxide "
                     "instead, and get no energy from it.",
             "correct": False,
             "why": "Nothing respires carbon monoxide. The harm is done to "
                    "the delivery of oxygen, not to what is being used as "
                    "fuel."},
            {"text": "Because breathing is not the reaction — oxygen has to "
                     "reach the cells to be used.",
             "correct": True},
            {"text": "Because the lungs stop taking oxygen out of the air "
                     "once carbon monoxide is present.",
             "correct": False,
             "why": "The lungs go on working and oxygen still crosses into "
                    "the blood. The problem is that there is nothing left to "
                    "carry it to the cells."},
            {"text": "Because the cells have used up the oxygen they had "
                     "stored and cannot replace it.",
             "correct": False,
             "why": "There was never any stored. Cells depend on a continuous "
                    "delivery, which is why an interruption is measured in "
                    "minutes."},
        ],
        "figure": None,
    },
    # ── easier · MRB-338 expansion ──────────────────────────
    {
        "id": "b8-01-e12",
        "band": "easier",
        "text": "Which part of the body takes the oxygen used in respiration "
                "out of the air and puts it into the blood?",
        "options": [
            {"text": "The lungs, where oxygen crosses into the blood.",
             "correct": True},
            {"text": "The heart, which pumps that blood around the body.",
             "correct": False,
             "why": "The heart moves blood that is already carrying its oxygen. "
                    "It loads none of it on."},
            {"text": "The stomach, which takes in what you swallow.",
             "correct": False,
             "why": "The stomach handles food, not air. The oxygen for "
                    "respiration never goes near it."},
            {"text": "The mitochondria, where the oxygen is used up.",
             "correct": False,
             "why": "That is where the oxygen is spent, not where it is "
                    "collected. It has to reach the cell first."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e13",
        "band": "easier",
        "text": "Most of the glucose your cells respire started out as food "
                "on a plate. What has to happen to that food first?",
        "options": [
            {"text": "It has to be breathed in through the lungs, arriving "
                     "with the oxygen.",
             "correct": False,
             "why": "Food is not a gas and does not enter through the lungs. It "
                    "is absorbed into the blood from the gut."},
            {"text": "It has to be digested to glucose, which the blood then "
                     "carries to the cells.",
             "correct": True},
            {"text": "It has to be burnt in the stomach, which is where its "
                     "energy is released.",
             "correct": False,
             "why": "Nothing is burnt anywhere in a body. The stomach digests "
                    "food; the energy is released in the cells."},
            {"text": "It has to be turned into oxygen, so that the cell has "
                     "both of its reactants ready.",
             "correct": False,
             "why": "Food never becomes oxygen. The oxygen comes from the air; "
                    "the food supplies the glucose."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e14",
        "band": "easier",
        "text": "A cell has just made carbon dioxide by respiring. What "
                "happens to that carbon dioxide next?",
        "options": [
            {"text": "It is stored inside the mitochondria, ready for the "
                     "cell to make use of later.",
             "correct": False,
             "why": "Nothing is stored. Carbon dioxide is waste, and a cell "
                    "that kept it would poison itself."},
            {"text": "It is broken down by the liver and turned back into "
                     "glucose.",
             "correct": False,
             "why": "The body cannot rebuild glucose from it. Plants can do "
                    "that using light; you cannot."},
            {"text": "It dissolves into the blood, is carried to the lungs "
                     "and is breathed out.",
             "correct": True},
            {"text": "It stays in the cell and is used again by the very next "
                     "reaction.",
             "correct": False,
             "why": "Respiration cannot use its own waste. The carbon dioxide "
                    "leaves the cell and then leaves the body."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e15",
        "band": "easier",
        "text": "Aerobic respiration is described as a chemical reaction. "
                "What is the best reason for calling it one?",
        "options": [
            {"text": "It gives out energy, and any change that gives out "
                     "energy is a chemical one.",
             "correct": False,
             "why": "Changes that are not chemical give out energy too — water "
                    "freezing is one. New substances are the test."},
            {"text": "It happens inside a living cell, and everything in a "
                     "cell is chemical.",
             "correct": False,
             "why": "Where a change happens does not decide what kind of change "
                    "it is. What matters is whether new substances are made."},
            {"text": "It uses a gas from the air, and a change using a gas is "
                     "a chemical one.",
             "correct": False,
             "why": "A gas can take part in changes that are not chemical, such "
                    "as dissolving in water."},
            {"text": "New substances are made: glucose and oxygen become "
                     "carbon dioxide and water.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e16",
        "band": "easier",
        "text": "A potted plant is left in a dark room all night. Is aerobic "
                "respiration happening inside it?",
        "options": [
            {"text": "Yes — every living plant cell respires, in the dark "
                     "exactly as in the light.",
             "correct": True},
            {"text": "No — a plant respires only once it has made some "
                     "glucose in the light.",
             "correct": False,
             "why": "The glucose made during the day is stored and respired "
                    "through the night. Respiration never stops."},
            {"text": "No — plants photosynthesise instead of respiring, so "
                     "they never have need of it.",
             "correct": False,
             "why": "Plants do both. Photosynthesis stores the glucose; "
                    "respiration releases the energy from it."},
            {"text": "Only in the leaves, since the roots and stem are not "
                     "alive at night.",
             "correct": False,
             "why": "Root and stem cells are alive day and night, and every one "
                    "of them respires."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e17",
        "band": "easier",
        "text": "The energy transferred when a gram of glucose is respired "
                "would be measured in which unit?",
        "options": [
            {"text": "Grams (g).",
             "correct": False,
             "why": "Grams measure mass. The mass of glucose respired and the "
                    "energy transferred are two different quantities."},
            {"text": "Degrees Celsius (°C).",
             "correct": False,
             "why": "Degrees Celsius measure temperature. A temperature rise is "
                    "a consequence of the transfer, not a measure of it."},
            {"text": "Kilojoules (kJ).",
             "correct": True},
            {"text": "Centimetres cubed (cm³).",
             "correct": False,
             "why": "Centimetres cubed measure the volume of a gas, and it is "
                    "the energy that is being asked for here."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e18",
        "band": "easier",
        "text": "Respiration is often described as releasing energy. Where "
                "was that energy before the reaction happened?",
        "options": [
            {"text": "In the oxygen, which is why a cell cannot manage "
                     "without a supply of it.",
             "correct": False,
             "why": "Oxygen holds no store of energy for the cell. It is the "
                    "substance the glucose reacts with."},
            {"text": "Stored in the glucose, which is the fuel the reaction "
                     "takes apart.",
             "correct": True},
            {"text": "Inside the mitochondria, which keep a supply ready for "
                     "the cell to spend.",
             "correct": False,
             "why": "Mitochondria are where the reaction happens. They are not "
                    "a store of energy waiting to be used."},
            {"text": "Nowhere — it is created as the carbon dioxide and the "
                     "water form.",
             "correct": False,
             "why": "Energy cannot be created. Respiration transfers it out of "
                    "a store that was already there."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e19",
        "band": "easier",
        "text": "What is the name of the reaction that uses glucose and "
                "oxygen inside cells to release energy?",
        "options": [
            {"text": "Photosynthesis, which happens in the light inside "
                     "plants.",
             "correct": False,
             "why": "Photosynthesis runs the other way: it builds glucose and "
                    "releases oxygen, and it needs light."},
            {"text": "Breathing, which happens in the lungs.",
             "correct": False,
             "why": "Breathing is the muscular job of moving air. It supplies "
                    "the reaction and is not the reaction."},
            {"text": "Digestion, which happens in the gut.",
             "correct": False,
             "why": "Digestion breaks food into small molecules such as "
                    "glucose. Releasing the energy comes afterwards."},
            {"text": "Aerobic respiration.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e20",
        "band": "easier",
        "text": "Inside a cell, glucose is taken apart in a long series of "
                "small steps. What controls those steps?",
        "options": [
            {"text": "Enzymes.",
             "correct": True},
            {"text": "A flame inside the cell.",
             "correct": False,
             "why": "There is no flame and no spark anywhere in a cell, and the "
                    "reaction needs neither of them."},
            {"text": "The warmth of the body.",
             "correct": False,
             "why": "Body temperature on its own is far too low to drive the "
                    "reaction. Enzymes are what make it possible at 37 °C."},
            {"text": "The blood supply.",
             "correct": False,
             "why": "Blood delivers the reactants and removes the waste. The "
                    "steps themselves are controlled inside the cell."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e21",
        "band": "easier",
        "text": "Which liquid is used in the laboratory to show that a gas is "
                "carbon dioxide?",
        "options": [
            {"text": "Iodine solution, which turns blue-black.",
             "correct": False,
             "why": "Iodine solution is the test for starch, and it is used on "
                    "a solid rather than on a gas."},
            {"text": "Limewater, which turns milky.",
             "correct": True},
            {"text": "Benedict's solution, which turns brick red.",
             "correct": False,
             "why": "Benedict's solution tests a liquid for sugar. It says "
                    "nothing about which gas is present."},
            {"text": "Blue litmus, which is bleached white.",
             "correct": False,
             "why": "Bleaching damp litmus is the test for chlorine. Litmus "
                    "otherwise only shows acid or alkali."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e22",
        "band": "easier",
        "text": "Which of these cells would you expect to hold the most "
                "mitochondria?",
        "options": [
            {"text": "A cell in a hair, which does very little.",
             "correct": False,
             "why": "A hair cell has a small energy bill, so it needs few "
                    "mitochondria to meet it."},
            {"text": "A fat storage cell, mostly full of a droplet.",
             "correct": False,
             "why": "Holding a store of fat is not hard work, and the cell "
                    "doing it needs little energy."},
            {"text": "A heart muscle cell, contracting every second.",
             "correct": True},
            {"text": "A skin surface cell, worn away and replaced.",
             "correct": False,
             "why": "Cells at the very surface of the skin are not active, and "
                    "many of them are already dead."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e23",
        "band": "easier",
        "text": "Roughly what mass of carbohydrate does a person of your age "
                "respire in a day?",
        "options": [
            {"text": "About 3 g",
             "correct": False,
             "why": "3 g is smaller than a teaspoon of sugar. A whole day's "
                    "worth is around a hundred times that."},
            {"text": "About 30 g",
             "correct": False,
             "why": "30 g is roughly a banana's worth, which is a small part of "
                    "a day rather than all of it."},
            {"text": "About 3 kg",
             "correct": False,
             "why": "3 kg of carbohydrate is about ten times what a person "
                    "eats, let alone respires, in a day."},
            {"text": "About 300 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e24",
        "band": "easier",
        "text": "A fish takes in oxygen dissolved in water rather than oxygen "
                "from the air. What reaction runs inside its cells?",
        "options": [
            {"text": "Aerobic respiration, the same reaction as in yours.",
             "correct": True},
            {"text": "A different reaction, because the oxygen came out of "
                     "water rather than air.",
             "correct": False,
             "why": "Where the oxygen came from makes no difference at all. An "
                    "oxygen molecule is the same molecule either way."},
            {"text": "Photosynthesis, because the fish is surrounded by water "
                     "all of the time.",
             "correct": False,
             "why": "Photosynthesis needs light and chlorophyll and builds "
                    "glucose. A fish does none of that."},
            {"text": "No reaction at all, because oxygen that is dissolved in "
                     "water cannot be used by a cell.",
             "correct": False,
             "why": "Dissolved oxygen is used exactly as oxygen from air is, "
                    "once it has crossed the gills into the blood."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e25",
        "band": "easier",
        "text": "Which statement is true of respiration but not of burning a "
                "fuel in air?",
        "options": [
            {"text": "It joins the fuel to oxygen and gives out carbon "
                     "dioxide as it goes.",
             "correct": False,
             "why": "Burning does that too. Both have the same reactants and "
                    "the same products."},
            {"text": "It happens at about body temperature, in many small "
                     "controlled steps.",
             "correct": True},
            {"text": "It releases energy that was stored in the fuel long "
                     "before the reaction.",
             "correct": False,
             "why": "Burning releases the same store. The difference is the "
                    "rate and the control, not where the energy came from."},
            {"text": "It produces water as well as carbon dioxide whenever it "
                     "takes place.",
             "correct": False,
             "why": "Burning a fuel that contains hydrogen makes water too, so "
                    "that is not what separates them."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e26",
        "band": "easier",
        "text": "Respiration makes water inside your cells. Besides leaving "
                "as vapour in your breath, how else does that water leave?",
        "options": [
            {"text": "In glucose, rebuilt by the liver.",
             "correct": False,
             "why": "The body has no way of rebuilding glucose from the "
                    "products of respiration."},
            {"text": "Nowhere — it stays inside the cells.",
             "correct": False,
             "why": "Water is not stockpiled in cells. What the body takes in "
                    "and what it loses are kept in balance."},
            {"text": "In urine and in sweat.",
             "correct": True},
            {"text": "In the carbon dioxide breathed out.",
             "correct": False,
             "why": "Water and carbon dioxide are different substances, and one "
                    "never turns into the other."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e27",
        "band": "easier",
        "text": "In the word summary for aerobic respiration, what does the "
                "arrow mean?",
        "options": [
            {"text": "That the two sides balance, so they can be swapped over "
                     "whenever you like.",
             "correct": False,
             "why": "The arrow points one way. Read backwards the summary "
                    "describes photosynthesis, a different reaction."},
            {"text": "That the substances on the left are heated up by the "
                     "ones on the right.",
             "correct": False,
             "why": "Nothing on either side heats anything. The arrow shows a "
                    "change, not a heating."},
            {"text": "That energy has to be put in first to make the reaction "
                     "start happening.",
             "correct": False,
             "why": "No flame or spark is needed to start it. The arrow means "
                    "one set of substances becomes another."},
            {"text": "That the substances on the left are changed into the "
                     "ones on the right.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e28",
        "band": "easier",
        "text": "Your body stays at about 37 °C even on a cold day. Which "
                "process supplies that warmth?",
        "options": [
            {"text": "Respiration in your cells, which warms you as it "
                     "transfers energy.",
             "correct": True},
            {"text": "The clothes you put on, which make heat to keep the "
                     "body warm.",
             "correct": False,
             "why": "Clothing traps warmth that is already there. It makes none "
                    "of its own."},
            {"text": "Breathing in warm air, which raises the temperature of "
                     "the blood a little.",
             "correct": False,
             "why": "On a cold day the air breathed in is colder than you are. "
                    "The warmth is made inside."},
            {"text": "Digestion in the stomach, which is where the food is "
                     "warmed up.",
             "correct": False,
             "why": "Digestion breaks food into smaller molecules. The energy "
                    "in them is released later, in the cells."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e29",
        "band": "easier",
        "text": "Air breathed out holds less oxygen and more carbon dioxide "
                "than air breathed in. Which process explains that change?",
        "options": [
            {"text": "The air is warmed in the lungs, and warm air holds less "
                     "oxygen than cold air.",
             "correct": False,
             "why": "Warming a sample of air does not change what it is made "
                    "of. Cells used the oxygen."},
            {"text": "Aerobic respiration in cells, which uses oxygen and "
                     "makes carbon dioxide.",
             "correct": True},
            {"text": "The lungs turn some of the oxygen into carbon dioxide "
                     "as the air passes through.",
             "correct": False,
             "why": "The lungs change nothing chemically. They are a swap "
                    "point; the reaction is in the cells."},
            {"text": "Some of the oxygen leaks out through the skin while you "
                     "are breathing in.",
             "correct": False,
             "why": "No measurable oxygen leaves through the skin. The missing "
                    "oxygen was used by cells."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e30",
        "band": "easier",
        "text": "One gram of glucose gives about 15.6 kJ when it is respired. "
                "How much would 2 g give?",
        "options": [
            {"text": "7.8 kJ",
             "correct": False,
             "why": "That is 15.6 divided by 2. Two grams release more energy "
                    "than one gram, not less, so multiply."},
            {"text": "15.6 kJ",
             "correct": False,
             "why": "That is the figure for one gram. It still has to be "
                    "multiplied by the mass respired."},
            {"text": "31.2 kJ",
             "correct": True},
            {"text": "156 kJ",
             "correct": False,
             "why": "That is 15.6 multiplied by 10. The mass here is 2 g, so a "
                    "power of ten has slipped in."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e31",
        "band": "easier",
        "text": "Every gram of glucose respired produces 0.6 g of water. What "
                "mass of water comes from 10 g of glucose?",
        "options": [
            {"text": "0.06 g",
             "correct": False,
             "why": "That is 0.6 divided by 10. Ten grams of glucose make more "
                    "water than one gram, so multiply."},
            {"text": "0.6 g",
             "correct": False,
             "why": "That is the water from a single gram. It has to be "
                    "multiplied by the 10 g respired."},
            {"text": "16 g",
             "correct": False,
             "why": "That is 10 added to 0.6 and rounded. The figures are a "
                    "rate and a mass, so they multiply."},
            {"text": "6 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-e32",
        "band": "easier",
        "text": "The oxygen you breathe in is used up by respiration. Which "
                "substances do its atoms end up in?",
        "options": [
            {"text": "In the carbon dioxide and the water.",
             "correct": True},
            {"text": "In glucose, which is rebuilt from them.",
             "correct": False,
             "why": "Respiration takes glucose apart rather than building it. "
                    "Building glucose is what photosynthesis does."},
            {"text": "In nothing — the atoms are destroyed.",
             "correct": False,
             "why": "Atoms are never destroyed. Every oxygen atom that reacts "
                    "ends up in one of the two products."},
            {"text": "It leaves again as oxygen gas.",
             "correct": False,
             "why": "Some breathed-in oxygen does leave unused, but the oxygen "
                    "that is respired ends up in the products."},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ────────────────────────
    {
        "id": "b8-01-s12",
        "band": "standard",
        "text": "A gardener says plants respire only at night, because in the "
                "daytime they photosynthesise instead. Why is that wrong?",
        "options": [
            {"text": "Plants never respire at all, because photosynthesis "
                     "does the same job for them.",
             "correct": False,
             "why": "Every living plant cell respires. Without it the plant "
                    "could not use the energy stored in its own glucose."},
            {"text": "Plant cells respire all the time, and in daylight they "
                     "photosynthesise as well.",
             "correct": True},
            {"text": "Plants respire only in the day, when there is light "
                     "available to drive the reaction.",
             "correct": False,
             "why": "Respiration needs no light. It runs through the night on "
                    "the glucose stored during the day."},
            {"text": "Plants respire only in the roots, because that is the "
                     "part no light ever reaches.",
             "correct": False,
             "why": "Leaf cells respire too, in full sunlight, at the same time "
                    "as they are photosynthesising."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s13",
        "band": "standard",
        "text": "A poison damages the mitochondria in a person's cells, while "
                "glucose and oxygen still reach every cell as normal. Predict "
                "what happens.",
        "options": [
            {"text": "Nothing changes, because the glucose and the oxygen are "
                     "all that the reaction really needs.",
             "correct": False,
             "why": "The reactants alone are not enough. With the mitochondria "
                    "damaged there is nowhere for the reaction to happen."},
            {"text": "The cells store the glucose and the oxygen until the "
                     "damage has been repaired.",
             "correct": False,
             "why": "Neither can be stockpiled, and the cell's energy bill "
                    "falls due every second."},
            {"text": "Aerobic respiration slows or stops, and the cells run "
                     "short of energy.",
             "correct": True},
            {"text": "The cells respire faster, making up for the "
                     "mitochondria that have been lost.",
             "correct": False,
             "why": "Fewer working mitochondria means less respiration, not "
                    "more. Damage cannot raise the rate."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s14",
        "band": "standard",
        "text": "Two boiling tubes of hydrogencarbonate indicator are wrapped "
                "in foil. One holds five woodlice on a gauze and the other "
                "holds nothing. After an hour the tube with the woodlice has "
                "turned yellow and the empty tube is unchanged. What does "
                "that show?",
        "options": [
            {"text": "The woodlice used up the oxygen, and a fall in oxygen "
                     "is what turns the indicator yellow.",
             "correct": False,
             "why": "The indicator responds to carbon dioxide dissolving and "
                    "making the solution acidic, not to oxygen."},
            {"text": "The foil warmed that tube, and warmth is what turns the "
                     "indicator yellow.",
             "correct": False,
             "why": "Both tubes were wrapped the same way and the empty one did "
                    "not change, which is what it is there for."},
            {"text": "The woodlice photosynthesised, because the foil kept "
                     "the light off them.",
             "correct": False,
             "why": "Animals do not photosynthesise, and photosynthesis needs "
                    "light rather than darkness."},
            {"text": "The woodlice released carbon dioxide, so they were "
                     "respiring.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s15",
        "band": "standard",
        "text": "Pondweed is sealed in a tube of hydrogencarbonate indicator "
                "and left in a dark cupboard. By morning the indicator has "
                "turned yellow. What does that tell you?",
        "options": [
            {"text": "Plant cells respire, releasing carbon dioxide even with "
                     "no light at all.",
             "correct": True},
            {"text": "The pondweed photosynthesised in the dark, which is "
                     "what released the gas.",
             "correct": False,
             "why": "Photosynthesis needs light, and it takes carbon dioxide in "
                    "rather than giving it out."},
            {"text": "Pondweed is not really a plant, so it respires the way "
                     "an animal does.",
             "correct": False,
             "why": "Pondweed is a plant, and every plant respires — as does "
                    "every animal."},
            {"text": "The water gave off carbon dioxide of its own once the "
                     "light was taken away.",
             "correct": False,
             "why": "A dark tube of indicator and water with no pondweed in it "
                    "stays orange, which is what a control shows."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s16",
        "band": "standard",
        "text": "A tank of cold-water fish is fitted with a pump that bubbles "
                "air through the water day and night. Explain why the pump is "
                "needed.",
        "options": [
            {"text": "The bubbles keep the water moving, so the fish do not "
                     "have to swim so hard.",
             "correct": False,
             "why": "Fish swim perfectly well in still water. What they cannot "
                    "do is respire without oxygen."},
            {"text": "The fish respire continuously, so the oxygen dissolved "
                     "in the water has to be replaced.",
             "correct": True},
            {"text": "The bubbles supply the fish with the carbon dioxide "
                     "that their cells need for respiring.",
             "correct": False,
             "why": "Carbon dioxide is a waste product of respiration, not "
                    "something a cell needs delivering."},
            {"text": "The air warms the water a little, which is what keeps "
                     "the fish alive through the winter.",
             "correct": False,
             "why": "Bubbling air does not warm a tank, and these are "
                    "cold-water fish. It is the oxygen they need."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s17",
        "band": "standard",
        "text": "In aerobic respiration 30 g of glucose reacts with 32 g of "
                "oxygen, and 44 g of carbon dioxide is produced. What mass of "
                "water is produced?",
        "options": [
            {"text": "76 g",
             "correct": False,
             "why": "That is the carbon dioxide added to the oxygen. The water "
                    "is what is left of the 62 g that went in."},
            {"text": "14 g",
             "correct": False,
             "why": "That is 44 g taken from the glucose alone. Both reactants "
                    "have to be counted in the total going in."},
            {"text": "18 g",
             "correct": True},
            {"text": "62 g",
             "correct": False,
             "why": "That is the total mass going in. The carbon dioxide "
                    "accounts for 44 g of it, so 18 g is left."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s18",
        "band": "standard",
        "text": "Air from the room is drawn through one tube of limewater "
                "while air breathed out is bubbled through a second tube. "
                "What result would you expect?",
        "options": [
            {"text": "Both tubes turn milky at the same rate, since air is "
                     "air whichever way it has been.",
             "correct": False,
             "why": "Breathed-out air holds far more carbon dioxide, because "
                    "the cells have been making it all along."},
            {"text": "Only the room-air tube turns milky, because that air is "
                     "the fresher of the two samples.",
             "correct": False,
             "why": "Freshness is not what limewater measures. It measures "
                    "carbon dioxide, and exhaled air holds more."},
            {"text": "Neither tube changes, because limewater detects carbon "
                     "dioxide only when it is a solid.",
             "correct": False,
             "why": "Limewater is the standard test for carbon dioxide gas, and "
                    "it goes milky within seconds on exhaled breath."},
            {"text": "The tube with breathed-out air turns milky far faster "
                     "than the other one does.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s19",
        "band": "standard",
        "text": "Six people are shut in a stopped lift for two hours, and the "
                "air inside becomes stuffy and warm. Explain the change in "
                "the air.",
        "options": [
            {"text": "Their cells respired, using oxygen, giving out carbon "
                     "dioxide and warming the lift.",
             "correct": True},
            {"text": "Their breathing turned the oxygen in the lift straight "
                     "into carbon dioxide as it passed through.",
             "correct": False,
             "why": "The lungs change nothing. The oxygen was carried to the "
                    "cells, and the cells made the carbon dioxide."},
            {"text": "The carbon dioxide they breathed out was built in the "
                     "lungs from the air they took in.",
             "correct": False,
             "why": "The carbon in it comes from glucose in their food, joined "
                    "to oxygen inside their cells."},
            {"text": "The warmth came from the lift motor rather than from "
                     "the six people standing inside it.",
             "correct": False,
             "why": "A stopped lift's motor is not running, and people warm a "
                    "small closed space surprisingly quickly."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s20",
        "band": "standard",
        "text": "Blood leaving a working muscle carries less oxygen and more "
                "carbon dioxide than the blood that arrived. Explain why.",
        "options": [
            {"text": "The blood loses its oxygen to the air as it passes "
                     "close underneath the skin.",
             "correct": False,
             "why": "Blood exchanges gases with the air only in the lungs. Here "
                    "the muscle cells took the oxygen."},
            {"text": "The muscle cells respired aerobically, taking oxygen in "
                     "and giving carbon dioxide out.",
             "correct": True},
            {"text": "The muscle turned the oxygen into carbon dioxide as the "
                     "blood was going past it.",
             "correct": False,
             "why": "Oxygen is used inside the cells, where it joins carbon "
                    "that came from glucose. It is not converted on its own."},
            {"text": "The blood slowed down inside the muscle, so it could "
                     "not carry as much oxygen.",
             "correct": False,
             "why": "How fast blood flows does not change what a sample of it "
                    "contains. The cells used the oxygen up."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s21",
        "band": "standard",
        "text": "Burning a spoonful of sugar and respiring the same sugar "
                "release about the same total energy. Explain why only one of "
                "them is any use to a cell.",
        "options": [
            {"text": "Burning gives different products, so the energy that "
                     "comes out of it cannot be used.",
             "correct": False,
             "why": "The products are the same — carbon dioxide and water. It "
                    "is the way the energy arrives that differs."},
            {"text": "Burning gives out less energy altogether, so there is "
                     "never quite enough of it to be useful.",
             "correct": False,
             "why": "The totals are about the same, which is what the question "
                    "says. The problem is not how much."},
            {"text": "Respiration releases it in small steps a cell can use; "
                     "burning releases it all at once.",
             "correct": True},
            {"text": "Respiration happens in a special part of the cell, and "
                     "that is what makes it useful.",
             "correct": False,
             "why": "Where the reaction happens is not what makes the energy "
                    "usable. It is released in small controlled steps rather "
                    "than in one rush."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s22",
        "band": "standard",
        "text": "Air breathed in is about 21% oxygen and air breathed out is "
                "still about 16% oxygen. Explain why the second figure is not "
                "zero.",
        "options": [
            {"text": "Cells take only the oxygen they are able to store, and "
                     "the rest is breathed out.",
             "correct": False,
             "why": "Cells store no oxygen at all. The rest is simply oxygen "
                    "that never crossed into the blood."},
            {"text": "The lungs put some of the oxygen back into the air "
                     "again before you breathe out.",
             "correct": False,
             "why": "Oxygen moves one way in the lungs, into the blood. Nothing "
                    "is handed back to the air."},
            {"text": "The oxygen is replaced by carbon dioxide, and carbon "
                     "dioxide contains oxygen atoms.",
             "correct": False,
             "why": "The 16% is oxygen gas, measured on its own. Carbon dioxide "
                    "is counted separately from it."},
            {"text": "Only some of the oxygen in a breath crosses into the "
                     "blood; the rest goes back out.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s23",
        "band": "standard",
        "text": "A small plant is sealed in a clear jar and left in bright "
                "light, and the oxygen in the jar rises. Does that mean the "
                "plant has stopped respiring?",
        "options": [
            {"text": "No — it respires the whole time, but photosynthesis is "
                     "faster, so oxygen builds up.",
             "correct": True},
            {"text": "Yes — a plant respires only when it is too dark for it "
                     "to photosynthesise instead.",
             "correct": False,
             "why": "Respiration runs continuously. What changes with the light "
                    "is how much photosynthesis happens alongside it."},
            {"text": "Yes — no plant cell is able to carry out both of those "
                     "reactions at the same time.",
             "correct": False,
             "why": "Both run at once in a lit leaf cell, in different parts of "
                    "the cell."},
            {"text": "No — the oxygen reading rose because the sealed jar "
                     "warmed up in the bright light.",
             "correct": False,
             "why": "Warming a sealed jar creates no oxygen. The extra oxygen "
                    "came from photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s24",
        "band": "standard",
        "text": "A cell takes glucose apart in many small steps rather than "
                "in one go. What is the advantage of working that way?",
        "options": [
            {"text": "It means the cell needs less oxygen than a single step "
                     "would have needed.",
             "correct": False,
             "why": "The oxygen needed depends on how much glucose is respired, "
                    "not on the number of steps."},
            {"text": "The energy comes out in useful amounts, with no rush of "
                     "heat to destroy the cell.",
             "correct": True},
            {"text": "It makes the reaction give out more energy than one big "
                     "step would.",
             "correct": False,
             "why": "The total is fixed by the reactants and products, and it "
                    "is the same however many steps there are."},
            {"text": "It lets the cell run the reaction backwards later and "
                     "get its glucose back.",
             "correct": False,
             "why": "Respiration is not reversed in a cell. Rebuilding glucose "
                    "is what photosynthesis does in a plant."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s25",
        "band": "standard",
        "text": "15 g of glucose reacts completely with 16 g of oxygen. "
                "Calculate the total mass of carbon dioxide and water made.",
        "options": [
            {"text": "1 g",
             "correct": False,
             "why": "That is one reactant subtracted from the other. The masses "
                    "going in are added, not subtracted."},
            {"text": "16 g",
             "correct": False,
             "why": "That is the oxygen on its own. The glucose has mass too, "
                    "and all of it appears in the products."},
            {"text": "31 g",
             "correct": True},
            {"text": "15 g",
             "correct": False,
             "why": "That is the glucose on its own. The oxygen atoms end up in "
                    "the products as well and count towards the total."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s26",
        "band": "standard",
        "text": "A bowl of rice supplies 50 g of glucose. Using 15.6 kJ per "
                "gram, calculate the energy transferred when all of it is "
                "respired.",
        "options": [
            {"text": "3.2 kJ",
             "correct": False,
             "why": "That is 50 divided by 15.6. The energy per gram is "
                    "multiplied by the mass, not divided into it."},
            {"text": "65.6 kJ",
             "correct": False,
             "why": "That is 50 added to 15.6. A rate and a mass multiply "
                    "together; they are not added."},
            {"text": "156 kJ",
             "correct": False,
             "why": "That is the figure for 10 g. The mass here is 50 g, so the "
                    "answer is five times larger."},
            {"text": "780 kJ",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s27",
        "band": "standard",
        "text": "A patch of tissue loses its blood supply completely. Explain "
                "why its cells cannot go on respiring aerobically for long.",
        "options": [
            {"text": "No fresh glucose or oxygen arrives, and the carbon "
                     "dioxide made has nowhere to go.",
             "correct": True},
            {"text": "The cells lose their mitochondria as soon as the blood "
                     "stops reaching them.",
             "correct": False,
             "why": "Mitochondria stay exactly where they are. What runs out is "
                    "the supply of reactants."},
            {"text": "Respiration happens in the blood, so it stops the "
                     "moment the flow stops.",
             "correct": False,
             "why": "Respiration happens inside the cells. The blood is the "
                    "delivery and collection service for it."},
            {"text": "The cells start respiring the carbon dioxide instead, "
                     "and that quickly poisons them.",
             "correct": False,
             "why": "Carbon dioxide is a waste product and no cell can respire "
                    "it. It does build up, but that is not the same as being "
                    "used as a fuel."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s28",
        "band": "standard",
        "text": "A sealed box holds a living organism and the air around it. "
                "After a day the oxygen inside has fallen, yet the total mass "
                "of the box and its contents is unchanged. Explain.",
        "options": [
            {"text": "The mass the oxygen lost was made up by the energy "
                     "released as it reacted.",
             "correct": False,
             "why": "Energy is not a substance and has no mass to contribute to "
                    "a total."},
            {"text": "The atoms were rearranged into carbon dioxide and "
                     "water, and nothing left the box.",
             "correct": True},
            {"text": "Mass is conserved only in reactions that happen outside "
                     "a living organism.",
             "correct": False,
             "why": "Conservation of mass applies to every chemical reaction, "
                    "and biology gets no exemption."},
            {"text": "The oxygen was destroyed, and the water that was made "
                     "happens to weigh the same.",
             "correct": False,
             "why": "Atoms are never destroyed. Every oxygen atom is still in "
                    "the box, inside one of the products."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s29",
        "band": "standard",
        "text": "Someone standing outside in the cold begins to shiver. "
                "Suggest why their body uses more oxygen while they are "
                "shivering.",
        "options": [
            {"text": "Cold air holds less oxygen in it, so many more breaths "
                     "are needed to take in the same amount.",
             "correct": False,
             "why": "The air is not the problem. Muscles are working, and "
                    "working muscles respire faster."},
            {"text": "Oxygen is used up faster in the cold, because the "
                     "reaction needs the extra warmth.",
             "correct": False,
             "why": "Cooling slows respiration rather than speeding it up. It "
                    "is the shivering muscles that raise the demand."},
            {"text": "Shivering muscles keep contracting, and contracting "
                     "muscles respire faster.",
             "correct": True},
            {"text": "Shivering squeezes the lungs, which forces extra oxygen "
                     "across into the blood.",
             "correct": False,
             "why": "Shivering is muscle contraction all over the body. The "
                    "extra oxygen is being used, not forced in."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s30",
        "band": "standard",
        "text": "Respiring 300 g of carbohydrate in a day transfers about "
                "4,680 kJ. Calculate the energy transferred per gram.",
        "options": [
            {"text": "1.56 kJ",
             "correct": False,
             "why": "A power of ten has been dropped. 4,680 divided by 300 is "
                    "15.6, not 1.56."},
            {"text": "4.68 kJ",
             "correct": False,
             "why": "That is the total divided by a thousand rather than by the "
                    "300 g respired."},
            {"text": "156 kJ",
             "correct": False,
             "why": "A power of ten has been gained. Dividing 4,680 by 300 "
                    "gives 15.6."},
            {"text": "15.6 kJ",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s31",
        "band": "standard",
        "text": "A person respires 300 g of glucose in a day and breathes out "
                "440 g of carbon dioxide. Explain how the gas can weigh more "
                "than the glucose it came from.",
        "options": [
            {"text": "Oxygen atoms from the air are joined on to the carbon, "
                     "and they bring their own mass.",
             "correct": True},
            {"text": "The gas picked up water vapour on its way out through "
                     "the lungs, which added to its mass.",
             "correct": False,
             "why": "Water is a separate product and is measured separately. "
                    "The extra mass came in as oxygen."},
            {"text": "Some of the energy released turned into mass as the "
                     "carbon dioxide was forming.",
             "correct": False,
             "why": "Energy is not a substance and adds no mass. The extra mass "
                    "arrived as oxygen from the air."},
            {"text": "The two figures cannot both be right, because mass is "
                     "conserved in every reaction.",
             "correct": False,
             "why": "Mass is conserved, and it balances here: 300 g of glucose "
                    "and 320 g of oxygen give 440 g of carbon dioxide and 180 g "
                    "of water."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-s32",
        "band": "standard",
        "text": "A patient with damaged lungs is given air with extra oxygen "
                "in it through a mask. Explain how that helps their cells.",
        "options": [
            {"text": "The extra oxygen is stored in the muscles for the "
                     "patient to draw on later.",
             "correct": False,
             "why": "Cells keep no store of oxygen. What they need is a "
                    "continuous supply of it."},
            {"text": "More oxygen reaches the blood, so the cells can go on "
                     "respiring aerobically.",
             "correct": True},
            {"text": "The extra oxygen lets the lungs respire in place of the "
                     "cells that are struggling.",
             "correct": False,
             "why": "Lungs do not respire on anything else's behalf. Every cell "
                    "respires for itself."},
            {"text": "The oxygen supplies the energy the patient cannot get "
                     "from their food any more.",
             "correct": False,
             "why": "Oxygen carries no energy store. The energy comes from "
                    "glucose; oxygen is what it reacts with."},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ─────────────────────────
    {
        "id": "b8-01-h12",
        "band": "harder",
        "text": "In a respirometer, small living organisms sit above soda "
                "lime, which absorbs any carbon dioxide released. Coloured "
                "liquid in a side tube moves towards the organisms. Explain "
                "why.",
        "options": [
            {"text": "The soda lime gives off a gas of its own, which pushes "
                     "the coloured liquid along the side tube.",
             "correct": False,
             "why": "Soda lime absorbs carbon dioxide and gives off nothing at "
                    "all."},
            {"text": "The organisms warm the air around them, and warmer air "
                     "takes up less room than cold air.",
             "correct": False,
             "why": "Warming air makes it expand, which would push the liquid "
                    "the other way."},
            {"text": "Oxygen is used up and the carbon dioxide made is "
                     "absorbed, so the volume of gas falls.",
             "correct": True},
            {"text": "The organisms draw the coloured liquid up the tube each "
                     "time they take a breath in.",
             "correct": False,
             "why": "Nothing is sucked along the tube. The liquid moves because "
                    "the volume of gas inside has fallen."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h13",
        "band": "harder",
        "text": "A cell transfers 312 kJ of energy by respiring glucose. "
                "Using 15.6 kJ per gram, calculate the mass of glucose "
                "respired.",
        "options": [
            {"text": "4,867 g",
             "correct": False,
             "why": "That is 312 multiplied by 15.6. To go from energy back to "
                    "mass the total is divided by the rate."},
            {"text": "20 g",
             "correct": True},
            {"text": "2 g",
             "correct": False,
             "why": "A power of ten has been lost. 312 divided by 15.6 is 20, "
                    "not 2."},
            {"text": "200 g",
             "correct": False,
             "why": "A power of ten has been gained. 20 g of glucose at 15.6 kJ "
                    "per gram gives the 312 kJ stated."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h14",
        "band": "harder",
        "text": "The same respirometer is run again with the soda lime left "
                "out, and this time the coloured liquid barely moves at all. "
                "Explain the difference.",
        "options": [
            {"text": "The carbon dioxide given off replaces the oxygen used, "
                     "so the volume hardly changes.",
             "correct": True},
            {"text": "Without soda lime the organisms stop respiring, so "
                     "there is no change left to measure.",
             "correct": False,
             "why": "They respire exactly as before. What has changed is that "
                    "their waste gas is no longer removed."},
            {"text": "The soda lime was what used up the oxygen in the first "
                     "run of the experiment.",
             "correct": False,
             "why": "Soda lime absorbs carbon dioxide only. The oxygen was used "
                    "by the organisms both times."},
            {"text": "The carbon dioxide takes up far more room than the "
                     "oxygen that it has replaced.",
             "correct": False,
             "why": "The two are exchanged in roughly equal volumes, which is "
                    "exactly why the level barely shifts."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h15",
        "band": "harder",
        "text": "A person at rest uses about 250 cm³ of oxygen every minute. "
                "Calculate the volume of oxygen they use in one hour.",
        "options": [
            {"text": "4.2 cm³",
             "correct": False,
             "why": "That is 250 divided by 60. An hour is longer than a "
                    "minute, so the volume must be larger."},
            {"text": "15,000 cm³",
             "correct": True},
            {"text": "1,500 cm³",
             "correct": False,
             "why": "A power of ten has been dropped. 250 multiplied by 60 is "
                    "15,000."},
            {"text": "250,000 cm³",
             "correct": False,
             "why": "That is 250 multiplied by a thousand. There are 60 minutes "
                    "in an hour, not a thousand."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h16",
        "band": "harder",
        "text": "During a long walk someone respires 150 g of glucose. Every "
                "180 g of glucose produces 264 g of carbon dioxide. Calculate "
                "the carbon dioxide produced.",
        "options": [
            {"text": "264 g",
             "correct": False,
             "why": "That is the figure for 180 g of glucose. Only 150 g was "
                    "respired, so the answer is smaller."},
            {"text": "102 g",
             "correct": False,
             "why": "That is the ratio used upside down. Carbon dioxide weighs "
                    "more than the glucose it came from."},
            {"text": "220 g",
             "correct": True},
            {"text": "396 g",
             "correct": False,
             "why": "That is 264 multiplied by 1.5 rather than by 150/180. 150 "
                    "g is less than 180 g, not more."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h17",
        "band": "harder",
        "text": "A student suggests that if you breathed pure oxygen you "
                "would not need to eat. Explain why that will not work.",
        "options": [
            {"text": "Pure oxygen would be poisonous in that amount, so the "
                     "body could not make use of it.",
             "correct": False,
             "why": "Whether pure oxygen is safe is a separate question. The "
                    "point is that oxygen holds no energy store."},
            {"text": "The lungs can take in only a fixed amount of oxygen, "
                     "however pure the air around them is.",
             "correct": False,
             "why": "The limit is not the issue. Even unlimited oxygen releases "
                    "nothing with no fuel to react with."},
            {"text": "The cells would respire faster and so would run out of "
                     "energy sooner than they do now.",
             "correct": False,
             "why": "The rate is set by what the cell needs. With no glucose "
                    "there is nothing to respire at any rate."},
            {"text": "Oxygen holds no store of energy; the glucose from food "
                     "is the fuel the reaction takes apart.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h18",
        "band": "harder",
        "text": "The energy figure on a food label is found by burning a "
                "sample of the food in oxygen. Explain why that gives a fair "
                "figure for what respiration transfers from it.",
        "options": [
            {"text": "The same substances react and the same products form, "
                     "so the energy released is the same.",
             "correct": True},
            {"text": "Burning and respiring happen at much the same "
                     "temperature, so the two must release the same.",
             "correct": False,
             "why": "A flame is hundreds of degrees and a cell is at about 37 "
                    "°C. The temperatures are nothing alike."},
            {"text": "Burning is the slower of the two, which is why it gives "
                     "out the same amount of energy.",
             "correct": False,
             "why": "Burning is far faster than respiration, and speed does not "
                    "decide the total energy released."},
            {"text": "The label is only ever a rough guess, so the two "
                     "figures are not really comparable.",
             "correct": False,
             "why": "The measurement is careful, and the agreement follows from "
                    "the reactants and products being the same."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h19",
        "band": "harder",
        "text": "Glucose and oxygen keep arriving at a cell, but the route "
                "that carries its waste away is blocked. Explain why "
                "respiration in that cell still suffers.",
        "options": [
            {"text": "The waste is turned back into glucose, which the cell "
                     "then goes on to respire a second time.",
             "correct": False,
             "why": "Nothing rebuilds glucose from carbon dioxide in an animal "
                    "cell. Only photosynthesis does that."},
            {"text": "Carbon dioxide builds up, turning the cell acidic and "
                     "stopping the reaction.",
             "correct": True},
            {"text": "The mitochondria fill up with water and stop working "
                     "within a matter of seconds.",
             "correct": False,
             "why": "The water made is a small amount and the body deals with "
                    "it. The gas is the pressing problem."},
            {"text": "Respiration cannot start at all until the waste from "
                     "the last reaction has gone.",
             "correct": False,
             "why": "It runs, and goes on running for a while. The trouble is "
                    "that the waste accumulates as it does."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h20",
        "band": "harder",
        "text": "A single-celled organism in pond water needs no transport "
                "system, while a mouse cannot survive without one. Explain "
                "the difference in terms of respiration.",
        "options": [
            {"text": "The single-celled organism does not respire, so nothing "
                     "needs bringing to it.",
             "correct": False,
             "why": "Every living cell respires, and a single-celled organism "
                    "is no exception."},
            {"text": "The mouse needs a transport system in order to carry "
                     "the energy around its body.",
             "correct": False,
             "why": "Energy is not moved about as a substance. What is carried "
                    "is glucose and oxygen."},
            {"text": "Every cell needs oxygen and glucose, and in a mouse "
                     "most cells are far from the surface.",
             "correct": True},
            {"text": "The single cell stores enough oxygen inside itself to "
                     "last it for its whole life.",
             "correct": False,
             "why": "No cell stores oxygen. It reaches the surface of a single "
                    "cell by diffusion, continuously."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h21",
        "band": "harder",
        "text": "Over a day a person respires about 300 g of glucose and uses "
                "about 320 g of oxygen. A student is surprised that more "
                "oxygen is needed than food. Explain.",
        "options": [
            {"text": "One of the figures must be wrong, because a reactant "
                     "cannot outweigh the fuel itself.",
             "correct": False,
             "why": "Both are reactants, and the equation genuinely needs "
                    "slightly more oxygen by mass than glucose."},
            {"text": "Most of that oxygen is breathed straight out again "
                     "without ever having been used.",
             "correct": False,
             "why": "That is true of a single breath, but the 320 g is the "
                    "oxygen the cells actually used."},
            {"text": "Oxygen is denser than glucose, so a smaller amount of "
                     "it goes very much further.",
             "correct": False,
             "why": "These are total masses over a day, not a comparison of two "
                    "equal volumes."},
            {"text": "Each glucose molecule reacts with six oxygen molecules, "
                     "which weigh slightly more between them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h22",
        "band": "harder",
        "text": "A person's temperature is held at 42 °C for several hours. "
                "Explain why that puts their cells in danger, given how "
                "respiration is controlled.",
        "options": [
            {"text": "The enzymes controlling the steps are damaged at that "
                     "temperature and stop working.",
             "correct": True},
            {"text": "The glucose in the blood boils away, so the cells are "
                     "left with no fuel to respire.",
             "correct": False,
             "why": "Nothing boils at 42 °C. The damage is done to the enzymes, "
                    "not to the glucose."},
            {"text": "Respiration halts because the reaction can only happen "
                     "at exactly 37 °C and no other.",
             "correct": False,
             "why": "A small rise in temperature speeds respiration up. It is "
                    "the destruction of enzymes that stops it."},
            {"text": "The warmth makes the cells respire so fast that the "
                     "body's oxygen supply is used up.",
             "correct": False,
             "why": "Faster respiration does raise demand, but the danger at 42 "
                    "°C is the enzymes being destroyed."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h23",
        "band": "harder",
        "text": "Two identical flasks of living organisms are set up with "
                "indicator, one kept at 10 °C and the other at 30 °C. Predict "
                "the difference and explain it.",
        "options": [
            {"text": "Both change at the same rate, since it is the same kind "
                     "of organism in each flask.",
             "correct": False,
             "why": "Rate depends on temperature as well as on the organism, so "
                    "the warmer flask changes faster."},
            {"text": "The warmer flask changes faster, because respiration "
                     "runs faster when it is warmer.",
             "correct": True},
            {"text": "The cooler flask changes faster, because cold cells "
                     "work harder in order to keep warm.",
             "correct": False,
             "why": "Cooling slows the reactions inside a cell rather than "
                    "driving them on."},
            {"text": "Neither flask changes, because organisms sealed into a "
                     "flask stop respiring at once.",
             "correct": False,
             "why": "Sealing a flask does not stop respiration. It is how the "
                    "change in the gas is measured."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h24",
        "band": "harder",
        "text": "A sports scientist works out how much energy someone is "
                "transferring by measuring the oxygen they use. Explain why "
                "oxygen used is a good measure of energy released.",
        "options": [
            {"text": "Because the oxygen itself carries the energy that the "
                     "person is spending.",
             "correct": False,
             "why": "Oxygen holds no energy store. It is a reactant, and the "
                    "store is in the glucose."},
            {"text": "Because the oxygen breathed in is the only one of the "
                     "substances involved that ever leaves the body again "
                     "after use.",
             "correct": False,
             "why": "Oxygen enters the body. It is carbon dioxide and water "
                    "that leave it."},
            {"text": "Because a fixed mass of glucose is respired for each "
                     "mass of oxygen used, releasing a fixed amount of "
                     "energy.",
             "correct": True},
            {"text": "Because breathing is far easier to measure than "
                     "anything else about a person.",
             "correct": False,
             "why": "Convenience is not the reason. The link works because the "
                    "equation fixes the ratio."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h25",
        "band": "harder",
        "text": "Hydrogencarbonate indicator turns yellow when its "
                "surroundings become more acidic. Explain why carbon dioxide "
                "from respiring organisms turns it yellow.",
        "options": [
            {"text": "Carbon dioxide takes the oxygen out of the solution, "
                     "and that is what makes it turn acidic.",
             "correct": False,
             "why": "Nothing is removed from the solution. The gas itself "
                    "dissolves and forms an acid."},
            {"text": "The gas warms the solution as it bubbles in, and a warm "
                     "solution is always acidic.",
             "correct": False,
             "why": "Warming a solution does not make it acidic. Dissolving "
                    "carbon dioxide in it does."},
            {"text": "The indicator is detecting the oxygen used up rather "
                     "than the gas that was made.",
             "correct": False,
             "why": "The indicator responds to acidity, and the acidity comes "
                    "from carbon dioxide dissolving."},
            {"text": "Carbon dioxide dissolves in water to make a weak acid, "
                     "which lowers the pH.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h26",
        "band": "harder",
        "text": "A flask of living organisms uses 64 g of oxygen. Every 180 g "
                "of glucose respired uses 192 g of oxygen and makes 108 g of "
                "water. Calculate the mass of water made.",
        "options": [
            {"text": "36 g",
             "correct": True},
            {"text": "60 g",
             "correct": False,
             "why": "That is the mass of glucose respired. The question asks "
                    "for the water, which is 0.6 g per gram of glucose."},
            {"text": "38.4 g",
             "correct": False,
             "why": "That is 0.6 of the oxygen rather than of the glucose. Find "
                    "the glucose first: 64 g of oxygen means 60 g of glucose."},
            {"text": "108 g",
             "correct": False,
             "why": "That is the water from 180 g of glucose. Only 60 g was "
                    "respired here, so the answer is a third of it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h27",
        "band": "harder",
        "text": "A student concludes that respiration must be happening in a "
                "flask simply because the temperature inside it has risen. "
                "Give the best reason that conclusion is not yet safe.",
        "options": [
            {"text": "Respiration never warms anything, so a temperature rise "
                     "must have another cause entirely.",
             "correct": False,
             "why": "Respiration does warm its surroundings. That is not where "
                    "this conclusion goes wrong."},
            {"text": "Something other than living cells could have warmed the "
                     "flask, so a comparison is needed.",
             "correct": True},
            {"text": "Temperature cannot be measured accurately enough to "
                     "show a change of only a degree or two.",
             "correct": False,
             "why": "A thermometer measures a rise of a degree or two perfectly "
                    "well. Accuracy is not the weakness here."},
            {"text": "A temperature rise shows that breathing is happening "
                     "rather than that respiration is.",
             "correct": False,
             "why": "Breathing moves air and is not what warms a flask. The "
                    "doubt is about what else might have."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h28",
        "band": "harder",
        "text": "All the energy respiration transfers eventually leaves your "
                "body. A student says that means energy is being destroyed. "
                "Explain what is really happening.",
        "options": [
            {"text": "The energy is destroyed once the body has finished "
                     "using it to do work.",
             "correct": False,
             "why": "Energy is never destroyed. It is transferred, and it "
                    "spreads out into the surroundings."},
            {"text": "The energy goes back into glucose, which is why you "
                     "have to keep on eating.",
             "correct": False,
             "why": "Glucose is not rebuilt in the body. Eating replaces the "
                    "store that has been spent."},
            {"text": "It is transferred to the surroundings, mostly by "
                     "heating, and none of it is lost.",
             "correct": True},
            {"text": "It leaves inside the carbon dioxide, which carries it "
                     "out of the body.",
             "correct": False,
             "why": "Carbon dioxide is a substance leaving the body. Energy is "
                    "not carried out inside it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h29",
        "band": "harder",
        "text": "During an operation the carbon dioxide in a patient's "
                "exhaled breath is monitored, and a sudden fall is treated as "
                "an emergency. Explain why.",
        "options": [
            {"text": "It means the patient is respiring too fast and has used "
                     "up all of their glucose.",
             "correct": False,
             "why": "Faster respiration would raise the carbon dioxide breathed "
                    "out, not lower it."},
            {"text": "It means too much oxygen is being given, and that "
                     "pushes the carbon dioxide out first.",
             "correct": False,
             "why": "Extra oxygen does not displace carbon dioxide from the "
                    "blood in that way."},
            {"text": "It means the carbon dioxide is being stored in the "
                     "blood rather than leaving it.",
             "correct": False,
             "why": "There is no store. A fall means less is arriving at the "
                    "lungs, which is the warning."},
            {"text": "Either respiration or the blood carrying its waste has "
                     "failed, and cells are at risk.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h30",
        "band": "harder",
        "text": "Respiring 300 g of glucose makes about 180 g of water inside "
                "the body. A student says that means you can drink 180 g less "
                "each day. Evaluate that claim.",
        "options": [
            {"text": "It is partly right: the water is real, but it is small "
                     "beside the two litres a day a person loses.",
             "correct": True},
            {"text": "It is right, and the body makes all the water it needs "
                     "from respiration without drinking at all.",
             "correct": False,
             "why": "180 g is a small fraction of a day's needs, so most water "
                    "still has to be drunk."},
            {"text": "It is wrong, because water made inside the body is not "
                     "the same substance as water that is drunk.",
             "correct": False,
             "why": "It is ordinary water and the body uses it. The point is "
                    "how little of it there is."},
            {"text": "It is wrong, because every gram of that water is "
                     "breathed straight back out again as vapour.",
             "correct": False,
             "why": "Some leaves as vapour and some is used by the body. Either "
                    "way the amount is small."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h31",
        "band": "harder",
        "text": "A sealed bag of washed salad leaves holds less oxygen after "
                "a week in a fridge than it did on the day it was packed. "
                "Explain what has used the oxygen.",
        "options": [
            {"text": "The plastic of the bag slowly takes in oxygen while it "
                     "sits in the cold.",
             "correct": False,
             "why": "The packaging is not what changes the gas inside it. The "
                    "leaves are still alive."},
            {"text": "The leaf cells are still alive and have gone on "
                     "respiring inside the bag.",
             "correct": True},
            {"text": "The leaves photosynthesised in the light of the fridge "
                     "and used the oxygen up doing it.",
             "correct": False,
             "why": "Photosynthesis releases oxygen rather than using it, and a "
                    "closed fridge is dark."},
            {"text": "The oxygen leaked out through the bag because the "
                     "fridge is so cold inside.",
             "correct": False,
             "why": "A sealed bag holds its gas in. What changed the air inside "
                    "it was respiration."},
        ],
        "figure": None,
    },
    {
        "id": "b8-01-h32",
        "band": "harder",
        "text": "Glucose is 40% carbon by mass. What mass of carbon leaves as "
                "carbon dioxide when 250 g of glucose is respired?",
        "options": [
            {"text": "40 g",
             "correct": False,
             "why": "That is the percentage copied out as a mass. It has to be "
                    "applied to the 250 g respired."},
            {"text": "625 g",
             "correct": False,
             "why": "That is 250 divided by 0.4. A part of the glucose cannot "
                    "weigh more than all of it."},
            {"text": "100 g",
             "correct": True},
            {"text": "150 g",
             "correct": False,
             "why": "That is the other 60% of the glucose, which is the "
                    "hydrogen and oxygen in it rather than the carbon."},
        ],
        "figure": None,
    },
]
