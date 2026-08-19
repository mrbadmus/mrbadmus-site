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
            {"text": "The flight muscle cell respires far faster, because "
                     "contracting constantly needs energy constantly.",
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
]
