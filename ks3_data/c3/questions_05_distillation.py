# -*- coding: utf-8 -*-
"""C3 lesson 05 — Distillation: twelve questions (MRB-269).

The lesson's argument is that distillation is TWO jobs and not one: boil to
separate, cool to collect, and a student who does only one of them gets
nothing. These twelve probe that argument from the angles the ladder leaves
alone — the condenser's actual job, what the thermometer is telling you, the
ink and ethanol runs the ladder never visits, and the difference between a
distillate that is salty and one that is merely scarce.

The distractors are built from the misconceptions the lesson declares and the
two it inherits.

`MIX-10` (boiling carries dissolved salt over with the steam) is the declared
one and drives the wrong options in e02, e04, s01, s04 and h02 — every one of
them lets a dissolved solid ride out of the flask in a gas, or blames the
apparatus for stopping it.

`MIX-08` (evaporated water is gone — destroyed) is `c3-04`'s register entry
and is inherited here rather than re-declared: Design's own rung 1 offers "the
water is destroyed by boiling" as an option, so the idea is live on this page.
It drives e01, e04 and h04.

`MIX-07` (a fine enough filter would separate salt from water) is `c3-03`'s,
and the hook rules it out in its first three lines. It drives h01, where the
student is invited to call distillation a slow filter.

A fourth strand belongs to this lesson and is in no register: **cooling is
optional**. It reads the condenser as a convenience, an accelerator, or a
device that catches the salt, rather than as the half of the method that
collects anything at all. It drives e02, s01, s02 and h04, and s01 is the
question that carries it directly.

Nothing here re-asks a rung. Rung 1 asks what is collected from sea water and
rung 2 asks why a distillate is salty; e01 and e03 approach the first through
evaporation and through the word `distillate`, and h04 approaches the second
from the opposite failure — a distillate that is clean but scarce.
"""

