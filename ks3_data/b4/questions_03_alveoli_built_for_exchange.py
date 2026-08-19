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
    {
        "id": "b4-03-e04",
        "band": "easier",
        "text": "Roughly how much gas exchange surface do your alveoli give "
                "you in total?",
        "options": [
            {"text": "About 70 cm², roughly the area of a page in your "
                     "book.",
             "correct": False,
             "why": "Out by a factor of about ten thousand. Seventy square "
                    "metres is closer to a third of a tennis court than to a "
                    "page."},
            {"text": "About 30 m², the same as the lining of the small "
                     "intestine.",
             "correct": False,
             "why": "30 m² is the gut's figure, spread through six metres of "
                    "tube. The lungs fit more than twice that area into a far "
                    "smaller space."},
            {"text": "About 6 litres — the volume of air the chest can "
                     "hold.",
             "correct": False,
             "why": "Six litres is a volume, not a surface, and that is the "
                    "swap the hook is built to catch. The smooth bag holds the "
                    "same volume and would kill you in minutes."},
            {"text": "About 70 m², packed inside a chest of only six litres.",
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
]
