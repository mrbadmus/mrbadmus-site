"""Chemistry · Energy changes — the MRB-338 expansion, subtopic
`cells-and-batteries`.

The twelve shipped rows cover the bare construction of a simple cell, the
series-addition arithmetic, the zinc/copper polarity and the primary versus
secondary split. This file goes wider across the same spec point (4.5.2.1)
rather than round it again: the electrolyte as a component in its own right
(what makes one, concentration, temperature, volume, and the fact that
swapping it never moves the polarity), parallel wiring against series,
ranking named metal pairs from the reactivity series, the redox vocabulary
applied electrode by electrode including the mass changes, capacity in mAh
and Wh as numbers to work with, named battery chemistries matched to named
uses, the degradation of a rechargeable cell over many cycles, and the
disposal and recycling reasoning.
"""

TOPIC = "energy-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ────────────────────────────────────────────────────────────
    {
        "id": "ks4-cells-and-batteries-e05",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the direction in which electrons travel through the "
                "external circuit of a simple chemical cell.",
        "options": [
            "From the positive electrode along the wire to the negative one",
            "From the negative electrode along the wire to the positive one",
            "Out of both electrodes into the electrolyte, where the flows "
            "meet",
            "Backwards and forwards between the two electrodes, reversing "
            "several times a second",
        ],
        "correct_index": 1,
        "why": "The more reactive metal is oxidised and releases electrons, "
               "so electrons leave the negative electrode and travel round "
               "the external circuit to the positive one.",
    },
    {
        "id": "ks4-cells-and-batteries-e06",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the atoms of the more reactive metal "
                "at the negative electrode of a simple cell.",
        "options": [
            "They lose electrons and pass into the electrolyte as positively "
            "charged ions",
            "They gain electrons from the electrolyte and are deposited as a "
            "thicker coating of metal",
            "They stay locked in the metal while protons leave along the "
            "connecting wire",
            "They split into smaller atoms, and it is these that dissolve "
            "into the solution",
        ],
        "correct_index": 0,
        "why": "Oxidation is the loss of electrons, so the more reactive "
               "metal gives up electrons and its atoms enter the solution as "
               "ions.",
    },
    {
        "id": "ks4-cells-and-batteries-e07",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify a substance that would work as the electrolyte in a "
                "simple chemical cell.",
        "options": [
            "Distilled water, because its molecules carry charge from one "
            "metal to the other",
            "Copper sulfate solution, because it contains dissolved ions that "
            "are free to move",
            "Solid sodium chloride, because its ions travel freely through "
            "the giant lattice",
            "Hexane, because its molecules break up into ions as soon as a "
            "metal is dipped in",
        ],
        "correct_index": 1,
        "why": "An electrolyte is a solution or molten compound containing "
               "ions that can move, and copper sulfate solution supplies "
               "exactly that.",
    },
    {
        "id": "ks4-cells-and-batteries-e08",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one factor that affects the voltage produced by a "
                "simple chemical cell.",
        "options": [
            "The size of the two metal strips that are dipped down into the "
            "electrolyte solution",
            "The length of the connecting wire running between the electrodes",
            "The volume of electrolyte solution poured into the beaker",
            "The difference in reactivity between the two metals used",
        ],
        "correct_index": 3,
        "why": "The voltage depends on how far apart the two metals sit in "
               "the reactivity series; the further apart, the larger the "
               "voltage.",
    },
    {
        "id": "ks4-cells-and-batteries-e09",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens inside a rechargeable cell while it is "
                "being charged.",
        "options": [
            "An external supply reverses the reactions, reforming the "
            "original reactants",
            "Fresh electrons are pumped in from the mains supply and stored "
            "inside the electrolyte",
            "The two electrodes swap places so that the reaction can start "
            "over again",
            "New electrolyte is made from the products, which are themselves "
            "unchanged",
        ],
        "correct_index": 0,
        "why": "Charging drives the cell's redox reactions backwards, so the "
               "substances used up during discharge are restored.",
    },
    {
        "id": "ks4-cells-and-batteries-e10",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit that is commonly used to give the capacity of "
                "a rechargeable battery.",
        "options": [
            "Volts (V), which count the number of hours a battery will keep "
            "working for",
            "Grams (g), since a heavier battery stores a proportionally "
            "larger amount of charge",
            "Milliamp-hours (mAh), a measure of the charge the battery can "
            "supply",
            "Ohms, which measure how much energy a battery still has left to "
            "give out",
        ],
        "correct_index": 2,
        "why": "Capacity is the charge a battery can deliver, and it is "
               "quoted in milliamp-hours (or in watt-hours for the energy "
               "stored).",
    },
    {
        "id": "ks4-cells-and-batteries-e11",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "An alkaline AA cell is used once and then thrown away. State "
                "the name given to this type of cell.",
        "options": [
            "A secondary cell, because its chemical reactions can be run in "
            "either direction",
            "A fuel cell, because its reactants are supplied from outside the "
            "cell",
            "An electrolytic cell, because it makes electricity out of a "
            "liquid",
            "A primary cell, because its reactions cannot be reversed",
        ],
        "correct_index": 3,
        "why": "A primary (non-rechargeable) cell runs on irreversible "
               "reactions, so once its reactants are used up it can only be "
               "discarded.",
    },
    {
        "id": "ks4-cells-and-batteries-e12",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why used batteries should be taken to a collection "
                "point rather than put in ordinary household waste.",
        "options": [
            "They hold toxic metals that would pollute land and water in "
            "landfill",
            "They rust away in the bin, and the rust gives off a gas that "
            "damages the ozone layer",
            "They are made of glass, which has to be melted down in a "
            "separate furnace",
            "They give off carbon dioxide as they rot, adding to the "
            "greenhouse effect",
        ],
        "correct_index": 0,
        "why": "Batteries contain metals such as lead, cadmium, nickel and "
               "lithium, which are toxic and must be recovered rather than "
               "left to escape into the environment.",
    },
    # ── standard ──────────────────────────────────────────────────────────
    {
        "id": "ks4-cells-and-batteries-s05",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical 2.0 V cells are connected in parallel rather "
                "than in series. Determine the voltage across the pair.",
        "options": [
            "1.0 V",
            "2.0 V",
            "4.0 V",
            "8.0 V",
        ],
        "correct_index": 1,
        "why": "Only cells in series add their voltages; cells in parallel "
               "give the voltage of a single cell, but can supply current for "
               "longer.",
    },
    {
        "id": "ks4-cells-and-batteries-s06",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student builds a zinc and copper cell using distilled "
                "water in place of an electrolyte solution. Explain why the "
                "voltmeter reads close to zero.",
        "options": [
            "Distilled water holds almost no ions, so charge cannot be "
            "carried between the electrodes",
            "Distilled water has no charge of its own, so it cancels out the "
            "voltage of the cell",
            "Distilled water coats each of the metals in a thin oxide layer "
            "that blocks the reaction completely",
            "Distilled water makes both metals equally reactive, so there is "
            "no difference left to use",
        ],
        "correct_index": 0,
        "why": "An electrolyte must supply mobile ions to complete the "
               "circuit inside the cell, and distilled water contains far too "
               "few.",
    },
    {
        "id": "ks4-cells-and-batteries-s07",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why using a more concentrated electrolyte can "
                "increase the voltage a simple cell produces.",
        "options": [
            "A concentrated solution supplies more ions in each unit volume "
            "for the electrode reactions",
            "A concentrated solution is denser, so the electrodes sit deeper "
            "and touch more liquid",
            "A concentrated solution makes the more reactive of the two "
            "metals climb higher up the reactivity series",
            "A concentrated solution conducts heat better, so the whole cell "
            "warms itself up as it runs",
        ],
        "correct_index": 0,
        "why": "Concentration is one of the factors AQA lists: more ions per "
               "unit volume supports the reactions at the electrodes, which "
               "raises the voltage.",
    },
    {
        "id": "ks4-cells-and-batteries-s08",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A simple cell is built from a magnesium strip and a zinc "
                "strip in an electrolyte. Predict which metal becomes the "
                "negative electrode.",
        "options": [
            "Zinc, since the heavier of two metals gathers electrons at its "
            "surface",
            "Zinc, since the less reactive metal is the one that is oxidised",
            "Magnesium, since the more reactive metal is the one oxidised",
            "Magnesium, since it is the weaker conductor of the two metals",
        ],
        "correct_index": 2,
        "why": "Magnesium is above zinc in the reactivity series, so "
               "magnesium is oxidised, releases electrons, and becomes the "
               "negative electrode.",
    },
    {
        "id": "ks4-cells-and-batteries-s09",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens to the mass of the negative electrode "
                "as a simple cell is used.",
        "options": [
            "It rises, as ions from the electrolyte are deposited on the "
            "metal surface as fresh atoms",
            "It stays the same, because the electrons that leave have almost "
            "no mass",
            "It rises at first and then falls back to the value it started at",
            "It falls, as metal atoms are oxidised and pass into the solution "
            "as ions",
        ],
        "correct_index": 3,
        "why": "The more reactive metal dissolves as it is oxidised, so the "
               "negative electrode loses mass while the cell runs.",
    },
    {
        "id": "ks4-cells-and-batteries-s10",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cell is made from an aluminium strip and a copper strip in "
                "an electrolyte. Predict which metal is the positive "
                "electrode.",
        "options": [
            "Copper, because the less reactive metal takes in electrons",
            "Aluminium, because it is the more reactive of the two metals",
            "Aluminium, because its ions carry less charge than copper ions "
            "do",
            "Copper, because it is the better conductor of electricity",
        ],
        "correct_index": 0,
        "why": "Aluminium is well above copper in the reactivity series, so "
               "aluminium is oxidised and copper, the less reactive metal, is "
               "the positive electrode where reduction happens.",
    },
    {
        "id": "ks4-cells-and-batteries-s11",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A battery of capacity 2400 mAh supplies a steady current of "
                "300 mA. Calculate how long it can run the device.",
        "options": [
            "0.125 hours",
            "8 hours",
            "80 hours",
            "2100 hours",
        ],
        "correct_index": 1,
        "why": "Time = capacity ÷ current = 2400 mAh ÷ 300 mA = 8 hours.",
    },
    {
        "id": "ks4-cells-and-batteries-s12",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a petrol car is fitted with a lead-acid battery "
                "rather than a set of alkaline cells.",
        "options": [
            "Lead-acid cells are lighter, so the car burns less fuel as it "
            "drives",
            "Lead-acid cells last the life of a car, while alkaline cells "
            "wear out fast",
            "Lead-acid cells are rechargeable, so the car's alternator can "
            "restore them as it drives",
            "Lead-acid cells hold no toxic metals, so scrapping the car is "
            "simpler",
        ],
        "correct_index": 2,
        "why": "A lead-acid battery is a secondary cell whose reactions are "
               "reversible, so the car recharges it in use instead of "
               "replacing it after every start.",
    },
    {
        "id": "ks4-cells-and-batteries-s13",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A model train controller is powered by five identical cells "
                "joined in series, giving 6.5 V in total. Calculate the "
                "voltage of one cell.",
        "options": [
            "0.77 V",
            "1.3 V",
            "3.3 V",
            "32.5 V",
        ],
        "correct_index": 1,
        "why": "Cells in series add, so each cell contributes 6.5 V ÷ 5 = 1.3 "
               "V.",
    },
    {
        "id": "ks4-cells-and-batteries-s14",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how plugging a lithium-ion cell into a charger "
                "allows it to be used again.",
        "options": [
            "The charger tops the cell up with fresh electrolyte drawn from "
            "the mains supply",
            "The charger heats the electrodes so that the reaction products "
            "evaporate away",
            "The charger pushes current the other way, reversing the "
            "reactions and remaking the reactants",
            "The charger removes the products, leaving the reactants behind "
            "untouched",
        ],
        "correct_index": 2,
        "why": "In a secondary cell the reactions are reversible, so an "
               "external supply driving current backwards converts the "
               "products back into the original reactants.",
    },
    {
        "id": "ks4-cells-and-batteries-s15",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why warming the electrolyte can change the voltage "
                "that a simple cell produces.",
        "options": [
            "Warming turns some of the electrolyte into a gas, so fewer ions "
            "are left in the beaker",
            "Warming raises the temperature at which the two metals begin to "
            "melt into the solution",
            "Warming makes the more reactive metal expand, giving it a larger "
            "surface to react with",
            "Warming alters the rate of the reactions at the electrodes, and "
            "so the voltage produced",
        ],
        "correct_index": 3,
        "why": "Temperature is one of the factors AQA lists: it changes how "
               "fast the electrode reactions proceed, and so the voltage the "
               "cell gives.",
    },
    {
        "id": "ks4-cells-and-batteries-s16",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the electrolyte in a simple cell must be a "
                "solution or a molten compound rather than a solid.",
        "options": [
            "A solid contains no ions, so there would be nothing there to "
            "carry the charge",
            "A solid is heavier than a solution, so the electrodes could not "
            "be held upright in it",
            "A solid has no electrons of its own, whereas a solution borrows "
            "them from the metals",
            "A solid holds its ions fixed in place, so they cannot move to "
            "carry charge across the cell",
        ],
        "correct_index": 3,
        "why": "Ions only become mobile when an ionic compound is dissolved "
               "or melted, and mobile ions are what complete the circuit "
               "inside the cell.",
    },
    {
        "id": "ks4-cells-and-batteries-s17",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the energy transfer that takes place in a chemical "
                "cell while it is supplying a circuit.",
        "options": [
            "Electrical energy from the circuit is transferred to a chemical "
            "store in the electrolyte",
            "Energy from a chemical store is transferred electrically to the "
            "circuit",
            "Thermal energy from the room is transferred electrically to the "
            "circuit",
            "Energy stored in the electrons themselves is transferred to the "
            "two metals",
        ],
        "correct_index": 1,
        "why": "A chemical cell transfers energy from the chemical store of "
               "its reactants to the circuit by an electric current; charging "
               "a secondary cell runs that transfer the other way.",
    },
    {
        "id": "ks4-cells-and-batteries-s18",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pacemaker is sealed inside a patient's chest. Suggest why "
                "it is fitted with a long-life primary cell.",
        "options": [
            "A primary cell gives a considerably higher voltage than any "
            "rechargeable cell of the same size",
            "A primary cell contains no metals, so it cannot harm the patient "
            "if the casing leaks",
            "A primary cell works steadily for years with no access needed to "
            "recharge it",
            "A primary cell recharges itself from the warmth of the body, so "
            "it lasts indefinitely",
        ],
        "correct_index": 2,
        "why": "A sealed implant cannot be plugged in, so a cell that "
               "delivers a small, steady current for years without recharging "
               "is the sensible choice.",
    },
    {
        "id": "ks4-cells-and-batteries-s19",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe why the capacity of a rechargeable battery falls "
                "after it has been through many charge and discharge cycles.",
        "options": [
            "The battery slowly fills up with electrons that it cannot push "
            "out again",
            "The electrolyte leaks out through the casing, leaving the "
            "electrodes dry",
            "The battery charges to a lower voltage each time, so it stores "
            "less",
            "The electrode materials degrade with repeated cycling, so less "
            "charge can be stored",
        ],
        "correct_index": 3,
        "why": "Repeated cycling damages the electrode materials, so a "
               "fully-charged old battery holds less charge than it did when "
               "it was new.",
    },
    {
        "id": "ks4-cells-and-batteries-s20",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one benefit, other than reduced pollution, of "
                "collecting used batteries for recycling.",
        "options": [
            "Metals such as nickel and lithium are recovered, so less ore has "
            "to be mined",
            "The charge left in each spent cell is collected and fed back "
            "into the National Grid supply",
            "Recycled cells are returned to the shops and sold on as new "
            "cells once again",
            "The plastic casings are burned, which produces electricity "
            "without any waste",
        ],
        "correct_index": 0,
        "why": "Recycling recovers valuable metals from spent cells, reducing "
               "the quantity of ore that must be extracted and processed.",
    },
    {
        "id": "ks4-cells-and-batteries-s21",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe, in terms of electrons, what takes place at the "
                "positive electrode of a simple chemical cell.",
        "options": [
            "Electrons are gained, so the species there is being reduced",
            "Electrons are lost, so the species there is being oxidised",
            "Electrons are shared between the metal and the ions in solution",
            "Electrons are manufactured from the metal atoms and sent out "
            "along the wire",
        ],
        "correct_index": 0,
        "why": "Reduction is the gain of electrons, and it happens at the "
               "positive electrode, which is made of the less reactive metal.",
    },
    {
        "id": "ks4-cells-and-batteries-s22",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A working cell is altered by lifting one electrode clear of "
                "the liquid while the wires stay joined. Explain why the "
                "voltmeter now reads zero.",
        "options": [
            "The lifted electrode cools, so its reaction is too slow to give "
            "a reading",
            "The lifted electrode is no longer in the electrolyte, so ions "
            "cannot complete the circuit",
            "The lifted electrode loses its charge to the air surrounding the "
            "apparatus",
            "The lifted electrode reacts with oxygen instead, which produces "
            "no voltage",
        ],
        "correct_index": 1,
        "why": "The circuit is completed by ions moving through the "
               "electrolyte, so an electrode out of the solution breaks that "
               "path and no current flows.",
    },
    {
        "id": "ks4-cells-and-batteries-s23",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wind farm stores surplus electricity in a large battery "
                "installation. Explain why secondary cells are used for this.",
        "options": [
            "Secondary cells give out no heat at any stage, so none of the "
            "stored energy is wasted in the store",
            "Secondary cells produce electricity from the wind directly, with "
            "no turbine needed",
            "Secondary cells hold a far higher voltage per cell than any "
            "primary cell can reach",
            "Secondary cells can be charged and discharged repeatedly as "
            "supply and demand change",
        ],
        "correct_index": 3,
        "why": "Grid storage has to absorb and release energy over and over, "
               "which only a rechargeable cell with reversible reactions can "
               "do.",
    },
    {
        "id": "ks4-cells-and-batteries-s24",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A phone battery is rated 4000 mAh and a tablet battery 8000 "
                "mAh. Both devices draw the same steady current. Compare how "
                "long each runs.",
        "options": [
            "The tablet runs for twice as long as the phone",
            "The phone runs for twice as long as the tablet",
            "Both run for the same length of time",
            "The tablet runs for four times as long as the phone",
        ],
        "correct_index": 0,
        "why": "At the same current, running time is proportional to "
               "capacity, and 8000 mAh is double 4000 mAh.",
    },
    {
        "id": "ks4-cells-and-batteries-s25",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe one change to a zinc and copper cell that would "
                "give a larger voltage, and justify the change.",
        "options": [
            "Use a much larger strip of zinc, so that more atoms are able to "
            "react at once",
            "Replace the zinc with magnesium, which sits further from copper "
            "in the reactivity series",
            "Use a longer connecting wire, so that the electrons gather more "
            "push on the way round",
            "Replace the copper with a second strip of zinc, so both "
            "electrodes react together",
        ],
        "correct_index": 1,
        "why": "Voltage depends on the gap between the two metals in the "
               "reactivity series, and magnesium is further from copper than "
               "zinc is.",
    },
    {
        "id": "ks4-cells-and-batteries-s26",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a zinc-carbon cell cannot be recharged.",
        "options": [
            "Its reactions are irreversible, so a supply cannot restore the "
            "original reactants",
            "Its two electrodes are made from the same material, so charging "
            "the cell would have no effect",
            "Its casing is sealed, so a charging current has no route into "
            "the chemicals inside",
            "Its electrolyte is a paste, and a charging current passes "
            "through liquids alone",
        ],
        "correct_index": 0,
        "why": "A primary cell's redox reactions cannot be driven backwards, "
               "so no external supply can rebuild the reactants that have "
               "been used up.",
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "ks4-cells-and-batteries-h05",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Three cells are built, each with silver as one electrode and "
                "magnesium, zinc or copper as the other. Predict the order of "
                "their voltages, largest first.",
        "options": [
            "Copper-silver, then zinc-silver, then magnesium-silver",
            "Zinc-silver, then copper-silver, then magnesium-silver",
            "Magnesium-silver, then zinc-silver, then copper-silver",
            "All three give the same voltage, since silver is shared by them",
        ],
        "correct_index": 2,
        "why": "Voltage grows with the reactivity gap, and magnesium is "
               "furthest from silver, then zinc, with copper the nearest to "
               "it.",
    },
    {
        "id": "ks4-cells-and-batteries-h06",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A zinc and copper cell is rebuilt with its copper sulfate "
                "solution replaced by dilute sulfuric acid. Predict the "
                "effect on the cell.",
        "options": [
            "The voltage may change, and copper becomes the negative "
            "electrode instead",
            "The voltage stays exactly as it was, since the electrolyte plays "
            "no part in how a cell works",
            "The voltage falls to zero, because an acid attacks both of the "
            "metal electrodes",
            "The voltage may change, but zinc remains the negative electrode",
        ],
        "correct_index": 3,
        "why": "The electrolyte is one of the factors that affects the size "
               "of the voltage, but polarity is fixed by which metal is more "
               "reactive, and zinc is still above copper.",
    },
    {
        "id": "ks4-cells-and-batteries-h07",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four identical 3.7 V lithium-ion cells are joined in series "
                "to make a pack. Two such packs are then joined in parallel. "
                "Determine the voltage supplied.",
        "options": [
            "3.7 V",
            "7.4 V",
            "14.8 V",
            "29.6 V",
        ],
        "correct_index": 2,
        "why": "The series pack gives 4 × 3.7 V = 14.8 V, and joining two "
               "identical packs in parallel leaves the voltage unchanged "
               "while doubling the charge available.",
    },
    {
        "id": "ks4-cells-and-batteries-h08",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A battery rated 3000 mAh when new falls to 80% of that "
                "capacity after several years. Determine how long it then "
                "runs a device drawing 250 mA.",
        "options": [
            "9.6 hours",
            "12.0 hours",
            "15.0 hours",
            "2.4 hours",
        ],
        "correct_index": 0,
        "why": "80% of 3000 mAh is 2400 mAh, and 2400 mAh ÷ 250 mA = 9.6 "
               "hours.",
    },
    {
        "id": "ks4-cells-and-batteries-h09",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the choice of lithium-ion rather than lead-acid "
                "cells for the main battery of an electric car.",
        "options": [
            "Lead-acid cells cannot be recharged, so an electric car fitted "
            "with them could be driven once",
            "Lithium-ion cells store more energy per kilogram, though they "
            "contain metals that need recycling",
            "Lead-acid cells contain no toxic metals, so they would be the "
            "greener choice for a car",
            "Lithium-ion cells are primary cells, so the car's battery would "
            "be swapped at each charging stop",
        ],
        "correct_index": 1,
        "why": "Both are secondary cells, but lithium-ion packs store far "
               "more energy for their mass, which is what gives a car useful "
               "range; their metals still have to be recovered at end of "
               "life.",
    },
    {
        "id": "ks4-cells-and-batteries-h10",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a zinc and copper cell standing in copper sulfate "
                "solution, explain the mass changes at the two electrodes.",
        "options": [
            "Both electrodes lose mass, since both metals are oxidised into "
            "the surrounding solution",
            "Both electrodes gain mass, since ions are deposited on each of "
            "them as the cell runs",
            "Zinc gains mass as ions land on it, while copper loses mass as "
            "it dissolves away",
            "Zinc loses mass as it is oxidised, while copper gains mass as "
            "copper ions are reduced onto it",
        ],
        "correct_index": 3,
        "why": "Zinc is oxidised and dissolves as Zn2+ ions, while Cu2+ ions "
               "from the solution are reduced and deposited on the copper "
               "electrode.",
    },
    {
        "id": "ks4-cells-and-batteries-h11",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that using a thicker strip of zinc in a "
                "zinc and copper cell will raise its voltage. Evaluate this "
                "claim.",
        "options": [
            "The claim is correct, because a thicker strip has more atoms "
            "ready to give up electrons",
            "The claim is correct, because a thicker strip is a better "
            "conductor and so wastes less voltage",
            "The claim is wrong: the voltage is set by the reactivity gap, "
            "though the cell may last longer",
            "The claim is wrong: a thicker strip reduces the voltage, because "
            "the ions then have much further to travel",
        ],
        "correct_index": 2,
        "why": "Voltage depends on the difference in reactivity between the "
               "two metals, not on how much metal is present; a larger "
               "electrode simply provides more reactant.",
    },
    {
        "id": "ks4-cells-and-batteries-h12",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A device needs 4.8 V and must run for as long as possible. "
                "Describe how to connect eight identical 1.2 V cells to "
                "achieve this.",
        "options": [
            "Connect all eight cells in series, giving a much higher voltage "
            "for a longer time",
            "Connect all eight cells in parallel, since parallel wiring adds "
            "the voltages together",
            "Connect four cells in series and leave the other four "
            "unconnected as spares",
            "Connect two sets of four cells in series, then join the two sets "
            "in parallel",
        ],
        "correct_index": 3,
        "why": "Four cells in series give 4 × 1.2 V = 4.8 V, and putting a "
               "second identical set in parallel keeps that voltage while "
               "doubling the charge available.",
    },
    {
        "id": "ks4-cells-and-batteries-h13",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A five-year-old phone is charged to 100% but runs for far "
                "less time than it did when new. Explain this observation.",
        "options": [
            "The charger has worn out and now stops before the battery is "
            "properly full",
            "The battery voltage has halved with age, so the phone draws "
            "twice the current",
            "The battery has absorbed water vapour from the air, which "
            "dilutes the electrolyte inside it",
            "Repeated cycling has degraded the electrodes, so 100% now "
            "represents less charge",
        ],
        "correct_index": 3,
        "why": "The percentage is a fraction of the battery's present "
               "capacity, and cycling has reduced that capacity, so a full "
               "old battery holds less charge than a full new one.",
    },
    {
        "id": "ks4-cells-and-batteries-h14",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that recycling household batteries is "
                "unnecessary because each cell is small.",
        "options": [
            "The claim is sound, because the metals in a cell are harmless "
            "once the cell is flat",
            "The claim is sound, because small cells break down quickly and "
            "leave nothing behind",
            "The claim is weak: billions are discarded, and their toxic "
            "metals build up in the environment",
            "The claim is weak: small cells hold more toxic metal than large "
            "ones of the same type",
        ],
        "correct_index": 2,
        "why": "The hazard is cumulative — vast numbers of small cells carry "
               "a large total mass of lead, cadmium, nickel and lithium, "
               "which recycling keeps out of land and water.",
    },
    {
        "id": "ks4-cells-and-batteries-h15",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A camera needs a supply of 7.2 V. Determine how many 1.2 V "
                "nickel-metal hydride cells must be connected in series.",
        "options": [
            "4 cells",
            "5 cells",
            "6 cells",
            "9 cells",
        ],
        "correct_index": 2,
        "why": "Series voltages add, so the number of cells is 7.2 V ÷ 1.2 V "
               "= 6.",
    },
    {
        "id": "ks4-cells-and-batteries-h16",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A battery of six identical cells in series measures 8.4 V. "
                "Determine the voltage of a battery built from ten of the "
                "same cells in series.",
        "options": [
            "1.4 V",
            "10.0 V",
            "14.0 V",
            "84.0 V",
        ],
        "correct_index": 2,
        "why": "Each cell gives 8.4 V ÷ 6 = 1.4 V, so ten of them in series "
               "give 10 × 1.4 = 14.0 V.",
    },
    {
        "id": "ks4-cells-and-batteries-h17",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One 1.5 V cell and two 3.7 V cells are connected in series "
                "in a single loop. Determine the total voltage.",
        "options": [
            "2.2 V",
            "5.2 V",
            "8.9 V",
            "20.5 V",
        ],
        "correct_index": 2,
        "why": "Series voltages add whatever their sizes: 1.5 + 3.7 + 3.7 = "
               "8.9 V.",
    },
    {
        "id": "ks4-cells-and-batteries-h18",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the concentration of the electrolyte affects a "
                "cell's voltage but simply using a bigger volume of the same "
                "solution does not.",
        "options": [
            "A bigger volume dilutes the solution, so its concentration drops "
            "and cancels the gain",
            "Concentration sets how crowded the ions are, while a larger "
            "volume adds reactant without changing that",
            "A bigger volume cools the cell down, and the two effects balance "
            "one another exactly",
            "Concentration alters the reactivity of each metal, while volume "
            "alters the size of the electrodes",
        ],
        "correct_index": 1,
        "why": "Voltage responds to how concentrated the electrolyte is, not "
               "to how much of it there is; extra solution of the same "
               "concentration lets the cell run longer instead.",
    },
    {
        "id": "ks4-cells-and-batteries-h19",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student rubs the magnesium electrode of a magnesium and "
                "copper cell with emery paper, and the voltage rises. Suggest "
                "an explanation.",
        "options": [
            "Rubbing removes the dull oxide layer, exposing magnesium metal "
            "to the electrolyte",
            "Rubbing charges the strip with static electricity, adding to the "
            "cell's voltage",
            "Rubbing makes the strip thinner, and a thin electrode gives a "
            "larger voltage",
            "Rubbing adds particles of emery to the metal, and these react "
            "with the electrolyte",
        ],
        "correct_index": 0,
        "why": "Magnesium carries a surface layer of oxide that gets between "
               "the metal and the electrolyte; cleaning it off lets the "
               "magnesium itself take part.",
    },
    {
        "id": "ks4-cells-and-batteries-h20",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A designer connects four identical cells in parallel instead "
                "of in series. Describe the effect on the voltage and on how "
                "long the battery lasts.",
        "options": [
            "The voltage is four times that of one cell, and it lasts as long "
            "as one cell would",
            "The voltage is a quarter that of one cell, and the battery lasts "
            "four times as long as one cell",
            "The voltage and the lifetime are both four times those of a "
            "single cell on its own",
            "The voltage equals that of one cell, and the battery lasts about "
            "four times as long",
        ],
        "correct_index": 3,
        "why": "Parallel cells share the current rather than adding voltages, "
               "so the voltage matches a single cell while the charge "
               "available is the sum of all four.",
    },
    {
        "id": "ks4-cells-and-batteries-h21",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A battery is labelled 3.7 V and 2000 mAh. Calculate the "
                "energy it stores, in watt-hours.",
        "options": [
            "0.54 Wh",
            "7.4 Wh",
            "74 Wh",
            "7400 Wh",
        ],
        "correct_index": 1,
        "why": "2000 mAh is 2.0 Ah, and energy in watt-hours is voltage × "
               "charge = 3.7 V × 2.0 Ah = 7.4 Wh.",
    },
    {
        "id": "ks4-cells-and-batteries-h22",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Pack A is rated 12 V and 4.0 Ah; pack B is rated 8.0 V and "
                "10 Ah. Determine which pack stores more energy, and by how "
                "much.",
        "options": [
            "Pack A, by 32 Wh",
            "Pack B, by 32 Wh",
            "Pack A, by 48 Wh",
            "They store equal energy",
        ],
        "correct_index": 1,
        "why": "Energy = voltage × charge, so pack A holds 12 × 4.0 = 48 Wh "
               "and pack B holds 8.0 × 10 = 80 Wh, a difference of 32 Wh.",
    },
    {
        "id": "ks4-cells-and-batteries-h23",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a working zinc and copper cell the copper electrode is "
                "swapped for an iron one. Predict the effect on the voltage "
                "and explain your prediction.",
        "options": [
            "It falls, because iron sits closer to zinc in the reactivity "
            "series than copper does",
            "It rises, because iron is a poorer conductor and so holds back "
            "more of the charge",
            "It stays the same, because the voltage depends on the "
            "electrolyte and not the metals",
            "It falls to zero, because iron and zinc are both transition "
            "metals with similar reactivities",
        ],
        "correct_index": 0,
        "why": "Voltage grows with the reactivity gap; iron lies between zinc "
               "and copper, so swapping copper for iron narrows the gap and "
               "the voltage drops.",
    },
    {
        "id": "ks4-cells-and-batteries-h24",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four identical 1.5 V cells are wired in one series loop, but "
                "a technician fits one of them the wrong way round. Determine "
                "the voltage of the battery.",
        "options": [
            "6.0 V",
            "4.5 V",
            "3.0 V",
            "0 V",
        ],
        "correct_index": 2,
        "why": "The reversed cell opposes the others, so the battery gives (3 "
               "× 1.5) − 1.5 = 3.0 V.",
    },
    {
        "id": "ks4-cells-and-batteries-h25",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what happens at the electrodes of a rechargeable "
                "cell while it is discharging with what happens while it is "
                "charging.",
        "options": [
            "The same reactions run in the same direction both times; "
            "charging merely speeds them up",
            "Discharging oxidises the more reactive electrode; charging "
            "drives that reaction backwards",
            "Discharging reduces the more reactive electrode; charging "
            "oxidises the less reactive one",
            "Discharging uses the electrolyte, while charging works entirely "
            "through the external wires",
        ],
        "correct_index": 1,
        "why": "Discharge is the spontaneous redox reaction of the cell; "
               "charging uses an external supply to force that reaction in "
               "reverse and restore the reactants.",
    },
    {
        "id": "ks4-cells-and-batteries-h26",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Three identical cells, each of capacity 2500 mAh, are "
                "connected in parallel. Determine the total capacity of the "
                "arrangement.",
        "options": [
            "833 mAh",
            "2500 mAh",
            "5000 mAh",
            "7500 mAh",
        ],
        "correct_index": 3,
        "why": "Cells in parallel share the current, so the charge each can "
               "supply adds up: 3 × 2500 mAh = 7500 mAh.",
    },
]