UNIT = "C3"
LESSON = "distillation"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-05-e01",
        "band": "easier",
        "text": "Evaporation and distillation both start by boiling a salt "
                "solution. What is the difference between them?",
        "options": [
            {"text": "Distillation destroys the water so that only the salt "
                     "is left", "correct": False,
             "why": "Nothing is destroyed by boiling. The water becomes a gas "
                    "and goes somewhere — distillation is the method that "
                    "decides where."},
            {"text": "Distillation boils the solution to drive the water "
                     "off, while evaporation does not boil it at all",
             "correct": False,
             "why": "Both drive the water off as a gas. What differs is "
                    "whether anything is waiting to catch it."},
            {"text": "Distillation catches the vapour and keeps the liquid; "
                     "evaporation lets it go and keeps the solid",
             "correct": True},
            {"text": "Distillation keeps the solid and evaporation keeps the "
                     "liquid", "correct": False,
             "why": "That is the right idea the wrong way round. Evaporation "
                    "keeps the solid; distillation is the one that keeps the "
                    "liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e02",
        "band": "easier",
        "text": "Cold water runs through the outer jacket of the condenser. "
                "What is that cold water there to do?",
        "options": [
            {"text": "Cool the vapour so that it turns back into a liquid",
             "correct": True},
            {"text": "Trap the salt so that it cannot travel out with the "
                     "vapour", "correct": False,
             "why": "The salt never leaves the flask, so there is nothing to "
                    "trap. It has no way of becoming a gas at these "
                    "temperatures."},
            {"text": "Cool the flask so that the solution stops boiling over",
             "correct": False,
             "why": "The jacket is nowhere near the flask, and boiling is the "
                    "half of the method that does the separating. Cooling the "
                    "flask would stop the run."},
            {"text": "Wash the vapour clean before it reaches the beaker",
             "correct": False,
             "why": "The cold water is sealed in the outer jacket and never "
                    "touches the vapour. All it does is take heat away "
                    "through the glass."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e03",
        "band": "easier",
        "text": "Sea water is distilled and a liquid collects in the beaker. "
                "What is that liquid called?",
        "options": [
            {"text": "The residue — what is left behind at the end",
             "correct": False,
             "why": "The residue is what stays in the flask, which here is "
                    "the salt. The beaker holds the part that travelled."},
            {"text": "The distillate — the liquid collected after condensing",
             "correct": True},
            {"text": "The filtrate — the liquid that has passed through",
             "correct": False,
             "why": "A filtrate is what comes through filter paper. Nothing "
                    "has been filtered here; the water travelled as a gas."},
            {"text": "The solute — the part that was dissolved in it",
             "correct": False,
             "why": "The solute is the salt, and it is still in the flask. "
                    "The water is the solvent, and it is the part collected."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e04",
        "band": "easier",
        "text": "Blue ink is distilled. What is the colour of the liquid that "
                "collects in the beaker?",
        "options": [
            {"text": "Blue, because the colour travels with the water",
             "correct": False,
             "why": "The dye is a solid dissolved in the water and it cannot "
                    "become a gas. Only the water travels, and water is "
                    "colourless."},
            {"text": "Paler blue, because only some of the dye comes over",
             "correct": False,
             "why": "None of the dye comes over. There is no amount of "
                    "boiling that turns a dissolved dye into a gas at 100 "
                    "°C."},
            {"text": "Colourless, because the boiling has destroyed the dye",
             "correct": False,
             "why": "Right answer, wrong reason — and the reason matters. The "
                    "dye is not destroyed; it is left behind in the flask as "
                    "a ring of solid you can still see."},
            {"text": "Colourless, because the dye stays behind in the flask",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-05-s01",
        "band": "standard",
        "text": "A student runs a still with the cold water through the "
                "condenser switched off, and takes it all the way to the last "
                "stage. What is in the beaker at the end?",
        "options": [
            {"text": "A full beaker of pure water — vapour cools by itself "
                     "once it is out of the flask", "correct": False,
             "why": "Not fast enough, and not inside the apparatus. A "
                    "condenser as warm as the vapour takes no heat out of it, "
                    "so the vapour leaves at the open end."},
            {"text": "Nothing — the vapour was never cooled, so it left "
                     "through the open end", "correct": True},
            {"text": "Nothing — with no cooling the mixture never separated "
                     "in the first place", "correct": False,
             "why": "The separating worked perfectly, and the flask proves "
                    "it: the salt is there and the water is not. It is the "
                    "collecting that never happened."},
            {"text": "Salt water — without cooling, salt comes over with the "
                     "vapour as well", "correct": False,
             "why": "Cooling has nothing to do with the salt. Salt cannot "
                    "become a gas at these temperatures whether the condenser "
                    "is cold or not."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s02",
        "band": "standard",
        "text": "A mixture of ethanol and water is distilled to collect the "
                "ethanol. When should the beaker be changed for a fresh one?",
        "options": [
            {"text": "When the thermometer starts to climb from 78 °C "
                     "towards 100 °C", "correct": True},
            {"text": "When the first drops appear, because those first drops "
                     "are the water", "correct": False,
             "why": "The first drops are mostly ethanol — it boils at the "
                    "lower temperature, so it is the one that leaves first."},
            {"text": "As soon as the mixture starts to boil, because both "
                     "liquids come over together", "correct": False,
             "why": "They do not come over together in equal shares. At "
                    "78 °C the vapour is mostly ethanol, because the "
                    "water is not hot enough to boil."},
            {"text": "Never — the ethanol and the water settle into layers in "
                     "the beaker", "correct": False,
             "why": "Ethanol and water mix completely and never form layers. "
                    "The thermometer is the only thing telling you what is "
                    "arriving."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s03",
        "band": "standard",
        "text": "Sea water is heated in a still. The thermometer settles just "
                "above 100 °C, and creeps higher as the run goes on. Why?",
        "options": [
            {"text": "The Bunsen is turned up high, and a bigger flame boils "
                     "a liquid at a higher temperature", "correct": False,
             "why": "A bigger flame boils a liquid faster, not hotter. Once "
                    "it is boiling, the temperature is set by what is in the "
                    "flask."},
            {"text": "The salt is boiling too, and its own high boiling point "
                     "pulls the reading up", "correct": False,
             "why": "The salt is nowhere near boiling — it would need to be "
                    "far hotter than this. It stays a solid dissolved in the "
                    "liquid the whole time."},
            {"text": "Dissolved salt raises the boiling point, and raises it "
                     "further as the solution gets stronger", "correct": True},
            {"text": "Thermometers always read a degree or two high when they "
                     "are held in a vapour", "correct": False,
             "why": "The bulb sits level with the side arm precisely so that "
                    "it reads the vapour honestly. The reading is real, and "
                    "the salt is why."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s04",
        "band": "standard",
        "text": "Boiling sea water gives fresh water, but most new "
                "desalination plants push sea water through a membrane "
                "instead. What is the main reason?",
        "options": [
            {"text": "Boiling leaves salt in the water, and a membrane does "
                     "not", "correct": False,
             "why": "Boiling leaves the salt behind in the tank. Done "
                    "properly, distilled sea water has no salt in it at all."},
            {"text": "A membrane makes fresh water without having to take "
                     "anything at all out of the sea water",
             "correct": False,
             "why": "It takes out exactly the same salt. The two methods "
                    "separate the same two things and differ in what they "
                    "cost to run."},
            {"text": "Boiling cannot be done at the scale a town needs",
             "correct": False,
             "why": "It can, and thermal plants exist that do it. They are "
                    "simply expensive to run compared with a membrane."},
            {"text": "Boiling a tonne of sea water takes far more energy than "
                     "pushing it through a membrane", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-05-h01",
        "band": "harder",
        "text": "A student says distillation is really just a slow filter: "
                "the apparatus holds the salt back and lets the water "
                "through. What is wrong with that?",
        "options": [
            {"text": "Filtering sorts by size and cannot hold back dissolved "
                     "salt at all; distillation works because only one of the "
                     "two can become a gas", "correct": True},
            {"text": "Nothing is wrong — the condenser is the filter, heat "
                     "is what pushes the water through it, and the salt is "
                     "what stays on the other side", "correct": False,
             "why": "The condenser has no holes, and nothing passes through "
                    "its walls or stays on the far side of them. It takes "
                    "heat out of a vapour, which is a different job "
                    "entirely."},
            {"text": "It is the right idea, but filtering would be quicker "
                     "than boiling", "correct": False,
             "why": "Filtering sea water is quick and useless: the salt goes "
                    "straight through with the water, because it is dissolved "
                    "rather than floating."},
            {"text": "Filtering would work on sea water, but only with paper "
                     "fine enough to stop salt", "correct": False,
             "why": "No paper is fine enough. Dissolved salt particles travel "
                    "in among the water particles, so any gap that lets water "
                    "through lets salt through."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h02",
        "band": "harder",
        "text": "A cold plate held just above a pan of hard-boiling sea water "
                "collects drops that taste salty. Held high above the same "
                "pan, it collects drops that taste of nothing. Why the "
                "difference?",
        "options": [
            {"text": "Low down the steam is hotter, and hotter steam can "
                     "carry more salt", "correct": False,
             "why": "No temperature you can reach in a pan makes salt into a "
                    "gas. Hotter steam is still nothing but water particles."},
            {"text": "High up the salt has had time to fall back out of the "
                     "steam", "correct": False,
             "why": "The salt was never in the steam to fall out of it. What "
                    "fell back were droplets of liquid sea water, salt and "
                    "all."},
            {"text": "Low down the plate catches thrown droplets of sea water "
                     "as well as vapour; high up, only vapour reaches it",
             "correct": True},
            {"text": "The high plate was not cold enough to condense the salt "
                     "along with the water", "correct": False,
             "why": "How cold the plate is decides how much water condenses "
                    "on it, never whether salt is present. There is no salt "
                    "in the vapour to condense."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h03",
        "band": "harder",
        "text": "Liquid A boils at 65 °C and liquid B boils at "
                "120 °C. A mixture of the two is distilled, and the "
                "thermometer holds steady near 70 °C. What is arriving "
                "in the beaker?",
        "options": [
            {"text": "Mostly B, because the liquid with the higher boiling "
                     "point is the one driven off first", "correct": False,
             "why": "It is the other way round. A higher boiling point means "
                    "it takes more heat to make it a gas, so B is still in "
                    "the flask at 70 °C."},
            {"text": "Mostly A, because 70 °C is above its boiling point "
                     "and far below B's", "correct": True},
            {"text": "Equal amounts of A and B, because a mixture boils as "
                     "one liquid", "correct": False,
             "why": "A mixture keeps the boiling points of the things in it. "
                    "That is the whole reason two liquids can be separated "
                    "this way."},
            {"text": "Pure A and nothing else, because one still separates "
                     "them completely", "correct": False,
             "why": "Mostly, not purely. Some B always comes over as well, "
                    "which is why getting further needs a fractionating "
                    "column rather than one pass."},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h04",
        "band": "harder",
        "text": "A student's distillate is not salty at all, but there is far "
                "less of it than expected, and the room smells of the "
                "mixture. What is the most likely fault?",
        "options": [
            {"text": "They boiled too hard, so droplets were thrown over into "
                     "the condenser", "correct": False,
             "why": "That fault makes the distillate salty, not scarce — and "
                    "this distillate is clean. Something is leaving the "
                    "apparatus instead of arriving."},
            {"text": "Some of the water was destroyed by the boiling, so "
                     "there was less of it to collect", "correct": False,
             "why": "Boiling destroys nothing. Every particle that left the "
                    "flask is somewhere, and the smell in the room says "
                    "where."},
            {"text": "The thermometer bulb was too low, so the mixture boiled "
                     "at the wrong temperature", "correct": False,
             "why": "Where the bulb sits changes the reading you get, not how "
                    "much comes over. A badly placed bulb misleads you; it "
                    "does not lose you the product."},
            {"text": "The condenser was not cooling well, so much of the "
                     "vapour left through the open end", "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-05-e05",
        "band": "easier",
        "text": "What does it mean to condense a gas?",
        "options": [
            {"text": "To squash it into a smaller space until the particles "
                     "are forced close enough together to touch one another",
             "correct": False,
             "why": "Squashing a gas is a different thing altogether. "
                    "Condensing is done by cooling"},
            {"text": "To make it more concentrated by removing some of it",
             "correct": False,
             "why": "That is the everyday use of the word, as in condensed "
                    "milk. In this lesson it names a change of state"},
            {"text": "To turn it back into a liquid by cooling it",
             "correct": True},
            {"text": "To turn it into a new substance",
             "correct": False,
             "why": "Condensing makes nothing new. The liquid is the same "
                    "substance the gas was"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e06",
        "band": "easier",
        "text": "What is a boiling point?",
        "options": [
            {"text": "The highest temperature a liquid can be heated to "
                     "before the substance itself starts to break down into "
                     "something else",
             "correct": False,
             "why": "Nothing breaks down at a boiling point. The liquid "
                    "simply turns to gas"},
            {"text": "The temperature a liquid has to reach before any of it "
                     "can evaporate",
             "correct": False,
             "why": "A puddle dries at 8 °C. Evaporation happens from the "
                    "surface at any temperature"},
            {"text": "The same temperature for every liquid",
             "correct": False,
             "why": "Different for each one — which is exactly what makes "
                    "liquids separable by distilling"},
            {"text": "The temperature at which a liquid turns to gas "
                     "throughout",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e07",
        "band": "easier",
        "text": "Which piece of the still turns the vapour back into a "
                "liquid?",
        "options": [
            {"text": "The condenser",
             "correct": True},
            {"text": "The flask",
             "correct": False,
             "why": "The flask is where the mixture is boiled. The vapour "
                    "leaves it as a gas"},
            {"text": "The thermometer, which is placed at the side arm so "
                     "that the vapour has to pass over it on its way out",
             "correct": False,
             "why": "The thermometer measures and changes nothing. It is "
                    "there to tell you what is coming over"},
            {"text": "The beaker at the end",
             "correct": False,
             "why": "The beaker collects the liquid once it has already "
                    "condensed further back"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-05-s05",
        "band": "standard",
        "text": "A mixture of ethanol (boiling point 78 °C) and water "
                "(100 °C) is heated in a still. Which comes over first, and "
                "why?",
        "options": [
            {"text": "Water, because there is more of it in the mixture and "
                     "the substance in the majority is always the one that "
                     "boils away first",
             "correct": False,
             "why": "How much there is does not decide the order. The lower "
                    "boiling point comes over first"},
            {"text": "Water, because it boils at the higher temperature",
             "correct": False,
             "why": "A higher boiling point means it takes MORE heating to "
                    "turn to gas, so it comes over later"},
            {"text": "Ethanol, because it boils at the lower temperature",
             "correct": True},
            {"text": "Both at once, because they are mixed",
             "correct": False,
             "why": "Being mixed is what makes the separation possible. The "
                    "vapour at 78 °C is mostly ethanol"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s06",
        "band": "standard",
        "text": "The thermometer bulb sits level with the side arm rather "
                "than down in the liquid. Why is it put there?",
        "options": [
            {"text": "Because a thermometer left in a boiling liquid would be "
                     "broken by the bubbles knocking against the bulb",
             "correct": False,
             "why": "A thermometer sits in boiling liquid quite safely. It is "
                    "moved for what it tells you, not to protect it"},
            {"text": "So it reads the temperature of the room, as a control",
             "correct": False,
             "why": "It is inside the apparatus, in the vapour's path. "
                    "Nothing here is measuring the room"},
            {"text": "Because the liquid in the flask is always hotter than "
                     "its own boiling point",
             "correct": False,
             "why": "A boiling liquid sits at its boiling point. The reading "
                    "that matters is the vapour's"},
            {"text": "So it reads the temperature of the vapour that is "
                     "leaving, which is what tells you what is coming over",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s07",
        "band": "standard",
        "text": "A life raft's emergency kit holds a solar still: a black "
                "tray, a clear cover, and nothing else. How does it give "
                "drinking water?",
        "options": [
            {"text": "The sun evaporates the water slowly and the cool cover "
                     "condenses it, and the salt stays in the tray",
             "correct": True},
            {"text": "The black tray absorbs the salt out of the sea water as "
                     "it warms",
             "correct": False,
             "why": "Nothing absorbs the salt. The water is moved and the "
                    "salt is left behind"},
            {"text": "The cover filters the sea water as it drips through it "
                     "into a channel at the edge",
             "correct": False,
             "why": "Nothing is poured through anything, and a filter cannot "
                    "hold back dissolved salt"},
            {"text": "The sun boils the sea water hard, and boiling destroys "
                     "the salt in it",
             "correct": False,
             "why": "The sun never gets it near boiling, and nothing destroys "
                    "salt. It is left behind"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-05-h05",
        "band": "harder",
        "text": "A fractionating column is described as a still with the same "
                "trick repeated dozens of times up its length. Why does "
                "repeating it help?",
        "options": [
            {"text": "Because each repeat raises the temperature a little "
                     "further up the column",
             "correct": False,
             "why": "A column is COOLER at the top, not hotter. What repeats "
                    "is the boil-and-condense step"},
            {"text": "Because a taller column holds more liquid, so more of "
                     "it can be collected",
             "correct": False,
             "why": "The height is about purity, not about quantity"},
            {"text": "Because each repeat enriches the vapour further, so a "
                     "single pass that only improves the mixture becomes a "
                     "real separation",
             "correct": True},
            {"text": "Because the extra distance gives the salt time to "
                     "settle out on the way up",
             "correct": False,
             "why": "A column separates liquids from each other. No solid is "
                    "travelling up it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h06",
        "band": "harder",
        "text": "A crude oil refinery draws petrol off near the TOP of its "
                "column and bitumen off at the BOTTOM. What does that tell you "
                "about the two?",
        "options": [
            {"text": "Petrol is more valuable, and the most valuable products "
                     "are always taken from the top of a column so that they "
                     "can be piped away first",
             "correct": False,
             "why": "Value has nothing to do with where a substance comes "
                    "off. Boiling point does"},
            {"text": "Bitumen has the lower boiling point, so it condenses "
                     "first at the bottom",
             "correct": False,
             "why": "A LOW boiling point means a substance stays a gas "
                    "longer, so it goes higher before condensing"},
            {"text": "Petrol is lighter than air, so it rises",
             "correct": False,
             "why": "Petrol vapour is heavier than air. What lifts it up the "
                    "column is heat, and what stops it is cooling"},
            {"text": "Petrol has the lower boiling point, so it travels "
                     "furthest up before condensing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h07",
        "band": "harder",
        "text": "Sea water is distilled and left running far longer than "
                "usual. The boiling point in the flask has been creeping up "
                "all along. What happens in the end?",
        "options": [
            {"text": "The solution gets more and more concentrated until salt "
                     "starts to crystallise in the flask",
             "correct": True},
            {"text": "The distillate slowly turns salty, because the "
                     "stronger the solution gets the more of the salt is "
                     "carried over with the vapour",
             "correct": False,
             "why": "Salt cannot become a gas at these temperatures however "
                    "strong the solution is. Only careless boiling throws "
                    "droplets over"},
            {"text": "The flask boils dry and the water is destroyed",
             "correct": False,
             "why": "Nothing is destroyed. Every gram of the water is in the "
                    "beaker as distillate"},
            {"text": "The boiling point falls back to 100 °C once enough "
                     "water has gone",
             "correct": False,
             "why": "It climbs the other way. Less water and the same salt "
                    "makes a stronger solution, which boils higher still"},
        ],
        "figure": None,
    },
]
