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
            {"text": "Respiration slightly outruns photosynthesis, so net "
                     "carbon dioxide movement is out.",
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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-05-e05",
        "band": "easier",
        "text": "A guard cell is described as turgid. What does turgid mean?",
        "options": [
            {"text": "Swollen and firm, because the cell is full of water.",
             "correct": True},
            {"text": "Limp and soft, because water has left the cell.",
             "correct": False,
             "why": "That is the opposite state, and it is the one in which "
                    "the pore closes. Turgid guard cells bow apart and open "
                    "it."},
            {"text": "Stiffened by a thick wall on the outside edge.",
             "correct": False,
             "why": "It is the inner edge of a guard cell that has the thicker "
                    "wall, and thickness is not what turgid describes. Turgid "
                    "is about water."},
            {"text": "Growing larger permanently, so the pore stays open.",
             "correct": False,
             "why": "Nothing grows and nothing is permanent. The cells swell "
                    "and shrink with water, over and over through a day."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e06",
        "band": "easier",
        "text": "By what process do gases get into and out of a leaf?",
        "options": [
            {"text": "By breathing, using the stomata as tiny mouths.",
             "correct": False,
             "why": "A plant has no diaphragm, no ribs and no muscle, so it "
                    "cannot ventilate anything. Stomata are holes, and holes "
                    "do not breathe."},
            {"text": "By being pumped in and out by the guard cells.",
             "correct": False,
             "why": "Guard cells open and close the pore; they move no gas "
                    "through it. Nothing in a plant pumps a gas anywhere."},
            {"text": "By diffusion, driven only by concentration differences.",
             "correct": True},
            {"text": "By a pressure difference the leaf creates inside "
                     "itself.",
             "correct": False,
             "why": "No plant generates a pressure difference — that is the "
                    "whole distinction between a plant and your chest. Gases "
                    "arrive and leave with nothing pushing them."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e07",
        "band": "easier",
        "text": "At one particular light level a plant's carbon dioxide "
                "reading holds perfectly steady. What is that light level "
                "called?",
        "options": [
            {"text": "The saturation point.", "correct": False,
             "why": "Saturation is about how much water vapour air can hold, "
                    "which is a different idea altogether. The steady reading "
                    "has its own name."},
            {"text": "The compensation point.", "correct": True},
            {"text": "The dormant point.", "correct": False,
             "why": "Nothing is dormant. Both processes are running at full "
                    "rate at that light level, which is why the reading holds "
                    "still."},
            {"text": "The limiting point.", "correct": False,
             "why": "Limiting factors are what make photosynthesis level off "
                    "in bright light. The steady reading happens at a low "
                    "light level, where the two rates are equal."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e08",
        "band": "easier",
        "text": "Which gas does photosynthesis use, and which does it make?",
        "options": [
            {"text": "It uses oxygen and makes carbon dioxide.",
             "correct": False,
             "why": "That is respiration, which runs in a plant continuously. "
                    "Photosynthesis works the other way round."},
            {"text": "It uses nitrogen and makes oxygen.",
             "correct": False,
             "why": "Nitrogen takes no part in either process. Photosynthesis "
                    "takes in carbon dioxide."},
            {"text": "It uses carbon dioxide and makes carbon dioxide.",
             "correct": False,
             "why": "A process cannot use and make the same gas here. "
                    "Photosynthesis consumes carbon dioxide, and the gas it "
                    "gives out is oxygen."},
            {"text": "It uses carbon dioxide and makes oxygen.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e09",
        "band": "easier",
        "text": "Most stomata are on the shaded underside of a leaf rather "
                "than the sunlit top. What is the advantage of that?",
        "options": [
            {"text": "The underside is cooler and more sheltered, so less "
                     "water is lost through an open pore.",
             "correct": True},
            {"text": "The underside is where the light falls, so "
                     "photosynthesis is faster there.",
             "correct": False,
             "why": "The light falls on the top of a leaf, not the bottom. And "
                    "stomata let gases through — they do not collect light."},
            {"text": "The underside is thicker, so the pores can be held open "
                     "more firmly.",
             "correct": False,
             "why": "Nothing holds a pore open but the shape of the two guard "
                    "cells beside it. The position is about water, not about "
                    "grip."},
            {"text": "Carbon dioxide sinks, so there is more of it "
                     "underneath a leaf.",
             "correct": False,
             "why": "The air around a leaf is thoroughly mixed and carbon "
                    "dioxide does not pool underneath it. The advantage of the "
                    "shaded side is that it loses less water."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-e10",
        "band": "easier",
        "text": "A plant is in bright sunlight. Which way is carbon dioxide "
                "moving overall?",
        "options": [
            {"text": "Out of the leaf, because respiration is running "
                     "faster than usual in the warmth.",
             "correct": False,
             "why": "Respiration runs at the same rate whatever the light, and "
                    "in bright light it is outrun by photosynthesis. The "
                    "overall movement is inwards."},
            {"text": "Neither way, because the two processes always cancel "
                     "each other out.",
             "correct": False,
             "why": "They cancel at one particular light level only. In bright "
                    "light photosynthesis is several times faster, so they do "
                    "not."},
            {"text": "Into the leaf, because photosynthesis is using it "
                     "faster than respiration makes it.",
             "correct": True},
            {"text": "Into the leaf, because respiration has switched off for "
                     "the daytime.",
             "correct": False,
             "why": "The direction is right and the reason is not. Respiration "
                    "never switches off — it is simply hidden underneath a "
                    "larger opposite flow."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-05-s05",
        "band": "standard",
        "text": "A leaf still attached to a healthy plant has its underside "
                "coated all over with petroleum jelly. Predict what happens "
                "to that leaf.",
        "options": [
            {"text": "It photosynthesises faster, because no water can be "
                     "lost from it.",
             "correct": False,
             "why": "Blocking the pores does stop water leaving, but the same "
                    "pores were the only way in for carbon dioxide. You cannot "
                    "close one without closing the other."},
            {"text": "Photosynthesis nearly stops, because carbon dioxide can "
                     "no longer get in.",
             "correct": True},
            {"text": "Nothing changes, because gases can pass through the "
                     "upper surface instead.",
             "correct": False,
             "why": "The upper surface has very few stomata, and in many "
                    "plants effectively none. Almost all the traffic goes "
                    "through the underside."},
            {"text": "Respiration stops, because oxygen can no longer reach "
                     "the cells.",
             "correct": False,
             "why": "Respiration is the process that does not stop. There is "
                    "oxygen inside the leaf already, and respiration "
                    "carries on using it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s06",
        "band": "standard",
        "text": "Two identical plants are sealed in jars with carbon dioxide "
                "sensors. One jar is in bright light and the other in "
                "complete darkness. Predict the two readings after an hour.",
        "options": [
            {"text": "Both readings fall, because plants always take carbon "
                     "dioxide in.",
             "correct": False,
             "why": "That is true only while photosynthesis is running. In the "
                    "dark the only process left is respiration, and it "
                    "releases carbon dioxide."},
            {"text": "Both readings hold steady, because respiration and "
                     "photosynthesis always cancel.",
             "correct": False,
             "why": "They cancel at one particular light level only. Neither "
                    "bright light nor darkness is that level."},
            {"text": "The bright jar rises and the dark jar falls.",
             "correct": False,
             "why": "This has both the right way round the wrong way. In "
                    "bright light photosynthesis wins and the reading falls; "
                    "in darkness respiration is alone and the reading rises."},
            {"text": "The bright jar falls and the dark jar rises.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s07",
        "band": "standard",
        "text": "A wilted pot plant is watered and by the evening it has "
                "recovered. Explain what has happened at its stomata.",
        "options": [
            {"text": "Water has moved back into the guard cells, which have "
                     "become turgid and bowed apart again.",
             "correct": True},
            {"text": "The guard cells have grown new tissue to replace what "
                     "was lost while it was dry.",
             "correct": False,
             "why": "Nothing was lost and nothing has been rebuilt. Closing a "
                    "stoma is a reversible change of shape, driven entirely by "
                    "water moving in and out."},
            {"text": "The guard cells have relaxed, letting the pore fall "
                     "open under its own weight.",
             "correct": False,
             "why": "There is no muscle to relax and nothing falls open. The "
                    "pore opens because the two cells swell and curve away "
                    "from each other."},
            {"text": "The plant has stopped photosynthesising, so it no "
                     "longer needs the pores shut.",
             "correct": False,
             "why": "It is the other way round. Shutting the pores is what "
                    "stopped photosynthesis, and reopening them is what lets "
                    "it start again."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s08",
        "band": "standard",
        "text": "A grower adds extra carbon dioxide to the air in a "
                "greenhouse on a very hot, dry day. Why might it make far "
                "less difference than expected?",
        "options": [
            {"text": "Because the extra carbon dioxide makes the guard cells "
                     "swell up and shut.",
             "correct": False,
             "why": "It is water, not carbon dioxide, that opens and closes a "
                    "stoma. The reason the pores are shut on a hot dry day is "
                    "the plant saving water."},
            {"text": "Because respiration speeds up in the heat and consumes "
                     "all of the extra gas.",
             "correct": False,
             "why": "Respiration does not consume carbon dioxide — it produces "
                    "it. And its rate is not what changes here."},
            {"text": "Because the plants may have shut their stomata to save "
                     "water, so the gas cannot get in.",
             "correct": True},
            {"text": "Because a leaf can only take in a fixed amount of "
                     "carbon dioxide however much is available.",
             "correct": False,
             "why": "There is no fixed quota. Diffusion follows the "
                    "concentration difference, so more outside would normally "
                    "mean more crossing in — if the pores were open."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s09",
        "band": "standard",
        "text": "Each guard cell has a much thicker wall along its inner "
                "edge, next to the pore, than along its outer edge. What does "
                "that thickening achieve?",
        "options": [
            {"text": "It stops water escaping from the guard cells into the "
                     "pore.",
             "correct": False,
             "why": "Water vapour leaves through the pore whatever the walls "
                    "are like — that is the price of an open stoma. The "
                    "thickening does a mechanical job instead."},
            {"text": "It makes a filling cell curve rather than swell evenly, "
                     "so the pair bows apart.",
             "correct": True},
            {"text": "It makes the guard cells stiff enough to push the pore "
                     "open like a lever.",
             "correct": False,
             "why": "Nothing pushes. The cells change shape because water "
                    "enters them, and the uneven walls decide what shape they "
                    "change into."},
            {"text": "It protects the inside of the leaf from drying out when "
                     "the pore is open.",
             "correct": False,
             "why": "The inside of a leaf has to stay wet for diffusion to "
                    "work, and no wall prevents that water leaving. The "
                    "thickening controls the bending."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-s10",
        "band": "standard",
        "text": "An alveolus is the surface where gas crosses in a lung. What "
                "plays that part in a leaf?",
        "options": [
            {"text": "The stomata themselves, which are the place where gas "
                     "crosses into the plant.",
             "correct": False,
             "why": "A stoma is the way in, in the way that the trachea is the "
                    "way into a lung. Gases cross into the cells further in, "
                    "not at the pore."},
            {"text": "The guard cells, which take the gases in as they swell "
                     "up with water.",
             "correct": False,
             "why": "Guard cells control the pore's size and nothing else. "
                    "They are not where the exchange with the leaf's cells "
                    "happens."},
            {"text": "The waxy upper surface, which is the largest area the "
                     "leaf has.",
             "correct": False,
             "why": "The upper surface is a barrier, not an exchange surface. "
                    "It is unbroken precisely so that water is not lost "
                    "through it."},
            {"text": "The air spaces inside the leaf, where air meets the "
                     "moist surfaces of the cells.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-05-h05",
        "band": "harder",
        "text": "A sealed jar holds a plant at exactly the light level where "
                "its carbon dioxide reading is steady. A cloud passes and the "
                "light dips for a minute. Predict what the sensor does.",
        "options": [
            {"text": "The reading starts to rise, because respiration is now "
                     "outrunning photosynthesis.",
             "correct": True},
            {"text": "The reading starts to fall, because less light means "
                     "less carbon dioxide is produced.",
             "correct": False,
             "why": "Light does not control the production of carbon dioxide — "
                    "respiration does, and it is unchanged. What the cloud "
                    "reduces is the consumption."},
            {"text": "The reading stays steady, because the plant adjusts its "
                     "respiration to match.",
             "correct": False,
             "why": "Respiration does not adjust to anything here; its rate is "
                    "flat at every light level. Nothing keeps the balance once "
                    "the light moves."},
            {"text": "The reading stays steady, because a passing cloud is "
                     "too brief to have any effect.",
             "correct": False,
             "why": "Photosynthesis follows the light immediately, with no "
                    "delay to ride out. As soon as it slows, the balance "
                    "tips."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h06",
        "band": "harder",
        "text": "A water lily's floating leaves have their stomata on the "
                "upper surface, unlike almost every land plant. Explain why.",
        "options": [
            {"text": "The upper surface is warmer, so the guard cells can "
                     "open more easily there.",
             "correct": False,
             "why": "Guard cells open when water enters them, whatever the "
                    "temperature. What matters here is which side of the leaf "
                    "the air is on."},
            {"text": "Water lilies have no need to save water, so the pores "
                     "can be anywhere.",
             "correct": False,
             "why": "It is true that a floating leaf is in no danger of drying "
                    "out, which is why the usual reason for hiding the pores "
                    "underneath has gone. But that only removes an objection — "
                    "it does not explain the move upwards."},
            {"text": "The underside is in the water, so pores there would "
                     "meet no air to exchange gases with.",
             "correct": True},
            {"text": "Gases dissolve better in warm surface water, so the "
                     "pores collect them from above.",
             "correct": False,
             "why": "Stomata exchange gases with air, not with water, and they "
                    "collect nothing. The pores are on top because that is the "
                    "side the air is on."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h07",
        "band": "harder",
        "text": "At a particular light level a leaf photosynthesises at 9 "
                "units and respires at 2 units. What is the net movement of "
                "carbon dioxide?",
        "options": [
            {"text": "11 units into the leaf.", "correct": False,
             "why": "The two rates have been added. They move carbon dioxide "
                    "in opposite directions, so they have to be subtracted."},
            {"text": "7 units into the leaf.", "correct": True},
            {"text": "7 units out of the leaf.", "correct": False,
             "why": "The size is right and the direction is not. "
                    "Photosynthesis is the larger of the two here, and it is "
                    "the one that takes carbon dioxide in."},
            {"text": "2 units out of the leaf.", "correct": False,
             "why": "This reports the respiration rate on its own and ignores "
                    "photosynthesis. The net figure is what is left after the "
                    "two are set against each other."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h08",
        "band": "harder",
        "text": "A student decides to measure oxygen in the sealed jar "
                "instead of carbon dioxide. Would that tell a different "
                "story?",
        "options": [
            {"text": "Yes — oxygen only moves during the day, so nothing "
                     "would be seen at night.",
             "correct": False,
             "why": "Oxygen moves at night too: respiration consumes it, so "
                    "the reading falls. Something is always happening to both "
                    "gases."},
            {"text": "Yes — oxygen readings would stay flat, because plants "
                     "do not exchange oxygen.",
             "correct": False,
             "why": "Plants exchange oxygen constantly. Respiration uses it "
                    "and photosynthesis makes it, so the reading moves as much "
                    "as the carbon dioxide one does."},
            {"text": "No — the same story, with the readings simply going the "
                     "other way at each light level.",
             "correct": True},
            {"text": "No — the two gases move in the same direction, so the "
                     "readings would be identical.",
             "correct": False,
             "why": "The conclusion is right but the reason has the gases "
                    "moving together. They move in opposite directions, which "
                    "is exactly why one reading mirrors the other."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h09",
        "band": "harder",
        "text": "A leaf on a hot dry afternoon has kept most of its stomata "
                "closed for hours in full sunshine. A sensor in a sealed "
                "bag around it shows carbon dioxide slowly rising. Explain "
                "why.",
        "options": [
            {"text": "Respiration carries on inside the leaf, while "
                     "photosynthesis is starved of carbon dioxide.",
             "correct": True},
            {"text": "The closed stomata trap carbon dioxide inside the bag, "
                     "which the sensor then detects.",
             "correct": False,
             "why": "Shut pores would keep gas inside the leaf, not push it "
                    "into the bag. What is raising the bag's reading is gas "
                    "still coming out of the plant."},
            {"text": "Photosynthesis has been damaged by the strong sunlight "
                     "and has stopped producing oxygen.",
             "correct": False,
             "why": "Bright light does not damage photosynthesis here; it "
                    "levels off rather than failing. What has stopped it is "
                    "the shortage of carbon dioxide behind a closed pore."},
            {"text": "Respiration has speeded up in the heat until it "
                     "overtakes photosynthesis.",
             "correct": False,
             "why": "Respiration does not change rate here — it is the one "
                    "constant in the whole lesson. The balance has tipped "
                    "because photosynthesis fell, not because respiration "
                    "rose."},
        ],
        "figure": None,
    },
    {
        "id": "b4-05-h10",
        "band": "harder",
        "text": "Why can a sealed jar and a carbon dioxide sensor never "
                "measure a plant's rate of photosynthesis on its own?",
        "options": [
            {"text": "Because photosynthesis does not involve carbon dioxide "
                     "at every possible light level.",
             "correct": False,
             "why": "Photosynthesis consumes carbon dioxide whenever it runs "
                    "at all. The problem is not what it uses — it is what else "
                    "is going on at the same time."},
            {"text": "Because a carbon dioxide sensor cannot work properly "
                     "inside a sealed container.",
             "correct": False,
             "why": "They work perfectly well sealed in — that is how the "
                    "steady dawn reading was found. The limitation is "
                    "biological, not technical."},
            {"text": "Because respiration is always running as well, so the "
                     "sensor only ever sees the difference.",
             "correct": True},
            {"text": "Because the stomata may be closed, so no gas reaches "
                     "the sensor.",
             "correct": False,
             "why": "Closed stomata would be a problem on a hot dry day, but "
                    "not on an ordinary one. Even with the pores wide open the "
                    "sensor still cannot separate the two processes."},
        ],
        "figure": None,
    },
]
