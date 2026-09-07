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
            {"text": "A living, single-celled fungus that respires the sugar "
                     "it is given.",
             "correct": True},
            {"text": "A bacterium, like the ones that turn milk into "
                     "yoghurt.",
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
            {"text": "Micro-organisms already in the flour and the air are "
                     "respiring the sugars.",
             "correct": True},
            {"text": "The flour reacts with the water, giving off gas as a "
                     "raising agent.",
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
            {"text": "Heating kills what was already in the milk; cooling "
                     "stops the culture being killed too.",
             "correct": True},
            {"text": "Heating starts the reaction, and cooling slows it so "
                     "the yoghurt sets gently.",
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
