"""Physics · Atomic structure — the MRB-338 expansion of `nuclear-fission`.

One leaf only: AQA 8463 §6.4.5.1, physics only — the induced splitting of a
large nucleus, the chain reaction, critical mass, and the reactor built round
all three.

The original twelve rows in `atomic_structure__b.py` take the definition, the
absorbed neutron, the two fissile nuclides, the moderator's job, the products
of one event, how a chain reaction continues, the barium/krypton neutron
count, critical mass, reactor against weapon, the sub-critical lump, the
moderator/control-rod confusion and the low-carbon evaluation.

This file works the part of the reactor those rows never reach: the CONTROL
RODS by name and material, the COOLANT and the path from core to turbine to
grid, the ENRICHMENT of the fuel, the uranium-236 intermediate, E = mc² and
the 200 MeV scale, why fission is induced rather than spontaneous, and why
the fragments left behind are radioactive. Its two nuclear-equation rows ask
for the missing NUCLIDE rather than the neutron count, so neither shares a
frame with the existing `s03`.

⚠️ Every nuclear equation in this file was balanced twice, mass number and
atomic number separately, as part of the cold read.

This is a physics-only Triple subtopic, so every row carries
`triple_only=True` at `foundation` tier. Working lives in `why`, never in an
option.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The named components, the energy scale, and the induced-not-spontaneous
    # distinction.
    {
        "id": "ks4-nuclear-fission-e05",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name a material used to make the control rods in a nuclear "
                "reactor.",
        "options": [
            "Graphite",
            "Boron",
            "Aluminium",
            "Copper",
        ],
        "correct_index": 1,
        "why": "Control rods are made of boron or cadmium, because both "
               "absorb neutrons strongly.",
    },
    {
        "id": "ks4-nuclear-fission-e06",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the job of the coolant in a nuclear reactor.",
        "options": [
            "It absorbs spare neutrons so the reaction cannot grow",
            "It slows the neutrons down so they can be captured",
            "It carries thermal energy away from the core to the steam "
            "generator",
            "It shields the operators from the gamma radiation in the core",
        ],
        "correct_index": 2,
        "why": "The coolant, usually water or carbon dioxide, transfers the "
               "energy released by fission out of the core so it can be used.",
    },
    {
        "id": "ks4-nuclear-fission-e07",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name two materials commonly used as the moderator in a "
                "reactor.",
        "options": [
            "Boron and cadmium",
            "Lead and concrete",
            "Water and graphite",
            "Uranium and plutonium",
        ],
        "correct_index": 2,
        "why": "Water and graphite are both made of light atoms, which slow "
               "neutrons efficiently by repeated collisions.",
    },
    {
        "id": "ks4-nuclear-fission-e08",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the rate of fission when the control "
                "rods are pushed further into the core.",
        "options": [
            "It falls, because more neutrons are absorbed before they reach a "
            "nucleus",
            "It rises, because the rods slow the neutrons and make fission "
            "more likely, which is why they are withdrawn to shut a reactor "
            "down",
            "It stays the same, because the rods only shield the operators "
            "outside",
            "It rises, because the rods push the fuel rods closer together",
        ],
        "correct_index": 0,
        "why": "Control rods take neutrons out of the chain, so the deeper "
               "they go the fewer fissions follow each one.",
    },
    {
        "id": "ks4-nuclear-fission-e09",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the thermal energy produced in a reactor core is "
                "used for.",
        "options": [
            "To melt the fuel rods so fresh uranium can be added",
            "To boil water into steam, which drives a turbine and a generator",
            "To keep the moderator warm enough to slow the neutrons",
            "To split further uranium nuclei by heating them until they break "
            "apart into two halves",
        ],
        "correct_index": 1,
        "why": "A nuclear station is a steam station: the core is the heat "
               "source, and everything after it is a conventional turbine and "
               "generator.",
    },
    {
        "id": "ks4-nuclear-fission-e10",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State roughly what proportion of the uranium in a reactor's "
                "fuel rods is uranium-235.",
        "options": [
            "About 3 to 5 per cent",
            "About 50 per cent",
            "About 90 per cent",
            "Very nearly all of it",
        ],
        "correct_index": 0,
        "why": "Reactor fuel is enriched only to a few per cent uranium-235; "
               "the rest is uranium-238.",
    },
    {
        "id": "ks4-nuclear-fission-e11",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which nucleus exists for an instant after a "
                "uranium-235 nucleus absorbs a neutron.",
        "options": [
            "Uranium-234",
            "Uranium-236",
            "Plutonium-239",
            "Uranium-238",
        ],
        "correct_index": 1,
        "why": "Absorbing one neutron raises the mass number by one, giving a "
               "highly unstable uranium-236 nucleus that splits almost "
               "immediately.",
    },
    {
        "id": "ks4-nuclear-fission-e12",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the equation that links the mass lost in a fission "
                "event to the energy released.",
        "options": [
            "E = mgh",
            "E = mc²",
            "E = ½mv²",
            "E = mcΔT",
        ],
        "correct_index": 1,
        "why": "The products weigh slightly less than the reactants, and that "
               "mass difference appears as energy through E = mc².",
    },
    {
        "id": "ks4-nuclear-fission-e13",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State approximately how much energy a single fission of "
                "uranium-235 releases.",
        "options": [
            "About 2 eV",
            "About 200 eV",
            "About 200 MeV",
            "About 200 J",
        ],
        "correct_index": 2,
        "why": "One fission releases about 200 MeV, which is some fifty "
               "million times more than a single chemical reaction such as "
               "burning a carbon atom.",
    },
    {
        "id": "ks4-nuclear-fission-e14",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how nuclear fission differs from radioactive decay.",
        "options": [
            "Fission has to be triggered by an absorbed neutron, while decay "
            "happens on its own",
            "Fission releases no energy, while decay releases a great deal of "
            "it",
            "Fission happens only to small nuclei, while decay happens only "
            "to large ones",
            "Fission changes the atomic number, while decay leaves it "
            "unchanged",
        ],
        "correct_index": 0,
        "why": "Decay is spontaneous and cannot be controlled; fission of "
               "uranium-235 is induced by a neutron, which is exactly why a "
               "reactor can be controlled at all.",
    },
    {
        "id": "ks4-nuclear-fission-e15",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to a chain reaction in a mass of fissile "
                "material larger than the critical mass.",
        "options": [
            "It dies out, because the extra material absorbs the neutrons",
            "It is sustained, and will grow unless something removes neutrons",
            "It never starts, because the neutrons cannot reach the centre of "
            "the material",
            "It continues at a fixed rate that cannot be altered",
        ],
        "correct_index": 1,
        "why": "Above the critical mass enough neutrons are captured rather "
               "than lost, so the reaction sustains itself and needs control "
               "rods to hold it steady.",
    },
    {
        "id": "ks4-nuclear-fission-e16",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to the two smaller nuclei produced when "
                "a large nucleus splits.",
        "options": [
            "Isotopes",
            "Fission fragments",
            "Alpha particles",
            "Ions",
        ],
        "correct_index": 1,
        "why": "The two daughter nuclei left after a split are called fission "
               "fragments, and both are themselves unstable.",
    },
    {
        "id": "ks4-nuclear-fission-e17",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a reactor core is surrounded by a thick concrete "
                "shield.",
        "options": [
            "To absorb the radiation, so people outside receive a very small "
            "dose",
            "To slow the neutrons down before they escape into the building",
            "To keep the core warm enough for fission to continue",
            "To hold the fuel rods in position while the reactor is running",
        ],
        "correct_index": 0,
        "why": "The core is an intense source of penetrating radiation, so "
               "metres of dense concrete stand between it and everyone "
               "working outside.",
    },
    {
        "id": "ks4-nuclear-fission-e18",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how much carbon dioxide a nuclear power station gives "
                "off while it is generating electricity.",
        "options": [
            "About the same as a gas-fired station of the same output",
            "Almost none, because nothing is being burned",
            "More than a coal station, because of the heat produced",
            "None at any stage, including building and decommissioning, when "
            "the site is first prepared",
        ],
        "correct_index": 1,
        "why": "The energy comes from splitting nuclei rather than from a "
               "combustion reaction, so the generating process itself "
               "releases essentially no carbon dioxide.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # Balancing a fission equation for the missing nuclide, the control-rod
    # mechanism, the energy path, and what enrichment is for.
    {
        "id": "ks4-nuclear-fission-s05",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how an operator uses the control rods to hold a "
                "reactor's power output steady.",
        "options": [
            "The rods are moved until, on average, one neutron from each "
            "fission goes on to cause exactly one more",
            "The rods are pushed fully in, which fixes the number of fissions "
            "at a constant value for as long as they stay there during a shift",
            "The rods are withdrawn a little further every hour, to make up "
            "for the fuel being used up inside the fuel rods",
            "The rods are used to add extra neutrons whenever the power "
            "output starts to drop",
        ],
        "correct_index": 0,
        "why": "Steady power means each generation of fissions is the same "
               "size as the last, and the rods are adjusted to absorb exactly "
               "the surplus neutrons.",
    },
    {
        "id": "ks4-nuclear-fission-s06",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a moderator is made of light atoms such as those "
                "in water or graphite rather than of a heavy metal like lead.",
        "options": [
            "Light atoms are cheaper, and a moderator has to fill a very large "
            "volume around every one of the fuel rods inside the core",
            "A neutron transfers much more of its energy when it collides "
            "with a light nucleus, so it slows down in fewer collisions",
            "Heavy nuclei are shielded from neutrons by their much larger "
            "clouds of electrons, whatever speed the neutron happens to be "
            "travelling at",
            "Light atoms attract neutrons electrically, which draws them "
            "towards the fuel",
        ],
        "correct_index": 1,
        "why": "A collision with a nucleus of similar mass transfers the most "
               "energy, so a neutron slows quickly in water but bounces off a "
               "heavy nucleus with almost its original speed.",
    },
    {
        "id": "ks4-nuclear-fission-s07",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why nuclear fission in a reactor is described as an "
                "induced process.",
        "options": [
            "It is caused by heating the fuel to a very high temperature",
            "It happens only when the fuel is compressed by the pressure "
            "vessel",
            "It has to be started by a neutron being absorbed, rather than "
            "happening of its own accord",
            "It is driven by an electric current passed through the fuel rods",
        ],
        "correct_index": 2,
        "why": "Uranium-235 sits stable in a fuel rod until a neutron arrives; "
               "because the trigger is external, the rate can be raised and "
               "lowered at will.",
    },
    {
        "id": "ks4-nuclear-fission-s08",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A uranium-235 nucleus absorbs a neutron and splits into "
                "strontium-90, three neutrons and one other nucleus. "
                "Determine the mass number of that other nucleus.",
        "options": [
            "145",
            "143",
            "146",
            "140",
        ],
        "correct_index": 1,
        "why": "Mass number is conserved: 235 + 1 = 236, and 236 − 90 − 3 = "
               "143.",
    },
    {
        "id": "ks4-nuclear-fission-s09",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Uranium has an atomic number of 92 and strontium 38. In the "
                "fission of uranium-235 into strontium-90, three neutrons and "
                "one other nucleus, determine the atomic number of that other "
                "nucleus.",
        "options": [
            "54",
            "56",
            "51",
            "130",
        ],
        "correct_index": 0,
        "why": "A neutron has no charge, so atomic number is conserved "
               "between the uranium and the two fragments: 92 − 38 = 54.",
    },
    {
        "id": "ks4-nuclear-fission-s10",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the sequence by which energy released in a reactor "
                "core ends up as electricity.",
        "options": [
            "Core heats the coolant, coolant boils water, steam turns a "
            "turbine, turbine turns a generator",
            "Core emits gamma rays, gamma rays strike a solar panel, panel "
            "produces a current",
            "Core produces neutrons, neutrons flow along the cables as an "
            "electric current",
            "Core heats the control rods, hot rods produce a voltage across "
            "the pressure vessel and its casing and the shielding around it",
        ],
        "correct_index": 0,
        "why": "Everything after the core is conventional power-station "
               "engineering; fission simply replaces the furnace.",
    },
    {
        "id": "ks4-nuclear-fission-s11",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why one kilogram of uranium fuel releases far more "
                "energy than one kilogram of coal.",
        "options": [
            "Uranium atoms are heavier, so a kilogram of uranium contains more "
            "atoms than a kilogram of coal of the same grade does",
            "Each fission releases millions of times more energy than each "
            "chemical reaction in burning coal",
            "Uranium burns at a much higher temperature than coal does",
            "Coal releases most of its energy as light, which cannot be used "
            "to drive a turbine",
        ],
        "correct_index": 1,
        "why": "A chemical reaction rearranges electrons and releases a few "
               "electronvolts; a fission rearranges a nucleus and releases "
               "about 200 million.",
    },
    {
        "id": "ks4-nuclear-fission-s12",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the fuel in a power reactor cannot produce an "
                "explosion like a nuclear weapon.",
        "options": [
            "Reactor fuel is only a few per cent uranium-235, far too dilute "
            "for the runaway reaction a weapon needs",
            "Reactor fuel is made of uranium-238, which cannot undergo fission "
            "under any conditions, however many neutrons it absorbs",
            "The coolant absorbs all the energy released, so no explosion is "
            "possible even if the control rods were removed",
            "A reactor contains less than the critical mass of fuel at any "
            "time",
        ],
        "correct_index": 0,
        "why": "A weapon needs uranium enriched to well over ninety per cent; "
               "at a few per cent the neutrons are absorbed or lost long "
               "before the reaction could grow that fast.",
    },
    {
        "id": "ks4-nuclear-fission-s13",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the uranium-238 that makes up most of a fuel rod "
                "contributes little to the chain reaction.",
        "options": [
            "Uranium-238 has no neutrons to release, so it cannot pass the "
            "reaction on",
            "Uranium-238 is not radioactive, so nothing happens to it in the "
            "core",
            "Uranium-238 does not split when it absorbs a slow neutron, "
            "whereas uranium-235 does",
            "Uranium-238 is held in a separate part of the reactor away from "
            "the moderator",
        ],
        "correct_index": 2,
        "why": "Slow neutrons make uranium-235 split but are simply captured "
               "by uranium-238, which is why the fuel has to be enriched.",
    },
    {
        "id": "ks4-nuclear-fission-s14",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why control rods are made from a material that "
                "absorbs neutrons rather than one that reflects them.",
        "options": [
            "Reflected neutrons would be sent back into the fuel and could "
            "cause further fission, so the rate would rise instead of falling",
            "Reflected neutrons would damage the pressure vessel by striking "
            "it repeatedly until the steel became too weak to hold the "
            "pressure",
            "No material is able to reflect a neutron, because neutrons carry "
            "no charge, so an absorbing rod is the only design that could ever "
            "work",
            "Reflecting rods would have to be moved much faster, which the "
            "machinery cannot manage safely during an emergency shutdown of "
            "the reactor at the plant",
        ],
        "correct_index": 0,
        "why": "The rods exist to take neutrons out of the chain "
               "permanently; anything that returned them to the fuel would do "
               "the opposite job.",
    },
    {
        "id": "ks4-nuclear-fission-s15",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fuel rods taken out of a reactor are stored under "
                "water in a deep pool for several years.",
        "options": [
            "The water dissolves the remaining uranium so the rods can be "
            "reused in a fresh fuel assembly",
            "The water stops any further fission by washing the neutrons away",
            "The water keeps the rods cool and absorbs the radiation while "
            "the fragments decay",
            "The water reacts with the fuel to convert it into a stable "
            "compound",
        ],
        "correct_index": 2,
        "why": "Spent fuel is hot and intensely radioactive, and a deep pool "
               "both carries the heat away and shields the radiation while "
               "the most active isotopes decay.",
    },
    {
        "id": "ks4-nuclear-fission-s16",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a nuclear station is described as providing "
                "reliable base-load electricity while a wind farm is not.",
        "options": [
            "A reactor can be run at a steady chosen output whatever the "
            "weather is doing",
            "A reactor produces a much larger voltage, which the grid can use "
            "more easily",
            "A reactor needs no fuel, so it cannot be interrupted by a "
            "delivery failing",
            "A reactor's output rises automatically whenever demand on the "
            "grid increases",
        ],
        "correct_index": 0,
        "why": "The fission rate is set by the control rods rather than by "
               "conditions outside, so a reactor's output can be planned days "
               "ahead.",
    },
    {
        "id": "ks4-nuclear-fission-s17",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why natural uranium has to be enriched before it is "
                "used in most reactors.",
        "options": [
            "Natural uranium contains chemical impurities that would poison "
            "the coolant and would clog the pipes within a few weeks of "
            "running",
            "Natural uranium holds too little uranium-235 for a chain "
            "reaction to be sustained in an ordinary reactor",
            "Natural uranium is not radioactive until it has been enriched, so "
            "it releases no neutrons of its own in a reactor core",
            "Natural uranium is too dense to be shaped into fuel rods without "
            "processing in a specialised enrichment plant first",
        ],
        "correct_index": 1,
        "why": "Only about 0.7 per cent of natural uranium is uranium-235, "
               "and enrichment raises that to the few per cent a reactor "
               "needs.",
    },
    {
        "id": "ks4-nuclear-fission-s18",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an uncontrolled chain reaction each fission causes exactly "
                "two further fissions. Starting from a single fission, "
                "calculate how many fissions occur in the fourth generation.",
        "options": [
            "8",
            "4",
            "16",
            "6",
        ],
        "correct_index": 0,
        "why": "The generations run 1, then 2, then 4, then 8 — the number "
               "doubles each time.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Both conservation rules at once, the consequences of removing a
    # component, and judgements about mass, waste and fuel.
    {
        "id": "ks4-nuclear-fission-h05",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A uranium-235 nucleus absorbs a neutron and splits into "
                "zirconium-99 and tellurium-135 together with some neutrons. "
                "Determine how many neutrons are released.",
        "options": [
            "1",
            "3",
            "2",
            "0",
        ],
        "correct_index": 2,
        "why": "Mass number is conserved: 235 + 1 = 236, and 99 + 135 = 234, "
               "so the remaining 2 mass units are two neutrons.",
    },
    {
        "id": "ks4-nuclear-fission-h06",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One fission event yields caesium-140 (atomic number 55) "
                "together with two free neutrons. Given that the original "
                "nucleus was uranium-235, atomic number 92, identify the "
                "second fragment by its mass number and its atomic number.",
        "options": [
            "Mass number 96, atomic number 37",
            "Mass number 94, atomic number 37",
            "Mass number 94, atomic number 39",
            "Mass number 95, atomic number 38",
        ],
        "correct_index": 1,
        "why": "Mass number gives 236 − 140 − 2 = 94, and atomic number gives "
               "92 − 55 = 37, since the two neutrons carry no charge.",
    },
    {
        "id": "ks4-nuclear-fission-h07",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the coolant must keep circulating for a long time "
                "after a reactor has been shut down.",
        "options": [
            "Fission continues at a reduced rate for weeks after the control "
            "rods are lowered, which is what keeps the core hot",
            "The fission fragments in the fuel go on decaying, and their "
            "radiation keeps heating the core",
            "The moderator releases the energy it absorbed while the reactor "
            "was running back into the coolant for several weeks and into the "
            "pipework",
            "Stopping the flow would let the coolant freeze solid inside the "
            "pipes and split them open as it expanded",
        ],
        "correct_index": 1,
        "why": "Shutting down stops the chain reaction but not the decay of "
               "the fragments already made, and that decay heat is enough to "
               "damage the core if it is not carried away.",
    },
    {
        "id": "ks4-nuclear-fission-h08",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reactor is running at constant power, and each fission "
                "releases two or three neutrons. Explain what becomes of the "
                "neutrons that do not cause a further fission.",
        "options": [
            "They are absorbed by the control rods or by uranium-238, or they "
            "escape from the core altogether",
            "They decay into gamma rays within a fraction of a second",
            "They are pushed back into the fuel rods by the pressure vessel "
            "and stored there until the next generation begins",
            "They become part of the coolant, which is why it has to be "
            "replaced regularly throughout the reactor's working life and at "
            "every refuelling",
        ],
        "correct_index": 0,
        "why": "Steady power means exactly one neutron per fission continues "
               "the chain; the surplus has to be removed, and the control "
               "rods are what the operator uses to remove the right amount.",
    },
    {
        "id": "ks4-nuclear-fission-h09",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what happens to a reactor that loses its moderator "
                "with one whose control rods are withdrawn completely.",
        "options": [
            "Both cases stop the reaction, because neither component can be "
            "removed while the fuel is in place, since the fuel rods "
            "themselves hold both in place throughout a shutdown",
            "Losing the moderator makes the reaction grow, while withdrawing "
            "the rods shuts it down, which is why the two are adjusted on "
            "separate days",
            "Losing the moderator leaves fast neutrons that rarely cause "
            "fission, so the rate falls; withdrawing the rods lets the rate "
            "grow",
            "Both cases make the reaction grow, because each component exists "
            "only to slow neutrons down, the moderator merely doing it rather "
            "more slowly",
        ],
        "correct_index": 2,
        "why": "The two components pull in opposite directions: the moderator "
               "makes fission more likely and the rods make it less, so "
               "removing each has the opposite effect.",
    },
    {
        "id": "ks4-nuclear-fission-h10",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A nuclear station and a coal station produce the same "
                "electrical output for a year. Compare the masses of fuel "
                "they consume and explain the difference.",
        "options": [
            "The nuclear station uses a far smaller mass, because each "
            "fission releases millions of times more energy than each "
            "combustion reaction",
            "The nuclear station uses a far larger mass, because most of the "
            "uranium in the fuel is not uranium-235 and passes through the "
            "core unchanged unburned",
            "They use similar masses, because both are limited by the same "
            "turbine efficiency and by the same steam pressure at the inlet",
            "The coal station uses a smaller mass, because coal burns at a "
            "higher temperature than a reactor core is ever allowed to reach "
            "in service",
        ],
        "correct_index": 0,
        "why": "Energy density is the whole difference: a few tonnes of "
               "uranium replaces millions of tonnes of coal, because nuclear "
               "energy comes from the nucleus rather than from electrons.",
    },
    {
        "id": "ks4-nuclear-fission-h11",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the two fragments left after a uranium nucleus "
                "splits are themselves radioactive.",
        "options": [
            "They are still uranium, and uranium is radioactive whatever its "
            "mass number",
            "They were struck by the neutron that caused the split, which "
            "made them unstable",
            "They hold too many neutrons for their number of protons, so they "
            "are unstable and decay",
            "They have gained electrons during the split, which leaves them "
            "electrically unbalanced for a time",
        ],
        "correct_index": 2,
        "why": "A heavy nucleus needs proportionally more neutrons than a "
               "medium one, so the fragments inherit a neutron excess and "
               "decay, usually by beta emission.",
    },
    {
        "id": "ks4-nuclear-fission-h12",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine what would happen to the chain reaction if the "
                "graphite moderator in a reactor were replaced by a material "
                "that absorbs neutrons strongly.",
        "options": [
            "It would run faster, because absorbed neutrons release more "
            "energy when they are captured",
            "It would stop, because the neutrons would be removed instead of "
            "being slowed for the next fission",
            "It would continue unchanged, because the fuel rods supply their "
            "own neutrons",
            "It would run faster at first and then stop, as the absorber "
            "became saturated with neutrons",
        ],
        "correct_index": 1,
        "why": "The material would be acting as a giant control rod: with the "
               "neutrons absorbed rather than moderated, nothing carries the "
               "chain from one generation to the next.",
    },
    {
        "id": "ks4-nuclear-fission-h13",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The operators of a reactor need to double its power output. "
                "Determine what they do and explain why it works.",
        "options": [
            "Add more moderator, so that each neutron is slowed twice as much "
            "and is captured twice as readily by a nucleus",
            "Withdraw the control rods a little, so fewer neutrons are "
            "absorbed and more go on to cause fission",
            "Increase the coolant flow, so the extra heat removed forces more "
            "fissions to occur in the fuel rods",
            "Raise the core temperature, so the uranium nuclei split more "
            "readily",
        ],
        "correct_index": 1,
        "why": "The number of fissions per second is set by how many neutrons "
               "survive to find a nucleus, and the control rods are the "
               "adjustable part of that balance.",
    },
    {
        "id": "ks4-nuclear-fission-h14",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes that fission releases energy because the "
                "neutron carries a great deal of energy into the nucleus. "
                "Explain the error.",
        "options": [
            "The neutron carries almost no energy of its own, because it has "
            "no charge to accelerate it, which is why a neutron has to be "
            "slowed before it is useful towards the nucleus",
            "The neutron carries energy away rather than in, which is why the "
            "fragments are left cold, which is what leaves the fission "
            "fragments moving so fast",
            "The energy comes from the products having slightly less mass "
            "than the reactants, not from the neutron's own energy",
            "The energy comes from the electrons stripped off the uranium atom "
            "as it splits, which are torn away as the two fragments fly apart",
        ],
        "correct_index": 2,
        "why": "The incoming neutron is slow and carries very little energy; "
               "the 200 MeV released comes from a mass difference converted "
               "through E = mc².",
    },
    {
        "id": "ks4-nuclear-fission-h15",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that, because fission converts mass into "
                "energy, a reactor's fuel becomes measurably lighter as it "
                "runs.",
        "options": [
            "The claim is wrong, because mass is conserved exactly in every "
            "nuclear process, including the fission of uranium",
            "The claim is right in principle, but the mass converted is a "
            "minute fraction of the fuel and far too small to weigh",
            "The claim is right, and the loss is large enough for operators "
            "to monitor the fuel by weight",
            "The claim is wrong, because the energy released comes from the "
            "neutrons rather than from the fuel rods themselves in the core",
        ],
        "correct_index": 1,
        "why": "The mass defect is real and is where the energy comes from, "
               "but it amounts to roughly one part in a thousand of the mass "
               "of the nuclei that split.",
    },
    {
        "id": "ks4-nuclear-fission-h16",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine which single change would increase the rate of "
                "fission taking place in a reactor core.",
        "options": [
            "Inserting the boron control rods further into the core",
            "Replacing the graphite moderator with a sheet of cadmium",
            "Removing some of the water that acts as moderator and coolant "
            "from the core",
            "Replacing some of the uranium-238 in the fuel with uranium-235",
        ],
        "correct_index": 3,
        "why": "More uranium-235 means more nuclei that a slow neutron can "
               "split; each of the other three changes removes neutrons or "
               "removes the moderation that lets them be captured.",
    },
    {
        "id": "ks4-nuclear-fission-h17",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In many reactors the same water acts as both moderator and "
                "coolant. Explain how one substance performs two different "
                "jobs.",
        "options": [
            "The water is split into two separate circuits, one of which is "
            "chemically altered to moderate before either job can begin "
            "properly",
            "Only the water nearest the fuel moderates; the rest is too far "
            "from the neutrons to be struck",
            "Collisions with its light nuclei slow the neutrons, and the same "
            "collisions warm the water so it carries the energy away",
            "The water moderates while the reactor is starting up and cools it "
            "once full power is reached, once the coolant pumps have reached "
            "full speed",
        ],
        "correct_index": 2,
        "why": "Both jobs are the same physics seen from two sides: the "
               "energy the neutrons lose in slowing down is exactly the "
               "energy the water gains and carries to the steam generator.",
    },
    {
        "id": "ks4-nuclear-fission-h18",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the proposal that every gas-fired power station in "
                "the country should be replaced by a nuclear one within five "
                "years.",
        "options": [
            "It is straightforward, because a reactor can be built in a few "
            "months once the site is chosen, provided the planning permission "
            "is granted without delay",
            "It is impossible, because nuclear stations cannot produce enough "
            "power to replace a gas station, however many reactors happened to "
            "be built on one site",
            "It is unrealistic on that timescale: reactors take many years "
            "and great expense to build, and the waste and decommissioning "
            "have to be planned for",
            "It is unnecessary, because gas-fired stations release no carbon "
            "dioxide when they are working properly, since the carbon dioxide "
            "is captured inside the turbine hall",
        ],
        "correct_index": 2,
        "why": "The carbon case for fission is strong, but the practical "
               "case turns on build times measured in decades, very high "
               "capital cost and a long-lived waste stream.",
    },

    # ══ standard · s19–s26 ═══════════════════════════════════════════════
    # The reactor's own engineering the earlier rows never reach: coolant
    # pressure, cladding, waste heat, refuelling and core geometry.
    {
        "id": "ks4-nuclear-fission-s19",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the coolant in a pressurised water reactor is "
                "kept under very high pressure rather than at normal "
                "atmospheric pressure.",
        "options": [
            "High pressure raises the temperature at which the coolant "
            "boils, so it stays liquid and can carry more thermal energy "
            "out of the core",
            "High pressure slows the neutrons passing through the "
            "coolant, which increases the chance of each one causing a "
            "further fission",
            "High pressure keeps the fuel rods pressed tightly together, "
            "which raises the rate of fission taking place inside the "
            "core",
            "High pressure prevents any radioactive material from "
            "escaping the reactor, doing the same job as the concrete "
            "shield around the core",
        ],
        "correct_index": 0,
        "why": "Raising the pressure raises the boiling point, so the "
               "coolant can be heated well above 100°C in the core while "
               "remaining liquid and carrying away far more energy.",
    },
    {
        "id": "ks4-nuclear-fission-s20",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain the purpose of the metal cladding that surrounds "
                "each pellet of fuel inside a fuel rod.",
        "options": [
            "It absorbs surplus neutrons, doing the same job inside the "
            "fuel rod that the control rods do for the whole core",
            "It seals the fuel pellets in, stopping the radioactive "
            "fission fragments they produce from escaping into the "
            "coolant",
            "It slows fast neutrons down to the speed needed to cause "
            "further fission, working alongside the moderator",
            "It converts the thermal energy released by fission directly "
            "into electricity before the coolant even reaches it",
        ],
        "correct_index": 1,
        "why": "Cladding is a sealed metal tube around the fuel, so the "
               "highly radioactive fission fragments stay locked inside "
               "it rather than contaminating the coolant.",
    },
    {
        "id": "ks4-nuclear-fission-s21",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why large visible plumes of steam are often seen "
                "rising from the cooling towers of a nuclear power "
                "station.",
        "options": [
            "The steam is radioactive water vapour vented from the "
            "reactor core once it has passed through the turbine",
            "The steam is produced by burning a small amount of fuel to "
            "keep the cooling towers themselves from freezing in winter",
            "Not all the thermal energy taken from the core can be "
            "turned into electricity, and the surplus is released to the "
            "air as waste heat",
            "The steam is a safety signal, deliberately released so "
            "engineers can check the wind direction before venting any "
            "real emissions",
        ],
        "correct_index": 2,
        "why": "A power station's turbine can only convert part of the "
               "thermal energy supplied into electricity, and the "
               "cooling towers release the rest as harmless waste heat.",
    },
    {
        "id": "ks4-nuclear-fission-s22",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Reactor fuel is enriched to about 4% uranium-235, while "
                "weapon-grade uranium is enriched to about 90%. Explain "
                "why the reactor's fuel cannot sustain the runaway chain "
                "reaction a weapon needs.",
        "options": [
            "A 4% enrichment produces fuel rods that are too brittle to "
            "be shaped into the compact form a runaway reaction requires",
            "A 4% enrichment means the fuel contains too few neutrons of "
            "any kind to start a chain reaction under any conditions "
            "whatsoever, however the core is arranged or moderated",
            "A 4% enrichment cools far more slowly than 90% enrichment, "
            "which prevents the reaction from ever accelerating",
            "At only 4% uranium-235, far too many neutrons are absorbed "
            "by the surrounding uranium-238 for the reaction to grow "
            "explosively, however the fuel is arranged",
        ],
        "correct_index": 3,
        "why": "Uranium-238 captures slow neutrons without splitting, so "
               "at low enrichment the surplus fissile material a runaway "
               "reaction needs simply is not there.",
    },
    {
        "id": "ks4-nuclear-fission-s23",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why only a fraction of a reactor's fuel rods are "
                "replaced during a refuelling outage, rather than the "
                "entire core at once.",
        "options": [
            "Replacing the whole core at once would take the station "
            "offline for far longer, so operators replace only the most "
            "depleted rods each time",
            "The reactor's control rods can only be removed safely if "
            "some of the original fuel rods are left in position "
            "throughout the outage",
            "A completely fresh core would be too reactive to control "
            "safely, so some used fuel must always remain to slow the "
            "reaction down",
            "Fuel rods near the edge of the core deplete faster than "
            "rods at the centre, so the edge rods are the ones scheduled "
            "for early replacement",
        ],
        "correct_index": 0,
        "why": "Staggering replacement keeps the station generating for "
               "more of the time and spreads the cost of a shutdown, "
               "rather than losing weeks to replace every rod together.",
    },
    {
        "id": "ks4-nuclear-fission-s24",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a reactor's power output is described in "
                "megawatts rather than simply as a number of fissions "
                "occurring each second.",
        "options": [
            "The number of fissions per second cannot be measured "
            "directly by any instrument available to a power station's "
            "control room",
            "Megawatts describe the energy delivered each second in a "
            "unit the electricity grid and its customers can use "
            "directly",
            "Fissions per second and megawatts give exactly the same "
            "numerical value, so megawatts is simply the more familiar "
            "of the two",
            "A count of fissions per second says nothing about how much "
            "uranium-235 is left in the core, whereas megawatts does",
        ],
        "correct_index": 1,
        "why": "The grid runs on watts, so quoting output in megawatts "
               "connects the reactor to what it is actually supplying, "
               "rather than to an internal count nobody outside the "
               "plant uses.",
    },
    {
        "id": "ks4-nuclear-fission-s25",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A safety report imagines a fault in which each fission "
                "goes on to trigger three more, rather than the single "
                "further fission a steady reaction relies on. Beginning "
                "from one such fission, work out the total taking place "
                "two multiplication steps later.",
        "options": [
            "27",
            "3",
            "9",
            "6",
        ],
        "correct_index": 2,
        "why": "Generation one is 1 fission, generation two is 3, and "
               "generation three is 3 × 3 = 9.",
    },
    {
        "id": "ks4-nuclear-fission-s26",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the fuel rods in a reactor core are spaced "
                "apart by a moderator rather than packed together as "
                "tightly as the fuel would allow.",
        "options": [
            "Packing the rods tightly would make the fuel too hot to "
            "handle safely during the loading process, before the "
            "reactor is even switched on",
            "Spacing the rods apart reduces the total mass of "
            "uranium-235 in the core, which keeps it safely below the "
            "critical mass at all times",
            "Tightly packed rods would block the coolant from flowing "
            "between them, which is the only reason spacing between "
            "them is needed",
            "The moderator needs space around each rod so that fast "
            "neutrons can collide with it enough times to be slowed "
            "before reaching the next rod",
        ],
        "correct_index": 3,
        "why": "Neutrons are slowed by repeated collisions with the "
               "moderator, and that takes room — without gaps between "
               "the rods, there is nowhere for the moderator to do its "
               "job.",
    },

    # ══ harder · h19–h26 ═════════════════════════════════════════════════
    # Failure and waste reasoning the earlier rows never reach, a fresh
    # balanced equation, and two calculations of their own.
    {
        "id": "ks4-nuclear-fission-h19",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The pumps circulating coolant through a reactor fail "
                "completely, and the control rods are fully inserted at "
                "the same moment. Explain why the fuel can still "
                "overheat.",
        "options": [
            "The fission fragments already in the fuel keep decaying and "
            "releasing heat, and with no coolant flowing that heat has "
            "nowhere to go",
            "The control rods generate their own heat as they absorb "
            "neutrons, and without coolant flow that heat builds up "
            "inside the core",
            "Stopping the coolant flow makes the moderator slow neutrons "
            "even more effectively, which raises the fission rate back "
            "above normal",
            "The fuel continues to undergo fission at its normal rate "
            "even with the control rods fully inserted, because "
            "inserting them only slows neutrons rather than absorbing "
            "them",
        ],
        "correct_index": 0,
        "why": "Inserting the rods stops the chain reaction, but the "
               "decay of fission fragments already made continues "
               "regardless, and without coolant flow that decay heat has "
               "no way to escape.",
    },
    {
        "id": "ks4-nuclear-fission-h20",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Spent fuel contains a mixture of fission fragments, some "
                "dangerous for only days and others for thousands of "
                "years. Explain why a single storage plan cannot treat "
                "all of it the same way.",
        "options": [
            "Every fission fragment produced has an identical half-life, "
            "so a single storage plan already treats the whole mixture "
            "correctly",
            "The fragments' half-lives differ hugely, so some become "
            "safe within a human lifetime while others need isolating "
            "for far longer than any building lasts",
            "The whole batch of fragments decays away within a few days "
            "of leaving the core, so a short-term storage plan covers "
            "the mixture completely",
            "The mixture separates itself naturally within a few years "
            "into a short-lived batch and a long-lived batch that need "
            "no further attention afterwards",
        ],
        "correct_index": 1,
        "why": "A wide spread of half-lives means the waste is not one "
               "hazard but many, ranging from a threat measured in years "
               "to one measured in millennia.",
    },
    {
        "id": "ks4-nuclear-fission-h21",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In one fission event, a uranium-235 nucleus absorbing a "
                "neutron splits into iodine-137 (atomic number 53), "
                "three neutrons and one further nucleus. Determine the "
                "mass number and the atomic number of that further "
                "nucleus.",
        "options": [
            "Mass number 96, atomic number 41",
            "Mass number 99, atomic number 39",
            "Mass number 96, atomic number 39",
            "Mass number 99, atomic number 41",
        ],
        "correct_index": 2,
        "why": "Mass number gives 236 − 137 − 3 = 96, and atomic number "
               "gives 92 − 53 = 39, since the three neutrons carry no "
               "charge.",
    },
    {
        "id": "ks4-nuclear-fission-h22",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that, because a power reactor cannot "
                "explode like a nuclear weapon, an accident there can "
                "never release dangerous radioactivity to the "
                "surroundings.",
        "options": [
            "The claim is sound, because only an explosion of the kind a "
            "weapon produces could ever spread radioactive material "
            "beyond a reactor's containment",
            "The claim is sound, because a reactor's fuel is far too "
            "dilute to release any radioactive material under any "
            "circumstances, whatever else fails",
            "The claim is unsound, because a weapon-style explosion is "
            "in fact the only thing a reactor's containment is actually "
            "built to withstand",
            "The claim is unsound: severe overheating, a fire or a loss "
            "of containment can release radioactive material without "
            "any weapon-like explosion occurring",
        ],
        "correct_index": 3,
        "why": "History shows that a meltdown or a fire in damaged fuel "
               "can breach containment and release radioactive material, "
               "even though nothing like a nuclear weapon's explosion "
               "takes place.",
    },
    {
        "id": "ks4-nuclear-fission-h23",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an arbitrarily large mass of NATURAL, "
                "unenriched uranium still cannot sustain a chain "
                "reaction in an ordinary water-moderated reactor, "
                "however much of it is used.",
        "options": [
            "Natural uranium is almost entirely uranium-238, which "
            "captures the slow neutrons the moderator produces instead "
            "of letting them reach the rare uranium-235 nuclei",
            "Natural uranium has no critical mass at all, so no "
            "quantity of it, however large, could ever be assembled "
            "into a chain reaction of any kind, whatever moderator "
            "or geometry were chosen",
            "A water moderator cannot slow neutrons enough to interact "
            "with natural uranium, whatever its enrichment happens to be "
            "at the time",
            "Natural uranium releases too little heat for a "
            "water-moderated reactor's coolant system to remove safely, "
            "regardless of how much fuel is present",
        ],
        "correct_index": 0,
        "why": "It is not simply a matter of mass: with so few "
               "uranium-235 nuclei among the uranium-238, capture wins "
               "out over fission whatever quantity of natural uranium is "
               "used.",
    },
    {
        "id": "ks4-nuclear-fission-h24",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cladding around a fuel pellet develops a small crack "
                "while the reactor is running. Explain why this is "
                "treated as a serious fault even if the reactor's power "
                "output does not change.",
        "options": [
            "A cracked cladding sends the fission rate into an "
            "immediate and uncontrollable rise, regardless of what the "
            "control rods happen to be doing in the core at the time",
            "Fission fragments can now escape into the coolant, "
            "contaminating it and the whole cooling circuit even though "
            "the fission rate itself is unaffected",
            "The moderator can now enter the fuel rod through the "
            "crack, which stops that rod contributing anything further "
            "to the chain reaction",
            "A cracked cladding melts the fuel pellet inside it within "
            "seconds, before the reactor's instruments can register any "
            "change in its power output",
        ],
        "correct_index": 1,
        "why": "Cladding failure is a containment problem rather than a "
               "power problem: the fission rate can stay the same while "
               "radioactive material begins leaking into the coolant.",
    },
    {
        "id": "ks4-nuclear-fission-h25",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reactor releases 3200 MW of thermal power. Each "
                "fission releases about 3.2 × 10⁻¹¹ J. Estimate the "
                "number of fissions occurring in the core each second.",
        "options": [
            "1.0 × 10¹⁸",
            "3.2 × 10²⁰",
            "1.0 × 10²⁰",
            "1.0 × 10²²",
        ],
        "correct_index": 2,
        "why": "3200 MW is 3.2 × 10⁹ J each second, and "
               "3.2 × 10⁹ ÷ 3.2 × 10⁻¹¹ = 1.0 × 10²⁰ fissions per "
               "second.",
    },
    {
        "id": "ks4-nuclear-fission-h26",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that nuclear power cannot be "
                "considered a low-carbon technology because of the "
                "radioactive waste it produces.",
        "options": [
            "The claim is sound, because carbon dioxide emissions and "
            "radioactive waste are simply two different names for the "
            "same environmentally harmful by-product",
            "The claim is sound, because any technology that produces "
            "hazardous waste of any kind must automatically be excluded "
            "from ever being described as a low-carbon technology",
            "The claim is unsound, because nuclear waste decays away "
            "completely within a few years, leaving carbon dioxide as "
            "the long-term concern that then remains",
            "The claim is unsound, because carbon emissions and "
            "radioactive waste are two separate issues: a reactor can "
            "release very little of one while still producing a real "
            "amount of the other",
        ],
        "correct_index": 3,
        "why": "Low-carbon describes emissions released while generating "
               "electricity, which fission produces very little of; "
               "that judgement is separate from the real, long-lived "
               "challenge of storing its waste.",
    },
]
