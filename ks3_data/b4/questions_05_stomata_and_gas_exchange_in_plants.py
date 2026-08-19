"""B4 lesson 05 — Stomata and gas exchange in plants: twelve questions (MRB-269).

The lesson has two halves and the bank probes both. One half is the pore: a
stoma is a gap held open between two guard cells that swell with water, most of
them on the shaded underside, and every open pore leaks water vapour — so
shutting it is a decision that buys water and spends growth. The other half is
the ledger: respiration is flat at every light level, photosynthesis rises with
light and levels off, and the only thing a sensor outside the leaf can see is
the difference. The easier band checks the pore's structure, its mechanism, the
cost of a moist surface and what the word `net` actually names. The standard
band puts the student back in the situations the page showed them — the hot dry
afternoon, the light dragged to zero, the four bars moving, the leaf beside an
alveolus and a villus. The harder band takes the ideas somewhere the page did
not go: a desert plant that shuts its pores by day, two sealed jars a sensor
cannot tell apart, a thicker leaf, and a houseplant living just below the
compensation point.

All three declared misconceptions supply distractors. BREATH-12 ("plants take
in carbon dioxide and give out oxygen; animals do the opposite") drives the
reversed-direction option in s02 and the "photosynthesis has stopped" option in
h04. BREATH-13 ("plants respire at night and photosynthesise in the day")
drives the "respiration has switched on for the night" option in s02, the
climbing respiration bar in s03, the "stopped respiring" option in h02 and the
speeded-up respiration in h04 — and it is deliberately attacked from both ends,
because the flat top bar is the thing the whole lesson rests on. BREATH-15
("plants breathe through their stomata") drives the pressure-difference options
in s04 and h03 and the muscle options in e01 and e02. Two further errors the
lesson exists to correct supply the rest: that the pore can somehow let carbon
dioxide in without letting water out (e03, h01), and that closing the stomata
is a plant failing rather than a plant choosing (s01).

`figure` is None throughout. This lesson's only figure,
`b4-guard-cells-two-state`, is declared with `status: "needed"` and has not been
drawn, so no question is allowed to depend on a student seeing it.
"""

