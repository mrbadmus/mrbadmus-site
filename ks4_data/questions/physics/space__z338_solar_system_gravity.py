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

    # ── standard, continued: a third orbit type, the ISS, the Oort cloud,
    # the ecliptic, ground-based radio astronomy, an interstellar visitor,
    # a fresh unit conversion and the Kuiper Belt ──────────────────────────
    {
        "id": "ks4-solar-system-gravity-s19",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why GPS navigation satellites orbit at an altitude "
                "of roughly 20 000 km, between the low orbits used for "
                "imaging and the geostationary orbit used for "
                "television.",
        "options": [
            "That altitude lets a receiver on the ground see several "
            "satellites of a whole network at once, while each "
            "satellite still orbits fast enough to cover the globe "
            "within hours",
            "20 000 km is simply the lowest altitude at which a "
            "satellite can carry a working GPS receiver on board "
            "without it overheating",
            "20 000 km is the one and only altitude in the whole of "
            "near-Earth space at which the Earth's gravity happens to "
            "be weak enough for a satellite of a GPS network's typical "
            "mass to remain safely in orbit at all",
            "GPS satellites orbit there because it is exactly halfway "
            "between low Earth orbit and geostationary orbit, which "
            "keeps the delay equal for every user",
        ],
        "correct_index": 0,
        "why": "A medium orbit balances two needs: it is high enough "
               "that many satellites are visible from any point on "
               "Earth at once, and low enough that each completes an "
               "orbit every few hours rather than staying fixed above "
               "one spot.",
    },
    {
        "id": "ks4-solar-system-gravity-s20",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The International Space Station orbits at a low altitude "
                "with a period of about 90 minutes. Calculate roughly "
                "how many complete orbits it makes in 24 hours.",
        "options": [
            "8",
            "16",
            "24",
            "48",
        ],
        "correct_index": 1,
        "why": "24 hours is 1440 minutes, and 1440 ÷ 90 = 16 orbits.",
    },
    {
        "id": "ks4-solar-system-gravity-s21",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why astronomers believe there is a vast, thinly "
                "populated cloud of icy bodies — the Oort cloud — "
                "surrounding the Solar System far beyond Neptune.",
        "options": [
            "Space telescopes such as Hubble and James Webb have already "
            "photographed the whole cloud directly, showing millions of "
            "individual icy bodies scattered clearly across a single "
            "wide-field image",
            "Every dwarf planet discovered so far has come from that "
            "region, and none has ever been found any closer to the "
            "Sun",
            "It is inferred from the orbits of long-period comets, "
            "which arrive from every direction and take thousands of "
            "years to return, suggesting a spherical reservoir around "
            "the whole system",
            "It was detected because its combined gravity is strong "
            "enough to measurably slow the outer planets in their "
            "orbits",
        ],
        "correct_index": 2,
        "why": "No object that far out can be seen directly with "
               "current telescopes; the Oort cloud's existence is "
               "inferred from the paths that long-period comets are "
               "observed to take.",
    },
    {
        "id": "ks4-solar-system-gravity-s22",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the eight planets are usually shown lying on "
                "roughly the same flat plane as they orbit the Sun, "
                "rather than at random angles to one another.",
        "options": [
            "Each planet's own gravity has gradually pulled every "
            "other planet's orbit into line with its own, levelling "
            "the whole system out over billions of years since it "
            "first formed",
            "The Sun's magnetic field constrains every charged particle "
            "in the Solar System to travel within one flat plane",
            "Telescopes can only usefully observe one plane at a time, "
            "so planets outside it are simply left off most diagrams",
            "The planets formed from the same flattened, spinning disc "
            "of gas and dust that surrounded the young Sun, so their "
            "orbits still largely share that disc's plane",
        ],
        "correct_index": 3,
        "why": "The Solar System formed from a single rotating disc, "
               "and the planets that condensed within it inherited "
               "orbits close to that disc's plane.",
    },
    {
        "id": "ks4-solar-system-gravity-s23",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a large radio telescope, unlike a telescope "
                "observing visible light or infrared, can usefully be "
                "built on the ground rather than launched into space.",
        "options": [
            "Radio waves from space pass through the Earth's "
            "atmosphere largely unaffected, so a ground-based dish can "
            "still collect them clearly",
            "Radio telescopes are far too heavy to be launched into "
            "orbit by any rocket currently available anywhere",
            "Radio waves are blocked completely by the atmosphere, so a "
            "ground-based telescope has to be built underground to "
            "detect them at all",
            "Radio astronomy does not depend on collecting radiation "
            "at all, so no telescope of any kind is actually needed "
            "for it",
        ],
        "correct_index": 0,
        "why": "The atmosphere is largely transparent to radio waves, "
               "unlike to much of the infrared and to X-rays, so a "
               "radio telescope loses little by staying on the ground.",
    },
    {
        "id": "ks4-solar-system-gravity-s24",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object from outside the Solar System passes close to "
                "the Sun on a path that will carry it back out into "
                "interstellar space, never to return. Explain what "
                "this tells you about its speed relative to the Sun's "
                "gravity.",
        "options": [
            "Its speed must be exactly zero relative to the Sun at the "
            "single moment of closest approach, and it is that "
            "momentary stillness which is what then lets it escape "
            "afterwards",
            "Its speed is great enough that the Sun's gravity can bend "
            "its path but not enough to pull it into a closed orbit, "
            "so it escapes rather than returning",
            "The Sun's gravity has no effect on it at all, because the "
            "object formed outside the Solar System entirely",
            "The object must be travelling slower than every planet in "
            "the Solar System, since only a slow object could have "
            "arrived from outside it",
        ],
        "correct_index": 1,
        "why": "A body bound in orbit is pulled back again and again; "
               "one that escapes was moving fast enough that gravity "
               "could deflect its path but never capture it.",
    },
    {
        "id": "ks4-solar-system-gravity-s25",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A star is measured to be 8.6 light-years from Earth. "
                "Taking one light-year as 9.46 × 10¹⁵ m and one "
                "astronomical unit as 1.5 × 10¹¹ m, determine roughly "
                "how many astronomical units away the star is.",
        "options": [
            "5.4 × 10³ AU",
            "8.6 × 10⁴ AU",
            "5.4 × 10⁵ AU",
            "5.4 × 10⁷ AU",
        ],
        "correct_index": 2,
        "why": "8.6 × 9.46 × 10¹⁵ ≈ 8.1 × 10¹⁶ m, and dividing by "
               "1.5 × 10¹¹ m gives roughly 5.4 × 10⁵ AU.",
    },
    {
        "id": "ks4-solar-system-gravity-s26",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain what the Kuiper Belt is, and how it differs from "
                "the asteroid belt.",
        "options": [
            "It is a ring of rocky debris between Mars and Jupiter, "
            "identical to the asteroid belt but discovered more "
            "recently by astronomers",
            "It is the cloud of gas and dust from which the Sun itself "
            "first formed, lying far closer in than any of the eight "
            "planets",
            "It is the name given to the rings of Saturn, made of icy "
            "fragments rather than the rock that makes up the asteroid "
            "belt",
            "It is a region of icy bodies, including Pluto, orbiting "
            "beyond Neptune — far further out and far colder than the "
            "rocky asteroid belt",
        ],
        "correct_index": 3,
        "why": "The Kuiper Belt is a distinct, distant region of icy "
               "bodies beyond Neptune, quite unlike the much closer, "
               "rocky asteroid belt.",
    },

    # ── harder, continued: an MEO orbital-radius calculation, the
    # telescope-in-space claim tested, the Oort cloud's scale, a parsec
    # conversion, an interstellar visitor, a real probe compared, ISS
    # speed and the LEO-versus-GEO synthesis ────────────────────────────
    {
        "id": "ks4-solar-system-gravity-h19",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A GPS satellite orbits at an altitude of 20 200 km above "
                "the Earth's surface. Taking the Earth's radius as "
                "6400 km, determine the radius of the satellite's "
                "orbit measured from the centre of the Earth.",
        "options": [
            "26 600 km",
            "20 200 km",
            "13 800 km",
            "33 000 km",
        ],
        "correct_index": 0,
        "why": "Orbital radius is altitude plus the Earth's radius: "
               "20 200 + 6400 = 26 600 km.",
    },
    {
        "id": "ks4-solar-system-gravity-h20",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that every kind of astronomical "
                "telescope works better if it is launched into space "
                "rather than built on the ground.",
        "options": [
            "The claim is sound, because the vacuum of space always "
            "improves the sharpness of any image, whatever wavelength "
            "is being observed",
            "The claim is unsound: a radio telescope loses little by "
            "staying on the ground, since the atmosphere barely "
            "absorbs radio waves, while space chiefly benefits "
            "telescopes working in wavelengths the atmosphere blocks",
            "The claim is sound, because ground-based telescopes can "
            "never physically be built larger than a few metres across "
            "anywhere on Earth, while a telescope launched into space "
            "faces no such size limit on the mirror it carries at all",
            "The claim is unsound, because no telescope of any kind "
            "performs any better in space than the equivalent "
            "instrument does on the ground",
        ],
        "correct_index": 1,
        "why": "The advantage of space depends on the wavelength: it "
               "matters enormously for infrared and X-rays, which the "
               "atmosphere absorbs, but far less for radio, which "
               "passes through largely unaffected.",
    },
    {
        "id": "ks4-solar-system-gravity-h21",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A short-period comet returns every 76 years and is "
                "thought to originate from the Kuiper Belt. A "
                "long-period comet has an orbital period of 4 million "
                "years. Explain what the size of the second period "
                "suggests about where that comet came from.",
        "options": [
            "It suggests the comet came from just beyond Neptune, the "
            "same region as the short-period comet, but on a "
            "slower-moving orbit",
            "It suggests the comet has been gradually slowed down by "
            "repeated close passes near the Sun, stretching out its "
            "period over many thousands of past orbits",
            "It suggests the comet's orbit extends vastly further out "
            "than the Kuiper Belt, consistent with an origin in the "
            "much more distant Oort cloud",
            "It suggests the period has been measured incorrectly, "
            "since no comet is expected to take anywhere near that "
            "long to complete one orbit",
        ],
        "correct_index": 2,
        "why": "An orbital period that long implies an aphelion far "
               "beyond the Kuiper Belt, which is exactly the kind of "
               "extremely wide, slow orbit expected of an Oort cloud "
               "comet.",
    },
    {
        "id": "ks4-solar-system-gravity-h22",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galaxy is measured to be 2.5 million parsecs from "
                "Earth. Taking one parsec as 3.26 light-years and one "
                "light-year as 9.46 × 10¹⁵ m, determine roughly its "
                "distance in metres.",
        "options": [
            "7.7 × 10²¹ m",
            "2.5 × 10²² m",
            "3.1 × 10²² m",
            "7.7 × 10²² m",
        ],
        "correct_index": 3,
        "why": "2.5 × 10⁶ × 3.26 ≈ 8.15 × 10⁶ light-years, and "
               "8.15 × 10⁶ × 9.46 × 10¹⁵ ≈ 7.7 × 10²² m.",
    },
    {
        "id": "ks4-solar-system-gravity-h23",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A newspaper reports that an interstellar object passing "
                "through the Solar System 'proves the Sun's gravity "
                "has grown weaker than before'. Evaluate this claim.",
        "options": [
            "The claim is unsound: the object's escape has nothing to "
            "do with a change in the Sun's gravity, and everything to "
            "do with the object arriving too fast to be captured into "
            "orbit",
            "The claim is sound, because only a gravitational field "
            "that had genuinely weakened over time would ever allow any "
            "object to leave the Solar System once it had already "
            "entered it",
            "The claim is sound, but only for objects heavier than a "
            "typical comet, since the Sun's gravity has weakened just "
            "enough to release large bodies",
            "The claim is unsound, because interstellar objects are "
            "not affected by the Sun's gravity at all as they pass "
            "through the Solar System",
        ],
        "correct_index": 0,
        "why": "An object on a hyperbolic path was always going to "
               "escape, at any strength of the Sun's gravity — its "
               "speed on arrival, not a change in gravity, decides "
               "that.",
    },
    {
        "id": "ks4-solar-system-gravity-h24",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "New Horizons reached Pluto, at about 33 AU, roughly nine "
                "years after launch. An earlier probe reached Mars, at "
                "about 1.5 AU, in around seven months. Using only the "
                "distances, explain why the difference in journey time "
                "is so much larger than the difference in distance "
                "alone would suggest.",
        "options": [
            "Pluto is constantly moving further away from the Sun "
            "during the whole nine-year journey, which adds a great "
            "deal of extra distance beyond the original 33 AU that the "
            "probe then has to make up along the way",
            "Distance is only part of the story: reaching a far world "
            "at a useful speed and arrival trajectory takes a "
            "carefully planned, often slower path rather than a "
            "straight line at constant speed",
            "The Mars probe used a completely different type of engine "
            "from the Pluto probe, which explains the whole of the "
            "difference in journey time",
            "The 33 AU distance to Pluto was measured incorrectly, and "
            "the true distance is over twenty times what is usually "
            "quoted for it",
        ],
        "correct_index": 1,
        "why": "Interplanetary missions do not fly in a straight line "
               "at one constant speed; the actual trajectory, gravity "
               "assists and arrival requirements all lengthen the real "
               "journey well beyond what distance alone implies.",
    },
    {
        "id": "ks4-solar-system-gravity-h25",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The International Space Station orbits at a radius of "
                "about 6800 km from the centre of the Earth, "
                "completing one orbit every 90 minutes. Taking the "
                "orbit as a circle, estimate its orbital speed in "
                "kilometres per hour.",
        "options": [
            "1500 km/h",
            "7100 km/h",
            "28 500 km/h",
            "45 200 km/h",
        ],
        "correct_index": 2,
        "why": "Circumference is 2π × 6800 ≈ 42 700 km, covered in "
               "90 minutes = 1.5 hours, giving 42 700 ÷ 1.5 ≈ "
               "28 500 km/h.",
    },
    {
        "id": "ks4-solar-system-gravity-h26",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A company plans a satellite internet constellation, "
                "giving fast, low-delay connections worldwide, and is "
                "choosing between geostationary orbit and a low Earth "
                "orbit for its satellites. Evaluate which is the "
                "better choice for this purpose.",
        "options": [
            "Geostationary orbit is better, because a single satellite "
            "stationed there can already cover almost half of the "
            "Earth's surface at once, so the whole network would need "
            "far fewer satellites overall to run",
            "Geostationary orbit is better, because its huge altitude "
            "gives it by far the lowest possible signal delay of any "
            "orbit available",
            "Low Earth orbit is better only because satellites are "
            "cheaper to build at that altitude, not because of any "
            "advantage in how the service performs",
            "Low Earth orbit is better for low delay, because the much "
            "shorter distance to each satellite cuts the signal's "
            "travel time, even though many more satellites are needed "
            "for constant coverage",
        ],
        "correct_index": 3,
        "why": "Distance drives delay directly, and a low orbit's far "
               "shorter path more than makes up for needing a larger "
               "constellation to keep coverage continuous as the "
               "satellites move overhead.",
    },
]
