"""B4 lesson 03 — Alveoli: built for exchange: twelve questions (MRB-269).

The lesson makes one argument twice: an exchange surface is judged on area,
distance, concentration difference and moisture, and diffusion across it runs
in both directions all the time. The bank probes both halves. The easier band
checks the physical picture a student must hold — two cell layers between air
and blood, what the film of liquid is for, what a capillary actually is, and
how big seventy square metres is against six litres. The standard band puts
that picture to work on the situations the page already drew: the tank claim,
the two crossing counts and the difference between them, why a villus needs one
flow and an alveolus needs two, and whether any of it costs energy. The harder
band takes the four requirements somewhere the lesson never went — a lung
losing surface without losing volume, alveoli part-filled with fluid, carbon
dioxide going the other way across the same wall, and a fish gill.

All three declared misconceptions supply distractors throughout. BREATH-06
("oxygen is pumped across into the blood") drives the alveolar-cells-spend-
energy option in s04, the breathing-pushes-molecules option in s04, and the
oxygen-pushes-carbon-dioxide-out option in h03. BREATH-07 ("oxygen moves in
because it wants to spread out evenly") drives the gain-starts-when-they-are-
equal option in s02 and the gases-even-themselves-out option in h03. BREATH-08
("alveoli are where the air is stored") drives both "nothing is wrong" and
"the store is in the bronchi" in s01, the storage option in e02, and the
volume-in-litres option in e04. Three further errors the lesson exists to
correct supply the rest: that blood touches the air directly (e01, e03), that
volume and surface are the same measure (e04, h01), and that more moisture must
mean more exchange (h02).

`figure` is None throughout: this lesson declares no figures.
"""

