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

⊕ MRB-338 night 3 — topped up to 30/30/30 (e11–e30, s11–s30, h11–h30),
appended, with the original thirty untouched in place. The new rows go
WIDER rather than round again: the per-resource stores, the three axis
orderings read off one at a time, where each resource's energy started
(Carboniferous forest, plankton, the Moon, the mantle, exploding stars),
the costs that are not carbon — particulates, waste, flooded valleys,
estuaries, farmland lost to fuel crops — and the evaluations a country
actually faces.

⚠️ The leaf arrived carrying a rank-spread failure: length rank 1 held
50.0% of its thirty keys, over the 40% ceiling. The thirty are frozen and
append-only, so the sixty new rows were weighted deliberately away from
rank 1 (11 of 60) to dilute it. The leaf now reads 28.9 / 27.8 / 23.3 /
20.0 across ranks 1–4.
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
            {"text": "It runs out after a fixed number of years and cannot be "
                     "used again",
             "correct": False,
             "why": "That is what non-renewable means. Intermittent is about "
                    "availability day to day."},
            {"text": "It releases its energy in sudden bursts",
             "correct": False,
             "why": "The bursts are not the point; being unavailable when you "
                    "want it is."},
            {"text": "It is available only sometimes, not when you choose",
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

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-05-e11",
        "band": "easier",
        "text": "Which store does coal hold its energy in before it is burned?",
        "options": [
            {"text": "A chemical store", "correct": True},
            {"text": "A gravitational store", "correct": False,
             "why": "Gravitational stores are things held high up, such as the "
                    "water behind a dam."},
            {"text": "A nuclear store", "correct": False,
             "why": "Nuclear stores sit inside heavy atoms such as uranium, "
                    "not inside coal."},
            {"text": "A kinetic store", "correct": False,
             "why": "Coal in a heap is not moving, and movement is not what "
                    "burning it releases."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e12",
        "band": "easier",
        "text": "Where does the energy in the tides come from?",
        "options": [
            {"text": "The Sun's heat lifting water into the sky",
             "correct": False,
             "why": "That is where the water behind a hydroelectric dam comes "
                    "from, not the tide."},
            {"text": "The Moon's gravity pulling the oceans", "correct": True},
            {"text": "Heat left over from the Earth's formation",
             "correct": False,
             "why": "That heat is what geothermal power uses, and it does not "
                    "move the sea."},
            {"text": "The Earth's rotation alone", "correct": False,
             "why": "Rotation sets the timing of the tides, but the pull that "
                    "raises them comes from the Moon."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e13",
        "band": "easier",
        "text": "A solar panel takes its energy from what?",
        "options": [
            {"text": "The warm air around the panel", "correct": False,
             "why": "A panel works from light falling on it, not from the "
                    "warmth of the air."},
            {"text": "The chemical store inside the panel", "correct": False,
             "why": "Nothing inside a panel is burnt or rearranged while it "
                    "generates."},
            {"text": "Radiation from the Sun", "correct": True},
            {"text": "A thermal store built up overnight", "correct": False,
             "why": "A panel stores nothing overnight; it generates only while "
                    "light is falling on it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e14",
        "band": "easier",
        "text": "Which of these empties a nuclear store?",
        "options": [
            {"text": "Water falling through a dam", "correct": False,
             "why": "That empties a gravitational store, which is a different "
                    "store altogether."},
            {"text": "Coal burning in a furnace", "correct": False,
             "why": "Burning coal empties a chemical store, and no nuclei are "
                    "split doing it."},
            {"text": "Wind turning a turbine", "correct": False,
             "why": "Moving air is a kinetic store, and that is what a turbine "
                    "takes from."},
            {"text": "Uranium inside a reactor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e15",
        "band": "easier",
        "text": "Roughly how long ago did the forests that became coal grow?",
        "options": [
            {"text": "About three hundred million years ago", "correct": True},
            {"text": "About three thousand years ago", "correct": False,
             "why": "Three thousand years is nothing on this scale, and no "
                    "forest turns to coal in it."},
            {"text": "About three million years ago", "correct": False,
             "why": "Too recent by a factor of about a hundred, which is why "
                    "coal cannot refill."},
            {"text": "Within the last hundred years", "correct": False,
             "why": "Wood grown this century is biomass, and biomass is the "
                    "renewable case."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e16",
        "band": "easier",
        "text": "Crude oil formed from the remains of what?",
        "options": [
            {"text": "Trees that fell into swamps and never rotted",
             "correct": False,
             "why": "That is how coal formed. Oil began out at sea instead."},
            {"text": "Tiny sea creatures called plankton", "correct": True},
            {"text": "Volcanic rock from deep underground", "correct": False,
             "why": "Rock holds no chemical store of this kind, and oil is not "
                    "volcanic in origin."},
            {"text": "Salt from seas that dried up", "correct": False,
             "why": "Dried seas leave beds of salt, which burn nothing and "
                    "store nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e17",
        "band": "easier",
        "text": "Which of these takes up the least land and habitat?",
        "options": [
            {"text": "A large biomass plantation", "correct": False,
             "why": "Growing fuel takes more land than anything else except "
                    "flooding a valley."},
            {"text": "A hydroelectric reservoir", "correct": False,
             "why": "A dam floods a whole valley, the largest land cost on the "
                    "grid."},
            {"text": "A nuclear station", "correct": True},
            {"text": "A solar farm on open ground", "correct": False,
             "why": "Panels have to be spread over a wide area to catch enough "
                    "light."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e18",
        "band": "easier",
        "text": "Which resource sits highest on the carbon axis while it is "
                "generating?",
        "options": [
            {"text": "Natural gas", "correct": False,
             "why": "Gas releases about half the carbon of coal for each unit "
                    "of energy."},
            {"text": "Nuclear power", "correct": False,
             "why": "A generating nuclear station releases essentially no "
                    "carbon dioxide at all."},
            {"text": "Wood and biomass", "correct": False,
             "why": "Wood sits high on that axis, but coal sits higher "
                    "still."},
            {"text": "Coal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e19",
        "band": "easier",
        "text": "How does the carbon released by burning gas compare with "
                "burning coal, for each unit of energy?",
        "options": [
            {"text": "Roughly half as much", "correct": True},
            {"text": "Roughly the same amount", "correct": False,
             "why": "Gas is the cleaner of the two per unit, which is why "
                    "grids switched to it."},
            {"text": "Roughly twice as much", "correct": False,
             "why": "That reverses the comparison. Coal is the higher-carbon "
                    "fuel of the two."},
            {"text": "None at all", "correct": False,
             "why": "Gas is burnt, so it certainly releases carbon dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e20",
        "band": "easier",
        "text": "What makes the wind blow?",
        "options": [
            {"text": "The Moon pulling the atmosphere around with it as it "
                     "orbits the Earth",
             "correct": False,
             "why": "The Moon's pull raises tides in the sea. It does not "
                    "drive the weather."},
            {"text": "The Sun heating some parts of the atmosphere more than "
                     "others",
             "correct": True},
            {"text": "Heat rising out of the Earth's core and up "
                     "through the rock above", "correct": False,
             "why": "Geothermal heat warms rock and groundwater, not the "
                    "weather above it."},
            {"text": "The turning of wind turbines", "correct": False,
             "why": "Turbines take energy from the wind. They do not make "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e21",
        "band": "easier",
        "text": "Which two resources are intermittent?",
        "options": [
            {"text": "Coal and gas", "correct": False,
             "why": "Both can be switched on whenever they are wanted."},
            {"text": "Nuclear and hydroelectric", "correct": False,
             "why": "Both are available on demand, and a reservoir is released "
                    "when it is chosen."},
            {"text": "Wind and solar", "correct": True},
            {"text": "Tidal and nuclear", "correct": False,
             "why": "The tide comes and goes but is predictable, and nuclear "
                    "runs on demand."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e22",
        "band": "easier",
        "text": "For how long does nuclear waste stay dangerous?",
        "options": [
            {"text": "A few days", "correct": False,
             "why": "If it were days, storing it would not be the argument "
                    "that it is."},
            {"text": "A few months, until it is reprocessed", "correct": False,
             "why": "Reprocessing changes the form of the waste, not how long "
                    "it stays dangerous."},
            {"text": "About a hundred years", "correct": False,
             "why": "A century is far too short. The problem outlasts every "
                    "building we put it in."},
            {"text": "Thousands of years", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e23",
        "band": "easier",
        "text": "What is an energy resource?",
        "options": [
            {"text": "A store we can empty to do something useful",
             "correct": True},
            {"text": "Any device that runs on mains electricity",
             "correct": False,
             "why": "A device uses energy. A resource is where that energy "
                    "came from."},
            {"text": "A pathway that carries energy about", "correct": False,
             "why": "That describes electricity, which is a pathway and not a "
                    "resource."},
            {"text": "A unit that energy is measured in", "correct": False,
             "why": "Joules and kilowatt-hours are units. A resource is a "
                    "store."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e24",
        "band": "easier",
        "text": "Which renewable resource can be predicted to the minute, "
                "years in advance?",
        "options": [
            {"text": "Wind", "correct": False,
             "why": "Wind is forecast a few days ahead at best, and the "
                    "forecast is sometimes wrong."},
            {"text": "Tidal", "correct": True},
            {"text": "Solar", "correct": False,
             "why": "Sunrise is predictable, but cloud is not, so the output "
                    "is not either."},
            {"text": "Wood", "correct": False,
             "why": "Wood burns whenever it is fed into a furnace, so there is "
                    "nothing to predict."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e25",
        "band": "easier",
        "text": "The water behind a hydroelectric dam was lifted into the sky "
                "by what?",
        "options": [
            {"text": "The Moon's gravity, the same pull that raises the tides",
             "correct": False,
             "why": "The Moon raises the sea itself. It does not evaporate "
                    "water into cloud."},
            {"text": "Heat from radioactive decay far down inside the Earth",
             "correct": False,
             "why": "That heat warms rock and groundwater, and it is what "
                    "geothermal power uses."},
            {"text": "The Sun, which evaporated it into the clouds",
             "correct": True},
            {"text": "The turbines in the dam, which pumped it back up there",
             "correct": False,
             "why": "The turbines take energy out as the water falls, and "
                    "nothing in a dam lifts water into the sky."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e26",
        "band": "easier",
        "text": "Which resource means flooding a valley to build?",
        "options": [
            {"text": "A wind farm", "correct": False,
             "why": "Turbines stand on the ground, and the land between them "
                    "can still be farmed."},
            {"text": "A nuclear power station", "correct": False,
             "why": "A station sits on a small site and floods nothing at "
                    "all."},
            {"text": "A biomass plantation", "correct": False,
             "why": "A plantation takes a great deal of land, but it is "
                    "planted rather than flooded."},
            {"text": "A hydroelectric dam", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e27",
        "band": "easier",
        "text": "Is nuclear power renewable?",
        "options": [
            {"text": "No, because uranium is mined and used up",
             "correct": True},
            {"text": "Yes, because the same fuel rods are used again and "
                     "again",
             "correct": False,
             "why": "Rods are eventually spent and become waste. The uranium "
                    "never returns to the ground."},
            {"text": "Yes, because a reactor releases almost no carbon "
                     "dioxide",
             "correct": False,
             "why": "That is the carbon question, and it is separate from "
                    "whether the store refills."},
            {"text": "Yes, because a great deal of uranium is still left",
             "correct": False,
             "why": "How much is left is not the test. Whether the store "
                    "refills on a human timescale is."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e28",
        "band": "easier",
        "text": "Where does geothermal energy come from?",
        "options": [
            {"text": "Sunlight that has soaked down into the ground over many "
                     "thousands of summers",
             "correct": False,
             "why": "The Sun warms only the top few metres. Geothermal heat "
                    "comes from far deeper."},
            {"text": "Heat left from the Earth's formation and from "
                     "radioactive decay in the mantle",
             "correct": True},
            {"text": "Hot water pumped down from power stations",
             "correct": False,
             "why": "Nothing is pumped down. The heat is already there before "
                    "anyone drills."},
            {"text": "Friction as the Earth turns on its axis",
             "correct": False,
             "why": "Rotation does not heat the rock beneath us in any useful "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e29",
        "band": "easier",
        "text": "What is the main environmental cost of tidal power?",
        "options": [
            {"text": "The carbon dioxide released as the water turns the "
                     "turbines",
             "correct": False,
             "why": "Nothing is burnt in a barrage, so there is no carbon "
                    "dioxide to release."},
            {"text": "The waste it leaves behind, which stays dangerous for "
                     "centuries",
             "correct": False,
             "why": "That is the cost of nuclear power. A barrage leaves no "
                    "such waste at all."},
            {"text": "It disrupts the estuaries where a great deal lives",
             "correct": True},
            {"text": "The fuel that has to be shipped in", "correct": False,
             "why": "Tidal power needs no fuel. The Moon supplies the "
                    "movement for nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-e30",
        "band": "easier",
        "text": "Solar releases almost nothing while generating, so where does "
                "its carbon figure come from?",
        "options": [
            {"text": "From the sunlight itself, which carries carbon",
             "correct": False,
             "why": "Sunlight carries energy and nothing else. There is no "
                    "carbon in it."},
            {"text": "From the small amount of fuel a panel burns on a cloudy "
                     "day",
             "correct": False,
             "why": "A panel burns nothing at all, on a cloudy day or any "
                    "other."},
            {"text": "From the heat that the panels give off in the "
                     "summer months",
             "correct": False,
             "why": "Warm panels release heat, which is not the same thing as "
                    "carbon dioxide."},
            {"text": "From mining the materials and manufacturing the panels",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-05-s11",
        "band": "standard",
        "text": "Coal and wood both burn and both release carbon dioxide. "
                "What separates them when the grid is classified?",
        "options": [
            {"text": "Wood can be grown again within decades, while coal "
                     "cannot be replaced at all",
             "correct": True},
            {"text": "Wood releases no carbon dioxide at all once a "
                     "replacement tree has been planted",
             "correct": False,
             "why": "The carbon goes into the air the moment the wood burns, "
                    "whatever is planted afterwards."},
            {"text": "Coal releases its carbon slowly over many years, so it "
                     "does less harm each year",
             "correct": False,
             "why": "Coal releases its carbon as it burns, and it releases "
                    "more of it than wood does."},
            {"text": "Wood is burnt at a lower temperature, so it counts as "
                     "clean",
             "correct": False,
             "why": "Temperature decides neither whether a fuel is clean nor "
                    "whether it is renewable."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s12",
        "band": "standard",
        "text": "Tidal and wind are both renewable and both come and go. Why "
                "is tidal easier for a grid to plan around?",
        "options": [
            {"text": "Tidal power is available at every hour of the day and "
                     "night",
             "correct": False,
             "why": "A barrage generates only while the tide is running, which "
                    "is not every hour."},
            {"text": "The tides run to a timetable set by the Moon, so they "
                     "can be predicted years ahead",
             "correct": True},
            {"text": "Tidal power produces far more energy than any wind farm "
                     "can",
             "correct": False,
             "why": "How much it produces is a different question from when it "
                    "arrives."},
            {"text": "Tides are driven by the weather, and the weather is "
                     "forecast accurately many days ahead",
             "correct": False,
             "why": "Tides are driven by the Moon's gravity, and weather is "
                    "exactly what cannot be relied on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s13",
        "band": "standard",
        "text": "A resource is low on carbon, highest of all on land taken, "
                "and available on demand. Which is it?",
        "options": [
            {"text": "Solar, because the panels have to be spread over a "
                     "wide area",
             "correct": False,
             "why": "Solar is low-carbon and covers a lot of ground, but it is "
                    "not available on demand."},
            {"text": "Nuclear, because a reactor can run continuously for "
                     "months",
             "correct": False,
             "why": "Nuclear is low-carbon and runs on demand, but it takes "
                    "the least land of anything."},
            {"text": "Hydroelectric, because a reservoir floods a valley",
             "correct": True},
            {"text": "Natural gas, because it can be switched on whenever it "
                     "is wanted",
             "correct": False,
             "why": "Gas runs on demand and takes little land, and it is not "
                    "low-carbon at all."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s14",
        "band": "standard",
        "text": "Burning wood releases carbon dioxide, yet wood is classed as "
                "renewable. Why does the classification still hold?",
        "options": [
            {"text": "Because the carbon dioxide is reabsorbed before it "
                     "reaches the air",
             "correct": False,
             "why": "It reaches the air at once. Any reabsorbing happens "
                    "later, in a new tree."},
            {"text": "Because the amount released is too small to be worth "
                     "counting",
             "correct": False,
             "why": "Burning wood releases a great deal, more per unit of "
                    "energy than natural gas does."},
            {"text": "Because renewable describes any resource that grows "
                     "rather than one that is dug up",
             "correct": False,
             "why": "The test is whether the store refills on a human "
                    "timescale, not how it is gathered."},
            {"text": "Because the classification asks only whether the store "
                     "refills, and trees regrow",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s15",
        "band": "standard",
        "text": "Explain why a nuclear station takes far less land than a wind "
                "farm producing the same amount of electricity.",
        "options": [
            {"text": "A very large amount of energy comes out of a small mass "
                     "of uranium, so the site can be small",
             "correct": True},
            {"text": "Nuclear stations are built underground, so they take up "
                     "no land at the surface",
             "correct": False,
             "why": "Reactors are built at the surface. The buildings are "
                    "simply compact for what they produce."},
            {"text": "Wind farms have to be fenced off from the public for "
                     "safety reasons, and that is what takes up the land",
             "correct": False,
             "why": "Turbines are spread out to catch the wind, and the land "
                    "between them is still farmed."},
            {"text": "Nuclear stations are built on land that nobody else "
                     "wanted",
             "correct": False,
             "why": "Where a station is put does not change how much land it "
                    "needs."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s16",
        "band": "standard",
        "text": "Which statement compares coal and natural gas correctly?",
        "options": [
            {"text": "Coal releases less carbon per unit, but gas is quicker "
                     "to switch on",
             "correct": False,
             "why": "Coal is the higher-carbon of the two per unit, not the "
                    "lower."},
            {"text": "Gas releases about half the carbon per unit and is "
                     "quicker to switch on and off",
             "correct": True},
            {"text": "Both are renewable, since new coal and new gas are "
                     "still forming underground today",
             "correct": False,
             "why": "New fossil fuel forms far too slowly to count on any "
                    "human timescale."},
            {"text": "Gas is renewable and coal is not, and that is why the "
                     "grids switched over to gas",
             "correct": False,
             "why": "Gas is a finite fossil fuel. Grids switched for the lower "
                    "carbon, not for the supply."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s17",
        "band": "standard",
        "text": "A student says wind power is really a form of solar power. Is "
                "there anything in that?",
        "options": [
            {"text": "No, because the wind is raised by the Moon in exactly "
                     "the way that the tides are",
             "correct": False,
             "why": "The Moon raises tides in the sea. It does not set the air "
                    "moving."},
            {"text": "No, because wind and sunlight are separate resources "
                     "that have nothing whatever to do with each other",
             "correct": False,
             "why": "They are listed separately, but the wind is driven by the "
                    "Sun's uneven heating."},
            {"text": "Yes, because the Sun heats some parts of the atmosphere "
                     "more than others, and that moves the air",
             "correct": True},
            {"text": "Yes, because wind turbines have solar panels built into "
                     "them",
             "correct": False,
             "why": "Turbines carry no panels. The link lies in where the wind "
                    "itself comes from."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s18",
        "band": "standard",
        "text": "A school replaces its gas boiler with electric heaters and "
                "says it has stopped burning fossil fuel. The local grid runs "
                "mostly on coal. Is the school right?",
        "options": [
            {"text": "Yes, because no fuel is burnt anywhere on the school "
                     "site",
             "correct": False,
             "why": "None is burnt on site, but coal is burnt at the power "
                    "station to supply it."},
            {"text": "Yes, because electricity itself is a clean energy resource",
             "correct": False,
             "why": "Electricity is a pathway rather than a resource, and it "
                    "is as clean as whatever generated it."},
            {"text": "No, because electric heaters are less efficient than a "
                     "gas boiler",
             "correct": False,
             "why": "Electric heating turns almost all the electricity into "
                    "heat, so efficiency is not the flaw."},
            {"text": "No, the burning has moved to the power station",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s19",
        "band": "standard",
        "text": "Which resource runs out even though nothing is burnt to "
                "release its energy?",
        "options": [
            {"text": "Nuclear, because uranium is mined and cannot be "
                     "replaced",
             "correct": True},
            {"text": "Wind, because a still day means the supply has been used "
                     "up",
             "correct": False,
             "why": "A still day is a gap in supply. The wind returns, so "
                    "nothing has run out."},
            {"text": "Hydroelectric, because a reservoir empties as it "
                     "generates",
             "correct": False,
             "why": "Rain refills the reservoir, which is exactly what makes "
                    "it renewable."},
            {"text": "Solar, because the Sun will eventually burn out",
             "correct": False,
             "why": "The Sun will last billions of years, which is nothing "
                    "like a human timescale."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s20",
        "band": "standard",
        "text": "A country replaces its coal stations with gas stations. What "
                "has that achieved, and what has it not?",
        "options": [
            {"text": "It has removed the carbon entirely, and it has fixed the "
                     "supply problem too",
             "correct": False,
             "why": "Burning gas still releases carbon dioxide, roughly half "
                    "of coal's rather than none."},
            {"text": "It has roughly halved the carbon per unit, but the fuel "
                     "is still finite",
             "correct": True},
            {"text": "It has made the supply renewable, even though the carbon "
                     "figure is left unchanged",
             "correct": False,
             "why": "Gas is finite, and its carbon per unit is lower than "
                    "coal's rather than equal."},
            {"text": "It has changed nothing at all, since gas and coal are "
                     "really the same kind of fuel",
             "correct": False,
             "why": "Both are fossil fuels, but gas releases about half the "
                    "carbon for each unit of energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s21",
        "band": "standard",
        "text": "Apart from carbon dioxide, what else does burning wood put "
                "into the air?",
        "options": [
            {"text": "Nothing, because wood is a natural material",
             "correct": False,
             "why": "Being natural does not stop a fuel producing smoke as it "
                    "burns."},
            {"text": "Oxygen, which is given back as the wood burns",
             "correct": False,
             "why": "Burning uses oxygen up. It does not give any back."},
            {"text": "Soot and particulates, which damage lungs",
             "correct": True},
            {"text": "Uranium dust, in very small quantities", "correct": False,
             "why": "Wood contains no uranium. That belongs to nuclear fuel "
                    "instead."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s22",
        "band": "standard",
        "text": "Two valleys could be dammed for hydroelectricity. One holds a "
                "village and farmland; the other is bare rock. Which axis does "
                "that choice belong to?",
        "options": [
            {"text": "The carbon axis, because farmland stores carbon in its "
                     "soil",
             "correct": False,
             "why": "Soil does hold carbon, but what is being weighed here is "
                    "what the water will cover."},
            {"text": "The reliability axis, because the bigger valley would "
                     "hold a great deal more water",
             "correct": False,
             "why": "How much water is held is a supply question, not what "
                    "this comparison turns on."},
            {"text": "The cost axis, because bare rock is cheaper to buy",
             "correct": False,
             "why": "Price may differ, but the difference being weighed is "
                    "what is lost under the water."},
            {"text": "The land and habitat axis, because it decides what the "
                     "reservoir covers",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s23",
        "band": "standard",
        "text": "Two resources are both non-renewable. One is the "
                "highest-carbon on the grid and the other is nearly the "
                "lowest. Name the pair.",
        "options": [
            {"text": "Coal and nuclear", "correct": True},
            {"text": "Coal and natural gas", "correct": False,
             "why": "Both are non-renewable, but gas sits in the middle of the "
                    "carbon axis, not near the bottom."},
            {"text": "Wood and nuclear", "correct": False,
             "why": "Nuclear fits, but wood is renewable, so the pair fails "
                    "the first condition."},
            {"text": "Natural gas and tidal", "correct": False,
             "why": "Tidal is renewable, and gas is not the highest-carbon "
                    "resource on the grid."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s24",
        "band": "standard",
        "text": "A school fits solar panels and claims its electricity is now "
                "zero-carbon. What is the fair correction?",
        "options": [
            {"text": "The claim is exactly right, because a panel burns no "
                     "fuel",
             "correct": False,
             "why": "It burns none, but the claim covers more than what "
                    "happens on the roof."},
            {"text": "Almost none while generating, but making the panels took "
                     "mining and manufacturing",
             "correct": True},
            {"text": "The claim is wrong, because the panels release carbon "
                     "dioxide as they warm up in summer",
             "correct": False,
             "why": "A warm panel releases heat, which is not the same thing "
                    "as carbon dioxide."},
            {"text": "The claim is wrong, because the school still draws "
                     "electricity at night",
             "correct": False,
             "why": "Night-time electricity does come from the grid, but that "
                    "is a separate point from the panel's own figure."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s25",
        "band": "standard",
        "text": "On a still, dark, freezing January evening, demand is at its "
                "highest. Why is that the hardest moment for a grid running "
                "mostly on wind and solar?",
        "options": [
            {"text": "Because cold weather makes both the turbines and the "
                     "panels far less efficient",
             "correct": False,
             "why": "Cold air is denser and cold panels work rather better; "
                    "the problem is no wind and no light."},
            {"text": "Because the wind and the Sun have run out for the "
                     "winter",
             "correct": False,
             "why": "Neither has run out. Both return, which is why both count "
                    "as renewable."},
            {"text": "Because demand is at its peak at the very moment neither "
                     "is generating",
             "correct": True},
            {"text": "Because electricity cannot be carried along the cables "
                     "in freezing weather",
             "correct": False,
             "why": "Cables carry electricity perfectly well in the cold, and "
                    "rather better than in heat."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s26",
        "band": "standard",
        "text": "Why does a country build wind farms, nuclear stations and gas "
                "stations rather than just one of the three?",
        "options": [
            {"text": "Because each one of them is renewable in a different "
                     "way",
             "correct": False,
             "why": "Gas and nuclear are not renewable at all, so that cannot "
                    "be the reason."},
            {"text": "Because building several smaller stations is cheaper "
                     "than building one very large one",
             "correct": False,
             "why": "Cost varies, but the mix is chosen for what each resource "
                    "can and cannot do."},
            {"text": "Because the law requires a country to use every resource "
                     "available",
             "correct": False,
             "why": "No such requirement exists. The mix is an engineering "
                    "choice, not a legal one."},
            {"text": "Because no single resource is good on carbon, on demand "
                     "and on land at once",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s27",
        "band": "standard",
        "text": "Why can a tidal barrage not supply a city right through the "
                "day?",
        "options": [
            {"text": "It generates only while the tide is running",
             "correct": True},
            {"text": "The Moon is not above the sea for most of the day",
             "correct": False,
             "why": "A tide is raised on the far side of the Earth as well, so "
                    "that is not the limit."},
            {"text": "Seawater has to be replaced once it has been used",
             "correct": False,
             "why": "The same water flows back and forth. None of it is used "
                    "up."},
            {"text": "A barrage can work only during the hours of daylight",
             "correct": False,
             "why": "The tide runs at night as well. It is the tide, not the "
                    "light, that sets the timing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s28",
        "band": "standard",
        "text": "A country doubles the number of wind turbines it owns, yet "
                "its carbon emissions barely fall. Suggest the most likely "
                "reason.",
        "options": [
            {"text": "Wind turbines release carbon dioxide once there are "
                     "enough of them",
             "correct": False,
             "why": "A turbine releases none while it turns, however many are "
                    "built."},
            {"text": "Gas stations still run to cover the hours when the wind "
                     "is not blowing",
             "correct": True},
            {"text": "Doubling the turbines halves the energy each one "
                     "produces",
             "correct": False,
             "why": "Each turbine produces what the wind allows. They do not "
                    "share out a fixed total."},
            {"text": "Building turbines uses up the wind, so less is left for "
                     "the others",
             "correct": False,
             "why": "The wind is not consumed. A turbine slows the air a "
                    "little and it recovers."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s29",
        "band": "standard",
        "text": "Put coal, natural gas and nuclear in order of carbon released "
                "while generating, lowest first.",
        "options": [
            {"text": "Coal, natural gas, nuclear", "correct": False,
             "why": "That is the order reversed. Coal is the highest of the "
                    "three, not the lowest."},
            {"text": "Natural gas, coal, nuclear", "correct": False,
             "why": "Nuclear is the lowest of the three, so it cannot come "
                    "last."},
            {"text": "Nuclear, natural gas, coal", "correct": True},
            {"text": "Nuclear, coal, natural gas", "correct": False,
             "why": "Nuclear is right at the front, but coal sits above gas "
                    "rather than below it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-s30",
        "band": "standard",
        "text": "Which single change would cut a country's carbon the most, "
                "without anybody using less electricity?",
        "options": [
            {"text": "Replacing every one of the filament lamps in the "
                     "country with a modern LED bulb",
             "correct": False,
             "why": "That cuts how much electricity is used, which the "
                    "question rules out."},
            {"text": "Switching from gas cookers to electric ones on a grid "
                     "that runs mostly on coal",
             "correct": False,
             "why": "The carbon simply moves to the power station, and coal is "
                    "worse per unit than gas."},
            {"text": "Insulating every house in the country so that a great "
                     "deal less heating is needed",
             "correct": False,
             "why": "That is a reduction in use as well, which the question "
                    "rules out."},
            {"text": "Closing the coal stations and generating the same "
                     "electricity from wind",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-05-h11",
        "band": "harder",
        "text": "A campaigner argues that every non-renewable resource should "
                "be shut down at once. Using the grid, give the strongest "
                "objection.",
        "options": [
            {"text": "It would also shut down nuclear, which is the low-carbon "
                     "resource that runs on demand",
             "correct": True},
            {"text": "It would leave the country with no renewable resources "
                     "left",
             "correct": False,
             "why": "Shutting the non-renewables leaves every renewable "
                    "standing; that is the whole proposal."},
            {"text": "It would raise the carbon that wind and solar release "
                     "while they are both generating",
             "correct": False,
             "why": "Neither releases carbon while generating, and closing "
                    "other stations does not change that."},
            {"text": "It would make coal renewable, since less would be "
                     "burnt",
             "correct": False,
             "why": "Burning less coal does not refill the store. Renewable is "
                    "not about the rate of use."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h12",
        "band": "harder",
        "text": "A forest is cut for biomass and is not replanted. What "
                "happens to the argument that biomass is carbon-neutral?",
        "options": [
            {"text": "It is unaffected, because the carbon was absorbed before "
                     "the wood was burnt",
             "correct": False,
             "why": "Absorption in the past balances the release only if a new "
                    "tree absorbs it again."},
            {"text": "It collapses, because nothing is left to reabsorb the "
                     "carbon that was released",
             "correct": True},
            {"text": "It gets stronger, because the land can now be used for "
                     "wind turbines",
             "correct": False,
             "why": "What the land is used for next does not change the carbon "
                    "already in the air."},
            {"text": "It is unaffected, because the carbon stays locked in the "
                     "soil instead",
             "correct": False,
             "why": "The carbon in the wood went into the air when it burnt. "
                    "The soil does not hold it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h13",
        "band": "harder",
        "text": "A nuclear station and a wind farm both release almost no "
                "carbon while generating. Why do people still argue about "
                "which one to build?",
        "options": [
            {"text": "Because one of the two turns out to be high-carbon once "
                     "it has been running a while",
             "correct": False,
             "why": "Neither does. The two sit within a whisker of each other "
                    "on the carbon axis."},
            {"text": "Because just one of the two counts as an energy "
                     "resource",
             "correct": False,
             "why": "Both are energy resources. The disagreement is about "
                    "their other costs."},
            {"text": "Because they differ sharply on waste, on land and on "
                     "being available when wanted",
             "correct": True},
            {"text": "Because carbon is the one axis that decides what a "
                     "country should build",
             "correct": False,
             "why": "If carbon were the deciding axis these two would be hard "
                    "to separate, which is the opposite of the case."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h14",
        "band": "harder",
        "text": "Why does the carbon figure quoted for a solar panel depend on "
                "which country made it?",
        "options": [
            {"text": "Because the sunlight itself carries more carbon in some "
                     "countries than it does in others",
             "correct": False,
             "why": "Sunlight carries no carbon anywhere. It carries energy "
                    "and nothing else."},
            {"text": "Because panels made further away have to be shipped, and "
                     "that is the whole of the figure",
             "correct": False,
             "why": "Shipping adds a little, but manufacturing is where most "
                    "of the figure comes from."},
            {"text": "Because a panel generates a great deal more electricity "
                     "in a country that is sunnier",
             "correct": False,
             "why": "How much it generates changes the figure per unit a "
                    "little, but it is not what is being asked."},
            {"text": "Because the factory ran on that country's grid, and "
                     "grids differ in carbon",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h15",
        "band": "harder",
        "text": "Nuclear is described as almost carbon-free while generating. "
                "Why do those last two words matter?",
        "options": [
            {"text": "Mining the uranium, building the station and taking it "
                     "apart are not carbon-free",
             "correct": True},
            {"text": "A reactor releases a great deal of carbon dioxide once "
                     "it has been switched off again",
             "correct": False,
             "why": "A station that is off releases nothing. The carbon sits "
                    "in building and fuelling it."},
            {"text": "The waste slowly turns into carbon dioxide over the "
                     "thousands of years it lasts",
             "correct": False,
             "why": "The waste is radioactive rather than carbon-based, and it "
                    "does not become a gas."},
            {"text": "The phrase is there to make nuclear sound better than it "
                     "deserves",
             "correct": False,
             "why": "The phrase is precise rather than flattering, and the "
                    "same caution applies to solar panels."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h16",
        "band": "harder",
        "text": "Two countries each get two fifths of their electricity from "
                "renewables. One is mostly hydroelectric, the other mostly "
                "wind. Which will find the rest harder to plan?",
        "options": [
            {"text": "The hydroelectric one, because the water behind a dam "
                     "cannot be released at the moment it is wanted",
             "correct": False,
             "why": "A reservoir is released exactly when it is wanted, which "
                    "is why hydro counts as reliable."},
            {"text": "The wind one, because its output arrives when the "
                     "weather decides rather than when it is needed",
             "correct": True},
            {"text": "The wind one, because wind farms run out of wind sooner "
                     "than rivers run dry",
             "correct": False,
             "why": "Neither runs out. The difference between them is timing, "
                    "not supply."},
            {"text": "Neither, because two fifths is two fifths however it was "
                     "generated",
             "correct": False,
             "why": "How much is generated is half the question. When it "
                    "arrives is the other half."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h17",
        "band": "harder",
        "text": "A student ranks the resources on carbon alone and concludes "
                "that nuclear is the best choice. Which axis most weakens that "
                "conclusion?",
        "options": [
            {"text": "Land, because a nuclear station covers far more ground "
                     "than a wind farm of the same output",
             "correct": False,
             "why": "Nuclear takes the least land on the grid, so that axis "
                    "supports the conclusion rather than weakening it."},
            {"text": "Reliability, because a reactor cannot be turned up at "
                     "the exact moment it is wanted",
             "correct": False,
             "why": "Nuclear is among the most reliable resources there are, "
                    "so this axis supports it too."},
            {"text": "Waste, because what a reactor leaves behind stays "
                     "dangerous for thousands of years",
             "correct": True},
            {"text": "Renewability, because uranium will be exhausted within a "
                     "decade",
             "correct": False,
             "why": "Uranium is finite, but on a scale of many decades, and "
                    "supply is not the usual objection."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h18",
        "band": "harder",
        "text": "An engineer suggests building far more wind turbines than are "
                "needed, so that a light breeze is enough. Why does that not "
                "fully solve intermittency?",
        "options": [
            {"text": "Because the extra turbines slow the wind down until none "
                     "of them work",
             "correct": False,
             "why": "Turbines take a small share of the air's movement. They "
                    "do not stop the wind."},
            {"text": "Because a wind farm becomes non-renewable once it is "
                     "large enough",
             "correct": False,
             "why": "Size does not change whether a store refills, and the "
                    "wind refills whatever is built."},
            {"text": "Because the extra turbines would release carbon dioxide "
                     "as they turn",
             "correct": False,
             "why": "A turning turbine releases none, however many of them are "
                    "standing."},
            {"text": "Because a still day produces nothing, however many "
                     "turbines are standing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h19",
        "band": "harder",
        "text": "One island has a fast river falling from high ground; another "
                "is flat and windy. Each wants power it can rely on. Advise "
                "both islands.",
        "options": [
            {"text": "The river island can build hydroelectricity and rely on "
                     "it; the windy one cannot rely on wind alone",
             "correct": True},
            {"text": "Both should build wind farms, since wind is the more "
                     "renewable of the two",
             "correct": False,
             "why": "Neither is more renewable than the other; both refill. "
                    "Reliability is what separates them."},
            {"text": "Both should burn wood, since biomass is renewable and "
                     "available in every season",
             "correct": False,
             "why": "Biomass is renewable, but it emits heavily and takes a "
                    "great deal of land to grow."},
            {"text": "The windy island should build a dam; the river island "
                     "should rely on wind",
             "correct": False,
             "why": "A dam needs high ground and a river, which a flat island "
                    "has not got. The advice is the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h20",
        "band": "harder",
        "text": "Uranium is finite, yet arguments about nuclear power rarely "
                "turn on it running out. Suggest why not.",
        "options": [
            {"text": "Because more uranium can be manufactured once the "
                     "existing mines have been emptied",
             "correct": False,
             "why": "Uranium is an element. It is mined, and it cannot be "
                    "made."},
            {"text": "Because the known supply lasts many decades, while the "
                     "waste lasts far longer",
             "correct": True},
            {"text": "Because running out is not a real problem for any "
                     "resource",
             "correct": False,
             "why": "It is exactly the problem for coal, gas and oil, which is "
                    "why they are classed apart."},
            {"text": "Because uranium counts as renewable once it has been "
                     "reprocessed",
             "correct": False,
             "why": "Reprocessing recovers some fuel but puts no uranium back "
                    "into the ground."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h21",
        "band": "harder",
        "text": "A country has no rivers and no high ground. Which pair of "
                "resources would cover both low carbon and power on demand?",
        "options": [
            {"text": "Wind and solar, because between them one of the two is "
                     "generating at any time",
             "correct": False,
             "why": "There are calm winter nights when neither of them is "
                    "generating at all."},
            {"text": "Coal and gas, because both of them can be turned up the "
                     "moment they are wanted",
             "correct": False,
             "why": "Both meet the demand test and both fail the carbon test "
                    "badly."},
            {"text": "Nuclear and wind, because nuclear covers the hours when "
                     "the wind drops",
             "correct": True},
            {"text": "Tidal and solar, because between the two of them the "
                     "output can be predicted",
             "correct": False,
             "why": "Solar is not predictable through cloud, and neither runs "
                    "to order at midnight."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h22",
        "band": "harder",
        "text": "A student argues that because almost every resource traces "
                "back to the Sun, all of them must be renewable. What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong with it; coal really is ancient "
                     "sunlight, so coal is renewable too",
             "correct": False,
             "why": "Coal is ancient sunlight, but the store took three "
                    "hundred million years to fill."},
            {"text": "Coal does not trace back to the Sun, so the premise is "
                     "simply false",
             "correct": False,
             "why": "Coal is ancient plant matter, so the premise holds. It is "
                    "the conclusion that fails."},
            {"text": "The Sun is not renewable either, so the argument fails "
                     "at the start",
             "correct": False,
             "why": "The Sun will last billions of years, which is well beyond "
                    "any human timescale."},
            {"text": "Renewable is about how long the store takes to refill, "
                     "and that delay is what differs",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h23",
        "band": "harder",
        "text": "Each resource pays a different price. Which line matches the "
                "resource to its main cost correctly?",
        "options": [
            {"text": "Hydroelectricity, flooded land; nuclear, long-lived "
                     "waste; wind, still days",
             "correct": True},
            {"text": "Hydroelectricity, still days; nuclear, flooded land; "
                     "wind, long-lived waste",
             "correct": False,
             "why": "Every pairing has been shifted along by one, so none of "
                    "the three lands on the right resource."},
            {"text": "Hydroelectricity, long-lived waste; nuclear, still "
                     "days; wind, flooded land",
             "correct": False,
             "why": "Waste belongs to nuclear, still days to wind, and flooded "
                    "land to hydroelectricity."},
            {"text": "Hydroelectricity, carbon dioxide; nuclear, carbon "
                     "dioxide; wind, carbon dioxide",
             "correct": False,
             "why": "All three are low-carbon while generating, so carbon is "
                    "not the cost that separates them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h24",
        "band": "harder",
        "text": "A grid with a great deal of solar finds its hardest hour is "
                "the winter evening rather than the summer night. Explain "
                "that.",
        "options": [
            {"text": "Because the panels stop working altogether below "
                     "freezing",
             "correct": False,
             "why": "Cold panels work rather better than hot ones. The winter "
                    "problem is the lack of light."},
            {"text": "Because demand peaks on a winter evening, when there is "
                     "no light to generate from",
             "correct": True},
            {"text": "Because summer nights are longer than winter evenings",
             "correct": False,
             "why": "Winter nights are the longer of the two, which is part of "
                    "the difficulty."},
            {"text": "Because solar panels store up energy through the day and "
                     "release it again at night",
             "correct": False,
             "why": "A panel stores nothing. It generates only while light is "
                    "falling on it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h25",
        "band": "harder",
        "text": "Gas is often called a bridge fuel on the way to a low-carbon "
                "grid. Evaluate that description.",
        "options": [
            {"text": "It is wrong, because gas releases more carbon than coal "
                     "for each unit",
             "correct": False,
             "why": "Gas releases about half of coal's per unit, which is the "
                    "whole basis of the description."},
            {"text": "It is right, because gas is renewable and so the bridge "
                     "never has to end",
             "correct": False,
             "why": "Gas is a finite fossil fuel, so it cannot be the "
                    "destination."},
            {"text": "It is fair on carbon and on filling the gaps, but gas is "
                     "still finite and still emits",
             "correct": True},
            {"text": "It is wrong, because there is nothing that can be turned "
                     "on quickly enough to fill a gap",
             "correct": False,
             "why": "Gas is the quickest thing on the grid to turn up, which "
                    "is exactly why it is used for that."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h26",
        "band": "harder",
        "text": "Coal is worst on carbon, hydroelectricity worst on land and "
                "wind worst on availability. What does that pattern show about "
                "choosing a resource?",
        "options": [
            {"text": "That the axes will eventually come to agree with each "
                     "other once better data is gathered",
             "correct": False,
             "why": "The orderings differ because the resources differ, not "
                    "because the figures are poor."},
            {"text": "That a resource scoring worst on one axis is bound to "
                     "score best on all the others",
             "correct": False,
             "why": "Coal is worst on carbon and middling on land, so no such "
                    "rule holds."},
            {"text": "That the worst resource overall must be whichever one of "
                     "them appears worst most often",
             "correct": False,
             "why": "Counting appearances treats three different costs as "
                    "though they were one cost."},
            {"text": "That choosing a resource means choosing which cost to "
                     "accept, not avoiding them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h27",
        "band": "harder",
        "text": "A country must decide between more wind and a new nuclear "
                "station. Which piece of evidence would be most useful?",
        "options": [
            {"text": "A full year of demand data set against a full year of "
                     "wind records",
             "correct": True},
            {"text": "The number of people who say they prefer one of the "
                     "two",
             "correct": False,
             "why": "Preference may matter politically, but it says nothing "
                    "about whether the lights stay on."},
            {"text": "The carbon released by the two, since that settles the "
                     "question",
             "correct": False,
             "why": "Both are low-carbon while generating, so that figure "
                    "cannot separate them."},
            {"text": "The date on which each technology was first invented",
             "correct": False,
             "why": "Age tells you nothing about carbon, reliability, land or "
                    "waste."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h28",
        "band": "harder",
        "text": "Gas rather than nuclear is used to cover the hours when the "
                "wind drops. Suggest why, given that both run on demand.",
        "options": [
            {"text": "Because nuclear is intermittent and gas is not",
             "correct": False,
             "why": "Nuclear is one of the most reliable resources on the "
                    "grid, so intermittency is not its weakness."},
            {"text": "Because a gas station can be turned up and down quickly, "
                     "which suits short gaps",
             "correct": True},
            {"text": "Because a nuclear station releases far more carbon "
                     "dioxide than a gas station does",
             "correct": False,
             "why": "Nuclear releases essentially none while generating and "
                    "gas releases a great deal."},
            {"text": "Because gas is renewable, so it can be used as freely as "
                     "the gap requires",
             "correct": False,
             "why": "Gas is a finite fossil fuel. How freely it is used is a "
                    "separate matter again."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h29",
        "band": "harder",
        "text": "Biomass crops are grown on fields that used to grow food. "
                "Which cost does that belong to, and why is it easy to miss?",
        "options": [
            {"text": "The carbon cost, because crops release carbon dioxide as "
                     "they grow",
             "correct": False,
             "why": "Growing plants absorb carbon dioxide. They release it "
                    "when the fuel is burnt."},
            {"text": "The reliability cost, because a harvest can fail in a "
                     "bad year",
             "correct": False,
             "why": "A failed harvest is a real risk, but the field itself is "
                    "the cost being described."},
            {"text": "The land cost, because the fuel looks renewable and the "
                     "land it took is invisible",
             "correct": True},
            {"text": "The waste cost, because the ash that is left behind will "
                     "stay dangerous for centuries",
             "correct": False,
             "why": "Wood ash is not dangerous for centuries. That belongs to "
                    "nuclear waste instead."},
        ],
        "figure": None,
    },
    {
        "id": "p2-05-h30",
        "band": "harder",
        "text": "Wind, solar and tidal are all renewable, all low-carbon and "
                "none of them burns anything. Why does a grid still not run on "
                "those three alone?",
        "options": [
            {"text": "Because none of the three is really renewable once it is "
                     "examined closely",
             "correct": False,
             "why": "All three refill continuously, and that is not what stops "
                    "a grid using them alone."},
            {"text": "Because the three of them together release as much "
                     "carbon as coal does",
             "correct": False,
             "why": "All three release essentially nothing while generating, "
                    "however many are built."},
            {"text": "Because tidal power takes more land than all the others "
                     "put together",
             "correct": False,
             "why": "Hydroelectricity takes the most land; tidal affects "
                    "estuaries rather than covering land."},
            {"text": "Because none of the three can be turned up at the moment "
                     "it is wanted",
             "correct": True},
        ],
        "figure": None,
    },
]
