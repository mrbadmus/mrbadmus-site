"""Physics · Magnetism and electromagnetism — the MRB-338 expansion for
`electric-motors`.

The baseline twelve in `magnetism__a.py` own the energy transfer, the name of
the brushes, the statement of F = B I l, the supply-swap reversal, the opposed
forces on the two long sides, "more turns makes it faster", the complete-ring
rocking fault, the many-coil armature, one 50-turn force sum, the uneven
turning effect through a rotation, a 92%/30% efficiency comparison and the
disadvantage of raising current rather than turns.

This file takes the rest of the motor: what the split ring actually does to the
current, the couple the two forces make, the iron armature and its laminations,
the carbon brushes and why they are the sacrificial part, the radial field, the
position of greatest turning effect, the two reversals that cancel, stalling
and the heating it causes, the moment of the couple, P = F v, efficiency both
ways, the commutator gaps, the dead short sides, and the design arguments
between turns, current, field strength and wire thickness.

Direction-finding with the left hand, the tesla as a bare unit and plain
"calculate the force on a wire" practice belong to `flemings-left-hand-rule`;
the generator effect, slip rings on an alternator and transformers belong to
the triple-only leaves; solenoids belong to `electromagnetism`. Nothing here
crosses on to that ground — F = B I l appears only inside a motor, with turns,
moments or power attached to it.

Every number in the file has been worked through. The reasoning lives in `why`
and never in an option, and the four options of a row are kept to comparable
lengths so that neither the longest nor the shortest is a tell.
"""