UNIT = "B4"
LESSON = "alveoli-built-for-exchange"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-03-e01",
        "band": "easier",
        "text": "An oxygen molecule leaves the air inside an alveolus and ends "
                "up in the blood. How many cell layers does it cross on the "
                "way?",
        "options": [
            {"text": "One — the alveolus wall, with blood pressed straight "
                     "against it.",
             "correct": False,
             "why": "The capillary has a wall of its own, also one cell thick. "
                    "Two walls of one cell each is why the distance is so "
                    "short — but it is not one, and it is never zero."},
            {"text": "Two — the alveolus wall and the capillary wall, one cell "
                     "each.",
             "correct": True},
            {"text": "None — oxygen crosses a gap between the alveolus and the "
                     "blood.",
             "correct": False,
             "why": "There is no gap. If air met blood directly you would have "
                    "an air bubble in a blood vessel, which is fatal. Oxygen "
                    "dissolves and crosses through two living cell layers."},
            {"text": "Four — two layers of cells on each side of the exchange "
                     "surface.",
             "correct": False,
             "why": "Each wall is a single cell thick, not two. That "
                    "one-cell thinness is one of the four features that make "
                    "an alveolus work at all."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e02",
        "band": "easier",
        "text": "A film of liquid lines the inside of every alveolus. What is "
                "that film there for?",
        "options": [
            {"text": "Gases dissolve in it before they cross the alveolus "
                     "wall.",
             "correct": True},
            {"text": "It traps dust and germs before they can reach the "
                     "blood.",
             "correct": False,
             "why": "Mucus higher up the airway does that job. The film in an "
                    "alveolus is listed as one of the four requirements for "
                    "exchange itself — gases must go into solution before they "
                    "can diffuse across."},
            {"text": "It stops the thin alveolus walls from drying out and "
                     "dying.",
             "correct": False,
             "why": "It is easy to assume the liquid is there to protect the "
                    "cells. A moist surface is on the list because dissolved "
                    "gas is what crosses — that is the job it is doing here."},
            {"text": "It stores the oxygen until the blood is ready to take "
                     "it.",
             "correct": False,
             "why": "Nothing is stored anywhere in an alveolus. The film is a "
                    "few molecules deep and gases pass straight through it "
                    "into the capillary."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e03",
        "band": "easier",
        "text": "A dense network of capillaries runs over every alveolus. What "
                "is a capillary?",
        "options": [
            {"text": "A muscle that squeezes blood past the outside of the "
                     "alveolus.",
             "correct": False,
             "why": "Nothing here is squeezed or driven. A capillary is a "
                    "vessel, and the heart is what moves blood through it."},
            {"text": "A gap in the alveolus wall that lets blood reach the "
                     "air.",
             "correct": False,
             "why": "Blood never touches air. It stays inside a vessel that "
                    "has a wall of its own, and oxygen crosses both walls — "
                    "that is the two-cell distance."},
            {"text": "The smallest blood vessel, with a wall just one cell "
                     "thick.",
             "correct": True},
            {"text": "A small air tube carrying air down into the alveolus "
                     "itself.",
             "correct": False,
             "why": "That describes a bronchiole, which is part of the airway. "
                    "A capillary carries blood — it is the blood side of the "
                    "exchange surface, not the air side."},
        ],
        "figure": None,
    },
    # ⊕ MRB-233 (3c) SWEEP, 31 Aug 2026 — REWRITTEN, AND FOUND BY THE SWEEP
    # RATHER THAN BY THE RULING. Mide's B3 ruling was about the small
    # intestine; this question is about alveoli and sits in another unit. It
    # was caught because it did BOTH of the things the sweep forbids — it
    # marked a specific number as the answer ("About 70 m², packed inside a
    # chest of only six litres"), and it reached for a tennis court to size it
    # ("Seventy square metres is closer to a third of a tennis court than to a
    # page"). A third option cross-referenced the gut's 30 m².
    #
    # ⚠️ 70 m² IS NOT WRONG AND HAS NOT BEEN "ALIGNED TO 30 m²". The gut's
    # figure belongs to the gut. What changed is that the alveolar area is no
    # longer the thing being MARKED — the question now tests the principle,
    # which is what the sweep asks for where ~30 m² cannot apply.
    #
    # ⚠️ Deliberately NOT "why millions of small alveoli rather than one large
    # cavity" — that is this lesson's RUNG 1, and `h01` (emphysema) already
    # takes it at the harder band. What is left, and what the original
    # question's own distractors were built around, is the SURFACE/VOLUME swap:
    # the note on the old option called six litres "the swap the hook is built
    # to catch". That swap is now the whole question.
    {
        "id": "b4-03-e04",
        "band": "easier",
        "text": "Asked how much gas exchange surface the alveoli give, a "
                "student answers “about six litres”. What is wrong with that "
                "answer?",
        "options": [
            {"text": "Nothing is wrong — six litres is the usual figure "
                     "quoted for the alveoli.",
             "correct": False,
             "why": "Six litres is roughly the volume of air the chest can "
                    "hold, so it is a real figure about the lungs — but it "
                    "answers a different question from the one asked."},
            {"text": "The figure is far too small; the lungs hold a great "
                     "deal more air than six litres.",
             "correct": False,
             "why": "The size of the number is not the problem here. Whatever "
                    "number went in front of it, litres measure a volume and "
                    "the question asked for a surface."},
            {"text": "It should have been measured after a deep breath in, "
                     "rather than during quiet breathing.",
             "correct": False,
             "why": "When it was measured does not change WHAT was measured. "
                    "A volume taken at any moment of the breath is still a "
                    "volume, and still not an area."},
            {"text": "It gives a volume, not a surface — the two are "
                     "different quantities.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-03-s01",
        "band": "standard",
        "text": "“The alveoli are where your body keeps its store of "
                "air.” What is wrong with this statement?",
        "options": [
            {"text": "Nothing — holding a store of air is exactly what "
                     "alveoli do.",
             "correct": False,
             "why": "This is the idea the lesson exists to remove. An alveolus "
                    "is a surface being refreshed on one side and drained on "
                    "the other, not a container."},
            {"text": "Nothing is stored — alveolar air is partly replaced "
                     "about twelve times a minute.",
             "correct": True},
            {"text": "The store is real, but it sits in the bronchi rather "
                     "than in the alveoli.",
             "correct": False,
             "why": "Moving the store further up the airway keeps the wrong "
                    "idea. No part of the lungs holds a reserve — about half a "
                    "litre goes in and out with each quiet breath."},
            {"text": "Air is stored there, but only the oxygen — carbon "
                     "dioxide leaves at once.",
             "correct": False,
             "why": "Both gases are crossing all the time, in opposite "
                    "directions across the same wall. Neither one is held and "
                    "neither one waits."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s02",
        "band": "standard",
        "text": "With both flows running, the bench counts 1197 oxygen "
                "molecules crossing into the blood each second and 477 "
                "crossing out of it. How much oxygen does the body gain each "
                "second?",
        "options": [
            {"text": "1197 — the outward crossings come back, so they do not "
                     "count.",
             "correct": False,
             "why": "They do count, and they count against you. Every outward "
                    "crossing is oxygen leaving the blood, so the gain is what "
                    "is left after you subtract them."},
            {"text": "1674 — the two counts add together to give the total "
                     "movement.",
             "correct": False,
             "why": "Adding treats the outward crossings as a gain when they "
                    "are a loss. Net movement is the difference between the "
                    "two counts, never their sum."},
            {"text": "720 — the difference between the number crossing each "
                     "way.",
             "correct": True},
            {"text": "None yet — the gain starts once the two counts have "
                     "become equal.",
             "correct": False,
             "why": "Equal counts is precisely the state where the gain is "
                    "zero. Nothing is waiting to finish evening out; the "
                    "imbalance is the only thing that was ever doing "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s03",
        "band": "standard",
        "text": "In the small intestine, one flow — the blood — is enough to "
                "keep the concentration difference open. At an alveolus it "
                "takes two, blood flow and breathing. Why does the lung need "
                "both?",
        "options": [
            {"text": "Because the lungs are far larger, and one flow could "
                     "never reach all of that surface.",
             "correct": False,
             "why": "Size is not the reason. The gut's 30 m² is the same "
                    "problem on the same scale — what differs is that gas has "
                    "to travel in both directions."},
            {"text": "Because gases diffuse faster than dissolved food, so "
                     "they need a stronger push across.",
             "correct": False,
             "why": "Nothing is pushed in either organ. Diffusion is not "
                    "driven by force, and a faster-moving gas would need less "
                    "help, not more."},
            {"text": "Because blood moves more slowly through the lungs than "
                     "it does through the gut wall.",
             "correct": False,
             "why": "Blood speed is not what the second flow is for. Breathing "
                    "keeps the air side high while blood flow keeps the blood "
                    "side low."},
            {"text": "Because gas travels both ways, so both sides have to be "
                     "kept refreshed at once.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s04",
        "band": "standard",
        "text": "Which statement about the energy needed to move oxygen from "
                "an alveolus into the blood is correct?",
        "options": [
            {"text": "None is needed — the molecules' own random motion "
                     "carries them across.",
             "correct": True},
            {"text": "Cells in the alveolus wall spend energy moving each "
                     "oxygen molecule across.",
             "correct": False,
             "why": "This is the pump idea, and there is no pump in an "
                    "alveolus — no channel that grabs oxygen and nothing that "
                    "spends energy on it. Diffusion costs nothing."},
            {"text": "Breathing supplies it, pushing oxygen molecules through "
                     "the alveolus wall.",
             "correct": False,
             "why": "Breathing refreshes the air in the alveolus; it does not "
                    "push individual molecules through a wall. It holds the "
                    "concentration difference open, and the difference does "
                    "the rest."},
            {"text": "None is needed, because the wall is only two cells thick "
                     "in total.",
             "correct": False,
             "why": "The right answer for the wrong reason. Thinness shortens "
                    "the journey, but even a thick wall would need no energy — "
                    "diffusion never does."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-03-h01",
        "band": "harder",
        "text": "In emphysema the walls between neighbouring alveoli break "
                "down, so groups of alveoli merge into fewer, larger spaces. "
                "The volume of air the lungs hold does not fall — it often "
                "rises. Why does the patient still become breathless?",
        "options": [
            {"text": "The walls that remain grow thicker, so oxygen has "
                     "further to travel across.",
             "correct": False,
             "why": "Thickening happens in other lung diseases, not this one. "
                    "Here the walls are lost rather than thickened — what has "
                    "gone is surface, not thinness."},
            {"text": "The lungs now hold more air than the blood is able to "
                     "carry away from them.",
             "correct": False,
             "why": "There is no backlog and no queue. The blood takes oxygen "
                    "from whatever surface is available, and with less surface "
                    "less crosses."},
            {"text": "Much of the exchange surface has gone, and extra volume "
                     "cannot replace surface.",
             "correct": True},
            {"text": "Breathing faster would fix it, so the breathlessness "
                     "must have some other cause.",
             "correct": False,
             "why": "Breathing faster refreshes the air, but refreshed air is "
                    "useless where there is no surface for it to cross. The "
                    "limit here is area, not supply."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h02",
        "band": "harder",
        "text": "In some heart conditions, fluid leaks out of the capillaries "
                "and part-fills the alveoli. A student says this should help, "
                "because the lesson says the exchange surface must be moist. "
                "What actually happens?",
        "options": [
            {"text": "Exchange slows, because oxygen must cross a layer of "
                     "fluid as well.",
             "correct": True},
            {"text": "Exchange improves, because more moisture lets more "
                     "oxygen dissolve and cross.",
             "correct": False,
             "why": "A film a few molecules deep is all that is needed for a "
                    "gas to dissolve. Past that, more liquid only adds "
                    "distance — and requirement 2 is a short distance."},
            {"text": "Exchange stops completely, because oxygen simply cannot "
                     "pass through liquid at all.",
             "correct": False,
             "why": "Oxygen crosses liquid every time you breathe — the moist "
                    "lining and the blood are both liquid. Fluid makes the "
                    "journey longer, not impossible."},
            {"text": "Nothing changes, because oxygen dissolves in the moist "
                     "lining either way.",
             "correct": False,
             "why": "It does dissolve either way, but it then has much further "
                    "to diffuse. A short diffusion distance is one of the four "
                    "requirements, and the fluid is destroying it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h03",
        "band": "harder",
        "text": "Carbon dioxide crosses the same wall in the opposite "
                "direction. Applying the same rule you used for oxygen, what "
                "must be true for that to happen?",
        "options": [
            {"text": "The oxygen crossing inwards pushes the carbon dioxide "
                     "out the other way.",
             "correct": False,
             "why": "The two gases take no notice of each other. Each one "
                    "follows its own concentration difference, across the same "
                    "wall, at the same moment."},
            {"text": "Carbon dioxide waits until the oxygen has finished "
                     "crossing, then leaves.",
             "correct": False,
             "why": "There is no queue and nothing finishes. Both gases are "
                    "crossing continuously, in opposite directions, through "
                    "the same two cell layers."},
            {"text": "Gases even themselves out between two spaces, so it "
                     "leaves on its own.",
             "correct": False,
             "why": "Nothing is trying to even out. Carbon dioxide leaves only "
                    "because there is more of it in the blood than in the "
                    "alveolar air — no aim is involved anywhere."},
            {"text": "The blood arriving carries more carbon dioxide than the "
                     "alveolar air holds.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h04",
        "band": "harder",
        "text": "A fish gill is a stack of very thin filaments with blood "
                "flowing inside them and water flowing over the outside. Which "
                "of the four requirements is the flow of water meeting?",
        "options": [
            {"text": "Requirement 1 — the moving water adds to the gill's "
                     "total surface area.",
             "correct": False,
             "why": "The surface comes from the filaments themselves. Moving "
                    "water past a surface does not create more of it, any more "
                    "than breathing creates more alveoli."},
            {"text": "Requirement 3 — flowing water keeps the concentration "
                     "difference steep and open.",
             "correct": True},
            {"text": "Requirement 2 — the flow presses the filaments thinner, "
                     "shortening the crossing.",
             "correct": False,
             "why": "The thinness is built into the gill, exactly as the "
                    "one-cell alveolus wall is built into a lung. A flow of "
                    "water does not change how thick a wall is."},
            {"text": "Requirement 4 — the flow supplies the water that the "
                     "oxygen dissolves in.",
             "correct": False,
             "why": "The gill would be wet whether the water moved or not. "
                    "What the movement adds is fresh oxygen on the outside, "
                    "and that is requirement 3."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-03-e05",
        "band": "easier",
        "text": "What does the word diffusion mean?",
        "options": [
            {"text": "Particles being pushed from a crowded place towards "
                     "an emptier one by some kind of force on them.",
             "correct": False,
             "why": "Nothing pushes and no force is involved. The particles "
                    "were already moving randomly, and the movement is simply "
                    "unbalanced when one side is more crowded."},
            {"text": "Net movement of particles from a crowded place to a "
                     "less crowded one, by random motion.",
             "correct": True},
            {"text": "Particles moving in one direction only, and stopping "
                     "altogether once the two sides hold the same amount of "
                     "gas.",
             "correct": False,
             "why": "They cross in both directions the whole time. Only the "
                    "difference between the two counts is the net movement, "
                    "and that never means one-way traffic."},
            {"text": "Gases dissolving into a liquid so that they can then be "
                     "carried away in it.",
             "correct": False,
             "why": "Dissolving is what the moist lining allows, and it "
                    "happens before the crossing. Diffusion is the movement "
                    "itself."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e06",
        "band": "easier",
        "text": "Three of these are requirements for a good gas exchange "
                "surface. Which one is not?",
        "options": [
            {"text": "A large surface area.", "correct": False,
             "why": "This is the first requirement, and it is why there are "
                    "hundreds of millions of alveoli rather than one cavity."},
            {"text": "A short distance for the gas to cross.", "correct": False,
             "why": "This is the second requirement. It is why the alveolus "
                    "wall and the capillary wall are each a single cell "
                    "thick."},
            {"text": "A concentration difference that is kept open.",
             "correct": False,
             "why": "This is the third requirement, and it is what breathing "
                    "and blood flow exist to maintain."},
            {"text": "A thick protective outer layer over the surface.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e07",
        "band": "easier",
        "text": "Which of these changes to an alveolus would make gas "
                "exchange slower?",
        "options": [
            {"text": "Its wall becoming several cells thick instead of one.",
             "correct": True},
            {"text": "More capillaries running over its surface.",
             "correct": False,
             "why": "More capillaries drain the blood side faster, so the "
                    "concentration difference is kept steeper. That speeds "
                    "exchange up."},
            {"text": "A steeper difference in oxygen between the air and the "
                     "blood.",
             "correct": False,
             "why": "A steeper difference is the third requirement working "
                    "well. The bigger the difference, the more net crossings "
                    "there are each second."},
            {"text": "A thin film of liquid lining its inside surface.",
             "correct": False,
             "why": "That film is the fourth requirement, not a problem. Gases "
                    "have to dissolve before they can cross."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e08",
        "band": "easier",
        "text": "In which direction does oxygen cross the alveolus wall, and "
                "what makes it go that way?",
        "options": [
            {"text": "From the blood into the air, because the blood "
                     "arriving is under much greater pressure than the air "
                     "is.",
             "correct": False,
             "why": "Blood pressure does not move gases across a wall, and the "
                    "direction is the other way. Blood arriving at the lungs "
                    "is low in oxygen."},
            {"text": "From the air into the blood, because the wall only "
                     "opens one way.",
             "correct": False,
             "why": "The direction is right and the reason is not. Nothing "
                    "opens or closes — molecules cross both ways all the time, "
                    "and the imbalance decides the net result."},
            {"text": "From the air into the blood, because the air holds "
                     "more oxygen than the blood.",
             "correct": True},
            {"text": "From the air into the blood, because the cells lining "
                     "the wall carry it across for the body.",
             "correct": False,
             "why": "The direction is right, but no cell carries anything. "
                    "There is no pump in an alveolus and nothing spends energy "
                    "on the crossing."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e09",
        "band": "easier",
        "text": "Molecules cross an exchange surface in both directions at "
                "once. What does net movement mean?",
        "options": [
            {"text": "The total of the crossings in both directions, added "
                     "together into one figure.",
             "correct": False,
             "why": "Adding them treats the outward crossings as a gain, when "
                    "they are the opposite of one. The two counts have to be "
                    "subtracted."},
            {"text": "What is left after the crossings each way are subtracted "
                     "from each other.",
             "correct": True},
            {"text": "The crossings in the direction the body wants, ignoring "
                     "the rest.",
             "correct": False,
             "why": "The crossings the other way are real and they count "
                    "against the total. Ignoring them would give a figure much "
                    "larger than the body actually gains."},
            {"text": "The number of molecules left on the side they started "
                     "on.",
             "correct": False,
             "why": "Net movement is about what has moved, not about what "
                    "stayed. It is the difference between the two crossing "
                    "counts."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e10",
        "band": "easier",
        "text": "Which other organ meets the same four requirements for a "
                "good exchange surface as the lungs do?",
        "options": [
            {"text": "The heart, where blood is pumped past a very large "
                     "inner surface every minute.",
             "correct": False,
             "why": "The heart moves blood; it exchanges nothing across a "
                    "surface. Being large and having blood in it is not the "
                    "same as being an exchange surface."},
            {"text": "The trachea, which is long and lined all the way down.",
             "correct": False,
             "why": "The trachea is a transport tube. Nothing crosses into the "
                    "blood there, whatever its lining is like."},
            {"text": "The brain, which uses up more oxygen every minute "
                     "than any other organ in the whole body.",
             "correct": False,
             "why": "Using a great deal of oxygen is not the same as absorbing "
                    "it from outside the body. The organ compared with the "
                    "lungs here is the one that absorbs food."},
            {"text": "The small intestine, whose villi absorb digested food "
                     "from the gut.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-03-s05",
        "band": "standard",
        "text": "Blood arriving at the lungs has just come back from the "
                "body's tissues. What must be true of its oxygen level, and "
                "why does that matter?",
        "options": [
            {"text": "It must be lower than the alveolar air's, which is what "
                     "makes oxygen cross into it.",
             "correct": True},
            {"text": "It must be higher than the alveolar air's, so that "
                     "carbon dioxide can be swapped for oxygen.",
             "correct": False,
             "why": "Blood coming back from the tissues has given much of its "
                    "oxygen away, so it is the low side. Nothing is swapped "
                    "one-for-one either — each gas follows its own "
                    "difference."},
            {"text": "It must be the same as the alveolar air's, so that the "
                     "two sides are balanced.",
             "correct": False,
             "why": "Equal levels is precisely the state in which net "
                    "absorption falls to zero. A difference is what makes the "
                    "exchange happen."},
            {"text": "It must be zero, because the tissues take all of the "
                     "oxygen the blood carries.",
             "correct": False,
             "why": "The tissues take a share, never all of it. Blood "
                    "returning to the lungs still carries oxygen — it is "
                    "simply lower than the air in the alveoli."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s06",
        "band": "standard",
        "text": "Blood flow past the alveoli is stopped while breathing "
                "continues normally. The air on the alveolar side is as fresh "
                "as ever. Why does net absorption still collapse?",
        "options": [
            {"text": "Because the alveolar air stops being refreshed as "
                     "soon as the blood behind the wall stops moving.",
             "correct": False,
             "why": "Breathing has not stopped, so the air is still being "
                    "replaced about twelve times a minute. It is the other "
                    "side of the wall that has changed."},
            {"text": "Because oxygen cannot cross into blood that is not "
                     "moving.",
             "correct": False,
             "why": "It crosses perfectly well into still blood — for a while. "
                    "What stops is the draining away of what has crossed."},
            {"text": "Because the blood side fills with oxygen until both "
                     "sides nearly match.",
             "correct": True},
            {"text": "Because the wall itself gets thicker as soon as there "
                     "is no blood flowing behind it.",
             "correct": False,
             "why": "The wall is unchanged, and so are the surface area and "
                    "the moist lining. The only thing lost is the difference "
                    "across it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s07",
        "band": "standard",
        "text": "A student writes that the alveoli “take the oxygen out of "
                "the air and put it into the blood”. What is the best "
                "correction?",
        "options": [
            {"text": "The capillaries take it out; the alveoli only hold "
                     "the air still while they do.",
             "correct": False,
             "why": "This moves the taking rather than removing it. No "
                    "structure on either side takes anything — the molecules "
                    "cross on their own."},
            {"text": "The alveoli take nothing: oxygen crosses on its own, "
                     "because the air holds more than blood.",
             "correct": True},
            {"text": "The alveoli do take it out, but only when the body "
                     "actually needs it, which is why exercise speeds the "
                     "whole thing up.",
             "correct": False,
             "why": "Nothing in an alveolus decides when to act. Exercise "
                    "speeds exchange up by keeping the difference steeper, not "
                    "by switching anything on."},
            {"text": "The alveoli put oxygen into the blood, but the blood "
                     "has to be moving fast enough for them to manage it.",
             "correct": False,
             "why": "Blood flow matters, but it matters because it keeps the "
                    "blood side low. The alveoli still put nothing anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s08",
        "band": "standard",
        "text": "At a particular moment, 640 oxygen molecules a second cross "
                "into the blood and 640 a second cross out of it. What can "
                "you say about this surface?",
        "options": [
            {"text": "Nothing is crossing it in either direction any more.",
             "correct": False,
             "why": "Six hundred and forty crossings a second in each "
                    "direction is a great deal of movement. What has gone is "
                    "the imbalance, not the traffic."},
            {"text": "Oxygen is about to start moving the other way "
                     "instead, out of the blood and back into the alveolus.",
             "correct": False,
             "why": "Nothing is about to happen. Equal counts stay equal "
                    "unless something changes one side, and neither side is "
                    "favoured at this moment."},
            {"text": "The molecules have finished spreading out and have "
                     "now come to rest on both sides.",
             "correct": False,
             "why": "They are moving at hundreds of metres a second and "
                    "crossing constantly. Nothing has finished, and nothing "
                    "was ever trying to finish."},
            {"text": "The body gains no oxygen here, though molecules still "
                     "cross constantly.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s09",
        "band": "standard",
        "text": "A student says surface area is all that matters, so doubling "
                "the number of alveoli would double gas exchange even if the "
                "blood flow were halved. What is wrong with that?",
        "options": [
            {"text": "Slower blood flow lets the blood side rise, so the "
                     "concentration difference shrinks.",
             "correct": True},
            {"text": "Extra alveoli would have thicker walls, so each one "
                     "would work less well.",
             "correct": False,
             "why": "There is no reason for the walls to change. The problem "
                    "is on the blood side of the wall, not in the wall "
                    "itself."},
            {"text": "Nothing is wrong — surface area is the first thing an "
                     "exchange surface needs, so it is the one that counts.",
             "correct": False,
             "why": "Being the most obvious need does not make it the only one. "
                    "A huge surface with no difference across it exchanges "
                    "nothing at all."},
            {"text": "Doubling the alveoli would halve the moist lining, so "
                     "less oxygen could dissolve.",
             "correct": False,
             "why": "Every alveolus is lined, however many there are. The "
                    "requirement that suffers when the blood slows is the "
                    "maintained concentration difference."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s10",
        "band": "standard",
        "text": "During exercise the heart pumps blood past the alveoli much "
                "faster. What does that achieve for gas exchange?",
        "options": [
            {"text": "It increases the surface area available, because more "
                     "capillaries open up.",
             "correct": False,
             "why": "The surface belongs to the alveoli and does not change "
                    "when the blood speeds up. What changes is how quickly "
                    "absorbed oxygen is taken away."},
            {"text": "It shortens the diffusion distance, because the "
                     "faster blood presses in closer against the wall.",
             "correct": False,
             "why": "The distance is two cell walls, and pressing harder does "
                    "not change it. Faster flow works on the third "
                    "requirement, not the second."},
            {"text": "It carries oxygen away sooner, so the blood side "
                     "stays low and the difference steep.",
             "correct": True},
            {"text": "It gives each molecule of oxygen more energy of its "
                     "own, so that it crosses the thin wall much more "
                     "easily.",
             "correct": False,
             "why": "Crossing needs no energy at any speed, and nothing gives "
                    "a molecule any. Faster flow simply keeps one side of the "
                    "wall emptier."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-03-h05",
        "band": "harder",
        "text": "A patient is given air enriched to 40% oxygen through a "
                "mask. Predict what happens to net oxygen absorption at the "
                "alveoli, and why.",
        "options": [
            {"text": "It stays the same, because the wall can only let a "
                     "fixed amount of gas through in each second.",
             "correct": False,
             "why": "The wall sets no quota. How much crosses depends on the "
                    "difference across it, and that difference has just been "
                    "made bigger."},
            {"text": "It rises, because the air side is now higher and the "
                     "difference is bigger.",
             "correct": True},
            {"text": "It rises, because the extra oxygen pushes harder on "
                     "the wall.",
             "correct": False,
             "why": "The prediction is right and the reason is not. Nothing is "
                    "pushed across — more crossings simply happen inwards than "
                    "outwards when one side holds more."},
            {"text": "It falls, because the blood cannot cope with that "
                     "much oxygen arriving all at once.",
             "correct": False,
             "why": "Diffusion does not slow down because the far side is "
                    "busy. As long as the blood side stays lower than the air "
                    "side, oxygen keeps crossing inwards."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h06",
        "band": "harder",
        "text": "A single-celled organism has no lungs, no blood and no "
                "exchange surface of any kind, yet it gets all the oxygen it "
                "needs. Explain why that works for it and not for you.",
        "options": [
            {"text": "It needs no oxygen at all, so there is nothing for it "
                     "to exchange.",
             "correct": False,
             "why": "It respires like everything else alive, so it needs "
                    "oxygen. The question is how the oxygen reaches the inside "
                    "of it."},
            {"text": "Its cell can pump oxygen inwards, which the cells in your "
                     "body cannot do.",
             "correct": False,
             "why": "No cell pumps oxygen anywhere — diffusion is the only "
                    "mechanism, in a single cell and in you. What differs is "
                    "the distance involved."},
            {"text": "The water around it carries the oxygen inside, so no "
                     "diffusion is needed.",
             "correct": False,
             "why": "Oxygen still has to cross the cell surface, and it does "
                    "so by diffusion. Being surrounded by water does not move "
                    "anything into a cell."},
            {"text": "Every part of it is close to its surface, so diffusion "
                     "alone is fast enough.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h07",
        "band": "harder",
        "text": "In a very premature baby, the film of liquid lining the "
                "alveoli pulls their walls together so that they tend to "
                "stick shut. Which feature of a good exchange surface is "
                "causing the trouble?",
        "options": [
            {"text": "The moist surface — the same feature that lets gases "
                     "dissolve is what pulls the walls together.",
             "correct": True},
            {"text": "The short diffusion distance — walls that thin are too "
                     "weak to stay apart.",
             "correct": False,
             "why": "Thinness is not what closes them; a wet surface pulling "
                    "on itself is. A thin dry surface would not stick in the "
                    "same way."},
            {"text": "The large surface area — there is simply too much of it "
                     "for a small chest to hold open.",
             "correct": False,
             "why": "Adults have far more surface still and no such problem. "
                    "The difficulty comes from the liquid film, not from the "
                    "amount of surface."},
            {"text": "The concentration difference — with no air arriving "
                     "there is nothing to hold the alveoli open.",
             "correct": False,
             "why": "A concentration difference has no mechanical effect at "
                    "all; it cannot hold anything open. The feature at fault "
                    "is the moist lining."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h08",
        "band": "harder",
        "text": "An exchange surface is transferring 700 oxygen molecules a "
                "second, net. The concentration difference across it is then "
                "doubled and nothing else is changed. Roughly what net "
                "transfer would you expect?",
        "options": [
            {"text": "About 350 molecules a second.", "correct": False,
             "why": "This halves the transfer instead of doubling it. A bigger "
                    "difference makes more crossings happen inwards, not "
                    "fewer."},
            {"text": "Still about 700 molecules a second.", "correct": False,
             "why": "That would mean the difference across a surface makes no "
                    "odds, which is the opposite of the third requirement. "
                    "Diffusion follows the difference."},
            {"text": "About 1400 molecules a second.", "correct": True},
            {"text": "About 702 molecules a second.", "correct": False,
             "why": "This adds the two rather than scaling with the "
                    "difference. Doubling the difference roughly doubles the "
                    "net transfer."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h09",
        "band": "harder",
        "text": "Someone's lungs are entirely healthy, but their blood can "
                "carry only half as much oxygen as usual. Explain why gas "
                "exchange at the alveoli becomes less effective.",
        "options": [
            {"text": "The alveolar walls thicken to compensate, so every "
                     "crossing takes longer than before.",
             "correct": False,
             "why": "Nothing thickens, and the lungs are stated to be healthy. "
                    "The change is entirely on the blood side of a wall that "
                    "has not altered."},
            {"text": "The blood side rises towards the air side sooner, so "
                     "the difference closes.",
             "correct": True},
            {"text": "Diffusion needs energy from the blood, and there is "
                     "less of it.",
             "correct": False,
             "why": "Diffusion needs no energy from anywhere. What the blood "
                    "supplies is somewhere for the oxygen to go, and there is "
                    "now less of that."},
            {"text": "The surface area falls, because fewer alveoli are "
                     "used when the blood is able to carry less oxygen.",
             "correct": False,
             "why": "The alveoli are all still there and all still lined with "
                    "capillaries. The requirement that suffers is the "
                    "maintained concentration difference."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h10",
        "band": "harder",
        "text": "Crossing the alveolus wall costs no energy at all. So why "
                "does keeping gas exchange going still cost a body a great "
                "deal of energy?",
        "options": [
            {"text": "Because the cells of the alveolus wall spend energy "
                     "opening up a path for every single molecule that "
                     "crosses it.",
             "correct": False,
             "why": "There is no path to open and no cell that spends anything "
                    "on the crossing. The energy goes somewhere else "
                    "entirely."},
            {"text": "Because each oxygen molecule has to be given energy "
                     "before it will cross a wall as thin as that one.",
             "correct": False,
             "why": "The molecules already have all the movement they need, "
                    "and thinness makes crossing easier rather than harder. "
                    "Nothing is given energy."},
            {"text": "It does not — a body at rest spends no energy on "
                     "breathing or blood flow.",
             "correct": False,
             "why": "The breathing muscles and the heart work every minute of "
                    "your life, awake or asleep. Both cost energy "
                    "continuously."},
            {"text": "Because breathing and blood flow, which keep the "
                     "difference open, cost muscular work.",
             "correct": True},
        ],
        "figure": None,
    },
]
