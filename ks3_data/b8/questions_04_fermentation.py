# -*- coding: utf-8 -*-
"""B8 lesson 04 — Fermentation and what we use it for: twelve questions (MRB-269).

The lesson makes one claim and then hands the student four dials to test it:
fermentation is respiration, carried out by a living micro-organism, and which
organism you choose decides which product you get. The bank probes the three
places that claim breaks down — whether the organism is alive at all, whether
the conditions decide the route or merely the speed, and whether the product
belongs to the organism or to the food.

The distractors are built from the lesson's two declared misconceptions.
RESP-08 ("yeast is a powder — a raising agent, like baking powder") supplies
every option in which yeast dissolves, sets off a chemical reaction, breathes,
or is started by warm water for a physical reason. RESP-07 ("fermenting is just
food going off in a controlled way") supplies the kimchi that has been left to
spoil safely, the acid that was added rather than made, and the yoghurt that is
milk gone off under supervision. Four further errors the lesson exists to
correct are worked as well: that cold kills rather than slows, that heat-killed
cells recover once cooled, that ethanol rather than carbon dioxide raises
dough, and that a dial can change which product an organism makes — the bench's
own lesson that only the organism dial does that.

No question restates a ladder rung. Rung 1 owns the yeast word summary, so the
bank comes at the two routes through the bacterial one and through what is
absent from it; rung 2 owns the ethanol leaving the loaf, so the oven does not
appear here at all; rung 3 owns the yoghurt explanation, so preservation is
approached only through a jar that fails to make any acid; and rung 4 owns the
investigation design, so temperature appears as a reading off the bench and as
the difference between slow and dead.

`figure` is `None` throughout — the lesson declares no figures, and every stem
here is self-contained.
"""

