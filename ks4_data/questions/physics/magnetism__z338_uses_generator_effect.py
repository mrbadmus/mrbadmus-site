"""Physics · Magnetism and electromagnetism — the MRB-338 expansion for
`uses-generator-effect`.

The baseline twelve in `magnetism__b.py` own the steam turbine and its
alternator, the car alternator's job, the bicycle dynamo's energy transfer, the
frequency of the UK mains, the rotation rate a single pair of poles needs, the
rotating-magnet design, the wind turbine's gearbox, one dynamo efficiency sum,
the hydroelectric-against-gas comparison, adding turns to brighten a dynamo
lamp, doubling an alternator's rotation rate, and the engine loading that
follows from switching a car's electrical loads on.

This file takes the rest of the applied ground: slip rings against the split
ring and the two output traces they give, the resources that all end at a
generator and the one that does not, the stages of a nuclear station, standby
and wind-up machines, regenerative braking, the pickup, the wheel-speed sensor
and the seismometer, the power, efficiency and kilowatt-hour sums a generator
invites, the grid's frequency and what moves it, and the design arguments
between turns, stages, predictability and "free" energy.

The physics of induction itself — Lenz's law, the factors affecting an induced
pd, the right-hand rule, flux through a bare coil, eddy-current braking —
belongs to `induced-potential`; transformers, grid voltages and transmission
losses belong to `transformers`; microphones and loudspeakers have their own
leaves. Nothing here crosses on to that ground: every row sits on a named
machine and the energy chain it lives in.

Every number has been worked through. The reasoning lives in `why` and never in
an option, and the four options of a row are kept to comparable lengths so that
neither the longest nor the shortest is a tell.
"""

