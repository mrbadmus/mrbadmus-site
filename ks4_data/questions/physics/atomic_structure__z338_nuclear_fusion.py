"""Physics · Atomic structure — the MRB-338 expansion of `nuclear-fusion`.

One leaf only: AQA 8463 §6.4.5.2, physics only — joining two small nuclei, the
electrostatic repulsion that has to be overcome first, the temperature and
confinement that buys, fusion in the Sun, and why no fusion station yet sells
electricity.

The original twelve rows in `atomic_structure__b.py` take the definition, the
Sun's hydrogen-to-helium reaction, the deuterium–tritium products, plasma as a
name, magnetic confinement instead of a wall, deuterium from sea water,
gravity as the Sun's confinement, the mass defect, the fission/fusion
comparison, net energy gain, the absence of a runaway, and the per-nucleon
energy argument.

This file works what those rows leave out: the ELECTROSTATIC REPULSION and the
strong nuclear force behind the whole temperature requirement, tritium bred
from LITHIUM, the tokamak and ITER by name, inertial confinement by laser,
neutron activation of the reactor walls, and the two fusion equations the
existing rows never write out. Its equation rows ask for the missing particle,
which the existing `e03` does not.

⚠️ Two facts are deliberately not restated in any stem here: that deuterium
comes from sea water (`s02`'s keyed answer) and that the plasma is held by
magnetic fields rather than a wall (`s01`'s), because quoting either in a stem
would hand a pupil that row's answer in the same assignment (brief §9.6).

⚠️ On the energy comparison: fission releases MORE energy per reaction (about
200 MeV against fusion's 17.6 MeV). Fusion wins per NUCLEON and per kilogram of
fuel, and that is how it is put here and in the existing `h04`.

Physics-only Triple content, so every row carries `triple_only=True` at
`foundation` tier. Working lives in `why`, never in an option.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The repulsion, the force that beats it, the conditions, and the named
    # machines.
    {
        "id": "ks4-nuclear-fusion-e05",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why two nuclei push each other apart as they approach.",
        "options": [
            "They both carry a positive charge, so they repel each other",
            "They both carry a negative charge, so they repel each other",
            "Their gravitational fields cancel out at short range",
            "The neutrons inside them collide and bounce apart",
        ],
        "correct_index": 0,
        "why": "Every nucleus is positively charged, and like charges repel — "
               "which is the barrier fusion has to get past.",
    },
    {
        "id": "ks4-nuclear-fusion-e06",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the force that holds two nuclei together once they are "
                "close enough to fuse.",
        "options": [
            "The gravitational force between them",
            "The electrostatic force",
            "The strong nuclear force",
            "The magnetic force",
        ],
        "correct_index": 2,
        "why": "The strong nuclear force is far stronger than the "
               "electrostatic repulsion, but only over a range of about the "
               "size of a nucleus.",
    },
    {
        "id": "ks4-nuclear-fusion-e07",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate temperature needed inside an "
                "experimental fusion reactor.",
        "options": [
            "About 1000 °C",
            "About 100 000 °C",
            "About 100 million °C",
            "About 100 °C",
        ],
        "correct_index": 2,
        "why": "Around 100 million °C gives the nuclei enough kinetic energy "
               "to get close enough for the strong nuclear force to act.",
    },
    {
        "id": "ks4-nuclear-fusion-e08",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the element from which the tritium used in fusion "
                "research is obtained.",
        "options": [
            "Lithium",
            "Uranium",
            "Helium",
            "Carbon",
        ],
        "correct_index": 0,
        "why": "Tritium does not occur naturally in useful amounts, so it is "
               "made from lithium, which is mined in reasonable quantities.",
    },
    {
        "id": "ks4-nuclear-fusion-e09",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what four hydrogen nuclei eventually form in the core "
                "of the Sun.",
        "options": [
            "Two deuterium nuclei",
            "One helium-4 nucleus",
            "One lithium-7 nucleus",
            "Four separate neutrons",
        ],
        "correct_index": 1,
        "why": "Four protons combine to give a helium-4 nucleus, made of two "
               "protons and two neutrons, releasing energy as they do so.",
    },
    {
        "id": "ks4-nuclear-fusion-e10",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the ring-shaped machine designed to hold a fusion plasma "
                "with magnetic fields.",
        "options": [
            "A cyclotron",
            "A tokamak",
            "A calorimeter",
            "A turbine hall",
        ],
        "correct_index": 1,
        "why": "A tokamak is the doughnut-shaped design used by JET and ITER, "
               "in which the plasma circulates inside a ring of magnets.",
    },
    {
        "id": "ks4-nuclear-fusion-e11",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the large international fusion reactor being built in "
                "France.",
        "options": [
            "ITER",
            "CERN",
            "Sizewell C",
            "Hinkley Point",
        ],
        "correct_index": 0,
        "why": "ITER is an international project aiming to release several "
               "times more energy from fusion than is put into the plasma.",
    },
    {
        "id": "ks4-nuclear-fusion-e12",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Apart from using magnetic fields, state the other way of "
                "bringing fusion fuel to the conditions it needs.",
        "options": [
            "Spinning the fuel rapidly in a centrifuge",
            "Passing a very large electric current through solid fuel for "
            "several minutes",
            "Compressing a tiny fuel pellet with powerful lasers",
            "Freezing the fuel until its nuclei are forced together",
        ],
        "correct_index": 2,
        "why": "Inertial confinement fires many powerful lasers at a small "
               "pellet at once, compressing and heating it for the instant "
               "fusion needs.",
    },
    {
        "id": "ks4-nuclear-fusion-e13",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how much carbon dioxide a fusion reaction releases.",
        "options": [
            "A small amount, from the carbon in the reactor walls",
            "None at all, because no carbon compounds are involved in the "
            "reaction",
            "About the same as burning an equal mass of hydrogen gas",
            "More than fission, because of the higher temperature involved in "
            "the reaction",
        ],
        "correct_index": 1,
        "why": "Fusion joins hydrogen nuclei to make helium; there is no "
               "combustion and no carbon anywhere in the reaction.",
    },
    {
        "id": "ks4-nuclear-fusion-e14",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the part of the Sun in which fusion takes place.",
        "options": [
            "The surface, where the temperature is highest",
            "The outer atmosphere, which we see during an eclipse",
            "The core, where the temperature and pressure are greatest",
            "Evenly throughout, since the Sun is the same all the way down "
            "from core to surface",
        ],
        "correct_index": 2,
        "why": "Only the core is hot enough and dense enough for hydrogen "
               "nuclei to fuse; the surface is thousands of degrees rather "
               "than millions.",
    },
    {
        "id": "ks4-nuclear-fusion-e15",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the radioactive waste a fusion reactor would leave "
                "compared with a fission reactor.",
        "options": [
            "Far more, because of the enormous temperatures involved in the "
            "process",
            "Exactly the same, because both are nuclear processes",
            "None of any kind, at any point in the reactor's life",
            "Less, and with much shorter half-lives than fission waste",
        ],
        "correct_index": 3,
        "why": "Fusion makes helium rather than long-lived fission "
               "fragments; the activated reactor structure is a real waste "
               "stream but decays far more quickly.",
    },
    {
        "id": "ks4-nuclear-fusion-e16",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what damages the inner walls of a fusion reactor over "
                "time.",
        "options": [
            "Bombardment by the high-energy neutrons the reaction releases",
            "Corrosion by the helium gas that collects against them",
            "The weight of the plasma pressing down on the lower wall",
            "The magnetic fields slowly pulling the metal out of shape over "
            "many years of running",
        ],
        "correct_index": 0,
        "why": "The neutrons carry no charge, so the magnetic field cannot "
               "hold them back and they strike the wall, damaging it and "
               "making it radioactive.",
    },
    {
        "id": "ks4-nuclear-fusion-e17",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what a plasma consists of.",
        "options": [
            "A liquid so cold that its atoms have stopped moving",
            "A mixture of free nuclei and free electrons, with no neutral "
            "atoms left",
            "A gas of complete atoms held at a very high pressure",
            "A solid whose atoms have been packed into a regular lattice with "
            "no gaps left between them",
        ],
        "correct_index": 1,
        "why": "At fusion temperatures every atom has been stripped of its "
               "electrons, leaving a mixture of charged particles rather than "
               "neutral atoms.",
    },
    {
        "id": "ks4-nuclear-fusion-e18",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State when the first commercial fusion electricity is "
                "currently expected.",
        "options": [
            "Within the next two or three years",
            "Around the 2040s or 2050s",
            "It began supplying the grid in the 1990s and has done so ever "
            "since",
            "Around the year 2300",
        ],
        "correct_index": 1,
        "why": "Experimental machines have produced fusion for decades, but "
               "the engineering needed for a working power station is "
               "expected to take until the middle of this century.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # Why the conditions are what they are, how a charged plasma can be
    # steered, and the two fusion equations written out.
    {
        "id": "ks4-nuclear-fusion-s05",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fusion needs an extremely high temperature.",
        "options": [
            "Heat is what breaks the nuclei apart so that they can be rejoined "
            "in a new arrangement inside the hot plasma itself",
            "The nuclei need enough kinetic energy to overcome their "
            "electrostatic repulsion and get very close together",
            "The fuel has to be melted before its nuclei are free to move "
            "towards each other, which takes an enormous amount of energy to "
            "supply",
            "High temperatures make the strong nuclear force act over a much "
            "longer range",
        ],
        "correct_index": 1,
        "why": "Temperature is a measure of the average kinetic energy of the "
               "particles, and only the fastest nuclei can approach closely "
               "enough for the strong nuclear force to take over.",
    },
    {
        "id": "ks4-nuclear-fusion-s06",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a high pressure is needed as well as a high "
                "temperature.",
        "options": [
            "Pressure squeezes the nuclei past each other's repulsion without "
            "any need for speed, however slowly they happen to be moving",
            "Pressure lowers the temperature at which the strong nuclear "
            "force begins to act",
            "Pressure packs the nuclei closer together, so collisions happen "
            "often enough to give a useful rate",
            "Pressure prevents the helium produced from escaping before it "
            "can be collected",
        ],
        "correct_index": 2,
        "why": "Temperature decides whether a collision can lead to fusion; "
               "pressure decides how many collisions there are each second.",
    },
    {
        "id": "ks4-nuclear-fusion-s07",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why simply compressing cold hydrogen gas in a strong "
                "cylinder will not produce fusion.",
        "options": [
            "Cold hydrogen is a molecule rather than an element, so its nuclei "
            "are unable to fuse",
            "The cylinder walls would absorb the energy released as fast as it "
            "was produced by the compressed gas",
            "Cold hydrogen contains no neutrons, and fusion cannot take place "
            "without them to start the reaction off in the cylinder",
            "However hard it is squeezed, the nuclei move too slowly to "
            "overcome their mutual repulsion",
        ],
        "correct_index": 3,
        "why": "Pressure alone cannot force charged nuclei together — they "
               "must be moving fast enough, which is what the enormous "
               "temperature provides.",
    },
    {
        "id": "ks4-nuclear-fusion-s08",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fusion fuel becomes a plasma at the temperatures "
                "a reactor reaches.",
        "options": [
            "The particles collide so violently that every electron is "
            "stripped from its atom",
            "The fuel melts and then boils, and every boiling gas is called a "
            "plasma",
            "The nuclei break apart into separate protons and neutrons",
            "The magnetic field pulls the electrons out of the atoms one at a "
            "time",
        ],
        "correct_index": 0,
        "why": "At around a hundred million degrees no electron can stay "
               "bound to a nucleus, so the fuel exists as free nuclei and "
               "free electrons.",
    },
    {
        "id": "ks4-nuclear-fusion-s09",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a magnetic field can steer a plasma when it "
                "cannot steer an ordinary gas.",
        "options": [
            "A plasma is much denser than a gas, so the field has more to push "
            "against as it circulates around the ring of the tokamak",
            "A plasma is made of charged particles, and a magnetic field "
            "exerts a force on a moving charge",
            "A plasma is magnetic in itself, so it is attracted to the poles "
            "of the magnets surrounding the vessel",
            "A plasma moves more slowly than a gas, giving the field time to "
            "act on it",
        ],
        "correct_index": 1,
        "why": "The free nuclei and electrons in a plasma are charged and "
               "moving, so a magnetic field exerts a force on them and can "
               "bend their paths away from the walls.",
    },
    {
        "id": "ks4-nuclear-fusion-s10",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why tritium has to be manufactured rather than "
                "collected from a natural supply.",
        "options": [
            "Tritium is radioactive with a short half-life, so almost none "
            "survives naturally on Earth",
            "Tritium is a gas, so any natural supply would have escaped into "
            "space long ago",
            "Tritium exists in large amounts underground but is too expensive "
            "to extract",
            "Tritium is not an isotope of hydrogen, so it cannot be separated "
            "from water",
        ],
        "correct_index": 0,
        "why": "Tritium decays with a half-life of about twelve years, so "
               "there is no natural reservoir to draw on and it has to be "
               "made from lithium.",
    },
    {
        "id": "ks4-nuclear-fusion-s11",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fusion is not expected to leave waste that must "
                "be guarded for thousands of years.",
        "options": [
            "Every product of fusion is stable, so no radioactive material is "
            "created at any point in the reactor's life",
            "The waste is a gas, so it can be released into the atmosphere "
            "without any treatment once the reactor is shut down for the night",
            "The main product is helium, and the activated reactor parts "
            "decay far faster than fission fragments do",
            "The waste is consumed again by the plasma before the reactor is "
            "shut down",
        ],
        "correct_index": 2,
        "why": "Helium is stable, so the only waste is the reactor structure "
               "made radioactive by neutrons — a real problem, but on a "
               "timescale of decades rather than millennia.",
    },
    {
        "id": "ks4-nuclear-fusion-s12",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how fusion can release energy when energy has to be "
                "supplied to make it happen in the first place.",
        "options": [
            "The energy supplied is stored in the plasma and given back "
            "unchanged when it cools, so nothing is gained and nothing is lost "
            "overall",
            "The energy supplied gets the nuclei close enough, and the "
            "reaction itself then releases far more from the loss of mass",
            "The energy supplied is converted directly into the energy "
            "released, with nothing gained or lost, which is why the two "
            "figures are always equal at the end of a run",
            "The energy supplied is recovered from the magnets once the "
            "reaction becomes self-sustaining and the plasma current begins to "
            "circulate freely",
        ],
        "correct_index": 1,
        "why": "Heating the plasma is the cost of starting the reaction; the "
               "energy released comes from the mass difference between the "
               "reactants and the products.",
    },
    {
        "id": "ks4-nuclear-fusion-s13",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A deuterium nucleus (atomic number 1) fuses with a tritium "
                "nucleus (atomic number 1) to form one nucleus and one "
                "neutron. Determine the atomic number of the nucleus formed.",
        "options": [
            "1",
            "2",
            "4",
            "5",
        ],
        "correct_index": 1,
        "why": "A neutron carries no charge, so all the charge ends up in the "
               "new nucleus: 1 + 1 = 2, which is helium.",
    },
    {
        "id": "ks4-nuclear-fusion-s14",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two deuterium nuclei fuse to form a helium-3 nucleus and one "
                "other particle. Determine what that other particle is.",
        "options": [
            "A neutron",
            "A proton",
            "An electron",
            "An alpha particle",
        ],
        "correct_index": 0,
        "why": "Mass numbers give 2 + 2 = 4 and helium-3 accounts for 3, "
               "leaving 1; atomic numbers give 1 + 1 = 2 and helium-3 "
               "accounts for 2, leaving 0 — mass 1 with no charge is a "
               "neutron.",
    },
    {
        "id": "ks4-nuclear-fusion-s15",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why experimental reactors use deuterium and tritium "
                "rather than the ordinary hydrogen the Sun fuses.",
        "options": [
            "Deuterium and tritium are the only isotopes that carry no charge "
            "to repel each other, which is why they pass through each other so "
            "easily inside the vessel",
            "Ordinary hydrogen is unable to fuse outside a star's "
            "gravitational field, however hot the plasma inside a reactor "
            "happens to be",
            "Deuterium and tritium fuse at the lowest temperature of any "
            "reaction, so they are the least difficult to achieve on Earth",
            "Ordinary hydrogen would produce a fission chain reaction instead "
            "of fusing, which no fusion reactor is designed to contain safely",
        ],
        "correct_index": 2,
        "why": "Every fusion reaction needs an enormous temperature, but "
               "deuterium with tritium needs the least — which is why it is "
               "the reaction every experiment starts with.",
    },
    {
        "id": "ks4-nuclear-fusion-s16",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the neutron released by each deuterium–tritium "
                "fusion is useful to a reactor's designers.",
        "options": [
            "It carries no charge, so it leaves the plasma and can deliver "
            "its energy to the surrounding blanket",
            "It carries a charge, so the magnetic field can direct it straight "
            "into a generator outside the vessel",
            "It fuses with a second deuterium nucleus, doubling the energy "
            "released by each reaction in the plasma",
            "It slows the plasma down, which keeps the reaction at a safe rate "
            "without any need for external control by the operators",
        ],
        "correct_index": 0,
        "why": "The charged helium stays trapped in the plasma, but the "
               "uncharged neutron escapes the magnetic field carrying most of "
               "the energy, which is how the energy is collected.",
    },
    {
        "id": "ks4-nuclear-fusion-s17",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the fusion reaction stops if the plasma touches "
                "the inner surface of the reactor.",
        "options": [
            "The surface is electrically earthed, which neutralises the nuclei "
            "on contact and stops them moving altogether",
            "Contact cools the plasma far below the temperature fusion needs",
            "The surface reflects the nuclei away from one another, so they "
            "cannot meet",
            "The surface absorbs the helium produced, which stops the "
            "reaction continuing",
        ],
        "correct_index": 1,
        "why": "A solid wall is a vast heat sink compared with a thin plasma, "
               "so any contact drains the energy the reaction depends on — "
               "the wall is at risk, but so is the reaction.",
    },
    {
        "id": "ks4-nuclear-fusion-s18",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the Sun, four hydrogen nuclei are needed to form each "
                "helium-4 nucleus. Calculate how many helium-4 nuclei are "
                "formed from 2.0 × 10^12 hydrogen nuclei.",
        "options": [
            "8.0 × 10^12",
            "5.0 × 10^11",
            "2.0 × 10^11",
            "5.0 × 10^12",
        ],
        "correct_index": 1,
        "why": "Dividing by four gives 2.0 × 10^12 ÷ 4 = 5.0 × 10^11 helium "
               "nuclei.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Balancing a second fusion equation, judging the claims made about
    # fusion, and the engineering that follows from the neutron.
    {
        "id": "ks4-nuclear-fusion-h05",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In one branch of deuterium–deuterium fusion the products are "
                "tritium and a single light particle. Identify that particle "
                "by balancing the mass numbers and the charges.",
        "options": [
            "A neutron",
            "A proton",
            "A beta particle",
            "A helium-4 nucleus",
        ],
        "correct_index": 1,
        "why": "Mass numbers give 2 + 2 = 4 with tritium taking 3, leaving 1; "
               "atomic numbers give 1 + 1 = 2 with tritium taking 1, leaving "
               "1 — mass 1 with charge 1 is a proton.",
    },
    {
        "id": "ks4-nuclear-fusion-h06",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student argues that since fusion is the reverse of fission, "
                "it must absorb energy rather than release it. Explain the "
                "error.",
        "options": [
            "Fusion is not the reverse of fission, because the two use "
            "completely different fuels",
            "Fusion does absorb energy, and a reactor works only because the "
            "plasma is heated electrically from the grid",
            "In both processes the products have slightly less mass than the "
            "reactants, so both release energy",
            "Fission absorbs energy too, which is why a reactor must be "
            "supplied with electricity to run",
        ],
        "correct_index": 2,
        "why": "The two are opposite in what happens to the nuclei but "
               "identical in where the energy comes from — a mass defect, on "
               "opposite sides of the range of nuclear sizes.",
    },
    {
        "id": "ks4-nuclear-fusion-h07",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict how the temperature needed to fuse two helium nuclei "
                "compares with that needed to fuse two hydrogen nuclei, and "
                "explain why.",
        "options": [
            "It is lower, because a helium nucleus is heavier and so moves "
            "more steadily towards its partner",
            "It is the same, because the temperature depends only on the "
            "strong nuclear force",
            "It is lower, because helium nuclei already contain neutrons to "
            "shield the charge",
            "It is higher, because a helium nucleus carries twice the charge "
            "and so repels far more strongly",
        ],
        "correct_index": 3,
        "why": "The electrostatic repulsion grows with the product of the two "
               "charges, so a pair of helium nuclei need much more kinetic "
               "energy to reach the same separation.",
    },
    {
        "id": "ks4-nuclear-fusion-h08",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An experimental reactor needs a temperature several times "
                "higher than the Sun's core although it fuses similar fuel. "
                "Explain why.",
        "options": [
            "The Sun's core is vastly denser and holds its fuel for millions "
            "of years, so a slow reaction rate is enough; a reactor has "
            "seconds and must compensate with temperature",
            "The Sun's core is under a vacuum, which lowers the temperature at "
            "which its nuclei fuse, so the nuclei there need far less kinetic "
            "energy before they can approach one another",
            "The Sun's gravity acts directly on the nuclei, pulling them "
            "together without any need for kinetic energy, without any kinetic "
            "energy being required of the nuclei themselves",
            "The Sun fuses helium rather than hydrogen, and helium fuses at a "
            "far lower temperature than any tokamak on Earth can reach",
        ],
        "correct_index": 0,
        "why": "A star can afford an extremely slow reaction because it is "
               "enormous and ancient; a reactor must get a useful power "
               "output from a small volume in a short time.",
    },
    {
        "id": "ks4-nuclear-fusion-h09",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that fusion will solve the world's "
                "electricity problem within the next ten years.",
        "options": [
            "It is realistic, because JET has already supplied electricity to "
            "the grid for several years without any interruption to supply",
            "It is unrealistic, because the fuel needed is far too scarce to "
            "supply more than one country at any one time anywhere in the "
            "world that needs it",
            "It is unrealistic, because no reactor yet achieves a sustained "
            "net energy gain and a working station is expected decades away",
            "It is realistic, because the only remaining problem is the cost "
            "of the buildings",
        ],
        "correct_index": 2,
        "why": "The physics is understood and the fuel is abundant, but the "
               "engineering of sustained net gain and of materials that "
               "survive the neutrons is unsolved.",
    },
    {
        "id": "ks4-nuclear-fusion-h10",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine what happens inside a tokamak if its magnetic field "
                "fails suddenly.",
        "options": [
            "The plasma explodes outwards, destroying the building around it",
            "The plasma touches the wall, cools instantly and the fusion "
            "stops within a moment",
            "The plasma continues fusing, because it is already hot enough to "
            "sustain itself indefinitely",
            "The plasma is compressed by the walls, and the fusion rate rises "
            "sharply",
        ],
        "correct_index": 1,
        "why": "The plasma is extremely thin and only stays hot while it is "
               "held clear of the walls, so losing the field ends the "
               "reaction rather than releasing it.",
    },
    {
        "id": "ks4-nuclear-fusion-h11",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the structure of a fusion reactor becomes "
                "radioactive even though helium is not.",
        "options": [
            "The plasma leaks slowly through the wall and contaminates the "
            "metal behind it over the years the reactor runs",
            "The magnetic fields induce radioactivity in any metal placed "
            "inside them, however briefly it happens to be left there beside "
            "the plasma",
            "The high temperature of the wall makes its atoms unstable",
            "Neutrons from the reaction are absorbed by nuclei in the wall, "
            "turning some of them into unstable isotopes",
        ],
        "correct_index": 3,
        "why": "This is neutron activation: an uncharged neutron passes "
               "straight through the magnetic field, is captured by a "
               "structural nucleus and leaves it neutron-rich and unstable.",
    },
    {
        "id": "ks4-nuclear-fusion-h12",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine what a commercial deuterium–tritium fusion station "
                "would need to be supplied with in order to keep running.",
        "options": [
            "Water and lithium, since the tritium would be bred inside the "
            "reactor from the lithium",
            "Water and uranium, since the uranium supplies the neutrons the "
            "reaction needs to keep the reaction going",
            "Helium and lithium, since helium is the fuel and lithium the "
            "moderator",
            "Water alone, since both fuels can be separated from ordinary "
            "water",
        ],
        "correct_index": 0,
        "why": "Deuterium comes from water, but tritium has to be made — and "
               "the plan is to line the reactor with lithium so the escaping "
               "neutrons breed it on site.",
    },
    {
        "id": "ks4-nuclear-fusion-h13",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four experimental machines report the ratio of the energy "
                "released to the energy put in: P gives 0.30, Q gives 0.70, R "
                "gives 1.5 and S gives 0.90. Determine which has achieved a "
                "net energy gain.",
        "options": [
            "S, because its ratio is the closest of the four to 1",
            "R, because it is the only one of the four where more energy came "
            "out than was put in",
            "P, because the smallest ratio means the least energy was wasted",
            "None of them, because a net gain requires a ratio above 10",
        ],
        "correct_index": 1,
        "why": "A net gain means the ratio exceeds 1, so only R released more "
               "energy than it consumed; the other three still cost more than "
               "they gave.",
    },
    {
        "id": "ks4-nuclear-fusion-h14",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why raising the plasma temperature increases the rate "
                "at which fusion takes place.",
        "options": [
            "More of the nuclei are moving fast enough to overcome the "
            "repulsion, so a larger fraction of collisions lead to fusion",
            "The nuclei expand at higher temperatures, which makes them easier "
            "targets to hit, which is why a hotter plasma gives a higher "
            "reaction rate",
            "The strong nuclear force grows stronger as the temperature is "
            "raised, so the electrostatic barrier between two nuclei falls "
            "away",
            "Higher temperatures reduce the charge on each nucleus, so there "
            "is less repulsion to overcome, leaving nothing for the strong "
            "nuclear force to overcome",
        ],
        "correct_index": 0,
        "why": "Temperature sets the average kinetic energy, so heating the "
               "plasma both increases how often nuclei meet and increases the "
               "share of meetings energetic enough to fuse.",
    },
    {
        "id": "ks4-nuclear-fusion-h15",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what would follow a serious failure at a fission "
                "power station with a serious failure at a fusion one.",
        "options": [
            "Both would release long-lived radioactive material, because both "
            "produce fission fragments",
            "Neither would release anything, because both are designed to "
            "shut down safely",
            "A fission failure risks releasing long-lived material from a hot "
            "core, while a fusion failure mainly ends the reaction",
            "A fusion failure would be far worse, because the plasma holds "
            "enough energy to destroy the site and everything standing on it",
        ],
        "correct_index": 2,
        "why": "A fission core holds a large inventory of long-lived "
               "fragments and keeps making decay heat after shutdown; a "
               "fusion plasma is thin, holds little energy and stops the "
               "moment conditions are lost.",
    },
    {
        "id": "ks4-nuclear-fusion-h16",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A visitor worries that a plasma at 100 million °C would burn "
                "everyone in the building if it escaped. Evaluate this "
                "concern.",
        "options": [
            "It is justified, because anything at that temperature holds "
            "enough energy to set a building alight within seconds of escaping "
            "the vessel it was held in",
            "It is overstated: the plasma is extremely thin, so it holds very "
            "little energy in total and cools the instant it touches "
            "anything",
            "It is justified, because the magnetic fields would drive the "
            "plasma outwards through the wall",
            "It is overstated, because the temperature quoted is measured on a "
            "different scale from an ordinary thermometer used by plasma "
            "physicists",
        ],
        "correct_index": 1,
        "why": "Temperature measures energy per particle, and a tokamak holds "
               "only a few grams of fuel — so the total energy stored in the "
               "plasma is small, and contact with a wall ends it.",
    },
    {
        "id": "ks4-nuclear-fusion-h17",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fusion power station would still need a steam "
                "turbine and generator.",
        "options": [
            "The turbine is needed to pump the fuel into the reactor at high "
            "pressure before the confining magnets are switched on",
            "The generator produces the magnetic field that confines the "
            "plasma",
            "The neutrons heat a surrounding blanket, and that thermal energy "
            "has to be turned into electricity in the usual way",
            "The plasma produces an alternating current directly, which the "
            "turbine converts into direct current, which the grid then "
            "distributes to homes and factories",
        ],
        "correct_index": 2,
        "why": "Fusion is a heat source like any other: the energy arrives as "
               "fast neutrons, warms a blanket, boils water and drives a "
               "conventional turbine.",
    },
    {
        "id": "ks4-nuclear-fusion-h18",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the argument that fusion research should be stopped "
                "because no reactor has ever supplied electricity to a grid.",
        "options": [
            "It is a strong argument, because sixty years without a working "
            "station shows the physics must be wrong, and no country would "
            "still be funding it if it could work",
            "It is a weak argument, because a fusion station could be built "
            "today if any country chose to pay for one, since every technical "
            "difficulty was solved some years ago by the JET team",
            "It is a weak argument, because the potential reward is a clean "
            "fuel supply lasting millions of years, and each experiment moves "
            "the engineering forward",
            "It is a strong argument, because the fuel would run out within a "
            "few decades even if it worked, because the lithium needed to "
            "breed tritium is nearly exhausted",
        ],
        "correct_index": 2,
        "why": "The physics is settled and the fuel supply is enormous; the "
               "judgement is whether a long, expensive engineering programme "
               "is worth an energy source with no carbon dioxide and no "
               "long-lived waste.",
    },

    # ══ standard · s19–s26 ═══════════════════════════════════════════════
    # Confinement TIME as a third condition alongside temperature and
    # pressure, the reactor's own engineering, and fuel supply compared.
    {
        "id": "ks4-nuclear-fusion-s19",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fusion plasma must be held at the required "
                "temperature and pressure for a certain minimum time, and "
                "not just reach those conditions for an instant.",
        "options": [
            "A fusion reaction between two nuclei still takes a certain "
            "amount of time to occur even once the conditions are "
            "right, so the plasma has to be held together long enough "
            "for enough of them to happen",
            "The strong nuclear force only switches on after a fixed "
            "delay of several whole seconds following the moment two "
            "nuclei first meet, however high their temperature or "
            "pressure happens to be at that instant",
            "Holding the plasma for longer raises its temperature "
            "further without any extra heating being supplied, simply "
            "because of the time spent confined",
            "A longer confinement time converts more of the plasma into "
            "a solid, which then fuses far more easily than a plasma "
            "made of free nuclei ever could",
        ],
        "correct_index": 0,
        "why": "Meeting the temperature and pressure conditions makes "
               "fusion possible from moment to moment; enough of it "
               "happening to matter also needs those conditions "
               "sustained for long enough.",
    },
    {
        "id": "ks4-nuclear-fusion-s20",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fusion power station would need to be "
                "refuelled far less often than a coal or gas station "
                "generating the same amount of electricity.",
        "options": [
            "A fusion station burns its fuel more slowly than a "
            "fossil-fuel station of the same output, because the "
            "plasma is deliberately held at a fixed reaction rate that "
            "operators are not permitted to raise",
            "Each fusion reaction releases millions of times more "
            "energy than a single chemical reaction in burning coal or "
            "gas, so a tiny mass of fuel lasts a very long time",
            "A fusion station stores far more fuel on site than a coal "
            "or gas station is able to, simply because deuterium takes "
            "up less space to store",
            "A fusion station recycles its own exhaust gases back into "
            "fuel, whereas a coal or gas station cannot reuse anything "
            "it has already burned",
        ],
        "correct_index": 1,
        "why": "Nuclear reactions release far more energy per reaction "
               "than chemical ones, so the same electrical output needs "
               "a vastly smaller mass of fuel.",
    },
    {
        "id": "ks4-nuclear-fusion-s21",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the lithium blanket surrounding a fusion "
                "reactor's plasma is described as doing two jobs at "
                "once.",
        "options": [
            "It absorbs the escaping neutrons to breed fresh tritium, "
            "while at the same time shielding the magnets and the "
            "outer structure from that same neutron bombardment",
            "It cools the plasma directly by physical contact while "
            "also generating the whole of the magnetic field that "
            "confines it, both jobs coming from the same single layer "
            "of material",
            "It converts helium produced by the reaction back into "
            "hydrogen fuel, while also recording how much energy the "
            "reactor has produced",
            "It reflects escaped neutrons straight back into the plasma "
            "to cause further fusion, while also absorbing the "
            "deuterium fuel before it can escape",
        ],
        "correct_index": 0,
        "why": "The same neutrons that would otherwise damage the "
               "reactor's structure are instead put to use turning "
               "lithium into the tritium the plasma needs.",
    },
    {
        "id": "ks4-nuclear-fusion-s22",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare how a magnetic-confinement reactor and an "
                "inertial-confinement experiment hold their fuel at "
                "fusion conditions.",
        "options": [
            "Magnetic confinement compresses a tiny fuel pellet with "
            "banks of lasers for a brief instant, while inertial "
            "confinement holds a plasma steady for hours at a stretch "
            "inside its vessel",
            "Both methods hold their fuel in exactly the same way, "
            "using magnetic fields generated by superconducting coils "
            "arranged around the vessel",
            "Magnetic confinement uses gravity to hold the plasma "
            "together, while inertial confinement relies entirely on "
            "the plasma's own electric charge",
            "Magnetic confinement uses fields to hold a plasma together "
            "continuously, while inertial confinement compresses a "
            "small pellet with lasers for a brief instant before it "
            "flies apart",
        ],
        "correct_index": 3,
        "why": "The two approaches trade continuous, steady confinement "
               "for a repeated, momentary implosion — a difference in "
               "how the same conditions are reached and briefly held.",
    },
    {
        "id": "ks4-nuclear-fusion-s23",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why less external heating may be needed to keep "
                "a fusion plasma at its working temperature once the "
                "reaction is well under way.",
        "options": [
            "The helium nuclei produced by fusion carry kinetic energy "
            "of their own, and colliding with the surrounding plasma "
            "helps to keep it hot",
            "The magnetic field automatically grows stronger as more "
            "fusion reactions take place, which raises the plasma's "
            "temperature without extra heating",
            "The plasma's density falls once fusion begins, and a less "
            "dense plasma naturally holds a higher temperature for the "
            "same energy supplied",
            "Each fusion reaction releases a neutron that is captured "
            "immediately by the fuel remaining in the plasma, heating "
            "it directly on contact",
        ],
        "correct_index": 0,
        "why": "The charged helium nuclei stay trapped in the plasma by "
               "the magnetic field, and their energy helps sustain the "
               "temperature that keeps the reaction going.",
    },
    {
        "id": "ks4-nuclear-fusion-s24",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deuterium available in the oceans could supply "
                "humanity's energy needs by fusion for an estimated "
                "hundreds of millions of years, while known uranium "
                "reserves for fission are estimated at a few hundred "
                "years at current rates of use. Explain what this "
                "comparison is evidence for.",
        "options": [
            "That fission is already a cleaner and more sustainable "
            "source of energy than fusion could ever become, no matter "
            "how much engineering progress is eventually made on it",
            "That fusion fuel is far more abundant relative to demand "
            "than fission fuel, making it a more sustainable long-term "
            "energy source if it can be made to work",
            "That fusion reactors are already cheaper to build than "
            "fission reactors, because their fuel costs so much less to "
            "extract",
            "That fusion has already solved the engineering problems "
            "that fission still faces, since its fuel supply lasts so "
            "much longer",
        ],
        "correct_index": 1,
        "why": "The comparison is about how long the fuel would last, "
               "not about cost or engineering readiness — and on that "
               "measure fusion's fuel supply dwarfs fission's.",
    },
    {
        "id": "ks4-nuclear-fusion-s25",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why inertial confinement fusion fires many "
                "lasers at a fuel pellet from many directions at once, "
                "rather than one laser from a single direction.",
        "options": [
            "A single laser could not deliver enough total energy to "
            "the pellet, however powerful it was built to be",
            "Firing from many directions lets each laser use a "
            "lower-energy beam, which is simply cheaper to generate "
            "than one very powerful beam",
            "Compressing the pellet evenly from every side is needed to "
            "squeeze it inward symmetrically; a beam from one direction "
            "would push it sideways instead",
            "Multiple lasers are needed so that each one can target a "
            "different isotope within the pellet, since deuterium and "
            "tritium respond to different wavelengths",
        ],
        "correct_index": 2,
        "why": "An even, all-round squeeze compresses the pellet towards "
               "its centre; a push from only one side would simply "
               "scatter it rather than compressing it.",
    },
    {
        "id": "ks4-nuclear-fusion-s26",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fusion research is sometimes described as an "
                "attempt to 'build a star' inside a laboratory.",
        "options": [
            "Because a fusion reactor is built from the same materials "
            "that make up the core of a star, mined especially for the "
            "purpose",
            "Because the temperature reached inside a fusion reactor is "
            "made to match exactly the surface temperature of an "
            "average star, on purpose, by the engineers who built it",
            "Because a fusion experiment is classified as an "
            "astronomical instrument, in the same category as a "
            "telescope used to observe real stars",
            "Because it recreates, on a tiny scale, the same nuclear "
            "process — fusing light nuclei at extreme temperature — "
            "that powers every star, including the Sun",
        ],
        "correct_index": 3,
        "why": "Stars generate their energy by fusing hydrogen into "
               "helium, and a fusion reactor is an attempt to trigger "
               "and control that same reaction on Earth.",
    },

    # ══ harder · h19–h26 ═════════════════════════════════════════════════
    # Two calculations of the leaf's own, the nuance in "ignition", a fuel
    # cycle trade-off, and what a plasma ratio does and does not prove.
    {
        "id": "ks4-nuclear-fusion-h19",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A proposed fusion power station would supply 500 MW of "
                "electricity. Each D-T fusion releases about 17.6 MeV, "
                "which is 2.8 × 10⁻¹² J. Estimate the number of fusion "
                "reactions needed each second to supply this power.",
        "options": [
            "1.8 × 10²⁰",
            "1.8 × 10¹⁸",
            "5.6 × 10¹⁹",
            "1.8 × 10²²",
        ],
        "correct_index": 0,
        "why": "500 MW is 5.0 × 10⁸ J each second, and "
               "5.0 × 10⁸ ÷ 2.8 × 10⁻¹² ≈ 1.8 × 10²⁰ fusion reactions "
               "per second.",
    },
    {
        "id": "ks4-nuclear-fusion-h20",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plasma reaches the temperature and pressure needed for "
                "fusion, but only for a few milliseconds before it "
                "cools. Evaluate the claim that reaching those "
                "conditions is, by itself, enough to guarantee a useful "
                "amount of fusion energy has been released.",
        "options": [
            "The claim is sound, because temperature and pressure are "
            "the only two conditions fusion ever requires, whatever the "
            "duration involved or however briefly they are reached",
            "The claim is unsound, because the reactions still take a "
            "finite time to occur, so a few milliseconds of confinement "
            "yields only a small number of them",
            "The claim is sound, because fusion reactions happen "
            "instantaneously the moment the correct temperature and "
            "pressure are reached, however briefly",
            "The claim is unsound, because temperature and pressure by "
            "themselves can never cause fusion, whatever the "
            "confinement time turns out to be",
        ],
        "correct_index": 1,
        "why": "Reaching the right conditions makes fusion possible, but "
               "the amount of energy released also depends on how long "
               "those conditions are sustained.",
    },
    {
        "id": "ks4-nuclear-fusion-h21",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reactor is described as having achieved 'ignition', "
                "meaning the heat from its own fusion reactions is "
                "enough to sustain the plasma's temperature. Evaluate "
                "the claim that an ignited reactor therefore needs no "
                "further energy input of any kind to keep running.",
        "options": [
            "The claim is sound, because ignition means the reaction "
            "has become entirely self-sustaining for as long as any "
            "fuel remains inside the vessel, with no other input ever "
            "needed",
            "The claim is sound, because the magnetic field itself is "
            "powered by the fusion reactions once ignition is reached, "
            "requiring no external electricity",
            "The claim is unsound, because energy is still lost from "
            "the plasma to its surroundings and fresh fuel still has to "
            "be supplied, so some ongoing input remains",
            "The claim is unsound, because ignition only ever refers to "
            "the moment fusion first begins, and self-heating stops "
            "again immediately afterwards",
        ],
        "correct_index": 2,
        "why": "Ignition removes the need for heating from an outside "
               "source, but the plasma still loses energy and burns "
               "fuel, so fresh fuel and some level of support remain "
               "necessary.",
    },
    {
        "id": "ks4-nuclear-fusion-h22",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the D-T fuel cycle, which needs tritium bred "
                "from lithium, with the D-D fuel cycle, which uses only "
                "deuterium. Evaluate why most current reactor designs "
                "still choose D-T despite needing to breed tritium.",
        "options": [
            "D-T is chosen because deuterium alone cannot fuse with "
            "itself under any conditions reachable on Earth, so D-D is "
            "not a genuine option for a reactor at all",
            "D-T is chosen because it produces no neutrons at all, "
            "unlike D-D, which makes the whole reactor far easier to "
            "shield",
            "D-T is chosen because breeding tritium is cheaper than "
            "mining deuterium, even though D-D would be far easier to "
            "achieve technically",
            "D-T is chosen because it needs a much lower temperature to "
            "fuse than D-D does, which makes it the practical first "
            "step even though it requires breeding tritium",
        ],
        "correct_index": 3,
        "why": "D-T fuses at the lowest temperature of the practical "
               "reactions, so despite the added complication of "
               "breeding tritium it remains the easier reaction to "
               "achieve first.",
    },
    {
        "id": "ks4-nuclear-fusion-h23",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One kilogram of deuterium-tritium fuel releases "
                "approximately 3.4 × 10¹⁴ J when fused. One kilogram of "
                "coal releases about 3.0 × 10⁷ J when burned. Calculate "
                "roughly how many times more energy the fusion fuel "
                "releases per kilogram.",
        "options": [
            "About ten million times",
            "About ten thousand times",
            "About a hundred times",
            "About a thousand million times",
        ],
        "correct_index": 0,
        "why": "Dividing one energy density by the other: "
               "3.4 × 10¹⁴ ÷ 3.0 × 10⁷ ≈ 1.1 × 10⁷, which is roughly "
               "ten million.",
    },
    {
        "id": "ks4-nuclear-fusion-h24",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that, because fusion needs lithium "
                "just as batteries do, a future lithium shortage would "
                "limit fusion's usefulness just as quickly as it would "
                "limit battery manufacturing.",
        "options": [
            "The claim is sound, because both technologies convert "
            "lithium into usable electricity by the very same physical "
            "process, so each extracts exactly the same amount of "
            "energy from every atom of it they consume",
            "The claim is unsound, because fusion releases its energy "
            "from nuclear reactions rather than storing it chemically, "
            "so a given mass of lithium yields vastly more usable "
            "energy in a fusion plant than in a battery",
            "The claim is sound, because lithium is used only as a "
            "structural material in both technologies rather than as a "
            "source of energy in either",
            "The claim is unsound, because fusion reactors do not use "
            "lithium at all, and only battery manufacturing depends on "
            "it",
        ],
        "correct_index": 1,
        "why": "A battery stores energy chemically, while a fusion "
               "reactor releases it from the nucleus — so the same mass "
               "of lithium goes vastly further as fusion fuel than it "
               "does inside a battery.",
    },
    {
        "id": "ks4-nuclear-fusion-h25",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why researchers developing structural materials "
                "for a fusion reactor's inner wall look for alloys that "
                "become radioactive for only a short time after neutron "
                "bombardment, rather than simply the strongest "
                "available metal.",
        "options": [
            "A stronger metal would simply melt at the plasma's normal "
            "working temperature long before it was ever installed, "
            "whatever its activation properties turned out to be under "
            "neutron bombardment",
            "Strength and radioactive half-life are always linked in a "
            "metal, so a search for one property automatically finds "
            "the other as well",
            "A wall that decays away quickly can be handled, recycled "
            "or disposed of within decades, whereas one that stays "
            "highly radioactive for centuries becomes a long-term "
            "waste problem of its own",
            "A metal that becomes radioactive for a short time absorbs "
            "fewer neutrons overall, which increases the temperature "
            "the plasma can reach",
        ],
        "correct_index": 2,
        "why": "Choosing a material with a short activation lifetime "
               "turns the reactor's own structure into a manageable "
               "waste stream rather than one that rivals fission's for "
               "how long it must be kept isolated.",
    },
    {
        "id": "ks4-nuclear-fusion-h26",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An experiment reports a ratio of energy released to "
                "energy put into the plasma of 1.5, meaning more energy "
                "came out of the plasma than was put directly into it. "
                "Evaluate the claim that this proves a working fusion "
                "power station could be built today.",
        "options": [
            "The claim is sound, because any ratio above 1 for the "
            "plasma is exactly the same as a ratio above 1 for the "
            "whole power station, lasers and all",
            "The claim is sound, because the only remaining step once "
            "the plasma ratio exceeds 1 is to connect a conventional "
            "turbine and generator, which counts as straightforward, "
            "already-solved engineering",
            "The claim is unsound, because a ratio above 1 has in fact "
            "never been achieved by any fusion experiment, so the "
            "report itself must be mistaken",
            "The claim is unsound, because the ratio only measures "
            "energy delivered to the plasma itself, not the much larger "
            "amount used to run the lasers, magnets and cooling of the "
            "whole facility",
        ],
        "correct_index": 3,
        "why": "A power station has to come out ahead once every system "
               "is counted, not just the plasma; the energy spent "
               "running the equipment that heats and confines it is "
               "usually far larger than what reaches the plasma "
               "directly.",
    },
]
