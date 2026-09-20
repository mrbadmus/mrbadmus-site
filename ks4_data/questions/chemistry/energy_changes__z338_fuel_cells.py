"""Chemistry · Energy changes — the MRB-338 expansion, subtopic
`fuel-cells`.

The frozen twelve already hold the overall equation, the battery contrast,
platinum, quick refuelling, green hydrogen, efficiency against a petrol
engine, on-board storage, the lorry and bus evaluations and the Apollo
application. The weight here falls on the electrode chemistry those rows
never reach — both half equations, the redox vocabulary, the electron and
hydrogen-ion bookkeeping and the electrolyte's job — and on the two
evaluative veins the spec point actually rewards: operational emissions
against the carbon released where the hydrogen was made, and the fuel cell
route set against burning the same hydrogen in an engine. The remaining
rows take the advantages and obstacles into applications the frozen twelve
do not use — a warehouse forklift, a submarine, a rail line with no wires,
a remote weather station, a building site — and add four mole calculations
on 2H2 + O2 → 2H2O.
"""

TOPIC = "energy-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ───────────────────────────────────────────────────────────
    {
        "id": "ks4-fuel-cells-e05",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the only chemical product formed when a hydrogen fuel "
                "cell operates.",
        "options": [
            "Water, which leaves the cell through an outlet",
            "Carbon dioxide, formed as the hydrogen burns",
            "Hydrogen peroxide, formed from the two gases",
            "A mixture of water and carbon monoxide gas",
        ],
        "correct_index": 0,
        "why": "Hydrogen and oxygen combine to give water and nothing else, "
               "which is why a working fuel cell has no polluting exhaust.",
    },
    {
        "id": "ks4-fuel-cells-e06",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a working hydrogen fuel cell, oxygen gas reaches the "
                "positive electrode. State what happens to it.",
        "options": [
            "It is oxidised, losing electrons to the electrode",
            "It is reduced, gaining electrons from the electrode",
            "It is compressed by the catalyst into liquid oxygen",
            "It is stored in the electrode until the cell stops",
        ],
        "correct_index": 1,
        "why": "Oxygen gains electrons at the positive electrode, and gain of "
               "electrons is reduction.",
    },
    {
        "id": "ks4-fuel-cells-e07",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State where a fuel cell car obtains the oxygen that it needs.",
        "options": [
            "From a tank of oxygen carried beside the hydrogen",
            "From the water that the cell has already produced",
            "From the air around it, drawn in while the cell runs",
            "From the platinum, which releases it slowly in use",
        ],
        "correct_index": 2,
        "why": "Only the hydrogen has to be carried on board; the oxygen is "
               "taken from the surrounding air as the cell works.",
    },
    {
        "id": "ks4-fuel-cells-e08",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what must be supplied to a hydrogen fuel cell for it "
                "to keep producing electricity.",
        "options": [
            "Hydrogen alone, since oxygen is made inside the cell itself",
            "Mains electricity, which the cell then stores up for later",
            "Water, which the cell splits apart again as it is running",
            "Hydrogen and oxygen, fed in while the cell is working",
        ],
        "correct_index": 3,
        "why": "A fuel cell keeps no store of reactants of its own, so both "
               "gases must keep arriving for the electrode reactions to "
               "continue.",
    },
    {
        "id": "ks4-fuel-cells-e09",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the platinum in a hydrogen fuel cell "
                "while the cell is running.",
        "options": [
            "It speeds up the electrode reactions and is not used up",
            "It reacts with the hydrogen and has to be replaced often",
            "It is slowly turned into water along with the hydrogen",
            "It dissolves into the electrolyte and washes out as waste",
        ],
        "correct_index": 0,
        "why": "Platinum is a catalyst, so it takes part in the electrode "
               "reactions and is left unchanged at the end of them.",
    },
    {
        "id": "ks4-fuel-cells-e10",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the half equation for the reaction at the negative "
                "electrode of a hydrogen fuel cell.",
        "options": [
            "2H+ + 2e- → H2, so hydrogen ions take up the electrons",
            "H2 → 2H+ + 2e-, so hydrogen gives up the electrons",
            "H2 + 2e- → 2H-, so hydrogen takes a pair of electrons",
            "H2 + O2 → H2O2, with the electrons held in the metal",
        ],
        "correct_index": 1,
        "why": "Each hydrogen molecule loses two electrons at the negative "
               "electrode and leaves as two hydrogen ions.",
    },
    {
        "id": "ks4-fuel-cells-e11",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the electrical output of a hydrogen "
                "fuel cell if the hydrogen supply is cut off.",
        "options": [
            "It carries on unchanged, as the cell holds hydrogen inside it",
            "It rises sharply, as the oxygen is no longer being shared out",
            "It stops, because there is no longer a fuel to be oxidised",
            "It runs for several days on the water the cell has made",
        ],
        "correct_index": 2,
        "why": "A fuel cell holds no reserve of fuel, so the electrode "
               "reactions and the current they drive both stop as soon as "
               "the hydrogen stops arriving.",
    },
    {
        "id": "ks4-fuel-cells-e12",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process by which most of the hydrogen used today is "
                "manufactured.",
        "options": [
            "Electrolysis of sea water using electricity from wind farms",
            "Fractional distillation of crude oil in a tall column",
            "Heating limestone strongly to drive hydrogen out of it",
            "Steam reforming of natural gas at a high temperature",
        ],
        "correct_index": 3,
        "why": "Methane from natural gas is reacted with steam, which is "
               "cheap but releases carbon dioxide as a by-product.",
    },

    # ── standard ─────────────────────────────────────────────────────────
    {
        "id": "ks4-fuel-cells-s05",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Oxygen gas reacts at the positive electrode of a hydrogen "
                "fuel cell. Identify the correct half equation for this "
                "change.",
        "options": [
            "O2 + 4H+ + 4e- → 2H2O, because oxygen gains electrons here",
            "2H2O → O2 + 4H+ + 4e-, because oxygen is oxidised here",
            "O2 + 2H2 → 2H2O, because the electrons stay inside the gas",
            "O2 + 4H+ → 2H2O + 4e-, because oxygen releases electrons",
        ],
        "correct_index": 0,
        "why": "Oxygen is reduced at the positive electrode, taking in the "
               "four electrons that have travelled round the external "
               "circuit along with four hydrogen ions.",
    },
    {
        "id": "ks4-fuel-cells-s06",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why two molecules of hydrogen are used for every one "
                "molecule of oxygen in a hydrogen fuel cell.",
        "options": [
            "Hydrogen molecules are half the size of oxygen ones, so twice "
            "as many of them will fit",
            "Each hydrogen molecule releases two electrons and each oxygen "
            "molecule takes in four",
            "Oxygen is twice as reactive as hydrogen, so half as much of it "
            "is needed for the reaction",
            "Two hydrogen molecules are required to pull each oxygen "
            "molecule apart into its atoms",
        ],
        "correct_index": 1,
        "why": "The electrons lost at the negative electrode must match "
               "those gained at the positive one, and four electrons per "
               "oxygen molecule means two hydrogen molecules.",
    },
    {
        "id": "ks4-fuel-cells-s07",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the hydrogen ions made at the negative "
                "electrode of a fuel cell reach the positive electrode.",
        "options": [
            "They travel along the external circuit together with electrons",
            "They are carried across by the oxygen entering the cell",
            "They move through the electrolyte between the electrodes",
            "They escape into the air and re-enter at the other side",
        ],
        "correct_index": 2,
        "why": "The electrolyte conducts ions, so the hydrogen ions cross "
               "inside the cell to meet the oxygen at the positive "
               "electrode.",
    },
    {
        "id": "ks4-fuel-cells-s08",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hydrogen fuel cell is a redox system. Identify which "
                "substance is oxidised and which is reduced.",
        "options": [
            "Water is oxidised and hydrogen is reduced",
            "Oxygen is oxidised and water is reduced",
            "Hydrogen is reduced and oxygen is oxidised",
            "Hydrogen is oxidised and oxygen is reduced",
        ],
        "correct_index": 3,
        "why": "Hydrogen loses electrons at the negative electrode and "
               "oxygen gains them at the positive electrode, which is "
               "oxidation and reduction in turn.",
    },
    {
        "id": "ks4-fuel-cells-s09",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a car powered by a hydrogen fuel cell may still "
                "be linked to carbon dioxide emissions.",
        "options": [
            "Most hydrogen is made by reforming natural gas, which gives off "
            "carbon dioxide",
            "The cell gives off a small amount of carbon dioxide along with "
            "the water it makes",
            "The platinum catalyst releases carbon dioxide as the cell warms "
            "up during a journey",
            "Carbon dioxide drawn in from the air is concentrated by the "
            "cell and then let out",
        ],
        "correct_index": 0,
        "why": "The car's own exhaust is water, but the carbon dioxide given "
               "off where its hydrogen was manufactured still belongs to its "
               "overall footprint.",
    },
    {
        "id": "ks4-fuel-cells-s10",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bus fleet changes from reformed hydrogen to hydrogen made "
                "by electrolysis using wind electricity. Explain the effect "
                "on the carbon dioxide released overall.",
        "options": [
            "It rises, because electrolysis needs far more energy than "
            "reforming does",
            "It falls, because splitting water with wind electricity gives "
            "off no carbon dioxide",
            "It stays the same, because the same mass of hydrogen is burnt "
            "either way",
            "It falls to nothing, because wind turbines take carbon dioxide "
            "out of the air",
        ],
        "correct_index": 1,
        "why": "Steam reforming releases carbon dioxide from the natural gas "
               "it consumes, while electrolysis driven by renewable "
               "electricity releases none.",
    },
    {
        "id": "ks4-fuel-cells-s11",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the useful energy transfer when hydrogen is burned "
                "in an engine with that when the same hydrogen is fed to a "
                "fuel cell.",
        "options": [
            "The engine transfers more, because burning releases the energy "
            "faster than a cell can",
            "Both transfer the same amount, because exactly the same "
            "reaction happens in each one",
            "The fuel cell transfers more, because it misses out the "
            "combustion and engine stages",
            "The fuel cell transfers less, because some of the hydrogen "
            "leaves the cell unreacted",
        ],
        "correct_index": 2,
        "why": "Burning heats a gas that must then push pistons and turn a "
               "shaft, and energy is wasted at every one of those stages.",
    },
    {
        "id": "ks4-fuel-cells-s12",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Burning hydrogen in a vehicle engine can produce nitrogen "
                "oxides. Explain why a hydrogen fuel cell does not.",
        "options": [
            "The cell strips nitrogen out of the air before the oxygen "
            "reaches its electrode",
            "Nitrogen oxides come from nitrogen dissolved in a fuel, and "
            "hydrogen contains none",
            "The cell turns any nitrogen oxides that form back into "
            "nitrogen and oxygen again",
            "The cell works at a low temperature, so nitrogen from the air "
            "does not react",
        ],
        "correct_index": 3,
        "why": "Nitrogen oxides form when the high temperature inside an "
               "engine makes nitrogen and oxygen from the air combine, and "
               "a fuel cell never reaches that temperature.",
    },
    {
        "id": "ks4-fuel-cells-s13",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Water drips from a pipe beneath a fuel cell bus on a cold "
                "morning. Explain this observation.",
        "options": [
            "Water vapour made by the cell has condensed to a liquid in the "
            "cold air",
            "Rain that collected on the roof is being drained away through "
            "that pipe",
            "Hydrogen leaking from the tank is reacting with damp air under "
            "the vehicle",
            "The cell makes liquid water whenever the air outside falls "
            "below freezing",
        ],
        "correct_index": 0,
        "why": "Water is the cell's one chemical product, and the vapour "
               "leaving the outlet condenses when it meets cold air.",
    },
    {
        "id": "ks4-fuel-cells-s14",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fuel cell forklift trucks are chosen for work "
                "inside a warehouse.",
        "options": [
            "They need no oxygen supply, so they can work in the sealed "
            "parts of a warehouse",
            "They give off no exhaust fumes indoors, because water is their "
            "only product",
            "They run on air alone, so no fuel has to be stored anywhere on "
            "the warehouse site",
            "They are quieter, because the hydrogen tank soaks up the noise "
            "made by the motor",
        ],
        "correct_index": 1,
        "why": "A diesel forklift fills an enclosed space with carbon "
               "dioxide and particulates, while a fuel cell releases only "
               "water.",
    },
    {
        "id": "ks4-fuel-cells-s15",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a hydrogen fuel cell suits a remote weather "
                "station better than a rechargeable battery does.",
        "options": [
            "It makes its own hydrogen from the damp air at the station",
            "It needs no fuel, so nobody has to travel out to service it",
            "It gives a steady output for as long as its fuel supply lasts",
            "It works without oxygen, which is thin at a mountain station",
        ],
        "correct_index": 2,
        "why": "A battery's output falls as it discharges and it must then "
               "be recharged, while a fuel cell delivers the same output "
               "while fuel is fed to it.",
    },
    {
        "id": "ks4-fuel-cells-s16",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A submarine runs on hydrogen fuel cells while submerged. "
                "Explain why it must carry oxygen as well as hydrogen.",
        "options": [
            "Oxygen keeps the platinum catalyst from reacting with sea water",
            "Oxygen must be mixed into the tank to stop hydrogen exploding",
            "Oxygen is used to push the water made by the cell overboard",
            "The cell takes oxygen from the air, which it cannot reach",
        ],
        "correct_index": 3,
        "why": "A fuel cell needs a continuous oxygen supply at its positive "
               "electrode, and a submerged vessel cannot draw that oxygen "
               "from the atmosphere.",
    },
    {
        "id": "ks4-fuel-cells-s17",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why hydrogen fuel cells are expensive to "
                "manufacture.",
        "options": [
            "Their electrodes use platinum, a rare metal that costs a great "
            "deal per gram",
            "Their electrolyte has to be renewed each time the cell is "
            "refuelled with hydrogen",
            "Each cell has to be filled with pure oxygen held at a very high "
            "pressure",
            "The water that they produce has to be purified before the cell "
            "can be sold",
        ],
        "correct_index": 0,
        "why": "Platinum catalyses both electrode reactions, and it is among "
               "the rarest and costliest metals in industrial use.",
    },
    {
        "id": "ks4-fuel-cells-s18",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says the platinum in a fuel cell is gradually "
                "used up and has to be topped up. Identify the error.",
        "options": [
            "The platinum is used up, but so slowly that topping it up is "
            "unnecessary",
            "A catalyst is not consumed, so the same platinum keeps working "
            "throughout",
            "The cell uses no catalyst, because its electrode reactions are "
            "fast enough already",
            "The platinum is turned into water and leaves the cell with the "
            "other product",
        ],
        "correct_index": 1,
        "why": "A catalyst takes part in a reaction and is returned "
               "unchanged at the end of it, so the platinum is still there "
               "when the cell is dismantled.",
    },
    {
        "id": "ks4-fuel-cells-s19",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the output of a fuel cell does not fade during "
                "a long journey in the way a battery's output does.",
        "options": [
            "The cell warms up as it runs, and a warm cell gives a larger "
            "voltage than a cold one",
            "The cell recharges itself from the water that it has already "
            "produced during the trip",
            "Its reactants arrive from outside, so they never begin to run "
            "low within the cell",
            "Its electrodes hold a reserve of charge that is released when "
            "the output starts to drop",
        ],
        "correct_index": 2,
        "why": "A battery's stored reactants are consumed as it discharges, "
               "while a fuel cell's are replaced continuously from the tank "
               "and the air.",
    },
    {
        "id": "ks4-fuel-cells-s20",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why battery electric cars are at present more "
                "practical than fuel cell cars for most UK drivers.",
        "options": [
            "A battery can be recharged more quickly than a hydrogen tank "
            "can be filled up",
            "Battery cars give off no water, so they need no drainage "
            "underneath the vehicle",
            "A battery holds more energy per kilogram than a tank of "
            "hydrogen of the same mass",
            "Charging points are widespread, while hydrogen stations are "
            "still very rare",
        ],
        "correct_index": 3,
        "why": "The electricity network already reaches homes and car parks, "
               "so charging points are easy to add, whereas a hydrogen "
               "station is a new installation from scratch.",
    },
    {
        "id": "ks4-fuel-cells-s21",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a hydrogen refuelling station costs more to "
                "build than an electric charging point.",
        "options": [
            "Hydrogen has to be stored and delivered under very high "
            "pressure, needing special equipment",
            "Hydrogen must be manufactured at the station, because the gas "
            "cannot be transported safely",
            "Hydrogen stations have to be supervised at all times by a "
            "fully qualified chemist",
            "Hydrogen is a liquid at room temperature, so large heated "
            "tanks are needed to hold it",
        ],
        "correct_index": 0,
        "why": "Compressors, thick-walled pressure vessels and leak "
               "detection are all needed for hydrogen, while a charging "
               "point mainly needs a connection to a supply already there.",
    },
    {
        "id": "ks4-fuel-cells-s22",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Most hydrogen is still made from natural gas. Suggest why a "
                "city might nevertheless replace its diesel buses with fuel "
                "cell buses.",
        "options": [
            "The carbon dioxide given off when the hydrogen was made is "
            "taken back in by the cell",
            "The pollution is moved away from busy streets, improving air "
            "quality in the city",
            "Buses running on reformed hydrogen give off no carbon dioxide "
            "at any point in the chain",
            "Diesel engines cannot be fitted with exhaust filters, so their "
            "fumes cannot be cleaned up",
        ],
        "correct_index": 1,
        "why": "A fuel cell bus gives off water where people are breathing, "
               "so street-level nitrogen oxides and particulates fall even "
               "though carbon dioxide is released at the hydrogen plant.",
    },
    {
        "id": "ks4-fuel-cells-s23",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a hydrogen tank stores more energy per kilogram "
                "than a battery pack of the same mass.",
        "options": [
            "A battery pack holds a lot of water, which adds mass without "
            "storing any energy",
            "A hydrogen tank is kept under pressure, and it is the pressure "
            "that stores the energy",
            "Hydrogen releases a large quantity of energy for a very small "
            "mass of fuel",
            "A hydrogen tank is much bigger, and a bigger store holds more "
            "energy for each kilogram",
        ],
        "correct_index": 2,
        "why": "Hydrogen has a very high energy content for its mass, so the "
               "tank holding a given amount of energy is far lighter than "
               "the battery pack that would hold the same.",
    },
    {
        "id": "ks4-fuel-cells-s24",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the job done by the electrolyte inside a hydrogen "
                "fuel cell.",
        "options": [
            "It supplies the oxygen that the positive electrode needs in "
            "order to react",
            "It stores the electrical energy produced until the vehicle is "
            "next started up",
            "It reacts with the hydrogen to strip the electrons out of each "
            "molecule of it",
            "It lets ions pass between the electrodes while blocking "
            "electrons",
        ],
        "correct_index": 3,
        "why": "Because electrons cannot cross the electrolyte they are "
               "forced round the external circuit instead, and that flow is "
               "the cell's electrical output.",
    },
    {
        "id": "ks4-fuel-cells-s25",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a hydrogen refuelling area must be well "
                "ventilated and kept clear of naked flames.",
        "options": [
            "Hydrogen is highly flammable, and a leak would make an "
            "explosive mixture with air",
            "Hydrogen is poisonous, and breathing in the leaked gas would "
            "harm the people nearby",
            "Hydrogen reacts with damp air to make an acid that would "
            "corrode the pumps badly",
            "Hydrogen is denser than air, so a leak would gather around the "
            "feet of anyone there",
        ],
        "correct_index": 0,
        "why": "Hydrogen ignites over a wide range of concentrations in air, "
               "so any leak has to disperse well away from a source of "
               "ignition.",
    },
    {
        "id": "ks4-fuel-cells-s26",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens when the two electrode half equations "
                "of a hydrogen fuel cell are added together.",
        "options": [
            "The hydrogen ions cancel out and the result is H2 + O2 → H2O2",
            "The electrons and hydrogen ions cancel, leaving 2H2 + O2 → 2H2O",
            "The electrons are added up, giving 2H2 + O2 + 4e- → 2H2O",
            "Nothing cancels out, as the electrodes hold separate reactions",
        ],
        "correct_index": 1,
        "why": "Four electrons and four hydrogen ions appear on opposite "
               "sides of the two half equations, so they cancel and leave "
               "the overall cell reaction.",
    },

    # ── harder ───────────────────────────────────────────────────────────
    {
        "id": "ks4-fuel-cells-h05",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen refuelling stations remain scarce in the UK. "
                "Explain why this shortage is hard to solve.",
        "options": [
            "Hydrogen cannot be moved by road, so each station would have "
            "to manufacture its own supply",
            "Planning law forbids a hydrogen station from being built "
            "inside any town or city boundary",
            "Few stations are built while few hydrogen cars exist, and few "
            "are bought while stations are scarce",
            "The whole natural gas network would have to be rebuilt before "
            "a single station could be supplied",
        ],
        "correct_index": 2,
        "why": "Drivers will not buy a car they cannot refuel and companies "
               "will not build stations with no customers, so each side "
               "waits for the other to move first.",
    },
    {
        "id": "ks4-fuel-cells-h06",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate powering an ordinary family car used for short "
                "local journeys with a fuel cell rather than a battery.",
        "options": [
            "The fuel cell is better, because short journeys drain a "
            "battery unusually quickly",
            "The fuel cell is better, because a family car has no room "
            "anywhere for a battery pack",
            "The battery is better, because a fuel cell cannot deliver "
            "power at low road speeds",
            "The battery is better, because charging at home suits short "
            "trips and costs less",
        ],
        "correct_index": 3,
        "why": "Hydrogen's advantages are range and refuelling speed, and "
               "neither is needed for short local trips that an overnight "
               "charge covers cheaply.",
    },
    {
        "id": "ks4-fuel-cells-h07",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A warehouse works its forklift trucks around the clock. "
                "Evaluate replacing the battery trucks with fuel cell ones.",
        "options": [
            "Worth doing, because a truck goes back into service at once "
            "instead of waiting to charge",
            "Worth doing, because a fuel cell truck needs no fuel stored "
            "anywhere on the warehouse site",
            "Not worth doing, because a fuel cell cannot run without a "
            "break for a whole working shift",
            "Not worth doing, because the water produced would make the "
            "warehouse floor unsafe to drive on",
        ],
        "correct_index": 0,
        "why": "Round-the-clock working leaves no spare hours for a battery "
               "to charge or be swapped, while a hydrogen tank refills in "
               "about the time a diesel tank does.",
    },
    {
        "id": "ks4-fuel-cells-h08",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate using hydrogen fuel cells rather than a diesel "
                "generator to power a vessel travelling under water.",
        "options": [
            "The diesel generator wins, because it needs no oxygen at all "
            "while it is running",
            "The fuel cell wins, because stored hydrogen and oxygen give "
            "quiet power with no exhaust",
            "The fuel cell wins, because it takes the oxygen that it needs "
            "straight from sea water",
            "The diesel generator wins, because its exhaust gases dissolve "
            "harmlessly in sea water",
        ],
        "correct_index": 1,
        "why": "A submerged vessel can neither take in air nor vent exhaust "
               "gases, so a cell running on stored gases and producing only "
               "water suits it, and it runs almost silently.",
    },
    {
        "id": "ks4-fuel-cells-h09",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a hydrogen fuel cell car is a zero "
                "emission vehicle.",
        "options": [
            "The claim holds, because no carbon dioxide is released at any "
            "stage of the fuel's life",
            "The claim fails, because the car itself gives off carbon "
            "dioxide alongside the water",
            "The claim holds for the car's own exhaust, but not once "
            "hydrogen production is counted",
            "The claim fails, because the water that is released counts as "
            "an emission in its own right",
        ],
        "correct_index": 2,
        "why": "The car emits water alone as it drives, but most hydrogen "
               "is made by steam reforming natural gas, which releases "
               "carbon dioxide before the fuel reaches the tank.",
    },
    {
        "id": "ks4-fuel-cells-h10",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare making hydrogen by steam reforming with making it "
                "by the electrolysis of water.",
        "options": [
            "Reforming costs more but gives off less carbon dioxide than "
            "electrolysis does",
            "Both routes give off the same carbon dioxide, but electrolysis "
            "is by far the quicker",
            "Electrolysis is both cheaper and cleaner, which is why most "
            "hydrogen is made that way",
            "Reforming is cheaper but gives off carbon dioxide, while "
            "electrolysis is cleaner and dearer",
        ],
        "correct_index": 3,
        "why": "Natural gas is a cheap feedstock and reforming is well "
               "established, but it releases carbon dioxide, while "
               "electrolysis on renewable electricity releases none.",
    },
    {
        "id": "ks4-fuel-cells-h11",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The air filter over a fuel cell's intake becomes clogged "
                "with dust. Predict the effect on the cell's output and "
                "explain your answer.",
        "options": [
            "The output falls, because less oxygen reaches the positive "
            "electrode to be reduced",
            "The output rises, because the hydrogen is no longer being "
            "diluted by the incoming air",
            "The output holds steady, because the cell takes the oxygen it "
            "needs from its own water",
            "The output falls, because the dust settles on the platinum and "
            "reacts with the metal",
        ],
        "correct_index": 0,
        "why": "The current depends on both electrode reactions continuing, "
               "so restricting the oxygen supply limits the rate at which "
               "electrons can be accepted.",
    },
    {
        "id": "ks4-fuel-cells-h12",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "4.0 g of hydrogen reacts completely in a fuel cell. "
                "Calculate the mass of water produced. (Mr: H2 = 2, "
                "H2O = 18)",
        "options": [
            "18 g",
            "36 g",
            "32 g",
            "72 g",
        ],
        "correct_index": 1,
        "why": "4.0 g of hydrogen is 2.0 mol, and 2H2 + O2 → 2H2O gives the "
               "same number of moles of water, so the mass is 2.0 × 18 = "
               "36 g.",
    },
    {
        "id": "ks4-fuel-cells-h13",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the mass of oxygen that reacts completely with "
                "10 g of hydrogen in a fuel cell. (Mr: H2 = 2, O2 = 32)",
        "options": [
            "160 g",
            "320 g",
            "80 g",
            "16 g",
        ],
        "correct_index": 2,
        "why": "10 g of hydrogen is 5.0 mol, and 2H2 + O2 → 2H2O needs half "
               "as many moles of oxygen, so the mass is 2.5 × 32 = 80 g.",
    },
    {
        "id": "ks4-fuel-cells-h14",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine the number of moles of electrons that pass round "
                "the external circuit for each mole of oxygen reduced at the "
                "positive electrode.",
        "options": [
            "1 mol",
            "2 mol",
            "3 mol",
            "4 mol",
        ],
        "correct_index": 3,
        "why": "The half equation O2 + 4H+ + 4e- → 2H2O shows that every "
               "mole of oxygen molecules accepts four moles of electrons.",
    },
    {
        "id": "ks4-fuel-cells-h15",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A building site has no mains electricity. Evaluate using a "
                "hydrogen fuel cell generator there instead of a diesel one.",
        "options": [
            "The fuel cell is quieter and gives off only water, but "
            "hydrogen is harder to obtain on site",
            "The fuel cell is louder but cheaper to run, and its hydrogen "
            "is delivered exactly as diesel is",
            "The diesel generator gives off only water, so there is little "
            "to choose between the two of them",
            "The diesel generator is quieter, and the gases from its "
            "exhaust are harmless to the workers",
        ],
        "correct_index": 0,
        "why": "Fuel cells suit a site where noise and exhaust fumes "
               "matter, but diesel is easy to buy and store while hydrogen "
               "needs pressurised delivery and tanks.",
    },
    {
        "id": "ks4-fuel-cells-h16",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A rail operator must power trains on a long route with no "
                "overhead wires. Evaluate hydrogen fuel cells against a "
                "large battery pack.",
        "options": [
            "The battery wins, because charging equipment already stands "
            "beside every unwired line",
            "The fuel cell wins, because it gives the long range the route "
            "needs with a quick refill",
            "The fuel cell wins, because a moving train can collect the "
            "hydrogen it needs from the air",
            "The battery wins, because a battery train is unaffected by the "
            "mass that the pack adds",
        ],
        "correct_index": 1,
        "why": "A long unwired route needs range and a fast turnaround, and "
               "a hydrogen tank refills quickly while a battery big enough "
               "for the route would be heavy and slow to charge.",
    },
    {
        "id": "ks4-fuel-cells-h17",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country makes its hydrogen by electrolysis using "
                "electricity from coal-fired power stations. Explain the "
                "effect on the environmental case for its fuel cell cars.",
        "options": [
            "The case improves, because the electrolysis takes carbon "
            "dioxide back out of the coal smoke",
            "The case is unchanged, because the power station's carbon "
            "dioxide is captured by the electrolysis",
            "The case weakens, because carbon dioxide is released in "
            "generating the electricity used",
            "The case weakens, because hydrogen made from coal electricity "
            "burns far less cleanly in the cell",
        ],
        "correct_index": 2,
        "why": "Electrolysis is only as clean as the electricity driving "
               "it, so hydrogen made with coal-fired power carries the "
               "carbon dioxide released at that power station.",
    },
    {
        "id": "ks4-fuel-cells-h18",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Some countries with a great deal of cheap renewable "
                "electricity are building hydrogen plants for export. "
                "Suggest why.",
        "options": [
            "Hydrogen is simpler to ship than electricity because it needs "
            "no container to hold it",
            "Renewable electricity cannot be used in the country that "
            "generates it, so it has to be sold",
            "Hydrogen made in this way can be burned again to generate more "
            "renewable electricity",
            "Electricity is hard to store or send far, while hydrogen can "
            "be stored and shipped",
        ],
        "correct_index": 3,
        "why": "Electricity must be used as it is generated or stored at "
               "great cost, while turning it into hydrogen makes a fuel "
               "that can be kept and carried anywhere.",
    },
    {
        "id": "ks4-fuel-cells-h19",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bus company can burn hydrogen in modified engines or feed "
                "the same hydrogen to fuel cells. Justify which route gives "
                "the greater benefit.",
        "options": [
            "The fuel cells, because more of the energy is transferred "
            "usefully and no nitrogen oxides form",
            "The engines, because burning hydrogen releases all of its "
            "energy in one step with no losses",
            "The fuel cells, because burning hydrogen in an engine would "
            "release carbon dioxide as well",
            "The engines, because a fuel cell cannot supply a current large "
            "enough to drive a full bus",
        ],
        "correct_index": 0,
        "why": "Burning wastes energy as heat and reaches temperatures at "
               "which nitrogen and oxygen from the air combine, while a "
               "cell makes electricity directly and stays cool.",
    },
    {
        "id": "ks4-fuel-cells-h20",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen costs more per mile than electricity. Suggest why "
                "a bus company might still choose fuel cell buses.",
        "options": [
            "A fuel cell bus needs no driver training, and that saving is "
            "larger than the extra fuel cost",
            "Buses work long shifts, and a quick refill keeps them earning "
            "where charging would not",
            "The price of hydrogen is fixed by law, so the company can "
            "budget for its fuel bill exactly",
            "Fuel cell buses can be refuelled while carrying passengers, "
            "which battery buses cannot be",
        ],
        "correct_index": 1,
        "why": "A bus earns money only while it is on the road, so hours "
               "spent charging cost the operator more than the higher price "
               "of the fuel does.",
    },
    {
        "id": "ks4-fuel-cells-h21",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that hydrogen fuel cells will replace "
                "batteries in every kind of vehicle.",
        "options": [
            "The claim is sound, because fuel cells beat batteries on cost, "
            "range and refuelling alike",
            "The claim is unsound, because a fuel cell cannot produce "
            "enough power for a road vehicle",
            "The claim is unsound, because batteries suit short journeys "
            "where charging is easy",
            "The claim is sound, because charging points are being removed "
            "as hydrogen stations spread",
        ],
        "correct_index": 2,
        "why": "The two technologies fit different jobs: hydrogen suits "
               "heavy long-range vehicles needing a fast turnaround, while "
               "batteries suit lighter ones charged overnight.",
    },
    {
        "id": "ks4-fuel-cells-h22",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fuel cell produces 45 g of water. Determine the mass of "
                "hydrogen that reacted. (Mr: H2 = 2, H2O = 18)",
        "options": [
            "2.5 g",
            "90 g",
            "10 g",
            "5.0 g",
        ],
        "correct_index": 3,
        "why": "45 g of water is 2.5 mol, and 2H2 + O2 → 2H2O gives one "
               "mole of water for each mole of hydrogen, so the mass is "
               "2.5 × 2 = 5.0 g.",
    },
    {
        "id": "ks4-fuel-cells-h23",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the platinum in a fuel cell can be reclaimed "
                "when the cell reaches the end of its working life, and why "
                "that is worth doing.",
        "options": [
            "It is a catalyst, so it is unchanged and can be recovered for "
            "use in another cell",
            "It has turned into platinum oxide, a compound easily broken "
            "down to give the metal back",
            "It has dissolved in the electrolyte, from which the liquid is "
            "boiled off to leave the metal",
            "It is spread so thinly over the electrodes that hardly any of "
            "it is left to be recovered",
        ],
        "correct_index": 0,
        "why": "A catalyst is not consumed, so the metal is still present "
               "when the cell is dismantled, and reclaiming a rare and "
               "costly metal cuts both cost and mining.",
    },
    {
        "id": "ks4-fuel-cells-h24",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fuel cell transfers a greater proportion of "
                "its fuel's energy usefully than a power station burning the "
                "same fuel would.",
        "options": [
            "A power station loses energy because it has to cool its water "
            "right down before releasing it",
            "A cell makes electricity in one step, while a station heats "
            "water, turns a turbine and drives a generator",
            "A power station wastes energy because the hydrogen has to be "
            "compressed hard before it is burned",
            "A cell heats its hydrogen to a far higher temperature, so much "
            "less of the energy is left over",
        ],
        "correct_index": 1,
        "why": "Every extra transfer in the chain from burner to turbine to "
               "generator wastes energy as heat and friction, and a fuel "
               "cell has none of those stages.",
    },
    {
        "id": "ks4-fuel-cells-h25",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen is often described as an energy carrier rather "
                "than an energy source. Explain why.",
        "options": [
            "It carries energy along a pipeline, which no other fuel in use "
            "is able to do",
            "It carries its own oxygen with it, so the energy can be "
            "released wherever it is wanted",
            "It has to be manufactured using energy from elsewhere before "
            "it can release any",
            "It releases its energy without any chemical reaction taking "
            "place inside the cell",
        ],
        "correct_index": 2,
        "why": "Hydrogen is not found free in useful amounts, so energy "
               "from gas or from electricity must be spent making it, and "
               "the fuel then stores and moves that energy.",
    },
    {
        "id": "ks4-fuel-cells-h26",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fuel cell buses are usually refuelled at a single depot "
                "rather than at public stations. Evaluate the advantage of "
                "that arrangement.",
        "options": [
            "It removes the need for any hydrogen to be held under pressure "
            "at the depot itself",
            "It lets the whole fleet share one hydrogen tank that is passed "
            "between them each morning",
            "It means the buses can be refuelled without anybody on the "
            "site needing safety training",
            "One installation serves the whole fleet, so the infrastructure "
            "problem is far smaller",
        ],
        "correct_index": 3,
        "why": "The obstacle for private cars is that stations must be "
               "built everywhere, but a fleet that returns to one depot "
               "needs only that depot equipped.",
    },
]
