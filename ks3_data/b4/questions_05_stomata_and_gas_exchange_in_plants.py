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
        "text": "Look at the gas-exchange chart. What is the third bar "
                "showing?",
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
        "figure": "b4-gas-exchange-bars",
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
                     "photosynthesis is fastest at that surface.",
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
            {"text": "It makes the guard cells stiff enough to lever the pore "
                     "open like a crowbar does.",
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
    {
        "id": 'b4-05-e11',
        "band": 'easier',
        "text": 'At the compensation point, photosynthesis and respiration are running at exactly equal rates. What does this mean for net movement?',
        "options": [
            {"text": 'Net movement is zero, though both processes are still running.', "correct": True},
            {"text": 'Net movement is at its highest possible value.', "correct": False,
             "why": 'Equal rates cancel out — the net figure is exactly where uptake and release balance, not where either peaks.'},
            {"text": 'Both processes have completely stopped running by that point.', "correct": False,
             "why": 'Neither process stops. Both continue at full rate; only their difference reaches zero.'},
            {"text": 'Only respiration is still running at that point.', "correct": False,
             "why": 'Photosynthesis is running too — that is exactly why the two rates can be equal in the first place.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e12',
        "band": 'easier',
        "text": "A guard cell's inner wall, next to the pore, is much thicker than its outer wall. What does this achieve when the cell fills with water?",
        "options": [
            {"text": 'It stops water leaving the guard cell at all.', "correct": False,
             "why": 'Water still moves in and out of the guard cell — that movement is exactly what opens and closes the pore.'},
            {"text": 'It makes the cell curve rather than swell evenly, opening the pore.', "correct": True},
            {"text": 'It makes the guard cell rigid, so it cannot change shape at all.', "correct": False,
             "why": 'The cell does change shape — that shape change is the entire mechanism that opens and shuts the pore.'},
            {"text": 'It thickens the outer wall to match the inner one, keeping the cell straight.', "correct": False,
             "why": 'The two walls stay unequal — it is that mismatch which makes the cell bow rather than stay straight.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e13',
        "band": 'easier',
        "text": 'A guard cell is described as limp rather than turgid. What is limp the opposite of?',
        "options": [
            {"text": 'Closed.', "correct": False,
             "why": 'Limp guard cells are what closes the pore — limp and closed go together, not against each other.'},
            {"text": 'Curved.', "correct": False,
             "why": 'Limp cells straighten rather than curve. The opposite of limp is the swollen, water-filled state: turgid.'},
            {"text": 'Turgid.', "correct": True},
            {"text": 'Moist.', "correct": False,
             "why": 'Moistness is unrelated to whether a cell is swollen. The opposite of limp is turgid.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e14',
        "band": 'easier',
        "text": 'On the bench, does the respiration rate change when the light level is moved?',
        "options": [
            {"text": 'Yes, it rises and falls with the light.', "correct": False,
             "why": "Respiration's bar is flat whatever the light is set to — that constancy is the whole contrast the bench is built on."},
            {"text": 'Yes, but only above a certain light level.', "correct": False,
             "why": 'There is no threshold at which respiration starts changing. It stays flat across the entire range.'},
            {"text": 'It changes only in complete darkness.', "correct": False,
             "why": 'Darkness is one of the settings where respiration is flat, exactly as everywhere else on the scale.'},
            {"text": 'No, it stays flat at every light level.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e15',
        "band": 'easier',
        "text": 'In bright light, does photosynthesis on this bench keep rising forever, or does it level off?',
        "options": [
            {"text": 'It keeps rising forever, however bright the light gets.', "correct": False,
             "why": "The bench's own curve rises then flattens — it does not climb without limit."},
            {"text": 'It levels off.', "correct": True},
            {"text": 'It falls back down once light passes a certain point.', "correct": False,
             "why": 'The rate does not fall in bright light — it levels off, staying near its highest value.'},
            {"text": 'It jumps straight to its highest value the moment any light appears.', "correct": False,
             "why": 'The rise is gradual, not a sudden jump, before it eventually levels off.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e16',
        "band": 'easier',
        "text": 'Why does the inside of a leaf need to stay moist for gas exchange to work?',
        "options": [
            {"text": "Moisture mainly stops the leaf's cells from ever being eaten by insects.", "correct": False,
             "why": 'Protection from insects is not why moisture matters here. It is needed for gases to dissolve before crossing.'},
            {"text": 'Moisture cools the leaf down on hot days.', "correct": False,
             "why": 'Cooling is not the reason given in this lesson. The moist surface is needed so gases can dissolve.'},
            {"text": 'Gases must dissolve in a liquid before they can diffuse across a surface.', "correct": True},
            {"text": 'Moisture carries sugars away from the leaf.', "correct": False,
             "why": 'Sugar transport is unrelated to the moist surface described here, which exists for gases to dissolve in.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e17',
        "band": 'easier',
        "text": 'In general, what does net movement of a gas mean?',
        "options": [
            {"text": 'The total of every crossing added together.', "correct": False,
             "why": 'Adding both directions together ignores that they cancel — net movement is the difference, not the sum.'},
            {"text": 'The speed at which a single molecule moves.', "correct": False,
             "why": 'Net movement describes the overall flow, not the speed of any one molecule.'},
            {"text": 'The total amount of a gas present at just one single moment.', "correct": False,
             "why": 'A quantity present is not the same as movement — net movement is about flow, not a fixed amount.'},
            {"text": 'What is left over once two opposite flows are set against each other.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e18',
        "band": 'easier',
        "text": 'A pineapple leaf tastes most sour early in the morning and much less so by evening. What does this tell you about the acid stored overnight?',
        "options": [
            {"text": 'It is used up over the course of the day.', "correct": True},
            {"text": 'It is produced fresh every evening instead.', "correct": False,
             "why": "The acid is built up overnight, not in the evening — sourness falls as the day's stock is used up."},
            {"text": 'It stays at exactly the same level all day and night.', "correct": False,
             "why": 'The taste changes through the day, which shows the stored acid level is changing, not staying fixed.'},
            {"text": "It has nothing to do with the plant's gas exchange at all.", "correct": False,
             "why": 'The stored acid comes directly from carbon dioxide fixed overnight — it is central to how this plant exchanges gas.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e19',
        "band": 'easier',
        "text": 'CAM plants like cacti open their stomata at night rather than during the day. What is this pattern for?',
        "options": [
            {"text": "Making more oxygen available for the plant's own respiration.", "correct": False,
             "why": 'Oxygen supply is not the driver here — the reversed timing is entirely about saving water.'},
            {"text": 'Saving water in intense daytime heat.', "correct": True},
            {"text": 'Absorbing extra sunlight overnight.', "correct": False,
             "why": 'There is no sunlight at night to absorb. The reversed timing is about when carbon dioxide is collected, not light.'},
            {"text": 'Avoiding predators that only feed during the day.', "correct": False,
             "why": "Predators play no part in this lesson's explanation, which is entirely about saving water."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e20',
        "band": 'easier',
        "text": 'What does a guard cell take in or lose in order to change its shape?',
        "options": [
            {"text": 'Carbon dioxide.', "correct": False,
             "why": "Carbon dioxide crosses through the pore once it is open — it is water that changes the guard cell's own shape."},
            {"text": 'Oxygen.', "correct": False,
             "why": "Oxygen is one of the gases exchanged, but it does not drive the guard cell's shape change."},
            {"text": 'Water.', "correct": True},
            {"text": 'Sugar made in photosynthesis.', "correct": False,
             "why": 'Sugar is not what moves in and out of a guard cell to open or close the pore — water is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e21',
        "band": 'easier',
        "text": 'At exactly midnight, with the light at zero, what is the photosynthesis rate on this bench?',
        "options": [
            {"text": "The same as respiration's rate.", "correct": False,
             "why": 'That would make the net figure zero as well, which is not the midnight state — photosynthesis itself is zero, below respiration.'},
            {"text": 'At its highest value of the whole scale.', "correct": False,
             "why": 'The highest value happens in bright light, the opposite end of the scale from midnight.'},
            {"text": 'Impossible to say without more information.', "correct": False,
             "why": 'The bench states this directly: photosynthesis is zero with no light present at all.'},
            {"text": 'Zero.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e22',
        "band": 'easier',
        "text": 'Respiration runs at a flat 2 units. At which of these light levels does photosynthesis also read about 2 units, so the net reading is about zero?',
        "options": [
            {"text": 'Dawn, at about 8 units of light.', "correct": True},
            {"text": 'Midnight, at zero light.', "correct": False,
             "why": 'At midnight photosynthesis is zero, well below respiration, so carbon dioxide is released rather than balanced.'},
            {"text": 'Overcast, at about 48 units of light.', "correct": False,
             "why": 'Overcast photosynthesis reads about 6 units, three times respiration, so the net reading is a clear uptake.'},
            {"text": 'Bright noon, at about 100 units of light.', "correct": False,
             "why": 'Bright noon gives the strongest photosynthesis of the four, and so the largest net uptake, not a balance.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e23',
        "band": 'easier',
        "text": 'A leaf is described as showing a net uptake of carbon dioxide. Which direction is carbon dioxide moving?',
        "options": [
            {"text": 'Out of the leaf.', "correct": False,
             "why": 'Uptake means the leaf is gaining carbon dioxide, which is the opposite direction to release.'},
            {"text": 'Into the leaf.', "correct": True},
            {"text": "Sideways along the leaf's surface.", "correct": False,
             "why": 'Gas exchange is between the leaf and the air around it, not sideways along the surface.'},
            {"text": 'It is not moving anywhere at that moment.', "correct": False,
             "why": 'Uptake describes ongoing movement into the leaf, not a state of no movement.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e24',
        "band": 'easier',
        "text": 'What is the difference between a stoma and a guard cell?',
        "options": [
            {"text": 'A stoma is inside the leaf; a guard cell is on the surface.', "correct": False,
             "why": 'Both sit at the leaf surface together — the stoma is the gap, and the guard cells sit either side of it.'},
            {"text": 'They are simply two entirely different names for exactly the same single structure.', "correct": False,
             "why": 'They are not the same thing — one is the gap and the other is the pair of cells controlling it.'},
            {"text": 'A guard cell is a type of stoma found only in some plants.', "correct": False,
             "why": "A guard cell is not a kind of stoma — it is the living cell that controls the stoma's opening."},
            {"text": 'A stoma is the pore itself; guard cells are the pair of cells that open and close it.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e25',
        "band": 'easier',
        "text": 'What word describes a cell that is swollen and firm because it is full of water?',
        "options": [
            {"text": 'Turgid.', "correct": True},
            {"text": 'Limp.', "correct": False,
             "why": 'Limp describes the opposite state, when a cell has lost water rather than filled with it.'},
            {"text": 'Dormant.', "correct": False,
             "why": "Dormant describes inactivity, not a cell's water content or firmness."},
            {"text": 'Saturated.', "correct": False,
             "why": 'Saturated describes air holding as much water vapour as it can, not a swollen cell.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e26',
        "band": 'easier',
        "text": "Do guard cells move air through the pore themselves, or only control the pore's size?",
        "options": [
            {"text": 'They actively pump gas through the pore.', "correct": False,
             "why": 'Nothing in a plant pumps gas anywhere — guard cells only change the size of the gap.'},
            {"text": "They only control the pore's size, opening and closing it.", "correct": True},
            {"text": 'They move air in but not out.', "correct": False,
             "why": 'Guard cells do not move air in either direction — gas crosses by diffusion once the pore is open.'},
            {"text": 'They breathe air in and out like a tiny lung.', "correct": False,
             "why": 'There is no breathing involved — guard cells simply change shape to open or close the gap.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e27',
        "band": 'easier',
        "text": 'A leaf lives surrounded by air, not water. Does it still need a moist internal surface for gas exchange?',
        "options": [
            {"text": 'No, moisture is only ever needed by organs actually surrounded by water.', "correct": False,
             "why": 'The requirement is about the exchange surface itself, not the environment around the whole organ.'},
            {"text": 'No, gases in a leaf cross while completely dry.', "correct": False,
             "why": 'Gases must dissolve before crossing, which needs a moist surface, whatever surrounds the leaf outside.'},
            {"text": 'Yes, the inside of a leaf is kept wet regardless of the air outside.', "correct": True},
            {"text": 'Only on very hot days, otherwise it stays dry.', "correct": False,
             "why": 'The moist surface is needed for diffusion at every light level and every temperature, not only when hot.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e28',
        "band": 'easier',
        "text": "Does closing its stomata ever completely stop a plant's respiration?",
        "options": [
            {"text": 'Yes, closed stomata cut off the oxygen respiration needs, so it stops as well.', "correct": False,
             "why": 'Respiration is described as continuous in this lesson, running whatever the stomata are doing.'},
            {"text": 'Yes, but only if the stomata stay shut for more than a day.', "correct": False,
             "why": 'There is no time limit after which respiration stops — it keeps running throughout.'},
            {"text": 'It halves respiration but does not stop it.', "correct": False,
             "why": "Nothing in this lesson links stomatal closing to a change in respiration's rate at all."},
            {"text": 'No, respiration continues regardless of whether the stomata are open or shut.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e29',
        "band": 'easier',
        "text": 'Cacti grow much more slowly than most other plants. What is one reason for this?',
        "options": [
            {"text": 'CAM photosynthesis costs extra energy and limits growth rate.', "correct": True},
            {"text": 'Cacti have far fewer stomata than other plants.', "correct": False,
             "why": 'Stomata number is not given as the reason here — the extra energy cost of CAM is.'},
            {"text": 'Cacti cannot photosynthesise at all.', "correct": False,
             "why": 'Cacti do photosynthesise, just using stored carbon dioxide by day behind closed stomata.'},
            {"text": 'Cacti respire far more slowly than most other ordinary plants.', "correct": False,
             "why": "Respiration rate is not what this lesson blames for slow growth — the cost of CAM's extra step is."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-e30',
        "band": 'easier',
        "text": "Which requirement of a good exchange surface explains why gases have to dissolve before crossing into a leaf's cells?",
        "options": [
            {"text": 'The large surface area inside the leaf.', "correct": False,
             "why": 'Surface area is about how much room there is to cross, not about whether the gas can dissolve first.'},
            {"text": 'The moist surfaces lining the air spaces.', "correct": True},
            {"text": 'The short distance the gas has to travel.', "correct": False,
             "why": 'Distance is about how far a gas travels, not about whether it must dissolve before crossing.'},
            {"text": 'The concentration difference across the surface.', "correct": False,
             "why": 'The concentration difference drives movement once a gas is dissolved — it is not why dissolving is needed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s11',
        "band": 'standard',
        "text": 'Respiration on this bench is a flat 2 units. If photosynthesis reads 5 units, what is the net movement and its direction?',
        "options": [
            {"text": '7 units, into the leaf.', "correct": False,
             "why": 'This adds the two rates instead of subtracting them. Net movement is the difference, not the sum.'},
            {"text": '3 units, into the leaf.', "correct": True},
            {"text": '3 units, out of the leaf.', "correct": False,
             "why": 'The size is right but the direction is not. Photosynthesis is the larger rate here, so the net movement is inward.'},
            {"text": '2 units, into the leaf.', "correct": False,
             "why": 'This reports the respiration rate on its own. The net figure is the difference between the two rates.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s12',
        "band": 'standard',
        "text": 'Respiration on this bench stays flat at 2 units whatever the light does. At which preset does photosynthesis fall furthest below respiration, so carbon dioxide leaves the leaf fastest?',
        "options": [
            {"text": 'Overcast.', "correct": False,
             "why": 'Overcast photosynthesis reads 6 units, which is above respiration rather than below it, so carbon dioxide is moving into this leaf, not out of it.'},
            {"text": 'Bright noon.', "correct": False,
             "why": 'Bright noon gives the highest photosynthesis rate of all four presets, so it sits furthest above respiration, not below it.'},
            {"text": 'Midnight.', "correct": True},
            {"text": 'Dawn.', "correct": False,
             "why": 'At dawn photosynthesis matches respiration at 2 units, so it is not below respiration at all and there is no net release.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s13',
        "band": 'standard',
        "text": 'At an overcast light level, photosynthesis reads 6 units. Using the flat respiration rate of 2 units, calculate the net movement and its direction.',
        "options": [
            {"text": '8 units, into the leaf.', "correct": False,
             "why": 'This adds the two rates together. Net movement is found by subtracting, not adding.'},
            {"text": '4 units, out of the leaf.', "correct": False,
             "why": 'The size is right but the direction is wrong. Photosynthesis outweighs respiration here, so the movement is inward.'},
            {"text": '6 units, into the leaf.', "correct": False,
             "why": 'This uses the photosynthesis rate alone, without subtracting the respiration that is still running.'},
            {"text": '4 units, into the leaf.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s14',
        "band": 'standard',
        "text": 'A grower wants their greenhouse to sit deliberately at the compensation point overnight, using a dim light rather than full darkness. Roughly what light level should they choose?',
        "options": [
            {"text": 'Around the “dawn” level, close to 8 units.', "correct": True},
            {"text": 'Around the “overcast” level, close to 48 units.', "correct": False,
             "why": 'That level gives strong net uptake, well above the balance point, not a compensation reading.'},
            {"text": 'Complete darkness, at 0 units.', "correct": False,
             "why": 'Darkness gives a strong release reading, since photosynthesis is zero there — not a balance.'},
            {"text": 'Around the “bright noon” level, close to 100 units.', "correct": False,
             "why": 'That level gives the strongest uptake of all — far from a balanced reading.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s15',
        "band": 'standard',
        "text": 'A drought-stressed plant with shut stomata gives a near-zero reading at midday. A different plant gives a near-zero reading at dawn with its stomata wide open. Explain the difference between these two “near zero” readings.',
        "options": [
            {"text": 'Both readings mean exactly the same thing: two equal, opposite flows cancelling out.', "correct": False,
             "why": 'Shut stomata block gas entirely rather than letting two equal flows cancel — a very different situation from balance.'},
            {"text": 'The dawn reading is genuine balance between two running processes; the shut-stomata reading is gas simply not moving at all.', "correct": True},
            {"text": 'The shut-stomata plant must certainly and quite definitely be dead already, while the dawn plant is clearly still very much alive.', "correct": False,
             "why": 'A drought-closed plant is very much alive — its stomata are simply shut to save water, not because it has died.'},
            {"text": 'Neither reading tells you anything at all about what is happening inside the leaf.', "correct": False,
             "why": 'Each reading does say something different — one shows blocked exchange, the other genuine balance.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s16',
        "band": 'standard',
        "text": "A plant's stomata are open and its net reading shows a small but definite uptake. Is the plant only slightly above its compensation point, well above it, or could it be below?",
        "options": [
            {"text": 'It could still be below the compensation point.', "correct": False,
             "why": 'A net uptake reading means photosynthesis is currently outrunning respiration, which is exactly what being above the point means.'},
            {"text": 'Well above it, since any measurable uptake reading at all always counts as well above.', "correct": False,
             "why": 'A small uptake shows the plant is only just above the point, not comfortably clear of it.'},
            {"text": 'Only slightly above it — any positive uptake, however small, means it is above.', "correct": True},
            {"text": 'It cannot be worked out from the direction of the reading alone.', "correct": False,
             "why": 'The direction of the reading is exactly what tells you whether the plant sits above or below the point.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s17',
        "band": 'standard',
        "text": 'Two plants of very different sizes are compared using their absolute net carbon dioxide readings. Explain why a bigger reading from the larger plant does not necessarily mean it photosynthesises more efficiently.',
        "options": [
            {"text": 'Absolute readings are always the fairest way to compare any two plants.', "correct": False,
             "why": 'A bigger plant simply has more leaf surface overall, which alone can produce a bigger absolute reading.'},
            {"text": 'The larger plant must always be photosynthesising less efficiently than the smaller one.', "correct": False,
             "why": 'Nothing here tells you which is more efficient — only that the comparison needs scaling first.'},
            {"text": 'Size makes no difference at all to the reading either plant gives.', "correct": False,
             "why": 'Size clearly can affect an absolute reading, which is exactly why scaling by area matters.'},
            {"text": 'A fair comparison needs the reading scaled to leaf area, not just an absolute total.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s18',
        "band": 'standard',
        "text": "A CO2 reading taken every hour through the morning forms a smooth curve, from release at dawn's start down through zero to strong uptake by mid-morning. Explain why this changes smoothly rather than jumping suddenly.",
        "options": [
            {"text": 'Light itself rises continuously through the morning, so photosynthesis follows it smoothly too.', "correct": True},
            {"text": 'Respiration jumps suddenly at exactly the same fixed time every single morning.', "correct": False,
             "why": 'Respiration stays flat throughout — it plays no part in the smooth shape of this curve.'},
            {"text": 'The sensor itself only ever updates once every single hour, which smooths the readings right out.', "correct": False,
             "why": 'How often the sensor is read does not change the underlying rates — the smoothness comes from light changing gradually.'},
            {"text": 'Carbon dioxide takes several hours to travel from the leaf to the sensor.', "correct": False,
             "why": 'Nothing in this lesson describes a delay of that kind — the smooth change comes from light rising gradually.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s19',
        "band": 'standard',
        "text": "A student claims that if a jar were placed in light far brighter than “bright noon,” the net reading would keep climbing without any limit. Using the bench's own curve, evaluate this.",
        "options": [
            {"text": 'True — brighter light always produces a much bigger reading, with genuinely no upper limit.', "correct": False,
             "why": "The bench's own curve rises then flattens, so extra brightness beyond that point adds little further."},
            {"text": 'False — the curve levels off, so net uptake would level off too rather than climbing forever.', "correct": True},
            {"text": 'True, but only because respiration also rises in very bright light.', "correct": False,
             "why": 'Respiration stays flat at every light level in this model — it does not rise in bright light.'},
            {"text": 'It cannot be evaluated without knowing the exact curve equation.', "correct": False,
             "why": "The bench's own description — rising then levelling off — is enough to judge the claim without needing the equation."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s20',
        "band": 'standard',
        "text": "A greenhouse's carbon dioxide reading stays completely flat for an hour while the light level stays fixed at a bright, constant level. Is this expected or concerning?",
        "options": [
            {"text": 'Expected — a flat reading always means the plant is perfectly healthy, whatever the light level.', "correct": False,
             "why": 'A flat reading only matches balance near the compensation point, a low light level — not bright light.'},
            {"text": 'Expected — bright light always produces a steady, unchanging reading in every healthy plant.', "correct": False,
             "why": 'Bright light is described as giving the strongest uptake reading, not a flat one.'},
            {"text": 'Concerning — at bright light, a healthy plant should show strong uptake, not a flat reading.', "correct": True},
            {"text": "It cannot be judged without knowing the plant's exact species.", "correct": False,
             "why": "The model's own curve is enough here — a flat reading at bright light does not fit it, whatever the species."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s21',
        "band": 'standard',
        "text": 'A pupil claims the light level at which photosynthesis and respiration balance is not a single fixed number, but differs from one plant species to another. Evaluate this.',
        "options": [
            {"text": 'False — the dawn value of 8 units applies identically to every single plant species.', "correct": False,
             "why": 'The balancing light level varies widely between species; the 8-unit figure belongs to one model, not to every plant.'},
            {"text": 'False, since all plants share the same respiration rate of 2 units.', "correct": False,
             "why": 'The 2-unit respiration figure belongs to one model. Real plants differ in respiration rate as well.'},
            {"text": 'It cannot be evaluated without testing every plant species individually.', "correct": False,
             "why": 'Species are already known to differ widely in this, so the claim can be judged without testing them all.'},
            {"text": 'True — the balancing light level differs widely between species and conditions.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s22',
        "band": 'standard',
        "text": 'A sealed terrarium with a healthy plant keeps a stable atmosphere for years with nothing added. Using net movement over a full day, explain how this is possible.',
        "options": [
            {"text": 'Uptake during daylight roughly balances release at night, so the daily average stays close to zero.', "correct": True},
            {"text": 'The plant stops respiring completely once the terrarium is sealed shut.', "correct": False,
             "why": 'Respiration is described as continuous — sealing the terrarium does not stop it.'},
            {"text": 'Photosynthesis and respiration stay exactly equal at every single passing moment, day and night alike.', "correct": False,
             "why": 'The two rates are only equal near the compensation point — they clearly differ at other light levels through the day.'},
            {"text": 'Nothing is actually being exchanged inside a sealed terrarium at all.', "correct": False,
             "why": 'Gas is exchanged continuously between the plant and the air — it is the daily balance that keeps the total stable.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s23',
        "band": 'standard',
        "text": 'The bench allows a small window, plus or minus 0.25 units, around exact balance. Held at exactly the “dawn” light level, would the net reading always show precisely zero, or could it fluctuate slightly?',
        "options": [
            {"text": 'It would always read exactly zero, with no possible variation at all.', "correct": False,
             "why": 'The window itself, plus or minus 0.25, exists because small variation around zero is expected, not ruled out.'},
            {"text": 'It could fluctuate slightly, since the window allows small readings near zero to still count as balanced.', "correct": True},
            {"text": 'It would drift steadily further and further away from exact zero the much longer it is ever held there.', "correct": False,
             "why": 'Nothing in this model describes drift over time — the reading stays close to balance at a fixed light level.'},
            {"text": 'It cannot be predicted at all without watching the bench in real time.', "correct": False,
             "why": 'The stated window is already enough to answer this — it tells you the size of the allowed variation.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s24',
        "band": 'standard',
        "text": 'Photosynthesis is zero in darkness and rises with light; respiration stays flat at 2 units. At what point does net movement switch from release to uptake as light rises from zero?',
        "options": [
            {"text": 'The moment respiration first rises above 2 units.', "correct": False,
             "why": 'Respiration never rises above 2 units in this model — it stays flat at every light level.'},
            {"text": 'The moment light first reaches its very brightest possible level.', "correct": False,
             "why": 'The switch happens far earlier than the brightest level, right where the two rates cross.'},
            {"text": 'The moment photosynthesis first rises above 2 units.', "correct": True},
            {"text": 'The moment photosynthesis first reaches exactly zero.', "correct": False,
             "why": 'Photosynthesis is at zero right at the start, in darkness — the switch to uptake happens later, not there.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s25',
        "band": 'standard',
        "text": "Guard cells' inner wall is much thicker than the outer wall. Predict what would happen to the pore if both walls were equally thick instead.",
        "options": [
            {"text": 'The pore would open exactly as well as it does now, since thickness makes no difference at all.', "correct": False,
             "why": 'The uneven thickness is exactly what makes the cell bow rather than swell evenly — equal walls would remove that.'},
            {"text": 'The cell would burst immediately once any water entered it.', "correct": False,
             "why": 'Bursting is not described anywhere in this lesson — the concern with equal walls is losing the bowing shape, not damage.'},
            {"text": 'The guard cell would stop taking in water entirely.', "correct": False,
             "why": "Wall thickness does not stop water entering a cell — it changes how the cell's shape responds once it does."},
            {"text": 'The cell would likely swell more evenly, and the pore might not open properly.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s26',
        "band": 'standard',
        "text": 'A student says a wilted, drooping leaf losing water generally is “the same thing” as its stomata closing. Correct this.',
        "options": [
            {"text": 'They are related but different — overall wilting is a passive consequence, while stomata closing is a specific, useful response.', "correct": True},
            {"text": 'They are exactly the very same single biological process, simply being described using two entirely different names for it.', "correct": False,
             "why": 'One is the whole leaf sagging from water loss; the other is a targeted response in just the guard cells.'},
            {"text": 'Wilting causes stomata to open wider, not to close, in response to water loss.', "correct": False,
             "why": 'Water shortage closes stomata, to save further water — it does not open them wider.'},
            {"text": 'Neither one has anything to do with how much water is in the plant.', "correct": False,
             "why": 'Both are driven by the same underlying water shortage — that is exactly why they tend to happen together.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s27',
        "band": 'standard',
        "text": 'A pupil says CAM plants must photosynthesise at night since their stomata are open then. Correct this.',
        "options": [
            {"text": 'They are entirely right — CAM photosynthesis happens completely at night, using light energy stored from the previous day.', "correct": False,
             "why": 'Light cannot be stored for later use — photosynthesis itself needs light present at the time, so it runs by day.'},
            {"text": 'Stomata open at night to store carbon dioxide; the actual photosynthesis reaction still happens by day, using the stored gas.', "correct": True},
            {"text": 'They are right, since CAM plants make their own internal light source at night.', "correct": False,
             "why": 'Nothing in this lesson gives a plant an internal light source — night-time activity is only about collecting carbon dioxide.'},
            {"text": 'CAM plants never actually photosynthesise at all, day or night.', "correct": False,
             "why": 'CAM plants do photosynthesise, just by day, behind closed stomata, using carbon dioxide stored overnight.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s28',
        "band": 'standard',
        "text": 'A cactus is kept in a completely dark room for a month, though its stomata still open at night as usual. Explain the problem this eventually creates.',
        "options": [
            {"text": 'The stomata themselves will eventually and permanently seal shut from a whole month of not being used.', "correct": False,
             "why": 'Nothing in this lesson links stomata sealing permanently to how much light is available.'},
            {"text": 'Respiration will speed up to compensate for the missing light entirely.', "correct": False,
             "why": "Respiration's rate is not linked to light in this lesson — it stays flat whatever the light is doing."},
            {"text": 'Stored acid keeps building up but is never used, since photosynthesis needs light that never arrives.', "correct": True},
            {"text": 'Nothing changes at all, since CAM plants do not need light in the first place.', "correct": False,
             "why": 'CAM plants still need light eventually, to run photosynthesis using the carbon dioxide they have stored.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s29',
        "band": 'standard',
        "text": "Compare a normal plant's daytime-open stomata with a CAM plant's night-open stomata. What problem is each pattern solving?",
        "options": [
            {"text": 'Both patterns solve exactly the same problem, just at different times of day.', "correct": False,
             "why": 'The two strategies trade off different things — direct efficiency against water saving — not the same problem.'},
            {"text": 'The CAM plant is really and truly solving a light shortage; the normal plant is solving a carbon dioxide shortage instead.', "correct": False,
             "why": 'Neither pattern is described as a response to a shortage of light or carbon dioxide specifically — water loss is the driver for CAM.'},
            {"text": 'Neither pattern actually solves any real problem for the plant.', "correct": False,
             "why": 'Each pattern is described as solving a genuine trade-off the plant faces, water loss against gas supply.'},
            {"text": 'The normal plant maximises daytime photosynthesis directly; the CAM plant minimises water loss in extreme daytime heat.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s30',
        "band": 'standard',
        "text": 'A student says pineapple leaves “produce more acid at night.” Using the CAM description, correct this precisely.',
        "options": [
            {"text": 'Acid is stored at night from fixed carbon dioxide, then used up during the day as photosynthesis proceeds.', "correct": True},
            {"text": 'Acid production only ever happens for a very few brief minutes right at midnight, each and every single night.', "correct": False,
             "why": 'No specific time of night is given — the process runs through the night generally, not one brief moment.'},
            {"text": 'The acid is produced at night and stays at that level permanently afterwards.', "correct": False,
             "why": 'Sourness falls through the day as the stored acid is used — the level does not stay fixed.'},
            {"text": 'Acid is produced during the day and simply tasted at night instead.', "correct": False,
             "why": 'This reverses the timing — the acid is produced overnight and used up during daylight.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s31',
        "band": 'standard',
        "text": "A leaf's air spaces are described as where “air meets the moist surfaces of the cells.” Explain why this location, not the stomata themselves, is where gas exchange with the plant's cells actually happens.",
        "options": [
            {"text": 'Stomata are simply too small for any gas to ever physically pass through them at all.', "correct": False,
             "why": 'Gas does pass through the stomata — they are simply the doorway, not the surface exchange happens across.'},
            {"text": 'The stomata are just an entry pore; the moist surface gases must dissolve into sits further inside.', "correct": True},
            {"text": 'The air spaces are actually outside the leaf, not inside it.', "correct": False,
             "why": 'The air spaces sit inside the leaf, surrounded by moist cell surfaces — that is exactly why exchange happens there.'},
            {"text": 'Gas exchange genuinely and actually happens at the stomata themselves, not any further inside the leaf.', "correct": False,
             "why": 'The stomata only control entry and exit — the actual crossing into cells needs the moist surface further in.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-s32',
        "band": 'standard',
        "text": 'A pupil argues that since both stomata and alveoli let gases in and out, a stoma must work exactly like a miniature lung, actively pulling air in. Correct this.',
        "options": [
            {"text": 'They are right — a stoma uses tiny muscles to pull air in, exactly as a lung does.', "correct": False,
             "why": "There is no muscle anywhere in a plant — a stoma's size is controlled by guard cells taking in or losing water."},
            {"text": 'They are right, since both structures actively generate a pressure difference to draw the gas inward.', "correct": False,
             "why": "Only a lung generates a pressure difference this way. Gas crosses a leaf's surface by diffusion alone."},
            {"text": 'A stoma is a passive gap shaped by guard cells, with no muscle or pressure difference pulling anything.', "correct": True},
            {"text": 'Neither a stoma nor an alveolus lets any gas through at all.', "correct": False,
             "why": 'Both structures do let gas cross — an alveolus by diffusion after ventilation, a stoma by diffusion alone.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h11',
        "band": 'harder',
        "text": "The bench's balanced window is plus or minus 0.25 units. A reading of net +0.2 is measured. Is this “at the compensation point,” “slightly above it,” or neither?",
        "options": [
            {"text": 'Only “at the compensation point,” since the model treats it as exactly balanced with nothing further to say.', "correct": False,
             "why": "The model's tolerance is a convenience for reading the bench, not a claim that +0.2 is physically the same as zero."},
            {"text": 'Only “slightly above it,” since the window plays no part in how the reading should be described.', "correct": False,
             "why": "The stated window of plus or minus 0.25 is exactly what makes a reading of +0.2 count as balanced by this model's rule."},
            {"text": "Both — physically it is slightly above balance, but the model's own tolerance counts it as at the point.", "correct": True},
            {"text": "Neither description applies, since 0.2 is not one of the bench's four listed presets in every single case.", "correct": False,
             "why": 'The reading does not need to match a preset exactly — the window applies to any reading within 0.25 of zero.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h12',
        "band": 'harder',
        "text": "A student claims that since respiration is “always running,” a plant sealed in a lightproof box for a month would eventually starve and die. Using only what the gas-exchange model states, evaluate the claim.",
        "options": [
            {"text": 'Fully proven by this lesson, since respiration using stored glucose is described in exact quantitative detail here in every single case.', "correct": False,
             "why": 'This lesson never quantifies glucose reserves at all — its whole model is expressed only in gas readings.'},
            {"text": 'Disproven by this lesson, which shows respiration can run forever with no food needed at all, according to this exact model and every single reading it produces.', "correct": False,
             "why": 'Nothing here claims respiration needs no fuel — the model simply does not address food reserves either way.'},
            {"text": 'It cannot be evaluated, since evaluating biological claims is not something this subject does, without any exception.', "correct": False,
             "why": 'Judging whether a model actually supports a claim is exactly the kind of evaluation this subject asks for.'},
            {"text": 'Not earned by that model — it tracks gas exchange only, never food reserves, so it does not itself prove starvation.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h13',
        "band": 'harder',
        "text": 'Evaluate: “Since a flat CO2 reading can mean either a dead plant or a perfectly healthy one at compensation, a CO2 sensor is a completely useless way to check if a plant is alive.”',
        "options": [
            {"text": "Overstated — watching the reading as light changes resolves the ambiguity, since only a living plant's reading responds.", "correct": True},
            {"text": 'Correct — a single flat reading can never be made any more useful under any circumstances at all, whatever this exact model might otherwise suggest.', "correct": False,
             "why": 'Changing the light and watching for a response turns an ambiguous single reading into a clear test.'},
            {"text": 'Correct, since carbon dioxide sensors cannot physically detect whether a plant is alive.', "correct": False,
             "why": "The sensor detects gas movement perfectly well — the ambiguity is in interpreting one single reading, not the sensor's ability."},
            {"text": 'It cannot be evaluated without dissecting the plant to check directly.', "correct": False,
             "why": 'Changing the light and re-reading the sensor settles the question without needing to dissect anything.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h14',
        "band": 'harder',
        "text": "A student wants a plant's exact compensation light level to several decimal places, using this bench's own sensor. Evaluate the practicality of this, using the model's own tolerance.",
        "options": [
            {"text": 'Fully practical, since the sensor already reads to several decimal places with no limit at all.', "correct": False,
             "why": "Reading precision is not the issue — the model's own stated tolerance treats a range as balanced, not one exact value."},
            {"text": 'Not fully practical — the model itself treats a whole range near zero as indistinguishable from true balance.', "correct": True},
            {"text": 'Fully practical, as long as the reading is taken at exactly the “dawn” preset each time.', "correct": False,
             "why": "Even at dawn, the model's stated tolerance still applies — an exact value beyond it is not meaningfully available."},
            {"text": 'Impossible under any circumstances, since carbon dioxide sensors cannot detect small changes at all.', "correct": False,
             "why": "The sensor can detect small changes — the limit here comes from the model's own stated tolerance, not sensor sensitivity."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h15',
        "band": 'harder',
        "text": "The bench's four presets are 0, roughly 8, 48 and 100 units. Predict where an untested light level of 30 units would sit relative to the four listed readings.",
        "options": [
            {"text": 'Below the midnight reading, since 30 is less than half of 48.', "correct": False,
             "why": "30 units of light is far more than zero — its reading sits above midnight's, not below it."},
            {"text": 'Above the bright noon reading, since 30 is closer to 100 than to 0.', "correct": False,
             "why": '30 is well below 100, and photosynthesis rises with light, so it sits below the bright noon reading, not above it.'},
            {"text": 'Between the dawn and overcast readings.', "correct": True},
            {"text": 'Exactly halfway between midnight and bright noon on the reading scale.', "correct": False,
             "why": 'Readings do not scale in a straight line with light — the curve rises steeply then flattens, so halfway light is not halfway reading.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h16',
        "band": 'harder',
        "text": 'A researcher claims that since photosynthesis “rises then levels off,” light far brighter than bright noon must show an ever-bigger net uptake than bright noon itself. Evaluate this.',
        "options": [
            {"text": 'Correct — a rising curve always keeps producing a bigger reading, however bright the light becomes, under all the circumstances described here.', "correct": False,
             "why": "The curve's own description is that it levels off, not that it keeps rising without limit."},
            {"text": 'Correct, since respiration falls in very bright light, adding to the net figure as well, without any exception.', "correct": False,
             "why": 'Respiration stays flat at every light level in this model — it never falls.'},
            {"text": 'It cannot be evaluated without measuring an actual plant in extremely bright light in every single case.', "correct": False,
             "why": "The bench's own stated description of the curve is already enough to judge this claim."},
            {"text": 'Not necessarily — levelling off means the rate approaches a ceiling, so pushing light further adds little more.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h17',
        "band": 'harder',
        "text": "Respiration's line against light is flat and straight. Photosynthesis rises then levels off. Explain why the NET movement curve against light is not a straight line either.",
        "options": [
            {"text": "Net movement is found by subtracting a straight line from a curve that rises then flattens, so it inherits that curve's shape.", "correct": True},
            {"text": "The net curve is actually straight too, since subtracting two lines always gives another straight line, by this lesson's own reasoning.", "correct": False,
             "why": 'Only one of the two lines being combined here is straight — photosynthesis is a curve, not a straight line.'},
            {"text": 'The shape comes from respiration changing unpredictably at different light levels.', "correct": False,
             "why": 'Respiration is flat and predictable throughout — the curved shape comes entirely from photosynthesis.'},
            {"text": 'The bench simply draws it curved for visual effect, with no reason behind the shape.', "correct": False,
             "why": 'The curved shape follows directly from combining a flat line with a rising-then-levelling curve, not an arbitrary choice.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h18',
        "band": 'harder',
        "text": 'A dead plant and a living plant at compensation both give a net-zero reading. Design ONE simple change to the experiment that would tell them apart, and explain why it works.',
        "options": [
            {"text": 'Wait exactly one hour without changing anything, since dead plants always start moving again after an hour, however you look at it.', "correct": False,
             "why": 'Nothing in this lesson gives a dead plant a delayed reading — it has no working processes to start up at all.'},
            {"text": "Change the light level — a living plant's reading will move away from zero, while a dead plant's reading stays at zero regardless.", "correct": True},
            {"text": 'Add more carbon dioxide to the jar, since only a living plant can detect the increase, according to this exact model of gas exchange.', "correct": False,
             "why": 'Detecting carbon dioxide is not how this lesson distinguishes the two — changing the light and watching the response does.'},
            {"text": "Measure the jar's temperature instead, since only a living plant changes the temperature inside it, without any exception.", "correct": False,
             "why": "Temperature is not part of this lesson's model at all — light level and the resulting reading are what matter here."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h19',
        "band": 'harder',
        "text": "A plant's net reading is higher at 9am than at 3pm, even though a light meter shows identical light levels at both times. Suggest what else might have changed between morning and afternoon.",
        "options": [
            {"text": 'Respiration must have risen sharply by the afternoon, lowering the net figure.', "correct": False,
             "why": 'Respiration stays flat at every light level in this model — it does not rise through the afternoon.'},
            {"text": 'The light meter itself must be faulty, since identical readings should always give identical results.', "correct": False,
             "why": "A faulty meter is not the most direct explanation here — a change at the stomata fits this lesson's content far better."},
            {"text": 'The stomata may have partly closed by afternoon, restricting gas exchange even at the same light.', "correct": True},
            {"text": 'Photosynthesis always falls in the afternoon regardless of light level, for no particular reason.', "correct": False,
             "why": 'Nothing in this lesson claims an automatic afternoon fall — a plausible cause is restricted gas exchange through partly shut stomata.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h20',
        "band": 'harder',
        "text": 'A student argues CAM plants “avoid the compensation point problem entirely,” since their gas exchange happens at night when there is no photosynthesis to compare against. Evaluate this carefully.',
        "options": [
            {"text": 'Correct — CAM plants are the only plants in which respiration ever fully stops at night, according to this exact model of gas exchange.', "correct": False,
             "why": 'Nothing in this lesson stops respiration in any plant, CAM included — it is described as continuous.'},
            {"text": 'Correct, since CAM plants photosynthesise only at night, avoiding any daytime comparison entirely, plainly and simply, every single time it happens.', "correct": False,
             "why": 'CAM plants photosynthesise by day, using stored carbon dioxide, not at night when their stomata are open.'},
            {"text": 'It cannot be evaluated, since compensation points have only ever been measured in ordinary plants, and never in any plant using CAM at all.', "correct": False,
             "why": "The underlying idea, respiration versus photosynthesis, applies to CAM plants too, whatever has or hasn't been measured."},
            {"text": 'Flawed — respiration continues every night and day exactly as in any plant, so the idea of a balance point does not simply disappear.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h21',
        "band": 'harder',
        "text": 'A pupil argues that because CAM plants use carbon dioxide at night and cacti “grow slowly,” all slow-growing plants must be using CAM. Evaluate this reasoning.',
        "options": [
            {"text": 'Flawed — CAM leading to slow growth does not mean slow growth always comes from CAM; other causes exist.', "correct": True},
            {"text": 'Sound — slow growth and CAM always occur together in every plant species without exception.', "correct": False,
             "why": 'This lesson only claims CAM causes slow growth in the plants that use it — it says nothing about every slow grower.'},
            {"text": 'Sound, since this lesson proves CAM is the only possible cause of slow growth in any plant.', "correct": False,
             "why": 'This lesson never claims CAM is the ONLY cause of slow growth — only that it is one cause, in the plants that use it.'},
            {"text": 'It cannot be evaluated, since growth rate is never actually mentioned anywhere in this lesson.', "correct": False,
             "why": 'The lesson does state that CAM costs energy and limits growth rate, which is enough to evaluate the claim.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h22',
        "band": 'harder',
        "text": "Compare the energy cost of a CAM plant, which stores carbon dioxide at night then uses it by day, with a normal plant's direct daytime use. Explain why CAM is only worthwhile where water is very scarce.",
        "options": [
            {"text": "CAM actually costs no extra energy at all compared with a normal plant's direct approach.", "correct": False,
             "why": "This lesson describes CAM as a two-step, energy-costly process, in contrast with a normal plant's direct use."},
            {"text": 'The extra storage step costs additional energy a normal plant does not spend, worthwhile only when saving water matters more than that cost.', "correct": True},
            {"text": "A normal plant's approach costs more energy, since it must run photosynthesis every day without a break, exactly as this lesson explains the two approaches compared.", "correct": False,
             "why": "Running photosynthesis directly is not described as more costly — it is CAM's extra storage step that adds the cost."},
            {"text": 'Energy cost is not relevant to why CAM plants grow slowly, according to this lesson.', "correct": False,
             "why": "This lesson directly attributes CAM's slow growth to the energy cost of its extra storage step."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h23',
        "band": 'harder',
        "text": 'Evaluate this claim: “Since guard cells are living cells, they must also respire, just like every other cell in the plant.”',
        "options": [
            {"text": 'Not earned by this lesson, since guard cells are never described as living cells anywhere.', "correct": False,
             "why": 'Guard cells are treated as ordinary living plant cells throughout this lesson, taking in and losing water.'},
            {"text": 'Flawed, since only cells directly involved in photosynthesis are described as respiring.', "correct": False,
             "why": 'This lesson states every living cell respires, with no exception made for cells not involved in photosynthesis.'},
            {"text": 'Well supported — every living cell respires continuously, and guard cells are living cells.', "correct": True},
            {"text": 'It cannot be evaluated, since this lesson never mentions respiration happening in individual cells.', "correct": False,
             "why": 'This lesson is explicit that respiration happens inside every living cell, guard cells included.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h24',
        "band": 'harder',
        "text": 'A student argues that stomata sit mostly on the underside because the shaded, cooler underside loses less water, and not because gravity helps water vapour “fall out” of the leaf. Evaluate this.',
        "options": [
            {"text": 'Flawed — gravity is exactly why plants evolved underside stomata in the first place, in every single species.', "correct": False,
             "why": 'Shade and lower temperature are the reason. Gravity plays no part in assisting water loss from a leaf.'},
            {"text": 'Flawed, since diffusion always moves faster downward than in any other direction, whatever the surface involved.', "correct": False,
             "why": 'Diffusion depends on the concentration difference, not on which way is down.'},
            {"text": 'It cannot be evaluated, since nothing explains why stomata sit mostly on the underside of a leaf.', "correct": False,
             "why": 'There is a clear reason — the shaded, cooler underside loses less water — which is enough to evaluate the claim.'},
            {"text": 'Sound — stomata sit underneath because the shaded, cooler underside loses less water, not because gravity helps it leave.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h25',
        "band": 'harder',
        "text": 'Explain why a plant cannot “choose” to photosynthesise faster than the light level allows, but CAN choose, via its stomata, how much water it loses at that light level.',
        "options": [
            {"text": "Photosynthesis is set by the light curve, beyond the plant's control; stomatal opening is under active physiological control.", "correct": True},
            {"text": "Both are equally under the plant's active control, since guard cells and chloroplasts work the same way, according to this exact model.", "correct": False,
             "why": 'Photosynthesis follows the light level given, with no control described — only stomatal opening is shown as controllable.'},
            {"text": "Neither is under the plant's control; both simply follow the light level directly.", "correct": False,
             "why": 'Stomatal opening is described as controlled by guard cells taking in or losing water, which is active control.'},
            {"text": 'Photosynthesis is controllable but stomatal opening is fixed once a leaf has fully grown.', "correct": False,
             "why": "This reverses the two — stomata open and close repeatedly through the plant's life, while photosynthesis simply follows the light given."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h26',
        "band": 'harder',
        "text": 'Two identical plants both show net uptake, but one behind dimming glass shows a smaller positive number than the other. Explain this without an exact light measurement.',
        "options": [
            {"text": "The dimmed plant's respiration must have risen, reducing its net figure below the other plant's, under all the circumstances described here.", "correct": False,
             "why": 'Respiration stays flat regardless of light in this model — the smaller net figure comes entirely from reduced photosynthesis.'},
            {"text": 'Less light reaching the dimmed plant lowers its photosynthesis; since respiration is unaffected, its net figure is smaller but still positive.', "correct": True},
            {"text": 'Dimming glass must be adding extra carbon dioxide to the enclosed air around that plant.', "correct": False,
             "why": 'Nothing about dimming glass is described as adding gas — it simply reduces the light reaching the plant.'},
            {"text": 'The two plants cannot really be identical if their readings differ at all.', "correct": False,
             "why": 'Identical plants under different light levels are expected to give different readings, since photosynthesis depends on light.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h27',
        "band": 'harder',
        "text": "Doubling the light from a very low starting point produces a bigger jump in net uptake near dawn (the curve's steep part) than doubling it near bright noon (the flat part). Explain why, without needing the curve's equation.",
        "options": [
            {"text": "Respiration is lower near dawn, which makes any doubling of light appear to have a bigger effect, by this lesson's own reasoning about the two rates.", "correct": False,
             "why": 'Respiration is flat at every light level in this model — it does not vary between dawn and noon.'},
            {"text": 'Doubling light near bright noon actually produces the bigger jump, not doubling it near dawn, under every circumstance the curve in this lesson describes.', "correct": False,
             "why": 'The flat part of the curve, near bright noon, is exactly where a doubling produces the SMALLEST change.'},
            {"text": 'The curve rises steeply near dawn, so a given change in light produces a much bigger change in photosynthesis there than on the flat part.', "correct": True},
            {"text": "The bench's sensor is simply less accurate at low light levels such as dawn, according to this exact model's own readings.", "correct": False,
             "why": "Sensor accuracy is not described as varying with light — the bigger jump comes from the curve's own steepness near dawn."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h28',
        "band": 'harder',
        "text": 'A pupil claims the compensation point must sit exactly halfway between darkness and bright noon on the light scale. Using the actual dawn value of 8, against a scale running to 100, evaluate this.',
        "options": [
            {"text": 'True — 8 units is roughly half of the scale once the units are properly accounted for.', "correct": False,
             "why": '8 is not close to half of 100 by any reasonable reading of the scale — it sits near the dark end.'},
            {"text": 'True, since compensation points are always found exactly halfway up any light scale used.', "correct": False,
             "why": "This bench's own dawn value, 8 out of 100, directly contradicts a halfway claim."},
            {"text": 'It cannot be evaluated without converting the scale into real, measured light units first.', "correct": False,
             "why": "Comparing 8 with 50 on the bench's own stated scale is already enough to judge the claim."},
            {"text": 'False — 8 sits nowhere near halfway (50); plants can balance at quite low light levels.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h29',
        "band": 'harder',
        "text": 'A student wants to calculate how much sugar (glucose) a plant makes per day, using only this bench. Explain why this cannot be done directly from what the bench measures.',
        "options": [
            {"text": 'The bench measures carbon dioxide movement, not glucose, and converting between the two needs chemistry the model does not provide.', "correct": True},
            {"text": 'It can be done directly, since carbon dioxide readings and glucose amounts are treated as the exact same quantity, plainly and simply.', "correct": False,
             "why": 'A gas reading and an amount of sugar are different quantities — converting between them needs chemistry not covered here.'},
            {"text": 'It cannot be done because the bench never measures anything about carbon dioxide at all.', "correct": False,
             "why": 'Carbon dioxide movement is exactly what the bench measures — the missing piece is the chemistry linking gas to sugar.'},
            {"text": 'It cannot be done because glucose is only produced by animals, never by plants.', "correct": False,
             "why": 'Glucose is a product of photosynthesis in plants — the barrier here is missing chemistry, not biology.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h30',
        "band": 'harder',
        "text": 'Evaluate: “Net CO2 movement passes smoothly through every value as light changes, rather than jumping between three fixed modes of positive, negative and zero.”',
        "options": [
            {"text": 'Flawed — a leaf only ever sits in one of exactly three fixed states at any given moment, without any exception.', "correct": False,
             "why": "The net reading moves through a continuous range of values, not three separate fixed states."},
            {"text": 'Sound — net movement is continuous, moving smoothly through all values as light changes, not jumping between three fixed modes.', "correct": True},
            {"text": 'Flawed, since positive, negative and zero are the only mathematical categories a number can belong to.', "correct": False,
             "why": 'That is true of the sign of a number, but the actual VALUE still changes continuously within each category.'},
            {"text": "It cannot be evaluated without watching a real living plant, rather than only a simplified model.", "correct": False,
             "why": "A smoothly rising and levelling photosynthesis curve is enough to judge this claim."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h31',
        "band": 'harder',
        "text": 'A pupil argues that because closing stomata stops photosynthesis, it must also stop respiration, since both happen in the same leaf. Evaluate this.',
        "options": [
            {"text": 'Sound — anything that stops one chemical process in a leaf must stop every other one too.', "correct": False,
             "why": 'This lesson treats the two processes as independent — one depends on stomata being open, the other does not.'},
            {"text": 'Sound, since both processes are described as needing exactly the same gas supplied through the same stomata in light.', "correct": False,
             "why": 'Respiration is described as continuing throughout the states on this bench, including when net movement is entirely release, not uptake.'},
            {"text": 'Flawed — respiration runs continuously regardless of light or stomata state, unlike photosynthesis.', "correct": True},
            {"text": 'It cannot be evaluated, since this lesson never actually describes what closing stomata does.', "correct": False,
             "why": 'This lesson is explicit that closing stomata stops carbon dioxide entering, which is exactly what starves photosynthesis, not respiration.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-05-h32',
        "band": 'harder',
        "text": "A scientist studying a forest's total CO2 absorption cannot just measure one leaf once and multiply by the number of leaves. Name TWO separate reasons why not.",
        "options": [
            {"text": 'Forests contain too many leaves to count accurately, and leaves are different shapes from each other.', "correct": False,
             "why": "Counting difficulty and leaf shape are not reasons drawn from this lesson's own model of gas exchange."},
            {"text": 'Leaves cannot photosynthesise at all once removed from the tree, and CO2 sensors are never able to work outdoors in bright natural daylight.', "correct": False,
             "why": 'Neither claim appears in this lesson — the real reasons concern how a single reading varies and what it can and cannot tell you.'},
            {"text": 'Only the reasons already given for asthma and smoking in a completely different lesson apply here.', "correct": False,
             "why": "This lesson supplies its own reasons directly, about light-dependence and single-reading ambiguity, without needing another lesson's content."},
            {"text": 'Net movement varies continuously with light across the day and between leaves; and a single reading cannot say where a leaf sits without also knowing the light level.', "correct": True},
        ],
        "figure": None,
    },
]
