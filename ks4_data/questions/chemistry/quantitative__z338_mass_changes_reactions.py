"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`mass-changes-reactions`.

AQA 4.3.1.3, worked from both directions. A reading FALLS when a gas leaves an
open vessel — hydrogen from a metal and acid, carbon dioxide from a carbonate,
water vapour from a hydrated salt, the gaseous products of a burning fuel. A
reading RISES when a gas from the air joins a solid — a metal burning, iron
rusting. In a closed vessel it does neither. The rows cover predicting the
direction, doing the arithmetic in both directions, choosing apparatus that
demonstrates conservation, and the two conclusions students reach that are
wrong: that mass was destroyed, and that the balance must be faulty.

⚠️ FOUNDATION TIER. No mole appears anywhere; every calculation is conservation
arithmetic on masses given in the stem.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-mass-changes-reactions-e05",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flask of dilute hydrochloric acid with a strip of magnesium "
                "in it stands open on a balance. Predict how the reading "
                "changes as the reaction proceeds.",
        "options": [
            "It falls, because the hydrogen made escapes from the flask",
            "It rises, because the magnesium takes in acid as it dissolves",
            "It stays the same, because the magnesium is still in the flask",
            "It rises, because a new substance has been made in the flask",
        ],
        "correct_index": 0,
        "why": "Hydrogen gas bubbles out of an open flask and is no longer on "
               "the balance, so the reading drops by the mass of gas lost.",
    },
    {
        "id": "ks4-mass-changes-reactions-e06",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the change in which the mass of the solid in an open "
                "dish increases.",
        "options": [
            "Calcium carbonate being heated very strongly",
            "Iron wool rusting slowly in damp air",
            "Hydrated copper sulfate being heated",
            "A small candle burning in the dish",
        ],
        "correct_index": 1,
        "why": "Rusting adds oxygen and water from the air to the iron, so the "
               "solid gains mass while the other three all lose a gas.",
    },
    {
        "id": "ks4-mass-changes-reactions-e07",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the reading on a balance when a "
                "reaction that gives off a gas is carried out in a sealed "
                "flask.",
        "options": [
            "It rises by the mass of the gas that has been made",
            "It falls by the mass of the gas that has been made",
            "It does not change, because the gas cannot leave",
            "It falls and then rises back to its starting value",
        ],
        "correct_index": 2,
        "why": "A sealed flask is a closed system, so the gas is still inside "
               "it and still being weighed.",
    },
    {
        "id": "ks4-mass-changes-reactions-e08",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas that escapes when marble chips react with dilute "
                "hydrochloric acid in an open beaker.",
        "options": [
            "Hydrogen",
            "Oxygen",
            "Sulfur dioxide",
            "Carbon dioxide",
        ],
        "correct_index": 3,
        "why": "Marble is calcium carbonate, and a carbonate with an acid "
               "gives a salt, water and carbon dioxide.",
    },
    {
        "id": "ks4-mass-changes-reactions-e09",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student burns magnesium ribbon in an open crucible and "
                "finds the white ash is heavier than the ribbon was. State "
                "where the extra mass has come from.",
        "options": [
            "From oxygen in the air, which has joined the magnesium",
            "From the heat energy that the Bunsen burner put into the ribbon",
            "From the magnesium atoms, which grow larger when heated",
            "From carbon dioxide in the air, which sticks to the ash",
        ],
        "correct_index": 0,
        "why": "The magnesium reacts with oxygen from the air to make "
               "magnesium oxide, so the oxygen's mass is added to the solid.",
    },
    {
        "id": "ks4-mass-changes-reactions-e10",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a chemist can say mass has been conserved even "
                "though a balance reading has fallen.",
        "options": [
            "Because the balance reads a little low while a reaction happens",
            "Because the gas that left still has mass, just not on the balance",
            "Because the mass will come back once the reaction has finished",
            "Because a falling reading shows the products are lighter atoms",
        ],
        "correct_index": 1,
        "why": "Conservation of mass covers every substance made, and a gas "
               "that has drifted away is still one of the products.",
    },
    {
        "id": "ks4-mass-changes-reactions-e11",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the reaction whose balance reading would fall if it "
                "were carried out in an open flask.",
        "options": [
            "Copper heated in a crucible of air",
            "Iron wool left standing in damp air",
            "Zinc added to dilute sulfuric acid",
            "Silver nitrate mixed with sodium chloride solution",
        ],
        "correct_index": 2,
        "why": "Zinc with sulfuric acid gives off hydrogen, which leaves an "
               "open flask; the other three either gain a gas or exchange "
               "none.",
    },
    {
        "id": "ks4-mass-changes-reactions-e12",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two solutions are mixed in an open beaker on a balance and a "
                "precipitate forms. Predict what happens to the reading.",
        "options": [
            "It falls, because the precipitate settles to the bottom",
            "It rises, because a solid weighs more than a solution",
            "It falls, because the precipitate takes water out of solution",
            "It does not change, because no gas enters or leaves the beaker",
        ],
        "correct_index": 3,
        "why": "The precipitate is still in the beaker, and nothing has been "
               "gained from or lost to the air, so the total mass is "
               "unchanged.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-mass-changes-reactions-s05",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A conical flask of dilute acid and calcium carbonate stands "
                "open on a balance. The reading falls from 152.40 g to "
                "150.20 g. Calculate the mass of carbon dioxide released.",
        "options": [
            "2.20 g",
            "0.22 g",
            "22.0 g",
            "302.60 g",
        ],
        "correct_index": 0,
        "why": "The only substance to leave the flask is the gas, so its mass "
               "is 152.40 − 150.20 = 2.20 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s06",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crucible and its lid weigh 18.50 g. 1.60 g of magnesium "
                "ribbon is added and the crucible heated until the reaction "
                "is complete, when the total mass is 21.10 g. Calculate the "
                "mass of oxygen that combined with the magnesium.",
        "options": [
            "1.00 g",
            "0.60 g",
            "2.60 g",
            "1.60 g",
        ],
        "correct_index": 0,
        "why": "The crucible and magnesium came to 20.10 g, so the gain of "
               "1.00 g is the oxygen taken from the air.",
    },
    {
        "id": "ks4-mass-changes-reactions-s07",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the balance reading falls fastest at the very "
                "start when a carbonate reacts with acid in an open flask.",
        "options": [
            "Because the balance needs time to settle after the flask is "
            "placed on it",
            "Because the acid is most concentrated then, so gas is made "
            "fastest",
            "Because the carbon dioxide made at the start is denser than that "
            "made later",
            "Because the carbonate is at the top of the flask when the "
            "reaction begins",
        ],
        "correct_index": 1,
        "why": "The reaction is fastest when the acid is most concentrated, so "
               "carbon dioxide leaves the flask fastest at the start.",
    },
    {
        "id": "ks4-mass-changes-reactions-s08",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student plugs the neck of a flask with cotton wool during a "
                "reaction that gives off hydrogen. Explain the effect this "
                "has on the balance reading.",
        "options": [
            "The reading rises, because the cotton wool absorbs the hydrogen",
            "The reading still falls, because hydrogen passes through the wool",
            "The reading stays constant, because the wool seals the flask",
            "The reading falls faster, because the wool speeds the reaction up",
        ],
        "correct_index": 1,
        "why": "Cotton wool stops acid spray but not gas, so the hydrogen "
               "still leaves and the reading still drops.",
    },
    {
        "id": "ks4-mass-changes-reactions-s09",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron wool is sealed in a tube with damp air and left for a "
                "week, by which time it has rusted. Predict the mass of the "
                "sealed tube and its contents at the end of the week.",
        "options": [
            "Greater, because the iron has taken in oxygen and water",
            "Smaller, because rust is a more open, flaky solid than iron",
            "Unchanged, because nothing has entered or left the tube",
            "Greater, because rust contains water as well as iron and oxygen "
            "atoms",
        ],
        "correct_index": 2,
        "why": "The iron gains mass but the sealed air loses exactly the same "
               "mass, so the tube and its contents weigh what they always "
               "did.",
    },
    {
        "id": "ks4-mass-changes-reactions-s10",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "2.24 g of iron is heated in air until all of it has become "
                "iron(III) oxide, and the solid then weighs 3.20 g. Calculate "
                "the mass of oxygen that combined with the iron.",
        "options": [
            "5.44 g",
            "2.24 g",
            "1.28 g",
            "0.96 g",
        ],
        "correct_index": 3,
        "why": "The iron was already on the balance, so the increase of "
               "3.20 − 2.24 = 0.96 g is the oxygen added.",
    },
    {
        "id": "ks4-mass-changes-reactions-s11",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats 12.50 g of hydrated magnesium sulfate in an "
                "open dish until no further mass is lost, leaving 6.10 g of "
                "white powder. Calculate the mass of water driven off.",
        "options": [
            "6.40 g",
            "18.60 g",
            "6.10 g",
            "3.20 g",
        ],
        "correct_index": 0,
        "why": "Only water leaves the dish, so its mass is "
               "12.50 − 6.10 = 6.40 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s12",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the reaction that would show no change in mass when "
                "carried out in an open beaker on a balance.",
        "options": [
            "Magnesium added to dilute sulfuric acid",
            "Sodium carbonate added to dilute nitric acid solution",
            "Zinc added to copper(II) sulfate solution",
            "A small candle burning inside the beaker",
        ],
        "correct_index": 2,
        "why": "A displacement between a metal and a salt solution makes no "
               "gas at all, so nothing can enter or leave the beaker.",
    },
    {
        "id": "ks4-mass-changes-reactions-s13",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why heating copper in a sealed tube of air gives no "
                "change in the balance reading even though the copper itself "
                "gains mass.",
        "options": [
            "The oxygen came from the air already sealed inside the tube",
            "The copper loses as much heat energy as it gains in oxygen",
            "The black copper oxide formed is lighter than the copper was",
            "The tube expands as it is heated, which cancels out the gain in "
            "mass",
        ],
        "correct_index": 0,
        "why": "In a closed system the oxygen simply moves from the trapped "
               "air into the solid, so the total inside the tube is "
               "unchanged.",
    },
    {
        "id": "ks4-mass-changes-reactions-s14",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed flask holding a finished reaction mixture weighs "
                "96.40 g. The stopper is then removed and the mass falls to "
                "95.35 g. Calculate the mass of gas that had been produced.",
        "options": [
            "0.105 g",
            "10.5 g",
            "191.75 g",
            "1.05 g",
        ],
        "correct_index": 3,
        "why": "The gas was trapped until the stopper came out, so its mass is "
               "96.40 − 95.35 = 1.05 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s15",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the balance readings obtained when equal masses of "
                "calcium carbonate are heated, one sample in an open crucible "
                "and the other in a sealed tube.",
        "options": [
            "Both readings fall, because carbon dioxide is made in each case",
            "The open crucible reading falls; the sealed tube is unchanged",
            "Both readings are unchanged, because mass is conserved here",
            "The open crucible reading rises; the sealed tube reading falls",
        ],
        "correct_index": 1,
        "why": "Carbon dioxide is made in both, but only the open crucible "
               "lets it leave the balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-s16",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to demonstrate that mass is conserved when "
                "marble reacts with acid. Describe the change to the method "
                "that would show this.",
        "options": [
            "Weigh the marble and the acid separately before mixing them",
            "Use a larger mass of marble so the change is easier to see",
            "Warm the acid first so the reaction finishes more quickly",
            "Run the reaction in a stoppered flask and weigh it throughout",
        ],
        "correct_index": 3,
        "why": "Stoppering the flask keeps the carbon dioxide on the balance, "
               "so the reading stays constant and conservation is visible.",
    },
    {
        "id": "ks4-mass-changes-reactions-s17",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas syringe is sealed to a flask in which 0.50 g of "
                "magnesium reacts with excess acid. The whole apparatus "
                "weighs 210.60 g beforehand. Determine the reading once the "
                "reaction has finished.",
        "options": [
            "210.10 g",
            "211.10 g",
            "210.60 g",
            "210.56 g",
        ],
        "correct_index": 2,
        "why": "The hydrogen is held in the syringe, which is part of the "
               "weighed apparatus, so the reading does not move.",
    },
    {
        "id": "ks4-mass-changes-reactions-s18",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the balance reading stops changing part-way "
                "through a reaction carried out in an open flask.",
        "options": [
            "The balance has reached the limit of what it is able to measure",
            "One of the reactants has been used up, so no more gas is made",
            "The gas above the mixture has become too dense to leave the flask",
            "The products have settled, so they no longer press on the pan",
        ],
        "correct_index": 1,
        "why": "The reading only falls while gas is escaping, and gas stops "
               "being made once a reactant runs out.",
    },
    {
        "id": "ks4-mass-changes-reactions-s19",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "6.00 g of copper is heated in an open crucible until all of "
                "it has become copper(II) oxide, absorbing 1.50 g of oxygen. "
                "Determine the mass of copper oxide formed.",
        "options": [
            "4.50 g",
            "6.00 g",
            "7.50 g",
            "1.50 g",
        ],
        "correct_index": 2,
        "why": "Every atom stays in the crucible, so the oxide weighs "
               "6.00 + 1.50 = 7.50 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s20",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that a reaction giving off a gas in an open "
                "flask breaks the law of conservation of mass. Identify the "
                "mistake in this reasoning.",
        "options": [
            "The law applies to every product made, not only to what is still "
            "weighed",
            "The law applies to sealed containers, so an open flask sits "
            "outside of its scope",
            "The law applies to solids and liquids, but gases are counted "
            "separately",
            "The law applies once a reaction is complete, not while it is "
            "happening",
        ],
        "correct_index": 0,
        "why": "The gas is one of the products and still has its mass; the "
               "balance has simply stopped being able to weigh it.",
    },
    {
        "id": "ks4-mass-changes-reactions-s21",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flask of dilute acid and marble chips stands open on a "
                "balance, reading 204.50 g at the start. 1.32 g of carbon "
                "dioxide is released during the reaction. Determine the final "
                "reading.",
        "options": [
            "203.18 g",
            "205.82 g",
            "204.50 g",
            "203.30 g",
        ],
        "correct_index": 0,
        "why": "Only the gas leaves, so the reading drops by its mass: "
               "204.50 − 1.32 = 203.18 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s22",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a nail that has rusted in the open air weighs "
                "more than the nail did when it was new.",
        "options": [
            "Rust is a denser material than the iron that it has replaced",
            "Oxygen and water from the air have combined with the iron",
            "Iron atoms take up more room once they have been oxidised",
            "The damp air has left a film of moisture on the nail's surface",
        ],
        "correct_index": 1,
        "why": "Rust is hydrated iron(III) oxide, so the nail has gained the "
               "mass of the oxygen and water that reacted with it.",
    },
    {
        "id": "ks4-mass-changes-reactions-s23",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats 8.40 g of magnesium carbonate in an open "
                "crucible until no further change occurs, leaving 4.00 g of "
                "magnesium oxide. Determine the mass of carbon dioxide that "
                "escaped.",
        "options": [
            "12.40 g",
            "8.40 g",
            "2.20 g",
            "4.40 g",
        ],
        "correct_index": 3,
        "why": "The carbonate can only lose carbon dioxide, so "
               "8.40 − 4.00 = 4.40 g of gas left the crucible.",
    },
    {
        "id": "ks4-mass-changes-reactions-s24",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc reacts with dilute hydrochloric acid in a stoppered "
                "flask, and the same reaction is run in a flask with a "
                "balloon stretched over its neck. Compare what the balance "
                "shows in each case.",
        "options": [
            "The stoppered flask is unchanged; the balloon flask reading falls",
            "Both readings fall, because the hydrogen leaves the mixture",
            "Both readings are unchanged, because the gas is trapped in each",
            "The stoppered flask reading falls; the balloon flask is unchanged",
        ],
        "correct_index": 2,
        "why": "A balloon holds the hydrogen just as a stopper does, so in "
               "both cases every product stays on the balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-s25",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records the mass of an open flask every minute "
                "during a reaction that gives off carbon dioxide. Describe "
                "how the readings change with time.",
        "options": [
            "They fall by the same amount each minute until the acid runs out",
            "They fall quickly at first, then more slowly, then stop falling",
            "They stay level at first, then fall sharply once the gas builds up",
            "They fall slowly at first and then more quickly as it warms up",
        ],
        "correct_index": 1,
        "why": "Gas is lost fastest while the reaction is fastest, and the "
               "reading stops moving once a reactant is used up.",
    },
    {
        "id": "ks4-mass-changes-reactions-s26",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass on the balance appears to fall when a "
                "fuel burns but appears to rise when a metal burns.",
        "options": [
            "A fuel burns hotter, so more of its mass is turned into energy",
            "A fuel's products are gases that leave; a metal's product keeps "
            "its oxygen",
            "A fuel reacts with nitrogen while a metal reacts only with oxygen",
            "A fuel is a liquid or a gas already, so it cannot hold on to any "
            "mass",
        ],
        "correct_index": 1,
        "why": "Burning a fuel turns it into carbon dioxide and water vapour, "
               "which drift away, while a burning metal forms a solid oxide "
               "that stays on the balance.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-mass-changes-reactions-h05",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An empty crucible weighs 22.40 g. 3.60 g of a metal is added "
                "and heated in air until all of it is oxidised, after which "
                "the crucible and oxide weigh 28.40 g. Calculate the mass of "
                "oxygen that combined with the metal.",
        "options": [
            "6.00 g",
            "3.60 g",
            "2.40 g",
            "1.80 g",
        ],
        "correct_index": 2,
        "why": "The crucible and metal came to 26.00 g, so the extra "
               "28.40 − 26.00 = 2.40 g is oxygen from the air.",
    },
    {
        "id": "ks4-mass-changes-reactions-h06",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats 5.00 g of blue hydrated copper(II) sulfate "
                "until it is white and weighs 3.20 g, then concludes that "
                "1.80 g of the crystals must have been impurity. Evaluate "
                "this conclusion.",
        "options": [
            "Correct, because a pure sample would not lose mass on heating",
            "Correct, because it is the impurity that makes the crystals blue",
            "Wrong, because the 1.80 g is water of crystallisation driven off",
            "Wrong, because the missing 1.80 g was sulfur dioxide given off",
        ],
        "correct_index": 2,
        "why": "The blue crystals hold water chemically combined in them, and "
               "heating drives that water off as vapour, leaving the white "
               "anhydrous salt.",
    },
    {
        "id": "ks4-mass-changes-reactions-h07",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "1.60 g of a metal is heated in air and the oxide formed "
                "weighs 2.00 g. A 4.00 g sample of the same metal is then "
                "heated in the same way. Determine the mass of oxide formed "
                "from the second sample.",
        "options": [
            "5.00 g",
            "4.40 g",
            "6.40 g",
            "4.00 g",
        ],
        "correct_index": 0,
        "why": "Every 1.60 g of metal gives 2.00 g of oxide, and 4.00 g is "
               "2.5 times as much, so 2.00 × 2.5 = 5.00 g forms.",
    },
    {
        "id": "ks4-mass-changes-reactions-h08",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed flask holds 50.00 g of acid and 5.00 g of marble "
                "chips. When the reaction has finished the flask is opened "
                "and 1.10 g of carbon dioxide escapes. Determine the mass of "
                "the flask contents once it has been opened.",
        "options": [
            "53.90 g",
            "55.00 g",
            "56.10 g",
            "48.90 g",
        ],
        "correct_index": 0,
        "why": "The sealed flask held 55.00 g throughout, and opening it lets "
               "1.10 g of gas out, leaving 53.90 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-h09",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to show that mass is conserved when magnesium "
                "burns. Determine the apparatus that would demonstrate it.",
        "options": [
            "An open crucible with its lid resting slightly ajar on top",
            "A crucible standing on a balance inside a fume cupboard",
            "A flask fitted with a gas syringe to collect the product",
            "A sealed tube holding the magnesium and enough air to burn it",
        ],
        "correct_index": 3,
        "why": "Burning magnesium takes oxygen from the air, so only a sealed "
               "vessel keeps both the oxygen used and the oxide formed on the "
               "balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-h10",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a candle burning inside a sealed jar on a balance "
                "gives a steady reading while the same candle burning in the "
                "open air gives a falling one.",
        "options": [
            "In the jar the flame is smaller, so much less wax is used up",
            "In the jar nothing can leave, while in the open the products "
            "drift off",
            "In the jar the oxygen runs out, so no products are made at all",
            "In the open air the wax melts and runs off the balance pan",
        ],
        "correct_index": 1,
        "why": "The wax, the oxygen and the carbon dioxide and water made are "
               "all still inside the sealed jar; in the open air the two "
               "gaseous products leave the balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-h11",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heating 4.20 g of sodium hydrogencarbonate in an open tube "
                "leaves 2.65 g of sodium carbonate, and both water vapour and "
                "carbon dioxide escape. The carbon dioxide accounts for "
                "1.10 g. Determine the mass of water vapour lost.",
        "options": [
            "1.55 g",
            "2.65 g",
            "0.45 g",
            "1.10 g",
        ],
        "correct_index": 2,
        "why": "The tube lost 4.20 − 2.65 = 1.55 g in total, and 1.10 g of "
               "that was carbon dioxide, so 0.45 g was water vapour.",
    },
    {
        "id": "ks4-mass-changes-reactions-h12",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats iron wool in an open crucible and the reading "
                "rises by 0.48 g. They conclude that the balance must be "
                "faulty, because mass cannot increase. Evaluate this "
                "conclusion.",
        "options": [
            "Correct, because a solid cannot gain mass while it is being "
            "heated",
            "Wrong, because oxygen from the air has joined the iron in the "
            "crucible",
            "Correct, because the hot air rising off the crucible lifts the "
            "pan",
            "Wrong, because the iron has expanded and now presses harder on "
            "the pan",
        ],
        "correct_index": 1,
        "why": "The crucible is open, so oxygen can be added to the solid from "
               "the air, and 0.48 g of it has been.",
    },
    {
        "id": "ks4-mass-changes-reactions-h13",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two solutions react in an open beaker with no gas given off "
                "at all, yet the reading falls by 0.05 g over ten minutes. "
                "Suggest the cause of this fall.",
        "options": [
            "Water has evaporated from the surface of the solution",
            "The precipitate has dissolved back into the solution again",
            "The reaction has used some of the mass to release energy",
            "The beaker has cooled, so it now presses less on the pan",
        ],
        "correct_index": 0,
        "why": "Evaporation is a physical change that removes water vapour "
               "from an open beaker, and it costs mass just as an escaping "
               "gas does.",
    },
    {
        "id": "ks4-mass-changes-reactions-h14",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flask sealed to a gas syringe weighs 315.20 g. 0.24 g of "
                "magnesium is then dropped in and reacts completely with the "
                "excess acid inside, pushing hydrogen into the syringe. "
                "Determine the total mass afterwards.",
        "options": [
            "315.20 g",
            "314.96 g",
            "315.42 g",
            "315.44 g",
        ],
        "correct_index": 3,
        "why": "The magnesium adds 0.24 g to a closed system and the hydrogen "
               "stays inside the syringe, so the total is "
               "315.20 + 0.24 = 315.44 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-h15",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "5.0 g of calcium carbonate is heated in an open crucible, "
                "and a second 5.0 g sample is added to excess acid in an open "
                "flask. Compare the direction in which each balance reading "
                "moves.",
        "options": [
            "Only the heated sample falls, because heat drives the gas off",
            "Only the acid sample falls, because the bubbling carries the gas "
            "away",
            "Both fall, because each of them releases carbon dioxide",
            "Neither falls, because the carbonate is a solid in both cases",
        ],
        "correct_index": 2,
        "why": "A carbonate gives off carbon dioxide both when heated and when "
               "attacked by an acid, and an open vessel lets it go in either "
               "case.",
    },
    {
        "id": "ks4-mass-changes-reactions-h16",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heating 20.00 g of a hydrated salt to constant mass leaves "
                "12.80 g of the anhydrous salt. A second sample of the same "
                "salt leaves 6.40 g. Determine the mass of the second sample "
                "before heating.",
        "options": [
            "13.60 g",
            "6.40 g",
            "12.80 g",
            "10.00 g",
        ],
        "correct_index": 3,
        "why": "The second sample leaves half as much anhydrous salt, so it "
               "must have been half the size: 20.00 ÷ 2 = 10.00 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-h17",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nail rusts slowly inside a stoppered jar of damp air. "
                "Determine how the mass of the nail and the mass of the air "
                "in the jar each change.",
        "options": [
            "The nail gains mass and the air loses the same amount",
            "Both the nail and the air in the jar gain a little mass",
            "The nail gains mass and the air in the jar is unaffected",
            "The nail loses mass because flakes of rust fall off it",
        ],
        "correct_index": 0,
        "why": "The oxygen and water that join the nail come out of the air in "
               "the jar, so one gains exactly what the other loses.",
    },
    {
        "id": "ks4-mass-changes-reactions-h18",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed flask of magnesium and dilute acid weighs 126.40 g. "
                "The reaction makes 0.04 g of hydrogen. Determine the reading "
                "while the flask is still sealed and the reading once the "
                "stopper is removed.",
        "options": [
            "126.44 g sealed, then 126.40 g opened",
            "126.40 g sealed, then 126.36 g opened",
            "126.36 g sealed, then 126.36 g opened",
            "126.40 g sealed, then 126.40 g opened",
        ],
        "correct_index": 1,
        "why": "Nothing leaves while the flask is closed, and removing the "
               "stopper lets the 0.04 g of hydrogen out.",
    },
    {
        "id": "ks4-mass-changes-reactions-h19",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three students heat identical 4.00 g samples of copper in "
                "open crucibles and record final masses of 5.00 g, 5.00 g and "
                "4.20 g. Suggest why the third result is so much lower than "
                "the others.",
        "options": [
            "The third student weighed the crucible before the copper cooled",
            "The third student heated the copper for too long, so oxide was "
            "lost",
            "The third student's copper was only partly converted to the oxide",
            "The third student used a crucible of a slightly different mass",
        ],
        "correct_index": 2,
        "why": "The gain in mass is the oxygen taken up, so a much smaller "
               "gain means much less of the copper had reacted.",
    },
    {
        "id": "ks4-mass-changes-reactions-h20",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine why weighing a reaction inside a fume cupboard with "
                "the extraction fan running can give an unreliable balance "
                "reading.",
        "options": [
            "The fan cools the mixture, which slows the reaction right down",
            "The fan removes the gas, so the reading falls further than it "
            "should",
            "The moving air pushes on the pan and the apparatus as they are "
            "weighed",
            "The fan changes the air pressure, which alters the mass of the "
            "flask",
        ],
        "correct_index": 2,
        "why": "A draught applies its own force to the balance pan, so the "
               "reading drifts for a reason that has nothing to do with the "
               "chemistry.",
    },
    {
        "id": "ks4-mass-changes-reactions-h21",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "2.00 g of magnesium is added to 100.00 g of dilute "
                "hydrochloric acid in an open beaker weighing 85.00 g. All "
                "the magnesium dissolves and 0.16 g of hydrogen escapes. "
                "Determine the final balance reading.",
        "options": [
            "187.00 g",
            "185.00 g",
            "186.84 g",
            "184.84 g",
        ],
        "correct_index": 2,
        "why": "The beaker, acid and magnesium come to 187.00 g, and only the "
               "hydrogen leaves: 187.00 − 0.16 = 186.84 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-h22",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the method that would let a chemist find the mass "
                "of carbon dioxide made when a carbonate reacts with an acid.",
        "options": [
            "Weigh the solid that is left in the flask at the very end",
            "Weigh a stoppered flask before the reaction and after opening it",
            "Collect the gas in a syringe and read the volume it occupies",
            "Weigh the acid before the reaction and again once it has stopped",
        ],
        "correct_index": 1,
        "why": "Stoppering keeps every product on the balance, so the drop "
               "when the stopper comes out is exactly the mass of gas made.",
    },
    {
        "id": "ks4-mass-changes-reactions-h23",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the increase in a balance reading when a metal is "
                "heated in air equals the mass of oxygen added, rather than "
                "the mass of the oxide formed.",
        "options": [
            "Because the oxide is lighter than the metal and the oxygen "
            "together",
            "Because the metal was already on the balance before the heating "
            "began",
            "Because part of the oxide is lost as dust while the metal is "
            "heated",
            "Because the balance measures just the substances made during the "
            "change",
        ],
        "correct_index": 1,
        "why": "The balance was already carrying the metal, so the reading can "
               "only change by whatever has been added to it — the oxygen.",
    },
    {
        "id": "ks4-mass-changes-reactions-h24",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "1.44 g of magnesium is heated in an open crucible. The "
                "balance reading rises by 0.96 g and then stops rising. "
                "Determine the mass of magnesium oxide in the crucible.",
        "options": [
            "0.96 g",
            "1.44 g",
            "0.48 g",
            "2.40 g",
        ],
        "correct_index": 3,
        "why": "The rise is the oxygen taken up, and all of it has combined "
               "with the magnesium: 1.44 + 0.96 = 2.40 g of oxide.",
    },
    {
        "id": "ks4-mass-changes-reactions-h25",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs an open flask of acid and marble, lets the "
                "reaction finish, and finds the reading has fallen by 2.20 g. "
                "They say 2.20 g of marble has been destroyed. Evaluate this "
                "statement.",
        "options": [
            "Correct, because the marble is the solid that has been used up "
            "here",
            "Wrong, because the 2.20 g is carbon dioxide, and more marble than "
            "that reacted",
            "Correct, because the fall in mass measures the marble that has "
            "dissolved",
            "Wrong, because the 2.20 g is water lost from the acid by "
            "evaporation",
        ],
        "correct_index": 1,
        "why": "No mass is destroyed: 2.20 g of carbon dioxide left the flask, "
               "and since the gas is only part of the carbonate, over 2.20 g "
               "of marble must have reacted.",
    },
    {
        "id": "ks4-mass-changes-reactions-h26",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lit candle stands inside a large sealed bell jar on a "
                "balance and burns until it goes out. Predict the reading "
                "during the burning and once the flame has gone out.",
        "options": [
            "It falls while the candle burns, then holds steady afterwards",
            "It rises while the candle burns, then falls back afterwards",
            "It falls while the candle burns and keeps falling afterwards",
            "It does not change at any point, because the jar is sealed",
        ],
        "correct_index": 3,
        "why": "Everything the candle uses and everything it makes is inside "
               "the sealed jar, so the total on the balance never alters.",
    },
]
