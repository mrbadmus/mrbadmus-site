"""Physics · Space physics — the MRB-335 extension.

Space is Triple-only in its entirety, so it has no Combined cells at all —
`generate_site_v5.PATHWAY_TOPIC_MAP` omits the topic from the Combined tree
and RISKS C7 says the backend must too. Both TRIPLE cells were short on the
7 Sep table: Foundation at 36 and Higher at 48.

Three of the five subtopics are `tier='foundation'` — `solar-system-gravity`,
`stellar-evolution` and `red-shift-big-bang` — and only those three can feed
the Triple Foundation cell, so all twenty-four rows land there, eight each.
Triple Higher gains the sixteen `standard` and `harder` ones among them.

⚠️ `docs/ks4/pool-authoring.md` §2 records `stellar-evolution` as a subtopic
whose lesson page prints its whole examinable core as a matching block — one
life cycle, already paired. These eight work around that where they can: the
force that starts a protostar contracting, the balance that holds a main
sequence star steady, where the elements heavier than iron came from, and
why the Sun in particular will never go supernova.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── solar-system-gravity ──────── TRIPLE, foundation (6.8.1.1) ── +8 ──
    {
        "id": "ks4-solar-system-gravity-e05",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the solar system is made up of.",
        "options": [
            "The Sun and the eight planets, and nothing else",
            "The Milky Way galaxy and every one of the stars inside it",
            "The Sun, the planets and their moons, dwarf planets, asteroids "
            "and comets",
            "The Sun, the planets and the nearest few stars",
        ],
        "correct_index": 2,
        "why": "The solar system is everything held in orbit by the Sun's "
               "gravity, which is far more than the eight planets.",
    },
    {
        "id": "ks4-solar-system-gravity-e06",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State where the asteroid belt lies.",
        "options": [
            "Between Mars and Jupiter",
            "Between the Earth and Mars",
            "Beyond the orbit of Neptune",
            "Between the Sun and Mercury",
        ],
        "correct_index": 0,
        "why": "The asteroid belt sits between the rocky inner planets and "
               "the gas giants, orbiting the Sun between Mars and Jupiter.",
    },
    {
        "id": "ks4-solar-system-gravity-e07",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by an artificial satellite.",
        "options": [
            "A moon that orbits a planet naturally",
            "An object placed in orbit by people, such as a communications "
            "satellite",
            "A comet that returns to the inner solar system every few years",
            "A star that appears to move slowly across the night sky",
        ],
        "correct_index": 1,
        "why": "Artificial means made and placed there by people, as opposed "
               "to a natural satellite such as a moon.",
    },
    {
        "id": "ks4-solar-system-gravity-e08",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the shape of a planet's orbit around the Sun.",
        "options": [
            "A perfect circle",
            "A long, thin ellipse",
            "A slightly elliptical path, close to a circle",
            "A straight line that curves only at each end",
        ],
        "correct_index": 2,
        "why": "Planetary orbits are ellipses, but only slightly so — much "
               "closer to circles than a comet's stretched path.",
    },
    {
        "id": "ks4-solar-system-gravity-s05",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a satellite in a circular orbit is accelerating "
                "even though its speed never changes.",
        "options": [
            "Its direction is changing constantly, and a change of "
            "direction is a change of velocity",
            "Its speed really is increasing, but far too slowly for anyone "
            "to notice",
            "Gravity pushes it forwards along its path all the way round",
            "It is not accelerating — acceleration only means speeding up",
        ],
        "correct_index": 0,
        "why": "Velocity has a direction as well as a size, so turning "
               "constantly is accelerating even at a steady speed.",
    },
    {
        "id": "ks4-solar-system-gravity-s06",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A geostationary satellite stays above the same point on the "
                "equator. State its orbital period and explain why that "
                "value is needed.",
        "options": [
            "1 hour, so that it passes over each point many times a day",
            "12 hours, so that it appears above the point twice each day",
            "365 days, so that it matches the Earth's orbit around the Sun",
            "24 hours, so that it completes one orbit in the time the Earth "
            "turns once",
        ],
        "correct_index": 3,
        "why": "Only a 24-hour orbit keeps pace with the spinning Earth, so "
               "the satellite stays above the same longitude.",
    },
    {
        "id": "ks4-solar-system-gravity-h05",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Satellite A orbits at 400 km above the Earth and satellite "
                "B at 36 000 km. Compare their orbital speeds and periods, "
                "with reasons.",
        "options": [
            "B is faster and has the shorter period, because it has further "
            "to fall towards the Earth",
            "A is faster and has the shorter period, because gravity is "
            "stronger closer in and its path is shorter",
            "They travel at the same speed but have different periods",
            "A is faster but has the longer period, because it has more "
            "distance to cover",
        ],
        "correct_index": 1,
        "why": "A smaller orbit needs a greater speed to balance the "
               "stronger gravity there, and it is a shorter path, so the "
               "period is shorter for both reasons.",
    },
    {
        "id": "ks4-solar-system-gravity-h06",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a satellite must be given a particular speed "
                "for the orbit radius it is meant to keep, and predict what "
                "happens if it is launched too slowly.",
        "options": [
            "Any launch speed will do, because gravity adjusts itself to "
            "suit the orbit chosen",
            "Too slow and it stays motionless above one point on the ground",
            "Gravity gives exactly the force needed to curve its path at "
            "that radius; too slow and it spirals in",
            "Too slow and it flies off away from the Earth into space",
        ],
        "correct_index": 2,
        "why": "Orbit is a balance: at each radius there is one speed for "
               "which gravity bends the path into a circle, and too little "
               "speed lets gravity pull it down.",
    },

    # ── stellar-evolution ─────────── TRIPLE, foundation (6.8.1.3) ── +8 ──
    {
        "id": "ks4-stellar-evolution-e05",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the force that pulls a nebula together so that a star "
                "can begin to form.",
        "options": [
            "Magnetism",
            "Friction",
            "Electrostatic attraction",
            "Gravity",
        ],
        "correct_index": 3,
        "why": "Gravity acting on the gas and dust is what draws a nebula "
               "inwards and starts the whole process off.",
    },
    {
        "id": "ks4-stellar-evolution-e06",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a protostar is.",
        "options": [
            "A contracting cloud of gas and dust in which fusion has not yet "
            "begun",
            "A star that has just run out of hydrogen in its core",
            "The dense remnant left behind after a supernova",
            "A very small planet orbiting a newly formed star",
        ],
        "correct_index": 0,
        "why": "A protostar is the stage between the nebula and the main "
               "sequence: it is heating up under gravity but is not yet "
               "fusing.",
    },
    {
        "id": "ks4-stellar-evolution-e07",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the explosion that ends the life of a star far more "
                "massive than the Sun.",
        "options": [
            "A planetary nebula",
            "A supernova",
            "A solar flare",
            "A red giant",
        ],
        "correct_index": 1,
        "why": "A supernova is the collapse and explosion of a massive "
               "star's core once it can no longer fuse to release energy.",
    },
    {
        "id": "ks4-stellar-evolution-e08",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the element a star is made mostly of while it is on "
                "the main sequence.",
        "options": [
            "Iron",
            "Carbon",
            "Hydrogen",
            "Helium",
        ],
        "correct_index": 2,
        "why": "A main sequence star is mostly hydrogen, and fusing that "
               "hydrogen into helium is what keeps it shining.",
    },
    {
        "id": "ks4-stellar-evolution-s05",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a main sequence star stays the same size for "
                "billions of years.",
        "options": [
            "Gravity has no effect on a star once it has finished forming",
            "The outward pressure from fusion in the core exactly balances "
            "the inward pull of gravity",
            "There is nothing outside the star that could push it inwards",
            "The star's outer layers have cooled and frozen into a solid "
            "outer shell",
        ],
        "correct_index": 1,
        "why": "The main sequence IS that balance, and a star leaves it as "
               "soon as the fusion that provides the outward pressure "
               "falters.",
    },
    {
        "id": "ks4-stellar-evolution-s06",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain where the elements heavier than iron in the Earth's "
                "rocks came from.",
        "options": [
            "They were made by fusion in the core of the Sun",
            "They formed inside the Earth's core once the planet had cooled",
            "They have existed unchanged since the Big Bang",
            "They were made in the enormous energies of a supernova and "
            "scattered into space",
        ],
        "correct_index": 3,
        "why": "Fusion in a star stops at iron, so anything heavier had to "
               "be made in a supernova and then spread out to form new "
               "planets.",
    },
    {
        "id": "ks4-stellar-evolution-h05",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two stars form from the same nebula: one is twice the mass "
                "of the Sun and one is twenty times. Predict how their final "
                "remnants differ, and explain.",
        "options": [
            "Both end as white dwarfs, because the remnant does not depend "
            "on the mass",
            "The lighter one leaves a black hole, because it collapses "
            "fastest",
            "The lighter ends as a white dwarf; the heavier explodes and "
            "leaves a neutron star or black hole",
            "Both explode as supernovae, but only the heavier one leaves a "
            "remnant behind",
        ],
        "correct_index": 2,
        "why": "Mass decides the ending: a Sun-like star swells and sheds "
               "its layers, while a far more massive one collapses and "
               "explodes.",
    },
    {
        "id": "ks4-stellar-evolution-h06",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Sun will never become a supernova.",
        "options": [
            "Its mass is far too small for the core to collapse violently "
            "once fusion stops",
            "It has already used up all of its hydrogen",
            "It is too far from other stars for one to trigger it",
            "Supernovae only happen to stars that formed long after the Sun "
            "did",
        ],
        "correct_index": 0,
        "why": "A supernova needs the crushing gravity of a very massive "
               "core; the Sun will simply swell, shed its outer layers and "
               "leave a white dwarf.",
    },

    # ── red-shift-big-bang ────────── TRIPLE, foundation (6.8.2.1) ── +8 ──
    {
        "id": "ks4-red-shift-big-bang-e05",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the cosmic microwave background radiation is "
                "evidence for.",
        "options": [
            "The existence of dark matter",
            "The Big Bang",
            "The formation of the solar system",
            "The fusion of hydrogen inside stars",
        ],
        "correct_index": 1,
        "why": "It is the cooled remains of radiation from a time when the "
               "whole universe was hot and dense, which only the Big Bang "
               "theory predicts.",
    },
    {
        "id": "ks4-red-shift-big-bang-e06",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the observed wavelength of light from "
                "a galaxy that is moving away from Earth.",
        "options": [
            "It increases",
            "It decreases",
            "It stays exactly the same",
            "It falls to zero",
        ],
        "correct_index": 0,
        "why": "Recession stretches the light, which is why the wavelength "
               "grows and the light shifts towards the red end.",
    },
    {
        "id": "ks4-red-shift-big-bang-e07",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the red-shift of distant galaxies shows about "
                "the universe.",
        "options": [
            "It is contracting",
            "It is unchanging",
            "It is expanding",
            "It is rotating around the Earth",
        ],
        "correct_index": 2,
        "why": "Almost every galaxy is receding, and the further away it is "
               "the faster it goes, which is what an expanding universe "
               "looks like.",
    },
    {
        "id": "ks4-red-shift-big-bang-e08",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what blue-shift tells you about the motion of a "
                "source of light.",
        "options": [
            "The source is moving away from the observer",
            "The source is not moving at all",
            "The source is getting hotter",
            "The source is moving towards the observer",
        ],
        "correct_index": 3,
        "why": "Approaching motion squeezes the light, shortening its "
               "wavelength towards the blue end of the spectrum.",
    },
    {
        "id": "ks4-red-shift-big-bang-s05",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how the red-shift of distant galaxies supports the "
                "idea that the universe began in a hot, dense state.",
        "options": [
            "If everything is moving apart now, then in the past everything "
            "must have been much closer together",
            "Because red light carries less energy than blue light does, so "
            "it travels further",
            "Because galaxies must cool down as they grow older",
            "Because the light has taken billions of years to reach us",
        ],
        "correct_index": 0,
        "why": "Running the observed expansion backwards in time packs "
               "everything into a very small, very hot volume — which is the "
               "Big Bang.",
    },
    {
        "id": "ks4-red-shift-big-bang-s06",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cosmic microwave background is detected in every "
                "direction at almost exactly the same intensity. Explain "
                "what this shows.",
        "options": [
            "The Earth must lie at the exact centre of the universe",
            "The radiation comes from the Sun and is reflected back to us "
            "by interstellar dust",
            "It shows that the universe has stopped expanding",
            "The radiation fills the whole universe and dates from a time "
            "when all of it was hot",
        ],
        "correct_index": 3,
        "why": "A glow that is the same in every direction cannot have a "
               "single source — it has to be something the whole universe "
               "did at once.",
    },
    {
        "id": "ks4-red-shift-big-bang-h05",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galaxy is 300 Mpc from Earth and the Hubble constant is "
                "70 km/s/Mpc. Calculate its recession speed and state "
                "whether its light is red-shifted or blue-shifted.",
        "options": [
            "21 000 km/s, and its light is red-shifted",
            "21 000 km/s, and its light is blue-shifted",
            "4.3 km/s, and its light is red-shifted",
            "370 km/s, and its light is red-shifted",
        ],
        "correct_index": 0,
        "why": "v = H₀d = 70 × 300 = 21 000 km/s, and a galaxy receding at "
               "that speed has its light stretched towards the red.",
    },
    {
        "id": "ks4-red-shift-big-bang-h06",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Scientists once favoured the Steady State theory over the "
                "Big Bang. Explain what changed their minds, and why that is "
                "how science is meant to work.",
        "options": [
            "The Big Bang became more popular with the public, and science "
            "follows popular opinion",
            "The Steady State theory was never taken seriously by anyone",
            "Red-shift was discovered, which neither theory had predicted "
            "beforehand",
            "The cosmic microwave background was found — predicted by the "
            "Big Bang, not by the Steady State",
        ],
        "correct_index": 3,
        "why": "Two theories both explained the red-shift, and the one that "
               "made a prediction which then turned out to be true is the "
               "one that survived.",
    },
]
