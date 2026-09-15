"""Physics · Space — `solar-system-gravity`, the MRB-338 expansion.

The leaf already carried the bodies of the Solar System (natural and
artificial satellites, comets, the asteroid belt, the shape of an orbit), the
geostationary altitude and period, two unit conversions, and the two
misconception rows that matter most — "satellites stay up because there is no
gravity" and "nothing pulls back on the Sun". What it did NOT carry was the
SCALE of the system: the Sun's share of the mass, what a star and a galaxy
are, the astronomical unit and the light-year as UNITS rather than as
multipliers, the parsec, and the distances and travel times that follow.

So the weight here falls on scale and on measurement. The band split is
10 / 12 / 12 because the easier band was already eight rows deep on
definitions and needed only the named facts it was missing (the Sun's mass
share, the planet order, the low-orbit altitude band, the equator), while
standard and harder had six each and could carry the reasoning and the
arithmetic — light travel time, metres to astronomical units, an orbital
radius measured from the centre of the Earth rather than from the ground, and
two real probe scenarios (Voyager's signal delay, Neptune against Mars).

⚠️ The lesson page's two printed "Test yourself" tasks — why closer planets
orbit faster, and the advantage of a geostationary orbit over a low one for
communications — are deliberately not written around here. The nearest this
file comes is h09, which asks about one comet's speed at two points of a
single orbit, and h15, which asks what the equator constraint costs a polar
research station.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-solar-system-gravity-e09",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate share of the Solar System's total mass "
                "that is held in the Sun.",
        "options": [
            "About 99.8% of it",
            "About half of it, shared between the eight planets",
            "About 10% of it",
            "About 75% of it",
        ],
        "correct_index": 0,
        "why": "The Sun holds about 99.8% of the Solar System's mass, which is "
               "why its gravitational field governs every orbit in the system.",
    },
    {
        "id": "ks4-solar-system-gravity-e10",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the Sun is.",
        "options": [
            "A cloud of glowing gas and dust left over from a much older star",
            "A ball of hot plasma releasing energy by nuclear fusion",
            "A planet so large that the heat of its own core makes its surface "
            "glow white",
            "An enormous asteroid kept hot by the solar wind",
        ],
        "correct_index": 1,
        "why": "The Sun is a star: a ball of plasma whose core fuses hydrogen "
               "into helium and releases energy as it does so.",
    },
    {
        "id": "ks4-solar-system-gravity-e11",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name a dwarf planet of the Solar System.",
        "options": [
            "Titan",
            "Europa",
            "Pluto",
            "Vesta",
        ],
        "correct_index": 2,
        "why": "Pluto and Ceres are dwarf planets — bodies that orbit the Sun "
               "but are far smaller than the eight planets.",
    },
    {
        "id": "ks4-solar-system-gravity-e12",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the altitude range within which satellites in low Earth "
                "orbit travel.",
        "options": [
            "20 km to 200 km",
            "2000 km to 20 000 km",
            "200 000 km to 2 000 000 km",
            "200 km to 2000 km",
        ],
        "correct_index": 3,
        "why": "Low Earth orbit runs from about 200 km to about 2000 km — well "
               "below the 36 000 km of a geostationary orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-e13",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which list gives the four planets nearest the Sun, in "
                "order, beginning with the nearest.",
        "options": [
            "Mercury, Earth, Venus, Mars",
            "Venus, Mercury, Mars, Earth",
            "Mercury, Venus, Mars, Earth",
            "Mercury, Venus, Earth, Mars",
        ],
        "correct_index": 3,
        "why": "The order outwards from the Sun is Mercury, Venus, Earth, Mars, "
               "and then the asteroid belt before Jupiter.",
    },
    {
        "id": "ks4-solar-system-gravity-e14",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the part of the Earth that a geostationary satellite "
                "orbits above.",
        "options": [
            "The equator",
            "The magnetic North Pole",
            "Whichever country paid for the rocket that launched it",
            "The line of longitude that passes through Greenwich in London",
        ],
        "correct_index": 0,
        "why": "A geostationary satellite can only keep pace with a point on "
               "the equator, so its orbit lies in the equatorial plane.",
    },
    {
        "id": "ks4-solar-system-gravity-e15",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a galaxy.",
        "options": [
            "A great cloud of gas and dust inside which new stars are "
            "beginning to form",
            "An enormous group of billions of stars held together by gravity",
            "A star with the planets and moons that travel around it",
            "A group of eight planets in orbit around one central star",
        ],
        "correct_index": 1,
        "why": "A galaxy is a vast collection of stars bound by gravity; our "
               "own is the Milky Way.",
    },
    {
        "id": "ks4-solar-system-gravity-e16",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what one astronomical unit is equal to.",
        "options": [
            "The distance that light travels through space in one year",
            "The distance from the Sun to Neptune",
            "The average distance from the Earth to the Sun",
            "The width of the whole Solar System",
        ],
        "correct_index": 2,
        "why": "One astronomical unit is the average Earth–Sun distance, "
               "1.5 × 10¹¹ m, and it is used for distances inside the Solar "
               "System.",
    },
    {
        "id": "ks4-solar-system-gravity-e17",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the quantity that a light-year measures.",
        "options": [
            "A time",
            "A speed",
            "An age",
            "A distance",
        ],
        "correct_index": 3,
        "why": "Despite the word 'year' in its name, a light-year is a "
               "distance: how far light travels in one year, 9.46 × 10¹⁵ m.",
    },
    {
        "id": "ks4-solar-system-gravity-e18",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate number of stars in the Milky Way.",
        "options": [
            "A few hundred billion",
            "About two thousand",
            "About eight, one for each planet",
            "About two trillion, one for each planet in the galaxy",
        ],
        "correct_index": 0,
        "why": "The Milky Way holds roughly 200–400 billion stars; about two "
               "trillion is the estimated number of galaxies, not of stars.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-solar-system-gravity-s07",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe two differences between a star and a planet.",
        "options": [
            "A star is made of rock while a planet is made of gas, and a star "
            "is the hotter of the two",
            "A star gives out its own light and releases energy by fusion; a "
            "planet does neither",
            "A star is much larger than a planet, and a star needs a telescope "
            "to be seen",
            "A star is held in orbit by gravity while a planet moves freely "
            "through space",
        ],
        "correct_index": 1,
        "why": "Fusion is the defining difference: a star generates its own "
               "energy and shines, while a planet shines only by reflecting "
               "the light of its star.",
    },
    {
        "id": "ks4-solar-system-gravity-s08",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Sun is 1.5 × 10¹¹ m from the Earth and light travels at "
                "3.0 × 10⁸ m/s. Calculate the time light takes to reach the "
                "Earth from the Sun.",
        "options": [
            "50 s",
            "5000 s",
            "500 s",
            "2000 s",
        ],
        "correct_index": 2,
        "why": "time = distance ÷ speed = 1.5 × 10¹¹ ÷ 3.0 × 10⁸ = 500 s, "
               "which is 8 minutes 20 seconds.",
    },
    {
        "id": "ks4-solar-system-gravity-s09",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Milky Way is about 100 000 light-years across. Taking one "
                "light-year as 9.46 × 10¹⁵ m, determine its diameter in "
                "metres.",
        "options": [
            "9.46 × 10¹⁷ m",
            "9.46 × 10¹⁹ m",
            "9.46 × 10²⁰ m",
            "9.46 × 10²¹ m",
        ],
        "correct_index": 2,
        "why": "100 000 is 10⁵, so 10⁵ × 9.46 × 10¹⁵ = 9.46 × 10²⁰ m.",
    },
    {
        "id": "ks4-solar-system-gravity-s10",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A space probe is 4.5 × 10¹² m from the Sun. Taking one "
                "astronomical unit as 1.5 × 10¹¹ m, determine how many "
                "astronomical units that is.",
        "options": [
            "3.0 AU",
            "30 AU",
            "300 AU",
            "0.03 AU",
        ],
        "correct_index": 1,
        "why": "4.5 × 10¹² ÷ 1.5 × 10¹¹ = 30, so the probe is 30 AU out — "
               "about as far from the Sun as Neptune.",
    },
    {
        "id": "ks4-solar-system-gravity-s11",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe whose gravitational field holds the Moon in its "
                "orbit and whose holds the Earth in its orbit.",
        "options": [
            "The Sun holds both of them, because the Sun is the nearest body "
            "to each",
            "The Moon holds the Earth, and the Earth holds the Sun in turn",
            "The Earth holds both, because the Earth lies between the two",
            "The Earth holds the Moon, and the Sun holds the Earth",
        ],
        "correct_index": 3,
        "why": "A moon is a natural satellite of its planet, so the Earth's "
               "gravity holds the Moon, while the Sun's gravity holds the "
               "Earth in orbit around it.",
    },
    {
        "id": "ks4-solar-system-gravity-s12",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a satellite in a high orbit can keep travelling "
                "for many years without using any fuel.",
        "options": [
            "There is almost no air to slow it down, and gravity never needs "
            "fuel to curve its path",
            "The solar panels it carries turn sunlight into the thrust that it "
            "needs in order to keep moving",
            "Its engines are switched off, but the momentum it was given at "
            "launch stays with it for as long as it keeps orbiting",
            "Gravity is so weak that far out that the satellite coasts with no "
            "force acting on it",
        ],
        "correct_index": 0,
        "why": "Fuel is only needed to change motion; with negligible air "
               "resistance nothing slows the satellite, and the gravitational "
               "force that curves its path costs nothing.",
    },
    {
        "id": "ks4-solar-system-gravity-s13",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare an asteroid with a comet.",
        "options": [
            "Both are icy, but an asteroid orbits a planet while a comet orbits "
            "the Sun",
            "An asteroid is rocky and orbits between Mars and Jupiter; a comet "
            "is icy and takes a stretched orbit",
            "An asteroid is icy and orbits out beyond Neptune, while a comet is "
            "a rocky body of the belt between Mars and Jupiter",
            "Both are rocky, but an asteroid takes a circular orbit while a "
            "comet has been captured by a planet",
        ],
        "correct_index": 1,
        "why": "Asteroids are rocky bodies of the belt between Mars and "
               "Jupiter; comets are icy bodies on highly elliptical orbits "
               "around the Sun.",
    },
    {
        "id": "ks4-solar-system-gravity-s14",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An astronomer wants to observe infrared radiation from a "
                "distant galaxy. State which telescope is built for that work.",
        "options": [
            "The Chandra X-ray telescope",
            "The Hubble Space Telescope",
            "The James Webb Space Telescope",
            "An optical telescope on a mountain top",
        ],
        "correct_index": 2,
        "why": "James Webb is an infrared telescope; Hubble works mainly in "
               "visible light and Chandra in X-rays.",
    },
    {
        "id": "ks4-solar-system-gravity-s15",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a satellite built to photograph the ground in fine "
                "detail is placed in low Earth orbit.",
        "options": [
            "A camera can be aimed downwards from a low orbit alone",
            "A low orbit keeps the satellite above one point, so the same place "
            "can be photographed all day long",
            "Air inside the atmosphere makes an image sharper",
            "A low orbit is much closer to the surface, so far more detail can "
            "be resolved",
        ],
        "correct_index": 3,
        "why": "At 400 km a camera is roughly ninety times closer to the ground "
               "than at 36 000 km, so much finer detail can be seen.",
    },
    {
        "id": "ks4-solar-system-gravity-s16",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Moon is described as a natural satellite while "
                "a space station is described as an artificial one.",
        "options": [
            "The Moon was not put into orbit by people, whereas the station "
            "was launched there",
            "The Moon is made of rock while the station is made of metal",
            "The Moon orbits more slowly than the station does",
            "The Moon is held in orbit by gravity while the station is held "
            "there by the thrust of its engines",
        ],
        "correct_index": 0,
        "why": "The word artificial refers to how the satellite got there: "
               "people launched the station, while nobody put the Moon in "
               "orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-s17",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Sun, rather than Jupiter, lies at the centre "
                "of the Solar System.",
        "options": [
            "The Sun is the hottest body present, and heat is what draws the "
            "planets inwards towards it",
            "Jupiter formed long after the planets nearer in had already "
            "settled into the orbits that they still keep today",
            "The Sun's mass is far greater than everything else combined, so "
            "its gravitational field dominates",
            "The Sun is the one body in the Solar System that does not move, "
            "so everything else turns about it",
        ],
        "correct_index": 2,
        "why": "Gravitational attraction grows with mass, and the Sun holds "
               "almost all the mass of the system, so every other body orbits "
               "it.",
    },
    {
        "id": "ks4-solar-system-gravity-s18",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Sun looks far brighter to us than any other "
                "star, even though many stars are larger and hotter than it.",
        "options": [
            "The Sun is enormously closer to the Earth than any other star is",
            "The Sun is the largest and hottest star there is",
            "The Sun's light reaches us directly while other starlight is "
            "scattered away",
            "The Sun lies at the centre of the Milky Way",
        ],
        "correct_index": 0,
        "why": "The Sun is 1 AU away while the next nearest star is 4.25 "
               "light-years — roughly 270 000 times further — and brightness "
               "falls off sharply with distance.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-solar-system-gravity-h07",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A radio signal is sent from the ground up to a satellite "
                "36 000 km above the Earth and straight back down again. Radio "
                "waves travel at 3.0 × 10⁸ m/s. Determine the total time for "
                "the round trip.",
        "options": [
            "0.12 s",
            "0.24 s",
            "2.4 s",
            "0.0012 s",
        ],
        "correct_index": 1,
        "why": "The signal covers 2 × 3.6 × 10⁷ = 7.2 × 10⁷ m, and 7.2 × 10⁷ ÷ "
               "3.0 × 10⁸ = 0.24 s.",
    },
    {
        "id": "ks4-solar-system-gravity-h08",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this statement: 'The Solar System comes to an end at "
                "the orbit of Neptune.'",
        "options": [
            "Correct, because Neptune is the outermost of the eight planets and "
            "the Sun's gravitational field reaches no further",
            "Correct, because beyond Neptune a body would be pulled away by "
            "the gravity of the nearest other star",
            "Wrong, because the Sun's gravity holds dwarf planets and comets "
            "in orbit far beyond Neptune",
            "Wrong, because Neptune is not in fact the outermost planet of the "
            "Solar System",
        ],
        "correct_index": 2,
        "why": "Pluto orbits beyond Neptune and comets range far further out "
               "still, and everything held by the Sun's gravity belongs to the "
               "Solar System.",
    },
    {
        "id": "ks4-solar-system-gravity-h09",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A comet moves on a highly elliptical orbit. A student says it "
                "travels fastest at the far end of its orbit, where it is "
                "furthest from the Sun. Evaluate this statement.",
        "options": [
            "Correct, because a body out there has the furthest to travel, so "
            "it has to cover the ground more quickly",
            "Correct, because the Sun's gravitational pull is weaker out there "
            "and so there is far less to hold the comet back",
            "Wrong — it travels fastest when closest to the Sun, where the "
            "gravitational pull on it is strongest",
            "Wrong — its speed is the same all the way round, because the Sun "
            "sits exactly at the centre of the orbit",
        ],
        "correct_index": 2,
        "why": "The gravitational force on the comet is largest near the Sun, "
               "so that is where it is accelerated most and moves fastest; far "
               "out it crawls.",
    },
    {
        "id": "ks4-solar-system-gravity-h10",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A satellite orbits 36 000 km above the Earth's surface, and "
                "the radius of the Earth is 6400 km. Determine the radius of "
                "the satellite's orbit, measured from the centre of the Earth.",
        "options": [
            "29 600 km",
            "36 000 km",
            "42 400 km",
            "6400 km",
        ],
        "correct_index": 2,
        "why": "Orbital radius is measured from the centre of the planet, so it "
               "is the altitude plus the Earth's radius: 36 000 + 6400 = "
               "42 400 km.",
    },
    {
        "id": "ks4-solar-system-gravity-h11",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mars orbits the Sun at about 1.5 AU and Neptune at about "
                "30 AU. Suggest why a probe sent to Neptune takes more than a "
                "decade to arrive while one sent to Mars arrives in months.",
        "options": [
            "Neptune is about twenty times further from the Sun, so the journey "
            "is very much longer",
            "Neptune is a gas giant, and a probe must slow right down to "
            "approach one",
            "A probe cannot travel faster than the planet it is chasing",
            "The Sun's gravity pulls the probe backwards for the whole journey, "
            "and that pull grows stronger with distance",
        ],
        "correct_index": 0,
        "why": "30 AU against 1.5 AU is twenty times the distance from the Sun, "
               "so the path the probe has to fly is vastly longer.",
    },
    {
        "id": "ks4-solar-system-gravity-h12",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the astronomical unit, the light-year and the parsec, "
                "and state which of the three is the largest.",
        "options": [
            "The astronomical unit",
            "The light-year",
            "They are all exactly the same size",
            "The parsec",
        ],
        "correct_index": 3,
        "why": "One parsec is 3.26 light-years, and one light-year is about "
               "63 000 astronomical units, so the parsec is much the largest.",
    },
    {
        "id": "ks4-solar-system-gravity-h13",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Astronomers find a new body that orbits the Sun beyond "
                "Neptune, is roughly spherical, and is far smaller than "
                "Mercury. Suggest how they would classify it.",
        "options": [
            "As a moon of one of the gas giants",
            "As a dwarf planet",
            "As a comet",
            "As a star",
        ],
        "correct_index": 1,
        "why": "It orbits the Sun rather than a planet, and it is far too small "
               "to rank with the eight planets — that is what a dwarf planet "
               "is.",
    },
    {
        "id": "ks4-solar-system-gravity-h14",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Moon travels once around the Earth in 27 days along a "
                "path 2.4 × 10⁹ m long. There are 86 400 s in one day. "
                "Determine the Moon's orbital speed.",
        "options": [
            "89 m/s",
            "1000 m/s",
            "2600 m/s",
            "24 000 m/s",
        ],
        "correct_index": 1,
        "why": "27 days is 27 × 86 400 = 2.33 × 10⁶ s, and 2.4 × 10⁹ ÷ "
               "2.33 × 10⁶ is about 1000 m/s.",
    },
    {
        "id": "ks4-solar-system-gravity-h15",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a geostationary satellite cannot provide a "
                "reliable television signal to a research station at the South "
                "Pole.",
        "options": [
            "It orbits above the equator, so from the pole it sits at or below "
            "the horizon",
            "Its 24-hour period means that it passes over the pole for only a "
            "few minutes each day",
            "The signal is absorbed by the very cold air above the polar ice",
            "Its orbit is so high that the signal fades away before arriving",
        ],
        "correct_index": 0,
        "why": "A geostationary orbit lies in the plane of the equator, so at "
               "extreme latitudes the satellite is never usefully above the "
               "horizon.",
    },
    {
        "id": "ks4-solar-system-gravity-h16",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Voyager 1 probe is about 160 AU from the Sun. One "
                "astronomical unit is 1.5 × 10¹¹ m and radio waves travel at "
                "3.0 × 10⁸ m/s. Determine roughly how long a radio command "
                "takes to reach it.",
        "options": [
            "22 minutes",
            "2.2 hours",
            "22 days",
            "22 hours",
        ],
        "correct_index": 3,
        "why": "160 × 1.5 × 10¹¹ = 2.4 × 10¹³ m, and 2.4 × 10¹³ ÷ 3.0 × 10⁸ = "
               "8.0 × 10⁴ s, which is about 22 hours.",
    },
    {
        "id": "ks4-solar-system-gravity-h17",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student argues that because the astronomical unit is defined "
                "using the Earth's orbit, it cannot be used to describe the "
                "orbit of Neptune. Evaluate this argument.",
        "options": [
            "Correct, because a unit may describe the body it was defined from "
            "and no other",
            "Correct, because Neptune's orbit is elliptical while the "
            "astronomical unit assumes an orbit that is a perfect circle",
            "Wrong, because the astronomical unit is a fixed length, and a "
            "fixed length can always measure any distance",
            "Wrong, because the astronomical unit is defined using the orbit of "
            "Neptune rather than that of the Earth",
        ],
        "correct_index": 2,
        "why": "Once defined, 1 AU is just the fixed length 1.5 × 10¹¹ m, and a "
               "fixed length can measure any distance — Neptune's orbit is 30 "
               "of them.",
    },
    {
        "id": "ks4-solar-system-gravity-h18",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'A dwarf planet is just a large moon.' "
                "Evaluate this statement.",
        "options": [
            "Wrong — a dwarf planet always orbits the Sun, while a moon only "
            "ever orbits a planet",
            "Correct — both are small round bodies, so the words mean the same",
            "Correct, because a dwarf planet is a moon that has broken free of "
            "the planet it once travelled around",
            "Wrong — a dwarf planet is larger than any of the eight planets",
        ],
        "correct_index": 0,
        "why": "The difference is what the body orbits: a dwarf planet goes "
               "round the Sun, while a moon is a natural satellite of a planet.",
    },
]
