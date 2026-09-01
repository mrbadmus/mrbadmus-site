"""P2 lesson 05 — Fuels and energy resources: twelve questions (MRB-223).

Written against Design's page. The eight resources, the three axes and the
two "impossible" corners are hers, and both corners are kept unsoftened
here for the same reason they are kept on the page: they are the only
evidence that kills the belief.

The discriminations:

  · "renewable" answers ONE question — will the store refill? — and
    nothing else (`ENER-27`);
  · nuclear is finite and low-carbon; wood is renewable and high-carbon.
    Between them they occupy the two cells the misconception says are
    empty, and most of this bank turns on one or the other;
  · every axis reorders the ranking, so there is no best resource;
  · electricity is a PATHWAY, not a resource (`ENER-10`, re-confronted).

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 ("what does it mean to call a resource renewable?") and Rung 2
(the non-renewable low-carbon one) are NOT restated; check 6 of
`verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P2"
LESSON = "fuels-and-energy-resources"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p2-05-e01",
        "band": "easier",
        "text": "Which of these is a non-renewable energy resource?",
        "options": [
            {"text": "Wind", "correct": False,
             "why": "The air keeps moving as long as the Sun keeps heating "
                    "it unevenly. Wind does not run out."},
            {"text": "Coal", "correct": True},
            {"text": "Tidal", "correct": False,
             "why": "The tides come from the Moon's gravity and will keep "
                    "coming."},
            {"text": "Hydroelectric", "correct": False,
             "why": "The Sun keeps lifting water into the sky, so the "
                    "reservoir keeps refilling."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e02",
        "band": "easier",
        "text": "What store does the wind hold its energy in?",
        "options": [
            {"text": "A chemical store", "correct": False,
             "why": "Nothing is being burned or rearranged. Chemical stores "
                    "are fuels, food and batteries."},
            {"text": "A kinetic store", "correct": True},
            {"text": "A thermal store", "correct": False,
             "why": "The Sun's heating is what CAUSES the wind, but what the "
                    "turbine takes from is the movement itself."},
            {"text": "A nuclear store", "correct": False,
             "why": "Nuclear stores sit inside heavy atoms, not in moving "
                    "air."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e03",
        "band": "easier",
        "text": "Which resource is renewable but still releases a great deal "
                "of carbon dioxide when used?",
        "options": [
            {"text": "Solar power", "correct": False,
             "why": "Solar releases almost nothing while generating."},
            {"text": "Nuclear power", "correct": False,
             "why": "Nuclear is low-carbon, but it is not renewable — uranium "
                    "does not refill."},
            {"text": "Wood and biomass", "correct": True},
            {"text": "Tidal power", "correct": False,
             "why": "Tidal is renewable and low-carbon. Its costs are "
                    "elsewhere, in estuary habitats."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e04",
        "band": "easier",
        "text": "Is electricity an energy resource?",
        "options": [
            {"text": "No — it is a pathway that moves energy from a store to "
                     "where it is wanted",
             "correct": True},
            {"text": "Yes, and it is the cleanest of all the resources a "
                     "country can use",
             "correct": False,
             "why": "It is exactly as clean as whatever generated it, which "
                    "differs from country to country."},
            {"text": "Yes, and it is renewable because power stations keep on "
                     "making more of it",
             "correct": False,
             "why": "Making it always means emptying some other store. It is "
                    "not itself a store to refill."},
            {"text": "Yes, but only when it comes from a battery rather than "
                     "the mains",
             "correct": False,
             "why": "A battery holds a CHEMICAL store. The electricity is "
                    "still the pathway out of it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p2-05-s01",
        "band": "standard",
        "text": "A student says wind must be better than nuclear because "
                "wind is renewable. What has the argument missed?",
        "options": [
            {"text": "Nothing — being renewable is the only axis that "
                     "matters, so wind wins the comparison",
             "correct": False,
             "why": "The lesson's whole point is that it is one axis among "
                    "several, and the others disagree with it."},
            {"text": "That wind is not actually renewable, because a still "
                     "day leaves nothing to use",
             "correct": False,
             "why": "Wind is genuinely renewable — a still day is a supply "
                    "problem, not a running-out one. That is not the flaw."},
            {"text": "That renewability says nothing about whether the "
                     "resource is available when it is needed",
             "correct": True},
            {"text": "That nuclear is also renewable, because uranium can be "
                     "used again and again",
             "correct": False,
             "why": "Nuclear is not renewable — uranium is finite, and no "
                    "amount of reuse refills the ground. The point is that it "
                    "is low-carbon anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s02",
        "band": "standard",
        "text": "Which resource takes the most land and habitat, despite "
                "being renewable, low-carbon and reliable?",
        "options": [
            {"text": "Nuclear", "correct": False,
             "why": "Nuclear takes the LEAST land of anything on the grid, "
                    "and it is not renewable either."},
            {"text": "Solar", "correct": False,
             "why": "Solar takes a lot of land, but less than flooding a "
                    "valley, and it is not reliable on demand."},
            {"text": "Natural gas", "correct": False,
             "why": "Gas takes little land, and it is neither renewable nor "
                    "low-carbon."},
            {"text": "Hydroelectric", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s03",
        "band": "standard",
        "text": "Why is natural gas often used alongside wind and solar on a "
                "national grid?",
        "options": [
            {"text": "Because it can be switched on quickly when the wind "
                     "drops",
             "correct": True},
            {"text": "Because it is renewable, so the supply of it never runs "
                     "out",
             "correct": False,
             "why": "Gas is a fossil fuel and is finite."},
            {"text": "Because it produces no carbon dioxide when it is burned",
             "correct": False,
             "why": "It produces a substantial amount — around half that of "
                    "coal per unit, but far from none."},
            {"text": "Because wind turbines cannot work without gas to start "
                     "them",
             "correct": False,
             "why": "Turbines start and run perfectly well on their own. The "
                    "problem is what happens when the air is still."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s04",
        "band": "standard",
        "text": "Nuclear sits in the corner that “renewable means "
                "clean” says cannot exist. What is nuclear's real cost?",
        "options": [
            {"text": "The carbon dioxide it releases while generating",
             "correct": False,
             "why": "It releases essentially none while generating. That is "
                    "precisely why it occupies that corner."},
            {"text": "That the uranium runs out within a few years",
             "correct": False,
             "why": "It is finite, but on a scale of many decades, not "
                    "years — and running out is not the cost usually "
                    "argued about."},
            {"text": "That it cannot be switched on when it is needed",
             "correct": False,
             "why": "Nuclear is one of the most reliable resources on the "
                    "grid; wind and solar are the intermittent ones."},
            {"text": "Waste that stays dangerous for thousands of years",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p2-05-h01",
        "band": "harder",
        "text": "If “renewable” and “clean” meant the same "
                "thing, what would the two-axis grid look like?",
        "options": [
            {"text": "Every resource would sit at the same height",
             "correct": False,
             "why": "That would mean carbon did not vary at all, which is a "
                    "different claim again."},
            {"text": "Two opposite corners would be empty, with everything "
                     "on one diagonal",
             "correct": True},
            {"text": "The grid would need only one axis, and every resource "
                     "would be renewable",
             "correct": False,
             "why": "One axis would do, but nothing would make every "
                    "resource renewable — coal would still be finite."},
            {"text": "Nothing would change; the grid already looks that way",
             "correct": False,
             "why": "It does not. Nuclear and wood both sit in cells the "
                    "belief says are impossible."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h02",
        "band": "harder",
        "text": "A country plans to run entirely on wind and solar. What is "
                "the strongest practical objection?",
        "options": [
            {"text": "That wind and solar release too much carbon dioxide "
                     "while they are generating",
             "correct": False,
             "why": "Both are among the lowest-carbon options there are."},
            {"text": "That wind and solar will eventually run out, just as a "
                     "fossil fuel does",
             "correct": False,
             "why": "Both are renewable. Running out is not the problem."},
            {"text": "That demand does not fall when the wind drops, so "
                     "something must cover the gap",
             "correct": True},
            {"text": "That they take up far less land than a fossil-fuel "
                     "station would need",
             "correct": False,
             "why": "They take up MORE land, and in any case that would be a "
                    "point in favour if it were true."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h03",
        "band": "harder",
        "text": "Almost every resource on the grid traces back to the Sun. "
                "Which three do not?",
        "options": [
            {"text": "Coal, oil and gas", "correct": False,
             "why": "All three are ancient sunlight — forests and "
                    "plankton that photosynthesised and never fully "
                    "rotted."},
            {"text": "Wind, hydroelectric and biomass", "correct": False,
             "why": "All three are sunlight with a short delay: uneven "
                    "heating, evaporated water and this decade's growth."},
            {"text": "Solar, wind and tidal", "correct": False,
             "why": "Solar and wind are both the Sun. Only tidal belongs on "
                    "this list."},
            {"text": "Geothermal, tidal and nuclear", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h04",
        "band": "harder",
        "text": "The lesson refuses to name a best energy resource. What is "
                "the strongest reason for that refusal?",
        "options": [
            {"text": "Because the axes disagree, so any single winner depends "
                     "on which axis you stopped counting at",
             "correct": True},
            {"text": "Because the science behind each of the axes is not yet "
                     "settled enough to name a winner",
             "correct": False,
             "why": "The science on each axis is reasonably clear. It is the "
                    "combining of them that has no single answer."},
            {"text": "Because naming a winner would be a political statement "
                     "rather than a scientific judgement",
             "correct": False,
             "why": "Closer, but it dodges the actual structure: even with no "
                    "politics at all, three orderings that disagree cannot "
                    "produce one winner."},
            {"text": "Because every resource turns out to be about equally "
                     "good once all the axes are added up",
             "correct": False,
             "why": "They are not equal — they differ sharply, just not in "
                    "the same direction on every axis."},
        ],
        "figure": None,
    },
]
