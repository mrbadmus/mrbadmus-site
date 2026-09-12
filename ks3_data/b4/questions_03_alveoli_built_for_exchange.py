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
    {
        "id": "b4-03-e11",
        "band": "easier",
        "text": "The liquid lining an alveolus pulls its walls together, and a very "
                "premature baby's lungs sometimes stick shut because of it. "
                "What normally stops this happening?",
        "options": [
            {"text": "A layer of muscle in the alveolus wall that holds it "
                     "open by force.",
             "correct": False,
             "why": "There is no muscle in an alveolus wall at any age. "
                    "What keeps the film from sticking is a change to the "
                    "liquid itself, not a structure pulling against it."},
            {"text": "The dense capillary network, which is stiff enough to "
                     "hold the wall's shape.",
             "correct": False,
             "why": "Capillaries carry blood; they do nothing to a liquid "
                    "film's surface tension. The fix works on the liquid "
                    "directly."},
            {"text": "Breathing itself, which keeps the walls apart by "
                     "pushing air between them.",
             "correct": False,
             "why": "Air arriving does not prise a wall open. What is "
                    "pulling the walls together is the liquid's own surface "
                    "tension, and that has to be reduced chemically."},
            {"text": "Surfactant, a substance that lowers the surface "
                     "tension of the liquid film.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e12",
        "band": "easier",
        "text": "Surfactant is made by cells in the alveolar wall. Roughly "
                "when does the body start producing it, during pregnancy?",
        "options": [
            {"text": "From the very first weeks, before any other lung "
                     "tissue has formed.",
             "correct": False,
             "why": "Surfactant is one of the last things to develop, not "
                    "one of the first. It is produced late, from around "
                    "week 24 onwards."},
            {"text": "Not until several weeks after birth.",
             "correct": False,
             "why": "It has to be present before the first breath, or that "
                    "breath could not inflate the lungs. Production starts "
                    "before birth, from about week 24."},
            {"text": "From about week 24 of pregnancy onwards.",
             "correct": True},
            {"text": "Only once the baby starts breathing air for the first "
                     "time.",
             "correct": False,
             "why": "That would be too late — the first breath needs "
                    "surfactant already present to succeed. It starts being "
                    "made from about week 24, well before birth."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e13",
        "band": "easier",
        "text": "What does the term concentration difference mean?",
        "options": [
            {"text": "The total amount of a substance present on both sides "
                     "of a surface added together.",
             "correct": False,
             "why": "Adding the two sides together tells you nothing about "
                    "which way anything will move. Diffusion depends on the "
                    "gap between the two sides, not their total."},
            {"text": "How quickly a substance is moving as it crosses a "
                     "surface.",
             "correct": False,
             "why": "Speed of crossing is a result of the difference, not "
                    "the difference itself. The difference is a comparison "
                    "of amounts, not a measure of movement."},
            {"text": "The number of different gases present on one side of "
                     "a surface.",
             "correct": False,
             "why": "This counts how many kinds of gas are there, not how "
                    "much of any one of them. A concentration difference is "
                    "about amount, for a single substance, compared across "
                    "a surface."},
            {"text": "How much more of a substance there is on one side of "
                     "a surface than on the other.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e14",
        "band": "easier",
        "text": "What is meant by a gas exchange surface?",
        "options": [
            {"text": "Any part of the body where two different gases meet "
                     "each other in the air.",
             "correct": False,
             "why": "Gases mix in the air all the time without any exchange "
                    "happening. A gas exchange surface is specifically "
                    "where a gas crosses between air and blood."},
            {"text": "The surface where oxygen and carbon dioxide cross "
                     "between air and blood.",
             "correct": True},
            {"text": "The outer skin of the lungs, which separates them "
                     "from the rest of the chest.",
             "correct": False,
             "why": "The outer covering of a lung does no exchanging at "
                    "all. The exchange surface is deep inside, at the "
                    "alveoli."},
            {"text": "Any tube that carries air towards the alveoli.",
             "correct": False,
             "why": "A tube that carries air is doing transport, not "
                    "exchange. Nothing crosses into the blood until the air "
                    "reaches an alveolus."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e15",
        "band": "easier",
        "text": "Breathing and blood flow both help keep the concentration "
                "difference open. What is breathing's own job in doing "
                "that?",
        "options": [
            {"text": "Refreshing the air side, so the alveolar oxygen level "
                     "stays high.",
             "correct": True},
            {"text": "Carrying absorbed oxygen away, so the blood side "
                     "stays low.",
             "correct": False,
             "why": "That is blood flow's job, not breathing's. Breathing "
                    "acts on the air side of the wall; it does not touch "
                    "the blood at all."},
            {"text": "Squeezing oxygen molecules through the alveolus wall.",
             "correct": False,
             "why": "Nothing squeezes anything through a wall. Breathing "
                    "keeps the air side supplied; the crossing itself is "
                    "diffusion."},
            {"text": "Warming the air so that oxygen dissolves more easily.",
             "correct": False,
             "why": "Warming the air is not breathing's role here, and the "
                    "moist lining is what lets gases dissolve. Breathing's "
                    "job is refreshing the supply of air."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e16",
        "band": "easier",
        "text": "The oxygen level in the air and in the blood at an alveolus "
                "becomes exactly equal. Has diffusion stopped?",
        "options": [
            {"text": "Yes, because there is nothing left to make molecules "
                     "cross.",
             "correct": False,
             "why": "Molecules do not need a reason or a push to cross — "
                    "they are moving randomly the whole time. Equal levels "
                    "only means the crossings each way have become equally "
                    "likely."},
            {"text": "No — molecules are still crossing both ways, and the "
                     "net movement is simply zero.",
             "correct": True},
            {"text": "Yes, and it will only start again once fresh air "
                     "arrives.",
             "correct": False,
             "why": "Nothing has switched off waiting for a signal. "
                    "Crossings never stopped; only the net figure — the "
                    "difference between the two directions — reached zero."},
            {"text": "No, because one side always keeps a slight edge over "
                     "the other.",
             "correct": False,
             "why": "The question describes the levels as exactly equal, "
                    "with no edge on either side. Diffusion continuing does "
                    "not need one side to be ahead — it needs molecules "
                    "moving, and they always are."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e17",
        "band": "easier",
        "text": "Which requirement explains why the lungs contain about 500 "
                "million small alveoli rather than one large air space of "
                "the same volume?",
        "options": [
            {"text": "A short diffusion distance.",
             "correct": False,
             "why": "Distance is about the thickness of the wall a gas "
                    "crosses, which does not change with how many alveoli "
                    "there are. Splitting a space into many small sacs is "
                    "about area, not distance."},
            {"text": "A maintained concentration difference.",
             "correct": False,
             "why": "The concentration difference is kept open by breathing "
                    "and blood flow, not by how the space is divided up. "
                    "Dividing it into millions of sacs is what creates the "
                    "surface."},
            {"text": "A moist surface.",
             "correct": False,
             "why": "Moisture is about the liquid film lining each alveolus, "
                    "which would be needed whether there were one sac or "
                    "millions. The number of sacs is about surface area."},
            {"text": "A large surface area.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e18",
        "band": "easier",
        "text": "An oxygen molecule reaches the alveolus wall from the air "
                "side but happens not to cross at that moment. What "
                "happens to it?",
        "options": [
            {"text": "It is destroyed, because a failed crossing uses it "
                     "up.",
             "correct": False,
             "why": "Nothing is used up or destroyed by simply bumping into "
                    "a wall. The molecule carries on moving exactly as "
                    "before."},
            {"text": "It waits at the wall until it is its turn to cross.",
             "correct": False,
             "why": "There is no queue and no turn-taking at a wall. The "
                    "molecule keeps moving randomly and may reach the wall "
                    "again later, or never."},
            {"text": "It simply carries on moving randomly, and may reach "
                     "the wall again later.",
             "correct": True},
            {"text": "It is pushed back towards the middle of the alveolus "
                     "by the other molecules.",
             "correct": False,
             "why": "Nothing pushes it deliberately anywhere. Its next "
                    "collision is just as random as the last one — there is "
                    "no aim involved."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e19",
        "band": "easier",
        "text": "Suppose the liquid film lining an alveolus dried out "
                "completely and was not replaced. Which requirement would "
                "fail first?",
        "options": [
            {"text": "The alveolus would lose most of its surface area.",
             "correct": False,
             "why": "The alveolus would still have exactly the same "
                    "surface, folded the same way. Losing the liquid does "
                    "not shrink the area at all."},
            {"text": "The wall would become several cells thicker to "
                     "cross.",
             "correct": False,
             "why": "The wall itself would still be one cell thick. Drying "
                    "out changes what the gas has to dissolve in, not how "
                    "far it has to travel."},
            {"text": "The gases would have no liquid to dissolve in "
                     "before crossing.",
             "correct": True},
            {"text": "Breathing and blood flow would stop keeping the "
                     "difference open.",
             "correct": False,
             "why": "Breathing and blood flow could carry on exactly as "
                    "before. What has gone wrong here is specifically the "
                    "liquid the gas needs to dissolve in first."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e20",
        "band": "easier",
        "text": "Imagine a disease that made every capillary wall three "
                "cells thick instead of one, without changing anything "
                "else about the alveoli. Which requirement would fail "
                "first?",
        "options": [
            {"text": "The gas would have three times as far to travel "
                     "through the capillary wall.",
             "correct": True},
            {"text": "There would be much less surface available for gas "
                     "to cross.",
             "correct": False,
             "why": "Nothing here changes how much surface is available — "
                    "the alveoli themselves are untouched. What has changed "
                    "is how far a gas has to travel."},
            {"text": "The lining would no longer be able to stay moist.",
             "correct": False,
             "why": "A thicker wall is still just as capable of staying "
                    "moist. The problem this creates is one of distance, "
                    "not wetness."},
            {"text": "Breathing and blood flow would stop keeping the "
                     "difference open.",
             "correct": False,
             "why": "Breathing and blood flow are unaffected by how thick "
                    "the capillary wall is. What has been damaged is how "
                    "far the gas must diffuse."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e21",
        "band": "easier",
        "text": "Why does the body need oxygen to cross into the blood at "
                "the alveoli at all?",
        "options": [
            {"text": "So that every cell in the body can use it in "
                     "respiration.",
             "correct": True},
            {"text": "So that the blood has something to make new cells "
                     "with.",
             "correct": False,
             "why": "New cells are built mainly from things absorbed in "
                    "digestion, not from oxygen. Oxygen's role is in "
                    "respiration, releasing energy from glucose."},
            {"text": "So that carbon dioxide has a gas to react with "
                     "before it leaves.",
             "correct": False,
             "why": "Oxygen and carbon dioxide cross independently, each "
                    "following its own difference. Neither one reacts with "
                    "the other at the alveolus."},
            {"text": "So that the alveoli themselves have a reserve to "
                     "draw on.",
             "correct": False,
             "why": "Nothing is reserved anywhere in an alveolus. Oxygen "
                    "crosses straight into the blood and is carried away, "
                    "on its way to being used by cells across the body."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e22",
        "band": "easier",
        "text": "The wall between two neighbouring alveoli breaks down, so "
                "they merge into one larger space. What happens to the "
                "total exchange surface at that spot?",
        "options": [
            {"text": "It falls, because two separate surfaces have become "
                     "one.",
             "correct": True},
            {"text": "It rises, because the new space is bigger overall.",
             "correct": False,
             "why": "A bigger space is not the same as more surface. "
                    "Losing the wall between them removes surface that used "
                    "to line each one separately."},
            {"text": "It stays the same, because no tissue has actually "
                     "been destroyed.",
             "correct": False,
             "why": "Tissue has been destroyed — the shared wall itself, "
                    "which used to be lined surface on both sides. Merging "
                    "two sacs into one always loses surface."},
            {"text": "It cannot be worked out without knowing the new "
                     "space's volume.",
             "correct": False,
             "why": "Volume is not what decides this. Merging always turns "
                    "two linings into one, so the surface falls whatever "
                    "the resulting volume turns out to be."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e23",
        "band": "easier",
        "text": "Oxygen crosses from the alveolar air into the blood. Which "
                "way does carbon dioxide cross the same wall?",
        "options": [
            {"text": "From the alveolar air into the blood, alongside the "
                     "oxygen.",
             "correct": False,
             "why": "That would mean both gases moving the same way, which "
                    "is not what happens. Carbon dioxide moves the "
                    "opposite way to oxygen."},
            {"text": "From the blood into the alveolar air.",
             "correct": True},
            {"text": "It does not cross at all — it leaves the body some "
                     "other way.",
             "correct": False,
             "why": "The alveolus wall is exactly where carbon dioxide "
                    "leaves the blood. There is no other exit for it."},
            {"text": "Both ways equally, so there is no overall movement of "
                     "it.",
             "correct": False,
             "why": "There is a clear overall movement: out of the blood "
                    "and into the alveolar air, driven by the difference "
                    "between the two sides."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e24",
        "band": "easier",
        "text": "At an alveolus, which is higher: the carbon dioxide level "
                "in the blood arriving, or the carbon dioxide level in the "
                "alveolar air?",
        "options": [
            {"text": "The blood arriving.",
             "correct": True},
            {"text": "The alveolar air.",
             "correct": False,
             "why": "If the air held more carbon dioxide than the blood, it "
                    "would cross the other way. It leaves the blood because "
                    "the blood arriving holds more of it."},
            {"text": "Neither — the two are always equal at this point.",
             "correct": False,
             "why": "If the two were equal there would be no net movement "
                    "of carbon dioxide at all. There is a clear difference, "
                    "which is what drives it across."},
            {"text": "It depends entirely on how fast the person is "
                     "breathing at that moment.",
             "correct": False,
             "why": "Breathing rate changes how fast the alveolar air is "
                    "refreshed, not which side starts out higher. Blood "
                    "returning from the body's tissues is always the "
                    "higher side for carbon dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e25",
        "band": "easier",
        "text": "Which of these statements about diffusion at an alveolus "
                "is false?",
        "options": [
            {"text": "Molecules move in both directions across the wall "
                     "at once.",
             "correct": False,
             "why": "This one is true. Crossings happen both ways all the "
                    "time; only the difference between them is the net "
                    "movement."},
            {"text": "A molecule stops moving once it has crossed the "
                     "wall.",
             "correct": True},
            {"text": "No energy from any cell is spent making a molecule "
                     "cross.",
             "correct": False,
             "why": "This one is true. Diffusion needs no pump and no "
                    "energy — the molecules' own random motion is enough."},
            {"text": "Which way a gas crosses depends on where it is more "
                     "concentrated.",
             "correct": False,
             "why": "This one is true, and it is the whole basis of the "
                    "lesson: net movement runs from the more concentrated "
                    "side to the less concentrated one."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e26",
        "band": "easier",
        "text": "A dense network of capillaries wraps around every alveolus. "
                "What does making it dense, rather than sparse, actually "
                "achieve?",
        "options": [
            {"text": "It gives the alveolus a stronger structure, so it is "
                     "less likely to collapse.",
             "correct": False,
             "why": "Structural support is not a capillary's job — that is "
                    "closer to what surfactant does for the liquid film. A "
                    "capillary network is entirely about moving blood."},
            {"text": "It adds extra surface area for gas to cross, on top "
                     "of the alveolus wall itself.",
             "correct": False,
             "why": "Gas crosses through both walls together, but the "
                    "capillary itself does not add a separate exchange "
                    "surface. Density is about how much blood is brought "
                    "past, not about extra area."},
            {"text": "It slows the blood down, giving each red blood cell "
                     "longer to absorb oxygen.",
             "correct": False,
             "why": "Density is not about speed. A dense network is about "
                    "how much blood is in contact with the surface at any "
                    "one time, keeping the blood side low."},
            {"text": "It brings a great deal of blood very close to the "
                     "surface, so more of it can be kept low in oxygen at "
                     "once.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e27",
        "band": "easier",
        "text": "A person breathes in and out of a sealed bag, so the same "
                "air is used over and over and the oxygen left in it falls "
                "steadily towards the level already in their blood. Their "
                "alveoli are undamaged. Which requirement is failing?",
        "options": [
            {"text": "The alveoli have lost some of their surface.",
             "correct": False,
             "why": "Every alveolus is still there and still the same size, "
                    "so the amount of surface available for crossing has "
                    "not changed at all."},
            {"text": "The walls the gas crosses have grown thicker.",
             "correct": False,
             "why": "The alveolus wall and the capillary wall are each still "
                    "one cell thick, so a gas has exactly as far to travel "
                    "as it did before."},
            {"text": "The gap between the oxygen in the air and the "
                     "oxygen in the blood is closing.",
             "correct": True},
            {"text": "The liquid lining the alveoli has dried out.",
             "correct": False,
             "why": "The film of liquid lining the alveoli is untouched by "
                    "what is in the bag, so gases can still dissolve there "
                    "as easily as ever."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e28",
        "band": "easier",
        "text": "Roughly how much total gas exchange surface do a pair of "
                "human lungs provide?",
        "options": [
            {"text": "About 7 m².",
             "correct": False,
             "why": "This is ten times too small. The true figure is far "
                    "larger — roughly a classroom floor and a half."},
            {"text": "About 700 m².",
             "correct": False,
             "why": "This is ten times too large — closer to the area of "
                    "three tennis courts than a pair of lungs. The true "
                    "figure is a tenth of this."},
            {"text": "About 0.7 m².",
             "correct": False,
             "why": "This is a hundred times too small, about the size of "
                    "a large bath towel. The real total, from around 500 "
                    "million alveoli, is much greater."},
            {"text": "About 70 m².",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e29",
        "band": "easier",
        "text": "Does each alveolus have its own separate, private blood "
                "supply, or does it share one with its neighbours?",
        "options": [
            {"text": "Each alveolus has its own private blood vessel, "
                     "completely separate from every other alveolus.",
             "correct": False,
             "why": "The network runs across many alveoli at once rather "
                    "than being split into millions of private vessels. It "
                    "is described as dense precisely because it covers so "
                    "much surface continuously."},
            {"text": "Alveoli share one continuous, dense network of "
                     "capillaries running across many of them.",
             "correct": True},
            {"text": "Only some alveoli have any blood supply; the rest "
                     "rely on their neighbours to absorb for them.",
             "correct": False,
             "why": "Every alveolus needs its own capillaries pressed "
                    "against it — gas cannot travel sideways from one "
                    "alveolus's blood supply to feed another one."},
            {"text": "Alveoli have no blood supply of their own; blood "
                     "only reaches the airway higher up.",
             "correct": False,
             "why": "If blood never reached the alveoli themselves, no "
                    "oxygen could ever cross into it. The whole point of "
                    "the dense network is that it wraps every alveolus."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e30",
        "band": "easier",
        "text": "What is the name for one of the roughly 500 million tiny "
                "air sacs where gas crosses between the lungs and the "
                "blood?",
        "options": [
            {"text": "A bronchiole.",
             "correct": False,
             "why": "A bronchiole is one of the narrow tubes that carries "
                    "air towards these sacs. No gas crosses into the blood "
                    "along a bronchiole."},
            {"text": "An alveolus.",
             "correct": True},
            {"text": "A capillary.",
             "correct": False,
             "why": "A capillary is the tiny blood vessel wrapped around "
                    "the air sac, not the sac itself. Blood, not air, is "
                    "inside a capillary."},
            {"text": "A trachea.",
             "correct": False,
             "why": "The trachea is the single wide tube at the top of the "
                    "airway. It is nothing like the millions of tiny sacs "
                    "at the far end of it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-e31",
        "band": "easier",
        "text": "Between one quiet breath and the next, is the air inside "
                "an alveolus completely replaced, or only partly "
                "replaced?",
        "options": [
            {"text": "Completely replaced, so each breath starts with "
                     "entirely fresh air.",
             "correct": False,
             "why": "About half a litre moves with each quiet breath, which "
                    "is not the whole of what is already in the alveoli. "
                    "The old air is mixed with fresh, not swapped for it."},
            {"text": "Only partly replaced, roughly twelve times a minute.",
             "correct": True},
            {"text": "Not replaced at all between breaths — it only moves "
                     "when you breathe deeply.",
             "correct": False,
             "why": "Even a quiet breath moves some air in and out. It is "
                    "replaced a little with every single breath, not only "
                    "on deep ones."},
            {"text": "It depends on whether you are breathing in or "
                     "breathing out at that moment.",
             "correct": False,
             "why": "The replacement figure describes what happens over "
                    "whole breaths, not a difference between the two "
                    "halves of one breath. Either way, it is a partial "
                    "refresh, not a complete swap."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s11",
        "band": "standard",
        "text": "The alveoli give roughly 70 m² of exchange surface. An "
                "adult's skin covers roughly 2 m². Roughly how many times "
                "greater is the alveolar surface than the skin's?",
        "options": [
            {"text": "About 3.5 times greater.",
             "correct": False,
             "why": "This divides by ten too many times. 70 divided by 2 "
                    "gives 35, not a number close to it."},
            {"text": "About 35 times greater.",
             "correct": True},
            {"text": "About 350 times greater.",
             "correct": False,
             "why": "This multiplies rather than divides. Dividing 70 by "
                    "2 gives 35, ten times smaller than this."},
            {"text": "Roughly the same, since both are body surfaces.",
             "correct": False,
             "why": "Being surfaces of the same body does not make them "
                    "the same size. One is folded into a chest and is "
                    "dozens of times larger."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s12",
        "band": "standard",
        "text": "A small clot damages the capillaries around one patch of "
                "alveoli, but the alveoli themselves and the breathing "
                "supplying them are completely undamaged. What happens to "
                "gas exchange at that patch?",
        "options": [
            {"text": "It carries on completely normally, since the wall "
                     "and the air supply reaching it are both fine.",
             "correct": False,
             "why": "A working wall and air supply are not enough alone. "
                    "Without blood flowing past, the blood side is never "
                    "kept low."},
            {"text": "It fails, because the wall itself has been "
                     "damaged by the clot.",
             "correct": False,
             "why": "The wall is stated to be undamaged. What has "
                    "failed is the blood supply behind it."},
            {"text": "It fails, because blood is no longer carried away "
                     "to keep the blood side low.",
             "correct": True},
            {"text": "It improves, since still blood has longer to "
                     "absorb the oxygen.",
             "correct": False,
             "why": "Still blood reaches the air's level and then stops "
                    "absorbing. Movement, not delay, keeps the "
                    "difference open."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s13",
        "band": "standard",
        "text": "Premature babies with too little surfactant are sometimes "
                "given artificial surfactant delivered directly into their "
                "lungs. Why would blowing air in harder not be a "
                "substitute treatment?",
        "options": [
            {"text": "Harder blowing would damage tiny lungs faster than "
                     "surfactant ever could.",
             "correct": False,
             "why": "Damage is a real risk of forcing air in, but it is "
                    "not why surfactant is needed instead — pressure "
                    "does not fix a surface-tension problem."},
            {"text": "It would work just as well; surfactant is only "
                     "used because it is gentler.",
             "correct": False,
             "why": "It is not merely a gentler version of the same "
                    "fix. Extra pressure does not touch why the walls "
                    "are sticking."},
            {"text": "Blowing harder adds extra oxygen the baby badly "
                     "needs, which surfactant treatment does not supply.",
             "correct": False,
             "why": "Both treatments target the same problem — alveoli "
                    "that will not stay open — not a shortage of "
                    "oxygen."},
            {"text": "It does nothing to the surface tension pulling "
                     "the walls together; that is chemistry, not "
                     "pressure.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s14",
        "band": "standard",
        "text": "On the bench, 90 crossings happen each second for every "
                "1 kPa of concentration difference. If the difference is "
                "4 kPa, what net crossing rate would you expect?",
        "options": [
            {"text": "360 per second.",
             "correct": True},
            {"text": "22.5 per second.",
             "correct": False,
             "why": "This divides instead of multiplying. A bigger "
                    "difference means more crossings, not fewer."},
            {"text": "94 per second.",
             "correct": False,
             "why": "This adds the two figures instead of multiplying "
                    "them, as the rule requires."},
            {"text": "4 per second.",
             "correct": False,
             "why": "This uses the kPa figure alone and ignores the "
                    "90-per-kPa rule entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s15",
        "band": "standard",
        "text": "During light activity a patient's breaths each move "
                "0.6 litres, and they take 15 breaths a minute. Roughly "
                "how much air moves through the alveoli in one minute?",
        "options": [
            {"text": "About 9 litres.",
             "correct": True},
            {"text": "About 25 litres.",
             "correct": False,
             "why": "This divides the breath count by the volume instead "
                    "of multiplying them. Fifteen breaths of 0.6 litres "
                    "comes to nine litres."},
            {"text": "About 0.6 litres.",
             "correct": False,
             "why": "That is one breath's share, not a whole minute's. "
                    "Fifteen such breaths happen every minute."},
            {"text": "About 15 litres.",
             "correct": False,
             "why": "This treats the number of breaths as the answer. "
                    "Each breath moves 0.6 litres, not a whole one."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s16",
        "band": "standard",
        "text": "A student argues: “The alveolus wall is only one cell "
                "thick, so gas exchange there must use almost no "
                "energy.” Is the second half correctly linked to the "
                "first?",
        "options": [
            {"text": "Yes — a thinner wall always means a lower energy "
                     "cost for what crosses it.",
             "correct": False,
             "why": "Thinness affects distance and speed, not whether "
                    "crossing costs energy. Diffusion costs nothing at "
                    "any thickness."},
            {"text": "No — thinness is not why it costs nothing; "
                     "diffusion needs no energy at any thickness.",
             "correct": True},
            {"text": "No — a thinner wall actually costs more energy, "
                     "since gas can leak the wrong way too.",
             "correct": False,
             "why": "Nothing about thickness lets gas leak backwards, "
                    "and diffusion still costs no energy regardless."},
            {"text": "Yes, but only because this particular wall has no "
                     "muscle in it at all.",
             "correct": False,
             "why": "Whether a wall has muscle is irrelevant — diffusion "
                    "never uses energy anywhere in the body."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s17",
        "band": "standard",
        "text": "Capillaries always run alongside an alveolus rather than "
                "through the middle of its air space, even though that "
                "would put blood even closer to more air. Why?",
        "options": [
            {"text": "There is not enough room inside an alveolus for a "
                     "capillary to fit.",
             "correct": False,
             "why": "Size is not the barrier — capillaries are "
                    "extremely narrow. Blood staying inside a vessel is "
                    "the real reason."},
            {"text": "Blood is too heavy to be suspended in an "
                     "air-filled space.",
             "correct": False,
             "why": "Weight is not the issue. The problem is blood no "
                    "longer being separated from the air by a wall."},
            {"text": "Blood has to stay inside a vessel; running it "
                     "through the air space would remove the wall.",
             "correct": True},
            {"text": "Gas would diffuse far too fast and completely "
                     "overwhelm any blood placed in the air space.",
             "correct": False,
             "why": "Faster diffusion is not a danger here. Air meeting "
                    "blood with no wall is the real problem."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s18",
        "band": "standard",
        "text": "Two identical alveoli differ in one way: alveolus A has "
                "twice as many capillaries wrapped around it as alveolus "
                "B. At a given moment, which achieves better gas "
                "exchange, and why?",
        "options": [
            {"text": "B, because having fewer capillaries means far "
                     "less blood is ever competing for the same oxygen.",
             "correct": False,
             "why": "Blood vessels do not compete for oxygen. More "
                    "capillaries simply keeps more blood moving past the "
                    "surface."},
            {"text": "They are identical, since both share the same "
                     "area and wall thickness.",
             "correct": False,
             "why": "Area and thickness are only two of the four "
                    "requirements. Capillary number changes the third — "
                    "a maintained difference."},
            {"text": "B, because fewer capillaries leaves an overall "
                     "thinner wall to cross.",
             "correct": False,
             "why": "Capillary number does not change wall thickness. "
                    "It changes how much blood keeps the blood side "
                    "low."},
            {"text": "A, because more blood passing keeps the blood "
                     "side lower and the difference steeper.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s19",
        "band": "standard",
        "text": "Two students measure the same state — alveolar 13.3 "
                "kPa, blood 5.3 kPa, a difference of 8.0 kPa — but one "
                "mistakenly uses 45 crossings per kPa instead of the "
                "bench's actual 90. What net figure results, wrongly and "
                "correctly?",
        "options": [
            {"text": "Wrongly 360; correctly 720.",
             "correct": True},
            {"text": "Wrongly 45; correctly 90.",
             "correct": False,
             "why": "These are the constants themselves, not the "
                    "results of using them on the 8.0 kPa gap."},
            {"text": "Wrongly 720; correctly 360.",
             "correct": False,
             "why": "The two results are swapped — the smaller "
                    "constant, 45, must give the smaller answer."},
            {"text": "Wrongly 8; correctly 8.",
             "correct": False,
             "why": "This uses the kPa figure alone. Both results need "
                    "the gap multiplied by a crossings-per-kPa figure."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s20",
        "band": "standard",
        "text": "In the “breathing stopped” state, the alveolar reading "
                "itself falls, from 13.3 kPa to 5.5 kPa, even though the "
                "blood side keeps working normally. Why does the "
                "alveolar level fall if breathing, not blood flow, has "
                "stopped?",
        "options": [
            {"text": "Stopping breathing directly and immediately lowers "
                     "what the alveolar air itself actually contains.",
             "correct": False,
             "why": "Stopping breathing does not change the air already "
                    "there. It is blood still draining it that lowers "
                    "the level."},
            {"text": "Blood flow keeps draining oxygen away, and with "
                     "no fresh air arriving the level drops.",
             "correct": True},
            {"text": "The wall starts letting oxygen escape once "
                     "breathing stops refreshing it.",
             "correct": False,
             "why": "The wall is unchanged. Oxygen simply keeps leaving "
                    "the usual way and is not being replaced."},
            {"text": "The reading only appears to fall as the sensor "
                     "recalibrates itself.",
             "correct": False,
             "why": "The fall is a real reading, caused by blood taking "
                    "oxygen from air no longer being refreshed."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s21",
        "band": "standard",
        "text": "Using the bench's rule of 90 crossings per kPa per "
                "second, work out the inward count, outward count and "
                "net figure for an alveolar reading of 10 kPa and a "
                "blood reading of 4 kPa.",
        "options": [
            {"text": "Inward 900, outward 360, net 540.",
             "correct": True},
            {"text": "Inward 1000, outward 400, net 600.",
             "correct": False,
             "why": "This uses the two kPa readings directly, skipping "
                    "the 90-per-kPa rule entirely."},
            {"text": "Inward 360, outward 900, net −540.",
             "correct": False,
             "why": "The two sides are swapped — the higher reading, "
                    "10 kPa, gives the larger, inward count."},
            {"text": "Inward 900, outward 400, net 500.",
             "correct": False,
             "why": "The outward figure is wrong: 4 kPa multiplied by "
                    "90 gives 360 crossings, not 400."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s22",
        "band": "standard",
        "text": "An injury destroys the capillary network around one "
                "small patch of an alveolus, but the wall and moist "
                "lining there are completely undamaged. Would oxygen "
                "still cross into the blood there?",
        "options": [
            {"text": "Yes — a good wall and a moist lining alone are "
                     "always enough on their own for exchange.",
             "correct": False,
             "why": "A wall and a moist lining meet only two of the "
                    "four requirements. Without blood there, oxygen has "
                    "nowhere to go."},
            {"text": "It depends only on how thick the wall at that "
                     "patch still is.",
             "correct": False,
             "why": "Thickness affects speed where blood IS present. "
                    "Here no blood is present at all."},
            {"text": "No — without a capillary there, there is no "
                     "blood for the oxygen to cross into.",
             "correct": True},
            {"text": "Yes, but slowly, since some blood will eventually "
                     "reach the patch anyway.",
             "correct": False,
             "why": "The network there has been destroyed, not merely "
                    "reduced. No vessel means no blood, however long you "
                    "wait."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s23",
        "band": "standard",
        "text": "A student says: “All four requirements for a good "
                "exchange surface matter, and losing any one of them "
                "badly damages exchange even when the other three are "
                "excellent.” Is that a fair summary?",
        "options": [
            {"text": "No — surface area matters far more than the "
                     "other three, so the rest can be fairly ordinary.",
             "correct": False,
             "why": "None of the four is treated as most important — "
                    "losing any one badly damages exchange even with the "
                    "other three excellent."},
            {"text": "Yes — the four work together, and losing any one "
                     "badly damages exchange.",
             "correct": True},
            {"text": "No — none of the four is ever essential on its "
                     "own, only useful.",
             "correct": False,
             "why": "Each one is shown to be necessary: losing area, "
                    "distance, moisture or the difference each damages "
                    "exchange badly on its own."},
            {"text": "Yes — but only because moisture matters most, "
                     "and without it nothing can dissolve at all.",
             "correct": False,
             "why": "Moisture is essential, but so are the other three "
                    "— a moist surface with no blood flow still "
                    "exchanges nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s24",
        "band": "standard",
        "text": "Alveolar air is partly replaced roughly twelve times a "
                "minute. Roughly how many seconds does one replacement "
                "take?",
        "options": [
            {"text": "About 5 seconds.",
             "correct": True},
            {"text": "About 20 seconds.",
             "correct": False,
             "why": "Twenty seconds allows only three replacements a "
                    "minute, not twelve."},
            {"text": "About 12 seconds.",
             "correct": False,
             "why": "This uses the twelve as if it were a time. Sixty "
                    "seconds shared between twelve gives five."},
            {"text": "About 1 second.",
             "correct": False,
             "why": "One second each would mean sixty replacements a "
                    "minute, far more than the stated twelve."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s25",
        "band": "standard",
        "text": "A patient's breathing rate doubles, from 12 to 24 "
                "breaths a minute, while each breath stays the same "
                "size. What would you expect to happen to how often the "
                "alveolar air is replaced?",
        "options": [
            {"text": "It would fall, since faster breathing gives each "
                     "breath less time to work.",
             "correct": False,
             "why": "There are simply more breaths happening. The total "
                    "replacement rate rises with breathing rate."},
            {"text": "It would roughly double too, to about 24 times a "
                     "minute.",
             "correct": True},
            {"text": "It would stay at twelve times a minute "
                     "regardless of rate.",
             "correct": False,
             "why": "The replacement rate is tied directly to how often "
                    "a breath happens, so doubling the breaths roughly "
                    "doubles it."},
            {"text": "It cannot change unless the size of each breath "
                     "changes too.",
             "correct": False,
             "why": "The change stated is in how OFTEN a breath "
                    "happens, which decides replacement rate whatever "
                    "the breath's size."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s26",
        "band": "standard",
        "text": "In the “blood flow stopped” state, the blood reading "
                "rises from 5.3 kPa to 13.1 kPa, close to alveolar 13.3 "
                "kPa but not exactly equal. Why does it not reach exactly "
                "13.3?",
        "options": [
            {"text": "Stopped blood flow means crossings have stopped "
                     "entirely, freezing the reading short.",
             "correct": False,
             "why": "Crossings have not stopped — stationary blood "
                    "still gains oxygen slowly as the gap narrows."},
            {"text": "The two figures are meant to be equal; 13.1 is "
                     "just a rounding error.",
             "correct": False,
             "why": "The 0.2 kPa gap is real. The crossing rate falls "
                    "as the gap closes, so the last of it takes a very "
                    "long time to disappear."},
            {"text": "The alveolar reading is falling too, so the two "
                     "never get the chance to meet.",
             "correct": False,
             "why": "The alveolar reading stays fixed at 13.3 here — "
                    "breathing is still running normally."},
            {"text": "The crossings slow as the gap narrows, so "
                     "stationary blood approaches 13.3 without quite "
                     "reaching it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s27",
        "band": "standard",
        "text": "The carbon dioxide crossing out at an alveolus was made "
                "by respiring cells across the body, not by anything in "
                "the lung. Why does it still cross out at the alveolus "
                "even though nothing there produced it?",
        "options": [
            {"text": "Diffusion follows the concentration difference, "
                     "not where the gas was originally made.",
             "correct": True},
            {"text": "It only crosses because blood pressure from the "
                     "heart forces it through the wall.",
             "correct": False,
             "why": "Blood pressure does not push gas through a wall — "
                    "diffusion, driven by the difference, does the "
                    "moving."},
            {"text": "It crosses because the surrounding lung tissue "
                     "also makes some, adding extra pressure to leave.",
             "correct": False,
             "why": "Lung tissue does not produce carbon dioxide here — "
                    "all of it arrives already dissolved in the blood."},
            {"text": "It cannot cross out unless the lung first "
                     "converts it into oxygen.",
             "correct": False,
             "why": "Nothing converts one gas into another. It crosses "
                    "exactly as it arrived, following the difference."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s28",
        "band": "standard",
        "text": "A model alveolus is wrapped in an extra layer of thin "
                "plastic film, keeping the same total surface area and "
                "distance. Predict the effect on gas exchange.",
        "options": [
            {"text": "It improves, since plastic keeps the moist "
                     "lining from drying out.",
             "correct": False,
             "why": "Protecting moisture only helps if gas can still "
                    "pass through — plastic film does not let it."},
            {"text": "It slows a little, since the film adds some "
                     "extra distance to cross.",
             "correct": False,
             "why": "The distance is stated as unchanged. The problem "
                    "is a material gas cannot pass through at all."},
            {"text": "It stops, because the film is impermeable — "
                     "thin is not the same as letting gas through.",
             "correct": True},
            {"text": "It carries on completely unchanged, since thinness "
                     "alone is all requirement 2 ever really asks for.",
             "correct": False,
             "why": "A short distance only helps if the material also "
                    "lets gas through, which an impermeable film does "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s29",
        "band": "standard",
        "text": "A raincoat is thin but keeps water firmly out. Why "
                "can't an alveolus use a barrier like a raincoat instead "
                "of a wet, permeable lining?",
        "options": [
            {"text": "A raincoat would let oxygen through but not "
                     "carbon dioxide, upsetting the balance.",
             "correct": False,
             "why": "A raincoat is not selective between gases — it is "
                    "built to keep a substance out entirely."},
            {"text": "A raincoat cannot be kept moist enough for gases "
                     "to dissolve in it.",
             "correct": False,
             "why": "The real mismatch is that a raincoat is built to "
                    "block a substance, not to let one through."},
            {"text": "A raincoat is far too thick to ever act as an "
                     "exchange surface.",
             "correct": False,
             "why": "Thickness is not the mismatch — some raincoat "
                    "fabric is very thin. Blocking, not thickness, is "
                    "the problem."},
            {"text": "A raincoat is built to block a substance "
                     "completely; an alveolus needs the gas to pass "
                     "through.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s30",
        "band": "standard",
        "text": "During vigorous exercise, breathing rate and blood "
                "flow rate both rise together. Why would raising only "
                "one of the two give a smaller benefit than raising both "
                "together?",
        "options": [
            {"text": "Raising only blood flow would make the alveoli "
                     "physically larger over time.",
             "correct": False,
             "why": "Nothing changes an alveolus's physical size in "
                    "response to blood flow."},
            {"text": "Raising only one leaves the other side "
                     "un-helped, so the difference cannot stay as "
                     "steep.",
             "correct": True},
            {"text": "Raising only breathing has no effect at all "
                     "unless blood flow rises too.",
             "correct": False,
             "why": "Breathing alone does still help, by keeping the "
                    "air side higher — just a smaller benefit than "
                    "both together."},
            {"text": "Raising only one would actually damage the "
                     "alveoli, which raising both avoids.",
             "correct": False,
             "why": "Nothing here suggests damage from raising either "
                    "alone — the issue is a smaller benefit, not harm."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-s31",
        "band": "standard",
        "text": "Air pollution very slightly lowers the oxygen "
                "percentage indoors, from 21% to 20.5%. Using the "
                "concentration-difference idea, would you expect a "
                "measurable difference in gas exchange at rest?",
        "options": [
            {"text": "Yes — the body cannot function at all below "
                     "exactly 21% oxygen.",
             "correct": False,
             "why": "There is no cliff-edge at 21% — exchange responds "
                    "gradually to the size of the gap, not a fixed "
                    "threshold."},
            {"text": "It cannot be predicted without knowing the exact "
                     "wall thickness involved.",
             "correct": False,
             "why": "Thickness affects the SIZE of a response, not "
                    "whether a change this small is noticeable."},
            {"text": "Yes — any fall in oxygen percentage immediately "
                     "halves net absorption.",
             "correct": False,
             "why": "Net absorption follows the size of the difference "
                    "— half a per cent is far too small a fraction to "
                    "halve anything."},
            {"text": "No — such a tiny change barely alters the "
                     "concentration difference exchange depends on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h11",
        "band": "harder",
        "text": "A researcher doubles BOTH the surface area and the "
                "concentration difference of a model exchange surface at "
                "once. A colleague predicts net exchange will simply "
                "double. Evaluate that prediction.",
        "options": [
            {"text": "It is too high, because a bigger concentration "
                     "difference across the surface actually slows exchange "
                     "down instead.",
             "correct": False,
             "why": "A bigger difference speeds diffusion up throughout "
                    "this lesson, never slows it."},
            {"text": "It cannot be judged at all without also knowing "
                     "the exact wall thickness used in this particular "
                     "model.",
             "correct": False,
             "why": "Thickness is held constant here — area and "
                    "difference alone are enough to judge the claim."},
            {"text": "It is exactly right, since the two changes "
                     "simply add together.",
             "correct": False,
             "why": "Area and difference each scale the rate on their "
                    "own, so doubling both multiplies rather than "
                    "adds."},
            {"text": "It is too low — doubling two independent factors "
                     "multiplies the effect, giving roughly fourfold.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h12",
        "band": "harder",
        "text": "A fish gill and a human alveolus both meet the same "
                "four requirements. Which does the gill meet more "
                "easily, simply by being surrounded by water rather than "
                "air?",
        "options": [
            {"text": "A large surface area, since water naturally adds "
                     "surface to anything submerged.",
             "correct": False,
             "why": "Submersion adds no surface — the gill's area comes "
                    "from its own stack of filaments."},
            {"text": "A moist surface — water is already there, unlike "
                     "a lung keeping itself wet against air.",
             "correct": True},
            {"text": "A maintained concentration difference, since "
                     "water refreshes itself automatically all around a "
                     "gill.",
             "correct": False,
             "why": "Water does not refresh itself — the fish still "
                    "has to actively flow water over the gill."},
            {"text": "A short diffusion distance, since water conducts "
                     "gases better than air does.",
             "correct": False,
             "why": "Distance is set by wall thickness, not by the "
                    "medium outside it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h13",
        "band": "harder",
        "text": "A ventilator delivers a fixed one litre of air with "
                "every breath. A patient's oxygen demand rises with a "
                "fever, but breathing rate is not increased to match. "
                "Predict the consequence.",
        "options": [
            {"text": "Net absorption per breath stays capped by the "
                     "fixed delivery of fresh air.",
             "correct": True},
            {"text": "Nothing changes, since fever does not affect gas "
                     "exchange at the alveoli.",
             "correct": False,
             "why": "Rising demand drains blood faster, which would "
                    "help — but only if the air side is also refreshed "
                    "to match."},
            {"text": "The alveoli enlarge on their own to meet the "
                     "rising demand.",
             "correct": False,
             "why": "Alveoli do not change size moment to moment. The "
                    "limit here is how often fresh air arrives."},
            {"text": "Net absorption rises automatically to match "
                     "whatever the body needs.",
             "correct": False,
             "why": "Nothing in this model adjusts the difference to "
                    "demand — it depends only on what is delivered."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h14",
        "band": "harder",
        "text": "A net absorption of 630 molecules per second is "
                "measured at a concentration difference of 7 kPa. Using "
                "the bench's rule of 90 per kPa, does this fit the "
                "model?",
        "options": [
            {"text": "Yes — 7 kPa times 90 gives exactly 630.",
             "correct": True},
            {"text": "No — the rule predicts 700, so this is too low.",
             "correct": False,
             "why": "7 multiplied by 90 gives 630, not 700."},
            {"text": "No — the rule predicts 560, so this is too high.",
             "correct": False,
             "why": "560 would need a difference of about 6.2 kPa, not "
                    "the stated 7."},
            {"text": "It needs the separate alveolar and blood values "
                     "to be checked.",
             "correct": False,
             "why": "The rule only needs the SIZE of the difference — "
                    "7 kPa is enough."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h15",
        "band": "harder",
        "text": "An engineer proposes replacing millions of tiny "
                "alveoli with one accordion-folded sheet giving the same "
                "70 m² inside the same 6 litres. Evaluate this design "
                "using the four requirements.",
        "options": [
            {"text": "It could never work, since a folded sheet cannot "
                     "hold 70 m² inside 6 litres.",
             "correct": False,
             "why": "The question states this area IS achieved — the "
                    "real difficulty is supplying every fold with fresh "
                    "air and blood evenly."},
            {"text": "Area, distance and moisture could match, but "
                     "supplying every fold with fresh air and blood "
                     "evenly is what branching already achieves.",
             "correct": True},
            {"text": "It makes no real difference either way, since "
                     "the requirements only ever care about the final "
                     "totals reached.",
             "correct": False,
             "why": "Two requirements depend on active flows reaching "
                    "every part evenly — a question of shape, not just "
                    "totals."},
            {"text": "It would work noticeably better, since one "
                     "continuous sheet wastes no space at all on the "
                     "internal walls between separate sections.",
             "correct": False,
             "why": "Those walls carry the capillary network — removing "
                    "them makes even blood supply harder, not easier."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h16",
        "band": "harder",
        "text": "A student says: “Net movement can only ever approach "
                "zero, never reach it, so a genuinely dead lung would "
                "still show a tiny reading.” Evaluate this using what "
                "keeps net movement non-zero in a living lung.",
        "options": [
            {"text": "Right, because diffusion never actually stops in "
                     "any material, living or dead.",
             "correct": False,
             "why": "Whether molecules keep moving is not the same as "
                    "whether there is a NET reading — without refreshing "
                    "flows the two sides equalise fully."},
            {"text": "Right, because the moist lining itself keeps on "
                     "producing a small difference of its own even long "
                     "after death.",
             "correct": False,
             "why": "The lining is a surface gases dissolve in, not a "
                    "source of difference — nothing gives it that role "
                    "once the flows stop."},
            {"text": "Neither view can really be judged at all, since "
                     "no genuinely dead lung has ever been measured this "
                     "way.",
             "correct": False,
             "why": "What keeps a difference open is known, which is "
                    "enough to reason about what happens in its "
                    "absence."},
            {"text": "Wrong — with breathing and blood flow permanently "
                     "gone, the difference would genuinely equalise to "
                     "zero.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h17",
        "band": "harder",
        "text": "The bench's worked states all follow net = 90 × "
                "(alveolar kPa − blood kPa). Using this rule, predict "
                "the net movement for an alveolar reading of 8.0 kPa and "
                "a blood reading of 6.5 kPa.",
        "options": [
            {"text": "135 into the blood.",
             "correct": True},
            {"text": "90 into the blood.",
             "correct": False,
             "why": "This is the constant itself, not the result of "
                    "using it on the 1.5 kPa gap."},
            {"text": "1305 into the blood.",
             "correct": False,
             "why": "This multiplies by the two readings added "
                    "together, not by their difference."},
            {"text": "135 out of the blood.",
             "correct": False,
             "why": "The alveolar reading is higher here, so oxygen "
                    "moves INTO the blood, not out of it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h18",
        "band": "harder",
        "text": "An engineer's artificial lung lets its moist lining "
                "drain under gravity when a patient lies flat, leaving "
                "the top alveoli dry. Predict the effect there, and why "
                "real lungs avoid it.",
        "options": [
            {"text": "Nothing changes, since gravity affects blood "
                     "flow but not the moist lining.",
             "correct": False,
             "why": "The lining is a liquid, and liquids are exactly "
                    "what gravity moves — a pool can drain, unlike a "
                    "thin held film."},
            {"text": "Exchange there fails; real lungs keep only a "
                     "thin film held by surface properties, not a "
                     "drainable pool.",
             "correct": True},
            {"text": "The top alveoli simply borrow the surface they "
                     "are missing directly from the flooded ones sitting "
                     "below them.",
             "correct": False,
             "why": "Surface area belongs to each alveolus individually "
                    "— one cannot borrow another's."},
            {"text": "Exchange there actually improves, since a dry "
                     "surface lets gas cross straight through without "
                     "having to dissolve first at all.",
             "correct": False,
             "why": "Gas must dissolve before crossing — a dry surface "
                    "stops it rather than helping."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h19",
        "band": "harder",
        "text": "A student concludes: “A villus and an alveolus meet "
                "the same four requirements, so any organ meeting them "
                "must end up the same shape.” Evaluate this conclusion.",
        "options": [
            {"text": "Fair, because both organs are built from the "
                     "same tissue arranged the same way.",
             "correct": False,
             "why": "The two look nothing alike — one is finger-like "
                    "folds, the other branching sacs."},
            {"text": "Fair, but only because both sit inside similarly "
                     "sized body cavities.",
             "correct": False,
             "why": "Cavity size does not decide shape — the two are "
                    "different solutions whatever cavity they sit in."},
            {"text": "It cannot be judged without measuring both "
                     "organs' exact surface area.",
             "correct": False,
             "why": "The claim is about shape following automatically, "
                    "which comparing appearance alone can settle."},
            {"text": "Not fair — the requirements constrain what an "
                     "organ achieves, not the shape it takes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h20",
        "band": "harder",
        "text": "A patient has emphysema in one lung only; the other is "
                "healthy. At rest, their blood oxygen is only slightly "
                "below normal — far less affected than losing half their "
                "surface might suggest. Suggest why.",
        "options": [
            {"text": "At rest, the healthy lung's surface alone may "
                     "already exceed what the body needs.",
             "correct": True},
            {"text": "The damaged lung's alveoli quickly repair "
                     "themselves once demand at rest is lower.",
             "correct": False,
             "why": "Lost alveolar walls never repair, at any activity "
                    "level — the mild symptoms come from spare capacity."},
            {"text": "Losing half the surface only ever halves the "
                     "speed of exchange, never the total amount.",
             "correct": False,
             "why": "Speed is exactly what limits how much oxygen "
                    "crosses in a given time — this is not the "
                    "explanation here."},
            {"text": "The healthy lung's alveoli grow larger to make "
                     "up the missing surface.",
             "correct": False,
             "why": "Alveoli do not enlarge to compensate for damage "
                    "elsewhere — the healthy lung was already enough."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h21",
        "band": "harder",
        "text": "Two patients each have about half the normal exchange "
                "surface — one from emphysema, one born with naturally "
                "smaller but healthy lungs. Are their symptoms likely "
                "identical? Explain.",
        "options": [
            {"text": "Yes — half the surface is half the surface, "
                     "whatever the cause.",
             "correct": False,
             "why": "Having the same current surface does not mean the "
                    "same history — one has fallen from something "
                    "larger."},
            {"text": "No — the naturally smaller lungs cannot support "
                     "life at all.",
             "correct": False,
             "why": "Smaller but healthy lungs can support normal life "
                    "if demand has adjusted around that baseline from "
                    "birth."},
            {"text": "Not necessarily — one is a loss from a larger "
                     "baseline, likely worsening; the other is a stable "
                     "lifelong baseline.",
             "correct": True},
            {"text": "No — emphysema only ever affects a small handful "
                     "of alveoli, far fewer than a naturally small lung's "
                     "own shortfall.",
             "correct": False,
             "why": "Emphysema can spread widely, and both patients are "
                    "stated to have lost the same half."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h22",
        "band": "harder",
        "text": "Explain why real lungs achieve 70 m² using millions of "
                "small branching sacs rather than one large flat sheet "
                "folded to fit the same 6 litres.",
        "options": [
            {"text": "A folded sheet of that volume would simply have "
                     "too little total area.",
             "correct": False,
             "why": "Area is not the obstacle — a sheet can be folded "
                    "to give any area within a fixed volume."},
            {"text": "Branching sacs reach every point with a "
                     "capillary; a giant sheet needs an equally vast "
                     "supply reaching every point.",
             "correct": True},
            {"text": "Branching exists only to filter the air, not to "
                     "help exchange.",
             "correct": False,
             "why": "Filtering happens much higher up the airway. "
                    "Branching here is entirely about supplying a "
                    "surface."},
            {"text": "A folded sheet also lets gas cross both of its "
                     "own faces at once, a genuine advantage over "
                     "branching sacs which never do.",
             "correct": False,
             "why": "Whatever the shape, each patch still needs its own "
                    "fresh air and blood — folding does not solve that."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h23",
        "band": "harder",
        "text": "A villus wall is one cell thick with a capillary "
                "immediately behind it; an alveolus crosses both its own "
                "wall and the capillary's, one cell each. Is the "
                "alveolus's total distance longer, shorter or about the "
                "same as the villus's?",
        "options": [
            {"text": "Far shorter, since alveoli are smaller structures "
                     "overall than villi.",
             "correct": False,
             "why": "Overall structure size is not what distance "
                    "measures — it is the wall thickness a gas crosses."},
            {"text": "It cannot really be compared at all, since a "
                     "villus absorbs dissolved food rather than a gas of "
                     "any kind.",
             "correct": False,
             "why": "What is absorbed does not stop the two distances "
                    "being compared, both measured in cell layers."},
            {"text": "Far longer overall, since crossing two separate "
                     "cell walls always takes many times longer than "
                     "crossing only one.",
             "correct": False,
             "why": "Two one-cell walls are still an extremely short "
                    "distance, nothing like the leap this suggests."},
            {"text": "About the same order — both are one-cell-thick "
                     "layers, even though the alveolus crosses two.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h24",
        "band": "harder",
        "text": "A colleague argues: “A cold patient's blood exchanges "
                "gas more slowly at the alveoli, because cold slows "
                "diffusion.” Using only the concentration-difference "
                "model, is that argument sound?",
        "options": [
            {"text": "Sound, since the model states outright and "
                     "explicitly that colder blood diffuses gases far "
                     "more slowly.",
             "correct": False,
             "why": "The model never mentions temperature at all — "
                    "every state in it is expressed only in kPa "
                    "differences."},
            {"text": "Unsound, since the model proves temperature has "
                     "no effect on diffusion anywhere.",
             "correct": False,
             "why": "The model never mentions temperature — absence of "
                    "a claim is not a claim of no effect."},
            {"text": "It cannot really be judged at all, since "
                     "soundness only ever applies to mathematical "
                     "statements.",
             "correct": False,
             "why": "A scientific argument can be judged sound or not "
                    "by asking whether it is actually supported."},
            {"text": "Not earned by that model — it runs entirely on "
                     "concentration difference, never on temperature.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h25",
        "band": "harder",
        "text": "The model used here never gives the total volume of "
                "blood inside the pulmonary capillaries at once. A student "
                "concludes blood volume plays no part in gas exchange "
                "there. Evaluate this.",
        "options": [
            {"text": "It follows correctly — only surface area, "
                     "distance, concentration difference and moisture are "
                     "ever said to matter here.",
             "correct": False,
             "why": "Blood flow is exactly what maintains the third of "
                    "those four requirements, described in words "
                    "throughout."},
            {"text": "It does not follow, but only because volume and "
                     "flow are actually the same quantity.",
             "correct": False,
             "why": "Volume and flow differ — a fixed amount sitting "
                    "still is a volume; flow is that blood moving."},
            {"text": "It follows correctly — anything given no exact "
                     "figure plays no part in a model's science.",
             "correct": False,
             "why": "Many things matter without a number here — blood "
                    "flow's importance is described only in words."},
            {"text": "It does not follow — blood FLOW, not standing "
                     "volume, is what maintains a difference, whether "
                     "or not it is quantified.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h26",
        "band": "harder",
        "text": "A ventilator alarm sounds “gas exchange has stopped” "
                "after ten seconds of zero air movement. Explain "
                "why the alarm's logic could be wrong "
                "for a few more seconds.",
        "options": [
            {"text": "The alarm is never wrong at all, since breathing "
                     "and gas exchange are really just the same single "
                     "process.",
             "correct": False,
             "why": "This lesson treats them as different processes — "
                    "breathing moves air; exchange is the diffusion that "
                    "follows."},
            {"text": "The existing alveolar difference persists "
                     "briefly, so net absorption does not fall to zero "
                     "instantly.",
             "correct": True},
            {"text": "Blood flow alone can refresh the alveolar air "
                     "even with no breathing at all.",
             "correct": False,
             "why": "Blood flow acts on the blood side, not on "
                    "refreshing the air — the existing air difference is "
                    "what persists."},
            {"text": "The alarm is only wrong if the patient held their "
                     "breath deliberately.",
             "correct": False,
             "why": "Why exchange continues briefly is about what is "
                    "already in the alveoli, not who caused the stop."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h27",
        "band": "harder",
        "text": "Using net = 90 × concentration difference, what "
                "difference is needed to produce a net absorption of 990 "
                "molecules per second?",
        "options": [
            {"text": "11 kPa.",
             "correct": True},
            {"text": "9 kPa.",
             "correct": False,
             "why": "90 multiplied by 9 gives 810, not 990."},
            {"text": "900 kPa.",
             "correct": False,
             "why": "This multiplies rather than divides — the "
                    "difference is 990 divided by 90."},
            {"text": "89100 kPa.",
             "correct": False,
             "why": "This multiplies 990 by 90 instead of dividing by "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h28",
        "band": "harder",
        "text": "Imagine a material giving 180 crossings per kPa per "
                "second, double the bench's actual 90. Using the “both "
                "flows running” state (13.3 and 5.3 kPa), predict the "
                "new net, and whether the rest of the body receives "
                "double the oxygen.",
        "options": [
            {"text": "New net 1440, and this alone fully guarantees "
                     "double the oxygen finally delivered to the rest of "
                     "the body.",
             "correct": False,
             "why": "Doubling crossing speed at the alveoli does not "
                    "double delivery elsewhere — blood flow, unchanged "
                    "here, still carries it away."},
            {"text": "New net 720, unchanged from the original "
                     "calculation.",
             "correct": False,
             "why": "Doubling the constant doubles the net figure too, "
                    "from 720 to 1440."},
            {"text": "New net 1440; but unchanged blood flow may now be "
                     "the limiting step delivering it onward.",
             "correct": True},
            {"text": "It cannot be calculated without also doubling the "
                     "surface area.",
             "correct": False,
             "why": "The rule only needs the constant and the "
                    "difference — surface area plays no part here."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h29",
        "band": "harder",
        "text": "A patient's restricted chest wall movement means each "
                "breath moves far less air, though their alveoli and "
                "capillaries are entirely healthy. Which requirement is "
                "most directly threatened, and which is unaffected?",
        "options": [
            {"text": "Surface area is threatened, since restricted "
                     "breathing directly shrinks the alveoli.",
             "correct": False,
             "why": "The alveoli are stated healthy, and breathing does "
                    "not shrink them physically."},
            {"text": "All four are equally threatened, since restricted "
                     "breathing damages the whole system.",
             "correct": False,
             "why": "The alveoli and capillaries are explicitly "
                    "healthy — the structural requirements are intact."},
            {"text": "Moisture is threatened, since slower breathing "
                     "lets the lining dry out.",
             "correct": False,
             "why": "Nothing about restricted movement removes the "
                    "liquid film — that is maintained regardless."},
            {"text": "A maintained difference is threatened; area, "
                     "distance and moisture are structural and "
                     "unaffected.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h30",
        "band": "harder",
        "text": "A student notices the small intestine crosses one cell "
                "layer while the lungs cross two, and concludes the "
                "intestine must absorb faster OVERALL. Evaluate this.",
        "options": [
            {"text": "Fair, since one layer always beats two whatever "
                     "else differs between the organs.",
             "correct": False,
             "why": "Layer count is only one factor — far more alveolar "
                    "surface and two active flows can outweigh it."},
            {"text": "Fair, but only because the intestine also has a "
                     "larger total surface area.",
             "correct": False,
             "why": "The lungs' 70 m² is considerably larger than the "
                    "intestine's roughly 30 m², the opposite of this "
                    "claim."},
            {"text": "Not fair — speed depends on area, difference and "
                     "the amount to move, not layer count alone.",
             "correct": True},
            {"text": "It cannot be evaluated, since absorbing food and "
                     "exchanging gas cannot be compared for speed.",
             "correct": False,
             "why": "Both are diffusion following a difference across a "
                    "wall, which is exactly what a fair comparison "
                    "needs."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h31",
        "band": "harder",
        "text": "During a breath-hold, a diver's blood oxygen falls "
                "steadily even though their lungs still hold plenty of "
                "air. Explain why air remaining does not mean exchange "
                "is still working at full effect.",
        "options": [
            {"text": "Holding a breath blocks diffusion from happening "
                     "at all.",
             "correct": False,
             "why": "Diffusion needs no permission and cannot be "
                    "blocked — it continues using whatever difference "
                    "exists."},
            {"text": "Blood keeps taking oxygen with no fresh air "
                     "arriving, so the alveolar level itself falls over "
                     "time.",
             "correct": True},
            {"text": "Exchange there is working exactly as usual; the "
                     "fall comes from elsewhere in the body.",
             "correct": False,
             "why": "If exchange there were unchanged, the alveolar "
                    "level would not be falling — the fall is direct "
                    "evidence it is slowing."},
            {"text": "The falling oxygen is caused entirely by muscles "
                     "using it up, unrelated to the alveoli.",
             "correct": False,
             "why": "Muscle use alone would not explain a falling "
                    "reading AT the alveoli, which is what is happening "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "b4-03-h32",
        "band": "harder",
        "text": "A textbook lists the four requirements in a fixed "
                "order, 1 to 4. A student says the numbering is only an "
                "order of listing, and which one matters most depends on "
                "what has gone wrong. Using the emphysema and "
                "premature-baby cases, evaluate that.",
        "options": [
            {"text": "No — both cases are ultimately surface-area "
                     "problems, confirming requirement 1 matters most.",
             "correct": False,
             "why": "The premature baby's problem is surface tension in "
                    "the moist lining, not a lack of area at all."},
            {"text": "No — the baby's case is really about distance, "
                     "since a stuck alveolus blocks the gas's path.",
             "correct": False,
             "why": "The problem is whether the alveolus opens at all, "
                    "caused by surface tension — a requirement-4 issue."},
            {"text": "Yes — area is what has failed in emphysema, and "
                     "moisture is what has failed for the baby.",
             "correct": True},
            {"text": "Yes — but only because the two cases are actually "
                     "the same underlying problem.",
             "correct": False,
             "why": "They are different failures: lost area in one, a "
                    "surface-tension problem in the moist lining in the "
                    "other."},
        ],
        "figure": None,
    },
]
