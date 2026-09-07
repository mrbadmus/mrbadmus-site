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
]