UNIT = "B4"
LESSON = "stomata-and-gas-exchange-in-plants"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-05-e01",
        "band": "easier",
        "text": "Where on a leaf are most stomata found, and what holds one "
                "open?",
        "options": [
            {"text": "Mostly on the upper surface, held open by the leaf's "
                     "stiff outer wall.",
             "correct": False,
             "why": "Two errors in one. Most stomata are on the shaded, "
                    "sheltered underside, and the pore is a gap between two "
                    "curved cells — not a fixed hole in a wall, or it could "
                    "never be shut."},
            {"text": "Mostly on the underside, held open between a pair of "
                     "guard cells.",
             "correct": True},
            {"text": "Mostly on the underside, held open by tiny muscles in "
                     "the leaf surface.",
             "correct": False,
             "why": "You have the position right, but nothing in a plant has "
                    "muscle. Guard cells open the pore by taking water in and "
                    "swelling — the plant controls its gas exchange by moving "
                    "water."},
            {"text": "Spread evenly over both surfaces, held open by the "
                     "pressure of the air.",
             "correct": False,
             "why": "Most are on the underside, and air pressure holds nothing "
                    "open. The guard cells do that, by becoming turgid; the "
                    "air outside a leaf is not pushing gases anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e02",
        "band": "easier",
        "text": "A stoma is opening. What is happening to the two guard cells "
                "on either side of it?",
        "options": [
            {"text": "Water moves in, they become turgid and bow apart.",
             "correct": True},
            {"text": "Water moves out, they go limp and are pulled apart.",
             "correct": False,
             "why": "You have the water going the wrong way. Losing water is "
                    "what closes a stoma: limp guard cells straighten up and "
                    "the pore shuts."},
            {"text": "They contract like a muscle and haul the pore open.",
             "correct": False,
             "why": "There is no muscle anywhere in a plant. The shape change "
                    "is done entirely by water moving into and out of the two "
                    "cells."},
            {"text": "They grow larger, so the pore stays open for good.",
             "correct": False,
             "why": "The change is reversible and happens over and over "
                    "through a day. Water in opens the pore; water out closes "
                    "it again."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e03",
        "band": "easier",
        "text": "The inside of a leaf is wet. What does keeping it wet cost "
                "the plant?",
        "options": [
            {"text": "Nothing — the wet surface is what stops water escaping.",
             "correct": False,
             "why": "Backwards. Diffusion needs a moist surface, and a pore "
                    "open enough to let carbon dioxide in is open enough to "
                    "let water vapour out."},
            {"text": "It slows diffusion down, so gases move through more "
                     "slowly.",
             "correct": False,
             "why": "A moist surface is a requirement for diffusion, not an "
                    "obstacle to it. The price it carries is water, not "
                    "speed."},
            {"text": "Water vapour diffuses out through every stoma that is "
                     "open.",
             "correct": True},
            {"text": "Energy, which the plant spends pumping water to the "
                     "surface.",
             "correct": False,
             "why": "The lesson names water lost, not energy spent. Water "
                    "vapour leaves by diffusion, with nothing pushing it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e04",
        "band": "easier",
        "text": "On the bench the third bar is labelled “What a sensor "
                "outside the leaf measures”. What is that bar showing?",
        "options": [
            {"text": "The two rates above it, added together.",
             "correct": False,
             "why": "The two processes move carbon dioxide in opposite "
                    "directions, so they subtract rather than add. Net "
                    "movement is what is left when opposite flows cancel."},
            {"text": "Whichever of the two processes is currently running.",
             "correct": False,
             "why": "Both are always running. The net figure is what is left "
                    "over from two flows happening at once, not a label for "
                    "the one that won."},
            {"text": "The rate of photosynthesis, on its own.",
             "correct": False,
             "why": "That is the second bar. The third takes respiration off "
                    "it, which is why it can point the other way when the "
                    "light is off."},
            {"text": "The difference between the two rates above it.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-05-s01",
        "band": "standard",
        "text": "A crop in full sunshine grows more slowly on a hot, dry "
                "afternoon than on a mild one. What is going on?",
        "options": [
            {"text": "The light is too strong, so photosynthesis has been "
                     "damaged and shut down.",
             "correct": False,
             "why": "Photosynthesis levels off in bright light on this bench; "
                    "it does not fall. What slows the crop is happening at the "
                    "pore, not in the reaction."},
            {"text": "Respiration speeds up in the heat until it cancels "
                     "photosynthesis out.",
             "correct": False,
             "why": "The top bar does not move. Respiration runs at the same "
                    "rate whatever else changes here — that is the contrast "
                    "the whole lesson rests on."},
            {"text": "The plants have shut their stomata to save water, "
                     "keeping carbon dioxide out.",
             "correct": True},
            {"text": "The plants have wilted, so their leaves have failed and "
                     "stopped working.",
             "correct": False,
             "why": "Closing the stomata is a decision, not a failure. The "
                    "plant is choosing survival over growth: no water lost, "
                    "and no growth either."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s02",
        "band": "standard",
        "text": "You drag the light on the bench all the way down to zero. "
                "Which way is each gas moving, and why?",
        "options": [
            {"text": "Carbon dioxide out and oxygen in — the same direction as "
                     "your own breathing.",
             "correct": True},
            {"text": "Carbon dioxide in and oxygen out, because a plant does "
                     "the opposite of an animal.",
             "correct": False,
             "why": "This is the most stubborn wrong idea in the subject. In "
                    "the dark only respiration is running, so the plant takes "
                    "in oxygen and gives out carbon dioxide, exactly as you "
                    "do."},
            {"text": "Carbon dioxide out and oxygen in, because respiration "
                     "has switched on for the night.",
             "correct": False,
             "why": "Right direction, wrong reason. Respiration was running at "
                    "that same rate all day — darkness did not switch it on, "
                    "it removed the larger opposite flow hiding it."},
            {"text": "Neither way — with no light there is no gas exchange "
                     "happening at all.",
             "correct": False,
             "why": "Respiration never stops, so the exchange never stops. "
                    "Zero light removes photosynthesis only, and leaves "
                    "respiration running on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s03",
        "band": "standard",
        "text": "A student drags the light from darkness up to bright noon and "
                "writes down four observations. Which one is wrong?",
        "options": [
            {"text": "Photosynthesis rose fast at first, then levelled off.",
             "correct": False,
             "why": "That observation is right, so it is not the error. "
                    "Photosynthesis rises with light and then levels off as "
                    "other factors become limiting."},
            {"text": "Respiration climbed steadily as the light went up.",
             "correct": True},
            {"text": "The net figure went from release to uptake.",
             "correct": False,
             "why": "That observation is right, so it is not the error. In the "
                    "dark the plant releases carbon dioxide; in bright light "
                    "photosynthesis outruns respiration and the flow "
                    "reverses."},
            {"text": "At one setting the net figure read zero.",
             "correct": False,
             "why": "That observation is right, so it is not the error. It is "
                    "the compensation point, and it is the reading the whole "
                    "lesson is built around."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s04",
        "band": "standard",
        "text": "A leaf, an alveolus and a villus look nothing like each "
                "other. What do all three actually share?",
        "options": [
            {"text": "A rich blood supply, to carry the substance away "
                     "quickly.",
             "correct": False,
             "why": "An alveolus and a villus have one; a leaf has no blood at "
                    "all. What all three share is a concentration difference "
                    "kept up by cells using whichever substance they need."},
            {"text": "A pressure difference that pushes the substance across "
                     "the surface.",
             "correct": False,
             "why": "Only breathing generates a pressure difference, and even "
                    "there the movement across the surface itself is "
                    "diffusion. Nothing in a plant pushes gases anywhere."},
            {"text": "A thick, tough outer layer, protecting the delicate "
                     "cells that lie underneath.",
             "correct": False,
             "why": "The opposite is needed. The diffusion distance has to be "
                    "very short, which is why a leaf is thin and an alveolus "
                    "wall is a single cell thick."},
            {"text": "A large moist surface, a short distance and a "
                     "concentration difference.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-05-h01",
        "band": "harder",
        "text": "A desert plant keeps its stomata shut right through the day "
                "and opens them only at night. What does that cost it?",
        "options": [
            {"text": "Nothing — the pore is only there for water, so shutting "
                     "it costs no carbon dioxide.",
             "correct": False,
             "why": "One pore carries both. Shutting it stops water leaving "
                    "and stops carbon dioxide entering in the same movement — "
                    "the two cannot be separated."},
            {"text": "Its respiration, which cannot run while the pores are "
                     "shut.",
             "correct": False,
             "why": "Respiration runs continuously, and on this bench its bar "
                    "is flat at every setting. What closed pores cost is the "
                    "carbon dioxide, not the respiration."},
            {"text": "Carbon dioxide, which cannot get in during the brightest "
                     "hours of the day.",
             "correct": True},
            {"text": "Nothing — it gains, because the night air is richer in "
                     "carbon dioxide.",
             "correct": False,
             "why": "Nothing in the lesson says night air is richer. Shutting "
                    "the pores by day is a sacrifice made to save water, and "
                    "it gives up the brightest hours to make it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h02",
        "band": "harder",
        "text": "Two sealed jars each hold a carbon dioxide sensor. Jar A "
                "holds a healthy plant in dim light and jar B holds a dead "
                "one. Both readings hold perfectly steady. What do the "
                "readings on their own prove?",
        "options": [
            {"text": "Nothing that separates the two — a net of zero looks "
                     "like nothing happening.",
             "correct": True},
            {"text": "That the plant in jar A has stopped respiring, just like "
                     "the dead one.",
             "correct": False,
             "why": "Respiration never stops. In jar A both processes are "
                    "running at full rate and subtracting to zero, which is "
                    "not the same as neither running."},
            {"text": "That both plants are dead, since a living plant always "
                     "moves the reading.",
             "correct": False,
             "why": "A living plant can hold a reading flat, and that is the "
                    "whole lesson. At one light level the two rates cancel "
                    "exactly, so a flat line proves nothing about life."},
            {"text": "That jar B holds more carbon dioxide inside it than jar "
                     "A does.",
             "correct": False,
             "why": "A steady reading says the amount is not changing. It says "
                    "nothing about how much is in there — the sensor reports "
                    "change, not total."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h03",
        "band": "harder",
        "text": "A gardener says a much thicker leaf would hold more cells and "
                "so photosynthesise more. Using this lesson, what is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong — a thicker leaf really would "
                     "photosynthesise more per leaf.",
             "correct": False,
             "why": "It would also put its innermost cells out of reach. There "
                    "is no ventilation inside a leaf, so a gas has only "
                    "diffusion to cross the distance with."},
            {"text": "A thick leaf could not open its stomata, as the guard "
                     "cells would be buried.",
             "correct": False,
             "why": "The stomata sit in the surface whatever the leaf's "
                    "thickness. The problem is the distance from that surface "
                    "inwards, which diffusion alone has to cover."},
            {"text": "Gases move inside a leaf only by diffusion, so inner "
                     "cells are out of reach.",
             "correct": True},
            {"text": "A thick leaf would have to pull air inside it, the way "
                     "your lungs do.",
             "correct": False,
             "why": "No plant generates a pressure difference — no diaphragm, "
                    "no rib cage, no ventilation anywhere. That is exactly why "
                    "thickness is a hard limit rather than a problem to "
                    "engineer around."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h04",
        "band": "harder",
        "text": "A healthy, well-watered houseplant sits in a room slightly "
                "dimmer than the light level at which its two bars are equal. "
                "Over several weeks it slowly shrinks. Why?",
        "options": [
            {"text": "Its stomata have closed in the low light, so no gas can "
                     "get in.",
             "correct": False,
             "why": "Water, not light, is what shuts a stoma in this lesson. "
                    "Gases are still moving here — the net figure is small, "
                    "and pointing the wrong way."},
            {"text": "Respiration slightly outruns photosynthesis, so the net "
                     "movement of carbon dioxide is outwards.",
             "correct": True},
            {"text": "Photosynthesis has stopped altogether, because dim light "
                     "is not enough to start it.",
             "correct": False,
             "why": "There is no threshold to cross. Photosynthesis rises "
                    "smoothly from zero with the light, so in dim light it is "
                    "running — just more slowly than respiration."},
            {"text": "Respiration has speeded up to make up for the light that "
                     "is missing.",
             "correct": False,
             "why": "Respiration does not respond to light at all; its bar is "
                    "flat at every setting. The balance shifts because "
                    "photosynthesis changed, never because respiration did."},
        ],
        "figure": None,
    },
]
