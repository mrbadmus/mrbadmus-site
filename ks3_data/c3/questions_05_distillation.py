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
]
