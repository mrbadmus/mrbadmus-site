"""Physics · Space physics — the Solar System, orbits, stars and cosmology.

Sixty assignment questions across the five Space subtopics. Every one of them
is Triple-only (Space physics is not in AQA Combined Science 8464), so the
`triple_only` flag is True throughout; `gravity-stable-orbits` and
`dark-matter-dark-energy` are additionally Higher tier.

The distractors are built from the misconceptions the lesson pages declare:
geostationary altitudes and periods swapped with LEO ones; the Sun placed at
the exact centre of a planet's orbit; orbital speed thought to rise with
radius; a satellite "held up" by the absence of gravity; a star "burning" fuel
chemically; main-sequence lifetime read straight off mass the wrong way round;
the Sun ending as a supernova or a black hole; a white dwarf mistaken for a
small main-sequence star; a planetary nebula mistaken for planet formation;
red-shift read as galaxies flying through space away from a centre, or as dust
reddening; and dark matter and dark energy treated as the same thing.

Two authoring notes for whoever changes one of these:

* `red-shift-big-bang` is Foundation tier, so it carries ONE straight
  substitution into v = H₀d (the equation is declared in the subtopic's own
  body, not only in its Higher extension) and no rearrangement of it.
* Nothing here restates a lesson page's own "Test yourself" question. The two
  reserved stems per subtopic are listed in the brief; the closest this file
  comes is by asking for a different quantity, a different direction of
  reasoning, or a different case entirely.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── solar-system-gravity ────────────────────────────────────────────
    {
        "id": "ks4-solar-system-gravity-e01",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a natural satellite.",
        "options": [
            "A rocky body that orbits the Sun inside the asteroid belt",
            "Any object placed into orbit by a rocket launched from Earth",
            "A body such as a moon that orbits a planet and was not put "
            "there by people",
            "A star close enough to a planet to be held in its gravitational "
            "field",
        ],
        "correct_index": 2,
        "why": "Moons are natural satellites: they orbit planets, and unlike "
               "artificial satellites nobody launched them there.",
    },
    {
        "id": "ks4-solar-system-gravity-e02",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which statement describes a comet?",
        "options": [
            "An icy body that follows a highly elliptical orbit around the Sun",
            "A rocky body that orbits the Sun between Mars and Jupiter",
            "A natural satellite held in orbit around a planet",
            "A ball of plasma releasing energy by nuclear fusion",
        ],
        "correct_index": 0,
        "why": "Comets are icy bodies on long, highly elliptical orbits — the "
               "rocky bodies between Mars and Jupiter are asteroids.",
    },
    {
        "id": "ks4-solar-system-gravity-e03",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate altitude of a geostationary orbit above "
                "the Earth's surface.",
        "options": [
            "200 km",
            "400 km",
            "2000 km",
            "36 000 km",
        ],
        "correct_index": 3,
        "why": "A geostationary orbit sits at about 36 000 km — the one "
               "radius at which the orbital period is 24 hours; the smaller "
               "figures are low Earth orbit altitudes.",
    },
    {
        "id": "ks4-solar-system-gravity-e04",
        "subtopic_slug": "solar-system-gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what keeps the Moon in orbit around the Earth.",
        "options": [
            "The magnetic attraction between the Earth's core and the Moon",
            "The gravitational attraction of the Earth acting on the Moon",
            "The pressure of sunlight pushing the Moon along its orbit",
            "The Earth's atmosphere dragging the Moon around with it",
        ],
        "correct_index": 1,
        "why": "Gravity is the non-contact force that acts between all "
               "masses, and the Earth's gravity is what holds the Moon in "
               "orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-s01",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Proxima Centauri is 4.25 light-years from Earth. One "
                "light-year is 9.46 × 10¹⁵ m. Calculate this distance in "
                "metres.",
        "options": [
            "4.02 × 10¹⁶ m",
            "4.02 × 10¹⁵ m",
            "4.02 × 10¹⁷ m",
            "2.23 × 10¹⁵ m",
        ],
        "correct_index": 0,
        "why": "4.25 × 9.46 × 10¹⁵ = 4.02 × 10¹⁶ m — the number of "
               "light-years multiplies the length of one light-year.",
    },
    {
        "id": "ks4-solar-system-gravity-s02",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Sun is described as lying at one focus of a "
                "planet's orbit rather than at its exact centre.",
        "options": [
            "Planetary orbits are perfect circles, but the Sun wobbles about "
            "the centre of each one",
            "Planetary orbits are perfect circles with the Sun fixed exactly "
            "at the centre of each one",
            "Planetary orbits are spirals, because every planet is slowly "
            "falling in towards the Sun",
            "Planetary orbits are slightly elliptical, so a planet's distance "
            "from the Sun changes as it orbits",
        ],
        "correct_index": 3,
        "why": "Orbits are slightly elliptical with the Sun at one focus, so "
               "the Sun–planet distance varies through each orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-s03",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A satellite is observed to complete one orbit of the Earth "
                "every 100 minutes. Deduce what this tells you about its "
                "orbit, and give a reason.",
        "options": [
            "It is in a geostationary orbit, because it returns to the same "
            "point each time",
            "It is in a low orbit, because only a small orbital radius gives "
            "so short a period",
            "It is in a very high orbit, because a longer path takes less "
            "time to complete",
            "It has left orbit altogether, because no stable orbit has a "
            "period of less than a day",
        ],
        "correct_index": 1,
        "why": "The smaller the orbital radius the faster the satellite must "
               "travel and the shorter its period, so a period far under a "
               "day means a low orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-s04",
        "subtopic_slug": "solar-system-gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Jupiter orbits at an average distance of 5.2 AU from the "
                "Sun. One astronomical unit is 1.5 × 10¹¹ m. Calculate "
                "Jupiter's average orbital radius in metres.",
        "options": [
            "7.8 × 10¹⁰ m",
            "2.9 × 10¹⁰ m",
            "7.8 × 10¹¹ m",
            "7.8 × 10¹² m",
        ],
        "correct_index": 2,
        "why": "5.2 × 1.5 × 10¹¹ = 7.8 × 10¹¹ m — the number of AU multiplies "
               "the length of one AU.",
    },
    {
        "id": "ks4-solar-system-gravity-h01",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Satellites stay up because there is no "
                "gravity that far above the Earth.' Evaluate this statement.",
        "options": [
            "It is correct, because the Earth's gravitational field stops at "
            "the top of the atmosphere",
            "It is correct, because a satellite in a vacuum has no weight and "
            "so cannot fall",
            "It is wrong, because gravity there is far too weak to matter and "
            "the satellite simply travels in a straight line",
            "It is wrong, because gravity there is still strong and supplies "
            "the centripetal force that curves the satellite's path",
        ],
        "correct_index": 3,
        "why": "Gravity does not switch off with height — it is precisely the "
               "gravitational pull that acts as the centripetal force, "
               "bending the satellite's motion into an orbit.",
    },
    {
        "id": "ks4-solar-system-gravity-h02",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says: 'The Sun's gravity holds the planets in "
                "orbit, so nothing pulls on the Sun itself.' Evaluate this "
                "statement.",
        "options": [
            "Correct — gravitational attraction acts only from the larger "
            "body onto the smaller one",
            "Incorrect — each planet pulls back on the Sun with a force of "
            "the same size, but the Sun's huge mass means it barely moves",
            "Incorrect — the planets together pull on the Sun far harder "
            "than it pulls on them, because there are eight of them",
            "Correct — the Sun is fixed at the centre of the Solar System "
            "and cannot be moved by anything",
        ],
        "correct_index": 1,
        "why": "Gravity acts between every pair of masses and pulls equally "
               "hard on both, so the same force that curves a planet's path "
               "also acts on the Sun — it is simply far too massive to be "
               "shifted much by it.",
    },
    {
        "id": "ks4-solar-system-gravity-h03",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the diameter of the Milky Way is quoted in "
                "light-years rather than in astronomical units.",
        "options": [
            "Because the astronomical unit may only be used for distances "
            "measured inside a single galaxy",
            "Because the light-year measures a time while the astronomical "
            "unit measures a distance",
            "Because a light-year is a far larger unit, so the same distance "
            "is written as a manageable number",
            "Because light-years can be measured with a telescope while "
            "astronomical units can only be calculated",
        ],
        "correct_index": 2,
        "why": "A light-year (9.46 × 10¹⁵ m) is roughly 63 000 AU, so "
               "interstellar distances come out as sensible numbers rather "
               "than astronomically large ones.",
    },
    {
        "id": "ks4-solar-system-gravity-h04",
        "subtopic_slug": "solar-system-gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A newly discovered dwarf planet orbits the Sun at about "
                "40 AU. Neptune orbits at about 30 AU. Suggest, with a "
                "reason, how the dwarf planet's orbital period compares with "
                "Neptune's.",
        "options": [
            "Longer, because the Sun's gravity is weaker further out, so it "
            "orbits more slowly along a longer path",
            "Shorter, because objects further from the Sun are made to travel "
            "faster along their orbits",
            "The same, because every body in the Solar System completes one "
            "orbit in one Earth year",
            "Longer, because the Sun's gravity grows stronger with distance "
            "and holds the dwarf planet back",
        ],
        "correct_index": 0,
        "why": "A larger orbit means weaker gravity and therefore a lower "
               "orbital speed, and the path round is longer too — so the "
               "period is longer on both counts.",
    },

    # ── gravity-stable-orbits ───────────────────────────────────────────
    {
        "id": "ks4-gravity-stable-orbits-e01",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the direction of the centripetal force acting on a "
                "satellite in a circular orbit.",
        "options": [
            "Forwards, along the satellite's direction of travel",
            "Towards the centre of the orbit",
            "Outwards, away from the centre of the orbit",
            "Backwards, opposite to the satellite's direction of travel",
        ],
        "correct_index": 1,
        "why": "Centripetal means centre-seeking: for an orbit the force is "
               "gravity, and it always points towards the centre.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e02",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite moves round a circular orbit at a constant "
                "speed. State what is happening to its velocity.",
        "options": [
            "Its velocity is constant, because its speed is constant",
            "Its velocity is zero, because the forces acting on it are "
            "balanced",
            "Its velocity increases steadily as gravity pulls it inwards",
            "Its velocity changes continuously, because its direction is "
            "changing",
        ],
        "correct_index": 3,
        "why": "Velocity is speed in a given direction, so a body going round "
               "a circle at steady speed still has a changing velocity — and "
               "so is accelerating.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e03",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the approximate orbital speed of a satellite in low "
                "Earth orbit at about 400 km altitude.",
        "options": [
            "7700 m/s",
            "3000 m/s",
            "770 m/s",
            "11 200 m/s",
        ],
        "correct_index": 0,
        "why": "Low Earth orbit needs about 7700 m/s; 3000 m/s is the "
               "geostationary orbital speed and 11 200 m/s is the Earth's "
               "escape velocity.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e04",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by the escape velocity of a planet.",
        "options": [
            "The speed at which a satellite travels in a stable circular "
            "orbit around the planet",
            "The speed reached by a spacecraft as it re-enters the planet's "
            "atmosphere",
            "The minimum speed an object needs in order to leave the planet's "
            "gravitational field",
            "The maximum speed an object can reach before its orbit becomes "
            "unstable",
        ],
        "correct_index": 2,
        "why": "Escape velocity is the minimum launch speed at which an "
               "object can get away from a body's gravitational field "
               "altogether — about 11.2 km/s for Earth.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s01",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Predict the path a satellite in a circular orbit would "
                "follow if the Earth's gravitational pull on it suddenly "
                "vanished.",
        "options": [
            "It would spiral slowly outwards, gradually leaving the Earth "
            "behind",
            "It would carry on circling, because it is already moving in a "
            "circle",
            "It would travel in a straight line, along the direction it "
            "happened to be moving at that instant",
            "It would stop moving, because there would be no force left to "
            "keep it going",
        ],
        "correct_index": 2,
        "why": "A body keeps moving in a straight line at a steady speed "
               "unless a resultant force acts on it, and gravity is the only "
               "force curving the satellite's path.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s02",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why there is only one possible altitude for a "
                "geostationary orbit.",
        "options": [
            "Only at that radius does the orbital speed set by gravity give a "
            "period of exactly 24 hours",
            "Only at that radius is the Earth's gravitational field strength "
            "zero, so a satellite stays put",
            "Only at that radius can a satellite be placed directly above a "
            "chosen city in the UK",
            "Only at that radius is a satellite far enough out to be beyond "
            "the whole of the atmosphere",
        ],
        "correct_index": 0,
        "why": "Each orbital radius fixes one stable speed and so one period; "
               "only at about 36 000 km does that period match the Earth's "
               "24-hour rotation.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s03",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite completes one circular orbit of radius "
                "7.0 × 10⁶ m in 5800 s. Calculate its orbital speed. Use "
                "speed = distance ÷ time, and circumference = 2πr.",
        "options": [
            "1200 m/s",
            "3800 m/s",
            "15 200 m/s",
            "7600 m/s",
        ],
        "correct_index": 3,
        "why": "The distance travelled is the circumference, 2π × 7.0 × 10⁶ = "
               "4.4 × 10⁷ m, and 4.4 × 10⁷ ÷ 5800 = 7600 m/s.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s04",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A probe must reach 11.2 km/s to leave the Earth completely. "
                "Predict what happens to a probe launched vertically at "
                "8.0 km/s, ignoring air resistance.",
        "options": [
            "It leaves the Earth, but travels away more slowly than one "
            "launched at 11.2 km/s",
            "It rises to a great height, slows to a stop and is then pulled "
            "back down by gravity",
            "It settles into a stable circular orbit at the height where it "
            "runs out of speed",
            "It stops rising and stays at that height, because gravity that "
            "far out is zero",
        ],
        "correct_index": 1,
        "why": "Below escape velocity the probe never gets clear of the "
               "gravitational field, so gravity decelerates it, stops it and "
               "brings it back.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h01",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A spacecraft is in the same circular orbit as a space "
                "station, but behind it. A student says it should fire its "
                "engines forwards to catch up. Evaluate this suggestion.",
        "options": [
            "Wrong — a forward burn lifts it into a larger, slower orbit, so "
            "it falls further behind",
            "Correct — a forward burn raises its speed at the same radius, so "
            "the gap closes steadily",
            "Wrong — a forward burn changes nothing, because gravity "
            "immediately cancels the extra speed",
            "Correct — the extra speed lowers the orbit, and satellites in "
            "lower orbits always catch up",
        ],
        "correct_index": 0,
        "why": "Speeding up at a given radius raises the orbit, and the "
               "stable speed in the higher orbit is lower — so the "
               "spacecraft ends up trailing further behind.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h02",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why gravity does no work on a satellite that is in a "
                "circular orbit, even though the satellite is moving.",
        "options": [
            "Because gravity is a non-contact force, and non-contact forces "
            "never transfer any energy",
            "Because gravity at that altitude is far too weak to transfer any "
            "measurable amount of energy at all",
            "Because gravity acts at right angles to the motion, so nothing moves "
            "in the direction of the force",
            "Because the satellite's kinetic energy rises by exactly the "
            "amount that gravity supplies to it",
        ],
        "correct_index": 2,
        "why": "Work done = force × distance moved in the direction of the "
               "force, and in a circular orbit the gravitational pull is "
               "always perpendicular to the velocity.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h03",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "The International Space Station travels at 7700 m/s in a "
                "circular orbit of radius 6.8 × 10⁶ m. Determine its orbital "
                "period. Use time = distance ÷ speed, and circumference "
                "= 2πr.",
        "options": [
            "883 s",
            "5550 s",
            "2770 s",
            "11 100 s",
        ],
        "correct_index": 1,
        "why": "One orbit is 2π × 6.8 × 10⁶ = 4.27 × 10⁷ m, and "
               "4.27 × 10⁷ ÷ 7700 = 5550 s, which is about 92 minutes.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h04",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain, in terms of escape velocity, why no light can leave "
                "a black hole.",
        "options": [
            "Light has no mass, so gravity cannot act on it, and it is "
            "trapped instead by a magnetic field",
            "The black hole absorbs the light and re-emits it as heat, so "
            "none of it leaves as visible light",
            "The black hole spins so fast that light is dragged round with it "
            "and never reaches the outside",
            "The escape velocity there is greater than the speed of light, "
            "and nothing can travel faster than light",
        ],
        "correct_index": 3,
        "why": "A black hole is so dense that its escape velocity exceeds "
               "3 × 10⁸ m/s, so not even light is fast enough to get out.",
    },

    # ── stellar-evolution ───────────────────────────────────────────────
    {
        "id": "ks4-stellar-evolution-e01",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the cloud of gas and dust from which all stars begin to "
                "form.",
        "options": [
            "A white dwarf",
            "A protostar",
            "A planetary nebula",
            "A nebula",
        ],
        "correct_index": 3,
        "why": "Stars form from nebulae — clouds of hydrogen gas and dust; a "
               "protostar is the next stage, once gravity has begun to pull "
               "the cloud together.",
    },
    {
        "id": "ks4-stellar-evolution-e02",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the nuclear reaction that supplies the energy of a "
                "main sequence star.",
        "options": [
            "The chemical burning of hydrogen gas in oxygen",
            "The fusion of hydrogen nuclei to form helium nuclei",
            "The fission of heavy nuclei such as uranium into lighter nuclei",
            "The radioactive decay of carbon nuclei inside the core",
        ],
        "correct_index": 1,
        "why": "Main sequence stars fuse hydrogen nuclei into helium — a "
               "nuclear process, not chemical burning, which is why no oxygen "
               "is needed.",
    },
    {
        "id": "ks4-stellar-evolution-e03",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the final remnant left by a star of about the same "
                "mass as the Sun.",
        "options": [
            "A supernova",
            "A neutron star",
            "A white dwarf",
            "A black hole",
        ],
        "correct_index": 2,
        "why": "A Sun-sized star ends as a white dwarf — the hot, dense core "
               "left after the outer layers drift away as a planetary nebula.",
    },
    {
        "id": "ks4-stellar-evolution-e04",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a planetary nebula is.",
        "options": [
            "A shell of glowing gas thrown off by a dying star of about the "
            "Sun's mass",
            "The cloud of dust and rock from which planets form around a "
            "young star",
            "A ring of planets left in orbit after their star has collapsed "
            "inwards",
            "The expanding cloud of gas produced when a massive star explodes "
            "as a supernova",
        ],
        "correct_index": 0,
        "why": "Despite the name, a planetary nebula has nothing to do with "
               "planets — it is the outer layers a dying Sun-like star sheds "
               "before becoming a white dwarf.",
    },
    {
        "id": "ks4-stellar-evolution-s01",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens to a star of about the Sun's mass when "
                "the hydrogen in its core runs out.",
        "options": [
            "It collapses straight into a white dwarf, with no further change "
            "in its size",
            "Its core contracts while its outer layers expand and cool, so it "
            "becomes a red giant",
            "It explodes at once as a supernova, scattering all of its "
            "material into space",
            "It stops shining immediately, because no fuel of any kind is "
            "left inside it",
        ],
        "correct_index": 1,
        "why": "With core hydrogen gone the core contracts and heats, fusion "
               "moves to a shell around it, and the outer layers swell and "
               "cool — a red giant.",
    },
    {
        "id": "ks4-stellar-evolution-s02",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a star far more massive than the Sun spends much "
                "less time on the main sequence, even though it starts with "
                "more hydrogen.",
        "options": [
            "Its stronger gravity pulls hydrogen away from the core, so less "
            "fuel is available there",
            "Its larger surface area lets heat escape more quickly, so the "
            "core cools and fusion stops",
            "Its greater mass squeezes the core to a much higher temperature, "
            "so it fuses hydrogen far faster",
            "Its greater mass makes it fuse helium instead of hydrogen, and "
            "helium releases less energy",
        ],
        "correct_index": 2,
        "why": "More mass means more gravitational compression, a hotter core "
               "and a far higher rate of fusion — so the extra fuel is used "
               "up much sooner.",
    },
    {
        "id": "ks4-stellar-evolution-s03",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why iron is the heaviest element a massive star can "
                "make by fusion in its core.",
        "options": [
            "Fusing nuclei heavier than iron absorbs energy rather than releasing "
            "it, so it cannot power a star",
            "Iron is magnetic, and its magnetic field keeps any further "
            "nuclei from joining together",
            "Iron is the heaviest element that exists, so there is nothing "
            "heavier for a star to make",
            "Iron sinks down to the very centre of the star, where the temperature "
            "is far too low for fusion",
        ],
        "correct_index": 0,
        "why": "Fusion only powers a star while it releases energy, and "
               "fusing anything heavier than iron absorbs energy instead.",
    },
    {
        "id": "ks4-stellar-evolution-s04",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which sequence correctly describes the life cycle of a star "
                "far more massive than the Sun?",
        "options": [
            "Nebula → protostar → main sequence → red giant → planetary nebula → "
            "white dwarf → black dwarf",
            "Protostar → nebula → main sequence → red supergiant → supernova "
            "→ black dwarf",
            "Nebula → main sequence → protostar → red supergiant → supernova → "
            "neutron star or black hole",
            "Nebula → protostar → main sequence → red supergiant → supernova "
            "→ neutron star or black hole",
        ],
        "correct_index": 3,
        "why": "Massive stars swell into red supergiants, explode as "
               "supernovae, and leave either a neutron star or, if the "
               "remnant core is massive enough, a black hole.",
    },
    {
        "id": "ks4-stellar-evolution-h01",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a protostar becomes hot enough to start fusion, "
                "given that no fusion is taking place in it yet.",
        "options": [
            "Friction between the dust grains inside the cloud warms it as they rub "
            "past one another",
            "Light from nearby stars is absorbed by the cloud and becomes "
            "trapped inside it",
            "Gravity pulls the cloud inwards, transferring gravitational potential "
            "energy to its thermal store",
            "Hydrogen begins to burn chemically inside the cloud, releasing heat "
            "until nuclear fusion can begin",
        ],
        "correct_index": 2,
        "why": "As the cloud collapses under its own gravity its "
               "gravitational potential energy is transferred to the thermal "
               "energy store of the gas, raising the core to ~10 million °C.",
    },
    {
        "id": "ks4-stellar-evolution-h02",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A star has ended its life as a neutron star. Deduce what "
                "this tells you about the star.",
        "options": [
            "It was far more massive than the Sun, but its supernova remnant was "
            "too light to leave a black hole",
            "It had about the same mass as the Sun, so it shed a planetary "
            "nebula and left its dense core behind",
            "It was less massive than the Sun, so its core collapsed gently without "
            "ever exploding at all",
            "It was among the very heaviest stars, because only the heaviest "
            "stars leave any remnant at all",
        ],
        "correct_index": 0,
        "why": "Only massive stars go supernova, and the remnant is a neutron "
               "star when the leftover core is dense but below the mass "
               "needed to form a black hole.",
    },
    {
        "id": "ks4-stellar-evolution-h03",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says: 'A white dwarf is just a small main sequence "
                "star.' Evaluate this statement.",
        "options": [
            "Correct — a white dwarf fuses hydrogen very slowly, which is why "
            "it is so small and faint",
            "Correct — white dwarfs and main sequence stars are both stable, "
            "so they are the same kind of object",
            "Wrong — a white dwarf is much larger than a main sequence star "
            "but has a far cooler surface",
            "Wrong — no fusion happens in a white dwarf; it is a hot, dense "
            "remnant core that is slowly cooling",
        ],
        "correct_index": 3,
        "why": "A main sequence star is stable because fusion balances "
               "gravity; a white dwarf has no fusion at all and simply cools "
               "over billions of years.",
    },
    {
        "id": "ks4-stellar-evolution-h04",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict what will happen to the Sun and the inner planets "
                "when the Sun leaves the main sequence in about 5 billion "
                "years.",
        "options": [
            "It will explode as a supernova, and the shockwave will strip "
            "away the Earth's atmosphere",
            "It will swell into a red giant that reaches the inner planets, "
            "then leave a white dwarf behind",
            "It will collapse into a black hole, and the Earth will slowly "
            "spiral inwards into it",
            "It will shrink straight into a neutron star, leaving the Earth's "
            "orbit completely unchanged",
        ],
        "correct_index": 1,
        "why": "The Sun is not massive enough to go supernova: it will expand "
               "into a red giant, shed a planetary nebula and end as a white "
               "dwarf.",
    },

    # ── red-shift-big-bang ──────────────────────────────────────────────
    {
        "id": "ks4-red-shift-big-bang-e01",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by red-shift.",
        "options": [
            "Light from a source is shifted to longer wavelengths, towards "
            "the red end of the spectrum",
            "Light from a source is shifted to shorter wavelengths, towards "
            "the red end of the spectrum",
            "A distant galaxy glows red because the stars inside it are "
            "extremely hot",
            "A distant galaxy looks red because red light travels furthest "
            "through empty space",
        ],
        "correct_index": 0,
        "why": "Red-shift is the stretching of light to longer wavelengths, "
               "which happens when the source and observer are moving apart.",
    },
    {
        "id": "ks4-red-shift-big-bang-e02",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate age of the universe.",
        "options": [
            "4.6 million years",
            "4.6 billion years",
            "13.8 billion years",
            "13.8 million years",
        ],
        "correct_index": 2,
        "why": "The universe is about 13.8 billion years old — 4.6 billion "
               "years is the age of the Solar System, which formed long "
               "afterwards.",
    },
    {
        "id": "ks4-red-shift-big-bang-e03",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the temperature of the cosmic microwave background "
                "radiation.",
        "options": [
            "0 K",
            "2.7 K",
            "273 K",
            "2700 K",
        ],
        "correct_index": 1,
        "why": "The afterglow of the hot early universe has been stretched "
               "and cooled by 13.8 billion years of expansion to just 2.7 K.",
    },
    {
        "id": "ks4-red-shift-big-bang-e04",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the proportions of hydrogen and helium, by mass, that "
                "the Big Bang theory predicts and that observations of the "
                "oldest stars confirm.",
        "options": [
            "50% hydrogen and 50% helium",
            "25% hydrogen and 75% helium",
            "95% hydrogen and 5% helium",
            "75% hydrogen and 25% helium",
        ],
        "correct_index": 3,
        "why": "Big Bang nucleosynthesis predicts about 75% hydrogen and 25% "
               "helium by mass, and that is what the oldest stars are "
               "observed to contain.",
    },
    {
        "id": "ks4-red-shift-big-bang-s01",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an astronomer in a distant galaxy would also see "
                "almost every other galaxy moving away from them.",
        "options": [
            "Because our galaxy sits at the centre of the universe, and "
            "everything moves away from that centre",
            "Because all the galaxies were thrown outwards from one explosion "
            "in space, like pieces of shrapnel",
            "Because that astronomer's galaxy would then be the true centre "
            "of the universe instead of ours",
            "Because space itself is expanding everywhere, so every galaxy "
            "moves away from every other galaxy",
        ],
        "correct_index": 3,
        "why": "It is space between the galaxies that is stretching, so the "
               "recession looks the same from every galaxy and there is no "
               "centre.",
    },
    {
        "id": "ks4-red-shift-big-bang-s02",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galaxy is 100 Mpc from Earth. The Hubble constant is "
                "70 km/s/Mpc. Calculate the galaxy's recession speed using "
                "v = H₀d.",
        "options": [
            "700 km/s",
            "7000 km/s",
            "70 000 km/s",
            "0.7 km/s",
        ],
        "correct_index": 1,
        "why": "v = H₀d = 70 × 100 = 7000 km/s — the Hubble constant "
               "multiplies the distance in Mpc.",
    },
    {
        "id": "ks4-red-shift-big-bang-s03",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the red-shift of a galaxy 1000 Mpc away with that of "
                "a galaxy 100 Mpc away, and explain the difference.",
        "options": [
            "Smaller, because its light has spread out over a greater "
            "distance and lost energy on the way",
            "The same, because red-shift depends on the type of galaxy rather "
            "than on how far away it is",
            "Greater, because the more distant galaxy is receding faster, so "
            "its light is stretched more",
            "Greater, because the more distant galaxy is older, so its stars "
            "are cooler and redder",
        ],
        "correct_index": 2,
        "why": "Hubble's law says recession speed rises with distance, and a "
               "faster recession stretches the light by a larger amount.",
    },
    {
        "id": "ks4-red-shift-big-bang-s04",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The light from the Andromeda galaxy is blue-shifted rather "
                "than red-shifted. Explain how this is possible in an "
                "expanding universe.",
        "options": [
            "Andromeda is close enough that its motion towards us outweighs "
            "the expansion, so its light is compressed",
            "Andromeda is far hotter than other galaxies, so the light it "
            "gives out is mainly blue to begin with",
            "Andromeda is the one galaxy that space is not expanding around, "
            "so its light reaches us unchanged",
            "Andromeda is so distant that its light has been stretched right "
            "past red and round to blue again",
        ],
        "correct_index": 0,
        "why": "Expansion dominates only at large distances; nearby "
               "Andromeda's own motion towards the Milky Way shortens the "
               "wavelengths we receive.",
    },
    {
        "id": "ks4-red-shift-big-bang-h01",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Red-shift shows that the galaxies are "
                "flying apart through space, away from the point where the "
                "Big Bang happened.' Explain what is wrong with this.",
        "options": [
            "Nothing is wrong — the Big Bang happened at one point, and the "
            "galaxies are still travelling away from it",
            "The Big Bang was an expansion of space itself, not an explosion "
            "at a point in space, so no such centre exists",
            "Red-shift actually shows the galaxies moving towards us, so the "
            "whole statement is the wrong way round",
            "The galaxies are not moving at all — dust between them absorbs "
            "the blue light and leaves the red",
        ],
        "correct_index": 1,
        "why": "Space itself is expanding everywhere at once, so there is no "
               "location the galaxies are flying away from.",
    },
    {
        "id": "ks4-red-shift-big-bang-h02",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Big Bang theory predicted a faint background glow in "
                "1948, and that glow was first detected in 1964. Explain why "
                "this order of events strengthens the theory.",
        "options": [
            "Because a scientific theory can only be accepted once it has stood "
            "unchallenged for fifteen years",
            "Because the detection was made by accident, and accidental "
            "results are more trustworthy",
            "Because the delay shows the glow was produced by the theory "
            "rather than by the early universe",
            "Because the theory made a testable prediction first, so the result "
            "could not be fitted to it later",
        ],
        "correct_index": 3,
        "why": "A theory that predicts something nobody has yet seen, and is "
               "then proved right, has passed a genuine test rather than "
               "merely explaining what was already known.",
    },
    {
        "id": "ks4-red-shift-big-bang-h03",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Galaxy P shows twice as much red-shift as galaxy Q. Compare "
                "their distances from Earth and explain your reasoning.",
        "options": [
            "P is about twice as far away as Q, because recession speed is "
            "proportional to distance",
            "P is about half as far away as Q, because galaxies nearer to us "
            "recede more quickly",
            "P and Q are the same distance away, because red-shift depends on "
            "the mass of a galaxy",
            "P is about four times as far away as Q, because red-shift "
            "depends on the distance squared",
        ],
        "correct_index": 0,
        "why": "Hubble's law, v = H₀d, is a direct proportion — twice the "
               "recession speed means twice the distance.",
    },
    {
        "id": "ks4-red-shift-big-bang-h04",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why astronomers describe observing a galaxy 10 "
                "billion light-years away as 'looking back in time'.",
        "options": [
            "Because clocks in that galaxy run slowly, so the galaxy is "
            "genuinely still in the past",
            "Because red-shifted light travels more slowly than blue light "
            "and so arrives much later",
            "Because the light left the galaxy 10 billion years ago, so we "
            "see it as it was at that time",
            "Because the expansion of space carries the galaxy's image "
            "backwards through time towards us",
        ],
        "correct_index": 2,
        "why": "Light travels at a finite speed, so light arriving now from "
               "10 billion light-years away set out 10 billion years ago.",
    },

    # ── dark-matter-dark-energy ─────────────────────────────────────────
    {
        "id": "ks4-dark-matter-dark-energy-e01",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the approximate proportion of the universe made up of "
                "ordinary matter.",
        "options": [
            "About 27%",
            "About 68%",
            "About 5%",
            "About 95%",
        ],
        "correct_index": 2,
        "why": "Everything we can see — stars, gas, planets — is only about "
               "5% of the universe; the other 95% is dark matter and dark "
               "energy.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-e02",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State why dark matter cannot be seen with any telescope.",
        "options": [
            "It is too far away for even the largest telescopes to resolve",
            "It does not emit, absorb or reflect electromagnetic radiation",
            "It is hidden behind the clouds of dust in the plane of our "
            "galaxy",
            "It is black in colour, so it reflects no light back towards us",
        ],
        "correct_index": 1,
        "why": "Telescopes work by collecting electromagnetic radiation, and "
               "dark matter does not interact with it at all.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-e03",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the effect that dark energy has on the expansion of "
                "the universe.",
        "options": [
            "It gradually slows the expansion down",
            "It has no measurable effect on the rate of expansion",
            "It holds the expansion at a perfectly steady rate",
            "It makes the expansion get faster over time",
        ],
        "correct_index": 3,
        "why": "Dark energy acts as a repulsive effect, so the expansion of "
               "the universe is accelerating rather than slowing.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-e04",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by gravitational lensing.",
        "options": [
            "The bending of light from a distant object as it passes a very "
            "massive object",
            "The focusing of starlight by the curved glass lens of a large "
            "optical telescope",
            "The reddening of starlight as it passes through clouds of "
            "interstellar dust",
            "The splitting of starlight into a spectrum by the gravity of a "
            "nearby star",
        ],
        "correct_index": 0,
        "why": "A large mass curves space-time, so light passing it is bent — "
               "the mass acts rather like a lens.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-s01",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the amount of gravitational lensing seen around "
                "a galaxy cluster is evidence for dark matter.",
        "options": [
            "Far more lensing is seen than the visible matter could produce, "
            "so extra unseen mass must be present",
            "Lensing is only ever seen where there is no visible matter, so "
            "dark matter must be causing all of it",
            "Dark matter bends light much more strongly than ordinary matter "
            "of the same mass would do",
            "Lensing shows that light is absorbed by dark matter and then "
            "re-emitted in a different direction",
        ],
        "correct_index": 0,
        "why": "The bending measures the total mass present, and it comes out "
               "far larger than the mass we can see — the shortfall is dark "
               "matter.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-s02",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Describe the difference between dark matter and dark energy.",
        "options": [
            "They are two names for the same thing — the invisible 95% of the "
            "universe",
            "Dark matter drives the expansion apart, while dark energy pulls "
            "galaxies back together",
            "Dark matter has mass and attracts by gravity; dark energy is an "
            "energy driving the expansion faster",
            "Dark matter is found only inside galaxies; dark energy is "
            "starlight too faint for us to see",
        ],
        "correct_index": 2,
        "why": "Dark matter is matter — it has mass and pulls things together "
               "gravitationally; dark energy is an unknown energy that pushes "
               "the expansion faster.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-s03",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why astronomers had expected the expansion of the "
                "universe to be slowing down.",
        "options": [
            "Because the push of the Big Bang had run out, leaving nothing to "
            "keep the galaxies moving apart",
            "Because the gravitational attraction between all the matter in "
            "the universe should pull it back together",
            "Because the universe loses energy as its light travels across "
            "the enormous distances between galaxies",
            "Because measurements of the microwave background show the "
            "universe cooling, and cooling means slowing",
        ],
        "correct_index": 1,
        "why": "Every mass in the universe attracts every other, so gravity "
               "alone would gradually brake the expansion — which is why the "
               "1998 result was such a surprise.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-s04",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why type Ia supernovae are useful for measuring "
                "distances across the universe.",
        "options": [
            "They are the brightest objects in the universe, so they can be "
            "seen from any distance at all",
            "They occur at a steady rate everywhere, so counting them over a "
            "year gives the distance",
            "They all happen at the same distance from us, so they provide a "
            "fixed scale to measure against",
            "They all reach about the same true brightness, so how dim one "
            "looks tells you how far away it is",
        ],
        "correct_index": 3,
        "why": "A known true brightness makes them 'standard candles': the "
               "fainter one appears, the further away it must be.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-h01",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Evaluate this claim: 'Dark matter has now been detected "
                "directly in laboratory experiments.'",
        "options": [
            "True — the Large Hadron Collider produced and identified dark "
            "matter particles in its collisions",
            "True — the Euclid space telescope has photographed dark matter "
            "in several nearby galaxies",
            "False — dark matter cannot be detected in any way at all, so it "
            "remains an idea with no evidence",
            "False — despite many experiments it has only ever been detected "
            "through its gravitational effects",
        ],
        "correct_index": 3,
        "why": "Every piece of evidence for dark matter — rotation curves, "
               "lensing, the CMB — is gravitational; no experiment has yet "
               "caught a dark matter particle.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-h02",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Predict what would happen to the universe if dark energy "
                "were to weaken until gravity dominated.",
        "options": [
            "The expansion would slow, stop and then reverse, so the universe "
            "would eventually collapse",
            "The expansion would simply carry on at exactly its present rate "
            "for the rest of time",
            "The expansion would speed up even more, tearing galaxies apart "
            "in a so-called 'Big Rip'",
            "The universe would stay at exactly its present size, held in "
            "balance by gravity for ever",
        ],
        "correct_index": 0,
        "why": "Gravity between all the matter in the universe is attractive, "
               "so without dark energy to oppose it the expansion would brake "
               "and reverse.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-h03",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Suggest why the discovery of dark matter and dark energy has "
                "not led astronomers to abandon the Big Bang model.",
        "options": [
            "Because the model is now too well established for any new "
            "observation to be allowed to change it",
            "Because both dark matter and dark energy were predictions made "
            "by the original Big Bang model",
            "Because the model still explains red-shift, the microwave background "
            "and the helium abundance",
            "Because dark matter and dark energy act only on the future of "
            "the universe, while the model describes only its past",
        ],
        "correct_index": 2,
        "why": "A model is abandoned when its predictions fail; the Big Bang "
               "model's predictions still hold, and dark matter and dark "
               "energy are extensions to it rather than refutations of it.",
    },
    {
        "id": "ks4-dark-matter-dark-energy-h04",
        "subtopic_slug": "dark-matter-dark-energy",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student argues that because 95% of the universe is "
                "unexplained, scientists must have got physics completely "
                "wrong. Evaluate this argument.",
        "options": [
            "It is fair, because a model that cannot account for 95% of what it "
            "describes can be of no real value",
            "It is unfair — the 95% is unidentified, not unmeasured, and its "
            "effects are predicted accurately",
            "It is fair, because dark matter and dark energy show that "
            "gravity does not work the way we describe it",
            "It is unfair, because the 95% has in fact been fully identified "
            "and only the naming of it is unfinished",
        ],
        "correct_index": 1,
        "why": "Dark matter and dark energy are measured quantities whose "
               "effects the model reproduces — what is missing is what they "
               "are made of, not whether they are there.",
    },
]
