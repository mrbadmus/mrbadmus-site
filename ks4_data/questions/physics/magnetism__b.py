"""Physics · Magnetism — the transducer and generator half of the topic.

Five Triple-only, Higher-tier subtopics: loudspeakers and headphones, induced
potential, uses of the generator effect, microphones and transformers. The
distractors are built on the four misconceptions the briefs declare and the
lesson prose keeps meeting: the motor effect and the generator effect swapped
round, an induced pd thought to depend on the magnet's strength alone rather
than on the RATE of flux change, and step-up and step-down inverted. (The
"a transformer cannot work on d.c." misconception is deliberately NOT used:
the transformers lesson page prints that exact question with its answer.)
The calculations' wrong options are the
wrong workings — inverted turns ratio, I×R instead of I²R, the secondary
current quoted as the primary, a dropped power of ten — never noise.

Written for MRB-332 against docs/ks4/pool-authoring.md. `magnetism__a.py`
holds the other five subtopics of this topic.
"""

TOPIC = "magnetism"
SUBJECT = "physics"

QUESTIONS = [
    # ── loudspeakers-headphones ─────────────────────────────────────────
    # AQA 6.7.2.4 (HT only, physics only). TRIPLE + HIGHER.
    {
        "id": "ks4-loudspeakers-headphones-e01",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "The permanent magnet is taken out of a loudspeaker and the "
                "same alternating current is passed through its voice coil. "
                "State what the cone does.",
        "options": [
            "It vibrates at twice the frequency, because the coil's own "
            "magnetic field then acts alone",
            "It vibrates exactly as before, because the current alone is what "
            "moves it",
            "It stays still, because there is no longer a magnetic field for "
            "the current to feel a force in",
            "It is pushed steadily outwards and held there by the coil's own "
            "magnetic field",
        ],
        "correct_index": 2,
        "why": "The motor effect needs both a current and a magnetic field "
               "for that current to sit in; with the magnet gone no force "
               "acts on the coil at all.",
    },
    {
        "id": "ks4-loudspeakers-headphones-e02",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the useful energy transfer that takes place in a "
                "loudspeaker.",
        "options": [
            "Electrical energy to kinetic energy of the cone to sound energy",
            "Sound energy to kinetic energy of the cone to electrical energy",
            "Electrical energy to thermal energy of the coil to sound energy",
            "Kinetic energy of the cone to electrical energy to sound energy",
        ],
        "correct_index": 0,
        "why": "The amplifier's electrical energy makes the coil and cone "
               "move, and the moving cone pushes air to make sound; the "
               "reverse chain is a microphone, not a loudspeaker.",
    },
    {
        "id": "ks4-loudspeakers-headphones-e03",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which effect makes the voice coil of a loudspeaker "
                "move.",
        "options": [
            "The generator effect, because motion of the coil induces a "
            "current in it",
            "Electrostatic attraction between the charged cone and the "
            "magnet",
            "Electromagnetic induction in a soft iron core behind the cone",
            "The motor effect, because a current-carrying wire in a field "
            "feels a force",
        ],
        "correct_index": 3,
        "why": "A current in the coil sits in the magnet's field, so the coil "
               "feels a force — that is the motor effect, and the generator "
               "effect is its exact reverse.",
    },
    {
        "id": "ks4-loudspeakers-headphones-e04",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "The diaphragm in a pair of headphones is far smaller than a "
                "loudspeaker cone. State the reason for this.",
        "options": [
            "A smaller diaphragm vibrates faster, so headphones sound higher "
            "in pitch than loudspeakers",
            "Only a small volume of air has to be moved to reach an ear a "
            "centimetre away",
            "A smaller diaphragm needs no permanent magnet, which keeps the "
            "headphones light",
            "A smaller diaphragm works by the generator effect instead of the "
            "motor effect",
        ],
        "correct_index": 1,
        "why": "Loudness depends on how much air is set moving, and an "
               "earpiece only has to move the air in the ear canal rather "
               "than filling a room.",
    },
    {
        "id": "ks4-loudspeakers-headphones-s01",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A typical loudspeaker transfers only a few per cent of its "
                "input energy usefully. Explain where most of the input "
                "energy is transferred.",
        "options": [
            "To sound waves that travel backwards from the rear of the cone",
            "To thermal energy, mostly by resistance heating of the voice coil",
            "To the permanent magnet, whose field is topped up by the current",
            "To kinetic energy of the permanent magnet as it vibrates in step",
        ],
        "correct_index": 1,
        "why": "The voice coil has resistance, so most of the electrical "
               "energy is dissipated as heat in the wire before it can be "
               "transferred to the air.",
    },
    {
        "id": "ks4-loudspeakers-headphones-s02",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A loudspeaker is supplied with 60 W of electrical power and "
                "emits 1.8 W as sound. Calculate its efficiency.",
        "options": [
            "0.03%",
            "33%",
            "97%",
            "3%",
        ],
        "correct_index": 3,
        "why": "Efficiency is useful output over total input: 1.8 ÷ 60 = 0.03, "
               "which is 3%.",
    },
    {
        "id": "ks4-loudspeakers-headphones-s03",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A woofer has a large cone and a tweeter has a small one. "
                "Explain why the large cone suits low-frequency sound.",
        "options": [
            "A large cone shifts a large volume of air on each slow, wide "
            "vibration, which is what low notes need",
            "A large cone carries more turns of wire, so a low-frequency "
            "current produces a bigger force on it",
            "A large cone has a lower resistance, so a larger current flows "
            "through it at low frequencies",
            "A large cone is heavier, so the weak force of a low-frequency "
            "signal cannot make it distort",
        ],
        "correct_index": 0,
        "why": "Loudness comes from the volume of air moved, and low notes "
               "need large slow movements of a lot of air — which a big cone "
               "can supply and a tweeter cannot.",
    },
    {
        "id": "ks4-loudspeakers-headphones-s04",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The permanent magnet in a loudspeaker is replaced by a "
                "weaker one and the same a.c. signal is used. Predict the "
                "effect on the sound produced.",
        "options": [
            "The pitch falls, because a weaker field lets the cone vibrate "
            "more slowly",
            "The pitch rises, because the cone is held less firmly in its "
            "resting position",
            "The sound is quieter, because a smaller force moves the cone a "
            "shorter distance",
            "Nothing changes, because loudness is fixed entirely by the a.c. "
            "signal supplied",
        ],
        "correct_index": 2,
        "why": "Pitch is set by the frequency of the a.c., which has not "
               "changed; a weaker field gives a smaller force, so the cone's "
               "amplitude — and the loudness — falls.",
    },
    {
        "id": "ks4-loudspeakers-headphones-h01",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student writes: 'The cone vibrates because the permanent "
                "magnet is pulled backwards and forwards by the coil.' "
                "Identify the error in this reasoning.",
        "options": [
            "There is no error at all — the magnet really does move, and "
            "the cone is fixed to it",
            "The magnet is not permanent — it is an electromagnet fed by the "
            "same alternating current",
            "The force acts directly on the cone itself, rather than on the "
            "magnet or on the coil",
            "The magnet is fixed and heavy; the force acts on the "
            "current-carrying coil, which moves",
        ],
        "correct_index": 3,
        "why": "Both magnet and coil feel equal and opposite forces, but the "
               "magnet is clamped to the frame and massive, so it is the light "
               "coil and its cone that actually move.",
    },
    {
        "id": "ks4-loudspeakers-headphones-h02",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A loudspeaker is driven by an alternating signal of period "
                "4.0 ms. Determine the frequency of the sound produced and "
                "state whether a person could hear it.",
        "options": [
            "0.25 Hz — far below the audible range of 20 Hz to 20 000 Hz",
            "25 Hz — just inside the audible range of 20 Hz to 20 000 Hz",
            "250 Hz — well inside the audible range of 20 Hz to 20 000 Hz",
            "2500 Hz — above the audible range of 20 Hz to 20 000 Hz",
        ],
        "correct_index": 2,
        "why": "f = 1 ÷ T = 1 ÷ 0.0040 s = 250 Hz, and the cone vibrates at "
               "the frequency of the current, so the sound is 250 Hz.",
    },
    {
        "id": "ks4-loudspeakers-headphones-h03",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Two loudspeakers are identical except that one has twice as "
                "many turns on its voice coil. The same current at the same "
                "frequency flows in each. Predict the difference in the sound.",
        "options": [
            "The sound from the larger coil is higher in pitch, because more "
            "turns raise the frequency of the force",
            "The sound from the larger coil is louder, because a bigger force "
            "moves the cone through a greater distance",
            "The sound from the larger coil is quieter, because extra turns "
            "weaken the field of the permanent magnet",
            "The two sounds are identical, because the number of turns only "
            "matters inside a transformer",
        ],
        "correct_index": 1,
        "why": "Each turn in the field feels its own force, so doubling the "
               "turns at the same current doubles the total force and the "
               "cone's amplitude — the pitch, set by frequency, is unchanged.",
    },
    {
        "id": "ks4-loudspeakers-headphones-h04",
        "subtopic_slug": "loudspeakers-headphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the physics used by a loudspeaker with that used by "
                "a car's electric starter motor.",
        "options": [
            "Both use the motor effect on a current-carrying coil: a.c. makes "
            "the loudspeaker coil oscillate, d.c. and a commutator make the "
            "motor coil turn",
            "Both use the generator effect: the loudspeaker turns motion into "
            "sound, and the starter motor turns motion into a current in the "
            "car battery",
            "Both use the motor effect, but the loudspeaker's coil rotates "
            "continuously while the starter motor's coil only rocks back and "
            "forth",
            "The loudspeaker uses the motor effect and the starter motor uses "
            "induction, so the two devices share no underlying physics at all",
        ],
        "correct_index": 0,
        "why": "Both are the motor effect — a force on a current in a field — "
               "and only the supply and the connections differ, giving an "
               "oscillation in one case and continuous rotation in the other.",
    },

    # ── induced-potential ───────────────────────────────────────────────
    # AQA 6.7.3.1 (HT only, physics only). TRIPLE + HIGHER.
    {
        "id": "ks4-induced-potential-e01",
        "subtopic_slug": "induced-potential",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the name given to the effect in which a potential "
                "difference is induced across a conductor that is moved "
                "through a magnetic field.",
        "options": [
            "The motor effect",
            "The generator effect",
            "The heating effect of a current",
            "The magnetising effect of a current",
        ],
        "correct_index": 1,
        "why": "Motion in and electricity out is the generator effect; the "
               "motor effect is its exact reverse, with a current supplied "
               "and motion produced.",
    },
    {
        "id": "ks4-induced-potential-e02",
        "subtopic_slug": "induced-potential",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which of these actions would induce a potential "
                "difference across a coil of wire.",
        "options": [
            "Holding a very strong magnet close to one end of the coil",
            "Connecting the two ends of the coil to a battery",
            "Warming the coil gently with a Bunsen burner",
            "Pulling a magnet quickly out of the middle of the coil",
        ],
        "correct_index": 3,
        "why": "Moving the magnet changes the flux through the coil, and a "
               "changing flux is the one thing that induces a pd.",
    },
    {
        "id": "ks4-induced-potential-e03",
        "subtopic_slug": "induced-potential",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "In Fleming's right-hand rule the first finger points along "
                "the magnetic field and the thumb points along the motion of "
                "the wire. State what the second finger shows.",
        "options": [
            "The direction of the induced current in the wire",
            "The direction of the force acting on the wire",
            "The direction of the field the coil produces around itself",
            "The direction from the north pole to the south pole of the magnet",
        ],
        "correct_index": 0,
        "why": "In the right-hand rule the second finger gives the induced "
               "current; the left-hand rule, with the second finger as the "
               "supplied current, is the motor-effect version.",
    },
    {
        "id": "ks4-induced-potential-e04",
        "subtopic_slug": "induced-potential",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State how a simple alternating-current generator connects "
                "its rotating coil to the external circuit.",
        "options": [
            "Through a split-ring commutator, which swaps the connections "
            "every half turn",
            "Through one solid ring, which allows the coil to turn in one "
            "direction only",
            "Through slip rings, which turn with the coil and never swap the "
            "connections",
            "Through two carbon rings clamped to the outside of the permanent "
            "magnet",
        ],
        "correct_index": 2,
        "why": "Slip rings rotate with the coil, so each end of the coil keeps "
               "its own contact and the output reverses with the coil — "
               "giving a.c.",
    },
    {
        "id": "ks4-induced-potential-s01",
        "subtopic_slug": "induced-potential",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A magnet is pushed towards a coil that forms part of a "
                "complete circuit. Explain why a force must be kept on the "
                "magnet to keep it moving.",
        "options": [
            "The magnet is attracted to the iron inside the copper wire and "
            "must be pulled free of it",
            "The induced current heats the wire, and the warm air around it "
            "pushes back on the magnet",
            "The induced current sets up a field that opposes the motion, so "
            "work has to be done against it",
            "The coil's own field always attracts the magnet, so the magnet "
            "has to be slowed as it nears",
        ],
        "correct_index": 2,
        "why": "The induced current always opposes the change causing it, so "
               "the coil pushes back — and that work done is the source of the "
               "electrical energy produced.",
    },
    {
        "id": "ks4-induced-potential-s02",
        "subtopic_slug": "induced-potential",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The coil of a simple generator is rotated steadily at 25 "
                "revolutions per second. Determine the frequency of the "
                "alternating potential difference produced.",
        "options": [
            "25 Hz",
            "50 Hz",
            "12.5 Hz",
            "1500 Hz",
        ],
        "correct_index": 0,
        "why": "One complete rotation produces one complete cycle of output, "
               "so the output frequency equals the rotation rate.",
    },
    {
        "id": "ks4-induced-potential-s03",
        "subtopic_slug": "induced-potential",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The slip rings of a generator are replaced by a split-ring "
                "commutator and the coil is turned at the same speed. Predict "
                "the output.",
        "options": [
            "Alternating current at twice the frequency it had before",
            "A perfectly smooth and constant direct current",
            "No output at all, because the connections break twice per turn",
            "Pulsing direct current — the pd rises and falls but never "
            "reverses",
        ],
        "correct_index": 3,
        "why": "The commutator swaps the connections each half turn, so the "
               "output keeps one sign, but its size still varies through each "
               "turn — pulsing d.c., not a steady value.",
    },
    {
        "id": "ks4-induced-potential-s04",
        "subtopic_slug": "induced-potential",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A straight wire is moved downwards between the poles of a "
                "magnet and a current is induced. Predict the induced current "
                "if the wire is instead moved upwards at the same speed.",
        "options": [
            "The same size, flowing in the same direction as before",
            "The same size, but flowing in the opposite direction",
            "Twice the size, and flowing in the opposite direction",
            "No current at all, because a wire must move downwards to cut "
            "field lines",
        ],
        "correct_index": 1,
        "why": "Reversing the motion reverses the induced current — Fleming's "
               "right-hand rule with the thumb turned round — while the speed, "
               "and so the size, is unchanged.",
    },
    {
        "id": "ks4-induced-potential-h01",
        "subtopic_slug": "induced-potential",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A strong magnet dropped down a vertical copper tube falls "
                "far more slowly than an identical magnet dropped down a "
                "plastic tube of the same size. Explain this observation.",
        "options": [
            "Currents induced in the copper make a field that opposes the "
            "magnet's motion",
            "Copper is a magnetic material, so it attracts the magnet and "
            "holds it back",
            "The copper tube is much heavier, so it resists the magnet's fall "
            "more strongly",
            "Air cannot escape past a magnet in a metal tube as easily as in "
            "a plastic one",
        ],
        "correct_index": 0,
        "why": "The falling magnet changes the flux through the copper, "
               "inducing currents whose field opposes the change — copper is "
               "not magnetic, but it does conduct.",
    },
    {
        "id": "ks4-induced-potential-h02",
        "subtopic_slug": "induced-potential",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "The same bar magnet is pushed fully into two coils. Coil A "
                "has 200 turns and takes 0.50 s; coil B has 400 turns and "
                "takes 2.0 s. Compare the induced potential differences.",
        "options": [
            "B is twice A, because B has twice as many turns of wire",
            "A is twice B: twice the turns doubles the pd, but four times the "
            "time quarters it",
            "They are equal, because the same magnet is used in both coils",
            "B is four times A, because the number of turns matters far more "
            "than the time taken",
        ],
        "correct_index": 1,
        "why": "The pd goes with turns × rate of flux change: A gives "
               "200 ÷ 0.50 = 400 units against B's 400 ÷ 2.0 = 200, so A is "
               "twice B.",
    },
    {
        "id": "ks4-induced-potential-h03",
        "subtopic_slug": "induced-potential",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An electric motor and a generator can be built from exactly "
                "the same parts. Explain what decides which of the two a "
                "particular device is.",
        "options": [
            "Using a permanent magnet makes the device a motor; using an "
            "electromagnet makes it a generator",
            "Slip rings make it a motor; a split-ring commutator makes it a "
            "generator",
            "The energy transfer: current in, rotation out is a motor; "
            "rotation in, current out is a generator",
            "The rotation speed: the device is a generator only if it turns "
            "faster than the mains frequency of 50 Hz",
        ],
        "correct_index": 2,
        "why": "The same coil in the same field either feels a force when a "
               "current is supplied, or has a pd induced when it is turned — "
               "what is put in decides which.",
    },
    {
        "id": "ks4-induced-potential-h04",
        "subtopic_slug": "induced-potential",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A small generator on a bicycle wheel gives an output of "
                "3.0 V when the bicycle travels at 4.0 m/s. Estimate the "
                "output at 10 m/s and state the assumption made.",
        "options": [
            "1.2 V, assuming the induced pd is inversely proportional to speed",
            "3.0 V, assuming the induced pd is fixed by the magnet alone",
            "19 V, assuming the induced pd is proportional to the square of "
            "the speed",
            "7.5 V, assuming the induced pd is proportional to the rate of "
            "rotation",
        ],
        "correct_index": 3,
        "why": "The pd goes with the rate of change of flux, so it scales "
               "directly with speed: 3.0 V × (10 ÷ 4.0) = 7.5 V.",
    },

    # ── uses-generator-effect ───────────────────────────────────────────
    # AQA 6.7.3.2 (HT only, physics only). TRIPLE + HIGHER.
    {
        "id": "ks4-uses-generator-effect-e01",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the device that a steam turbine in a power station is "
                "used to turn.",
        "options": [
            "A transformer, which raises the pressure of the steam supplied",
            "A dynamo, which supplies the National Grid with direct current",
            "An electric motor, which then drives the generator alongside it",
            "An alternator, which produces the alternating current supplied",
        ],
        "correct_index": 3,
        "why": "Power stations generate a.c., and it is an alternator — a "
               "generator with slip rings — that the turbine turns.",
    },
    {
        "id": "ks4-uses-generator-effect-e02",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the purpose of the alternator fitted to a car engine.",
        "options": [
            "To turn the engine over when the ignition key is first turned",
            "To recharge the battery while the engine is running",
            "To step the battery's 12 V up to the voltage the spark plugs need",
            "To store energy so the car can be driven for a time without fuel",
        ],
        "correct_index": 1,
        "why": "The engine turns the alternator, which transfers kinetic "
               "energy to electrical energy and keeps the battery charged.",
    },
    {
        "id": "ks4-uses-generator-effect-e03",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A bicycle dynamo is driven by the front wheel and lights a "
                "lamp. State the energy transfer taking place.",
        "options": [
            "Chemical energy stored in the dynamo to light energy in the lamp",
            "Electrical energy from the lamp to kinetic energy of the wheel",
            "Kinetic energy of the wheel to electrical energy to light and "
            "heat",
            "Magnetic energy stored in the magnet to electrical energy, until "
            "it runs down",
        ],
        "correct_index": 2,
        "why": "A dynamo stores nothing — the cyclist's work turns the "
               "magnet or coil, and that is what supplies the electrical "
               "energy.",
    },
    {
        "id": "ks4-uses-generator-effect-e04",
        "subtopic_slug": "uses-generator-effect",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the frequency of the alternating supply that the "
                "National Grid delivers to UK homes.",
        "options": [
            "50 Hz",
            "60 Hz",
            "230 Hz",
            "3000 Hz",
        ],
        "correct_index": 0,
        "why": "UK mains is 50 Hz, so a two-pole alternator has to turn 50 "
               "times every second to match it.",
    },
    {
        "id": "ks4-uses-generator-effect-s01",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A power-station alternator with a single pair of magnetic "
                "poles must produce 50 Hz mains electricity. Calculate the "
                "rotation rate needed, in revolutions per minute.",
        "options": [
            "3000 rpm",
            "50 rpm",
            "500 rpm",
            "180 000 rpm",
        ],
        "correct_index": 0,
        "why": "One turn gives one cycle, so 50 turns per second, and "
               "50 × 60 = 3000 turns per minute.",
    },
    {
        "id": "ks4-uses-generator-effect-s02",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "In many large generators the magnet rotates inside a coil "
                "that is held still, rather than the coil rotating in a fixed "
                "field. Explain why a pd is still induced.",
        "options": [
            "The magnet's field grows stronger as it spins faster, and a "
            "growing field creates the pd",
            "The stationary coil acts as an electromagnet and produces its "
            "own alternating field",
            "The flux through the fixed coil still changes as the magnet "
            "turns, and change is what matters",
            "No pd is induced in that design — the conductor itself has to "
            "move for induction to happen",
        ],
        "correct_index": 2,
        "why": "Induction depends on the flux through the coil changing, not "
               "on which part happens to be the one moving.",
    },
    {
        "id": "ks4-uses-generator-effect-s03",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A wind turbine's blades turn far more slowly than its "
                "generator needs. Explain the purpose of the gearbox fitted "
                "between them.",
        "options": [
            "It converts the generator's alternating output into direct "
            "current for the National Grid",
            "It raises the generator's rotation rate, giving a faster flux "
            "change and a larger pd",
            "It lowers the rotation rate so that the generator is not damaged "
            "in a strong wind",
            "It stores energy when the wind drops so that the output pd stays "
            "perfectly constant",
        ],
        "correct_index": 1,
        "why": "Induced pd rises with the rate of change of flux, so the "
               "gearbox trades slow blade rotation for the fast rotation the "
               "generator needs.",
    },
    {
        "id": "ks4-uses-generator-effect-s04",
        "subtopic_slug": "uses-generator-effect",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A cyclist supplies 12 W of mechanical power to a dynamo, "
                "which delivers 6.0 V at 0.50 A to a lamp. Calculate the "
                "efficiency of the dynamo.",
        "options": [
            "4.2%",
            "50%",
            "75%",
            "25%",
        ],
        "correct_index": 3,
        "why": "Useful output = V × I = 6.0 × 0.50 = 3.0 W, so the efficiency "
               "is 3.0 ÷ 12 = 0.25, which is 25%.",
    },
    {
        "id": "ks4-uses-generator-effect-h01",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A hydroelectric station transfers about 90% of its input "
                "energy to electricity, while a gas-fired station transfers "
                "about 45%. Explain the main reason for the difference.",
        "options": [
            "Hydroelectric alternators use stronger magnets, which makes "
            "induction more efficient",
            "Water carries far more energy per kilogram than natural gas does "
            "when it is burned",
            "The gas station must first boil water to steam, and much of that "
            "energy escapes as heat",
            "Hydroelectric stations run at a higher frequency, so less energy "
            "is wasted in the cables",
        ],
        "correct_index": 2,
        "why": "Both end in a generator of similar efficiency; the gas "
               "station's losses come earlier, in the heating and steam "
               "stages the hydroelectric station does not have.",
    },
    {
        "id": "ks4-uses-generator-effect-h02",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A bicycle lamp run from a dynamo is bright at speed but dim "
                "when the cyclist rides slowly. Suggest one change to the "
                "dynamo that would brighten the lamp at low speed.",
        "options": [
            "Connect the lamp with thicker wires, so that a larger pd is "
            "induced in the dynamo coil",
            "Fit a smaller lamp, because a shorter filament glows more "
            "brightly at the same pd",
            "Gear the dynamo down so that it turns more slowly and produces a "
            "steadier output pd",
            "Wind more turns onto the coil, because the induced pd is "
            "proportional to the turns",
        ],
        "correct_index": 3,
        "why": "Speed is fixed by the cyclist, so the way to raise the pd is "
               "to raise one of the other factors — turns, coil area or "
               "magnet strength.",
    },
    {
        "id": "ks4-uses-generator-effect-h03",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the output of an alternator turning at 30 "
                "revolutions per second with the output of the same machine "
                "turning at 60 revolutions per second.",
        "options": [
            "Both double: the frequency goes from 30 Hz to 60 Hz and the peak "
            "pd is larger too",
            "The frequency doubles to 60 Hz but the peak pd is unchanged, "
            "because the magnet is the same",
            "The peak pd doubles but the frequency stays at 50 Hz, which is "
            "fixed by the National Grid",
            "Neither changes, because an alternator's output is set only by "
            "the turns on its coil",
        ],
        "correct_index": 0,
        "why": "Turning twice as fast gives twice as many cycles per second "
               "and twice the rate of flux change, so both the frequency and "
               "the peak pd rise.",
    },
    {
        "id": "ks4-uses-generator-effect-h04",
        "subtopic_slug": "uses-generator-effect",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A car alternator is driven by a belt from the engine. When "
                "the headlights, heater and rear-screen heater are all "
                "switched on, the engine has to work harder. Explain why.",
        "options": [
            "The extra devices raise the circuit's resistance, so the belt "
            "has to be driven faster to compensate",
            "A larger induced current makes a field that opposes the "
            "rotation, so more work must be done",
            "The battery discharges, and a discharged battery is heavier for "
            "the engine to carry along",
            "The alternator's magnets weaken as more current is drawn, so "
            "more belt turns are needed",
        ],
        "correct_index": 1,
        "why": "The induced current always opposes the change producing it, "
               "so drawing more current makes the alternator harder to turn — "
               "the engine supplies that extra energy.",
    },

    # ── microphones ─────────────────────────────────────────────────────
    # AQA 6.7.3.3 (HT only, physics only). TRIPLE + HIGHER.
    {
        "id": "ks4-microphones-e01",
        "subtopic_slug": "microphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the job of the permanent magnet inside a dynamic "
                "(moving-coil) microphone.",
        "options": [
            "To provide the magnetic field that the moving coil travels "
            "through",
            "To pull the diaphragm back to its resting position after each "
            "vibration",
            "To supply the energy that the microphone's output signal carries",
            "To amplify the small potential difference induced in the coil",
        ],
        "correct_index": 0,
        "why": "Induction needs a field for the conductor to move through; "
               "the magnet supplies it, while the energy of the signal comes "
               "from the sound itself.",
    },
    {
        "id": "ks4-microphones-e02",
        "subtopic_slug": "microphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the correct order of stages inside a dynamic "
                "microphone.",
        "options": [
            "Coil moves, then the diaphragm vibrates, then a sound wave is "
            "produced",
            "Sound wave arrives, then the coil moves, then the diaphragm "
            "vibrates",
            "Sound arrives, the diaphragm vibrates, the coil moves in the "
            "field, a pd is induced",
            "A sound wave arrives, the magnet itself moves, the diaphragm "
            "vibrates, and a pd is induced",
        ],
        "correct_index": 2,
        "why": "The sound drives the diaphragm, the diaphragm carries the "
               "coil through the magnet's field, and that motion is what "
               "induces the pd.",
    },
    {
        "id": "ks4-microphones-e03",
        "subtopic_slug": "microphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the output of a dynamic microphone whose diaphragm is "
                "completely still in a silent room.",
        "options": [
            "A steady direct pd, because the coil sits inside a magnetic field",
            "No pd at all, because the flux through the coil is not changing",
            "An alternating pd at 50 Hz, produced by the permanent magnet "
            "itself",
            "A large pd, because the coil rests closest to the magnet when "
            "still",
        ],
        "correct_index": 1,
        "why": "A conductor at rest in a field has no changing flux through "
               "it, so nothing is induced — the microphone needs the motion.",
    },
    {
        "id": "ks4-microphones-e04",
        "subtopic_slug": "microphones",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State why the signal from a dynamic microphone is passed "
                "through a preamplifier before it is recorded.",
        "options": [
            "To convert the direct current the microphone gives into "
            "alternating current",
            "To lower the frequency of the signal so that it can be stored "
            "digitally",
            "To remove the magnetic field that the microphone adds to the "
            "signal",
            "The induced pd is only a few millivolts, far too small to record "
            "directly",
        ],
        "correct_index": 3,
        "why": "A small coil moving slowly induces only millivolts, so the "
               "signal has to be amplified before anything downstream can use "
               "it.",
    },
    {
        "id": "ks4-microphones-s01",
        "subtopic_slug": "microphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A singer holds the same note but sings it more loudly into a "
                "dynamic microphone. Explain the effect on the output signal.",
        "options": [
            "The output frequency rises, because a louder sound is also a "
            "higher-pitched sound",
            "The output frequency falls, because the diaphragm is pushed "
            "harder and moves more slowly",
            "The output is unchanged, because the induced pd depends only on "
            "the magnet's strength",
            "The output amplitude rises, because the diaphragm and coil move "
            "further and faster",
        ],
        "correct_index": 3,
        "why": "A louder sound carries larger pressure variations, so the coil "
               "moves faster and further — a bigger induced pd at the same "
               "frequency.",
    },
    {
        "id": "ks4-microphones-s02",
        "subtopic_slug": "microphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A condenser microphone needs a power supply of its own, but "
                "a dynamic microphone does not. Explain why.",
        "options": [
            "A dynamic microphone has a small battery sealed inside its own "
            "case",
            "A dynamic microphone induces its own pd; a condenser type needs "
            "a pd across its plates",
            "A condenser microphone has to warm its diaphragm up before it "
            "becomes sensitive to sound at all",
            "A condenser microphone contains a small motor that the supply is "
            "needed to drive",
        ],
        "correct_index": 1,
        "why": "The dynamic microphone generates its signal by induction, "
               "taking its energy from the sound itself; the condenser type "
               "only alters an externally supplied pd.",
    },
    {
        "id": "ks4-microphones-s03",
        "subtopic_slug": "microphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A pair of headphones is plugged into a microphone socket and "
                "someone speaks into them. Predict what is recorded, and "
                "explain.",
        "options": [
            "Nothing at all, because a loudspeaker cannot be operated the "
            "other way round",
            "Nothing, unless the headphones are first given a power supply of "
            "their own",
            "A weak signal, because the moving coil in a field induces a pd — "
            "the same physics reversed",
            "Nothing, because the sound waves would force current the wrong "
            "way and damage the coil",
        ],
        "correct_index": 2,
        "why": "A moving-coil earpiece and a dynamic microphone are the same "
               "parts, so speech that moves the diaphragm induces a pd, just "
               "a very small one.",
    },
    {
        "id": "ks4-microphones-s04",
        "subtopic_slug": "microphones",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A microphone produces an output of 2.0 mV. It feeds an "
                "amplifier with a voltage gain of 250. Calculate the "
                "amplifier's output potential difference.",
        "options": [
            "0.50 V",
            "125 V",
            "500 V",
            "0.0080 V",
        ],
        "correct_index": 0,
        "why": "Gain multiplies the input: 2.0 mV = 0.0020 V, and "
               "0.0020 V × 250 = 0.50 V.",
    },
    {
        "id": "ks4-microphones-h01",
        "subtopic_slug": "microphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A ribbon microphone hangs a thin metal ribbon between the "
                "poles of a magnet, with no coil at all. Explain how it still "
                "produces a signal.",
        "options": [
            "The sound wave charges the ribbon, and that moving charge is the "
            "signal",
            "The ribbon is a conductor moving in a magnetic field, so a pd is "
            "induced across it",
            "The ribbon heats as it vibrates, and the change in its resistance "
            "makes the signal",
            "The ribbon's motion changes the strength of the permanent magnet, "
            "driving a current",
        ],
        "correct_index": 1,
        "why": "Induction needs a conductor and a changing flux, not a coil — "
               "a single moving strip of metal cutting field lines is enough.",
    },
    {
        "id": "ks4-microphones-h02",
        "subtopic_slug": "microphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student writes: 'A microphone works by the motor effect, "
                "because a force pushes its diaphragm inwards.' Identify what "
                "is wrong with this reasoning.",
        "options": [
            "The motor effect starts with a current; here the motion comes "
            "first and induces the current",
            "Nothing is wrong — sound applies a force to the diaphragm, so "
            "this is the motor effect",
            "The only error is 'inwards' — the diaphragm is actually pulled "
            "outwards first every time",
            "The error is that no force acts at all, because sound waves "
            "carry no energy to the diaphragm",
        ],
        "correct_index": 0,
        "why": "The motor effect is current in, motion out; a microphone is "
               "motion in, current out, which is the generator effect.",
    },
    {
        "id": "ks4-microphones-h03",
        "subtopic_slug": "microphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Two dynamic microphones are identical except that one coil "
                "has 150 turns and the other has 600. The same sound reaches "
                "each. Determine how their induced potential differences "
                "compare.",
        "options": [
            "The 600-turn coil gives a quarter of the pd, because more turns "
            "means more resistance",
            "Both give the same pd, because the sound and the magnet are the "
            "same in each case",
            "The 600-turn coil gives twice the pd, because pd depends on the "
            "square root of the turns",
            "The 600-turn coil gives four times the pd, assuming both coils "
            "move alike in the same field",
        ],
        "correct_index": 3,
        "why": "Each turn has its own pd induced and they add, so the pd is "
               "proportional to the number of turns: 600 ÷ 150 = 4.",
    },
    {
        "id": "ks4-microphones-h04",
        "subtopic_slug": "microphones",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An old telephone handset used a moving-coil microphone and a "
                "moving-coil earpiece. Explain, in terms of energy, why the "
                "earpiece needed an amplifier but the microphone did not.",
        "options": [
            "The microphone stores energy in its own magnet, so it never "
            "needs any supply of its own",
            "The earpiece uses the motor effect, which can only ever be "
            "driven by direct current",
            "The microphone takes its energy from the sound, but moving air "
            "needs far more power than that signal carries",
            "The earpiece works at higher frequencies than the microphone, "
            "and high frequencies always need more power",
        ],
        "correct_index": 2,
        "why": "A microphone only has to be driven by the sound falling on "
               "it, but an earpiece must supply the energy of the sound it "
               "makes, and that has to come from an amplifier.",
    },

    # ── transformers ────────────────────────────────────────────────────
    # AQA 6.7.3.4 (HT only, physics only). TRIPLE + HIGHER.
    {
        "id": "ks4-transformers-e01",
        "subtopic_slug": "transformers",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer has the same number of turns on its primary "
                "and secondary coils. A potential difference of 24 V is "
                "supplied to the primary. State the output potential "
                "difference.",
        "options": [
            "48 V, because the two coils add their potential differences "
            "together",
            "12 V, because the input pd is shared equally between the two "
            "coils",
            "24 V, because equal numbers of turns give equal potential "
            "differences",
            "0 V, because a transformer cannot work unless the two coils have "
            "different numbers of turns",
        ],
        "correct_index": 2,
        "why": "Vₛ/Vₚ = Nₛ/Nₚ, so an equal turns ratio leaves the pd "
               "unchanged — a transformer like this isolates a circuit rather "
               "than changing its pd.",
    },
    {
        "id": "ks4-transformers-e02",
        "subtopic_slug": "transformers",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the purpose of the soft iron core in a transformer.",
        "options": [
            "It carries the current across from the primary coil to the "
            "secondary coil",
            "It stores the energy that the secondary coil then releases into "
            "the circuit",
            "It converts the alternating current into direct current for the "
            "secondary coil",
            "It carries the changing magnetic flux from the primary coil to "
            "the secondary coil",
        ],
        "correct_index": 3,
        "why": "The two coils are not electrically joined at all — iron is "
               "easily magnetised, so it channels the changing flux from one "
               "coil to the other.",
    },
    {
        "id": "ks4-transformers-e03",
        "subtopic_slug": "transformers",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer has 500 turns on its primary coil and 100 "
                "turns on its secondary coil. State the type of transformer.",
        "options": [
            "Step-up, because the primary coil is the one with more turns",
            "Step-down, because the secondary has fewer turns than the primary",
            "Step-up, because the ratio of the two turn counts is greater "
            "than one",
            "Neither — a whole-number turns ratio leaves the pd completely "
            "unchanged",
        ],
        "correct_index": 1,
        "why": "The output pd follows the secondary's share of the turns, so "
               "100 turns out of 500 gives a fifth of the input pd.",
    },
    {
        "id": "ks4-transformers-e04",
        "subtopic_slug": "transformers",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer has 50 turns on its primary coil and 300 "
                "turns on its secondary coil. The primary pd is 12 V. "
                "Calculate the secondary pd.",
        "options": [
            "72 V",
            "2.0 V",
            "12 V",
            "3600 V",
        ],
        "correct_index": 0,
        "why": "Vₛ = Vₚ × Nₛ/Nₚ = 12 V × 300/50 = 72 V.",
    },
    {
        "id": "ks4-transformers-s01",
        "subtopic_slug": "transformers",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer steps 400 V down to 20 V. Its primary coil "
                "has 1200 turns. Calculate the number of turns on the "
                "secondary coil.",
        "options": [
            "60 turns",
            "24 000 turns",
            "30 turns",
            "600 turns",
        ],
        "correct_index": 0,
        "why": "Nₛ = Nₚ × Vₛ/Vₚ = 1200 × 20/400 = 60 turns.",
    },
    {
        "id": "ks4-transformers-s02",
        "subtopic_slug": "transformers",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer is 100% efficient. Its primary pd is 240 V and "
                "its primary current is 0.50 A. The secondary pd is 12 V. "
                "Calculate the secondary current.",
        "options": [
            "0.025 A",
            "10 A",
            "0.50 A",
            "20 A",
        ],
        "correct_index": 1,
        "why": "VₚIₚ = VₛIₛ, so Iₛ = (240 × 0.50) ÷ 12 = 10 A — stepping the "
               "pd down steps the current up.",
    },
    {
        "id": "ks4-transformers-s03",
        "subtopic_slug": "transformers",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a step-up transformer does not produce extra "
                "power.",
        "options": [
            "It does produce extra power, which is exactly why the National "
            "Grid uses one",
            "The extra power comes from the iron core, which is slowly used "
            "up in service",
            "Extra power is produced but lost as heat in the cables, so none "
            "of it can be used",
            "The current falls in the same ratio as the pd rises, so VₚIₚ and "
            "VₛIₛ stay equal",
        ],
        "correct_index": 3,
        "why": "A transformer changes pd, not energy: raising the pd by a "
               "factor lowers the current by the same factor, so power in "
               "equals power out.",
    },
    {
        "id": "ks4-transformers-s04",
        "subtopic_slug": "transformers",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The core of a real transformer is built from thin iron "
                "sheets insulated from one another rather than one solid "
                "block. Explain why.",
        "options": [
            "Thin sheets are much easier to bend into shape around the two "
            "coils during manufacture",
            "Thin sheets make the field stronger by concentrating the flux "
            "into separate layers",
            "It reduces the currents induced in the core itself, which would "
            "heat it and waste energy",
            "It lets air flow between the sheets, cooling the core while the "
            "transformer is running",
        ],
        "correct_index": 2,
        "why": "The changing flux would induce currents in a solid iron core "
               "too, heating it; insulated laminations break up the paths "
               "those currents could take.",
    },
    {
        "id": "ks4-transformers-h01",
        "subtopic_slug": "transformers",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A power station transmits 20 MW along a cable of resistance "
                "5.0 Ω at 400 kV. Calculate the power wasted as heat in the "
                "cable.",
        "options": [
            "0.25 kW",
            "1.25 MW",
            "125 kW",
            "12.5 kW",
        ],
        "correct_index": 3,
        "why": "I = P ÷ V = 20 000 000 ÷ 400 000 = 50 A, and the loss is "
               "I²R = 50² × 5.0 = 12 500 W = 12.5 kW.",
    },
    {
        "id": "ks4-transformers-h02",
        "subtopic_slug": "transformers",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the power wasted in a cable of resistance 4.0 Ω when "
                "10 MW is transmitted at 10 kV with the waste when the same "
                "power is transmitted at 100 kV.",
        "options": [
            "4.0 MW at 10 kV and 40 kW at 100 kV — a hundred times less waste",
            "4.0 MW at 10 kV and 400 kW at 100 kV — ten times less waste",
            "40 kW at 10 kV and 4.0 MW at 100 kV — the higher pd wastes more",
            "4.0 MW at both, because the cable's resistance has not been "
            "changed",
        ],
        "correct_index": 0,
        "why": "Ten times the pd means a tenth of the current, and the loss "
               "goes as I², so it falls by a factor of a hundred: 1000 A "
               "gives 4.0 MW, 100 A gives 40 kW.",
    },
    {
        "id": "ks4-transformers-h03",
        "subtopic_slug": "transformers",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A transformer runs from a 230 V mains supply and lights a "
                "lamp rated 9.0 V, 18 W at its normal brightness. The "
                "transformer is 90% efficient. Calculate the current drawn "
                "from the mains.",
        "options": [
            "0.078 A",
            "0.87 A",
            "0.087 A",
            "2.0 A",
        ],
        "correct_index": 2,
        "why": "Input power = 18 ÷ 0.90 = 20 W, so Iₚ = 20 ÷ 230 = 0.087 A.",
    },
    {
        "id": "ks4-transformers-h04",
        "subtopic_slug": "transformers",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An electric train draws power from a 25 kV overhead line. "
                "Its transformer supplies 750 V to the motors, which draw "
                "900 A. Calculate the current taken from the overhead line, "
                "assuming the transformer is 100% efficient.",
        "options": [
            "2.7 A",
            "27 A",
            "900 A",
            "30 000 A",
        ],
        "correct_index": 1,
        "why": "VₚIₚ = VₛIₛ, so Iₚ = (750 × 900) ÷ 25 000 = 27 A — the "
               "step-down of pd is a step-up of current.",
    },
]
