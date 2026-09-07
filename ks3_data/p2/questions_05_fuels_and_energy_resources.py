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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-05-e05",
        "band": "easier",
        "text": "Which of these is a renewable energy resource?",
        "options": [
            {"text": "Coal", "correct": False,
             "why": "Coal took hundreds of millions of years to form, so the "
                    "store does not refill on any human timescale."},
            {"text": "Wind", "correct": True},
            {"text": "Natural gas", "correct": False,
             "why": "Gas formed over geological time as well, and burning it "
                    "empties a store that is not replaced."},
            {"text": "Uranium", "correct": False,
             "why": "Uranium is mined and used up. It is low-carbon, which is "
                    "a different question from renewable."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e06",
        "band": "easier",
        "text": "What does intermittent mean, applied to an energy resource?",
        "options": [
            {"text": "It runs out after a fixed number of years",
             "correct": False,
             "why": "That is what non-renewable means. Intermittent is about "
                    "availability day to day."},
            {"text": "It releases its energy in sudden bursts",
             "correct": False,
             "why": "The bursts are not the point; being unavailable when you "
                    "want it is."},
            {"text": "It is available only sometimes, and not when you "
                     "choose",
             "correct": True},
            {"text": "It produces only a small amount of energy",
             "correct": False,
             "why": "Wind farms produce a great deal. How MUCH is a different "
                    "question from WHEN."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e07",
        "band": "easier",
        "text": "Which of these is renewable but still produces smoke and "
                "carbon dioxide when it is used?",
        "options": [
            {"text": "Solar", "correct": False,
             "why": "A solar panel burns nothing at all while it is "
                    "generating."},
            {"text": "Wind", "correct": False,
             "why": "A turbine burns nothing while it turns, so there is "
                    "nothing to smoke."},
            {"text": "Nuclear", "correct": False,
             "why": "Nuclear is low-carbon, but it is non-renewable, so it "
                    "fails the first half of the question."},
            {"text": "Wood", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e08",
        "band": "easier",
        "text": "Why is electricity not an energy resource?",
        "options": [
            {"text": "Because it is a pathway that carries energy from a "
                     "resource",
             "correct": True},
            {"text": "Because it runs out too quickly to count as one",
             "correct": False,
             "why": "Running out is not the test. Electricity holds nothing "
                    "in the first place."},
            {"text": "Because it is generated in too many different ways",
             "correct": False,
             "why": "Being generated many ways is a consequence of it being a "
                    "pathway, not the reason."},
            {"text": "Because it cannot be measured in joules",
             "correct": False,
             "why": "The energy it carries is measured in joules perfectly "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e09",
        "band": "easier",
        "text": "What does biomass mean?",
        "options": [
            {"text": "The mass of a power station's fuel store",
             "correct": False,
             "why": "It is a kind of fuel, not a measurement of how much fuel "
                    "there is."},
            {"text": "Fuel grown recently — wood, crops or waste",
             "correct": True},
            {"text": "Any fuel that produces no carbon dioxide",
             "correct": False,
             "why": "Biomass burns and does release carbon dioxide; being "
                    "recently grown is what defines it."},
            {"text": "The energy stored inside the nucleus of an atom",
             "correct": False,
             "why": "That is nuclear fuel, which is neither grown nor "
                    "renewable."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e10",
        "band": "easier",
        "text": "Which question does the word renewable answer?",
        "options": [
            {"text": "How much carbon dioxide the resource releases",
             "correct": False,
             "why": "Carbon is a separate question, and the answers do not "
                    "line up with renewable."},
            {"text": "Whether the resource is available whenever it is "
                     "wanted",
             "correct": False,
             "why": "That is reliability. Wind is renewable and often "
                    "unavailable."},
            {"text": "How much land the resource takes up", "correct": False,
             "why": "Land use is another separate question — hydroelectricity "
                    "is renewable and takes a great deal."},
            {"text": "Whether the store refills on a human timescale",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-05-s05",
        "band": "standard",
        "text": "A student says nuclear cannot be low-carbon because it is "
                "non-renewable. What has gone wrong in the reasoning?",
        "options": [
            {"text": "Nothing — non-renewable resources always release a lot "
                     "of carbon",
             "correct": False,
             "why": "Nuclear is the counter-example: non-renewable and among "
                    "the lowest-carbon of all."},
            {"text": "Two separate questions have been treated as one",
             "correct": True},
            {"text": "Nuclear is in fact renewable, so the premise is wrong",
             "correct": False,
             "why": "Uranium is mined and used up, so the premise about "
                    "renewability is right — the link is not."},
            {"text": "Carbon dioxide is not released by burning anything",
             "correct": False,
             "why": "Burning fuels certainly does release it; nuclear simply "
                    "burns nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s06",
        "band": "standard",
        "text": "Why is gas often kept on a grid that already has a lot of "
                "wind and solar?",
        "options": [
            {"text": "Because gas is cheaper than any renewable resource",
             "correct": False,
             "why": "Price varies and is not why it is kept; being available "
                    "on demand is."},
            {"text": "Because wind and solar cannot be measured accurately "
                     "enough to plan with",
             "correct": False,
             "why": "Both are forecast in detail. The problem is that the "
                    "forecast sometimes says there will be none."},
            {"text": "Because gas can be turned up when the wind drops",
             "correct": True},
            {"text": "Because wind and solar release carbon dioxide as they "
                     "generate",
             "correct": False,
             "why": "Neither releases any while generating, so that is not "
                    "the reason for the pairing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s07",
        "band": "standard",
        "text": "A wind farm generates nothing on a still day. Which word "
                "describes that?",
        "options": [
            {"text": "Non-renewable, because it has run out for the day",
             "correct": False,
             "why": "Nothing has run out — the wind will return, which is "
                    "exactly why it is renewable."},
            {"text": "Intermittent, because the supply comes and goes",
             "correct": True},
            {"text": "Inefficient, because it wastes the energy it could have "
                     "made",
             "correct": False,
             "why": "There is nothing to waste when there is no wind; "
                    "efficiency is a different measure."},
            {"text": "Dissipated, because the energy has spread out",
             "correct": False,
             "why": "Dissipation is about energy spreading into thermal "
                    "stores, not about a resource being unavailable."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s08",
        "band": "standard",
        "text": "Which pair of statements about hydroelectricity is right?",
        "options": [
            {"text": "Renewable and reliable, but it floods a great deal of "
                     "land",
             "correct": True},
            {"text": "Renewable and low-impact, because water is returned to "
                     "the river",
             "correct": False,
             "why": "The water is returned, but a reservoir permanently "
                    "floods the valley behind the dam."},
            {"text": "Non-renewable, because a reservoir eventually empties",
             "correct": False,
             "why": "Rain refills it, which is what makes the resource "
                    "renewable."},
            {"text": "Renewable but intermittent, like wind and solar",
             "correct": False,
             "why": "A reservoir can be released on demand, so it is one of "
                    "the reliable renewables."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s09",
        "band": "standard",
        "text": "Two resources are described as low-carbon while generating. "
                "Which pair fits?",
        "options": [
            {"text": "Coal and wood", "correct": False,
             "why": "Both are burnt, and both release carbon dioxide as they "
                    "generate."},
            {"text": "Gas and biomass", "correct": False,
             "why": "Gas and biomass are both burnt, so neither is low-carbon "
                    "at the point of generating."},
            {"text": "Nuclear and solar", "correct": True},
            {"text": "Wood and solar", "correct": False,
             "why": "Solar qualifies, but wood is burnt and smokes — that is "
                    "the classic renewable-is-not-clean case."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s10",
        "band": "standard",
        "text": "Which store does a hydroelectric dam empty as it generates?",
        "options": [
            {"text": "The chemical store of the water", "correct": False,
             "why": "Nothing chemical happens; the water is unchanged after "
                    "it passes through."},
            {"text": "The gravitational store of the water held high up",
             "correct": True},
            {"text": "The thermal store of the reservoir", "correct": False,
             "why": "The water's temperature barely changes; the height it "
                    "falls through is what is used."},
            {"text": "The nuclear store inside the water's atoms",
             "correct": False,
             "why": "That store is untouched — a dam splits no nuclei."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-05-h05",
        "band": "harder",
        "text": "Wood and nuclear sit in opposite corners of the "
                "renewable-and-clean grid. What does that pair show?",
        "options": [
            {"text": "That the grid has been drawn wrongly, since both "
                     "corners cannot be real",
             "correct": False,
             "why": "Both corners are occupied by real resources, which is "
                    "the point of drawing it."},
            {"text": "That renewable and low-carbon are separate properties "
                     "that need not agree",
             "correct": True},
            {"text": "That wood is a better resource than nuclear",
             "correct": False,
             "why": "The grid ranks nothing; it shows the two questions come "
                    "apart."},
            {"text": "That nuclear will one day be classed as renewable",
             "correct": False,
             "why": "Uranium is still mined and used up, whatever else is "
                    "true of it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h06",
        "band": "harder",
        "text": "A grid with many wind farms builds an enormous battery "
                "store beside them. Which problem is that meant to solve?",
        "options": [
            {"text": "That wind is intermittent, so windy hours have to "
                     "supply still ones",
             "correct": True},
            {"text": "That wind is non-renewable, so the supply has to be "
                     "rationed",
             "correct": False,
             "why": "Wind refills continuously; storing it is about timing, "
                    "not about running out."},
            {"text": "That wind turbines release carbon dioxide that has to "
                     "be captured",
             "correct": False,
             "why": "A turbine releases none while it turns, and a battery "
                    "captures nothing anyway."},
            {"text": "That wind farms take up land that could be farmed",
             "correct": False,
             "why": "Land use is a real issue, but a battery does nothing "
                    "about how much land the turbines stand on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h07",
        "band": "harder",
        "text": "Which resource does NOT trace its energy back to the Sun?",
        "options": [
            {"text": "Wind, which is driven by uneven heating of the air",
             "correct": False,
             "why": "That uneven heating is sunlight, so wind traces straight "
                    "back to the Sun."},
            {"text": "Coal, formed from plants that grew long ago",
             "correct": False,
             "why": "Those plants photosynthesised, so the store began as "
                    "sunlight."},
            {"text": "Hydroelectricity, from rain that fell on high ground",
             "correct": False,
             "why": "The Sun evaporated that water and lifted it, so this "
                    "traces back too."},
            {"text": "Nuclear, from uranium formed before the Sun existed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h08",
        "band": "harder",
        "text": "Burning wood releases carbon dioxide, yet it is sometimes "
                "called carbon-neutral. What is the argument, and its "
                "weakness?",
        "options": [
            {"text": "Wood releases no carbon dioxide at all, so the label is "
                     "simply correct",
             "correct": False,
             "why": "It certainly does release it — that is why the argument "
                    "has to be made at all."},
            {"text": "The tree absorbed that carbon as it grew, but a "
                     "replacement takes decades",
             "correct": True},
            {"text": "The carbon dioxide is captured at the chimney, so none "
                     "reaches the air",
             "correct": False,
             "why": "Capture is a separate technology and is not what the "
                    "carbon-neutral claim rests on."},
            {"text": "Wood burns at a lower temperature, so less carbon "
                     "dioxide forms",
             "correct": False,
             "why": "Temperature does not change how much carbon the wood "
                    "contained in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h09",
        "band": "harder",
        "text": "Why does the lesson refuse to name one best energy "
                "resource?",
        "options": [
            {"text": "Because too little is known about any of them to "
                     "compare",
             "correct": False,
             "why": "A great deal is known about all of them; the difficulty "
                    "is that they are good at different things."},
            {"text": "Because the answers are political and science has "
                     "nothing to say",
             "correct": False,
             "why": "Science supplies the carbon, land and reliability "
                    "figures the decision rests on."},
            {"text": "Because best depends on which of several separate "
                     "questions you are asking",
             "correct": True},
            {"text": "Because the best resource has not yet been invented",
             "correct": False,
             "why": "The refusal is about the ones we have, not about waiting "
                    "for a new one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h10",
        "band": "harder",
        "text": "A island wants power that is renewable, low-carbon AND "
                "available on demand. Which is the best fit?",
        "options": [
            {"text": "Solar, because sunlight is free and endless",
             "correct": False,
             "why": "It fails the last test: nothing is generated at night, "
                    "however endless the supply."},
            {"text": "Gas, because it can be turned up whenever it is wanted",
             "correct": False,
             "why": "It meets the demand test and fails the other two — gas "
                    "is neither renewable nor low-carbon."},
            {"text": "Wind, because turbines run day and night",
             "correct": False,
             "why": "They run only while the wind blows, so the on-demand "
                    "test is the one it fails."},
            {"text": "Hydroelectricity, if the island has the high ground for "
                     "it",
             "correct": True},
        ],
        "figure": None,
    },
]