TOPIC = "magnetism"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The two kinds of ring and the two traces they give, the resources that
    # end at a generator and the one that does not, and the everyday machines
    # a student meets: standby sets, wind-up torches, dynamos, regeneration.
    {
        "id": "ks4-uses-generator-effect-e05",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A generator has two slip rings, one joined to each end of "
                "the rotating coil, with a carbon brush pressed against each "
                "ring. State what kind of current this arrangement supplies "
                "to the circuit outside.",
        "options": [
            "Alternating current, because each end of the coil keeps its own "
                "ring",
            "Direct current, because the brushes always press on the same "
                "ring as the coil turns",
            "A current in one direction only, which grows larger and larger "
                "on every single half turn",
            "No current at all, because a smooth ring can never keep contact "
                "with a brush that is held still",
        ],
        "correct_index": 0,
        "why": "Each end of the coil stays joined to its own ring and its own "
               "brush for the whole rotation. The induced pd in each side "
               "reverses every half turn, so the output reverses with it and "
               "the machine supplies a.c. A brush slides on a smooth ring "
               "perfectly well, which is the point of the design.",
    },
    {
        "id": "ks4-uses-generator-effect-e06",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "The two slip rings on a generator are replaced by a single "
                "ring cut into two insulated halves. State what the output of "
                "the machine becomes.",
        "options": [
            "Alternating current, but at exactly twice the frequency it had "
                "before",
            "Direct current, since the connections swap over every time the "
                "induced pd reverses",
            "Alternating current at the same frequency as before, but with "
                "every peak made twice as tall",
            "No output at all, because a ring cut in half can only ever be "
                "used in a motor",
        ],
        "correct_index": 1,
        "why": "The split ring swaps which brush feeds which end of the coil "
               "at the instant the induced pd changes sign. The two reversals "
               "cancel, so the current in the external circuit always leaves "
               "by the same brush. The output is d.c. The same split ring is "
               "used in a motor, but it works in a generator too.",
    },
    {
        "id": "ks4-uses-generator-effect-e07",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "The output of an a.c. generator is displayed on an "
                "oscilloscope against time. Describe the shape of the trace.",
        "options": [
            "A straight horizontal line, held at one steady positive value "
                "the whole time",
            "A series of positive humps that all sit above the time axis, one "
                "per half turn",
            "A wave rising to a positive peak, falling through zero to a "
                "negative peak, then repeating",
            "A line that climbs steadily up from zero and then drops back to "
                "zero once per turn",
        ],
        "correct_index": 2,
        "why": "As the coil turns, the side that was cutting field lines "
               "downwards starts cutting them upwards, so the induced pd "
               "changes sign. Plotted against time that gives a smooth wave "
               "with a positive peak, a zero, a negative peak and another "
               "zero in each complete rotation.",
    },
    {
        "id": "ks4-uses-generator-effect-e08",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "That same machine is then fitted with a split ring in place "
                "of its slip rings, and its output is displayed on the "
                "oscilloscope again. Describe the new trace.",
        "options": [
            "A perfectly flat line held at the peak value, because a split "
                "ring smooths the output completely",
            "Exactly the same wave as before, because a split ring changes "
                "nothing about the induced pd",
            "A flat line sitting at zero, since the two halves exactly cancel out",
            "A series of humps that all lie on the same side of the axis, "
                "never below it",
        ],
        "correct_index": 3,
        "why": "The split ring flips the connections at each reversal, so the "
               "part of the wave that would have gone negative is turned back "
               "up. The trace becomes a run of humps all on one side of the "
               "axis: d.c., but a very bumpy d.c. that never settles at one "
               "steady value.",
    },
    {
        "id": "ks4-uses-generator-effect-e09",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name three renewable resources that all end up producing "
                "electricity by turning a generator.",
        "options": [
            "Wind, falling water in a hydroelectric scheme, and the rise and "
                "fall of the tide",
            "Solar cells fixed to a roof, a rechargeable chemical battery, "
                "and wind across open ground",
            "Coal, oil and natural gas, all of them burned to raise high-pressure "
                "steam",
            "Solar cells, solar heating panels, and a fuel cell running on "
                "hydrogen",
        ],
        "correct_index": 0,
        "why": "Wind turns blades, falling water and moving tidal water turn "
               "turbines, and in every case the turning shaft drives a "
               "generator. Coal, oil and gas also end at a generator but they "
               "are not renewable. Solar cells and fuel cells have no turning "
               "part at all.",
    },
    {
        "id": "ks4-uses-generator-effect-e10",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "One of the following ways of producing electricity does not "
                "use the generator effect at any stage. State which one.",
        "options": [
            "A gas-fired power station, where the burning gas boils water "
                "into steam",
            "Solar cells, which transfer energy from light straight into "
                "electricity with no moving parts",
            "A wind turbine, whose blades are turned round by the air moving past "
                "them",
            "A tidal barrage, where water flowing through the gates turns "
                "turbines",
        ],
        "correct_index": 1,
        "why": "A solar cell produces a pd directly from light falling on a "
               "semiconductor. There is no coil, no magnet and nothing "
               "rotating, so no induction. The other three all finish with a "
               "shaft turning a generator, whatever is used to turn it.",
    },
    {
        "id": "ks4-uses-generator-effect-e11",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the order of the stages in a nuclear power station, "
                "from the fuel to the electricity leaving the building.",
        "options": [
            "The fuel burns, and the hot gases push straight on to the turbine "
                "and then the generator",
            "Fission heats the core, the heat charges a very large battery, "
                "and the battery supplies the grid",
            "Fission heats water to steam, and the steam turns a turbine and "
                "generator",
            "Fission produces electricity in the fuel rods directly, and a "
                "turbine smooths it",
        ],
        "correct_index": 2,
        "why": "Nuclear fission in the fuel rods heats the coolant, the "
               "coolant boils water into high-pressure steam, the steam "
               "drives a turbine and the turbine turns a generator. Nothing "
               "burns, no battery is involved, and the fuel rods produce heat "
               "rather than electricity.",
    },
    {
        "id": "ks4-uses-generator-effect-e12",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A hospital keeps a diesel generator in a locked room, wired "
                "up so that it starts automatically. State what it is there "
                "for.",
        "options": [
            "To supply power to the operating theatres at all times, so that "
                "the mains is never needed in there",
            "To charge the batteries in every piece of portable equipment "
                "used on the hospital wards",
            "To make the hospital's own electricity more cheaply than the mains "
                "does",
            "To keep the power on if the mains supply to the whole hospital "
                "ever fails",
        ],
        "correct_index": 3,
        "why": "It is a standby set. Fuel drives the engine, the engine turns "
               "a generator and the generator induces a pd, so theatres, "
               "ventilators and lighting keep working through a mains "
               "failure. It runs only when it is needed, so it is neither the "
               "normal supply nor a cheaper one.",
    },
    {
        "id": "ks4-uses-generator-effect-e13",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A wind-up torch lights for a few minutes after its handle "
                "has been cranked. State what it contains in place of a "
                "battery.",
        "options": [
            "A small generator that a tightly wound clockwork spring keeps turning",
            "A solar cell which stores up the light it collected while the "
                "torch was outside",
            "A large electromagnet which holds on to its magnetism for a few "
                "minutes after winding",
            "A tank of compressed air, pumped up by the handle, that then "
                "forces the lamp to glow brightly",
        ],
        "correct_index": 0,
        "why": "Cranking the handle winds a spring, and the spring then "
               "unwinds through a gearbox and turns a small generator. The "
               "changing flux in its coil induces the pd that lights the "
               "lamp, which is why the light fades as the spring runs down.",
    },
    {
        "id": "ks4-uses-generator-effect-e14",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A cyclist riding at night has a lamp powered by a dynamo "
                "that presses against the front wheel. State what happens to "
                "the lamp when she stops at traffic lights.",
        "options": [
            "It stays just as bright, because the dynamo stores energy as it "
                "turns",
            "It goes out, because nothing is turning the dynamo, so no pd is "
                "induced at all",
            "It grows brighter for a moment, because the dynamo is no longer "
                "taking any energy from the wheel",
            "It dims a little but stays lit, since the magnet keeps its own "
                "field",
        ],
        "correct_index": 1,
        "why": "A dynamo induces a pd only while its magnet and coil are "
               "moving relative to one another. Once the wheel stops, the "
               "flux through the coil stops changing, the induced pd falls to "
               "zero and the lamp goes out. That is why dynamo lamps are "
               "usually fitted with a small backup cell.",
    },
    {
        "id": "ks4-uses-generator-effect-e15",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the energy store that a wind turbine draws on when it "
                "generates electricity.",
        "options": [
            "The thermal store of the air, which cools as the blades take "
                "energy from it",
            "The chemical store of the atmosphere, released as the air is "
                "stirred up",
            "The kinetic store of the moving air, which is always left slower "
                "once it has passed the blades",
            "The gravitational store of the blades, which fall as they swing "
                "downwards",
        ],
        "correct_index": 2,
        "why": "The turbine takes energy from the kinetic store of the moving "
               "air, which is why the air leaving the blades is slower than "
               "the air arriving. The temperature of the air barely changes, "
               "and a blade that swings down also swings back up, so nothing "
               "is gained gravitationally.",
    },
    {
        "id": "ks4-uses-generator-effect-e16",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what a hydroelectric power station uses to turn its "
                "turbines.",
        "options": [
            "Hot steam raised by burning the vegetation that was cleared out "
                "of the valley behind the dam",
            "The wind funnelled down the valley, which is stronger there than "
                "it is on open ground",
            "A diesel engine, started up whenever the reservoir behind the dam "
                "fills",
            "Water falling from a high reservoir, through large pipes built "
                "into the dam",
        ],
        "correct_index": 3,
        "why": "Water held high behind the dam has a large gravitational "
               "potential store. Released down the pipes it gains speed, and "
               "the fast-moving water pushes the turbine blades round. The "
               "turbine turns the generator, and nothing needs to be burned "
               "anywhere in the chain.",
    },
    {
        "id": "ks4-uses-generator-effect-e17",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what regenerative braking does with the kinetic energy "
                "of an electric car that is slowing down.",
        "options": [
            "It runs the motor as a generator, so that the energy goes back "
                "to the battery",
            "It stores the energy in a spring inside each wheel, released when "
                "the car pulls away again",
            "It turns all of the energy into heat in the brake discs and the pads",
            "It sends the energy back into the fuel tank as extra fuel for "
                "later",
        ],
        "correct_index": 0,
        "why": "When the driver lifts off, the wheels keep turning the "
               "machine, which now acts as a generator. The induced current "
               "charges the battery, and the field of that current opposes "
               "the rotation, which is what slows the car. Ordinary brakes "
               "would have dumped the same energy as heat.",
    },
    {
        "id": "ks4-uses-generator-effect-e18",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which part of a coal-fired power station actually "
                "produces the potential difference.",
        "options": [
            "The boiler, where the burning coal heats water into "
                "high-pressure steam",
            "The generator, in which a coil and a magnet are always made to "
                "move relative to one another",
            "The turbine, whose blades are pushed round by the steam rushing past "
                "them",
            "The cooling towers, where the used steam gives up its heat to the "
                "air",
        ],
        "correct_index": 1,
        "why": "Everything before the generator is there to make a shaft "
               "turn. Only in the generator does a conductor move relative to "
               "a magnetic field, and only there is a pd induced. The boiler, "
               "turbine and cooling towers handle energy but induce nothing.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # Energy chains named in order, the three induction sensors a student
    # meets outside the lab, the generator's arithmetic, and the reasons a
    # real machine's output is limited by the speed it is driven at.
    {
        "id": "ks4-uses-generator-effect-s05",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A small hydroelectric generator supplies a current of 8.0 A "
                "at a potential difference of 250 V. Calculate its output "
                "power.",
        "options": [
            "0.032 kW",
            "2000 kW",
            "2000 W",
            "31.25 W",
        ],
        "correct_index": 2,
        "why": "P = V I = 250 V x 8.0 A = 2000 W, which is 2.0 kW. Dividing "
               "the pd by the current instead gives 31.25 W, and reading the "
               "answer straight off as kilowatts makes it a thousand times "
               "too large.",
    },
    {
        "id": "ks4-uses-generator-effect-s06",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A hand-cranked generator is easy to turn while its two "
                "terminals are left unconnected, but becomes noticeably "
                "harder to turn as soon as a lamp is joined across them. "
                "Explain why.",
        "options": [
            "The lamp's resistance adds to the coil's, and a larger total "
                "resistance always resists turning",
            "The connecting wires make the circuit heavier, so more work is "
                "needed for each turn",
            "The lamp warms the coil, and a warm coil always turns more stiffly",
            "A current now flows, and its magnetic field opposes the motion "
                "that is making it",
        ],
        "correct_index": 3,
        "why": "With the terminals open a pd is induced but no current flows. "
               "Connect the lamp and a current flows, and that current "
               "produces its own magnetic field which opposes the change "
               "causing it. The hand has to do work against that opposition, "
               "and that work is what lights the lamp.",
    },
    {
        "id": "ks4-uses-generator-effect-s07",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A diesel generator is supplied with 40 kW of mechanical "
                "power by its engine and delivers 14 kW of electrical power. "
                "Calculate its efficiency.",
        "options": [
            "35%",
            "0.35%",
            "285%",
            "2.9%",
        ],
        "correct_index": 0,
        "why": "efficiency = useful output power / total input power = 14 kW "
               "/ 40 kW = 0.35, which is 35%. Dividing the other way round "
               "gives 285%, which is impossible, and forgetting to multiply "
               "the ratio by 100 gives 0.35%.",
    },
    {
        "id": "ks4-uses-generator-effect-s08",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Give the energy transfers in a wind turbine, in the order "
                "they happen.",
        "options": [
            "Chemical store of the air, to kinetic store of the blades, to "
                "electrical",
            "Kinetic store of the air, to kinetic store of the blades, to "
                "electrical output",
            "Thermal store of the sunlit ground, to the kinetic store of the "
                "blades, to a chemical store",
            "Electrical store in the generator, to the kinetic store of the "
                "moving air",
        ],
        "correct_index": 1,
        "why": "Moving air has a kinetic store. It pushes the blades, which "
               "gain a kinetic store of their own, and the shaft they turn "
               "drives the generator, which transfers the energy "
               "electrically. Air does have a thermal store, but the turbine "
               "does not draw on it.",
    },
    {
        "id": "ks4-uses-generator-effect-s09",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A coal-fired station burns fuel to produce electricity. "
                "State the sequence of stores the energy passes through, from "
                "the coal onwards.",
        "options": [
            "Chemical store of the coal, to an electrical store, and then to "
                "a thermal store",
            "Thermal store of the coal, to a nuclear store, to the kinetic "
                "store of the turbine",
            "Chemical store of the coal, to the thermal store of the steam, "
                "then to kinetic, then to electrical",
            "Kinetic store of the coal on the conveyor, to a thermal store, "
                "to electrical",
        ],
        "correct_index": 2,
        "why": "Burning empties the chemical store of the coal into the "
               "thermal store of the water and steam. The steam drives the "
               "turbine, giving it a kinetic store, and the turbine turns the "
               "generator, which transfers energy electrically. Coal holds no "
               "nuclear store, and nothing goes electrical first.",
    },
    {
        "id": "ks4-uses-generator-effect-s10",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "An electric guitar pickup is a coil wound round a small "
                "permanent magnet, sitting just below a steel string. Explain "
                "why plucking the string produces an electrical signal.",
        "options": [
            "The magnet's own field is turned into a current by the steel "
                "string, which acts as a conductor here",
            "The string rubs on the magnet as it moves, and the friction "
                "heats the coil slightly",
            "The vibrating string plucks at the coil and shakes it about in the "
                "field",
            "The vibrating steel string changes the flux through the coil, "
                "inducing a pd",
        ],
        "correct_index": 3,
        "why": "The magnet magnetises the piece of steel string just above "
               "it. As the string vibrates, that little magnet moves towards "
               "and away from the coil, so the flux through the coil rises "
               "and falls and a pd is induced at the same frequency as the "
               "string is vibrating.",
    },
    {
        "id": "ks4-uses-generator-effect-s11",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The same guitar is restrung with nylon strings and the "
                "pickup now produces no signal at all. Explain why.",
        "options": [
            "Nylon is not magnetic, so a vibrating nylon string cannot change "
                "the flux at all",
            "Nylon is an insulator, so no current can be induced anywhere "
                "along the length of the string",
            "Nylon strings are far too light to shake the magnet inside the coil",
            "Nylon strings vibrate at frequencies the coil cannot respond to",
        ],
        "correct_index": 0,
        "why": "The pickup works because the magnet magnetises the steel "
               "string. Nylon cannot be magnetised, so the vibrating string "
               "leaves the flux through the coil unchanged and no pd is "
               "induced. The current is induced in the coil, not in the "
               "string, so the string's own conductivity is beside the point.",
    },
    {
        "id": "ks4-uses-generator-effect-s12",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "An anti-lock braking system needs to know how fast each "
                "wheel is turning. A toothed steel ring fixed to the wheel "
                "passes close to a coil wound on a magnet. Explain how the "
                "sensor produces its signal.",
        "options": [
            "The teeth complete a circuit through the coil once for every "
                "tooth that passes",
            "Each tooth passing changes the flux through the coil, so a pulse "
                "of pd is induced every time",
            "The teeth scrape the magnet and the friction makes a small "
                "heating current",
            "The coil sends out a pulse which reflects off each tooth and "
                "returns",
        ],
        "correct_index": 1,
        "why": "A steel tooth arriving concentrates the magnet's field "
               "through the coil and a gap lets it fall again, so the flux "
               "rises and falls once per tooth and induces a pulse each time. "
               "Counting the pulses per second gives the wheel's rotation "
               "rate, and no contact is needed anywhere.",
    },
    {
        "id": "ks4-uses-generator-effect-s13",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A standby generator delivers a steady output power of 8.0 kW "
                "for 6.0 hours. Calculate the energy it delivers, in "
                "kilowatt-hours.",
        "options": [
            "1.3 kWh",
            "480 kWh",
            "48 kWh",
            "172 800 kWh",
        ],
        "correct_index": 2,
        "why": "One kilowatt-hour is the energy delivered by one kilowatt in "
               "one hour, so E = P t = 8.0 kW x 6.0 h = 48 kWh. Converting "
               "the hours into seconds as well multiplies by a further 3600 "
               "and gives 172 800, and dividing instead of multiplying gives "
               "1.3.",
    },
    {
        "id": "ks4-uses-generator-effect-s14",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A seismometer records ground movement using a heavy magnet "
                "hung on a long spring inside a coil that is bolted to the "
                "ground. Explain how it records a passing earthquake wave.",
        "options": [
            "The spring stretches, and the extra tension in it is measured "
                "directly as a potential difference",
            "The ground shakes the magnet while the coil stays still, so the "
                "coil produces no signal",
            "The magnet is heated by the wave, and a hot magnet gives a "
                "larger pd",
            "The coil moves with the ground while the heavy magnet lags "
                "behind, so a pd is induced",
        ],
        "correct_index": 3,
        "why": "The magnet is heavy and hangs on a soft spring, so its "
               "inertia keeps it nearly still while the bolted-down coil "
               "moves with the ground. That relative movement changes the "
               "flux through the coil and induces a pd, and the size of the "
               "pd tracks how fast the ground is moving.",
    },
    {
        "id": "ks4-uses-generator-effect-s15",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a lamp driven by a bicycle dynamo glows only "
                "faintly when the rider is moving at walking pace.",
        "options": [
            "The flux through the coil changes slowly, so only a small pd is "
                "induced",
            "The dynamo has to warm up before it works properly, and slow "
                "riding never warms it",
            "The lamp's resistance rises sharply at low speeds, so far less "
                "current can get through it",
            "The magnet inside loses a good deal of its strength whenever it "
                "is turned more slowly than usual",
        ],
        "correct_index": 0,
        "why": "The induced pd depends on how fast the flux through the coil "
               "changes. At walking pace the dynamo turns slowly, the flux "
               "changes slowly and the pd is small, so only a small current "
               "flows and the lamp is dim. The magnet's strength does not "
               "depend on how fast it is turned.",
    },
    {
        "id": "ks4-uses-generator-effect-s16",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the many generators feeding the National Grid "
                "must all be kept turning in step with one another.",
        "options": [
            "So that any one station can be switched off without warning the "
                "others",
            "So that their alternating outputs stay in phase and do not work "
                "against each other",
            "So that the total current in the grid cables is always shared "
                "out equally between all of them",
            "So that every station burns its fuel at exactly the same steady rate",
        ],
        "correct_index": 1,
        "why": "Every machine feeding the grid must reach its positive peak "
               "at the same instant. If one drifts out of step its pd opposes "
               "the others for part of each cycle, very large currents "
               "circulate between the machines and protection equipment "
               "disconnects it. Stations do not have to be equally loaded.",
    },
    {
        "id": "ks4-uses-generator-effect-s17",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A car's alternator keeps the battery charged while the "
                "engine idles, but at that speed it cannot supply the "
                "headlights, the heated rear screen and the blower all at "
                "once. Explain why.",
        "options": [
            "At idle the battery is nearly flat, and a flat battery cannot "
                "pass a current",
            "At idle the alternator produces direct current, which lamps "
                "cannot use",
            "At idle the alternator turns slowly, so the pd and the current "
                "it can supply are both small",
            "At idle the drive belt slips, so none of the engine's power "
                "reaches it",
        ],
        "correct_index": 2,
        "why": "The alternator is belt-driven, so at idle it turns slowly, "
               "the flux through its coils changes slowly and the pd induced "
               "is small. The small current that follows is enough to trickle "
               "charge the battery but not to run several heavy loads, which "
               "is why lights dim at a standstill.",
    },
    {
        "id": "ks4-uses-generator-effect-s18",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Two identical generators are installed, one driven by a "
                "steady flow of water through a pipe and the other by gusty "
                "wind. Compare the electrical output of the two machines.",
        "options": [
            "The wind-driven one gives the larger output on average, because a "
                "gust carries far more energy",
            "Both give exactly the same output, because the generators "
                "themselves are identical",
            "Neither gives a usable output until the driving speed is held "
                "steady",
            "The water-driven one gives a steady pd; the wind-driven one "
                "rises and falls",
        ],
        "correct_index": 3,
        "why": "The induced pd depends on how fast the machine is turned. A "
               "steady flow of water turns the shaft at a constant rate and "
               "gives a constant peak pd and frequency, while a gusty wind "
               "turns it at a rate that keeps changing, so both the pd and "
               "the frequency vary with the gusts.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # The limits on regeneration, the arithmetic of matching a station with
    # turbines, grid frequency and what moves it, and the evaluation
    # questions: free energy, predictability, stages and machine choice.
    {
        "id": "ks4-uses-generator-effect-h05",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why regenerative braking can never return all of a "
                "car's kinetic energy to its battery.",
        "options": [
            "Some energy is always wasted heating the motor windings, the "
                "cables and the battery",
            "The battery can only ever be charged from the mains supply, "
                "never from the moving car itself",
            "A generator can never produce a pd while a car is slowing down",
            "Kinetic energy is not one of the stores that a battery is able to "
                "hold",
        ],
        "correct_index": 0,
        "why": "The current induced in the windings passes through the "
               "resistance of the coils, the cables and the battery itself, "
               "and every one of those heats up. Air resistance and rolling "
               "friction take a share too, so only part of the kinetic store "
               "ever reaches the battery's chemical store.",
    },
    {
        "id": "ks4-uses-generator-effect-h06",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A car fitted with regenerative braking slows from motorway "
                "speed to a complete halt. Explain why the system is of "
                "little use in the final moments, and state what stops the "
                "car instead.",
        "options": [
            "It still works normally, but the driver cannot feel it working "
                "at low speeds",
            "The wheels turn too slowly to induce much pd, so the friction "
                "brakes always take over at the end",
            "The battery is full by then, so the friction brakes are used for "
                "the last part of the stop",
            "The motor reverses at low speed, and reversing it pushes the car "
                "backwards",
        ],
        "correct_index": 1,
        "why": "The induced pd depends on how fast the machine is turned, so "
               "as the wheels slow the pd, the current and the opposing force "
               "all shrink towards zero. The retarding effect fades away just "
               "when the car most needs holding, so ordinary friction brakes "
               "bring it to rest and hold it there.",
    },
    {
        "id": "ks4-uses-generator-effect-h07",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A gas-fired power station has an electrical output of 500 "
                "MW. One wind turbine has a rated output of 2.0 MW. Calculate "
                "how many of these turbines would be needed to match the "
                "station's rated output.",
        "options": [
            "1000 turbines",
            "100 turbines",
            "250 turbines",
            "2500 turbines",
        ],
        "correct_index": 2,
        "why": "number needed = 500 MW / 2.0 MW = 250 turbines. Multiplying "
               "instead of dividing gives 1000, and slipping a factor of ten "
               "gives 2500 or 100. In practice more would be needed still, "
               "because a turbine rarely runs at its rated output.",
    },
    {
        "id": "ks4-uses-generator-effect-h08",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student writes that a wind turbine is 100% efficient "
                "because the wind itself costs nothing. Evaluate this "
                "statement.",
        "options": [
            "It is correct, because efficiency compares what you get out with "
                "what you have to pay out for it",
            "It is correct for the turbine but wrong for the generator, which "
                "wastes a little as heat",
            "It is wrong, because no wind turbine has ever actually been built",
            "It is wrong: efficiency compares energy out with energy in, not "
                "with money",
        ],
        "correct_index": 3,
        "why": "Efficiency is useful output energy divided by total input "
               "energy, and cost has nothing to do with it. A turbine leaves "
               "most of the air's kinetic store in the air that flows past "
               "and around the blades, and wastes more in the gearbox and "
               "windings, so it is well short of 100%.",
    },
    {
        "id": "ks4-uses-generator-effect-h09",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A wind turbine has a rated power of 3.0 MW but averages only "
                "30% of that figure over a whole year. Estimate the energy it "
                "generates in one year, in megawatt-hours. Take one year as "
                "8760 hours.",
        "options": [
            "7900 MWh",
            "26 300 MWh",
            "23 700 MWh",
            "2 630 MWh",
        ],
        "correct_index": 0,
        "why": "Average power = 0.30 x 3.0 MW = 0.90 MW, so E = P t = 0.90 MW "
               "x 8760 h = 7884 MWh, about 7900 MWh. Forgetting the 30% "
               "altogether gives 26 300 MWh, using 90% instead gives 23 700 "
               "MWh, and a slipped power of ten gives 2 630 MWh.",
    },
    {
        "id": "ks4-uses-generator-effect-h10",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the energy chain of a gas-fired power station with "
                "that of a wind turbine, and identify the stage at which the "
                "gas station loses the most energy.",
        "options": [
            "The two chains are identical, so neither one wastes more than the "
                "other",
            "Both end at a generator, but only the gas one has a hot stage, "
                "and it loses most there",
            "The gas station loses most of its energy inside the generator, "
                "where the coils get very warm",
            "The wind turbine loses more, because much of the air slips past "
                "the blades",
        ],
        "correct_index": 1,
        "why": "The turbine's chain is kinetic to kinetic to electrical. The "
               "gas station inserts a thermal stage: hot exhaust gases go up "
               "the stack and warm steam goes to the cooling towers, and that "
               "is where most of the input is lost. Generators themselves are "
               "well over 90% efficient in both machines.",
    },
    {
        "id": "ks4-uses-generator-effect-h11",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the electrical output of a tidal barrage can be "
                "predicted far more reliably than the output of a wind farm.",
        "options": [
            "Tidal water is much denser than air, so a barrage never has to "
                "stop working",
            "A barrage runs at constant output day and night, so nothing "
                "about it can change",
            "The tides follow the Moon on a fixed timetable, while the wind is "
                "never certain day to day",
            "Wind farms are switched off whenever the weather forecast is "
                "uncertain",
        ],
        "correct_index": 2,
        "why": "Tides are driven by the Moon and Sun, so their times and "
               "heights are known years ahead and the barrage's output can be "
               "timetabled. Wind speed can only be forecast a few days out. A "
               "barrage's output is predictable but not constant: it rises "
               "and falls through each tidal cycle.",
    },
    {
        "id": "ks4-uses-generator-effect-h12",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the frequency of the alternating supply sent out "
                "by a power station must be held steady even when demand "
                "across the country rises sharply.",
        "options": [
            "A drifting frequency would make every cable in the grid overheat "
                "and eventually melt right through",
            "The frequency sets the size of the pd, so letting it drift would "
                "change the mains voltage",
            "A higher frequency would make the electricity cost far more to make",
            "Appliances and clocks are built for one fixed frequency and go "
                "wrong otherwise",
        ],
        "correct_index": 3,
        "why": "Mains motors, timers and mains-driven clocks are designed "
               "around one frequency, and machines all over the grid must "
               "stay in step with it. Operators hold it steady by burning "
               "more fuel and admitting more steam as demand rises. "
               "Frequency and pd are set independently of each other.",
    },
    {
        "id": "ks4-uses-generator-effect-h13",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Overnight a fault takes two large generating sets off the "
                "grid, and for a few seconds the demand exceeds the supply. "
                "State what happens to the frequency of the supply, and "
                "explain why.",
        "options": [
            "It falls, because the extra load drags on the generators that "
                "are left and slows them",
            "It rises sharply, because the whole of the demand is now shared out "
                "between far fewer machines",
            "It stays exactly the same, because frequency is set by the "
                "cables",
            "It drops to zero at once, because the grid always shuts itself down",
        ],
        "correct_index": 0,
        "why": "Each generator still connected now carries a larger current, "
               "and the field of that current opposes its rotation more "
               "strongly. With no extra steam supplied the machines slow "
               "slightly, and since frequency is set by rotation rate the "
               "supply frequency falls until more generation is brought on.",
    },
    {
        "id": "ks4-uses-generator-effect-h14",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Winding more turns on to a generator's coil increases the pd "
                "it induces. Explain why this cannot give more electrical "
                "power for nothing.",
        "options": [
            "The extra turns add resistance, and that resistance exactly "
                "cancels the extra pd",
            "Energy must always be conserved, so any extra drawn out has first "
                "to be put in by the driver",
            "The pd rises but the current falls in the same ratio, so the "
                "power never changes",
            "More turns make the coil heavier, and a heavier coil simply "
                "turns more slowly",
        ],
        "correct_index": 1,
        "why": "More turns do give a larger pd and a larger current through "
               "the same load. That larger current opposes the rotation more "
               "strongly, so whatever drives the shaft must do more work each "
               "turn. The extra electrical power is paid for in mechanical "
               "power, exactly as conservation of energy requires.",
    },
    {
        "id": "ks4-uses-generator-effect-h15",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A cyclist claims that the dynamo fitted to her bicycle gives "
                "her free lighting, because she never has to buy batteries "
                "for it. Evaluate the claim.",
        "options": [
            "It is fair enough: the wheel would have been turning anyway, so the "
                "lamp costs her nothing at all",
            "It is fair for a short ride but not a long one, because the dynamo "
                "slowly wears out",
            "It is not free, because the cyclist has to pedal harder to supply "
                "it",
            "It is not free, because the dynamo's magnet has to be replaced "
                "each year",
        ],
        "correct_index": 2,
        "why": "The current in the dynamo's coil makes a field that opposes "
               "the wheel's rotation, so the cyclist has to push harder "
               "against that drag. The energy in the lamp comes from her "
               "food, not from nowhere. It is free of batteries and of money, "
               "but never free of energy.",
    },
    {
        "id": "ks4-uses-generator-effect-h16",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Modern cars are fitted with an alternator rather than the "
                "d.c. dynamo that older cars carried. Give the main reason "
                "for the change.",
        "options": [
            "An alternator needs no magnet at all, which makes it a great "
                "deal lighter and cheaper to build",
            "An alternator runs directly from the battery, so the engine does "
                "not have to drive it",
            "A dynamo cannot be made small enough to fit under a modern bonnet",
            "An alternator has no commutator to wear out and charges well at "
                "idling speed",
        ],
        "correct_index": 3,
        "why": "A d.c. dynamo's split ring and brushes rub and wear, and it "
               "gives a useful output only at higher speeds. An alternator "
               "uses slip rings, which wear far less, and produces a usable "
               "output even at idle. It still has to be belt-driven by the "
               "engine, and it still needs a magnetic field.",
    },
    {
        "id": "ks4-uses-generator-effect-h17",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "In an electric car the same machine both drives the wheels "
                "and slows the car down again. Explain how one machine can do "
                "both jobs, and state what changes between the two.",
        "options": [
            "Current in gives motion out, and motion in gives current out "
                "instead",
            "The coil is rewound the other way round whenever the driver "
                "lifts off the pedal",
            "A second, separate machine is switched in, because one machine "
                "can only ever do one job",
            "The magnets inside are swapped for stronger ones each time the "
                "car changes from one to the other",
        ],
        "correct_index": 0,
        "why": "A coil in a field is a motor when a current is driven through "
               "it and a generator when something turns it. The hardware is "
               "identical; only the direction of energy flow changes. Driving "
               "sends energy from battery to wheels, and braking sends it "
               "from wheels back to battery.",
    },
    {
        "id": "ks4-uses-generator-effect-h18",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Generating electricity from falling water is far more "
                "efficient than generating it by burning a fuel. Explain the "
                "difference in terms of the number of energy transfers "
                "involved.",
        "options": [
            "Water is free, and a free resource always gives higher "
                "efficiency",
            "The water route has fewer transfers, and some energy is "
                "dissipated at every one",
            "Burning a fuel makes a much larger pd, and a large pd is always "
                "harder to control safely",
            "A water turbine spins faster, and faster machines waste less energy",
        ],
        "correct_index": 1,
        "why": "Falling water goes gravitational to kinetic to electrical. "
               "Burning fuel goes chemical to thermal to kinetic to "
               "electrical, and the thermal stage is the leaky one, with hot "
               "gases and warm water carrying energy away. Every extra "
               "transfer is another chance to dissipate energy.",
    },
]