UNIT = "B8"
LESSON = "fermentation"
LESSON_NUMBER = 4

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-04-e01",
        "band": "easier",
        "text": "A jar of kimchi is labelled “fermented”. What has "
                "actually been done to the cabbage inside it?",
        "options": [
            {"text": "It has been left to go off slowly, under conditions "
                     "that keep it safe",
             "correct": False,
             "why": "This is the idea the lesson exists to kill. Milk or "
                    "cabbage spoils because whatever lands on it grows. "
                    "Fermenting is the opposite — one chosen "
                    "micro-organism is given the conditions it likes, and its "
                    "waste product is what keeps everything else out."},
            {"text": "A chosen micro-organism has respired the sugars in it "
                     "without oxygen",
             "correct": True},
            {"text": "Acid has been added to it, which is what gives it the "
                     "sour taste",
             "correct": False,
             "why": "Nothing went into the jar but salt and time. The acid is "
                    "made inside it, by bacteria, out of the sugars in the "
                    "cabbage. That is the difference between a fermented food "
                    "and a pickled one."},
            {"text": "It has been heated to kill the micro-organisms that "
                     "would spoil it",
             "correct": False,
             "why": "Heat would kill the organism you want as well — set "
                    "the bench to 80 °C and it reports nothing, "
                    "permanently. A fermented food is one where a "
                    "micro-organism was deliberately kept alive."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e02",
        "band": "easier",
        "text": "Warm milk is sealed in a vessel with yoghurt bacteria and "
                "left alone. What do they make from the sugar in it?",
        "options": [
            {"text": "Ethanol and carbon dioxide, as a brewer’s yeast "
                     "does",
             "correct": False,
             "why": "That is the yeast route. Which organism you put in the "
                    "vessel is what decides the product, and these bacteria "
                    "take the other route entirely."},
            {"text": "Carbon dioxide and water, and nothing else at all",
             "correct": False,
             "why": "Those are the products of aerobic respiration, and this "
                    "vessel is sealed. With no oxygen the sugar is only "
                    "partly broken down, and it stops at an acid."},
            {"text": "Lactic acid and carbon dioxide, in roughly equal "
                     "amounts",
             "correct": False,
             "why": "Lactic acid, yes — but this route makes no gas at "
                    "all. That is exactly why a yoghurt sets into a solid "
                    "instead of foaming up the way dough does."},
            {"text": "Lactic acid alone — this route makes no gas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e03",
        "band": "easier",
        "text": "Dried yeast is always started in warm water, never in "
                "boiling water. Why?",
        "options": [
            {"text": "Yeast is alive, and boiling water denatures its enzymes "
                     "and kills it",
             "correct": True},
            {"text": "Warm water dissolves the yeast grains, and boiling "
                     "water would not",
             "correct": False,
             "why": "The grains do not dissolve at all. They are dormant "
                    "cells, and warm water revives them — yeast is a "
                    "living fungus, not a powder that goes into solution."},
            {"text": "Warm water sets off the chemical reaction that releases "
                     "the gas",
             "correct": False,
             "why": "That is baking powder, which is a chemical and works in "
                    "a bowl of anything. Yeast releases the gas by respiring, "
                    "at its own pace, and it has to be alive to do it."},
            {"text": "Boiling water drives off the ethanol, and ethanol is "
                     "what raises dough",
             "correct": False,
             "why": "Carbon dioxide raises the dough; the ethanol is the "
                    "other product and it leaves later, in the oven. And "
                    "nothing has respired yet, so there is no ethanol there "
                    "to drive off."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e04",
        "band": "easier",
        "text": "The bench holds live yeast, sealed, at 30 °C — but "
                "the sugar dial is set to None. What does it report?",
        "options": [
            {"text": "The cells die, because an organism with no food cannot "
                     "survive",
             "correct": False,
             "why": "Not on this bench. Starved is not the same as killed: "
                    "the yeast is alive and unharmed, and it starts work the "
                    "moment sugar arrives. Only the 80 °C setting kills."},
            {"text": "Carbon dioxide but no ethanol, since only ethanol comes "
                     "from sugar",
             "correct": False,
             "why": "Both products come out of the same glucose molecule. No "
                    "sugar means neither of them, not one of them."},
            {"text": "Nothing at all — fermentation is respiration, and "
                     "respiration needs a fuel",
             "correct": True},
            {"text": "A slow trickle of gas, because the yeast can respire "
                     "the water instead",
             "correct": False,
             "why": "Water is not a fuel — there is no energy in it to "
                    "release. Respiration breaks down sugar, and there is "
                    "none in the vessel."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-04-s01",
        "band": "standard",
        "text": "A brewer forgets to seal the vessel, and the pump stirs it "
                "for a week. At the end there is no alcohol in it. What went "
                "wrong?",
        "options": [
            {"text": "The ethanol evaporated away through the open top of the "
                     "vessel",
             "correct": False,
             "why": "There was never any to evaporate. With air available the "
                    "yeast did not take the ethanol route in the first place "
                    "— that is what the seal is for."},
            {"text": "With oxygen available the yeast respired aerobically, "
                     "making water instead",
             "correct": True},
            {"text": "Oxygen stops yeast respiring, so the vessel simply "
                     "stood still all week",
             "correct": False,
             "why": "The opposite happened. With oxygen the yeast grows "
                    "faster than it ever does sealed — full rate, lots "
                    "of new cells. It just makes different products."},
            {"text": "The stirring broke the yeast cells up before they could "
                     "finish",
             "correct": False,
             "why": "Stirring does it no harm. Open, stirred and fed is "
                    "exactly how baker’s yeast is manufactured — "
                    "the organism thrives, which is the whole problem here."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s02",
        "band": "standard",
        "text": "Instead of proving dough somewhere warm for two hours, a "
                "baker leaves it in the fridge all night. It still rises. Why "
                "does that work?",
        "options": [
            {"text": "In the cold the yeast switches to a slower reaction "
                     "that makes no ethanol",
             "correct": False,
             "why": "It is the same reaction throughout — glucose to "
                    "ethanol and carbon dioxide. Temperature changes how fast "
                    "it runs, never what comes out of it."},
            {"text": "The cold kills most of the yeast, and the survivors "
                     "work overnight",
             "correct": False,
             "why": "Cold does not kill. At 4 °C every cell is alive and "
                    "unharmed, just unhurried. Heat is the setting that kills "
                    "on this bench, and that one is permanent."},
            {"text": "The rise is air expanding in the cold dough, not gas "
                     "from the yeast",
             "correct": False,
             "why": "Air already in the dough is the wrong answer the hook "
                    "offers you. The holes are carbon dioxide, released by "
                    "yeast respiring — warm or cold, that is where the "
                    "gas comes from."},
            {"text": "At 4 °C the yeast is alive and unharmed, and "
                     "everything simply happens slowly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s03",
        "band": "standard",
        "text": "A student says a rising loaf and a setting yoghurt are "
                "“completely different processes”. What is the best "
                "reply?",
        "options": [
            {"text": "Both are a micro-organism respiring sugar without "
                     "oxygen — only the organism differs",
             "correct": True},
            {"text": "Agreed — the loaf is a chemical reaction and the "
                     "yoghurt is bacteria growing",
             "correct": False,
             "why": "Nothing in the loaf is a chemical raising agent. Yeast "
                    "is a living fungus, respiring in dough exactly as the "
                    "bacteria are respiring in the milk."},
            {"text": "Agreed — one is respiration, the other is milk "
                     "going off under supervision",
             "correct": False,
             "why": "Yoghurt is not spoiled milk. Particular bacteria are "
                    "added on purpose, and the lactic acid they respire out "
                    "of the sugar is what sets it and what keeps it."},
            {"text": "Not quite — it is the same reaction, so both of "
                     "them release carbon dioxide",
             "correct": False,
             "why": "Same process, not the same reaction. Yeast gives ethanol "
                    "and carbon dioxide; these bacteria give lactic acid and "
                    "no gas at all. The organism decides the product."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s04",
        "band": "standard",
        "text": "A fermenting vessel has an airlock: gas bubbles out through "
                "it, but air cannot get in. Why does it have to work both "
                "ways?",
        "options": [
            {"text": "Ethanol vapour has to get out, and air would react with "
                     "the beer",
             "correct": False,
             "why": "The ethanol is the product — the brewer is keeping "
                    "it, not venting it. What has to leave is the carbon "
                    "dioxide, because the yeast makes more of it than the "
                    "vessel can hold."},
            {"text": "The yeast has to breathe out, and breathing in would "
                     "use the sugar faster",
             "correct": False,
             "why": "Yeast has no lungs and does not breathe — the gas "
                    "is waste from respiring. And air does more than speed "
                    "things up: it moves the yeast onto the aerobic route, "
                    "where there is no ethanol at all."},
            {"text": "Carbon dioxide has to escape, and oxygen would stop the "
                     "yeast making ethanol",
             "correct": True},
            {"text": "Gas has to escape, and cold air would take the vessel "
                     "below its optimum",
             "correct": False,
             "why": "An airlock is not insulation. What it keeps out is "
                    "oxygen, because with oxygen the yeast respires "
                    "aerobically and the product you wanted never appears."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-04-h01",
        "band": "harder",
        "text": "A company grows genetically modified yeast in a huge tank to "
                "make human insulin. Air is bubbled through it and it is "
                "stirred hard — the opposite of a brewery. Why?",
        "options": [
            {"text": "Oxygen is what switches on the inserted human gene in "
                     "each cell",
             "correct": False,
             "why": "Nothing turns the gene on and off with oxygen. The air "
                    "is there for the organism’s respiration, not for "
                    "the gene it is carrying."},
            {"text": "Without air the yeast would make ethanol, which would "
                     "spoil the medicine",
             "correct": False,
             "why": "Ethanol would be a nuisance, but that is not what the "
                    "air is for. The tank is aerated to grow yeast fast: more "
                    "cells means more insulin."},
            {"text": "The bubbling stops the tank overheating as the yeast "
                     "respires",
             "correct": False,
             "why": "Big fermenters are cooled deliberately, and not by the "
                    "air line. The air is there to hold the yeast on the "
                    "aerobic route, where it grows fastest."},
            {"text": "The insulin comes from the cells, and yeast with air "
                     "grows fastest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h02",
        "band": "harder",
        "text": "A vessel of yeast is held at 80 °C for an hour. It is "
                "then cooled to 30 °C and sugar is stirred in. What "
                "happens next?",
        "options": [
            {"text": "It ferments normally now, because both bad settings "
                     "have been put right",
             "correct": False,
             "why": "One of the two was permanent. At 80 °C the enzymes "
                    "are denatured, and cooling never puts a denatured enzyme "
                    "back — the same permanent change you met in Enzymes "
                    "in digestion."},
            {"text": "Nothing. The heat denatured its enzymes, and cooling "
                     "cannot undo that",
             "correct": True},
            {"text": "It ferments slowly at first, then speeds up as the "
                     "cells recover",
             "correct": False,
             "why": "Slow-then-faster is what cold does — at 4 °C a "
                    "yeast is alive and simply unhurried. Heat is a different "
                    "thing altogether: the cells are dead, and dead cells do "
                    "not recover."},
            {"text": "It makes carbon dioxide but no ethanol, because heat "
                     "spoiled one route",
             "correct": False,
             "why": "There are not two separate routes inside the yeast to "
                    "damage one at a time. Both products come from the one "
                    "reaction, and a dead cell runs none of it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h03",
        "band": "harder",
        "text": "Two jars of warm milk get the same yoghurt bacteria. One is "
                "sealed; the other is left open and stirred. The open jar "
                "never sets, and spoils within a day. Which explanation "
                "covers both?",
        "options": [
            {"text": "Oxygen is poisonous to these bacteria, so they die and "
                     "leave the milk plain",
             "correct": False,
             "why": "Air does not kill them — they simply do their work "
                    "without it, and work badly with it. What ruins the jar "
                    "is that nothing useful is made while everything else in "
                    "the room is invited in."},
            {"text": "The stirring breaks the curd up as fast as it forms, so "
                     "it cannot set",
             "correct": False,
             "why": "Leave the open jar perfectly still and it still fails. "
                    "The problem is the conditions the bacteria are in, not "
                    "the spoon."},
            {"text": "Little usable acid forms, the pH never falls, and other "
                     "organisms get in",
             "correct": True},
            {"text": "With oxygen they make ethanol instead of lactic acid, "
                     "and that will not set milk",
             "correct": False,
             "why": "That is the yeast route, and no dial turns one organism "
                    "into another. These bacteria make lactic acid or they "
                    "make nothing you could use."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h04",
        "band": "harder",
        "text": "The bench reads: yoghurt bacteria, sealed vessel, 4 °C, "
                "sugar supplied — rate 12% of maximum. Which product "
                "panel goes with that?",
        "options": [
            {"text": "Lactic acid 12 units, and no gas — this route "
                     "makes none",
             "correct": True},
            {"text": "Lactic acid 12 units, and carbon dioxide 12 units "
                     "alongside it",
             "correct": False,
             "why": "The gas row is the giveaway. Glucose to lactic acid is "
                    "the whole reaction for these bacteria — there is no "
                    "second product to read off, at any temperature."},
            {"text": "No lactic acid — at 4 °C the cells are too "
                     "cold to work",
             "correct": False,
             "why": "Cold is slow, not stopped. Twelve per cent of maximum is "
                    "a real rate, and it is exactly why a finished yoghurt "
                    "goes on souring gently in the fridge."},
            {"text": "Ethanol 12 units and carbon dioxide 12 units, as yeast "
                     "gives",
             "correct": False,
             "why": "That is what the yeast setting would give you. Changing "
                    "the temperature changes the rate; only changing the "
                    "organism changes the products."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-04-e05",
        "band": "easier",
        "text": "What kind of organism is yeast?",
        "options": [
            {"text": "A chemical powder that reacts as soon as it is wetted.",
             "correct": False,
             "why": "That is baking powder. Yeast is alive — dried yeast is "
                    "dormant cells, which is why warm water revives it and "
                    "boiling water kills it."},
            {"text": "A living, single-celled fungus that respires sugar.",
             "correct": True},
            {"text": "A bacterium, like the ones that turn milk into yoghurt "
                     "or cheese.",
             "correct": False,
             "why": "Both are micro-organisms and both ferment, but they are "
                    "different kinds of living thing — and they take "
                    "different routes, giving different products."},
            {"text": "A tiny green plant that makes its own food from light.",
             "correct": False,
             "why": "Yeast has no chlorophyll and cannot photosynthesise. It "
                    "lives on sugar supplied to it, which is why a vessel "
                    "with no sugar in it produces nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e06",
        "band": "easier",
        "text": "Which gas makes a ball of bread dough rise?",
        "options": [
            {"text": "Carbon dioxide", "correct": True},
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen is the thing the yeast in the middle of a dough "
                    "ball does not have. It is not a product of fermentation "
                    "at all."},
            {"text": "Ethanol", "correct": False,
             "why": "Ethanol is the other product, but in the dough it is a "
                    "liquid and it leaves later, in the oven. The holes are "
                    "carbon dioxide."},
            {"text": "Hydrogen", "correct": False,
             "why": "No respiration of any kind produces hydrogen gas. Yeast "
                    "gives ethanol and carbon dioxide, and it is the carbon "
                    "dioxide you can see."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e07",
        "band": "easier",
        "text": "Fermentation is another name for what?",
        "options": [
            {"text": "Food decaying slowly, under conditions that keep it "
                     "safe.",
             "correct": False,
             "why": "Decay is whatever happens to land on the food growing on "
                    "it. Fermentation is one chosen micro-organism, given the "
                    "conditions it likes, doing a reaction we want."},
            {"text": "A reaction between an acid and an alkali inside the "
                     "food.",
             "correct": False,
             "why": "Nothing is neutralised and no acid is added. The acid, "
                    "or the alcohol, is made by a living organism out of the "
                    "sugar."},
            {"text": "Aerobic respiration carried out by micro-organisms.",
             "correct": False,
             "why": "Half right — respiration by micro-organisms, but the "
                    "anaerobic route. Give the vessel air and yeast makes "
                    "carbon dioxide and water instead."},
            {"text": "Anaerobic respiration carried out by micro-organisms.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e08",
        "band": "easier",
        "text": "Which of these foods is made using lactic acid bacteria?",
        "options": [
            {"text": "Beer", "correct": False,
             "why": "Beer is yeast's work, and what the brewer wants from it "
                    "is the ethanol. Lactic acid bacteria produce no alcohol "
                    "at all."},
            {"text": "Bread", "correct": False,
             "why": "Bread is yeast as well, and it is the carbon dioxide "
                    "that raises the loaf. The bacteria's route makes no gas "
                    "to raise anything with."},
            {"text": "Yoghurt", "correct": True},
            {"text": "Cider", "correct": False,
             "why": "Cider is apple juice fermented by yeast, giving ethanol "
                    "and carbon dioxide. These bacteria give lactic acid "
                    "instead."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e09",
        "band": "easier",
        "text": "A baker and a brewer both use yeast, and yeast makes two "
                "products. Which product does each of them want?",
        "options": [
            {"text": "Both want the ethanol; the baker's simply bakes away "
                     "again.",
             "correct": False,
             "why": "The baker never wanted the ethanol. It is the gas that "
                    "raises the loaf, and the ethanol leaving in the oven is "
                    "a side effect."},
            {"text": "The baker wants the carbon dioxide; the brewer wants "
                     "the ethanol.",
             "correct": True},
            {"text": "The baker wants the ethanol; the brewer wants the "
                     "carbon dioxide.",
             "correct": False,
             "why": "The right two products, swapped over. The gas is what "
                    "raises dough, and the ethanol is what makes beer beer."},
            {"text": "Both want the carbon dioxide, and the ethanol is waste "
                     "to each of them.",
             "correct": False,
             "why": "The ethanol is exactly what a brewer is after. Only the "
                    "baker treats it as something to be rid of."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-e10",
        "band": "easier",
        "text": "Which of these does fermentation not need?",
        "options": [
            {"text": "Sugar for the organism to respire.", "correct": False,
             "why": "With no sugar nothing happens at all. A starved yeast is "
                    "alive and idle, because respiration must have a fuel."},
            {"text": "A living micro-organism.", "correct": False,
             "why": "The organism is what does the respiring. Kill it and the "
                    "vessel produces nothing, permanently."},
            {"text": "A temperature the organism can survive at.",
             "correct": False,
             "why": "Above the optimum the enzymes are denatured and the "
                    "organism dies, and the vessel then produces nothing at "
                    "all, permanently."},
            {"text": "Light for the organism to work by.", "correct": True},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-04-s05",
        "band": "standard",
        "text": "Bread recipes say to leave the dough somewhere warm, never "
                "somewhere as hot as possible. Why not hotter?",
        "options": [
            {"text": "Because the heat would drive the carbon dioxide out "
                     "before the dough could rise.",
             "correct": False,
             "why": "The gas is trapped in the dough as it forms. What too "
                    "much heat does is kill the organism that is making it."},
            {"text": "Because heat makes yeast produce lactic acid instead of "
                     "carbon dioxide.",
             "correct": False,
             "why": "Temperature changes the rate, never the products. Only "
                    "changing the organism changes what comes out."},
            {"text": "Because above its optimum the yeast's enzymes are "
                     "denatured and it dies.",
             "correct": True},
            {"text": "Because the dough would rise too fast to be shaped in "
                     "time.",
             "correct": False,
             "why": "Bakers do control the speed, but that is convenience "
                    "rather than chemistry. Too hot and there is no rise at "
                    "all, because the yeast is dead."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s06",
        "band": "standard",
        "text": "Sourdough is made from flour, water and time, with no yeast "
                "added at all — and it still rises. What must be happening?",
        "options": [
            {"text": "Micro-organisms in the flour and air respire the "
                     "sugars.",
             "correct": True},
            {"text": "The flour reacts with the water, giving off gas that "
                     "acts as a raising agent.",
             "correct": False,
             "why": "Flour and water produce no gas between them. Something "
                    "living has to respire the sugars, and in sourdough it "
                    "arrived by itself."},
            {"text": "Air folded in during kneading expands slowly over the "
                     "hours.",
             "correct": False,
             "why": "Kneading does fold air in, but trapped air does not "
                    "increase. The holes grow because gas is being made "
                    "inside them."},
            {"text": "Water can ferment sugars on its own if it is left long "
                     "enough.",
             "correct": False,
             "why": "Fermentation is respiration, and respiration needs a "
                    "living organism. Water does nothing on its own however "
                    "long it stands."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s07",
        "band": "standard",
        "text": "A bottle of home-made ginger beer is sealed with sugar and "
                "live yeast still in it and left somewhere warm. Why can it "
                "burst?",
        "options": [
            {"text": "The ethanol expands as it warms and forces the bottle "
                     "apart.",
             "correct": False,
             "why": "The liquid barely expands at all. What builds the "
                    "pressure is a gas being produced continuously inside a "
                    "sealed container."},
            {"text": "The yeast goes on growing until the cells fill the "
                     "bottle.",
             "correct": False,
             "why": "The cells stay a tiny fraction of the volume. The "
                    "pressure comes from the carbon dioxide they release, not "
                    "from the cells."},
            {"text": "Warmth makes the yeast switch to a reaction that gives "
                     "more gas.",
             "correct": False,
             "why": "The reaction does not change with temperature; only its "
                    "rate does. Warmth makes the same gas arrive faster."},
            {"text": "The yeast keeps fermenting, and the carbon dioxide has "
                     "nowhere to go.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s08",
        "band": "standard",
        "text": "A wine maker adds sugar to grape juice that is not sweet "
                "enough. Why does that raise the alcohol in the finished "
                "wine?",
        "options": [
            {"text": "Sugar turns into alcohol on its own once it dissolves "
                     "in the juice.",
             "correct": False,
             "why": "Nothing happens to it without the yeast. The sugar is "
                    "the fuel a living organism respires, and ethanol is what "
                    "that leaves behind."},
            {"text": "More sugar gives the yeast more to respire, and ethanol "
                     "is one product.",
             "correct": True},
            {"text": "Sugar makes the yeast work faster, so it uses up less "
                     "of the alcohol.",
             "correct": False,
             "why": "The yeast does not consume the ethanol at all. It is a "
                    "product being got rid of, not a store being kept."},
            {"text": "Sugar keeps oxygen out of the juice, which is what "
                     "allows ethanol.",
             "correct": False,
             "why": "Keeping oxygen out is the sealed vessel's job, not the "
                    "sugar's. The sugar's job is to be the fuel."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s09",
        "band": "standard",
        "text": "Some cakes are raised with baking powder and some breads "
                "with yeast. What is the essential difference between the "
                "two?",
        "options": [
            {"text": "Baking powder gives off carbon dioxide, and yeast gives "
                     "off oxygen.",
             "correct": False,
             "why": "Yeast gives carbon dioxide too — that is what raises the "
                    "loaf. Neither of them releases any oxygen."},
            {"text": "Baking powder has to be warmed, while yeast works at "
                     "any temperature.",
             "correct": False,
             "why": "Both halves are the wrong way round. Yeast is the fussy "
                    "one precisely because it is alive: cold slows it and "
                    "heat kills it."},
            {"text": "Baking powder is a chemical; yeast is alive and raises "
                     "dough by respiring.",
             "correct": True},
            {"text": "Baking powder produces alcohol as well, which is why "
                     "cakes taste different.",
             "correct": False,
             "why": "It produces none. Ethanol is yeast's second product, and "
                    "it takes a living organism to make it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-s10",
        "band": "standard",
        "text": "Ethanol for fuel is made by fermenting sugar cane. Which "
                "product is wanted, and what happens to the other one?",
        "options": [
            {"text": "The ethanol is wanted, and the carbon dioxide escapes "
                     "as a gas.",
             "correct": True},
            {"text": "The carbon dioxide is wanted, and the ethanol is burned "
                     "off first.",
             "correct": False,
             "why": "The whole point of the process is the liquid fuel. The "
                    "gas is released and is of no use here."},
            {"text": "Both are wanted, because ethanol and carbon dioxide "
                     "both burn well.",
             "correct": False,
             "why": "Carbon dioxide does not burn — it is one of the things "
                    "burning produces. Only the ethanol is a fuel."},
            {"text": "The ethanol is wanted, and the lactic acid has to be "
                     "removed.",
             "correct": False,
             "why": "Lactic acid comes from the bacterial route, and this is "
                    "yeast. Yeast's two products are ethanol and carbon "
                    "dioxide."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-04-h05",
        "band": "harder",
        "text": "At 30 °C a fermenting vessel releases 60 cm³ of carbon "
                "dioxide a minute. Cooled to 4 °C the rate falls to 12% of "
                "that. What is the rate at 4 °C?",
        "options": [
            {"text": "0 cm³ per minute", "correct": False,
             "why": "Cold slows fermentation; it does not stop it. Twelve per "
                    "cent of 60 is a real rate, which is why a yoghurt goes "
                    "on souring gently in a fridge."},
            {"text": "52.8 cm³ per minute", "correct": False,
             "why": "That is 60 with 12% taken off it. The question asks for "
                    "12% of the rate, which is 60 × 0.12."},
            {"text": "7.2 cm³ per minute", "correct": True},
            {"text": "500 cm³ per minute", "correct": False,
             "why": "That is 60 ÷ 0.12, dividing where you should multiply. "
                    "Cooling a vessel cannot make it faster."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h06",
        "band": "harder",
        "text": "Yeast and your own muscles both respire without oxygen. "
                "Which difference between the two matters most to a baker?",
        "options": [
            {"text": "Yeast gets more energy out of each glucose molecule "
                     "than your muscles do.",
             "correct": False,
             "why": "Both routes give far less than the aerobic one, and "
                    "neither yield is any use to a baker. What a baker needs "
                    "is a gas."},
            {"text": "Yeast produces a gas; human muscle produces lactic acid "
                     "and no gas.",
             "correct": True},
            {"text": "Yeast can respire without any sugar, and human muscle "
                     "cannot.",
             "correct": False,
             "why": "Neither can. Take the sugar away and a yeast makes "
                    "nothing at all, however right everything else is."},
            {"text": "Yeast respires only when warm; muscle respires at any "
                     "temperature.",
             "correct": False,
             "why": "Warmth changes yeast's rate, not whether it respires. "
                    "And rate is not what raises a loaf — the gas is."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h07",
        "band": "harder",
        "text": "Kimchi is made by covering cabbage in salt and leaving it, "
                "with no bacteria added from a packet. Where do the bacteria "
                "come from, and what is the salt for?",
        "options": [
            {"text": "The salt makes the acid, and the bacteria only add the "
                     "flavour.",
             "correct": False,
             "why": "The acid is made by bacteria respiring the sugars in the "
                    "cabbage. Salt produces none of it."},
            {"text": "The bacteria arrive in the salt, which also holds the "
                     "jar at the right pH.",
             "correct": False,
             "why": "Salt carries no bacteria and sets no pH. The pH falls "
                    "because lactic acid is being made inside the jar."},
            {"text": "The bacteria come from the air, and the salt kills them "
                     "off slowly.",
             "correct": False,
             "why": "If the salt killed them the jar would never ferment. It "
                    "holds back the organisms that would spoil the cabbage, "
                    "and the useful ones survive it."},
            {"text": "They are already on the leaves, and the salt holds back "
                     "the spoilage organisms.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h08",
        "band": "harder",
        "text": "A yoghurt maker heats the milk to near boiling, cools it to "
                "about 40 °C, and only then stirs in the culture. Explain "
                "both steps.",
        "options": [
            {"text": "Heating kills what was in the milk; cooling spares the "
                     "culture.",
             "correct": True},
            {"text": "Heating starts the souring reaction, and cooling slows "
                     "it so the yoghurt sets gently.",
             "correct": False,
             "why": "Heat starts nothing — the bacteria do that when they "
                    "arrive. The boiling is there to clear the milk of "
                    "everything else."},
            {"text": "Heating thickens the milk, and cooling makes that "
                     "thickening permanent.",
             "correct": False,
             "why": "What thickens milk is lactic acid curdling its protein, "
                    "and none has been made at that stage."},
            {"text": "Heating drives the oxygen out, and cooling keeps it out "
                     "for the bacteria.",
             "correct": False,
             "why": "The lid deals with the oxygen. Boiling is about what is "
                    "living in the milk, and cooling is about not killing "
                    "what you are about to add."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h09",
        "band": "harder",
        "text": "Two loaves use the same dough. One is proved for one hour at "
                "30 °C, the other for eight hours at 4 °C, and both rise the "
                "same amount. How is that possible?",
        "options": [
            {"text": "In the cold the yeast switches to a slower reaction "
                     "that gives more gas per cell.",
             "correct": False,
             "why": "There is no second reaction to switch to. The same one "
                    "runs more slowly, and the extra hours make up the "
                    "difference."},
            {"text": "Cold dough traps the gas better, so less of it has to "
                     "be produced.",
             "correct": False,
             "why": "Cold dough is stiffer, but the rise still measures gas "
                    "made. The cold batch simply had eight times as long to "
                    "make it."},
            {"text": "The rate is far lower but the time is far longer, so "
                     "the total gas is similar.",
             "correct": True},
            {"text": "Only the warm loaf really ferments; the cold one rises "
                     "as the dough relaxes.",
             "correct": False,
             "why": "At 4 °C the yeast is alive and working, just unhurried. "
                    "The holes in an overnight loaf are carbon dioxide, "
                    "exactly as in the warm one."},
        ],
        "figure": None,
    },
    {
        "id": "b8-04-h10",
        "band": "harder",
        "text": "Fermentation produces alcohol or acid rather than carbon "
                "dioxide and water. Justify calling it respiration all the "
                "same.",
        "options": [
            {"text": "Because the yeast breathes in through its membrane "
                     "while the reaction runs.",
             "correct": False,
             "why": "Yeast does not breathe, and breathing is not respiration "
                    "in any organism. What makes this respiration is what "
                    "happens to the glucose."},
            {"text": "Because energy is released from glucose inside a living "
                     "cell, without oxygen.",
             "correct": True},
            {"text": "Because the products can be burned to release energy "
                     "later on.",
             "correct": False,
             "why": "Ethanol does burn, which shows energy was left in it — "
                    "but burning it later is not what the organism did. The "
                    "yeast released energy for itself."},
            {"text": "Because the reaction gives off a gas, just as aerobic "
                     "respiration does.",
             "correct": False,
             "why": "The bacterial route gives off no gas at all and is still "
                    "respiration. What counts is energy released from glucose "
                    "in a living cell."},
        ],
        "figure": None,
    },
]

_MRB338_NEW_QUESTIONS = [
    {
        "id": 'b8-04-e11',
        "band": 'easier',
        "text": 'What is fermentation?',
        "options": [
            {"text": 'Anaerobic respiration carried out by a micro-organism.', "correct": True},
            {"text": 'Aerobic respiration carried out by a micro-organism.', "correct": False,
             "why": 'Fermentation is specifically the anaerobic route; the aerobic route is not called fermentation.'},
            {"text": 'Food decaying under uncontrolled conditions.', "correct": False,
             "why": 'Fermentation uses one chosen, deliberately added organism; decay is uncontrolled spoilage by whatever organism happens to land there.'},
            {"text": 'A chemical reaction between an acid and an alkali.', "correct": False,
             "why": 'That is neutralisation, an entirely different kind of reaction with no living organism involved.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e12',
        "band": 'easier',
        "text": 'What is the word summary for yoghurt bacteria fermenting glucose?',
        "options": [
            {"text": 'Glucose gives ethanol and carbon dioxide.', "correct": False,
             "why": "That is yeast's route; the bacteria in yoghurt make lactic acid instead."},
            {"text": 'Glucose gives carbon dioxide and water.', "correct": False,
             "why": "Those are aerobic products, not the bacteria's anaerobic ones."},
            {"text": 'Glucose gives lactic acid.', "correct": True},
            {"text": 'Glucose and oxygen give lactic acid.', "correct": False,
             "why": "These bacteria's fermentation needs no oxygen at all; adding it here is wrong."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e13',
        "band": 'easier',
        "text": 'Why does a baker use warm water rather than boiling water to activate dried yeast?',
        "options": [
            {"text": 'Boiling water evaporates too quickly to mix with the flour.', "correct": False,
             "why": 'Evaporation speed is not the issue; the real problem is that boiling water kills the living yeast.'},
            {"text": 'Warm water dissolves the yeast better than hot water.', "correct": False,
             "why": 'Dissolving is not the reason; hot water would dissolve yeast at least as well — the issue is that it kills it.'},
            {"text": 'Boiling water reacts chemically with the sugar in the dough.', "correct": False,
             "why": 'There is no such reaction; the issue is that boiling water kills the living yeast cells.'},
            {"text": "Boiling water denatures the yeast's enzymes and kills it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e14',
        "band": 'easier',
        "text": 'Which of these does fermentation need in order to happen?',
        "options": [
            {"text": 'A living micro-organism and a sugar for it to respire.', "correct": True},
            {"text": 'Light, so the organism can photosynthesise first.', "correct": False,
             "why": 'Fermentation is respiration, not photosynthesis; no light is needed.'},
            {"text": 'A constant supply of oxygen.', "correct": False,
             "why": 'Fermentation is anaerobic; it happens without oxygen, not because of it.'},
            {"text": 'A strong acid to start the reaction off.', "correct": False,
             "why": 'No acid is needed to start fermentation; a living organism and a sugar are enough.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e15',
        "band": 'easier',
        "text": 'Yeast fermenting sugar makes two products at once. A baker keeps one of them and a brewer keeps the other. Which keeps which?',
        "options": [
            {"text": 'The baker wants the ethanol; the brewer wants the carbon dioxide.', "correct": False,
             "why": 'That is the two swapped round — bread rises on the gas, and beer is made from the alcohol.'},
            {"text": 'The baker wants the carbon dioxide; the brewer wants the ethanol.', "correct": True},
            {"text": 'Both want the ethanol, and the gas is wasted in both cases.', "correct": False,
             "why": 'The baker specifically wants the gas, to raise the dough; only the brewer is after the ethanol.'},
            {"text": 'Both want the carbon dioxide, and the ethanol is wasted in both cases.', "correct": False,
             "why": 'The brewer specifically wants the ethanol; only the baker is after the gas.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e16',
        "band": 'easier',
        "text": 'How does warm milk become yoghurt?',
        "options": [
            {"text": 'Heat alone curdles the milk protein directly.', "correct": False,
             "why": 'Heat alone does not make yoghurt; it is the lactic acid made by the bacteria that curdles the milk.'},
            {"text": "The milk's own sugar slowly turns into protein over several days on its own.", "correct": False,
             "why": 'Sugar does not turn into protein; bacteria ferment the sugar into lactic acid, which then curdles the protein already there.'},
            {"text": 'Bacteria ferment the sugar in milk, making lactic acid that curdles it.', "correct": True},
            {"text": 'Cooling the milk suddenly and immediately thickens it into a finished yoghurt on its own.', "correct": False,
             "why": 'Cooling alone does not make yoghurt; fermentation by bacteria over time does.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e17',
        "band": 'easier',
        "text": 'A vessel of yeast is heated to 80 °C and then cooled back down. Does it ferment again?',
        "options": [
            {"text": 'Yes — cooling it back down restarts the fermentation.', "correct": False,
             "why": 'The damage from 80 °C is permanent; cooling cannot undo denatured enzymes or bring dead cells back.'},
            {"text": 'Yes, but only after being reheated a second time to reactivate whatever survived the first heating.', "correct": False,
             "why": 'Reheating cannot repair enzymes that have already been permanently denatured.'},
            {"text": 'No, but only until fresh sugar is added.', "correct": False,
             "why": 'Adding sugar makes no difference; the yeast itself has been permanently killed by the heat.'},
            {"text": "No — the heat permanently denatured the yeast's enzymes and killed it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e18',
        "band": 'easier',
        "text": 'A sealed vessel has healthy yeast, warmth, and no oxygen, but no sugar at all. Does fermentation happen?',
        "options": [
            {"text": 'No — fermentation is respiration, and respiration needs a substrate to respire.', "correct": True},
            {"text": 'Yes — yeast can ferment its own cell contents instead.', "correct": False,
             "why": 'Yeast does not respire its own body; without an external sugar supply, nothing is fermented.'},
            {"text": 'Yes, but only very slowly, taking several days to use up whatever tiny trace of sugar remains.', "correct": False,
             "why": 'Without any sugar at all, no fermentation happens, however long it is left.'},
            {"text": 'No, because a yeast cell with nothing at all to respire counts as dead for every practical purpose.', "correct": False,
             "why": 'The yeast is alive and unharmed; it simply has nothing to respire, which is a different situation from being dead.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e19',
        "band": 'easier',
        "text": 'Yeast is grown in an open, stirred, oxygenated tank rather than a sealed one. What happens?',
        "options": [
            {"text": 'It ferments even faster than it would in an identical sealed vessel with no oxygen at all.', "correct": False,
             "why": 'With oxygen available, yeast switches to aerobic respiration rather than fermenting faster.'},
            {"text": 'It respires aerobically, grows quickly, and makes no ethanol.', "correct": True},
            {"text": 'It stops respiring altogether because of the oxygen.', "correct": False,
             "why": 'Oxygen does not stop yeast respiring; it lets it switch to the aerobic route instead.'},
            {"text": 'It makes ethanol and carbon dioxide even faster.', "correct": False,
             "why": 'With oxygen available, yeast respires aerobically and makes no ethanol at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e20',
        "band": 'easier',
        "text": 'Yoghurt bacteria are left in an open, stirred vessel of milk rather than a sealed one. What is the result?',
        "options": [
            {"text": 'Perfect yoghurt forms even faster than usual, since stirring helps the bacteria spread through the milk.', "correct": False,
             "why": 'An open, stirred vessel invites in other organisms and does not favour these bacteria; it does not speed up yoghurt-making.'},
            {"text": 'The bacteria make ethanol instead of lactic acid.', "correct": False,
             "why": 'These bacteria do not switch to making ethanol; the problem is contamination and poor conditions, not a different product.'},
            {"text": 'Poor conditions — no usable lactic acid forms, and the milk does not set.', "correct": True},
            {"text": 'Nothing at all changes compared with an identical, properly sealed vessel kept at the same temperature.', "correct": False,
             "why": 'An open, stirred vessel is a real problem for these bacteria — it invites contamination, unlike a sealed one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e21',
        "band": 'easier',
        "text": 'A ball of dough is left in the fridge overnight instead of on a warm shelf. What happens to the yeast?',
        "options": [
            {"text": 'It dies from the cold within a few hours.', "correct": False,
             "why": 'Cold does not kill yeast the way heat does; it simply slows the fermentation down.'},
            {"text": 'It ferments at exactly the same rate as it would sitting out on a warm shelf all night.', "correct": False,
             "why": 'Cold slows the rate of fermentation considerably; it does not leave the rate unchanged.'},
            {"text": 'It stops respiring completely until it is warmed up.', "correct": False,
             "why": 'Yeast in the fridge keeps respiring, just very slowly, rather than stopping altogether.'},
            {"text": 'It stays alive and ferments, but much more slowly than in the warm.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e22',
        "band": 'easier',
        "text": 'Why does a fermenting vessel have an airlock rather than an open lid?',
        "options": [
            {"text": 'It lets carbon dioxide escape while keeping oxygen from getting in.', "correct": True},
            {"text": 'It lets oxygen in to help the yeast respire faster.', "correct": False,
             "why": 'The airlock is there to keep oxygen out, not to let it in; oxygen would push the yeast off the fermenting route.'},
            {"text": 'It lets the ethanol evaporate out of the vessel while the reaction is still running.', "correct": False,
             "why": "Keeping the ethanol in the vessel is usually the point; the airlock's job is releasing gas while blocking air."},
            {"text": 'It stops any gas at all from ever escaping the sealed fermenting vessel.', "correct": False,
             "why": 'The airlock is specifically designed to let gas escape, while stopping air getting in.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e23',
        "band": 'easier',
        "text": 'Most insulin used today is made how?',
        "options": [
            {"text": 'Extracted from the pancreases of pigs and cattle slaughtered for meat.', "correct": False,
             "why": 'That was the older method; almost all insulin today comes from genetically modified micro-organisms instead.'},
            {"text": 'By micro-organisms carrying an inserted human gene, grown in fermenters.', "correct": True},
            {"text": 'Synthesised directly from sugar with no living organism involved.', "correct": False,
             "why": 'A living, genetically modified organism does the making; it is not built directly from sugar with no organism at all.'},
            {"text": 'Extracted from a genetically modified plant.', "correct": False,
             "why": 'The organisms used are micro-organisms, such as bacteria or yeast, not plants.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e24',
        "band": 'easier',
        "text": 'A sourdough loaf rises with no yeast added by the baker at all. What made the gas?',
        "options": [
            {"text": 'A chemical reaction between the flour and the water alone.', "correct": False,
             "why": 'Flour and water do not react chemically to make gas; living micro-organisms already present are respiring.'},
            {"text": 'Air folded into the dough during kneading, expanding in the oven.', "correct": False,
             "why": 'The rise comes from a gas made by fermentation over time, not simply from air trapped while kneading.'},
            {"text": 'Wild micro-organisms already present in the flour and the air.', "correct": True},
            {"text": 'The water itself fermenting on its own, without any organism.', "correct": False,
             "why": 'Water cannot ferment on its own; a living micro-organism has to be present to do it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e25',
        "band": 'easier',
        "text": 'How does a fermented food differ from food that has simply gone off?',
        "options": [
            {"text": 'A fermented food has one chosen organism added deliberately, under chosen conditions.', "correct": True},
            {"text": 'A fermented food has had all its micro-organisms removed.', "correct": False,
             "why": 'Fermentation deliberately adds a living organism; it does not remove micro-organisms.'},
            {"text": 'Food that has gone off contains no micro-organisms at all.', "correct": False,
             "why": 'Spoiled food is full of micro-organisms; the difference is that fermentation uses one chosen organism, not none at all.'},
            {"text": 'There is no real difference between the two.', "correct": False,
             "why": 'Fermentation is a deliberately controlled process with a chosen organism, unlike random, uncontrolled spoilage.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e26',
        "band": 'easier',
        "text": 'A brewer and a baker start with identical yeast and sugar. Why do they end up with such different products?',
        "options": [
            {"text": 'They actually use two different reactions in yeast.', "correct": False,
             "why": 'It is the same fermentation reaction in both cases; what differs is which product each maker chooses to keep.'},
            {"text": 'They keep or release different products from the same reaction.', "correct": True},
            {"text": "The baker's yeast makes only gas, and the brewer's yeast makes only ethanol.", "correct": False,
             "why": 'The same yeast makes both products at once in each case; the difference is which one is captured and used.'},
            {"text": 'The temperature used is different in each case, which changes the products.', "correct": False,
             "why": 'Both can ferment at similar temperatures; the difference in the final product is which one is kept, not the temperature.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e27',
        "band": 'easier',
        "text": 'How does baking powder differ from yeast as a raising agent?',
        "options": [
            {"text": 'Baking powder is alive, just like yeast.', "correct": False,
             "why": 'Baking powder is a chemical mixture; it is not a living organism at all.'},
            {"text": 'Yeast produces gas by a purely chemical reaction with no organism involved.', "correct": False,
             "why": 'Yeast is a living organism, and its gas comes from respiration, not from a purely chemical reaction.'},
            {"text": 'Baking powder is a chemical; yeast is a living organism that respires.', "correct": True},
            {"text": 'There is no real difference; both work by the same process.', "correct": False,
             "why": 'Baking powder releases gas by a chemical reaction; yeast releases gas by respiring as a living organism.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e28',
        "band": 'easier',
        "text": 'A company grows genetically modified yeast to make a human protein and keeps the tank well aerated throughout. Why?',
        "options": [
            {"text": 'Aerating it makes the yeast ferment the sugar faster.', "correct": False,
             "why": 'Aeration pushes the yeast towards the aerobic route rather than fermenting; that is the whole point of keeping it aerated.'},
            {"text": 'Without air the yeast would die within minutes.', "correct": False,
             "why": 'Yeast survives perfectly well without air, respiring anaerobically instead; the aeration here is about growth rate, not survival.'},
            {"text": 'The air reacts directly with the sugar to release the protein.', "correct": False,
             "why": "Air does not react with sugar to release protein; the protein comes from the yeast's own genetically modified biology as it grows."},
            {"text": 'Aerating it keeps the yeast respiring aerobically, growing fast and making the protein efficiently.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e29',
        "band": 'easier',
        "text": 'Two batches of wine are made from the same grapes, but one has extra sugar stirred in before fermenting. That batch ends up stronger. Explain why.',
        "options": [
            {"text": 'More sugar gives the yeast more to ferment, producing more ethanol.', "correct": True},
            {"text": 'Sugar makes the yeast use less oxygen overall.', "correct": False,
             "why": 'The amount of sugar does not change how much oxygen the yeast uses; it changes how much ethanol can be made.'},
            {"text": 'Sugar keeps the mixture at a steady temperature during fermentation.', "correct": False,
             "why": 'Sugar is the fuel being fermented, not something that controls temperature.'},
            {"text": 'Sugar stops unwanted bacteria from growing in the juice.', "correct": False,
             "why": 'Extra sugar does not stop bacteria growing; it is fermented by the yeast to make more ethanol.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-e30',
        "band": 'easier',
        "text": 'Which of these is made using fermentation?',
        "options": [
            {"text": 'Fresh milk straight from the cow.', "correct": False,
             "why": 'Fresh milk has not been fermented at all; cheese is milk that has been fermented and processed.'},
            {"text": 'Cheese.', "correct": True},
            {"text": 'Table salt.', "correct": False,
             "why": 'Salt is a mineral with no living organism or fermentation involved in making it.'},
            {"text": 'Fresh orange juice, straight from the fruit.', "correct": False,
             "why": 'Fresh juice has not fermented; fermenting it would make something like cider, not fresh juice.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s11',
        "band": 'standard',
        "text": 'A student argues that since fermentation is anaerobic, and anaerobic means not breathing, fermentation must therefore be a kind of breathing. Explain the flaw.',
        "options": [
            {"text": 'Fermentation is a chemical reaction inside cells, not breathing, which is the separate process of moving air.', "correct": True},
            {"text": 'The student is right; fermentation and breathing are the same process viewed two ways.', "correct": False,
             "why": "Breathing moves air in and out of lungs; fermentation is a chemical reaction inside a micro-organism's cells."},
            {"text": 'The flaw is that fermentation actually needs oxygen, unlike breathing.', "correct": False,
             "why": 'Fermentation specifically needs no oxygen; the real flaw is treating a chemical reaction as if it were breathing.'},
            {"text": 'There is no flaw; every anaerobic process is a form of breathing.', "correct": False,
             "why": 'No anaerobic process is a form of breathing; breathing is gas exchange, unrelated to what happens inside a cell.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s12',
        "band": 'standard',
        "text": "A brewer's notes say ‘glucose gives ethanol + carbon dioxide + heat’. A student says heat should not be listed. Are they right?",
        "options": [
            {"text": 'No — heat genuinely is one of the three separate products this reaction makes, alongside ethanol and the gas.', "correct": False,
             "why": 'Heat is energy being released, not a substance the reaction produces; it is never written as a product.'},
            {"text": 'Yes — heat is released, not a substance made, so it is never listed as a product.', "correct": True},
            {"text": 'No, but only because it should be written on the left instead.', "correct": False,
             "why": 'Fermentation does not need heat supplied to start it; heat is released by the reaction, not put into it.'},
            {"text": 'Yes, but only because oxygen should be added on the left instead.', "correct": False,
             "why": 'Fermentation uses no oxygen at all; that would be a separate and larger error than the heat one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s13',
        "band": 'standard',
        "text": 'Two identical flasks of yeast and sugar solution are set up, one sealed and one left open and stirred in air. After a day the sealed one smells strongly of alcohol and the open one does not, but has grown far more yeast. Explain both observations.',
        "options": [
            {"text": 'The open flask fermented much faster than the sealed one, but its ethanol evaporated away before it could ever be smelled.', "correct": False,
             "why": 'The open flask is aerated, so its yeast is respiring aerobically rather than fermenting at all.'},
            {"text": "The sealed flask's yeast grew faster because it had no competition for space.", "correct": False,
             "why": 'It is the open, aerated flask that grows faster; oxygen lets yeast grow much more quickly than fermentation does.'},
            {"text": 'The sealed flask fermented; the open, aerated one respired aerobically instead, growing fast and making no ethanol.', "correct": True},
            {"text": 'Both flasks did exactly the same thing, and the smell difference is due to the container shape.', "correct": False,
             "why": 'The two flasks ran different reactions — anaerobic in the sealed one, aerobic in the open one — because of the oxygen.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s14',
        "band": 'standard',
        "text": 'A yeast culture is heated briefly to 80 °C, checked, and found to be completely inactive even after a week back on a warm shelf. Explain why waiting longer does not help.',
        "options": [
            {"text": 'The yeast is only resting rather than dead, and it will become fully active again given enough further time.', "correct": False,
             "why": 'The damage from 80 °C is permanent, not a resting state; no amount of further time restores dead cells.'},
            {"text": 'The yeast needs fresh sugar before it can start fermenting again.', "correct": False,
             "why": 'Adding sugar cannot help; the yeast cells themselves have been permanently killed by the heat.'},
            {"text": 'The yeast needs to be cooled even further before it revives.', "correct": False,
             "why": 'Further cooling cannot undo the permanent damage already done by the high temperature.'},
            {"text": "The heat permanently denatured the yeast's enzymes and killed the cells; nothing about waiting reverses that.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s15',
        "band": 'standard',
        "text": 'A student sets up yeast with plenty of sugar and warmth, but with no way for oxygen to reach it and no way for gas to escape. Predict what happens as time passes.',
        "options": [
            {"text": 'It ferments, and the trapped carbon dioxide builds up pressure inside the container.', "correct": True},
            {"text": 'It respires aerobically at first, then switches once the trapped oxygen runs out.', "correct": False,
             "why": 'There is no oxygen supply described at all; the yeast ferments from the very start.'},
            {"text": 'Nothing happens, since a completely sealed container prevents any reaction at all.', "correct": False,
             "why": 'A sealed container does not stop fermentation; the gas produced simply has nowhere to escape.'},
            {"text": 'The yeast eventually explodes from the inside as it runs out of space to grow.', "correct": False,
             "why": 'It is gas pressure building up in the container that is the risk, not the yeast cells expanding.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s16',
        "band": 'standard',
        "text": 'A student compares yoghurt made in a sealed jar at 30 °C with a batch made in an open bowl stirred occasionally at the same temperature. Only the sealed jar sets. Explain why.',
        "options": [
            {"text": 'The open bowl simply lost too much heat to the surrounding air to ferment properly at all.', "correct": False,
             "why": 'Both are kept at the same temperature; the real difference is exposure to oxygen and contamination.'},
            {"text": 'The open bowl lets in oxygen and other organisms, disrupting the lactic acid bacteria.', "correct": True},
            {"text": 'Stirring itself directly destroys the lactic acid as it forms.', "correct": False,
             "why": "Stirring is not what breaks down lactic acid; the open bowl's exposure to air is the problem."},
            {"text": 'The sealed jar simply had more bacteria added to it to begin with.', "correct": False,
             "why": "The situation describes identical starting bacteria; the sealed jar's protection is what differs."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s17',
        "band": 'standard',
        "text": 'A baker notices dough left overnight in the fridge rises far less than the same dough left for two hours on a warm counter, even though both eventually use all the sugar available. Explain the difference in terms of rate.',
        "options": [
            {"text": 'The cold dough must contain a completely different, weaker strain of yeast that makes less gas overall.', "correct": False,
             "why": 'It is the same yeast in both cases; the cold one is simply fermenting more slowly.'},
            {"text": 'The warm dough uses up its sugar supply before the cold dough starts fermenting at all.', "correct": False,
             "why": 'The cold dough is fermenting the entire time, just slowly; it is not waiting to start.'},
            {"text": 'The cold dough ferments at a much slower rate, so it has not produced as much gas within the same time.', "correct": True},
            {"text": 'The cold dough loses its carbon dioxide through the fridge wall as fast as it makes it.', "correct": False,
             "why": 'Gas does not pass through a fridge wall in this way; the difference is simply the rate of fermentation.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s18',
        "band": 'standard',
        "text": 'A vineyard owner ferments the same grape juice at two different temperatures and finds the warmer batch finishes in half the time, with a similar final alcohol content. Explain why the TIME differs but the final AMOUNT does not.',
        "options": [
            {"text": 'The warmer batch actually uses more sugar overall, which is hidden by the alcohol reading.', "correct": False,
             "why": 'Both batches ferment the same amount of available sugar; temperature changes the speed, not the supply.'},
            {"text": 'The cooler batch loses some of its ethanol to evaporation, which balances out the slower rate.', "correct": False,
             "why": 'The situation is about time taken and final alcohol content, not about differing evaporation.'},
            {"text": 'Temperature does not actually affect fermentation rate at all; the timing must be due to something else.', "correct": False,
             "why": 'Temperature is well known to change fermentation rate, which is exactly what explains the timing here.'},
            {"text": 'Higher temperature speeds up the rate, but the same total sugar is available to be converted either way.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s19',
        "band": 'standard',
        "text": 'A student argues that yeast used to bake bread must be a completely different organism from yeast used to brew beer, since one makes mostly gas and the other mostly alcohol. Evaluate this claim.',
        "options": [
            {"text": 'It can be the same organism; what differs is which product the maker chooses to capture.', "correct": True},
            {"text": 'No single organism could ever make both products from one reaction.', "correct": False,
             "why": 'The same yeast fermenting sugar makes both products at once; the maker keeps whichever one they want.'},
            {"text": "Brewer's yeast has had its gas-making ability bred out.", "correct": False,
             "why": "Brewer's yeast still makes carbon dioxide too; it is simply not what the brewer keeps."},
            {"text": "The claim is wrong, but only because baker's yeast makes no ethanol at all under any conditions.", "correct": False,
             "why": "Baker's yeast does make ethanol; it is simply left to evaporate during baking."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s20',
        "band": 'standard',
        "text": 'A microbiologist wants to grow a large amount of yeast quickly for sale, rather than making beer or bread. Suggest what conditions they should use, and explain why fermentation conditions would not achieve this goal.',
        "options": [
            {"text": 'A sealed, warm tank exactly like a brewery, because fermentation is the route that makes the most yeast cells overall in the end.', "correct": False,
             "why": 'Fermentation is the slower-growing route for yeast; an aerated tank supports much faster growth.'},
            {"text": 'An open, well-aerated tank, because aerobic respiration lets the yeast grow far faster than fermenting.', "correct": True},
            {"text": 'A sealed, cold tank, because slowing fermentation right down always lets far more cells quietly build up over a longer stretch of time.', "correct": False,
             "why": 'Slowing fermentation down does not increase yeast growth; oxygen is what lets it grow quickly.'},
            {"text": 'It makes no difference which conditions are used, since yeast grows at the same rate either way.', "correct": False,
             "why": 'Yeast grows much faster with oxygen available than it does while fermenting.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s21',
        "band": 'standard',
        "text": 'A home brewer forgets to fit an airlock and leaves the lid slightly open overnight. The next day the mixture tastes sour rather than alcoholic. Suggest what has most likely happened.',
        "options": [
            {"text": 'The yeast simply worked much faster than expected overnight and used up all of its sugar supply.', "correct": False,
             "why": 'Faster fermentation would give a stronger alcoholic taste, not a sour one.'},
            {"text": 'The open lid let all the ethanol evaporate, leaving only the sugar taste behind.', "correct": False,
             "why": 'A sour taste is not the taste of plain sugar; it points to an acid having formed.'},
            {"text": 'Oxygen and other organisms, likely bacteria, contaminated the mixture and produced acid instead of ethanol.', "correct": True},
            {"text": 'Cold air coming in overnight reacted directly with the sugar to make it sour.', "correct": False,
             "why": 'Air does not react directly with sugar to produce sourness; contamination is more likely.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s22',
        "band": 'standard',
        "text": 'A student reads that penicillin, insulin and Quorn are all made using fermenters, and concludes that a fermenter must always contain yeast. Evaluate this conclusion.',
        "options": [
            {"text": 'The conclusion is correct, since only yeast of all the micro-organisms that exist can ever be grown usefully in a fermenter.', "correct": False,
             "why": 'Fermenters are used for a wide range of micro-organisms, not only yeast.'},
            {"text": 'The conclusion is correct, because Quorn, insulin and penicillin are all made by yeast specifically.', "correct": False,
             "why": 'Penicillin comes from a fungus that is not the same organism as yeast.'},
            {"text": 'The conclusion is wrong, but only because none of the three products are actually made in fermenters at all.', "correct": False,
             "why": 'All three genuinely are grown in fermenters; the flaw is assuming the organism must always be yeast.'},
            {"text": 'The conclusion is wrong — a fermenter can hold a fungus, a bacterium or a genetically modified microbe, not only yeast.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s23',
        "band": 'standard',
        "text": 'A café owner notices that opened kombucha (a fermented tea drink) left out on the counter all day becomes noticeably more sour than a freshly opened bottle. Explain why.',
        "options": [
            {"text": 'The fermenting organisms in it are still alive, so they carry on converting more sugar into acid.', "correct": True},
            {"text": 'Sunlight streaming through the window breaks the sugar down into acid directly, with no organism involved at all.', "correct": False,
             "why": 'Sunlight does not convert sugar into acid; the souring is caused by living organisms fermenting it further.'},
            {"text": 'The drink simply evaporates a little over the course of the day, concentrating whatever acid was already there to begin with.', "correct": False,
             "why": 'Evaporation would concentrate flavours generally, but the souring here is from ongoing fermentation.'},
            {"text": 'Kombucha stops fermenting the moment the bottle is opened.', "correct": False,
             "why": 'Opening the bottle does not stop the living organisms fermenting further.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s24',
        "band": 'standard',
        "text": 'A gardener wants to make silage (fermented animal feed) from freshly cut grass by packing it tightly into an airtight container. Explain why excluding air matters.',
        "options": [
            {"text": 'Tight packing simply keeps the grass at a higher temperature throughout, and that alone is the only thing that really matters.', "correct": False,
             "why": 'Temperature is not the main reason; excluding air favours fermentation over aerobic spoilage.'},
            {"text": 'Excluding air favours the fermenting bacteria that preserve the grass, rather than the aerobic decay organisms.', "correct": True},
            {"text": 'Sealing it out from air stops every single micro-organism of any kind from surviving anywhere inside the container.', "correct": False,
             "why": 'Sealing it out from air does not kill the organisms; it favours the anaerobic ones over aerobic spoilage.'},
            {"text": 'The grass needs no micro-organisms at all to become silage; sealing alone preserves it chemically.', "correct": False,
             "why": 'Silage-making relies on fermenting bacteria producing acid, not sealing with no organisms.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s25',
        "band": 'standard',
        "text": 'A student argues that since a penicillin fermenter and a beer fermenter both control temperature, pH and oxygen, they must be doing fundamentally the same job. Evaluate this claim.',
        "options": [
            {"text": 'The claim is entirely wrong, since penicillin fermenters use no living organism of any kind at all.', "correct": False,
             "why": 'A penicillin fermenter grows a living fungus, just as a brewery grows living yeast.'},
            {"text": 'The claim is entirely correct with no meaningful difference between the two uses at all.', "correct": False,
             "why": 'The organism, the product and the purpose differ completely, even if the engineering is similar.'},
            {"text": 'The engineering is similar, but what is growing inside and the product wanted are very different.', "correct": True},
            {"text": 'Beer fermenters do not actually control oxygen at all.', "correct": False,
             "why": 'A brewery does control oxygen carefully, usually excluding it to keep the yeast fermenting.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s26',
        "band": 'standard',
        "text": 'A soy sauce maker ferments soybeans and wheat with a chosen fungus and bacteria over many months. A student says this must be exactly the same process as making yoghurt, since both use fermentation. Evaluate this claim.',
        "options": [
            {"text": 'The claim is entirely correct, and the two processes are identical in every respect.', "correct": False,
             "why": 'The organisms, raw materials, time taken and products made are all quite different between the two.'},
            {"text": 'Soy sauce making is not really fermentation at all.', "correct": False,
             "why": 'Soy sauce making genuinely is a fermentation process, using chosen fungi and bacteria.'},
            {"text": 'The claim is wrong, but only because yoghurt takes far longer to make than soy sauce.', "correct": False,
             "why": 'It is soy sauce that typically takes far longer; other differences matter too.'},
            {"text": 'Both are fermentation, but the organisms, raw material, time and final product all differ greatly.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s27',
        "band": 'standard',
        "text": 'A brewer ages beer in a sealed barrel for months after the main, fast fermentation has finished. A student asks why fermentation would continue at all once most of the sugar is used up. Explain.',
        "options": [
            {"text": 'A small amount of unfermented sugar and remaining yeast can continue reacting slowly.', "correct": True},
            {"text": 'Fermentation has actually finished completely, and nothing chemical happens during the ageing at all.', "correct": False,
             "why": 'A small amount of continuing fermentation is exactly why brewers age beer sealed rather than open.'},
            {"text": 'The yeast starts making an entirely new gas once the sugar runs out.', "correct": False,
             "why": 'There is no new gas; any continuing reaction is simply fermentation of the sugar still remaining.'},
            {"text": 'The barrel needs to stay sealed only to protect the flavour, not because of any ongoing reaction.', "correct": False,
             "why": 'Keeping it sealed also protects any continuing slow fermentation from oxygen.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s28',
        "band": 'standard',
        "text": 'A student is given two unlabelled fizzy drinks: one carbonated by direct gas injection, one made by natural fermentation in a sealed bottle. Suggest a test, other than taste, to tell them apart.',
        "options": [
            {"text": 'Measuring how fizzy each drink is would tell the two apart reliably enough on its own.', "correct": False,
             "why": 'Both a directly carbonated and a fermented drink can be equally fizzy.'},
            {"text": 'Testing for a small amount of alcohol, since a fermented drink is likely to contain some.', "correct": True},
            {"text": 'Checking the sugar content, since only fermented drinks contain any sugar at all.', "correct": False,
             "why": 'A directly carbonated drink can still contain sugar; a trace of alcohol is more distinctive.'},
            {"text": 'There is no way to tell the two apart by any test at all.', "correct": False,
             "why": 'Testing for alcohol is a genuine way to distinguish them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s29',
        "band": 'standard',
        "text": 'A student reads that Quorn is made from a fungus grown in a fermenter and harvested, and concludes it must involve exactly the same fermentation reaction as making beer. Evaluate this claim.',
        "options": [
            {"text": 'Any product at all that is grown in a fermenter must be made by an identical fermentation reaction.', "correct": False,
             "why": 'The vessel is the same; the organism, conditions and product can differ a great deal.'},
            {"text": "Quorn's fungus is actually just a renamed strain of ordinary brewer's yeast.", "correct": False,
             "why": "Quorn is made from a different fungus, not a strain of brewer's yeast."},
            {"text": 'Both use a fermenter and a living organism, but the organism and what is harvested differ greatly.', "correct": True},
            {"text": "Quorn's fungus makes no use of sugar at all.", "correct": False,
             "why": "Quorn's fungus, like yeast, needs a sugar supply to grow."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s30',
        "band": 'standard',
        "text": 'A student notices that both baking powder and yeast make bread rise, and argues that since both release carbon dioxide, they must work by the exact same mechanism. Evaluate this claim.',
        "options": [
            {"text": 'Any process that releases carbon dioxide must be the same kind of reaction.', "correct": False,
             "why": 'Releasing the same gas does not mean the underlying process is the same.'},
            {"text": 'The claim is correct, because yeast is actually a non-living chemical raising agent, just like baking powder.', "correct": False,
             "why": 'Yeast is a living, single-celled fungus, not a non-living chemical raising agent.'},
            {"text": 'Baking powder does not actually release carbon dioxide at all.', "correct": False,
             "why": 'Baking powder does release carbon dioxide when wet and warm.'},
            {"text": 'Baking powder releases gas by a chemical reaction; yeast releases it as a living organism respiring.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s31',
        "band": 'standard',
        "text": 'A wine maker finds that a batch fermented with wild yeast from grape skins tastes noticeably different from an identical batch fermented with a single, chosen strain added deliberately. Suggest why.',
        "options": [
            {"text": 'Wild grape skins carry a mixture of strains, each making slightly different flavour compounds.', "correct": True},
            {"text": 'Wild yeast makes no ethanol at all, only flavour compounds.', "correct": False,
             "why": 'Wild yeast still ferments the grape sugar into ethanol; the difference is in additional flavour compounds.'},
            {"text": 'The grape skins themselves change flavour on their own, with no yeast involved in either batch.', "correct": False,
             "why": 'Both batches rely on yeast fermenting the grape sugar.'},
            {"text": 'There should be no flavour difference at all, since both batches ferment the same grape sugar.', "correct": False,
             "why": 'Different yeast strains can genuinely produce different flavour compounds even from the same sugar.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-s32',
        "band": 'standard',
        "text": 'A student argues that because ethanol can be burned as a fuel, ethanol production by fermentation must release the same total energy as burning petrol directly. Evaluate this claim.',
        "options": [
            {"text": 'Ethanol and petrol must release exactly identical amounts of energy, given that both of them can be burned as a fuel.', "correct": False,
             "why": 'Different fuels release different amounts of energy per unit; being usable as fuel does not make them equal.'},
            {"text": 'The claim conflates two steps — fermentation itself releases little energy; burning ethanol afterwards releases far more.', "correct": True},
            {"text": 'Fermentation itself is really just a slow form of burning.', "correct": False,
             "why": 'Fermentation is a controlled biological reaction inside a living cell, quite different from burning.'},
            {"text": 'Ethanol cannot actually be burned as a fuel at all.', "correct": False,
             "why": 'Ethanol genuinely is burned as a fuel in some countries.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h11',
        "band": 'harder',
        "text": 'A microbiologist finds a strain of yeast that ferments glucose but appears completely unable to respire aerobically, even with plenty of oxygen present. Predict what would happen if this strain were grown in an open, well-aerated tank instead of a sealed one.',
        "options": [
            {"text": 'It would ferment anyway, since it cannot use the oxygen; the open tank would make little difference.', "correct": True},
            {"text": 'It would definitely respire aerobically once oxygen became available, just like ordinary yeast.', "correct": False,
             "why": 'This strain cannot respire aerobically at all, so oxygen being present would not change what reaction it runs.'},
            {"text": 'It would die immediately on contact with any oxygen at all.', "correct": False,
             "why": 'Nothing suggests oxygen is toxic to this strain, only that it cannot use it.'},
            {"text": 'It would stop fermenting completely and produce nothing at all.', "correct": False,
             "why": 'There is no reason for fermentation itself to stop; the strain simply continues fermenting.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h12',
        "band": 'harder',
        "text": 'A student claims that because fermentation is anaerobic and combustion is also possible without oxygen in rare cases, the two must be fundamentally similar processes. Evaluate this claim.',
        "options": [
            {"text": 'Both processes ultimately release energy from a fuel.', "correct": False,
             "why": 'Releasing energy from a fuel is true of many processes; it does not make a cellular reaction the same as combustion.'},
            {"text": 'They differ fundamentally — fermentation is a controlled enzyme reaction in a cell; combustion is uncontrolled, releasing heat and light at once.', "correct": True},
            {"text": 'The claim is correct, because fermentation also produces visible heat and light in large amounts, easily bright enough to see clearly from right across a darkened room.', "correct": False,
             "why": 'Fermentation releases only a small, controlled amount of energy, with no significant light.'},
            {"text": 'Fermentation never happens without oxygen present.', "correct": False,
             "why": 'Fermentation specifically happens without oxygen; the flaw is treating it as similar to combustion at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h13',
        "band": 'harder',
        "text": 'A wine maker ferments identical grape juice in two sealed vessels at the same temperature, one with twice as much yeast as the other. Both make a similar total amount of ethanol, but the one with more yeast finishes sooner. Explain both observations.',
        "options": [
            {"text": 'The vessel with more yeast must have used noticeably less sugar overall in order to reach that same final result.', "correct": False,
             "why": 'Both vessels start with the same sugar; more yeast changes the rate, not the total sugar converted.'},
            {"text": 'The two vessels cannot really have made the same amount of ethanol at all if one of them clearly finished so much sooner than the other.', "correct": False,
             "why": 'Finishing sooner is consistent with reaching the same final amount more quickly.'},
            {"text": 'More yeast raises the rate, finishing sooner, but the total ethanol is set by the fixed sugar in both vessels.', "correct": True},
            {"text": 'More yeast means more sugar is created during the reaction, which is why the amount stays the same.', "correct": False,
             "why": 'Fermentation consumes sugar; it does not create it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h14',
        "band": 'harder',
        "text": 'A researcher proposes that if a fermenting yeast culture were kept permanently at the temperature giving its fastest rate, ethanol production would carry on increasing forever. Evaluate this proposal.',
        "options": [
            {"text": 'The proposal is correct, since a faster rate always means more product will eventually be made overall.', "correct": False,
             "why": 'A faster rate empties the available sugar sooner, not later.'},
            {"text": 'Yeast at its optimum temperature never stops respiring at all.', "correct": False,
             "why": 'Even at an ideal temperature, yeast still depends on a supply of sugar.'},
            {"text": 'Very high temperatures always kill yeast instantly.', "correct": False,
             "why": "The described temperature is the yeast's own fastest rate, not a lethal one; the flaw is the fixed sugar supply."},
            {"text": 'It fails once the sugar runs out — a fixed amount of glucose gives only a fixed total amount of ethanol.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h15',
        "band": 'harder',
        "text": 'A brewer accidentally uses water containing a small amount of chlorine, intended to kill bacteria, to prepare a batch of beer. Fermentation barely happens at all. Explain why, connecting it to what chlorine is designed to do.',
        "options": [
            {"text": 'Chlorine kills micro-organisms generally, not just unwanted bacteria, so it damages the yeast too.', "correct": True},
            {"text": 'Chlorine reacts directly with the sugar, making it impossible for any organism to ferment it.', "correct": False,
             "why": "Chlorine's effect here is on living organisms, not the sugar molecule itself."},
            {"text": "The chlorine simply lowers the water's temperature too much for the yeast to work.", "correct": False,
             "why": "Chlorine's role here is chemical, killing living cells, not a change in temperature."},
            {"text": 'Chlorine only affects bacteria and never affects yeast, so something else must explain the failure.', "correct": False,
             "why": 'Chlorine is a general disinfectant that harms many kinds of micro-organism, including yeast.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h16',
        "band": 'harder',
        "text": 'A student argues that since penicillin, insulin and ethanol fuel are all made using living organisms in fermenters, biotechnology of this kind must always be a recent, twentieth-century invention. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since ancient peoples had no way of controlling which organism did the fermenting.', "correct": False,
             "why": 'Choosing starter cultures and specific brewing yeasts is an ancient practice.'},
            {"text": 'Bread and beer are not actually made using fermentation at all.', "correct": False,
             "why": 'Bread and beer are both classic examples of fermentation, going back thousands of years.'},
            {"text": 'Fermenting foods such as bread, beer and yoghurt are ancient technologies using the same underlying idea; only modifying the organism is modern.', "correct": True},
            {"text": 'The claim is wrong, but only because penicillin was discovered centuries before modern insulin production.', "correct": False,
             "why": 'The order products were developed does not address the real flaw in the claim.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h17',
        "band": 'harder',
        "text": 'A brewer scales up a successful 5-litre batch to a 5000-litre tank, keeping the same yeast, sugar concentration and temperature. A colleague warns this will not automatically give 1000 times more beer of the same quality. Suggest one reason why.',
        "options": [
            {"text": 'The reason is that yeast cells physically cannot survive at all in any single container larger than just a few litres in size.', "correct": False,
             "why": 'Yeast is grown successfully in huge industrial fermenters; size alone does not prevent survival.'},
            {"text": 'The reason is that sugar dissolved in water behaves in a completely different way in large volumes of liquid than it does in small ones.', "correct": False,
             "why": 'Sugar dissolved in water behaves the same chemically regardless of container size.'},
            {"text": "There is no real reason for concern, and the colleague's warning does not apply to fermentation at all.", "correct": False,
             "why": 'Evenness of conditions genuinely becomes harder to maintain at a much larger scale.'},
            {"text": 'A much larger tank is harder to keep evenly mixed and at an even temperature throughout, changing the result in places.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h18',
        "band": 'harder',
        "text": 'A student proposes that adding more yeast to a batch of dough will always make the bread rise higher, with no limit. Evaluate this proposal, considering what eventually limits how much a loaf can rise.',
        "options": [
            {"text": "It fails once the dough's structure can stretch no further, and the fixed sugar supply also limits the gas made.", "correct": True},
            {"text": 'The proposal is correct, since more yeast always means proportionally more gas with no other limit involved.', "correct": False,
             "why": 'The dough cannot stretch to hold unlimited gas, and the sugar supply is also fixed.'},
            {"text": 'Yeast can make an unlimited amount of gas from a fixed amount of sugar.', "correct": False,
             "why": 'A fixed amount of sugar can only ever be fermented into a fixed total amount of gas.'},
            {"text": 'Extra yeast always makes bread taste worse.', "correct": False,
             "why": 'Taste is separate from how high the loaf can physically rise.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h19',
        "band": 'harder',
        "text": 'A student is told Quorn, penicillin and yoghurt are all fermentation products, and infers that since fermentation is anaerobic, none of these organisms can ever use oxygen under any circumstances. Evaluate this inference.',
        "options": [
            {"text": 'The inference is correct, since any organism at all that is used in a fermenter must be completely and permanently unable to use oxygen.', "correct": False,
             "why": 'Many organisms grown in fermenters can also respire aerobically under different conditions.'},
            {"text": 'The inference overreaches — many such organisms, including yeasts and fungi, can also respire aerobically when conditions favour it.', "correct": True},
            {"text": 'The inference is correct, because oxygen is always completely poisonous to every single organism used to make any of these three named products.', "correct": False,
             "why": 'Oxygen is not poisonous to these organisms in general; that is not true of every organism used here.'},
            {"text": 'The inference is wrong, but only because none of these three products actually involve fermentation at all.', "correct": False,
             "why": 'All three genuinely are fermentation products.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h20',
        "band": 'harder',
        "text": 'A student measures carbon dioxide from a yeast culture every ten minutes, expecting a straight rising line all afternoon. Instead the rate slows after about an hour, though sugar remains. Suggest two explanations before concluding the yeast has died.',
        "options": [
            {"text": 'There is only one possible explanation: the yeast must already be completely dead.', "correct": False,
             "why": 'Falling sugar and rising ethanol both slow fermentation well before dead yeast should be assumed.'},
            {"text": 'The carbon dioxide must simply be dissolving back into the mixture rather than genuinely being produced any more slowly than before.', "correct": False,
             "why": 'The change points to conditions inside the flask changing, not gas dissolving back in.'},
            {"text": 'Falling sugar concentration slows the rate, and building ethanol also begins to inhibit the yeast before any cells die.', "correct": True},
            {"text": 'The temperature in the room must have dropped sharply at some point during the afternoon, which is what slowed the whole reaction down.', "correct": False,
             "why": 'Nothing describes a temperature change; falling sugar and rising ethanol explain it instead.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h21',
        "band": 'harder',
        "text": 'A rowing coach jokes that fermenting yeast and a rowing crew both ‘run out of steam’, and asks a student whether the underlying reasons are really the same. Evaluate the comparison.',
        "options": [
            {"text": 'The comparison is exactly right, since a rowing crew and a flask of fermenting yeast are both really just examples of one identical chemical reaction slowing down.', "correct": False,
             "why": 'Fermentation and muscle fatigue are different biological processes.'},
            {"text": 'Fermentation never slows down at any point once it has started.', "correct": False,
             "why": 'Fermentation does slow over time as sugar falls and ethanol rises.'},
            {"text": 'Rowers do not produce any lactic acid at all during a race.', "correct": False,
             "why": 'Rowers working hard do produce lactic acid.'},
            {"text": 'Both slow as a resource runs low or waste builds up, but yeast is limited by falling sugar and ethanol, a rower by lactic acid and glycogen.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h22',
        "band": 'harder',
        "text": 'A student proposes that since both yeast fermentation and human anaerobic respiration use no oxygen, a person could survive indefinitely without breathing, relying on their own ‘fermentation’ the way yeast does in a sealed vessel. Evaluate this proposal.',
        "options": [
            {"text": 'It fails — human anaerobic respiration gets far less energy and leaves lactic acid needing oxygen afterwards; it is a short backup, not a substitute for breathing.', "correct": True},
            {"text": 'The proposal is correct, since both processes are anaerobic and therefore functionally identical in every way.', "correct": False,
             "why": "Human muscle's route gets far less energy and produces a build-up that must eventually be repaid using oxygen."},
            {"text": 'The proposal is correct, because lactic acid can be recycled by the body indefinitely with no oxygen needed at all.', "correct": False,
             "why": 'Dealing with lactic acid afterwards specifically needs oxygen.'},
            {"text": 'Yeast fermentation actually does use oxygen.', "correct": False,
             "why": 'Yeast fermentation specifically happens without oxygen.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h23',
        "band": 'harder',
        "text": 'A student argues that since sourdough bread rises using wild yeast already in flour, adding shop-bought yeast to any dough must be unnecessary and just a modern convenience with no real benefit. Evaluate this argument.',
        "options": [
            {"text": 'Wild and shop-bought yeast always ferment at exactly the same rate.', "correct": False,
             "why": 'Wild fermentation using whatever is present is typically much slower and more variable.'},
            {"text": 'Wild fermentation works but is typically slower and less predictable than a chosen, concentrated strain — a genuine benefit, not only convenience.', "correct": True},
            {"text": 'The argument is correct, because shop-bought yeast is not really a living organism of any kind at all, but simply a manufactured chemical raising product.', "correct": False,
             "why": 'Shop-bought dried yeast is a living organism, dried into a dormant state.'},
            {"text": 'Wild yeast is toxic and cannot safely be used in bread at all.', "correct": False,
             "why": 'Wild yeast in sourdough is not toxic and is safely used worldwide.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h24',
        "band": 'harder',
        "text": 'A researcher ferments the same sugar solution with three different bacterial strains and finds each produces a different ratio of lactic acid to gas, even though all three are ‘lactic acid bacteria’. A student concludes the term must be meaningless. Evaluate this conclusion.',
        "options": [
            {"text": 'The conclusion is correct, since a genuinely meaningful scientific category of any kind can never contain any variation whatsoever between its own individual members.', "correct": False,
             "why": 'Many genuine scientific categories contain real variation while still being useful labels.'},
            {"text": 'Lactic acid bacteria by definition must produce identical amounts of every product.', "correct": False,
             "why": 'The defining feature is making lactic acid as the main product, not identical amounts of every by-product.'},
            {"text": 'The term correctly groups bacteria whose main product is lactic acid, though strains can still vary in exactly how much gas they also make.', "correct": True},
            {"text": 'The three strains must actually be exactly the same species.', "correct": False,
             "why": 'Different but related strains can share the label while still varying somewhat.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h25',
        "band": 'harder',
        "text": 'A student proposes testing whether temperature or sugar concentration has a bigger effect on yeast fermentation rate, by changing both variables together in the same flasks. Evaluate this experimental design.',
        "options": [
            {"text": 'Changing both variables together saves time and still shows which one matters most.', "correct": False,
             "why": 'Changing two variables at once means any change could be due to either one, or both.'},
            {"text": 'Gas production rate is not affected by either sugar concentration or temperature anyway.', "correct": False,
             "why": 'Both are well known to affect fermentation rate, which is why testing them properly matters.'},
            {"text": 'The design is flawed, but only because gas production of this kind cannot ever be measured accurately in an ordinary school laboratory.', "correct": False,
             "why": 'Gas production can be measured reasonably well in a school lab; the flaw is testing two variables at once.'},
            {"text": 'It is flawed — changing two variables at once makes it impossible to tell which one caused any change in rate.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h26',
        "band": 'harder',
        "text": 'A student ferments the same mass of glucose with yeast in one flask and lactic acid bacteria in an identical flask, and finds the yeast flask has lost slightly more total mass by the end. Explain this difference.',
        "options": [
            {"text": "The yeast flask loses mass mainly as escaping carbon dioxide gas; the bacteria's lactic acid stays dissolved in the liquid.", "correct": True},
            {"text": 'The yeast simply ferments a much larger overall fraction of the total glucose supplied than the bacteria manage to.', "correct": False,
             "why": 'The mass difference is best explained by which product can escape as a gas, not by fermented fraction.'},
            {"text": "The bacteria's flask must have started with less glucose than the yeast's flask.", "correct": False,
             "why": 'Both flasks start with the same mass of glucose.'},
            {"text": 'Lactic acid bacteria do not produce any measurable product at all, unlike yeast.', "correct": False,
             "why": 'Lactic acid bacteria do produce a real product; it simply stays dissolved.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h27',
        "band": 'harder',
        "text": 'A brewer claims that because their beer contains living yeast right up until bottling, fermentation inside a sealed, capped bottle will continue completely unchanged forever, slowly making the beer infinitely strong. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since living yeast sealed inside any container will always simply keep fermenting for as long as the individual cells themselves stay alive.', "correct": False,
             "why": 'Even living yeast cannot keep fermenting once its available sugar is used up.'},
            {"text": 'It fails for the usual reason — the sealed bottle has only a small, fixed amount of unfermented sugar left, so fermentation stops once that is used up.', "correct": True},
            {"text": 'Glass bottles slowly produce more sugar from the glass itself over time.', "correct": False,
             "why": 'Glass does not supply sugar to a fermenting drink.'},
            {"text": 'Yeast dies the instant a bottle is sealed.', "correct": False,
             "why": 'Yeast does not die simply from being sealed in a bottle.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h28',
        "band": 'harder',
        "text": 'A student argues that because both fermentation and photosynthesis can happen without external oxygen being supplied, the two processes must serve a similar biological purpose. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since not needing oxygen is enough to show two processes serve the same biological purpose.', "correct": False,
             "why": 'The two processes do opposite jobs — releasing energy versus building fuel.'},
            {"text": 'The claim is correct, because fermentation and photosynthesis both make glucose as their main product.', "correct": False,
             "why": 'Fermentation breaks glucose down; only photosynthesis makes it.'},
            {"text": 'It is wrong — fermentation releases energy from existing fuel, while photosynthesis builds new fuel using light; not needing oxygen is all they share.', "correct": True},
            {"text": 'Photosynthesis actually does need oxygen supplied from outside.', "correct": False,
             "why": 'Photosynthesis uses carbon dioxide and light, not a supply of oxygen.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h29',
        "band": 'harder',
        "text": 'An industrial fermenter produces bioethanol fuel around the clock, with fresh sugar solution pumped in continuously and product removed continuously, rather than run as one sealed batch. Suggest why a producer might prefer this over repeated separate batches.',
        "options": [
            {"text": 'The continuous approach is preferred only because it always uses noticeably less total yeast overall than any equivalent batch process ever possibly could.', "correct": False,
             "why": 'The yeast needed depends on scale and rate required, not simply on being continuous.'},
            {"text": 'The continuous approach is preferred because it somehow lets the yeast avoid making any ethanol at all until right at the very end of the run.', "correct": False,
             "why": 'A continuous system produces ethanol throughout, continuously removed.'},
            {"text": 'There is no real advantage to a continuous system, and it is only used because it looks more impressive to visitors.', "correct": False,
             "why": 'A continuous system offers a genuine practical advantage over batch downtime.'},
            {"text": 'It keeps the yeast at a steady, favourable sugar level throughout, avoiding slower late-batch rates and downtime between batches.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h30',
        "band": 'harder',
        "text": 'A student proposes that any two microbial products described as ‘fermented’ must have been made using the same species of organism, since fermentation is fermentation regardless of what is being made. Evaluate this claim, using named examples.',
        "options": [
            {"text": 'It is false — bread and beer use yeast, yoghurt uses lactic acid bacteria, soy sauce uses different fungi and bacteria again.', "correct": True},
            {"text": 'Yeast is used to ferment every one of these named foods.', "correct": False,
             "why": 'Yoghurt and soy sauce are not made using yeast; they rely on different bacteria and fungi.'},
            {"text": 'The word ‘fermented’ is strictly defined as meaning that one single specific organism was always used.', "correct": False,
             "why": '‘Fermented’ describes the type of anaerobic reaction, not one particular organism every time.'},
            {"text": 'The claim is wrong, but only because none of these particular named foods actually involve any kind of micro-organism at all in making them.', "correct": False,
             "why": 'All of the named foods genuinely rely on a living micro-organism.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-04-h31',
        "band": 'harder',
        "text": 'A student reads that fermentation ‘is respiration’ and also that ‘fermentation makes food’, and argues these two statements contradict each other, since respiration releases energy for the organism rather than making food for people. Evaluate this apparent contradiction.',
        "options": [
            {"text": 'The statements are genuinely contradictory, and one of them must simply be wrong.', "correct": False,
             "why": 'Both can be true: the organism respires for its own energy, and the leftover happens to be useful as food.'},
            {"text": 'There is no contradiction — the organism respires for its own energy, and the food product is simply its leftover waste.', "correct": True},
            {"text": 'The contradiction is resolved because fermenting organisms deliberately produce food for humans as their main purpose.', "correct": False,
             "why": 'A fermenting organism respires for its own energy; food for humans is an incidental waste product.'},
            {"text": 'The contradiction is resolved because respiration and making food are actually the exact same single process.', "correct": False,
             "why": 'The resolution is that food is a leftover product of respiration, not that the two ideas are identical.'},
        ],
        "figure": None,
    },
]

QUESTIONS.extend(_MRB338_NEW_QUESTIONS)
