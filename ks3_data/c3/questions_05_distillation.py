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

⊕ MRB-338, 12 Sep 2026 — 75 rows appended, 32/32/32. Nothing above was
touched: every id below `e08` / `s08` / `h08` is byte-identical to the row that
has been serving since MRB-335, because `bank_position < 12` is what every
automatic assignment in the estate has already drawn from.

The new rows go WIDE rather than deeper on the same four ideas. The apparatus
is examined as apparatus — the side arm's slope, the counter-current jacket,
the granules, the half-full flask, the open end, the long condenser — and the
practical's real errors are asked from the side a student meets them on (a
bulb clamped above the side arm, a bung in the open end, a run stopped early,
a jacket filled once). Fractional distillation, named in the stretch layer and
in `ks4_becomes` but examined nowhere, now carries a strand of its own: what a
fraction is, why a column is packed, why it is hottest at the bottom, and the
three real columns a student will meet again at KS4 — crude oil, liquid air
and a spirit still. The numbers are real and come out exactly: 3.5% sea water,
35 kg of salt in a cubic metre, 336 kJ against 2260 kJ.

Two things the ladder owns are deliberately NOT re-asked. Rung 2 diagnoses a
salty distillate from droplets thrown over by hard boiling, and rung 4 builds
a survival still out of a pan and a lid; no new row does either. The half-full
flask (`e11`) is the apparatus rule behind the first of those, asked as a rule
rather than as a diagnosis.
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
                "collects drops that dry to a white crust. Held high above "
                "the same pan, it collects drops that dry to nothing. Why "
                "the difference?",
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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-05-e08",
        "band": "easier",
        "text": "Copper sulfate solution is a solution of a blue solid in water. When it is distilled, which part of that solution ends up in the beaker?",
        "options": [
            {
             "text": "The solute, which here is the copper sulfate",
             "correct": False,
             "why": "The solute is the copper sulfate, and it never leaves the flask. It is the part that cannot become a gas",
            },
            {
             "text": "The solvent, which here is the water",
             "correct": True,
            },
            {
             "text": "Both of them, arriving as a weaker blue solution",
             "correct": False,
             "why": "Only one of the two can travel as a gas. A weaker solution would mean some of the solid had come over, and none does",
            },
            {
             "text": "Neither, because the heating makes a new substance",
             "correct": False,
             "why": "Nothing new is made. Both substances are the same at the end as at the start, simply in different places",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e09",
        "band": "easier",
        "text": "Distillation uses two changes of state, one after the other. "
                "Which two, and in which order?",
        "options": [
            {"text": "Gas to liquid in the flask, then liquid to gas in the "
                     "condenser", "correct": False,
             "why": "That is the right pair the wrong way round. Boiling "
                    "comes first, in the flask, and cooling comes second"},
            {"text": "Solid to liquid in the flask, then liquid to gas in the "
                     "condenser", "correct": False,
             "why": "Nothing melts in a still. The mixture is already a "
                    "liquid before the Bunsen is lit"},
            {"text": "Liquid to gas in the flask, then gas to liquid in the "
                     "condenser", "correct": True},
            {"text": "Liquid to gas in the flask, then gas to solid in the "
                     "condenser", "correct": False,
             "why": "The vapour turns back into a liquid, not into a solid. "
                    "Drops of liquid are what run into the beaker"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e10",
        "band": "easier",
        "text": "Anti-bumping granules are dropped into the flask before a "
                "still is heated. What are they for?",
        "options": [
            {"text": "To make the mixture boil smoothly instead of in sudden "
                     "violent bursts", "correct": True},
            {"text": "To lower the boiling point so that the mixture boils "
                     "sooner and the run is quicker", "correct": False,
             "why": "They change no boiling point at all. What they change is "
                    "how steadily the liquid boils"},
            {"text": "To soak up the dissolved solid so that it cannot leave "
                     "the flask with the vapour", "correct": False,
             "why": "The dissolved solid could not leave anyway, so there is "
                    "nothing for them to soak up"},
            {"text": "To spread the heat out so that the glass of the flask "
                     "cannot crack over the flame", "correct": False,
             "why": "They sit in the liquid, not against the glass, and "
                    "protecting the flask is not their job"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e11",
        "band": "easier",
        "text": "A still's flask is never filled more than about half full. "
                "Why not?",
        "options": [
            {"text": "A full flask would boil at a higher temperature than a "
                     "half-full one", "correct": False,
             "why": "How much liquid there is does not change its boiling "
                    "point. A full flask simply takes longer to get there"},
            {"text": "Room is needed above the liquid, or boiling throws "
                     "drops up the neck", "correct": True},
            {"text": "Room is needed above the liquid for the solid to "
                     "dissolve into as it is heated", "correct": False,
             "why": "The solid is already dissolved before any heating "
                    "starts, and it needs no room above the liquid"},
            {"text": "A full flask would cool the vapour before it ever "
                     "reached the condenser", "correct": False,
             "why": "The flask is the hot end of the apparatus. Nothing "
                    "inside it is cooling anything"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e12",
        "band": "easier",
        "text": "A still is used to separate two liquids from one another. "
                "Which property of the two liquids does it depend on?",
        "options": [
            {"text": "They are different colours, so each can be seen "
                     "arriving", "correct": False,
             "why": "Ethanol and water are both colourless and separate "
                    "perfectly well. Colour decides nothing here"},
            {"text": "One dissolves in water and the other does not",
             "correct": False,
             "why": "Two liquids that mix completely are exactly the case "
                    "distillation is for. Not mixing is what lets you pour "
                    "one off instead"},
            {"text": "One is heavier than the other, so it sinks to the "
                     "bottom", "correct": False,
             "why": "Liquids that separate into layers need no still at all. "
                    "A tap at the bottom would do it"},
            {"text": "They boil at different temperatures", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e13",
        "band": "easier",
        "text": "In a laboratory still, which part carries the vapour away "
                "from the flask towards the condenser?",
        "options": [
            {"text": "The side arm, sloping down from the neck of the flask",
             "correct": True},
            {"text": "The thermometer, which the vapour passes down the "
                     "inside of", "correct": False,
             "why": "A thermometer is sealed glass with nothing flowing "
                    "through it. It measures and carries nothing"},
            {"text": "The outer jacket, which the vapour flows along on its "
                     "way through", "correct": False,
             "why": "The outer jacket holds the cold water. The vapour "
                    "travels through the inner tube it surrounds"},
            {"text": "The beaker at the open end, which draws the vapour "
                     "towards it", "correct": False,
             "why": "The beaker sits at the end and collects. Nothing about "
                    "it pulls vapour anywhere"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e14",
        "band": "easier",
        "text": "The collecting end of a still is left open to the air rather "
                "than sealed shut. Why must it be left open?",
        "options": [
            {"text": "So that air can get in and do the cooling that the "
                     "condenser cannot manage", "correct": False,
             "why": "The cold water jacket does the cooling. Air getting in "
                    "is not part of the method"},
            {"text": "So that the dissolved solid has somewhere to escape to "
                     "as the run goes on", "correct": False,
             "why": "The dissolved solid stays in the flask throughout and "
                    "never needs anywhere to go"},
            {"text": "So that pressure cannot build up inside sealed glass",
             "correct": True},
            {"text": "So that any extra distillate can evaporate away again "
                     "once the beaker is full", "correct": False,
             "why": "Losing the distillate is the opposite of the point. The "
                    "whole method exists to collect it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e15",
        "band": "easier",
        "text": "What does fractional distillation separate?",
        "options": [
            {"text": "Solid lumps from the liquid they are floating in",
             "correct": False,
             "why": "That is filtration, and it needs no heat at all. "
                    "Floating lumps never dissolved in the first place"},
            {"text": "Coloured dyes from one another on a sheet of paper",
             "correct": False,
             "why": "That is chromatography, which uses a solvent creeping "
                    "up paper rather than boiling points"},
            {"text": "Two liquids that will not mix, sitting in two layers",
             "correct": False,
             "why": "Layers are poured or tapped apart and need no heat. "
                    "Distilling is for liquids that have mixed completely"},
            {"text": "Two or more liquids that mix, by their boiling points",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e16",
        "band": "easier",
        "text": "Air is cooled until it turns into a liquid, then warmed "
                "slowly. Nitrogen boils at −196 °C and oxygen boils at "
                "−183 °C. Which of the two comes off first?",
        "options": [
            {"text": "Nitrogen, because it boils at the lower temperature",
             "correct": True},
            {"text": "Oxygen, because it boils at the lower temperature",
             "correct": False,
             "why": "−183 °C is the higher of the two, because it is the "
                    "nearer to zero. Oxygen needs more warming, not less"},
            {"text": "Oxygen, because there is far less of it in air",
             "correct": False,
             "why": "How much of it there is decides nothing about the order. "
                    "Boiling point does"},
            {"text": "Neither, because a mixture boils away all at once",
             "correct": False,
             "why": "A mixture keeps the boiling points of the substances in "
                    "it, which is the whole reason this works"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e17",
        "band": "easier",
        "text": "A school technician needs water with nothing dissolved in it "
                "at all, starting from ordinary tap water. Which method gives "
                "it?",
        "options": [
            {"text": "Pour it through a clean filter paper in a funnel",
             "correct": False,
             "why": "Filter paper stops undissolved bits. Everything "
                    "dissolved goes straight through with the water"},
            {"text": "Distil it and keep the liquid that condenses",
             "correct": True},
            {"text": "Leave it to stand overnight and pour off the clear top",
             "correct": False,
             "why": "Standing lets undissolved bits settle. A dissolved solid "
                    "is spread evenly and never settles out"},
            {"text": "Warm it gently to drive the dissolved gas out of it",
             "correct": False,
             "why": "Warming does remove dissolved gas, but the dissolved "
                    "solids stay exactly where they were"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e18",
        "band": "easier",
        "text": "In a fractionating column, what is meant by a fraction?",
        "options": [
            {"text": "A fixed share of the mixture, such as a quarter of it",
             "correct": False,
             "why": "That is the everyday meaning of the word. Here it names "
                    "what was collected, not how much"},
            {"text": "The part of the mixture that refuses to boil at all",
             "correct": False,
             "why": "What never boils drains out at the bottom, and it is one "
                    "fraction among many rather than the meaning of the word"},
            {"text": "A group of substances that boil over a similar range of "
                     "temperatures", "correct": True},
            {"text": "A substance that has been broken into smaller pieces by "
                     "the heating", "correct": False,
             "why": "Nothing is broken up. Distilling moves substances about "
                    "and changes none of them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e19",
        "band": "easier",
        "text": "A crude oil fractionating column at a refinery is tens of "
                "metres tall. Where along its height is it hottest?",
        "options": [
            {"text": "At the top, because heat always rises to the highest "
                     "point available", "correct": False,
             "why": "The top is the coolest part, which is why only the "
                    "substances with the lowest boiling points reach it"},
            {"text": "In the middle, where the greatest number of fractions "
                     "come off", "correct": False,
             "why": "The middle is warm but not the hottest. The temperature "
                    "falls steadily from the bottom upwards"},
            {"text": "The same all the way up, so that every fraction is "
                     "heated equally", "correct": False,
             "why": "A column with one temperature would separate nothing. "
                    "The difference in temperature is what sorts them"},
            {"text": "At the bottom, where the heated crude oil goes in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e20",
        "band": "easier",
        "text": "Is any new substance made when a mixture is distilled?",
        "options": [
            {"text": "Yes — the boiling breaks the mixture down into new "
                     "substances", "correct": False,
             "why": "Boiling separates what was already there. Breaking "
                    "substances down is a chemical change and this is not one"},
            {"text": "No — both substances are unchanged, simply in different "
                     "places", "correct": True},
            {"text": "Yes — the water becomes steam, and steam is a different "
                     "substance", "correct": False,
             "why": "Steam is water as a gas. Same substance, different state"},
            {"text": "No, unless the flask is boiled dry, which makes a new "
                     "solid", "correct": False,
             "why": "The solid that appears was dissolved in the liquid all "
                    "along. Nothing made it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e21",
        "band": "easier",
        "text": "A still is run for an hour and a beaker of clear liquid "
                "collects at the open end. Where did that liquid come from?",
        "options": [
            {"text": "From the cold water in the outer jacket, which seeps "
                     "slowly into the tube", "correct": False,
             "why": "The jacket is sealed and its water never meets the "
                    "vapour. It only takes heat away through the glass"},
            {"text": "From the air inside the apparatus, which the cooling "
                     "squeezes the water out of", "correct": False,
             "why": "There is far too little water in a tube of air to fill a "
                    "beaker, and the air is not what is being cooled"},
            {"text": "From the flask, having travelled there as a gas",
             "correct": True},
            {"text": "It was made by the heating, out of the solid left in "
                     "the flask", "correct": False,
             "why": "Heating makes no new substance. Every drop was liquid in "
                    "the flask before the Bunsen was lit"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e22",
        "band": "easier",
        "text": "Sea water is about 3.5% dissolved salts by mass, so 1000 g "
                "of it holds 35 g of salt and 965 g of water. All the water "
                "is distilled off and collected. What mass is in the beaker?",
        "options": [
            {"text": "965 g", "correct": True},
            {"text": "1000 g", "correct": False,
             "why": "That is the whole sea water, salt included. The salt "
                    "stays in the flask, so it cannot be in the beaker"},
            {"text": "35 g", "correct": False,
             "why": "That is the mass of the salt, which is the part left "
                    "behind rather than the part collected"},
            {"text": "482.5 g", "correct": False,
             "why": "That is half the water. Distilling collects all of it, "
                    "not half"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e23",
        "band": "easier",
        "text": "Before air can be separated by fractional distillation, what "
                "has to be done to it first?",
        "options": [
            {"text": "It has to be warmed to well above 100 °C",
             "correct": False,
             "why": "Warming air separates nothing. The gases in it stay "
                    "mixed however hot they get"},
            {"text": "It has to be squashed hard until it turns into a solid",
             "correct": False,
             "why": "A still works on liquids. Air is taken down to a liquid, "
                    "not to a solid"},
            {"text": "It has to be dissolved in water to hold it still",
             "correct": False,
             "why": "Only a little air dissolves in water, and what dissolves "
                    "could not then be boiled apart"},
            {"text": "It has to be cooled until it becomes a liquid",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e24",
        "band": "easier",
        "text": "Blue ink is distilled. What happens to the ink still in the flask as the run goes on?",
        "options": [
            {
             "text": "It gets paler, as more and more of the dye is carried off",
             "correct": False,
             "why": "None of the dye is carried off. It is a solid dissolved in the water and it cannot become a gas",
            },
            {
             "text": "It gets darker, as the same dye is left in less water",
             "correct": True,
            },
            {
             "text": "It stays exactly as it was, because the dye and the water leave the flask in step with one another",
             "correct": False,
             "why": "The dye leaves the flask at no rate at all. It cannot become a gas, so the water goes, the dye stays, and the ink gets more concentrated.",
            },
            {
             "text": "It turns colourless, as the heat destroys the dye in it",
             "correct": False,
             "why": "Nothing is destroyed. The dye ends the run as a ring of solid you can still see",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e25",
        "band": "easier",
        "text": "Cold water is running through a still's condenser, but the "
                "Bunsen has not been lit. Nothing collects. Why not?",
        "options": [
            {"text": "No vapour is being made, so there is nothing to cool",
             "correct": True},
            {"text": "The cooling water has to be turned off before anything "
                     "can arrive in the beaker", "correct": False,
             "why": "The cooling is the half of the method that collects. "
                    "Turning it off is how you end up with nothing"},
            {"text": "The condenser needs a few minutes to fill up before it "
                     "will pass anything on", "correct": False,
             "why": "The jacket fills at once, and a full jacket with no heat "
                    "under the flask still collects nothing"},
            {"text": "The mixture has to be cooled first before it can be "
                     "made to boil", "correct": False,
             "why": "Cooling a mixture takes it further from boiling, not "
                    "nearer to it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e26",
        "band": "easier",
        "text": "Sodium chloride melts at about 800 °C and boils at about "
                "1400 °C. What does that explain about distilling sea water?",
        "options": [
            {"text": "That the flask has to be heated past 800 °C for the "
                     "separation to work", "correct": False,
             "why": "The flask only has to reach the water's boiling point. "
                    "The salt is meant to stay behind, not to melt"},
            {"text": "That the salt cannot become a gas at 100 °C, so it "
                     "stays in the flask", "correct": True},
            {"text": "That the salt boils away long before the water does",
             "correct": False,
             "why": "1400 °C is far above 100 °C, so the salt is the one that "
                    "cannot boil away at all here"},
            {"text": "That the salt has to be filtered out before boiling can "
                     "start", "correct": False,
             "why": "Dissolved salt goes straight through filter paper, and "
                    "the still deals with it without any help"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e27",
        "band": "easier",
        "text": "What does the word desalination mean?",
        "options": [
            {"text": "Adding salt to fresh water so that it keeps for longer",
             "correct": False,
             "why": "That is salting food, and it is the opposite operation. "
                    "Desalination takes salt away"},
            {"text": "Filtering the sand and grit out of sea water before it "
                     "is used", "correct": False,
             "why": "That removes what is floating in it. The dissolved salt "
                    "goes straight through a filter"},
            {"text": "Boiling sea water dry so that the salt can be sold",
             "correct": False,
             "why": "That is how sea salt is made, and it throws away the "
                    "water. Desalination is after the water"},
            {"text": "Taking the dissolved salts out of sea water to give "
                     "fresh water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e28",
        "band": "easier",
        "text": "Pure water boils at exactly 100 °C. A student's distillate "
                "from sea water boils at exactly 100 °C and holds there. What "
                "does that show?",
        "options": [
            {"text": "That the thermometer is faulty, since a distillate "
                     "always boils below 100 °C", "correct": False,
             "why": "There is nothing about being a distillate that lowers a "
                    "boiling point. The reading is real"},
            {"text": "That the distillate is pure water, with nothing "
                     "dissolved in it", "correct": True},
            {"text": "That the distillate is still slightly salty, since salt "
                     "water also boils at 100 °C", "correct": False,
             "why": "Salt water boils above 100 °C, and the more salt there "
                    "is the higher it goes. 100 °C exactly rules salt out"},
            {"text": "That the flask was boiled dry, which is the only way to "
                     "reach exactly 100 °C", "correct": False,
             "why": "Boiling the flask dry changes what is in the flask, not "
                    "the boiling point of what was collected"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e29",
        "band": "easier",
        "text": "Two liquids have boiling points so close together that a "
                "simple still barely separates them. What would be added to "
                "the apparatus?",
        "options": [
            {"text": "A fractionating column, standing above the flask",
             "correct": True},
            {"text": "A second condenser, joined on after the first one",
             "correct": False,
             "why": "Cooling the vapour twice collects the same mixture "
                    "twice. Cooling is not the step that is failing"},
            {"text": "A longer side arm, to give the vapour further to travel",
             "correct": False,
             "why": "Distance alone sorts nothing. What is needed is a "
                    "surface for the vapour to condense and re-boil on"},
            {"text": "A larger flask, so that more of the mixture is heated "
                     "at once", "correct": False,
             "why": "A bigger batch gives more of the same poor separation, "
                    "not a better one"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e30",
        "band": "easier",
        "text": "A condenser is built as a long tube inside a long water "
                "jacket, rather than a short one. Why is it made long?",
        "options": [
            {"text": "So that the thermometer can be fitted along the length "
                     "of it", "correct": False,
             "why": "The thermometer belongs back at the side arm, where the "
                    "vapour leaves the flask"},
            {"text": "So that the vapour is cooled for longer, and more of it "
                     "turns to liquid", "correct": True},
            {"text": "So that the vapour slows down enough for the heavier "
                     "parts to drop out of it", "correct": False,
             "why": "Nothing drops out of a vapour on the way. It is cooling, "
                    "not slowing, that turns it back into a liquid"},
            {"text": "So that the pressure inside builds up enough to push "
                     "the liquid along", "correct": False,
             "why": "The far end is open to the air, so no pressure builds. "
                    "The liquid runs down the slope"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e31",
        "band": "easier",
        "text": "A still separating ethanol from water is left running after "
                "all the ethanol has come over. What arrives in the beaker "
                "from then on?",
        "options": [
            {"text": "Nothing more at all, because the separation is finished",
             "correct": False,
             "why": "There is still water in the flask, and the flame is "
                    "still under it. It boils in its turn"},
            {"text": "The ethanol again, arriving more slowly than before",
             "correct": False,
             "why": "The ethanol has already gone. There is none left in the "
                    "flask to come over a second time"},
            {"text": "Mostly water, now that the flask is hot enough to boil "
                     "it", "correct": True},
            {"text": "A mixture of the two, in the same proportions as at the "
                     "start", "correct": False,
             "why": "The starting proportions are long gone. The ethanol left "
                    "first and the flask is nearly all water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-e32",
        "band": "easier",
        "text": "Distillation is described as two jobs rather than one. What "
                "are the two?",
        "options": [
            {"text": "Boil the mixture to separate it, then cool the vapour "
                     "to collect it", "correct": True},
            {"text": "Filter the mixture to clean it, then boil it to collect "
                     "the liquid", "correct": False,
             "why": "Nothing is filtered in a still, and filtering would not "
                    "touch a dissolved solid anyway"},
            {"text": "Boil the mixture to separate it, then boil it a second "
                     "time to purify it", "correct": False,
             "why": "The second job is cooling, not more boiling. Without it "
                    "the vapour simply leaves"},
            {"text": "Dissolve the solid first, then evaporate the liquid to "
                     "leave it behind", "correct": False,
             "why": "That describes evaporation, which keeps the solid and "
                    "throws the liquid away"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c3-05-s08",
        "band": "standard",
        "text": "While one pure substance is coming over from a still, the thermometer holds at one reading instead of climbing, even though the Bunsen is still burning. Why does it hold?",
        "options": [
            {
             "text": "While a liquid is boiling, the heat going in turns it to gas rather than raising its temperature",
             "correct": True,
            },
            {
             "text": "The thermometer has reached the highest reading its scale is able to give, so it cannot climb any further whatever the flask does",
             "correct": False,
             "why": "A laboratory thermometer reads far higher than this. It is the temperature that has stopped rising, not the scale",
            },
            {
             "text": "The Bunsen is putting in exactly as much heat as the condenser is taking out",
             "correct": False,
             "why": "The two are at opposite ends of the apparatus and do not balance each other. The flask is boiling either way",
            },
            {
             "text": "The vapour flowing past the bulb keeps it at a steady cool temperature",
             "correct": False,
             "why": "The vapour is the hottest thing passing the bulb. It is what the bulb is there to measure",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s09",
        "band": "standard",
        "text": "Cold water enters a condenser's jacket at the end furthest "
                "from the flask and leaves at the end nearest to it, so it "
                "flows against the vapour. Why is it plumbed that way?",
        "options": [
            {"text": "So that the warm water leaves before it can reach the "
                     "flask and heat it", "correct": False,
             "why": "The jacket never touches the flask. Where the water goes "
                    "afterwards changes nothing about the cooling"},
            {"text": "So that the vapour meets colder water the further along "
                     "it travels", "correct": True},
            {"text": "So that the cooling water can mix with the vapour at "
                     "the far end", "correct": False,
             "why": "The two never meet. The jacket is sealed away from the "
                    "inner tube the vapour travels down"},
            {"text": "So that the water runs downhill and no pump is needed "
                     "to move it", "correct": False,
             "why": "A condenser is plumbed either way up and the tap "
                    "supplies the pressure. The direction is about cooling"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s10",
        "band": "standard",
        "text": "A student pushes a rubber bung into the open end of a still "
                "so that no vapour can escape into the room. Why is that "
                "dangerous?",
        "options": [
            {"text": "The distillate would be forced back and boil a second "
                     "time in the flask", "correct": False,
             "why": "The danger comes long before that. Sealed glass with a "
                    "flame under it is the problem"},
            {"text": "The flask would cool so fast that the glass would crack "
                     "across", "correct": False,
             "why": "Sealing the end keeps heat in rather than letting it "
                    "out. Nothing cools faster"},
            {"text": "Pressure would build up inside sealed glass until "
                     "something burst", "correct": True},
            {"text": "The dissolved salt would be forced over into the beaker "
                     "with the vapour", "correct": False,
             "why": "Salt cannot become a gas at this temperature whatever "
                    "the pressure in the apparatus is"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s11",
        "band": "standard",
        "text": "A fermented liquid is about 12% ethanol in water. Distilling "
                "it gives a liquid with a far higher share of ethanol. "
                "Explain why.",
        "options": [
            {"text": "The heating turns some of the water into ethanol, so "
                     "there is more of it", "correct": False,
             "why": "Distilling makes no new substance. Every drop of the "
                    "ethanol was there before the flask was heated"},
            {"text": "The water is destroyed by the boiling, leaving the "
                     "ethanol behind", "correct": False,
             "why": "Nothing is destroyed. The water stays in the flask until "
                    "the temperature climbs enough to boil it too"},
            {"text": "The ethanol is heavier, so it runs down into the beaker "
                     "first", "correct": False,
             "why": "Both travel as a gas, so weight decides nothing. What "
                    "separates them is the temperature each one boils at"},
            {"text": "Ethanol boils lower, so the first vapour is richer in "
                     "it than the flask", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s12",
        "band": "standard",
        "text": "An ethanol and water mixture is distilled into two beakers: "
                "the first collected while the thermometer held near 78 °C, "
                "the second while it held near 100 °C. What is in each?",
        "options": [
            {"text": "First beaker mostly ethanol, second beaker mostly water",
             "correct": True},
            {"text": "First beaker mostly water, second beaker mostly ethanol",
             "correct": False,
             "why": "That is the order reversed. 78 °C is the ethanol's "
                    "boiling point, so the ethanol goes first"},
            {"text": "Both beakers hold the same mixture as the flask started "
                     "with", "correct": False,
             "why": "If that were so the still would have separated nothing. "
                    "The thermometer reading changed because the contents did"},
            {"text": "First beaker mostly water, second beaker a mixture of "
                     "the two", "correct": False,
             "why": "Nothing comes over at 78 °C except what boils at about "
                    "78 °C, and water is not close to boiling there"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s13",
        "band": "standard",
        "text": "A beaker of distillate from a sea water run is left "
                "uncovered on a warm bench for a week. It is found completely "
                "empty and clean. What happened to the liquid?",
        "options": [
            {"text": "It soaked back through the glass into the salt left in "
                     "the flask", "correct": False,
             "why": "Glass lets nothing through, and the flask is a separate "
                    "piece of apparatus altogether"},
            {"text": "It evaporated into the room, as any water left standing "
                     "does", "correct": True},
            {"text": "It turned back into sea water, which then dried to a "
                     "crust of salt", "correct": False,
             "why": "There is no salt in it to reappear, which is exactly why "
                    "the beaker is clean rather than crusted"},
            {"text": "It was destroyed slowly by the warmth of the bench",
             "correct": False,
             "why": "Warmth destroys no water. It moves it into the air as a "
                    "gas, where it still exists"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s14",
        "band": "standard",
        "text": "In a refinery column, refinery gas comes off below 25 °C, "
                "petrol between 40 °C and 100 °C, kerosene between 150 °C and "
                "250 °C, and diesel between 250 °C and 350 °C. Which is drawn "
                "off highest up the column?",
        "options": [
            {"text": "Diesel", "correct": False,
             "why": "Diesel has the highest boiling range of the four, so it "
                    "condenses soonest and comes off near the bottom"},
            {"text": "Kerosene", "correct": False,
             "why": "Kerosene condenses in the middle of the column, below "
                    "both petrol and refinery gas"},
            {"text": "Refinery gas", "correct": True},
            {"text": "Petrol", "correct": False,
             "why": "Petrol goes high, but not highest. Refinery gas boils "
                    "lower still and so travels past it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s15",
        "band": "standard",
        "text": "A chemist has copper sulfate solution and wants to end up with BOTH the dry copper sulfate and the water it was dissolved in. Which method gives both?",
        "options": [
            {
             "text": "Filtration, keeping the residue and the filtrate separately",
             "correct": False,
             "why": "Filter paper cannot hold back a dissolved solid, so the solution would pass through unchanged",
            },
            {
             "text": "Evaporating the solution to dryness in a dish",
             "correct": False,
             "why": "That gives the solid and lets the water go into the room, which is one of the two and not both",
            },
            {
             "text": "Leaving it on a windowsill to crystallise slowly",
             "correct": False,
             "why": "Slow evaporation gives better crystals, but the water still goes into the air uncollected",
            },
            {
             "text": "Distillation, collecting the water and keeping the solid",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s16",
        "band": "standard",
        "text": "A student distils 100 cm³ of sea water, collects 60 cm³ of "
                "distillate, then stops and says the other 40 cm³ has "
                "disappeared. Where is it actually?",
        "options": [
            {"text": "Still in the flask, as a smaller and saltier volume of "
                     "solution", "correct": True},
            {"text": "Lost into the room, because that much always escapes "
                     "past the condenser", "correct": False,
             "why": "A working condenser catches what reaches it. Stopping "
                    "early is what left the rest behind"},
            {"text": "Destroyed by the boiling, which is why it cannot be "
                     "collected", "correct": False,
             "why": "Boiling destroys nothing. The run was simply stopped "
                    "before the rest of the water had been boiled off"},
            {"text": "Soaked into the glass of the flask and the side arm",
             "correct": False,
             "why": "Glass absorbs no liquid. What is unaccounted for is "
                    "sitting in the flask where it started"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s17",
        "band": "standard",
        "text": "Vapour leaves the flask of a still at about 100 °C, yet the "
                "distillate arriving in the beaker is only lukewarm. Explain "
                "why.",
        "options": [
            {"text": "The vapour cools by mixing with the cold air at the "
                     "open end", "correct": False,
             "why": "It has already condensed by then. The cooling happens "
                    "inside the condenser, not in the air"},
            {"text": "The beaker is cold, and it is the beaker that does the "
                     "cooling", "correct": False,
             "why": "The liquid is already cool when it arrives. A beaker "
                    "sitting on the bench takes very little heat out"},
            {"text": "The condenser took heat out of it, first to condense it "
                     "and then to cool it further", "correct": True},
            {"text": "The liquid in the beaker is a different substance from "
                     "the vapour, and a cooler one", "correct": False,
             "why": "It is the same substance in a different state. Nothing "
                    "changed on the way except its temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s18",
        "band": "standard",
        "text": "The side arm of a still slopes downwards from the flask "
                "towards the condenser. Why is it built at that angle?",
        "options": [
            {"text": "So that hot vapour is forced to travel uphill and cools "
                     "as it climbs", "correct": False,
             "why": "The slope runs the other way. The vapour travels "
                    "downwards, and the jacket does the cooling"},
            {"text": "So that anything that condenses runs forward rather "
                     "than back into the flask", "correct": True},
            {"text": "So that the dissolved solid slides back down into the "
                     "flask instead of travelling on", "correct": False,
             "why": "The dissolved solid never enters the side arm. It cannot "
                    "become a gas, so it never leaves the liquid"},
            {"text": "So that the thermometer can be read from the side of "
                     "the bench more easily", "correct": False,
             "why": "The thermometer sits in the neck of the flask, and "
                    "reading it is not what sets the angle"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s19",
        "band": "standard",
        "text": "Two liquids in a mixture boil at 78 °C and 82 °C. One pass "
                "through a simple still barely separates them. Explain why, "
                "and say what would do better.",
        "options": [
            {"text": "The two boiling points are far too close, so the vapour "
                     "carries plenty of both; a fractionating column is "
                     "needed", "correct": True},
            {"text": "Neither liquid can boil until the other one does, so "
                     "a hotter flame is needed to start them both off",
             "correct": False,
             "why": "Each liquid boils at its own temperature whatever the "
                    "other does, and a hotter flame changes neither"},
            {"text": "The still is working properly, and a second "
                     "identical pass through the same apparatus would finish "
                     "the job off completely", "correct": False,
             "why": "A second identical pass improves it only slightly, which "
                    "is why a column repeats the step dozens of times"},
            {"text": "Liquids this close in boiling point cannot be separated "
                     "by any method at all", "correct": False,
             "why": "A fractionating column separates pairs far closer than "
                    "four degrees apart every day in industry"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s20",
        "band": "standard",
        "text": "A large desalination plant returns a very concentrated salt "
                "solution to the sea beside its outfall. Suggest why that is "
                "a problem for the sea life living there.",
        "options": [
            {"text": "The water there becomes far saltier than normal, which "
                     "many living things cannot survive", "correct": True},
            {"text": "The returned water is pure, so it makes the sea around "
                     "the outfall too fresh", "correct": False,
             "why": "The pure water is what the plant sells. What goes back "
                    "is the salt left over, in less water than before"},
            {"text": "The salt has been changed into a new substance by the "
                     "boiling", "correct": False,
             "why": "Distilling changes no substance. The salt going back is "
                    "the same salt that came in"},
            {"text": "The returned water carries the fuel the plant burned to "
                     "boil it", "correct": False,
             "why": "The fuel is burned in a separate boiler and never "
                    "reaches the sea water at all"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s21",
        "band": "standard",
        "text": "A simple still run on ethanol and water is honestly "
                "described as giving mostly ethanol rather than pure ethanol. "
                "What else is in that distillate?",
        "options": [
            {"text": "Nothing else — mostly is just a careful way of saying "
                     "pure", "correct": False,
             "why": "The word is doing real work. A single pass enriches the "
                    "mixture without ever finishing the job"},
            {"text": "Some water, which comes over along with the ethanol",
             "correct": True},
            {"text": "Some of the ethanol, changed by the heat into a "
                     "different substance", "correct": False,
             "why": "Distilling changes no substance. Whatever arrives is one "
                    "of the two that went in"},
            {"text": "Some of the cooling water, joining it inside the "
                     "condenser", "correct": False,
             "why": "The jacket is sealed away from the inner tube, so its "
                    "water never reaches the distillate"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s22",
        "band": "standard",
        "text": "A student distils 250 cm³ of sea water to dryness. Every 100 cm³ of that sea water holds 3.5 g of dissolved salt. What mass of salt is left in the flask?",
        "options": [
            {
             "text": "3.5 g",
             "correct": False,
             "why": "That is the salt in 100 cm³. There is two and a half times as much sea water as that",
            },
            {
             "text": "0.875 g",
             "correct": False,
             "why": "That is 3.5 g quartered. 250 cm³ is two and a half times 100 cm³, so the 3.5 g must be multiplied by 2.5, not divided by anything.",
            },
            {
             "text": "8.75 g",
             "correct": True,
            },
            {
             "text": "87.5 g",
             "correct": False,
             "why": "That is the right figures with the decimal point in the wrong place, ten times too large",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s23",
        "band": "standard",
        "text": "Nitrogen boils at −196 °C and oxygen at −183 °C. Explain "
                "why liquid air is separated in a tall fractionating column "
                "rather than in one simple still.",
        "options": [
            {"text": "Because a simple still cannot be built to work at "
                     "temperatures that low", "correct": False,
             "why": "Cold apparatus is not the difficulty. It is the two "
                    "boiling points being so close together"},
            {"text": "Because the column is what cools the air down enough to "
                     "become a liquid", "correct": False,
             "why": "The air is already a liquid before it enters. The column "
                    "sorts it rather than cooling it"},
            {"text": "Because nitrogen and oxygen are gases, and gases cannot "
                     "be distilled at all", "correct": False,
             "why": "Once they are liquids they distil like any other "
                    "liquids, which is exactly how this is done"},
            {"text": "Because the two boil only 13 degrees apart, so one pass "
                     "gives plenty of both", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s24",
        "band": "standard",
        "text": "A ship makes its fresh water by distilling sea water with "
                "waste heat from the engine. Why is that cheaper than a still "
                "that burns fuel of its own?",
        "options": [
            {"text": "The heat is produced anyway, and would otherwise be "
                     "thrown away", "correct": True},
            {"text": "Engine heat is hotter, so far less of it is needed to "
                     "boil the same sea water", "correct": False,
             "why": "The sea water still has to be boiled, which takes the "
                    "same heat from any source. What is saved is the fuel"},
            {"text": "A still driven by waste heat needs no condenser, so "
                     "there is less to run", "correct": False,
             "why": "Every still needs cooling to collect anything. Where the "
                    "heat came from changes nothing about that"},
            {"text": "Sea water taken from the open ocean is much less salty "
                     "than water near a coast", "correct": False,
             "why": "How salty the water is barely changes the cost, and it "
                    "is not what the waste heat is saving"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s25",
        "band": "standard",
        "text": "Salt is won from an underground bed by pumping water down, "
                "bringing the brine back up, and evaporating it. Why is it "
                "evaporated rather than distilled?",
        "options": [
            {"text": "Because distilling a brine leaves the salt too wet to "
                     "sell", "correct": False,
             "why": "Distilling would leave the salt just as dry. The two "
                    "methods leave the flask in the same state"},
            {"text": "Because the salt is the product, so collecting water "
                     "nobody wants is a wasted cost", "correct": True},
            {"text": "Because brine is too concentrated to be boiled in a "
                     "still at all", "correct": False,
             "why": "Brine boils perfectly well, a little above 100 °C. "
                    "Concentration is no barrier to distilling it"},
            {"text": "Because distilling would break the salt down before it "
                     "could be collected", "correct": False,
             "why": "Nothing breaks down. Salt would need to be thousands of "
                    "degrees hotter before anything happened to it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s26",
        "band": "standard",
        "text": "A mixture of methanol (boiling point 65 °C) and water is "
                "distilled. What reading does the thermometer hold steady at "
                "while the first liquid is coming over?",
        "options": [
            {"text": "About 100 °C", "correct": False,
             "why": "That is the water's boiling point, and the water is the "
                    "one still in the flask at this stage"},
            {"text": "About 82.5 °C", "correct": False,
             "why": "That is the average of the two boiling points, and a "
                    "still does not average them. It takes them in turn"},
            {"text": "About 65 °C", "correct": True},
            {"text": "About 165 °C", "correct": False,
             "why": "That adds the two boiling points together. A mixture "
                    "never boils higher than both of the things in it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s27",
        "band": "standard",
        "text": "A student distilling an ethanol and water mixture never "
                "changes the beaker, and lets the run go all the way to the "
                "end. What is in that single beaker?",
        "options": [
            {"text": "Only the ethanol, because the water never left the "
                     "flask at all", "correct": False,
             "why": "The water boils too, once the flask gets hot enough. "
                    "Running to the end brings it over as well"},
            {"text": "Only the water, because the ethanol escaped through the "
                     "open end", "correct": False,
             "why": "A working condenser catches the ethanol first. It is in "
                    "the beaker, under the water that followed it"},
            {"text": "Two clear layers, with the ethanol floating on the "
                     "water", "correct": False,
             "why": "Ethanol and water mix completely and never settle into "
                    "layers, however long they stand"},
            {"text": "Both liquids, mixed together again — nothing has been "
                     "separated", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s28",
        "band": "standard",
        "text": "A student clamps the thermometer so the bulb sits high in "
                "the neck of the flask, well above the side arm and out of "
                "the vapour's path. What happens to the reading?",
        "options": [
            {"text": "It reads low, because the bulb is not in the stream of "
                     "vapour leaving", "correct": True},
            {"text": "It reads high, because the neck is the hottest part of "
                     "the whole apparatus", "correct": False,
             "why": "The hottest place is the boiling liquid below. The neck "
                    "is cooler the further up it you go"},
            {"text": "It reads correctly, because the whole flask sits at one "
                     "temperature throughout", "correct": False,
             "why": "A flask over a flame is hot at the bottom and cooler at "
                    "the top, which is why placement matters"},
            {"text": "It gives no reading at all, because there is no liquid "
                     "touching the bulb", "correct": False,
             "why": "A thermometer reads whatever surrounds it, gas included. "
                    "The trouble is which gas it is reading"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s29",
        "band": "standard",
        "text": "Sea water and ink both leave a solid behind in the flask, "
                "but an ethanol and water mixture leaves a liquid behind. "
                "Explain the difference.",
        "options": [
            {"text": "The ethanol mixture is not really a mixture, so nothing "
                     "can be left behind", "correct": False,
             "why": "Two liquids that mix are a mixture, and the still "
                    "separates them exactly as it separates the others"},
            {"text": "In the first two a dissolved solid is left; in the "
                     "third both parts are liquids", "correct": True},
            {"text": "The ethanol mixture is heated too gently for any solid "
                     "to form in the flask", "correct": False,
             "why": "There was no solid in it to begin with. How hard it is "
                    "heated cannot produce one"},
            {"text": "In the first two the solid is made by the boiling, "
                     "which the third has none of", "correct": False,
             "why": "The solid was dissolved in the liquid before any heating "
                    "started. Boiling only uncovers it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s30",
        "band": "standard",
        "text": "One still is used for sea water, for blue ink, and for a mixture of ethanol and water. What do all three separations have in common?",
        "options": [
            {
             "text": "In each one the separation needs the mixture to be filtered first",
             "correct": False,
             "why": "Nothing is filtered in a still, and filter paper would not touch a dissolved solid in any case.",
            },
            {
             "text": "In each one the liquid collected is completely pure",
             "correct": False,
             "why": "The ethanol run gives mostly ethanol, not pure ethanol. One pass is not enough for that",
            },
            {
             "text": "In each one, one part becomes a gas at a lower temperature than the rest",
             "correct": True,
            },
            {
             "text": "In each one the condenser takes the dissolved substance out of the vapour",
             "correct": False,
             "why": "The condenser removes heat and nothing else. The dissolved substance never entered the vapour",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s31",
        "band": "standard",
        "text": "Once a sea water run is going, the beaker never has to be changed, but a run separating two liquids has to be watched closely. Explain why the two are different.",
        "options": [
            {
             "text": "Because two liquids boil far more violently than a solution does",
             "correct": False,
             "why": "How violently something boils is set by the flame. It is not what makes one run need watching",
            },
            {
             "text": "Because the two-liquid run makes more distillate, so its beaker fills up and must be emptied",
             "correct": False,
             "why": "Neither beaker fills up in a lesson. The reason one is swapped has nothing to do with how much arrives",
            },
            {
             "text": "Because a sea water still needs no thermometer at all, so there is no reading to watch and nothing that could change",
             "correct": False,
             "why": "Both stills have a thermometer. In one of them the reading changes in a way that matters",
            },
            {
             "text": "Because only one thing can come over from sea water, while two come over in turn from the liquids",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-s32",
        "band": "standard",
        "text": "A condenser is fed from a tap left running the whole time, "
                "rather than filling the jacket once and closing the tap. Why "
                "must the water keep moving?",
        "options": [
            {"text": "Standing water would warm up and stop taking heat out "
                     "of the vapour", "correct": True},
            {"text": "Standing water would be pulled into the inner tube and "
                     "spoil the distillate", "correct": False,
             "why": "The jacket is sealed from the inner tube. Nothing "
                    "crosses between them however long it stands"},
            {"text": "Moving water pushes the vapour along the tube towards "
                     "the beaker", "correct": False,
             "why": "The vapour is pushed along by the boiling behind it. The "
                    "jacket water pushes nothing"},
            {"text": "A full jacket would burst the glass once the vapour "
                     "reached it", "correct": False,
             "why": "The jacket is meant to be full, and its outlet is open. "
                    "No pressure builds up in it"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-05-h08",
        "band": "harder",
        "text": "Liquid air holds nitrogen (boiling point −196 °C), argon "
                "(−186 °C) and oxygen (−183 °C). As it is warmed slowly in a "
                "column, in what order are the three drawn off?",
        "options": [
            {"text": "Nitrogen, then argon, then oxygen", "correct": True},
            {"text": "Oxygen, then argon, then nitrogen", "correct": False,
             "why": "That is the order of boiling points reversed. The lowest "
                    "boiling point leaves first, and that is nitrogen's"},
            {"text": "Oxygen, then nitrogen, then argon", "correct": False,
             "why": "Argon boils between the other two, so it can be neither "
                    "the first nor the last of the three"},
            {"text": "All three together, because air is one mixture",
             "correct": False,
             "why": "Each keeps its own boiling point inside the mixture, "
                    "which is the only reason the column can sort them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h09",
        "band": "harder",
        "text": "A mixture of propanone (56 °C), ethanol (78 °C) and water "
                "(100 °C) is distilled into three receivers changed in turn. "
                "Which receiver holds which, and what does the thermometer do "
                "in between?",
        "options": [
            {"text": "Water, then ethanol, then propanone, with the reading "
                     "falling between each steady stretch", "correct": False,
             "why": "Both halves are back to front. The lowest boiling point "
                    "leaves first, and the reading climbs as the run goes on"},
            {"text": "Propanone, then ethanol, then water, with the reading "
                     "climbing between each steady stretch", "correct": True},
            {"text": "Propanone, then ethanol, then water, with the reading "
                     "dropping back between each steady stretch",
             "correct": False,
             "why": "The order is right and the reading is wrong. Each new "
                    "substance needs a higher temperature than the last"},
            {"text": "All three arrive mixed in the first receiver, and the "
                     "other two collect nothing", "correct": False,
             "why": "Three boiling points forty or more degrees apart come "
                    "over in turn, not all at once"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h10",
        "band": "harder",
        "text": "A life raft's emergency kit holds a solar still, while a small island community runs a fuel-fired one. Explain why each is the right choice where it is.",
        "options": [
            {
             "text": "The raft's water is purer, and a community can accept less pure water than one person can",
             "correct": False,
             "why": "Both give water with nothing dissolved in it. Purity is not what separates the two cases",
            },
            {
             "text": "A solar still works only on small volumes, and a fired still works only on large ones",
             "correct": False,
             "why": "Either could be built at either size. What decides it is the fuel available and the water needed",
            },
            {
             "text": "A raft has no fuel and needs little water; a community needs far more than the sun could supply",
             "correct": True,
            },
            {
             "text": "Sunlight is too weak at sea to boil anything, so the raft's still must work another way",
             "correct": False,
             "why": "A solar still does not need to boil anything. It evaporates slowly and condenses on a cool cover, and that is enough",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h11",
        "band": "harder",
        "text": "Distillation takes everything dissolved out of water, but a "
                "chemist warns that it cannot be trusted to remove a "
                "contaminant that boils at 65 °C. Explain the warning.",
        "options": [
            {"text": "A substance boiling at 65 °C would be destroyed by the "
                     "heating and its pieces would come over", "correct": False,
             "why": "Nothing is broken down at these temperatures. The "
                    "trouble is that it travels over whole"},
            {"text": "A substance boiling that low would stay in the flask, "
                     "so the run would have to be repeated", "correct": False,
             "why": "A low boiling point is exactly what makes something "
                    "leave first, not what keeps it behind"},
            {"text": "A substance boiling that low would block the condenser "
                     "before the water reached it", "correct": False,
             "why": "It passes through the condenser as easily as water does. "
                    "Nothing is blocked"},
            {"text": "It boils below water, so it comes over first and ends "
                     "up in the distillate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h12",
        "band": "harder",
        "text": "A mixture of 95% ethanol and 5% water is distilled. The "
                "thermometer holds steady throughout, and the distillate "
                "turns out to be 95% ethanol as well. What does that show?",
        "options": [
            {"text": "That some mixtures cannot be separated any further by "
                     "distilling them", "correct": True},
            {"text": "That the still is faulty and the run should be done "
                     "again", "correct": False,
             "why": "A faulty still gives less distillate or a salty one. "
                    "Coming over at the same composition every time is a real "
                    "result"},
            {"text": "That the mixture must be a pure substance after all",
             "correct": False,
             "why": "There are plainly two substances in it. Behaving like a "
                    "pure one when boiled does not make it one"},
            {"text": "That the ethanol and the water have the same boiling "
                     "point as each other", "correct": False,
             "why": "They boil 22 degrees apart, which is why every earlier "
                    "pass separated them so well"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h13",
        "band": "harder",
        "text": "A refinery column is at 350 °C at the bottom, about 200 °C a "
                "third of the way up, about 100 °C two thirds up and about "
                "25 °C at the top. Kerosene condenses between 150 °C and "
                "250 °C. Where is it drawn off?",
        "options": [
            {"text": "At the very bottom, with whatever never boiled at all",
             "correct": False,
             "why": "The bottom is at 350 °C, far too hot for kerosene to "
                    "condense. It is still a gas there"},
            {"text": "About a third of the way up, where the column is near "
                     "200 °C", "correct": True},
            {"text": "Two thirds of the way up, where the column is near "
                     "100 °C", "correct": False,
             "why": "By 100 °C the kerosene has already condensed lower down "
                    "and been drawn off"},
            {"text": "At the very top, where the lightest fractions leave",
             "correct": False,
             "why": "Only substances boiling below about 25 °C get that high. "
                    "Kerosene condenses long before"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h14",
        "band": "harder",
        "text": "Crude oil is heated to about 350 °C before it enters a "
                "refinery column, and part of it never becomes a gas at all. "
                "What happens to that part?",
        "options": [
            {"text": "It is broken down by the heat into the gases that rise "
                     "up the column", "correct": False,
             "why": "The column separates and changes nothing. Breaking "
                    "molecules up is a different process altogether"},
            {"text": "It stays in the heater and never enters the column at "
                     "all", "correct": False,
             "why": "The whole heated mixture is fed in. What does not boil "
                    "goes in as a liquid"},
            {"text": "It runs down and is drained off as a liquid at the "
                     "base", "correct": True},
            {"text": "It is carried up as a fine powder and collected at the "
                     "top", "correct": False,
             "why": "It is a thick liquid, not a powder, and nothing that "
                    "heavy travels upwards in a column"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h15",
        "band": "harder",
        "text": "A coastal town wants drinking water from the sea; a salt "
                "producer on the same coast wants sea salt. Which method "
                "suits each, and what decides it?",
        "options": [
            {"text": "Both should distil, because distillation is the more "
                     "thorough of the two methods", "correct": False,
             "why": "Distilling to get the salt means paying to collect water "
                    "the producer does not want"},
            {"text": "Both should evaporate, because evaporating costs less "
                     "than distilling does", "correct": False,
             "why": "Evaporating loses the water into the air, which is the "
                    "one thing the town cannot afford to lose"},
            {"text": "The town should evaporate and the producer should "
                     "distil, because of the volumes involved", "correct": False,
             "why": "That has the two the wrong way round. Which part you "
                    "keep decides it, not how much there is"},
            {"text": "The town distils and the producer evaporates: what you "
                     "want to keep decides it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h16",
        "band": "harder",
        "text": "Heating 1 kg of water from 20 °C to 100 °C takes about "
                "336 kJ. Turning that boiling water into steam takes a "
                "further 2260 kJ. What do the two figures together explain?",
        "options": [
            {"text": "That most of the energy goes into the boiling itself, "
                     "so distilling water is costly", "correct": True},
            {"text": "That heating the water up is the costly step, and the "
                     "boiling adds very little", "correct": False,
             "why": "The boiling figure is nearly seven times the heating "
                    "one. It is by far the larger of the two"},
            {"text": "That the two steps cost about the same, so neither is "
                     "worth avoiding", "correct": False,
             "why": "336 kJ and 2260 kJ are nothing like the same. One "
                    "dominates the bill entirely"},
            {"text": "That the condenser hands the energy straight back to "
                     "the flask, so the boiling is free", "correct": False,
             "why": "Nothing goes back to the flask. The heat released passes "
                    "into the cooling water and down the drain"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h17",
        "band": "harder",
        "text": "With no proper condenser available, a student runs the "
                "delivery tube from the flask through a coil of copper pipe "
                "standing in a bucket of cold water. Evaluate the substitute.",
        "options": [
            {"text": "It would not work, because a vapour can only condense "
                     "on glass", "correct": False,
             "why": "What the surface is made of does not matter. What "
                    "matters is that it is colder than the vapour"},
            {"text": "It would work, since it takes heat out too, though the "
                     "bucket warms and needs changing", "correct": True},
            {"text": "It would not work, because the vapour has to touch the "
                     "cold water itself to condense", "correct": False,
             "why": "In a proper condenser the two never touch either. The "
                    "heat travels through the wall between them"},
            {"text": "It would work only for liquids that boil below 50 °C, "
                     "and not for water", "correct": False,
             "why": "A bucket of cold water is well below water's boiling "
                    "point, so it cools water vapour perfectly well"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h18",
        "band": "harder",
        "text": "A still on sea water collects 40 cm³ in the first ten "
                "minutes but only 15 cm³ in the fourth ten minutes, with the "
                "flame never touched. Explain the fall.",
        "options": [
            {"text": "The salt has begun to block the side arm and slow the "
                     "vapour down", "correct": False,
             "why": "The salt never enters the side arm. It cannot become a "
                    "gas, so it stays in the flask"},
            {"text": "The thermometer has drifted, so the readings later in "
                     "the run mean less", "correct": False,
             "why": "What has fallen is the volume collected, which is "
                    "measured in the beaker and not on the thermometer"},
            {"text": "What is left is much saltier, so it boils higher and "
                     "the same flame drives less over", "correct": True},
            {"text": "The water left in the flask has been used up by the "
                     "salt dissolving into it as the run goes on",
             "correct": False,
             "why": "Dissolving uses no water up. The water that has gone is "
                    "in the beaker, collected"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h19",
        "band": "harder",
        "text": "Two identical stills run on the same sea water. One has jacket water at 5 °C, the other at 60 °C. Predict how the two distillates differ.",
        "options": [
            {
             "text": "The colder one gives a purer distillate, since less salt gets past it",
             "correct": False,
             "why": "No salt gets past either. There is none in the vapour for a colder jacket to stop",
            },
            {
             "text": "The warmer one collects more, because its vapour travels through faster",
             "correct": False,
             "why": "Faster vapour that is not cooled enough leaves through the open end rather than arriving in the beaker",
            },
            {
             "text": "There is no difference at all, since both jackets are below 100 °C",
             "correct": False,
             "why": "Both do condense, but not equally well. How much colder the jacket is changes how much is caught",
            },
            {
             "text": "The colder one collects more, and both distillates are equally free of salt",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h20",
        "band": "harder",
        "text": "A student proposes separating sand from water by "
                "distillation rather than by filtering. Would it work, and is "
                "it a sensible choice?",
        "options": [
            {"text": "It works — the water boils over and the sand stays — "
                     "but filtering is far quicker and cheaper",
             "correct": True},
            {"text": "It does not work, because sand would be carried over "
                     "with the steam", "correct": False,
             "why": "Sand is not even dissolved, let alone able to become a "
                    "gas. It stays in the flask"},
            {"text": "It does not work, because a still can only separate "
                     "substances that have dissolved into one another",
             "correct": False,
             "why": "A still separates whatever cannot boil from whatever "
                    "can. Being undissolved makes that easier, not harder"},
            {"text": "It works, and it is the better choice because the water "
                     "ends up cleaner", "correct": False,
             "why": "The water does end up clean either way, and paying for "
                    "fuel to do a job a paper cone does is not better"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h21",
        "band": "harder",
        "text": "A liquid mixture is distilled and the thermometer climbs "
                "steadily from 60 °C to 95 °C without ever holding at one "
                "reading. What does that suggest about the mixture?",
        "options": [
            {"text": "That it is a single pure substance being heated too "
                     "quickly", "correct": False,
             "why": "A pure substance holds at one reading while it boils, "
                    "however fast the flame is"},
            {"text": "That it holds many substances, with boiling points "
                     "spread across that range", "correct": True},
            {"text": "That the flame is being turned up steadily through the "
                     "run", "correct": False,
             "why": "A bigger flame boils a liquid faster, not hotter. The "
                    "reading is set by what is coming over"},
            {"text": "That the bulb was pushed down into the liquid, which "
                     "always gives a climbing reading", "correct": False,
             "why": "A misplaced bulb gives a wrong reading, not a steadily "
                    "rising one. It would still hold while one substance "
                    "boiled"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h22",
        "band": "harder",
        "text": "Two drops are taken from a still separating ethanol from "
                "water — one at the very start of collection, one twenty "
                "minutes later, both before the reading reaches 100 °C. Which "
                "holds more ethanol?",
        "options": [
            {"text": "The later drop, because the still gets better at "
                     "separating as it warms up", "correct": False,
             "why": "A still does not improve as it runs. What changes is "
                    "what is left in the flask to boil"},
            {"text": "Neither — every drop before 100 °C is identical in "
                     "composition", "correct": False,
             "why": "The flask's mixture changes throughout, so what comes "
                    "off it changes too"},
            {"text": "The first drop, because the flask has been losing "
                     "ethanol ever since", "correct": True},
            {"text": "The later drop, because the ethanol takes time to reach "
                     "the beaker", "correct": False,
             "why": "The ethanol arrives from the first drop onwards. Nothing "
                    "is queueing up in the condenser"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h23",
        "band": "harder",
        "text": "A student argues that because dissolved salt raises the "
                "boiling point, a very concentrated brine must give a "
                "slightly salty distillate. Evaluate that argument.",
        "options": [
            {"text": "Right — the higher the temperature, the more salt the "
                     "vapour can carry", "correct": False,
             "why": "No temperature a flask reaches makes salt into a gas. "
                    "Hotter vapour is still only water"},
            {"text": "Right, but only for brine near the point where salt "
                     "starts to crystallise", "correct": False,
             "why": "Even a saturated brine gives a distillate with no salt "
                    "in it. Concentration changes nothing about that"},
            {"text": "Wrong — concentrated brine does not boil any higher "
                     "than pure water does", "correct": False,
             "why": "It does boil higher, and higher still as it "
                    "concentrates. That half of the argument is sound"},
            {"text": "Wrong — the raised boiling point changes how hard it is "
                     "to boil, not what leaves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h24",
        "band": "harder",
        "text": "2000 g of sea water holds 70 g of salt and 1930 g of water. "
                "The still is stopped once 965 g of distillate has been "
                "collected. What is in the flask now?",
        "options": [
            {"text": "70 g of salt in 965 g of water — twice as concentrated "
                     "as at the start", "correct": True},
            {"text": "70 g of salt in 1930 g of water — as concentrated as at "
                     "the start", "correct": False,
             "why": "Half the water has been collected, so it cannot still be "
                    "in the flask. The salt is left in less water than before"},
            {"text": "35 g of salt in 965 g of water — half of each",
             "correct": False,
             "why": "None of the salt left the flask, so all 70 g of it is "
                    "still there. Only the water halved"},
            {"text": "No salt at all in 965 g of water — it came over with "
                     "the distillate", "correct": False,
             "why": "Salt cannot travel as a gas, so none of it reached the "
                    "beaker. The distillate is pure water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h25",
        "band": "harder",
        "text": "A fractionating column is fitted with trays, or packed with "
                "glass beads, rather than being left as an empty tube. Why?",
        "options": [
            {"text": "They slow the vapour down so that the heavier parts of "
                     "it drop out on the way", "correct": False,
             "why": "Nothing falls out of a vapour. The sorting is done by "
                    "condensing and re-boiling, not by weight"},
            {"text": "They give surfaces for the vapour to condense on and "
                     "boil off again, over and over", "correct": True},
            {"text": "They act as a filter, holding back the substances that "
                     "should not reach the top", "correct": False,
             "why": "A vapour passes any filter freely. Nothing in a column "
                    "is separated by size"},
            {"text": "They hold the heat in so that the whole column stays at "
                     "one temperature", "correct": False,
             "why": "A column at one temperature would separate nothing. The "
                    "change in temperature up its height is the point"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h26",
        "band": "harder",
        "text": "A pupil says a fractionating column is really just a very "
                "long condenser. Explain what is wrong with that.",
        "options": [
            {"text": "Nothing is wrong — both cool a vapour, and the column "
                     "is simply the longer of the two", "correct": False,
             "why": "A column does something a condenser never does: it lets "
                    "what has condensed boil off again"},
            {"text": "A condenser is longer than a column, so the comparison "
                     "is the wrong way round", "correct": False,
             "why": "A refinery column is tens of metres tall. Length is not "
                    "what separates the two"},
            {"text": "A condenser only cools; a column condenses and re-boils "
                     "again and again, which is what enriches the vapour",
             "correct": True},
            {"text": "A condenser is cooled by running water while a "
                     "column is cooled only by the air around it, and that is "
                     "the one real difference", "correct": False,
             "why": "How each one is cooled is a detail. What the column does "
                    "with the liquid afterwards is the difference"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h27",
        "band": "harder",
        "text": "A student must show that their distillate from sea water holds no salt. Which test does that?",
        "options": [
            {
             "text": "Look at it, because salt water is cloudy and fresh water is clear right through",
             "correct": False,
             "why": "Salt water is perfectly clear. Looking tells you nothing about what is dissolved in it",
            },
            {
             "text": "Smell it, because a distillate carrying salt smells of the sea",
             "correct": False,
             "why": "Salt has no smell at all, whether it is dissolved or dry",
            },
            {
             "text": "Check that it boils at exactly the same temperature as the sea water it was made from",
             "correct": False,
             "why": "Sea water boils above 100 °C. Matching it would be evidence of salt rather than evidence against it",
            },
            {
             "text": "Test it with a conductivity meter: salt solution conducts and pure water hardly does",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h28",
        "band": "harder",
        "text": "A student insists that a condenser must be taken down to "
                "0 °C with ice, or the vapour will not condense at all. "
                "Evaluate that claim.",
        "options": [
            {"text": "Wrong — it only has to be cooler than the vapour, and "
                     "tap water is easily cold enough", "correct": True},
            {"text": "Right — anything warmer than 0 °C leaves the vapour as "
                     "a gas", "correct": False,
             "why": "Water vapour condenses on any surface below 100 °C. A "
                    "cold window proves it every winter morning"},
            {"text": "Right for water, though ethanol would condense at a "
                     "higher temperature", "correct": False,
             "why": "Ethanol condenses below 78 °C, which is cooler than "
                    "water needs, not warmer. Neither needs ice"},
            {"text": "Wrong — how cold the condenser is makes no difference "
                     "to anything at all", "correct": False,
             "why": "It makes a great deal of difference to how much is "
                    "caught. What is wrong is the figure of 0 °C, not the "
                    "idea"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h29",
        "band": "harder",
        "text": "Petrol drawn from a refinery column boils over a range from "
                "about 40 °C to 100 °C rather than at one fixed temperature. "
                "What does that tell you about petrol?",
        "options": [
            {"text": "That it is one substance being heated unevenly through "
                     "the sample", "correct": False,
             "why": "A pure substance holds at one temperature however it is "
                    "heated. A range means more than one substance"},
            {"text": "That it is a mixture of many substances rather than a "
                     "pure one", "correct": True},
            {"text": "That it is one substance that boils differently in "
                     "different parts of the column", "correct": False,
             "why": "A substance carries its boiling point with it wherever "
                    "it is. The column does not change it"},
            {"text": "That it has been contaminated by the fraction collected "
                     "just above it", "correct": False,
             "why": "Petrol boils over a range as drawn, cleanly separated. "
                    "The range is what it is, not a fault"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h30",
        "band": "harder",
        "text": "A still's flask is warmed so gently that the liquid never "
                "actually boils, yet after an hour a little clear liquid has "
                "collected in the beaker. Explain how.",
        "options": [
            {"text": "The cooling water has seeped through the glass into the "
                     "inner tube", "correct": False,
             "why": "Glass lets nothing through. The jacket and the inner "
                    "tube stay entirely separate"},
            {"text": "The liquid crept along the inside of the glass as a "
                     "film until it reached the beaker", "correct": False,
             "why": "Liquid does not climb up and along a still. It travelled "
                    "as a gas and condensed"},
            {"text": "Liquid evaporates from its surface below its boiling "
                     "point, only far more slowly", "correct": True},
            {"text": "The liquid collected was condensed out of the air "
                     "inside the apparatus", "correct": False,
             "why": "There is far too little water in that much air to give "
                    "collectable drops"},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h31",
        "band": "harder",
        "text": "A whole still — flask, contents, condenser and beaker — is "
                "weighed before a run and again afterwards, with nothing "
                "allowed to escape. The total is unchanged. Why is that "
                "expected?",
        "options": [
            {"text": "Because water weighs nothing once it has become a gas",
             "correct": False,
             "why": "A gas has mass like anything else. If it did not, the "
                    "total would fall while the vapour was travelling"},
            {"text": "Because the condenser puts back exactly the mass the "
                     "flask has lost", "correct": False,
             "why": "The condenser adds nothing of its own. It only cools "
                    "what the flask sent it"},
            {"text": "Because mass is kept only in chemical reactions, and "
                     "distilling is one", "correct": False,
             "why": "Distilling is not a chemical reaction, and mass is kept "
                    "in physical changes too"},
            {"text": "Because nothing was made or destroyed — the substances "
                     "only moved", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-05-h32",
        "band": "harder",
        "text": "A desalination plant takes in 10 000 m³ of sea water a day, "
                "and every cubic metre of it holds 35 kg of dissolved salt. "
                "What mass of salt must the plant deal with each day?",
        "options": [
            {"text": "350 000 kg", "correct": True},
            {"text": "35 000 kg", "correct": False,
             "why": "That multiplies by 1000 rather than by 10 000. There are "
                    "ten thousand cubic metres, not one thousand"},
            {"text": "3 500 000 kg", "correct": False,
             "why": "That is ten times too large — the decimal point has "
                    "slipped one place"},
            {"text": "350 kg", "correct": False,
             "why": "That divides where it should multiply. More sea water "
                    "means more salt to deal with, not less"},
        ],
        "figure": None,
    },
]
