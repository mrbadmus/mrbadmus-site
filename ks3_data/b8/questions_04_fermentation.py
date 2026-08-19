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
]
