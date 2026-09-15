"""Physics · Energy — the MRB-338 expansion of `energy-resources`.

One leaf only: AQA 8463 §4.1.4, the main energy resources, what makes one
renewable, what each is used for, how reliable each is, and the environmental
and social cost of using it. The original twelve rows in `energy.py` define
renewable, name the solar-cell exception, name carbon dioxide, name the
geothermal source, classify bio-fuel, trace the coal-station chain, and take one
evaluation each of solar, bio-fuel, tidal siting and wind impact. This file takes
what they leave: the non-renewable definition from the other side, the rest of
the resource list classified, the turbine-and-generator mechanism named, the uses
beyond electricity, intermittency against predictability against switchability,
six further environmental costs, and the siting comparisons for places the
original four never visit.

The weight follows the CONTENT. `easier` stays at eight because recall here is
one definition, one mechanism, one waste product and a handful of
classifications, and asking those a ninth way would be the same question. The
demand lives in `standard`, where a resource's behaviour has to be explained
rather than named, and in `harder`, where two resources compete for one real
site and the pupil has to weigh reliability, cost and consequence against each
other — so that is where the twenty-two-row bands sit.

⚠️ Seam with `power`: a station's output may appear as a stated fact in MW. No
row here asks for a power from an energy and a time.
⚠️ Seam with `efficiency`: no row here asks for a ratio or a percentage.
⚠️ Seam with `energy-stores-systems`: that leaf owns the store-and-pathway chain
for a power station, including the nuclear one. No chain question appears here.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The non-renewable definition, the generating mechanism, three
    # classifications and the two waste products the first four never name.
    {
        "id": "ks4-energy-resources-e05",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Coal, oil and natural gas are all non-renewable. State what "
                "this means.",
        "options": [
            "They are used up faster than they are replaced, so one day they "
            "will run out",
            "They cannot be used to generate electricity without a turbine "
            "and a generator of some kind",
            "They cannot be moved from the place where they are found to the "
            "place where they are needed",
            "They release carbon dioxide, which is what makes a resource "
            "count as non-renewable",
        ],
        "correct_index": 0,
        "why": "A non-renewable resource is one the Earth does not replace on "
               "any useful timescale, so the supply is finite.",
    },
    {
        "id": "ks4-energy-resources-e06",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether nuclear fuel is renewable or non-renewable, "
                "and why.",
        "options": [
            "Renewable, because a nuclear station releases no carbon dioxide "
            "as it runs",
            "Non-renewable, because uranium is never replaced as it is used "
            "up",
            "Renewable, because the uranium can be put back into the ground "
            "after use",
            "Non-renewable, because a nuclear station has to be shut down "
            "every few years",
        ],
        "correct_index": 1,
        "why": "Uranium is mined from a finite supply and nothing replaces "
               "it, so nuclear fuel is non-renewable however clean it is.",
    },
    {
        "id": "ks4-energy-resources-e07",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two components that most power stations use to "
                "produce electricity.",
        "options": [
            "A battery and a transformer",
            "A boiler and a cooling tower",
            "A turbine and a generator",
            "A chimney and a condenser",
        ],
        "correct_index": 2,
        "why": "Almost every resource is used to turn a turbine, and the "
               "turning turbine drives a generator that does electrical "
               "work.",
    },
    {
        "id": "ks4-energy-resources-e08",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the renewable resource that uses the rise and fall of "
                "the sea twice a day.",
        "options": [
            "Wave power",
            "Wind power",
            "Hydroelectricity",
            "Tidal power",
        ],
        "correct_index": 3,
        "why": "Tides are the twice-daily rise and fall caused by the Moon, "
               "and a barrage takes energy from the water moving through it.",
    },
    {
        "id": "ks4-energy-resources-e09",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the resource that petrol and diesel are made from.",
        "options": [
            "Crude oil",
            "Coal",
            "Natural gas",
            "Uranium ore",
        ],
        "correct_index": 0,
        "why": "Petrol and diesel are fractions separated from crude oil, "
               "which is why transport still depends so heavily on it.",
    },
    {
        "id": "ks4-energy-resources-e10",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released by burning some fossil fuels that "
                "causes acid rain.",
        "options": [
            "Carbon dioxide",
            "Sulfur dioxide",
            "Nitrogen",
            "Steam and water vapour",
        ],
        "correct_index": 1,
        "why": "Sulfur in the fuel burns to sulfur dioxide, which dissolves "
               "in cloud droplets and falls as acid rain.",
    },
    {
        "id": "ks4-energy-resources-e11",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the waste product of a nuclear power station that has "
                "to be stored safely for a very long time.",
        "options": [
            "Sulfur dioxide from the reactor",
            "Warm cooling water from the turbines",
            "Radioactive waste from the used fuel",
            "Carbon dioxide from the fuel rods",
        ],
        "correct_index": 2,
        "why": "Used fuel stays radioactive for thousands of years, so it has "
               "to be stored where it cannot reach people or water.",
    },
    {
        "id": "ks4-energy-resources-e12",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which renewable resource produces no electricity at "
                "all during the night.",
        "options": [
            "Tidal power",
            "Wind power",
            "Geothermal power",
            "Solar cells",
        ],
        "correct_index": 3,
        "why": "Solar cells need light, so their output falls to nothing "
               "after dark while the other three can run at any hour.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each resource's own behaviour explained — how it generates, when it is
    # available, what it costs the environment — plus the uses beyond mains
    # electricity.
    {
        "id": "ks4-energy-resources-s05",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why coal is classed as a non-renewable resource.",
        "options": [
            "It took millions of years to form and is being burned far faster "
            "than that",
            "It is found in a handful of countries, so most of the world "
            "cannot obtain any",
            "It releases carbon dioxide, and a resource that does so cannot "
            "be renewable",
            "It has to be dug out of the ground rather than collected from "
            "the surface",
        ],
        "correct_index": 0,
        "why": "Coal formed from plants buried over geological time, so on "
               "any human timescale the supply is fixed and falling.",
    },
    {
        "id": "ks4-energy-resources-s06",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country generates 45% of its electricity from gas, 20% "
                "from nuclear, 15% from wind, 12% from coal and 8% from "
                "hydroelectricity. Calculate the percentage of its "
                "electricity that comes from renewable resources.",
        "options": [
            "8%",
            "23%",
            "43%",
            "35%",
        ],
        "correct_index": 1,
        "why": "Wind and hydroelectricity are the renewable resources in this "
               "mix, giving 15% + 8% = 23%. Gas and coal are fossil fuels and "
               "nuclear fuel is non-renewable.",
    },
    {
        "id": "ks4-energy-resources-s07",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a wind turbine produces electricity.",
        "options": [
            "Moving air is compressed inside the tower and the hot air drives "
            "a generator",
            "Moving air charges the blades as it passes, and that charge is "
            "collected at the base of the tower",
            "Moving air turns the blades, and the turning shaft drives a "
            "generator",
            "Moving air heats water inside the blades, and the steam drives a "
            "generator",
        ],
        "correct_index": 2,
        "why": "The air does work on the blades, filling their kinetic store, "
               "and the generator they turn does electrical work.",
    },
    {
        "id": "ks4-energy-resources-s08",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why geothermal power stations are built in only a "
                "few parts of the world.",
        "options": [
            "Because geothermal water is too hot to be piped safely in most "
            "countries",
            "Because most countries have no rock that is warmer than the "
            "surface",
            "Because the Earth's internal energy reaches the surface during "
            "the summer only",
            "Because hot rock lies close enough to the surface to be reached "
            "only in some places",
        ],
        "correct_index": 3,
        "why": "The rock has to be hot at a depth that can be drilled, which "
               "is true near volcanic regions and rarely elsewhere.",
    },
    {
        "id": "ks4-energy-resources-s09",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a nuclear power station is usually kept running "
                "at a steady output rather than being switched on and off.",
        "options": [
            "Because its output cannot be changed quickly, so it is used to "
            "cover the demand that is always there",
            "Because a reactor produces no radioactive waste while its output "
            "is held steady",
            "Because uranium is able to release energy while the reactor "
            "holds one steady temperature and no other",
            "Because a nuclear station produces more electricity in total if "
            "it is never inspected",
        ],
        "correct_index": 0,
        "why": "A reactor takes many hours to change output, so it supplies "
               "the steady base demand while faster stations follow the "
               "peaks.",
    },
    {
        "id": "ks4-energy-resources-s10",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what a solar cell and a solar water-heating panel "
                "each produce.",
        "options": [
            "Both produce electricity, but the panel produces a larger "
            "current than the cell does",
            "The cell warms water for the building, while the panel produces "
            "electricity for it",
            "Both warm water, but the cell does so using sunlight and the "
            "panel using the warm air",
            "The cell produces electricity, while the panel warms water for "
            "use in the building",
        ],
        "correct_index": 3,
        "why": "A photovoltaic cell does electrical work directly from light; "
               "a heating panel simply lets sunlight fill the thermal store "
               "of the water.",
    },
    {
        "id": "ks4-energy-resources-s11",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how burning coal in a power station contributes to "
                "climate change.",
        "options": [
            "The warm water it returns to the rivers nearby raises the "
            "temperature of the whole country",
            "The steam leaving its cooling towers adds a greenhouse gas to "
            "the atmosphere",
            "The carbon dioxide it releases traps energy that would otherwise "
            "leave the Earth",
            "The soot it releases settles on the ice caps and stops the Earth "
            "from warming any further at all",
        ],
        "correct_index": 2,
        "why": "Carbon dioxide is a greenhouse gas: it absorbs radiation on "
               "its way out of the atmosphere, so the surface warms.",
    },
    {
        "id": "ks4-energy-resources-s12",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the environmental damage that acid rain causes.",
        "options": [
            "It warms the rivers and the lakes it falls into, so that the "
            "fish living in them cannot breathe",
            "It blocks the sunlight from reaching crops, so harvests right "
            "across a region fail",
            "It settles as a fine dust that stops the rain from falling "
            "anywhere downwind of it",
            "It damages trees and makes lakes acidic, killing the fish that "
            "live in them",
        ],
        "correct_index": 3,
        "why": "Sulfur dioxide dissolved in rain lowers the pH of soil and "
               "water, harming forests and freshwater life.",
    },
    {
        "id": "ks4-energy-resources-s13",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the main environmental cost of building a large "
                "hydroelectric reservoir in a valley.",
        "options": [
            "A large area of land is flooded, destroying habitats and "
            "sometimes homes",
            "A large amount of carbon dioxide is released by the falling "
            "water each year",
            "A large volume of radioactive waste is produced by the turbines "
            "in the dam",
            "A large quantity of sulfur dioxide escapes from the water held "
            "behind the dam",
        ],
        "correct_index": 0,
        "why": "Filling the reservoir puts the valley floor under water for "
               "good, which is the price paid for a reliable renewable "
               "supply.",
    },
    {
        "id": "ks4-energy-resources-s14",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one reason why growing crops to make bio-fuel is "
                "criticised.",
        "options": [
            "Bio-fuel crops absorb no carbon dioxide from the air while they "
            "are growing",
            "Bio-fuel releases no energy when it is burned, so the crop is "
            "grown for nothing",
            "Land used for fuel crops is land that could have grown food "
            "instead",
            "Bio-fuel crops can be grown only on land that has never been "
            "farmed before",
        ],
        "correct_index": 2,
        "why": "Fuel and food compete for the same fields and water, which is "
               "a social cost rather than a physical one.",
    },
    {
        "id": "ks4-energy-resources-s15",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electricity demand of a country is not the "
                "same at every hour of the day.",
        "options": [
            "Because the national grid carries electricity at some times of "
            "the day and not others",
            "Because power stations are switched off overnight to let their "
            "turbines cool down",
            "Because people cook, wash and light their homes at some hours "
            "and sleep at others",
            "Because electricity travels more slowly along the cables when "
            "the air is colder",
        ],
        "correct_index": 2,
        "why": "Demand follows what people are doing, which is why a supply "
               "has to be able to rise and fall to match it.",
    },
    {
        "id": "ks4-energy-resources-s16",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an exposed coastal ridge is a good site for a "
                "wind farm.",
        "options": [
            "The salt in the sea air makes the blades turn more freely than "
            "they would inland",
            "The sea beside it can be used to cool the generators at the top "
            "of each tower",
            "Coastal land is cheaper to buy than farmland anywhere else in "
            "the country",
            "The wind there is stronger and steadier than it is over "
            "sheltered ground inland",
        ],
        "correct_index": 3,
        "why": "A turbine's output depends on the wind it meets, so a site is "
               "chosen for how strong and how reliable the wind is.",
    },
    {
        "id": "ks4-energy-resources-s17",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a tidal barrage across an estuary produces "
                "electricity.",
        "options": [
            "Water flowing through gaps in the barrage turns turbines built "
            "into it",
            "Waves breaking against the barrage push air through pipes to a "
            "generator",
            "The weight of the water resting on the barrage presses on cells "
            "that make a current",
            "Salt water passing over metal plates in the barrage produces a "
            "current directly",
        ],
        "correct_index": 0,
        "why": "The barrage holds back the tide and then lets it through, and "
               "the moving water turns turbines exactly as falling water does "
               "in a dam.",
    },
    {
        "id": "ks4-energy-resources-s18",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why tidal power and wave power are counted as two "
                "different resources.",
        "options": [
            "Tidal power counts as renewable, while wave power has to be "
            "classed as non-renewable",
            "Tides are caused by the Moon, while waves are raised by the wind "
            "blowing over the sea",
            "Tides are a feature of rivers, while waves belong to the open "
            "ocean",
            "Tidal stations turn a generator, while wave stations produce "
            "their current without needing one at all",
        ],
        "correct_index": 1,
        "why": "They have different causes, so they are available at "
               "different times and are harvested by different machines.",
    },
    {
        "id": "ks4-energy-resources-s19",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a country generates its electricity from a "
                "mixture of resources rather than from one alone.",
        "options": [
            "Because the national grid is unable to accept electricity from "
            "one source at a time",
            "Because a single resource may be unavailable or too costly at "
            "the moment it is needed",
            "Because using several resources means less electricity is wasted "
            "in the cables",
            "Because the law requires every resource on the list to be used "
            "somewhere in the country",
        ],
        "correct_index": 1,
        "why": "A mix covers the gaps: when the wind drops or a station is "
               "shut for repair, something else can carry the demand.",
    },
    {
        "id": "ks4-energy-resources-s20",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify two uses of energy resources other than generating "
                "mains electricity.",
        "options": [
            "Transport and the heating of buildings",
            "Transport and the storing of spare electricity inside the "
            "national grid itself",
            "Lighting streets and charging batteries at home",
            "Cooling buildings and running the national grid",
        ],
        "correct_index": 0,
        "why": "Fuels are burned directly to move vehicles and to warm homes, "
               "neither of which passes through a power station.",
    },
    {
        "id": "ks4-energy-resources-s21",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a nuclear power station releases no carbon "
                "dioxide while it is generating electricity.",
        "options": [
            "Because the carbon dioxide it makes is captured and stored "
            "inside the reactor building",
            "Because the cooling water dissolves the carbon dioxide before it "
            "can reach the air",
            "Because uranium contains no carbon dioxide, unlike the sulfur "
            "found in coal",
            "Because the energy comes from splitting nuclei rather than from "
            "burning a fuel",
        ],
        "correct_index": 3,
        "why": "Carbon dioxide comes from combustion, and nothing is burned "
               "in a reactor, so the generating stage adds none.",
    },
    {
        "id": "ks4-energy-resources-s22",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a mountainous country with heavy rainfall "
                "generates much of its electricity from hydroelectricity.",
        "options": [
            "Heavy rain cools the generators, letting them run at a larger "
            "output than usual",
            "Rain fills high reservoirs, and water falling from a height can "
            "turn turbines",
            "Mountain air is thinner, so the turbines in the dam meet less "
            "resistance as they spin",
            "Mountains shelter the dams from the wind, which would otherwise "
            "disturb the water",
        ],
        "correct_index": 1,
        "why": "The resource is water held high up: rainfall refills the "
               "reservoir and the drop to the turbines is what the country's "
               "landscape provides.",
    },
    {
        "id": "ks4-energy-resources-s23",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why oil remains the main resource used for transport "
                "even in countries with plenty of renewable electricity.",
        "options": [
            "Because renewable electricity is unable to drive a motor in a "
            "vehicle",
            "Because a litre of fuel is easy to carry and releases a great "
            "deal of energy",
            "Because oil is the one resource that can be stored for more than "
            "a few days",
            "Because renewable resources are all classed as non-renewable "
            "once they are moved",
        ],
        "correct_index": 1,
        "why": "Liquid fuel packs a large amount of energy into a small mass "
               "that a vehicle can carry, which is what transport needs.",
    },
    {
        "id": "ks4-energy-resources-s24",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a solar farm in the United Kingdom generates far "
                "less electricity in December than in June.",
        "options": [
            "The cells work less well once they are cold, so the winter "
            "output is smaller every year",
            "The panels are switched off through the winter to protect them "
            "from frost and from snow",
            "The days are shorter and the Sun is lower, so much less light "
            "reaches the panels",
            "The Sun is a great deal further away in December, so the light "
            "arriving carries less energy in it",
        ],
        "correct_index": 2,
        "why": "Output depends on the light collected, and a short day with a "
               "low Sun delivers a fraction of a long summer one.",
    },
    {
        "id": "ks4-energy-resources-s25",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the effect that the cooling water returned from a "
                "coal-fired power station has on a river.",
        "options": [
            "It raises the river's temperature, which can harm the fish "
            "living there",
            "It lowers the river's temperature, because the water returned "
            "has already been through a cooling tower",
            "It makes the river acidic, because the sulfur in the coal "
            "dissolves in the water",
            "It has no measurable effect, because the water is filtered "
            "before it is returned",
        ],
        "correct_index": 0,
        "why": "The water carries away the station's waste thermal energy, so "
               "it returns warmer and the river's dissolved oxygen falls.",
    },
    {
        "id": "ks4-energy-resources-s26",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the output of a tidal barrage varies through the "
                "day and yet can be known weeks in advance.",
        "options": [
            "Because the tides are driven by the weather, which is forecast "
            "weeks ahead",
            "Because the tides follow the motion of the Moon, which always "
            "repeats on a fixed timetable",
            "Because the barrage is opened and closed to a timetable set by "
            "the electricity company",
            "Because the tides rise and fall at random, and the average over "
            "a month is constant",
        ],
        "correct_index": 1,
        "why": "The Moon's orbit is regular, so tide times and heights can be "
               "calculated years ahead even though the output still rises and "
               "falls.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Two resources weighed against one real site, and the evaluations —
    # reliability, cost, and the impact that is easy to leave out.
    {
        "id": "ks4-energy-resources-h05",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a renewable resource has no "
                "environmental impact.",
        "options": [
            "The claim holds, because renewable means the resource is "
            "replaced as fast as it is used",
            "The claim holds, because nothing is burned, and burning is the "
            "only source of impact",
            "The claim fails, because building and installing the equipment "
            "always uses energy, materials and land",
            "The claim fails, because a renewable station emits more carbon "
            "dioxide than a coal one",
        ],
        "correct_index": 2,
        "why": "Renewable describes the supply of the resource, not the cost "
               "of the machinery, the land it occupies or its effect on "
               "wildlife.",
    },
    {
        "id": "ks4-energy-resources-h06",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country wants to cut its carbon dioxide emissions but "
                "needs a supply it can rely on. Compare nuclear and coal for "
                "this purpose.",
        "options": [
            "Coal is better, because it can be switched on quickly and coal "
            "releases no carbon dioxide",
            "Nuclear is better, because it is reliable and releases no carbon "
            "dioxide, though it leaves radioactive waste",
            "The two are equally suitable, because both of them are "
            "non-renewable resources",
            "Neither of them can be used, because a supply that is reliable "
            "is possible from a renewable resource alone",
        ],
        "correct_index": 1,
        "why": "Both run steadily whatever the weather, but only coal "
               "releases carbon dioxide, so nuclear meets both conditions at "
               "the price of its waste.",
    },
    {
        "id": "ks4-energy-resources-h07",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An inland desert country has strong sunshine all year, no "
                "rivers, no coastline and no volcanic rock. Determine the "
                "most suitable renewable resource.",
        "options": [
            "Solar, because the resource it needs is the one thing that site "
            "has in abundance",
            "Hydroelectricity, because a reservoir could be filled from the "
            "rain that falls on the desert each winter",
            "Tidal, because a desert country can build a barrage inland "
            "across a dry valley",
            "Geothermal, because the sand at the surface of a desert becomes "
            "extremely hot by day",
        ],
        "correct_index": 0,
        "why": "Each of the other three needs something the site does not "
               "have, while sunshine is exactly what solar cells and heating "
               "panels use.",
    },
    {
        "id": "ks4-energy-resources-h08",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A volcanic island has hot rock close to the surface and "
                "heavy rain on steep hills. Compare geothermal and "
                "hydroelectricity for it.",
        "options": [
            "Hydroelectricity alone would work, because a geothermal station "
            "needs a supply of fuel to be shipped in to it",
            "Both of them would work, and both would run the same in any week "
            "the weather brought",
            "Both would work, though the hydroelectric output would fall in a "
            "dry spell while geothermal would not",
            "Geothermal alone would work, because the rain on steep hills "
            "runs away far too fast to be collected",
        ],
        "correct_index": 2,
        "why": "The island suits both, but one resource depends on rainfall "
               "and the other on the Earth's internal energy, which does not "
               "vary.",
    },
    {
        "id": "ks4-energy-resources-h09",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the suggestion that every fossil-fuel power station "
                "in a country should be closed within a month.",
        "options": [
            "Sensible, because renewable stations already produce more "
            "electricity than any country needs",
            "Sensible, because a country that closes its fossil stations "
            "stops climate change on its own",
            "Doubtful, because the replacement capacity and the storage to go "
            "with it would not yet exist",
            "Doubtful, because fossil fuels release less carbon dioxide than "
            "the renewable resources would",
        ],
        "correct_index": 2,
        "why": "The demand does not fall because the stations shut, so the "
               "argument turns on what would be there to meet it rather than "
               "on the emissions alone.",
    },
    {
        "id": "ks4-energy-resources-h10",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that nuclear fuel should count as renewable "
                "because there is a great deal of uranium in the Earth. "
                "Evaluate this argument.",
        "options": [
            "It is sound, because a resource counts as renewable once a large "
            "enough stock has been found",
            "It is sound, because uranium re-forms in the ground as soon as "
            "the used fuel has been buried",
            "It fails, because renewable means the resource is replaced as it "
            "is used, not that there is a lot",
            "It fails, because uranium is used up so quickly that a station "
            "cannot be kept running for a whole year",
        ],
        "correct_index": 2,
        "why": "A large stock is still a finite stock; renewable is about "
               "replacement, so plentiful and renewable are not the same "
               "thing.",
    },
    {
        "id": "ks4-energy-resources-h11",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the cheapest resource to run is not always the "
                "one a country chooses.",
        "options": [
            "Because the cheapest resource to run is the one that is hardest "
            "to connect to a grid",
            "Because the running cost of a resource is fixed by law rather "
            "than by what it needs",
            "Because a cheap resource has to be sold abroad before it can be "
            "used at home",
            "Because reliability, building cost and environmental impact all "
            "weigh on the decision too",
        ],
        "correct_index": 3,
        "why": "The choice is a trade-off: a resource can be cheap to run and "
               "still be unreliable, costly to build or unacceptable "
               "locally.",
    },
    {
        "id": "ks4-energy-resources-h12",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest two reasons why a government might build a wind farm "
                "out at sea rather than on farmland.",
        "options": [
            "Offshore turbines need no generator of their own, and the sea "
            "water cools them as they turn",
            "The wind at sea is stronger and steadier, and fewer people live "
            "near enough to object",
            "Offshore turbines are cheaper to build, and the salt in the sea "
            "air makes their blades last far longer",
            "The sea is calmer than the land, so the blades turn at a more "
            "even rate all year",
        ],
        "correct_index": 1,
        "why": "There is nothing to shelter the wind at sea, and the visual "
               "and noise objections that hold up onshore schemes are far "
               "weaker.",
    },
    {
        "id": "ks4-energy-resources-h13",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An estuary is considered for either a tidal barrage or a "
                "wave farm. Compare the two for reliability of output.",
        "options": [
            "The barrage, because its output can be worked out in advance "
            "while waves depend on the weather",
            "The wave farm, because waves arrive continuously while the tide "
            "is high twice a day",
            "The two are equally reliable, because both of them take energy "
            "from moving sea water",
            "The wave farm, because its output ignores whatever happens above "
            "the surface",
        ],
        "correct_index": 0,
        "why": "Tides follow the Moon and are predictable years ahead; wave "
               "height depends on wind that cannot be forecast far in "
               "advance.",
    },
    {
        "id": "ks4-energy-resources-h14",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of these could supply a city on a still, "
                "overcast winter night.",
        "options": [
            "A solar farm, because its cells carry on working for hours after "
            "the light has gone",
            "A wind farm, because its blades go on turning by themselves once "
            "they have been started",
            "A solar water-heating scheme, because the water it has warmed "
            "holds that warmth right through the night",
            "A nuclear station, because its output does not depend on the "
            "weather or the time",
        ],
        "correct_index": 3,
        "why": "Three of these need sunlight or wind, neither of which is "
               "available, while a reactor runs at the same output whatever "
               "the night is like.",
    },
    {
        "id": "ks4-energy-resources-h15",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate a decision to keep one gas-fired power station "
                "closed but ready to run, rather than demolishing it.",
        "options": [
            "A good decision, because a station kept ready can cover a still "
            "week when renewable output is low",
            "A good decision, because a station that has been standing idle "
            "for months releases no carbon dioxide when it is used",
            "A poor decision, because a gas station cannot be restarted once "
            "it has been shut down",
            "A poor decision, because a country with any renewable capacity "
            "never needs another resource",
        ],
        "correct_index": 0,
        "why": "Gas can be brought up to output within hours, which is what "
               "makes it useful as a reserve against an intermittent supply.",
    },
    {
        "id": "ks4-energy-resources-h16",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why electricity from a resource that costs nothing "
                "to run can still be expensive.",
        "options": [
            "Because a resource that costs nothing to run has to be taxed "
            "more heavily than all the others",
            "Because the equipment is costly to build and has to be paid for "
            "out of the electricity sold",
            "Because a free resource has to be used at night, when "
            "electricity is worth the most",
            "Because the electricity produced from a resource that is free is "
            "wasted more quickly in the grid cables",
        ],
        "correct_index": 1,
        "why": "Wind and sunlight are free, but the turbines, panels and grid "
               "connections are not, and that cost is spread over every unit "
               "generated.",
    },
    {
        "id": "ks4-energy-resources-h17",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why local objections can stop a wind farm being "
                "built even where the wind is ideal.",
        "options": [
            "Because turbines reduce the amount of wind reaching the land "
            "behind them",
            "Because planning decisions must be made by the electricity "
            "company rather than by a council",
            "Because residents may object to the noise, the appearance and "
            "the effect on local wildlife",
            "Because a wind farm has to be built on land that nobody lives "
            "within sight of",
        ],
        "correct_index": 2,
        "why": "The choice of a resource is social as well as technical: a "
               "scheme needs planning permission, and objections are weighed "
               "in that decision.",
    },
    {
        "id": "ks4-energy-resources-h18",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a country with year-round sunshine "
                "needs no resource other than solar.",
        "options": [
            "The claim holds, because sunshine all year means the output "
            "never changes from hour to hour",
            "The claim holds, because solar cells store the light they "
            "collect until it is needed",
            "The claim fails, because sunshine is weaker in that country than "
            "it is in a cloudy one",
            "The claim fails, because nothing is generated at night, so "
            "storage or another resource is needed",
        ],
        "correct_index": 3,
        "why": "Even the sunniest country is dark for half of every day, so a "
               "solar-only supply needs storage or a second resource to cover "
               "the night.",
    },
    {
        "id": "ks4-energy-resources-h19",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why replacing petrol cars with electric cars reduces "
                "carbon dioxide emissions only partly in a country that burns "
                "coal for electricity.",
        "options": [
            "Because an electric car releases carbon dioxide from its battery "
            "as it is driven",
            "Because the emissions move from the car's exhaust to the chimney "
            "of the power station",
            "Because an electric car needs more energy to travel a kilometre "
            "than a petrol car does",
            "Because coal releases no carbon dioxide, so the change makes no "
            "difference either way",
        ],
        "correct_index": 1,
        "why": "The car itself emits nothing, but the electricity it uses was "
               "generated somewhere, so the emissions are shifted rather than "
               "removed.",
    },
    {
        "id": "ks4-energy-resources-h20",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the waste a nuclear power station produces with the "
                "waste a gas-fired station produces.",
        "options": [
            "Both produce carbon dioxide, but the nuclear station produces "
            "far more of it for each unit",
            "The nuclear station produces no waste of any kind, while the gas "
            "station leaves behind a radioactive ash",
            "Both produce radioactive waste, but it is the gas station that "
            "must store its waste for centuries",
            "The nuclear station produces a small volume of radioactive "
            "waste; the gas station releases carbon dioxide",
        ],
        "correct_index": 3,
        "why": "The two waste streams are different in kind: one is a small "
               "quantity of solid that must be contained, the other a gas "
               "released into the atmosphere.",
    },
    {
        "id": "ks4-energy-resources-h21",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that fossil fuels will not run out "
                "because new deposits keep being discovered.",
        "options": [
            "The claim holds, because the Earth goes on forming new coal and "
            "oil as fast as they are burned",
            "The claim holds, because a deposit that has been found can be "
            "used more than once",
            "The claim fails, because discovery only finds what already "
            "exists, while the total in the ground falls",
            "The claim fails, because a deposit that has only just been "
            "discovered lies too deep to be drilled or mined",
        ],
        "correct_index": 2,
        "why": "Finding a deposit does not create one: the stock formed over "
               "millions of years and every barrel burned lowers it.",
    },
    {
        "id": "ks4-energy-resources-h22",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydroelectric scheme pumps water back up to its reservoir "
                "at night. Suggest why an operator would do this.",
        "options": [
            "Pumping the water upwards generates extra electricity on the way "
            "up",
            "Pumping warms the water, so more energy is released when it "
            "falls again",
            "Pumping cleans the turbines, which would otherwise be blocked by "
            "the falling water",
            "Demand is low at night, so cheap electricity refills a store "
            "that can be released at a peak",
        ],
        "correct_index": 3,
        "why": "The reservoir acts as a store: the scheme fills a "
               "gravitational potential store when electricity is plentiful "
               "and empties it when it is scarce.",
    },
    {
        "id": "ks4-energy-resources-h23",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A remote farmhouse has no mains gas, a windy exposed site "
                "and a small stream. Determine a sensible resource for "
                "heating it, and justify the choice.",
        "options": [
            "Wood from the surrounding land, because it is a bio-fuel that "
            "can be regrown and burned on site",
            "Coal delivered by road, because a non-renewable fuel is what "
            "will warm a house",
            "Tidal power taken from the stream, because moving water turns a "
            "turbine",
            "Geothermal energy, because every farmhouse sits above rock that "
            "is hotter than the air",
        ],
        "correct_index": 0,
        "why": "A locally grown bio-fuel needs no pipeline and no delivery, "
               "and the two other renewable suggestions do not match what the "
               "site actually offers.",
    },
    {
        "id": "ks4-energy-resources-h24",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the carbon dioxide released by one country's "
                "power stations is treated as a global problem.",
        "options": [
            "Because the gas stays above the country that released it until "
            "the rain washes it back down",
            "Because each country is charged for the carbon dioxide that its "
            "neighbours release",
            "Because the gas mixes through the whole atmosphere, so the "
            "warming is shared by every country",
            "Because the carbon dioxide itself travels along the cables of "
            "the international electricity grid",
        ],
        "correct_index": 2,
        "why": "The atmosphere is one connected system, so a greenhouse gas "
               "added anywhere raises the temperature everywhere.",
    },
    {
        "id": "ks4-energy-resources-h25",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grid operator says tidal power is predictable but not "
                "constant, while wind is neither. Explain the distinction "
                "being made.",
        "options": [
            "Tidal output is known ahead but still rises and falls; wind "
            "output cannot be known ahead either",
            "Tidal output holds steady right through the day, while wind "
            "output changes from hour to hour",
            "Tidal output is predictable because it is small, and wind output "
            "is unpredictable because it is large",
            "Tidal output can be adjusted to match the demand, while wind "
            "output has to be used as it comes",
        ],
        "correct_index": 0,
        "why": "Predictable means you know in advance what you will get; "
               "constant would mean getting the same at every moment, and "
               "tidal power is the first without being the second.",
    },
    {
        "id": "ks4-energy-resources-h26",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate a proposal to supply a hospital's emergency "
                "electricity from solar panels alone.",
        "options": [
            "A sound proposal, because solar panels have no moving parts and "
            "so cannot fail",
            "A sound proposal, because a hospital needs its emergency supply "
            "during the daytime",
            "An unsound proposal, because solar panels cannot produce enough "
            "current to run any machine",
            "An unsound proposal, because an emergency supply must work at "
            "night and in poor weather",
        ],
        "correct_index": 3,
        "why": "An emergency supply is judged on whether it is available "
               "whenever it is called on, and solar output is nothing at "
               "night.",
    },
]