TOPIC = "magnetism"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The parts of a d.c. motor and what each one is for, the two reversals,
    # and what a motor's rating and its stalling mean in everyday use.
    {
        "id": "ks4-electric-motors-e05",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what the split-ring commutator does to the current in "
                "a d.c. motor's coil every half turn.",
        "options": [
            "It reverses the direction of the current that flows round the "
                "coil",
            "It switches the current off for an instant so that the coil can "
                "coast past the upright position",
            "It increases the size of the current, so that the coil is "
                "pushed harder on every turn",
            "It keeps the current flowing the same way round the coil "
                "throughout the turn",
        ],
        "correct_index": 0,
        "why": "The split ring swaps which brush feeds which end of the coil "
               "at every half turn. That reverses the current, so the forces "
               "on the two long sides swap over and keep pushing the coil the "
               "same way round instead of dragging it back.",
    },
    {
        "id": "ks4-electric-motors-e06",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "One long side of a motor's coil is pushed upward while the "
                "other is pushed downward. State what those two forces "
                "produce together.",
        "options": [
            "A single resultant force that pushes the whole coil sideways in "
                "the gap",
            "A turning effect, or a couple, that spins the whole coil about "
                "its own axis",
            "A stretching force that pulls the coil apart along the "
                "direction of the magnetic field lines",
            "A steady push directed along the very axis that the coil spins "
                "about",
        ],
        "correct_index": 1,
        "why": "Two equal forces acting in opposite directions on either side "
               "of an axis form a couple. Their resultant force is zero, but "
               "their moments add, so the coil turns.",
    },
    {
        "id": "ks4-electric-motors-e07",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the coil of a practical d.c. motor is wound on a "
                "core made of iron.",
        "options": [
            "Iron insulates the turns of the coil from each other so the "
                "current cannot short out",
            "Iron makes the coil much lighter, so it can be spun up to full "
                "speed more quickly",
            "The iron concentrates the magnetic field through the coil, so "
                "the forces on its sides are much larger",
            "Iron stops the coil from getting hot while a large current is "
                "passing through it",
        ],
        "correct_index": 2,
        "why": "Iron is easily magnetised, so it draws the field lines through "
               "the coil and raises the flux density there. A larger B in "
               "F = B I l means a larger force on each side for the same "
               "current, so a stronger turning effect.",
    },
    {
        "id": "ks4-electric-motors-e08",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what the brushes of a d.c. motor are made from, and "
                "give one reason for that choice.",
        "options": [
            "Copper, because copper has the lowest electrical resistance of "
                "any metal cheap enough to use",
            "Steel, because steel is hard enough that it will never wear "
                "away at all",
            "Plastic, because it stops the commutator from wearing down as "
                "the coil spins round",
            "Carbon, because it conducts well and slides smoothly against "
                "the commutator",
        ],
        "correct_index": 3,
        "why": "Carbon conducts well enough to carry the current, is soft "
               "enough to slide against the turning commutator without "
               "cutting into it, and is self-lubricating, so the rubbing "
               "contact stays good as it wears.",
    },
    {
        "id": "ks4-electric-motors-e09",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what the curved pole pieces of a real motor give it "
                "that flat magnet faces do not.",
        "options": [
            "A field that is at its strongest only at the very top of each "
                "turn",
            "A field that changes its direction twice in every turn, which "
                "keeps the coil moving round",
            "A radial field, so that the coil feels a steady turning effect "
                "all the way round",
            "A field that grows steadily stronger as the coil picks up speed",
        ],
        "correct_index": 2,
        "why": "Curved poles make the field lines run radially outward from "
               "the axis, so the coil sides always cut across the field at "
               "right angles. The force on them stays the same size at every "
               "angle, which gives a steady turning effect.",
    },
    {
        "id": "ks4-electric-motors-e10",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the position of a motor's coil in a uniform field at "
                "which the turning effect on it is greatest.",
        "options": [
            "When the plane of the coil lies along the field, so both long "
                "sides are always pushed squarely round",
            "When the coil has turned so that its own plane cuts straight "
                "across the field",
            "When the coil is moving at its very fastest, part way through "
                "one of its turns",
            "At the moment when the brushes reach the two gaps cut in the "
                "split ring",
        ],
        "correct_index": 0,
        "why": "The moment of a force is largest when the force acts at right "
               "angles to the line from the axis. That happens when the "
               "coil's plane lies along the field lines. A quarter turn later "
               "the forces act straight along that line and the moment is "
               "zero.",
    },
    {
        "id": "ks4-electric-motors-e11",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "In the equation F = B I l used for one side of a motor's "
                "coil, state what B stands for and the symbol for its unit.",
        "options": [
            "The number of turns that are wound on the coil, measured in "
                "turns per metre of the iron core",
            "The strength of the battery driving the coil, measured in volts "
                "per metre of wire",
            "The length of the wire lying inside the magnetic field, "
                "measured in metres",
            "Magnetic flux density between the poles, whose unit is the "
                "tesla, symbol T",
        ],
        "correct_index": 3,
        "why": "B is the magnetic flux density between the poles, measured in "
               "tesla (T). I is the current in amperes and l is the length of "
               "coil side inside the field, in metres.",
    },
    {
        "id": "ks4-electric-motors-e12",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A working d.c. motor has its magnet taken out and put back "
                "the other way round, with the supply left alone. State what "
                "the coil then does.",
        "options": [
            "It turns at the same speed and in the same direction, because "
                "the supply has not been altered",
            "It turns the opposite way round, at about the same speed as it "
                "did before",
            "It stops turning altogether, because the two forces acting on "
                "the coil now cancel out",
            "It turns the same way round as before, but a good deal more "
                "slowly",
        ],
        "correct_index": 1,
        "why": "Reversing the field reverses the force on each side of the "
               "coil, so the couple acts the other way and the coil turns the "
               "other way. Nothing about the size of the force has changed, so "
               "the speed is much the same.",
    },
    {
        "id": "ks4-electric-motors-e13",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Both the magnet and the supply connections of a d.c. motor "
                "are reversed at the same time. State the effect on the "
                "direction in which the coil turns.",
        "options": [
            "It reverses, because reversing the magnet on its own turns the "
                "coil the other way round",
            "It reverses, because the two separate changes add together to "
                "give a bigger change of direction",
            "It stops, because the two changes together cancel out the force "
                "on the coil",
            "It is unchanged, and the coil turns the same way round as it "
                "did before",
        ],
        "correct_index": 3,
        "why": "Each reversal on its own flips the force. Doing both flips it "
               "twice, which brings it back to where it started, so the coil "
               "turns exactly as it did before.",
    },
    {
        "id": "ks4-electric-motors-e14",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the effect on a d.c. motor's speed of raising the "
                "potential difference of its supply.",
        "options": [
            "It slows down, because a great deal more of the energy is "
                "wasted as heat",
            "It stays the same, because the speed is fixed by the number of "
                "turns wound on the coil",
            "It speeds up, because a larger current gives a larger force on "
                "each coil side",
            "It stops, because the coil overheats and burns out straight "
                "away",
        ],
        "correct_index": 2,
        "why": "A larger pd drives a larger current through the coil. Since "
               "F = B I l, the force on each side rises, the couple rises, and "
               "the coil turns faster.",
    },
    {
        "id": "ks4-electric-motors-e15",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Name two everyday appliances in which an electric motor does "
                "the useful job.",
        "options": [
            "A filament lamp and an electric kettle, both fitted with a "
                "rotating element",
            "A washing machine, whose drum is spun, and an electric fan, "
                "whose blades are driven round",
            "A television screen and a radio, in which the sound is made by "
                "turning",
            "A toaster and an immersion heater, which both turn while they "
                "are working",
        ],
        "correct_index": 1,
        "why": "A motor is used wherever something has to be turned: washing "
               "machine drums, fan blades, food mixers, electric drills, hair "
               "dryers and pumps. Lamps, kettles, toasters and heaters have no "
               "moving part at all.",
    },
    {
        "id": "ks4-electric-motors-e16",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what is meant by saying that an electric motor is "
                "stalled.",
        "options": [
            "Its coil is being held still even though the supply is still "
                "connected to it",
            "It is spinning quite freely with nothing at all attached to its "
                "shaft, so it reaches top speed",
            "Its supply has been switched off and the coil is slowing down "
                "under friction on its own",
            "It is running at exactly the rated speed that is marked on its "
                "casing",
        ],
        "correct_index": 0,
        "why": "A stalled motor is one whose load is too large for it, so the "
               "coil cannot turn even though current is still being supplied "
               "to it.",
    },
    {
        "id": "ks4-electric-motors-e17",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Name the part of a d.c. motor that spins, carrying the coil "
                "round with it.",
        "options": [
            "The armature, which is the coil together with the iron core "
                "that it is wound on",
            "The stator, which is the pair of fixed magnets standing on "
                "either side of the turning coil",
            "The commutator brush, which is clamped firmly to the outside of "
                "the casing",
            "The field winding, which is bolted firmly on to the outer "
                "casing",
        ],
        "correct_index": 0,
        "why": "The armature is the rotating assembly: the coil, the iron core "
               "it is wound on and the commutator fixed to the shaft. The "
               "magnets and the brushes stay still.",
    },
    {
        "id": "ks4-electric-motors-e18",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what a motor's power rating in watts tells someone who "
                "is choosing one for a job.",
        "options": [
            "How long the motor is likely to last before its worn brushes "
                "need replacing",
            "How much energy it transfers every second, and so how quickly "
                "it can do any given job",
            "The total energy that it will use over the whole of its working "
                "life",
            "The largest potential difference that may safely be put across "
                "its two terminals",
        ],
        "correct_index": 1,
        "why": "Power is energy transferred per second, so a 900 W motor does "
               "the same job in half the time a 450 W motor takes. It says "
               "nothing about lifetime, total energy used or safe voltage.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The motor sums — force, moment, power, efficiency — and the everyday
    # behaviour a working motor shows: starting current, stalling, sparking,
    # brush wear and running under load.
    {
        "id": "ks4-electric-motors-s05",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A hoist is driven by a winding of 120 turns carrying 0.80 A. "
                "Where that winding crosses a 0.20 T field it measures 5.0 cm. "
                "Work out the size of the push on the part that crosses.",
        "options": [
            "96.0 N",
            "0.096 N",
            "0.96 N",
            "0.0080 N",
        ],
        "correct_index": 2,
        "why": "F = N B I l with l in metres: F = 120 x 0.20 x 0.80 x 0.050 = "
               "0.96 N. Leaving the length in centimetres gives 96 N, and "
               "forgetting the 120 turns gives 0.0080 N.",
    },
    {
        "id": "ks4-electric-motors-s06",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "The force on each long side of a motor's coil is 0.40 N and "
                "the coil is 3.0 cm wide. Calculate the moment of the couple "
                "acting on the coil.",
        "options": [
            "0.0060 N m",
            "0.024 N m",
            "1.2 N m",
            "0.012 N m",
        ],
        "correct_index": 3,
        "why": "The moment of a couple is one force times the perpendicular "
               "distance between the two forces: 0.40 x 0.030 = 0.012 N m. "
               "Doubling for the second force counts it twice, and leaving "
               "the width in centimetres gives 1.2 N m.",
    },
    {
        "id": "ks4-electric-motors-s07",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A coil side 8.0 cm long lies in a field of 0.15 T and "
                "carries a current of 2.0 A. The total force on that side is "
                "4.8 N. Calculate the number of turns on the coil.",
        "options": [
            "2000",
            "16.0",
            "200",
            "0.024",
        ],
        "correct_index": 2,
        "why": "Rearranging F = N B I l gives N = F / (B I l) = 4.8 / (0.15 x "
               "2.0 x 0.080) = 4.8 / 0.024 = 200 turns. The value 0.024 is the "
               "denominator on its own.",
    },
    {
        "id": "ks4-electric-motors-s08",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A d.c. motor draws a current of 4.0 A from a 12 V supply. "
                "Calculate the electrical power supplied to it.",
        "options": [
            "48 W",
            "0.33 W",
            "3 W",
            "48 J",
        ],
        "correct_index": 0,
        "why": "P = V I = 12 x 4.0 = 48 W. Dividing instead of multiplying "
               "gives 0.33 W or 3 W, and the watt is a joule per second, so "
               "the unit is W and not J.",
    },
    {
        "id": "ks4-electric-motors-s09",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a d.c. motor draws a much larger current at the "
                "instant it is switched on than it does once it has reached "
                "full speed.",
        "options": [
            "The brushes make poor contact until they have worn down to fit "
                "the commutator",
            "The supply pd is always a good deal higher at the moment a "
                "switch is first closed",
            "The coil is cold at first, and a cold coil has a very much "
                "lower resistance",
            "At rest the coil is not yet moving through the field, so only "
                "its own resistance limits the current",
        ],
        "correct_index": 3,
        "why": "Once the coil is turning, its movement through the field sets "
               "up a pd that opposes the supply, so the net driving pd and the "
               "current both fall. At rest there is no such opposition, and "
               "the coil's resistance alone is very small.",
    },
    {
        "id": "ks4-electric-motors-s10",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor drives a belt with a steady force of 30 N and the "
                "belt moves at 0.50 m/s. Calculate the useful power output of "
                "the motor.",
        "options": [
            "0.017 W",
            "15 W",
            "60.0 W",
            "15 J",
        ],
        "correct_index": 1,
        "why": "P = F v = 30 x 0.50 = 15 W. Dividing the two values the wrong "
               "way round gives 0.017 W or 60 W, and power is measured in "
               "watts rather than joules.",
    },
    {
        "id": "ks4-electric-motors-s11",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor is supplied with 250 W of electrical power and "
                "delivers 180 W usefully. Calculate its efficiency and state "
                "the power being wasted.",
        "options": [
            "0.72, with 180 W wasted",
            "1.39, wasting 70 W",
            "0.28, wasting 180 W",
            "0.72, with 70 W wasted",
        ],
        "correct_index": 3,
        "why": "Efficiency = useful power out / total power in = 180 / 250 = "
               "0.72, which is 72%. The power wasted is the difference, "
               "250 - 180 = 70 W, almost all of it heating the coil and the "
               "bearings.",
    },
    {
        "id": "ks4-electric-motors-s12",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a motor that has stalled quickly becomes hot "
                "enough to damage itself.",
        "options": [
            "The coil's own resistance rises very sharply the moment it is "
                "stopped from turning",
            "The brushes rub far harder against the commutator when the coil "
                "is being held still",
            "None of the energy leaves as kinetic energy, so it all heats "
                "the coil, and the current is largest",
            "The magnets begin to lose their strength and give out the "
                "stored energy as heat",
        ],
        "correct_index": 2,
        "why": "A stalled coil does no useful work, so every joule supplied is "
               "dissipated in the coil's resistance. The current is also at "
               "its largest, because nothing is opposing the supply, and the "
               "heating goes as the current squared.",
    },
    {
        "id": "ks4-electric-motors-s13",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a motor's iron armature is built from thin iron "
                "sheets with insulation between them rather than from one "
                "solid block.",
        "options": [
            "It makes the whole armature lighter so that it can be spun up "
                "to full speed much sooner",
            "It cuts down the currents that circulate inside the iron and "
                "heat it",
            "It lets cooling air pass between the sheets and carry the waste "
                "heat away quickly",
            "It allows the coil to be wound on far more tightly than a "
                "single solid block of iron would allow",
        ],
        "correct_index": 1,
        "why": "A solid iron core sitting in a changing field has currents "
               "driven round inside it, and those currents heat the iron and "
               "waste energy. Thin insulated sheets break up the paths those "
               "currents would take.",
    },
    {
        "id": "ks4-electric-motors-s14",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the carbon brushes of a motor are made to wear "
                "away sooner than the commutator does.",
        "options": [
            "Brushes are cheap and easy to change, while the commutator is "
                "part of the rotor",
            "Carbon is the harder of the two materials, so it grinds the "
                "copper segments down first of all",
            "The brushes carry a much larger current than the commutator "
                "segments ever have to",
            "The brushes are the only part of the whole motor that ever gets "
                "warm",
        ],
        "correct_index": 0,
        "why": "Two rubbing surfaces always wear. The sensible design lets the "
               "cheap, easily replaced part take the wear, so a service means "
               "sliding in new brushes rather than stripping and rebuilding "
               "the armature.",
    },
    {
        "id": "ks4-electric-motors-s15",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a running d.c. motor often sparks where the "
                "brushes meet the commutator.",
        "options": [
            "The contact between them is broken and then remade as each gap "
                "passes by",
            "The current is alternating at that point, and an alternating "
                "current always arcs across a gap",
            "The carbon of the brushes burns away steadily in the air as the "
                "motor runs",
            "The coil stores up charge, which then leaks away through the "
                "air once on every turn",
        ],
        "correct_index": 0,
        "why": "Every time a gap in the split ring passes under a brush the "
               "circuit is broken and then remade. The current tries to keep "
               "flowing across the small air gap for an instant, and that is "
               "the spark.",
    },
    {
        "id": "ks4-electric-motors-s16",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Compare a motor built with one pair of magnetic poles with "
                "one built with three pairs spaced around the armature, for "
                "smoothness of running.",
        "options": [
            "The single-pair motor runs more smoothly, because the force "
                "drops away in only one place",
            "The three-pair motor runs more smoothly, because the turning "
                "effect dips less",
            "They run equally smoothly, since the coil itself is the same in "
                "both of them",
            "The three-pair motor runs more roughly, because the poles fight "
                "each other",
        ],
        "correct_index": 1,
        "why": "With one pair of poles the turning effect falls to zero twice "
               "in every turn. Three pairs mean the dips come more often but "
               "are far shallower, because another pole is always taking over, "
               "so the shaft turns much more evenly.",
    },
    {
        "id": "ks4-electric-motors-s17",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Predict what a running d.c. motor does if one of its two "
                "brushes loses contact with the commutator.",
        "options": [
            "It turns twice as fast, because only half the circuit is now "
                "being driven",
            "It reverses, because the current now takes the other path round "
                "the coil",
            "The circuit is broken, so no current flows and the coil coasts "
                "to a stop against friction",
            "It keeps turning at the same speed, since the other brush is "
                "still touching",
        ],
        "correct_index": 2,
        "why": "Both brushes are in series with the coil, so losing either one "
               "opens the circuit. With no current there is no force on the "
               "coil, and friction at the bearings brings the armature to "
               "rest.",
    },
    {
        "id": "ks4-electric-motors-s18",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the motor of an electric fan slows down when "
                "something is pushed against its spinning blades.",
        "options": [
            "The supply pd drops as soon as the blades are touched, leaving "
                "far less to drive the coil",
            "The magnetic field weakens because the coil is no longer moving "
                "through it freely",
            "The brushes lift clear of the commutator as the armature slows "
                "down",
            "The obstruction adds a moment opposing the coil, so it settles "
                "at a lower speed",
        ],
        "correct_index": 3,
        "why": "The blades now meet a larger resisting moment than the motor's "
               "couple can balance at that speed, so the armature decelerates. "
               "It settles where the two moments are equal again, which is at "
               "a lower speed.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Two-stage sums, the design arguments between turns, current, field and
    # wire thickness, and the evaluations a motor question can ask: where the
    # turning effect goes, why efficiency is bounded, and what stalling means
    # for a vehicle.
    {
        "id": "ks4-electric-motors-h05",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor coil has 80 turns and measures 4.0 cm across by "
                "6.0 cm along. Its two 6.0 cm sides lie at right angles to a "
                "field of 0.30 T and carry a current of 0.50 A. Calculate the "
                "force on one 6.0 cm side and the largest moment the coil can "
                "feel.",
        "options": [
            "A force of 0.72 N on each long side, and a largest moment of "
                "0.058 N m on the coil",
            "A force of 0.48 N on each long side, with a moment of 0.029 N m",
            "A force of 0.72 N on each long side, and a largest moment of "
                "0.029 N m",
            "A force of 0.72 N on each long side, and a moment of 2.9 N m",
        ],
        "correct_index": 2,
        "why": "F = N B I l = 80 x 0.30 x 0.50 x 0.060 = 0.72 N. The moment of "
               "the couple is one force times the width: 0.72 x 0.040 = "
               "0.0288, or 0.029 N m to two significant figures. Counting both "
               "forces doubles it wrongly; leaving the width in centimetres "
               "gives 2.9 N m.",
    },
    {
        "id": "ks4-electric-motors-h06",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Two motors have the same magnets and the same coil size. The "
                "second has twice as many turns as the first but carries half "
                "the current. Compare the turning effects of the two.",
        "options": [
            "They are the same, because the force depends on the turns "
                "multiplied by the current, which is unchanged",
            "The second is twice as strong, because adding more turns always "
                "wins over current",
            "The second is half as strong, because halving the current "
                "halves the force on it",
            "The second is four times as strong, because both of the changes "
                "help it round",
        ],
        "correct_index": 0,
        "why": "F = N B I l depends on the product N I. Doubling N and halving "
               "I leaves that product, and so the force and the moment, "
               "exactly as they were. The second motor does waste less heat, "
               "but its turning effect is identical.",
    },
    {
        "id": "ks4-electric-motors-h07",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why doubling the current in a motor's coil doubles "
                "the force on it but more than doubles the heating in the "
                "wire.",
        "options": [
            "Force rises with the current, but heating rises with the pd, "
                "which doubles twice over",
            "Force rises with the current, but heating rises with the "
                "resistance, which grows as the wire warms",
            "Force and heating both rise with the current, but the heating "
                "is delayed by the iron core",
            "The force is proportional to I, but the heating is proportional "
                "to I squared",
        ],
        "correct_index": 3,
        "why": "F = N B I l is a first power of I, so doubling I doubles the "
               "force. The power wasted in the coil is I squared times R, so "
               "doubling I makes the heating four times as large. That is why "
               "extra turns are usually preferred to extra current.",
    },
    {
        "id": "ks4-electric-motors-h08",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A designer has a fixed budget and can spend it either on "
                "more turns of wire or on a stronger magnet. Discuss which "
                "choice gives the better motor.",
        "options": [
            "Only a stronger magnet helps, because the force on the coil "
                "does not depend on the number of turns",
            "Both raise the force, so the extra mass and resistance of more "
                "wire decide it",
            "Only more turns help, because the field between the poles is "
                "fixed by the size of the gap",
            "Neither helps, because the turning effect is set only by the "
                "supply pd",
        ],
        "correct_index": 1,
        "why": "F = N B I l rises with either N or B, so both spend the budget "
               "usefully. The tie-break is that extra turns add resistance, "
               "which cuts the current and adds heating, and add mass, which "
               "makes the armature slower to speed up.",
    },
    {
        "id": "ks4-electric-motors-h09",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the turning effect on a coil changes as it "
                "rotates in a uniform field but stays steady in a radial one.",
        "options": [
            "In a uniform field the flux density itself rises and falls as "
                "the coil goes round",
            "In a radial field the current in the coil is reversed twice as "
                "often, which evens the push out",
            "In a uniform field the coil's resistance changes with its angle "
                "to the pole pieces",
            "In a radial field the coil sides always cut straight across the "
                "field",
        ],
        "correct_index": 3,
        "why": "In a uniform field the angle between the coil's plane and the "
               "field changes through a turn, so the moment of the two forces "
               "rises and falls. Curved poles make the field point outward "
               "from the axis everywhere, so that angle never changes.",
    },
    {
        "id": "ks4-electric-motors-h10",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor lifts a 2.5 kg load steadily at 0.40 m/s and is 75% "
                "efficient. Calculate the electrical power it must be "
                "supplied with. Take gravitational field strength as "
                "9.8 N/kg.",
        "options": [
            "9.80 W",
            "7.4 W",
            "13.1 W",
            "1.0 W",
        ],
        "correct_index": 2,
        "why": "Weight = 2.5 x 9.8 = 24.5 N, so the useful power is 24.5 x "
               "0.40 = 9.8 W. Input = useful / efficiency = 9.8 / 0.75 = "
               "13.1 W. Multiplying by 0.75 instead gives 7.4 W, and using the "
               "mass in place of the weight gives 1.0 W.",
    },
    {
        "id": "ks4-electric-motors-h11",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Evaluate the claim that a motor with more turns on its coil "
                "must always be more efficient than one with fewer.",
        "options": [
            "Right, because a larger turning effect always means a larger "
                "useful power output",
            "Wrong, because the longer wire has a higher resistance and "
                "wastes more of the input as heat",
            "Right, because the extra turns share the current out and so "
                "each one heats less",
            "Wrong, because adding more turns has no effect at all on the "
                "force produced",
        ],
        "correct_index": 1,
        "why": "More turns do give a larger force, but they also mean more "
               "metres of wire, more resistance and more heating for the same "
               "current, as well as a heavier armature. Efficiency is useful "
               "out over total in, so a bigger output does not settle it.",
    },
    {
        "id": "ks4-electric-motors-h12",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a real electric motor can never be fully "
                "efficient, naming two of the transfers that waste energy.",
        "options": [
            "Heating of the coil's resistance and friction at the bearings "
                "both waste energy",
            "Sound made by the spinning coil and the light given out at the "
                "brushes are the only losses",
            "The magnet loses its strength steadily and the iron core takes "
                "energy to magnetise",
            "The supply pd falls away a little as the motor gradually speeds "
                "up",
        ],
        "correct_index": 0,
        "why": "The coil has resistance, so some of the input always heats it. "
               "The bearings and the brushes rub, so some is lost to friction "
               "and a little to sound. None of these can be removed "
               "completely, so the efficiency is always below 1.",
    },
    {
        "id": "ks4-electric-motors-h13",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor is tested under load. At 0 rev/s its turning effect "
                "is 0.80 N m; at 10 rev/s it is 0.60 N m; at 20 rev/s it is "
                "0.40 N m; at 30 rev/s it is 0.20 N m; at 40 rev/s it is "
                "zero. Identify the stall point and the turning effect there.",
        "options": [
            "0 rev/s, where the coil is held still and the turning effect is "
                "its largest, 0.80 N m",
            "20 rev/s, the middle of the range, where the turning effect has "
                "fallen to half of its largest value",
            "40 rev/s, where the turning effect has fallen away to zero "
                "altogether",
            "10 rev/s, the fastest speed at which there is a useful turning "
                "effect",
        ],
        "correct_index": 0,
        "why": "Stall is the condition where the load holds the shaft still, "
               "so the speed is zero. The readings show the turning effect "
               "falling steadily with speed, so its largest value, 0.80 N m, "
               "is the one at 0 rev/s.",
    },
    {
        "id": "ks4-electric-motors-h14",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why an electric car's motor can give its full "
                "turning effect from rest, while a petrol engine cannot.",
        "options": [
            "The motor stores energy in its magnets while the car is parked "
                "and releases it at once",
            "The motor's force depends on the current, which is at its very "
                "largest when the coil is not moving",
            "The motor has gears that a petrol engine does not, so it always "
                "starts in a low gear",
            "The motor is much lighter than an engine, so far less force is "
                "needed to start it",
        ],
        "correct_index": 1,
        "why": "The motor's couple comes from F = N B I l, and the current is "
               "largest at rest, so the turning effect is available "
               "immediately. A petrol engine must already be turning fast "
               "enough for its cylinders to fire, which is why it needs a "
               "clutch and a starter.",
    },
    {
        "id": "ks4-electric-motors-h15",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the gaps in a motor's split-ring commutator must "
                "line up with the position at which the coil feels no turning "
                "effect.",
        "options": [
            "So the brushes get a moment to cool before they carry the "
                "current again",
            "So the coil is briefly free to slow down, which stops the motor "
                "racing away",
            "So the current reverses just as the coil is passing through "
                "that point",
            "So the current in the coil is at its largest exactly where the "
                "force on it is largest",
        ],
        "correct_index": 2,
        "why": "The coil coasts through that position on its momentum. "
               "Reversing the current exactly there means the forces have "
               "already swapped over by the time they can act again, so they "
               "keep pushing the coil onward instead of back.",
    },
    {
        "id": "ks4-electric-motors-h16",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor is rewound using wire of half the cross-sectional "
                "area, with the same number of turns and the same supply. "
                "Predict the effect on the current and on the turning effect.",
        "options": [
            "Both double, because thinner wire carries a bigger current for "
                "the same supply pd",
            "The current halves but the turning effect is unchanged, because "
                "the number of turns is the same",
            "Neither changes, because the supply pd has not been altered at "
                "all",
            "Both halve, because the resistance doubles and the force "
                "follows the current",
        ],
        "correct_index": 3,
        "why": "Halving the cross-sectional area doubles the resistance of the "
               "winding, so for the same pd the current halves. F = N B I l is "
               "proportional to the current, so the force on each side and the "
               "couple halve with it.",
    },
    {
        "id": "ks4-electric-motors-h17",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the forces on the two short sides of a motor's "
                "coil do nothing to turn it.",
        "options": [
            "The current in them is far smaller than the current in the two "
                "long sides",
            "They lie outside the magnetic field, where there are no field "
                "lines at all to push on them",
            "They act along the axis itself, so they have no moment about it "
                "at all",
            "They are much too short for a force of any useful size to act "
                "on them at all",
        ],
        "correct_index": 2,
        "why": "The forces on the short sides are directed along the axis of "
               "rotation, one each way. Their line of action passes through "
               "the axis, so their moment about it is zero: they stretch or "
               "squeeze the coil rather than turning it.",
    },
    {
        "id": "ks4-electric-motors-h18",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A workshop must choose between a cheap hoist motor that is "
                "45% efficient and a dearer one that is 90% efficient for the "
                "same lifting work. Estimate how much more electrical energy "
                "the cheap one uses, and say what that means for the choice.",
        "options": [
            "Twice as much, because halving the efficiency doubles the input "
                "needed for the same job",
            "Half as much again, because the difference between the two "
                "figures is forty-five percentage points",
            "Forty-five times as much, because efficiency is a ratio of the "
                "two figures",
            "The same, because the useful energy that is delivered is "
                "identical",
        ],
        "correct_index": 0,
        "why": "Input = useful output / efficiency. For the same useful "
               "output, an efficiency of 0.45 needs twice the input that 0.90 "
               "needs. The dearer motor halves the running electricity, so "
               "over a working life it can easily repay its extra cost.",
    },
]
