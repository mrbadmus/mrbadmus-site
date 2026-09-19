"""P12 lesson 04 — The Sun, stars and galaxies: twelve questions (MRB-223).

Written against Design's page. The star you can see in daylight and the
five rungs of the ladder of scale are hers.

⊕ MRB-297 · 1 Sep 2026 — this said "the distance ladder", which this
branch renamed "the ladder of scale" on the page itself
(`lesson_04_the_sun_stars_and_galaxies.py` #s-bench). The prose follows
the rename. ⚠️ The MODEL KEY stays `distance-ladder`: it is the dispatch
string `shared/ks3.js` matches on, and `ks3_art/p12.py` says so.

The discriminations, in the order the lesson builds them:

  · what a star IS, and that the Sun is one (`SPACE-11`);
  · what sits inside what — star, solar system, galaxy, universe
    (`SPACE-14`);
  · the solar system holds exactly ONE star, so the night sky is not part
    of it (`SPACE-13`);
  · brightness in our sky mixes up output and distance (`SPACE-12`). The
    harder band sits here.

⚠️ POSITION IS AUTHORED — 3,1,2,0 · 0,2,1,3 · 2,3,0,1, three of each.

⚠️ Neither marked rung is restated: the four-scale ordering and the
student who thinks the night sky is in our solar system are the ladder's,
and nothing here reuses either.
"""

UNIT = "P12"
LESSON = "the-sun-stars-and-galaxies"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-04-e01",
        "band": "easier",
        "text": "What is the Sun?",
        "options": [
            {"text": "A planet", "correct": False,
             "why": "Planets do not make their own light. They shine only "
                    "because a star is lighting them."},
            {"text": "A galaxy", "correct": False,
             "why": "A galaxy is hundreds of billions of stars. The Sun is "
                    "one star."},
            {"text": "A very large moon", "correct": False,
             "why": "A moon orbits a planet and gives out no light of its "
                    "own. Everything in the solar system orbits the Sun."},
            {"text": "A star", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e02",
        "band": "easier",
        "text": "How many stars are there in our solar system?",
        "options": [
            {"text": "None — the Sun is not a star", "correct": False,
             "why": "The Sun is a star, and an ordinary one at that."},
            {"text": "One", "correct": True},
            {"text": "Eight, one for each planet", "correct": False,
             "why": "The eight are planets, and they orbit the single star at "
                    "the centre."},
            {"text": "Hundreds of billions", "correct": False,
             "why": "That is roughly the number in the whole GALAXY, not in "
                    "one solar system."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e03",
        "band": "easier",
        "text": "What is a galaxy?",
        "options": [
            {"text": "A star with planets going round it, and nothing else",
             "correct": False,
             "why": "That is a solar system. A galaxy holds billions of "
                    "them."},
            {"text": "The whole of space and everything that is in it",
             "correct": False,
             "why": "That is the universe, which holds around two trillion "
                    "galaxies."},
            {"text": "An enormous collection of stars held together by "
                     "gravity", "correct": True},
            {"text": "A cloud of gas that has not turned into stars yet",
             "correct": False,
             "why": "That is a nebula. Galaxies contain nebulae, along with "
                    "hundreds of billions of finished stars."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e04",
        "band": "easier",
        "text": "Which galaxy is the Sun in?",
        "options": [
            {"text": "The Milky Way", "correct": True},
            {"text": "Andromeda", "correct": False,
             "why": "Andromeda is the nearest large galaxy to ours, about "
                    "2.5 million light years away."},
            {"text": "The solar system", "correct": False,
             "why": "The solar system is not a galaxy. It is the Sun and the "
                    "objects orbiting it, inside a galaxy."},
            {"text": "It is not in a galaxy — galaxies are somewhere else",
             "correct": False,
             "why": "Almost every star is in a galaxy, and ours is no "
                    "exception. The faint band across a dark sky is our own "
                    "galaxy seen edge-on."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-04-s01",
        "band": "standard",
        "text": "What makes a star give out light?",
        "options": [
            {"text": "Hydrogen nuclei fusing into helium in its core",
             "correct": True},
            {"text": "Burning, like a very large fire", "correct": False,
             "why": "Burning needs oxygen and would use the Sun up in a few "
                    "thousand years. Fusion has kept it going for about five "
                    "billion."},
            {"text": "Reflecting light from the galaxy around it",
             "correct": False,
             "why": "Planets and moons shine by reflection. A star makes its "
                    "own light."},
            {"text": "Friction as it spins", "correct": False,
             "why": "Friction could not begin to supply the energy a star "
                    "pours out every second."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s02",
        "band": "standard",
        "text": "Why does the Sun look so much bigger and brighter than any "
                "other star?",
        "options": [
            {"text": "Because it is by far the largest star there is "
                     "anywhere", "correct": False,
             "why": "It is fairly ordinary. Some stars are hundreds of times "
                    "its diameter."},
            {"text": "Because it is the only star inside our own galaxy",
             "correct": False,
             "why": "The Milky Way holds about 200 billion stars, and the Sun "
                    "is one of them."},
            {"text": "Because it is about 270 000 times closer than the next "
                     "nearest star", "correct": True},
            {"text": "Because it is the youngest star and young stars shine "
                     "hardest", "correct": False,
             "why": "The Sun is about halfway through its life, and age is "
                    "not what sets how bright a star looks from here."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s03",
        "band": "standard",
        "text": "Put these in order from largest to smallest: the Milky Way, "
                "the solar system, the universe, the Sun.",
        "options": [
            {"text": "The universe, the solar system, the Milky Way, the Sun",
             "correct": False,
             "why": "The Milky Way holds billions of solar systems, so it is "
                    "far the larger of those two."},
            {"text": "The universe, the Milky Way, the solar system, the Sun",
             "correct": True},
            {"text": "The Milky Way, the universe, the Sun, the solar system",
             "correct": False,
             "why": "The universe holds every galaxy, so nothing is larger. "
                    "And the Sun sits inside the solar system."},
            {"text": "The universe, the Milky Way, the Sun, the solar system",
             "correct": False,
             "why": "The last two are the wrong way round. The Sun is one "
                    "object inside the solar system."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s04",
        "band": "standard",
        "text": "Roughly how many galaxies are there in the observable "
                "universe?",
        "options": [
            {"text": "One — the Milky Way is everything there is",
             "correct": False,
             "why": "That was believed until the 1920s. Andromeda alone is a "
                    "second, and it is visible to the naked eye."},
            {"text": "About two hundred", "correct": False,
             "why": "About 200 billion is the star count for ONE galaxy. The "
                    "number of galaxies is larger still."},
            {"text": "Around two trillion", "correct": True},
            {"text": "About eight, one for each planet", "correct": False,
             "why": "Planets orbit a star inside a galaxy. They have nothing "
                    "to do with how many galaxies exist."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-04-h01",
        "band": "harder",
        "text": "Star A looks brighter in the night sky than star B. What "
                "can you conclude?",
        "options": [
            {"text": "Star A is closer than star B, because the nearer of two "
                     "stars always looks the brighter", "correct": False,
             "why": "It might be. It might also be enormously further away "
                    "and enormously brighter."},
            {"text": "Star A gives out more light than star B, because a "
                     "star's brightness in the sky is its own output",
             "correct": False,
             "why": "It might. Brightness in our sky depends on distance as "
                    "well, so this cannot be settled from the sky alone."},
            {"text": "Nothing certain — brightness in our sky depends on "
                     "distance as well as on output", "correct": True},
            {"text": "Star A is larger than star B, because a bigger star "
                     "pours out more light and so looks brighter",
             "correct": False,
             "why": "Size, output and distance are three different things, "
                    "and only their combination reaches your eye."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h02",
        "band": "harder",
        "text": "Betelgeuse is about 500 light years away and blazes in the "
                "night sky. Proxima Centauri is 4.24 light years away and "
                "needs a telescope. What does that tell you?",
        "options": [
            {"text": "Proxima Centauri must be hidden behind a thick cloud "
                     "of dust", "correct": False,
             "why": "Dust does dim some stars, and it is not needed here: "
                    "Proxima is simply a very faint kind of star."},
            {"text": "Betelgeuse must have been measured wrongly, because "
                     "closer stars always look brighter than distant ones",
             "correct": False,
             "why": "Closer stars do not always look brighter. That is the "
                    "assumption this pair of stars exists to break."},
            {"text": "One of the two distances must have been measured "
                     "wrongly", "correct": False,
             "why": "Both are well measured. The two stars really are that "
                    "different in the light they give out."},
            {"text": "Betelgeuse gives out vastly more light than Proxima "
                     "Centauri, enough to beat a hundredfold distance",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h03",
        "band": "harder",
        "text": "Most stars visible on a dark night have planets of their "
                "own. What follows about the phrase 'the solar system'?",
        "options": [
            {"text": "It names OUR star and everything orbiting it, and other "
                     "stars have systems of their own", "correct": True},
            {"text": "It names every star that has planets of its own, so "
                     "most of the night sky is part of it", "correct": False,
             "why": "It names ours alone. Every other star's system is a "
                    "separate one, light years away."},
            {"text": "It has become meaningless, because there are so many "
                     "other systems", "correct": False,
             "why": "It is a name for one particular system, which is exactly "
                    "as useful now as it was before the others were found."},
            {"text": "It should be replaced, because the Sun turns out not "
                     "to be special at all", "correct": False,
             "why": "The Sun is ordinary as stars go, and it is still the one "
                    "star our own system is built round."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h04",
        "band": "harder",
        "text": "Why is the Milky Way seen as a faint BAND across the sky "
                "rather than as a shape you can look at from outside?",
        "options": [
            {"text": "Because most of it is too dim for the human eye, and "
                     "only the brightest strip of it comes through",
             "correct": False,
             "why": "Its dimness explains why the band is faint. It does not "
                    "explain why the shape is a band."},
            {"text": "Because only part of it has formed so far, so the rest "
                     "of the shape is still missing", "correct": False,
             "why": "The whole galaxy has been there for billions of years. "
                    "What is limited is our viewpoint, not the galaxy."},
            {"text": "Because we are inside its disc, so its stars are spread "
                     "along a line right round us", "correct": True},
            {"text": "Because the rest of it is hidden behind Andromeda, which "
                     "blocks everything beyond it from view", "correct": False,
             "why": "Andromeda is 2.5 million light years away and covers a "
                    "tiny patch of sky. It hides nothing."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-04-e05",
        "band": "easier",
        "text": "What is a star?",
        "options": [
            {"text": "A ball of gas fusing hydrogen in its core",
             "correct": True},
            {"text": "A large rocky planet that glows", "correct": False,
             "why": "Planets do not glow with light of their own; they "
                    "reflect a star's."},
            {"text": "A galaxy seen from a long way off", "correct": False,
             "why": "A galaxy holds hundreds of billions of stars; a star is "
                    "one object."},
            {"text": "A piece of rock burning up in the atmosphere",
             "correct": False,
             "why": "That is a meteor, and it lasts a second or two."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e06",
        "band": "easier",
        "text": "A solar system is…",
        "options": [            {"text": "a star and everything orbiting it", "correct": True},
            {"text": "every star in a galaxy", "correct": False,
             "why": "That is roughly what a galaxy is; a solar system has one "
                    "star."},
            {"text": "the whole universe", "correct": False,
             "why": "The universe holds about two trillion galaxies, each "
                    "with billions of stars."},
            {"text": "a group of planets with no star", "correct": False,
             "why": "The star is the thing everything else orbits."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e07",
        "band": "easier",
        "text": "Roughly how many stars are in a galaxy?",
        "options": [
            {"text": "About a thousand", "correct": False,
             "why": "That is far too few — you can see more than that with "
                    "the naked eye on a dark night."},
            {"text": "About a million", "correct": False,
             "why": "Still far too few; a galaxy holds hundreds of thousands "
                    "of times that."},
            {"text": "Hundreds of billions", "correct": True},
            {"text": "Exactly one", "correct": False,
             "why": "One star with things orbiting it is a solar system, not "
                    "a galaxy."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e08",
        "band": "easier",
        "text": "What holds a galaxy together?",
        "options": [            {"text": "Magnetism between the stars", "correct": False,
             "why": "Magnetic fields exist in space but are far too weak to "
                    "hold a galaxy."},
            {"text": "The pressure of the light the stars give out",
             "correct": False,
             "why": "Light pressure pushes outwards; it would drive a galaxy "
                    "apart rather than bind it."},
            {"text": "Gravity between all its stars", "correct": True},
            {"text": "Nothing — a galaxy is slowly flying apart",
             "correct": False,
             "why": "Its stars orbit the centre together, held by gravity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-e09",
        "band": "easier",
        "text": "Is the Sun a star?",
        "options": [
            {"text": "No — it is far too large to be a star", "correct": False,
             "why": "It is an ordinary star; many are far larger."},
            {"text": "No — stars are only the small points seen at night",
             "correct": False,
             "why": "Those points are stars too, seen from enormously further "
                    "away."},
            {"text": "Yes — it is an ordinary star seen close up", "correct": True},
            {"text": "Yes, and the only one there is", "correct": False,
             "why": "There are hundreds of billions in our galaxy alone."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-04-s05",
        "band": "standard",
        "text": "Why do other stars look like tiny points of light?",
        "options": [            {"text": "Because they are much smaller than the Sun",
             "correct": False,
             "why": "Many are far larger; distance is what makes them look "
                    "like points."},
            {"text": "Because they are hidden behind the atmosphere",
             "correct": False,
             "why": "The atmosphere makes them twinkle; the distance makes "
                    "them small."},
            {"text": "Because they give out far less light", "correct": False,
             "why": "Some give out thousands of times more, and still look "
                    "like points."},
            {"text": "Because they are enormously further away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s06",
        "band": "standard",
        "text": "Which contains the other: the Milky Way, or the solar "
                "system?",
        "options": [            {"text": "The Milky Way contains the solar system", "correct": True},
            {"text": "The solar system contains the Milky Way",
             "correct": False,
             "why": "The solar system is one star and its planets; the Milky "
                    "Way holds hundreds of billions of stars."},
            {"text": "Neither contains the other; they sit side by side",
             "correct": False,
             "why": "The Sun is one of the Milky Way's stars, so it is "
                    "inside it."},
            {"text": "They are two names for the same thing", "correct": False,
             "why": "They are separated by a factor of hundreds of billions "
                    "of stars."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s07",
        "band": "standard",
        "text": "Roughly how much further away is the nearest star than the "
                "Sun?",
        "options": [
            {"text": "About a hundred times", "correct": False,
             "why": "That is nowhere near enough; it would still be well "
                    "inside the solar system."},
            {"text": "About a thousand times", "correct": False,
             "why": "Still far too close — that is roughly the outer edge of "
                    "the planets."},
            {"text": "About 270 000 times", "correct": True},
            {"text": "About twice as far", "correct": False,
             "why": "At twice the Sun's distance you would be at Mars, not "
                    "at another star."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s08",
        "band": "standard",
        "text": "What is the universe?",
        "options": [            {"text": "The Sun and everything that orbits it", "correct": False,
             "why": "That is the solar system, one star out of hundreds of "
                    "billions in our galaxy alone."},
            {"text": "The band of stars seen across the night sky",
             "correct": False,
             "why": "That band is our own galaxy seen from inside it, and it "
                    "is one galaxy among about two trillion."},
            {"text": "Every galaxy there is", "correct": True},
            {"text": "The space between the galaxies", "correct": False,
             "why": "The universe is everything, the galaxies included, not "
                    "only the gaps."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-s09",
        "band": "standard",
        "text": "Why is a bright star in the night sky not necessarily a "
                "close one?",
        "options": [            {"text": "Because brightness depends only on distance",
             "correct": False,
             "why": "If that were so, the brightest would always be the "
                    "nearest — and they are not."},
            {"text": "Because all stars give out the same amount of light",
             "correct": False,
             "why": "They differ by factors of many thousands, which is "
                    "exactly the point."},
            {"text": "Because the atmosphere brightens some stars and not "
                     "others",
             "correct": False,
             "why": "The air makes them twinkle; it does not pick some out to "
                    "brighten."},
            {"text": "Because how much light a star gives out varies "
                     "enormously as well",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-04-h05",
        "band": "harder",
        "text": "Why can a galaxy be called mostly empty when it holds "
                "hundreds of billions of stars?",
        "options": [            {"text": "Because the gaps between stars are vast compared with "
                     "the stars themselves",
             "correct": True},
            {"text": "Because most of its stars have burnt out",
             "correct": False,
             "why": "The great majority are shining; emptiness is about the "
                    "space between them."},
            {"text": "Because a galaxy is a flat disc with nothing above or "
                     "below it",
             "correct": False,
             "why": "It has thickness, and the emptiness is between the stars "
                    "within it."},
            {"text": "Because only the centre of a galaxy contains stars",
             "correct": False,
             "why": "Stars are spread right through it, including our own far "
                    "from the centre."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h06",
        "band": "harder",
        "text": "Andromeda is 2.5 million light years away. What are you "
                "seeing when you look at it?",
        "options": [            {"text": "It exactly as it is at this moment", "correct": False,
             "why": "The light has taken 2.5 million years to arrive, so it "
                    "cannot show the present."},
            {"text": "A reflection of our own galaxy", "correct": False,
             "why": "It is a separate galaxy, not an image of ours."},
            {"text": "It as it was 2.5 million years ago", "correct": True},
            {"text": "It as it will be in 2.5 million years", "correct": False,
             "why": "No observation can show the future; light carries the "
                    "past."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h07",
        "band": "harder",
        "text": "The Sun will one day run out of hydrogen in its core. What "
                "does that tell you about a star?",
        "options": [            {"text": "That it is burning like a fire, using oxygen",
             "correct": False,
             "why": "There is no oxygen and no burning; hydrogen is fused "
                    "into helium."},
            {"text": "That stars cannot last more than a few thousand years",
             "correct": False,
             "why": "The Sun has been shining for billions of years and has "
                    "billions left."},
            {"text": "That it will explode as soon as the hydrogen is gone",
             "correct": False,
             "why": "What happens next depends on the star's mass, and the "
                    "Sun will not explode."},
            {"text": "That it is fusing a supply of fuel that is large but "
                     "finite",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h08",
        "band": "harder",
        "text": "Two stars look equally bright, but one is ten times further "
                "away. What follows?",
        "options": [
            {"text": "They give out the same amount of light", "correct": False,
             "why": "Then the further one would look far fainter, and it does "
                    "not."},
            {"text": "The further one gives out far more light",
             "correct": True},
            {"text": "The nearer one gives out far more light",
             "correct": False,
             "why": "The nearer one has the advantage of distance already, so "
                    "it needs LESS output to match."},
            {"text": "Nothing can be said without knowing their colours",
             "correct": False,
             "why": "Colour tells you about temperature; the brightness and "
                    "distance already settle this."},
        ],
        "figure": None,
    },
    {
        "id": "p12-04-h09",
        "band": "harder",
        "text": "Why is the Sun the only star whose disc we can make out?",
        "options": [
            {"text": "Because it is the largest star there is",
             "correct": False,
             "why": "It is an ordinary star, and many are hundreds of times "
                    "wider."},
            {"text": "Because it is enormously closer than any other",
             "correct": True},
            {"text": "Because the others are hidden by the atmosphere",
             "correct": False,
             "why": "Telescopes above the atmosphere still see them as "
                    "points."},
            {"text": "Because it is the only one that gives out visible light",
             "correct": False,
             "why": "Every star we can see is giving out visible light, which "
                    "is how we see it."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ─────────────────────────────────────────
    {
            "id": 'p12-04-e10',
            "band": 'easier',
            "text": 'Roughly how old is the Sun?',
            "options": [
                {"text": 'About 4.6 billion years', "correct": True},
                {"text": 'About 4.6 million years', "correct": False, "why": 'That is a thousand times too young for a star this far through its life.'},
                {"text": 'About 100 years old', "correct": False, "why": "That is within a human lifetime, nowhere near a star's age."},
                {"text": 'About 4.6 trillion years', "correct": False, "why": 'That is older than the universe itself, at about 13.8 billion years.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e11',
            "band": 'easier',
            "text": 'What is a nebula?',
            "options": [
                {"text": 'A finished star that has burnt out completely', "correct": False, "why": 'A burnt-out star is dense and compact, not a spread-out cloud.'},
                {"text": 'A cloud of gas and dust where stars can form', "correct": True},
                {"text": 'A small moon orbiting a distant planet', "correct": False, "why": 'A moon is one solid orbiting body, not a cloud of gas and dust.'},
                {"text": 'The empty space between two galaxies', "correct": False, "why": 'That space is close to a true vacuum; a nebula is real gas and dust.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e12',
            "band": 'easier',
            "text": 'Sirius is the brightest star in the night sky. Is it also the closest star to the Sun?',
            "options": [
                {"text": 'Yes — the brightest star is the closest one', "correct": False, "why": 'Brightness mixes distance with light output, so brightest need not mean closest.'},
                {"text": 'Yes — Sirius is a member of the solar system', "correct": False, "why": 'Sirius is a separate star, light years away, not a member of the solar system.'},
                {"text": 'No — Proxima Centauri is the closer of the two', "correct": True},
                {"text": 'No — the closest star has not yet been identified', "correct": False, "why": 'The nearest star is well known: Proxima Centauri, at 4.24 light years.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e13',
            "band": 'easier',
            "text": 'What shape is our own galaxy, the Milky Way?',
            "options": [
                {"text": 'A thin ring with a hole through the middle', "correct": False, "why": 'A ring has no centre filled with stars; the Milky Way is thickest in the middle.'},
                {"text": 'A single straight line of stars in a row', "correct": False, "why": "The band in the sky is that shape seen edge-on, not the galaxy's actual form."},
                {"text": 'A perfect sphere, evenly bright all the way round with no visible structure', "correct": False, "why": 'A featureless sphere has no spiral arms and no flat disc, unlike the Milky Way.'},
                {"text": 'A barred spiral, with arms winding out from a central bar', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e14',
            "band": 'easier',
            "text": 'What sits at the centre of the Milky Way?',
            "options": [
                {"text": 'A supermassive black hole', "correct": True},
                {"text": 'A dense cluster of planets with no star nearby', "correct": False, "why": "Planets need a star to orbit; the centre's mass is not a group of planets."},
                {"text": 'A single star far bigger than the Sun', "correct": False, "why": 'The mass there is concentrated in a black hole, not a single giant star.'},
                {"text": 'The emptiest part of the whole galaxy', "correct": False, "why": 'The centre is the most crowded part of the galaxy, not the emptiest.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e15',
            "band": 'easier',
            "text": 'The Sun is classed as a yellow dwarf. What does that mean?',
            "options": [
                {"text": 'It is one of the largest kinds of star there is', "correct": False, "why": 'A yellow dwarf is unremarkable; supergiants are far bigger and brighter.'},
                {"text": 'It is a fairly ordinary, middle-sized star', "correct": True},
                {"text": 'It has already burnt out and stopped shining', "correct": False, "why": 'The Sun is actively fusing hydrogen right now, not a burnt-out object.'},
                {"text": 'It is a class found in other galaxies, never in ours', "correct": False, "why": 'The Sun itself is a yellow dwarf, and it is firmly inside the Milky Way.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e16',
            "band": 'easier',
            "text": 'Proxima Centauri is a red dwarf. Compared with the Sun, what does that make it?',
            "options": [
                {"text": 'A much larger and brighter star', "correct": False, "why": 'A red dwarf is the opposite: small and faint, well below the Sun.'},
                {"text": 'Exactly the same kind of star', "correct": False, "why": 'The Sun is a yellow dwarf; a red dwarf is a smaller, cooler class.'},
                {"text": 'Smaller and far fainter than the Sun', "correct": True},
                {"text": 'A star giving out no light of its own', "correct": False, "why": 'A red dwarf is a true star, fusing hydrogen, just far less of it.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e17',
            "band": 'easier',
            "text": 'Betelgeuse is classed as a red supergiant star. In terms of size and light output, what does that name tell you about it?',
            "options": [
                {"text": 'It shines with reflected light, not its own', "correct": False, "why": 'A supergiant makes its own light by fusion, on a huge scale, like any star.'},
                {"text": 'Roughly the same size and output as the Sun', "correct": False, "why": 'A red supergiant dwarfs an ordinary star like the Sun in size and output.'},
                {"text": 'One of the smallest known kinds of star', "correct": False, "why": 'A supergiant is among the largest kinds of star, not the smallest.'},
                {"text": 'Enormously larger and more luminous than the Sun', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e18',
            "band": 'easier',
            "text": 'What causes a star to appear to twinkle at night, while a planet does not?',
            "options": [
                {"text": 'Moving air in our own atmosphere bending its light', "correct": True},
                {"text": 'Clouds passing in front of stars more than planets', "correct": False, "why": "Clouds would block a planet's light just as much; twinkling happens on clear nights too."},
                {"text": "The star's own light flickering on and off", "correct": False, "why": "A star's output is steady; the flicker is added after the light leaves it."},
                {"text": 'Distant stars cooling and warming in fast cycles', "correct": False, "why": "A star's temperature does not swing on a timescale a person could see."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e19',
            "band": 'easier',
            "text": 'Roughly how many light years across is the Milky Way?',
            "options": [
                {"text": 'About 100 billion', "correct": False, "why": "That confuses the galaxy's width with its star count, roughly 200 billion."},
                {"text": 'About 100 000', "correct": True},
                {"text": 'About 100 million', "correct": False, "why": 'That is a thousand times too wide for our galaxy — closer to a gap between galaxies.'},
                {"text": 'About 100 light years', "correct": False, "why": 'That is far too small — smaller than the gap to even the nearest star.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e20',
            "band": 'easier',
            "text": 'Roughly how many stars does the Andromeda galaxy contain?',
            "options": [
                {"text": 'About two hundred billion', "correct": False, "why": "That figure is closer to the Milky Way's own star count."},
                {"text": 'About a thousand stars in total', "correct": False, "why": 'A galaxy holds vastly more than that, billions at the very least.'},
                {"text": 'About a trillion', "correct": True},
                {"text": 'One star, at its very centre', "correct": False, "why": 'A galaxy is defined by holding vast numbers of stars, not a single one.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e21',
            "band": 'easier',
            "text": "What does a star's colour mainly tell an astronomer?",
            "options": [
                {"text": 'How far away the star is from Earth', "correct": False, "why": "Distance is worked out from other clues, not from a star's colour."},
                {"text": 'How much the star weighs in kilograms', "correct": False, "why": "Mass is worked out separately, often from a companion star's orbit."},
                {"text": 'How old the star is, in years', "correct": False, "why": 'Age is estimated from other evidence, not read off from colour alone.'},
                {"text": "Roughly how hot the star's surface is", "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e22',
            "band": 'easier',
            "text": 'About how long does the Sun take to orbit the centre of the Milky Way once?',
            "options": [
                {"text": 'About 230 million years', "correct": True},
                {"text": 'About one year', "correct": False, "why": 'One year is how long EARTH takes to orbit the SUN, a much smaller circuit.'},
                {"text": 'About 230 days', "correct": False, "why": 'That is barely longer than an Earth year — nowhere near enough time.'},
                {"text": 'About 4.6 billion years', "correct": False, "why": "That is roughly the Sun's whole age, spanning many such orbits, not one."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e23',
            "band": 'easier',
            "text": 'About how far is the Sun from the centre of the Milky Way?',
            "options": [
                {"text": 'About 26 light years, barely off-centre', "correct": False, "why": 'That is a thousand times too close, closer than several nearby stars.'},
                {"text": 'About 26 000 light years, roughly halfway out', "correct": True},
                {"text": 'Right at the very centre', "correct": False, "why": 'The Sun sits out in a spiral arm, well away from the crowded centre.'},
                {"text": 'There is no fixed centre a distance like that could ever be measured from', "correct": False, "why": 'The galaxy has a definite centre, marked by its supermassive black hole.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e24',
            "band": 'easier',
            "text": 'Before the 1920s, what did most astronomers believe about the Milky Way?',
            "options": [
                {"text": 'That it was one of countless galaxies', "correct": False, "why": 'That view came AFTER the 1920s, once other galaxies were confirmed.'},
                {"text": 'That it held a few hundred stars, all visible to the naked eye on a dark night', "correct": False, "why": 'Even then its star count was already known to be enormous, not a few hundred.'},
                {"text": 'That it was the whole universe, with nothing beyond', "correct": True},
                {"text": 'That the Sun sat exactly at its centre', "correct": False, "why": "That belief is about the Sun's position, a separate question from other galaxies existing."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e25',
            "band": 'easier',
            "text": 'Why are galaxy star counts given as estimates rather than exact figures?',
            "options": [
                {"text": 'The number of stars changes from night to night', "correct": False, "why": "A galaxy's star count shifts over millions of years, not overnight."},
                {"text": 'Nobody has attempted to work them out', "correct": False, "why": 'Astronomers have worked hard on the estimates; they are simply not exact counts.'},
                {"text": 'Stars are too dim for a telescope to detect', "correct": False, "why": 'Enormous numbers ARE detected; the difficulty is totalling them, not seeing any.'},
                {"text": 'There are simply far too many to count one at a time', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e26',
            "band": 'easier',
            "text": 'Almost all the hydrogen in the universe formed minutes after the Big Bang. Where did the hydrogen now fusing in the Sun come from?',
            "options": [
                {"text": 'That original hydrogen, formed long before the Sun', "correct": True},
                {"text": 'It formed recently, inside the Sun itself', "correct": False, "why": 'Stars fuse hydrogen; they do not create it fresh from nothing.'},
                {"text": 'It arrived from a nearby star exploding just before the Sun formed', "correct": False, "why": 'A nearby explosion is where HEAVIER elements come from; hydrogen traces further back.'},
                {"text": 'Its origin has never been worked out', "correct": False, "why": "This is well established: it traces back to the universe's earliest minutes."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e27',
            "band": 'easier',
            "text": 'Where were the carbon and oxygen atoms in your body originally made?',
            "options": [
                {"text": 'In the Sun, carried to Earth by sunlight', "correct": False, "why": 'Sunlight carries energy, not atoms; these elements predate the solar system.'},
                {"text": 'Inside stars that died before the Sun formed', "correct": True},
                {"text": 'They have simply always existed, unchanged', "correct": False, "why": 'Fusion inside earlier stars built these elements up from hydrogen over time.'},
                {"text": 'On Earth, inside its rocky, iron-rich core', "correct": False, "why": "Earth's core makes no new elements; carbon and oxygen were forged in stars first."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e28',
            "band": 'easier',
            "text": 'Gold is heavier than iron and needs a far more violent event than ordinary fusion to be made. What kind of event is thought to make most of it?',
            "options": [
                {"text": "A star's ordinary, everyday fusion of hydrogen", "correct": False, "why": 'Ordinary fusion stops well before it can build something as heavy as gold.'},
                {"text": 'A comet striking the surface of a planet', "correct": False, "why": 'A comet impact releases far too little energy to build a new heavy element.'},
                {"text": 'Two neutron stars colliding', "correct": True},
                {"text": "A planet's own volcanic activity", "correct": False, "why": 'Volcanoes rearrange elements already present; they do not fuse new ones.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e29',
            "band": 'easier',
            "text": 'Betelgeuse gives out roughly how many times as much light as the Sun?',
            "options": [
                {"text": 'About half as much light', "correct": False, "why": 'A supergiant outshines an ordinary star; it does not give out less light.'},
                {"text": 'About the same amount of light', "correct": False, "why": 'A red supergiant vastly outshines the Sun; this is not a fair match.'},
                {"text": 'About ten times as much light', "correct": False, "why": 'That would be a bright star, but far short of the supergiant it actually is.'},
                {"text": 'About 100 000 times as much light', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-e30',
            "band": 'easier',
            "text": 'A chart of distances in space uses a scale on which each step upward is ten times the last, rather than an ordinary ruler scale. Why is that done?',
            "options": [
                {"text": 'The objects span far more powers of ten than an ordinary straight scale could show', "correct": True},
                {"text": 'It is done purely to make the bars look tidier and better spaced out', "correct": False, "why": 'Appearance is not the reason; on an ordinary scale the smallest bars would vanish altogether.'},
                {"text": 'Distances in space are measured with a completely different system of units from the ones used on Earth', "correct": False, "why": 'They use ordinary units perfectly well; the scale is about fitting a huge RANGE onto one chart.'},
                {"text": 'A ten-times scale is the only way to plot a distance given in light years', "correct": False, "why": 'A distance in light years plots on an ordinary scale like any other number; the range is what forces the choice.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s10',
            "band": 'standard',
            "text": "The Sun's total lifetime as a star is expected to be about ten billion years, and it is currently about 4.6 billion years old. What stage of its life is that?",
            "options": [
                {"text": 'Roughly the halfway point of its life', "correct": True},
                {"text": 'Right at the very beginning of its life', "correct": False, "why": '4.6 out of 10 billion years is close to the midpoint, not the very start.'},
                {"text": 'Almost at the very end of its life', "correct": False, "why": 'About 5.4 billion years remain, more time than has already passed.'},
                {"text": 'Impossible to judge from those two figures', "correct": False, "why": 'Dividing the age by the total lifetime gives the stage directly.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s11',
            "band": 'standard',
            "text": "The Sun takes about 230 million years to orbit the Milky Way's centre, and formed about 4.6 billion years ago. Roughly how many of these orbits has it completed?",
            "options": [
                {"text": 'About 200 orbits so far', "correct": False, "why": 'That divides by 23 million, ten times too short an orbit period.'},
                {"text": 'About 20 orbits so far', "correct": True},
                {"text": 'About 2 orbits so far', "correct": False, "why": '4.6 billion divided by 230 million comes out far larger than 2.'},
                {"text": "Impossible without the orbit's size", "correct": False, "why": 'Total age divided by orbit length gives the count directly, with no size needed.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s12',
            "band": 'standard',
            "text": 'The Milky Way is about 100 000 light years across, and the Sun sits about 26 000 light years from its centre. Is the Sun close to the centre, close to the edge, or midway?',
            "options": [
                {"text": 'Very close to the outer edge of the disc', "correct": False, "why": 'The edge sits at a radius of about 50 000 light years; 26 000 is only just past half.'},
                {"text": 'Very close to the crowded centre', "correct": False, "why": '26 000 out of a 50 000-light-year radius is just past half way out, not close in.'},
                {"text": 'Roughly midway between centre and edge', "correct": True},
                {"text": 'It cannot be judged without the exact shape', "correct": False, "why": "Comparing the radius to the Sun's distance is enough to place it roughly midway."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s13',
            "band": 'standard',
            "text": 'Andromeda holds roughly a trillion stars and the Milky Way roughly two hundred billion. Roughly how many times more stars does Andromeda have?',
            "options": [
                {"text": 'About fifty times as many', "correct": False, "why": 'That divides by ten too many; the real ratio is closer to five.'},
                {"text": 'Much the same number, roughly speaking', "correct": False, "why": 'A trillion against two hundred billion is a clear, measurable gap, not rounding.'},
                {"text": 'About twice as many', "correct": False, "why": 'A trillion is five times two hundred billion, not merely twice.'},
                {"text": 'About five times as many', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s14',
            "band": 'standard',
            "text": 'A dying star scatters newly made carbon and iron out as a cloud of gas and dust. Why does that matter for a solar system forming nearby afterwards?',
            "options": [
                {"text": "They can end up in the new star's own planets and anything living there", "correct": True},
                {"text": 'It has no later effect; the elements simply drift away and are lost', "correct": False, "why": 'The scattered elements are exactly what gets swept up into new stars and planets, not lost.'},
                {"text": 'It cools nearby space enough for a new star to form', "correct": False, "why": 'Gravity pulling gas together forms new stars; the point of the material is what it CONTAINS.'},
                {"text": 'It affects the new star itself, while any planets and living things there form from separate material', "correct": False, "why": 'Rocky planets and living bodies are built from these same scattered elements too.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s15',
            "band": 'standard',
            "text": "Why can an ordinary star's fusion not make elements heavier than iron, such as gold?",
            "options": [
                {"text": 'Ordinary stars are not hot enough for fusion at all', "correct": False, "why": 'Ordinary stars are plenty hot enough for hydrogen fusion; the limit is which elements it reaches.'},
                {"text": 'Fusing past iron takes in energy instead of releasing it', "correct": True},
                {"text": 'Iron is too rare for ordinary stars to ever reach', "correct": False, "why": 'Iron is a common product of stellar fusion; the limit is going beyond it.'},
                {"text": 'Gold atoms are too heavy to exist inside a star', "correct": False, "why": "Gold can exist inside a star; a star's ordinary fusion simply cannot build it there."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s16',
            "band": 'standard',
            "text": 'A telescope is pointed at a planet and a star of similar brightness, the same night. Which twinkles more, and why?',
            "options": [
                {"text": 'The planet, since it passes through more atmosphere', "correct": False, "why": 'Both are seen through the same overhead atmosphere; height above ground is not the difference.'},
                {"text": 'The star, since its own disc averages the flicker out', "correct": False, "why": 'It is the PLANET that shows a resolvable disc; a star stays a point, which is why it twinkles more.'},
                {"text": 'The star, since it stays a point that moving air can shimmer', "correct": True},
                {"text": 'Neither — twinkling depends on brightness alone', "correct": False, "why": 'Two equally bright objects can twinkle very differently, depending on whether either shows a disc.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s17',
            "band": 'standard',
            "text": 'Two stars are the same size and distance, but one shines blue-white and the other red. What does that colour difference mainly tell you?',
            "options": [
                {"text": 'The red star must give out more light overall', "correct": False, "why": 'Colour alone does not settle total output; here it points to surface temperature instead.'},
                {"text": 'The blue-white star must be further away', "correct": False, "why": 'The question fixes both at the same distance, so that cannot be what the colour shows.'},
                {"text": 'The two stars share the very same temperature', "correct": False, "why": 'A colour difference like this reflects a real temperature difference between the two.'},
                {"text": 'The blue-white star is hotter than the red one', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s18',
            "band": 'standard',
            "text": 'Before the 1920s, astronomers assumed every star belonged to one system that was the whole universe. What discovery overturned that?',
            "options": [
                {"text": 'Showing Andromeda lies far outside the Milky Way', "correct": True},
                {"text": 'Discovering that stars are powered by fusion', "correct": False, "why": 'That explains how a star shines, not whether other galaxies exist beyond ours.'},
                {"text": 'Counting the exact number of stars in the Milky Way', "correct": False, "why": 'An exact count within our own galaxy says nothing about anything beyond it.'},
                {"text": "Placing the Sun's exact position in the galaxy", "correct": False, "why": "That is about one star's location, a separate question from other galaxies existing."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s19',
            "band": 'standard',
            "text": 'Why can astronomers not simply count every star in the Milky Way one by one, to get an exact figure?',
            "options": [
                {"text": 'Because the definition of a star keeps changing', "correct": False, "why": 'The definition is settled; the difficulty is sheer numbers and things blocking the view.'},
                {"text": 'Because hundreds of billions exist, many hidden from view', "correct": True},
                {"text": 'Because most of its stars are too dim to detect', "correct": False, "why": 'Vast numbers ARE detected individually; totalling hundreds of billions is the real difficulty.'},
                {"text": 'Because stars form and die too fast for a count', "correct": False, "why": 'Stars form and die far too slowly to be the reason a snapshot count is impossible.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s20',
            "band": 'standard',
            "text": 'Proxima Centauri is a red dwarf and Betelgeuse a red supergiant. What difference do those two names point to?',
            "options": [
                {"text": 'Which constellation each one officially belongs to', "correct": False, "why": "A constellation is a pattern in Earth's sky, unrelated to a star's own class."},
                {"text": 'How far each star sits from the Sun', "correct": False, "why": 'Those names describe the stars themselves, not their distance from us.'},
                {"text": "A huge difference in each star's size and power", "correct": True},
                {"text": 'Whether the star still fuses hydrogen today', "correct": False, "why": 'Both fuse hydrogen right now; the names describe size and power, not activity.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s21',
            "band": 'standard',
            "text": "Betelgeuse gives out about 100 000 times the Sun's light, yet looks nowhere near 100 000 times brighter from Earth. What resolves that?",
            "options": [
                {"text": 'Its light is mostly heat rather than visible light', "correct": False, "why": 'Some output is invisible, but not nearly enough to explain the gap here.'},
                {"text": 'Human eyes cannot register so large a difference', "correct": False, "why": 'Eyes register huge brightness differences fine; distance is the missing factor.'},
                {"text": 'The 100 000 figure for its output is simply wrong', "correct": False, "why": 'The output figure is well measured; the separate factor here is distance.'},
                {"text": 'It is enormously further away, which cuts that advantage down', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s22',
            "band": 'standard',
            "text": "A supermassive black hole sits at the Milky Way's centre. Is the rest of the galaxy slowly falling into it?",
            "options": [
                {"text": 'No — its pull is strongest nearby, and distant stars simply orbit around it', "correct": True},
                {"text": 'Yes, but recently formed stars alone are affected', "correct": False, "why": "A star's age makes no difference to how galactic gravity sets a stable orbit."},
                {"text": 'Yes, every star is spiralling steadily inward', "correct": False, "why": 'Stars, the Sun included, stay in stable orbits; they are not spiralling in.'},
                {"text": 'No, it has no pull beyond its close surroundings', "correct": False, "why": 'Its gravity reaches right across the galaxy and helps set the orbits, just not overwhelmingly at a distance.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s23',
            "band": 'standard',
            "text": 'The Milky Way is about 100 000 light years across, and Andromeda is roughly twice as wide. Roughly how many light years across is Andromeda?',
            "options": [
                {"text": 'About 2 000 000 light years', "correct": False, "why": 'That multiplies by twenty rather than by two, ten times too large.'},
                {"text": 'About 200 000 light years', "correct": True},
                {"text": 'About 50 000 light years', "correct": False, "why": "That halves the Milky Way's width; Andromeda is the LARGER galaxy of the two."},
                {"text": 'About 100 000 light years', "correct": False, "why": "That is the Milky Way's own width, unchanged from the figure given."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s24',
            "band": 'standard',
            "text": 'A galaxy catalogue lists a spiral galaxy as roughly the same width as the Milky Way. What does that alone tell you about its star count?',
            "options": [
                {"text": 'It must hold far fewer stars, since a wider galaxy spreads its stars out more thinly overall', "correct": False, "why": 'There is no such rule; width and star count are just two separate properties.'},
                {"text": 'It must hold exactly the same number of stars', "correct": False, "why": 'Two similar-width galaxies can still differ in how densely their stars are packed.'},
                {"text": 'Nothing certain — width alone does not fix that', "correct": True},
                {"text": 'It must be far older, since width takes time to match', "correct": False, "why": "A galaxy's width is not a simple clock for its age; many factors shape how large it grows."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s25',
            "band": 'standard',
            "text": "The Sun's hydrogen dates back to the Big Bang, but the iron inside Earth was forged inside earlier stars. What does that show about the two elements?",
            "options": [
                {"text": 'Iron is older, since heavier elements form first', "correct": False, "why": 'The order runs the other way: light elements formed first, and stars built the heavier ones after.'},
                {"text": 'Neither is older, since all elements share one age', "correct": False, "why": 'They do not share an origin date; hydrogen is far older than iron.'},
                {"text": 'Both formed at exactly the same moment, together', "correct": False, "why": 'Only hydrogen and a little helium formed that early; iron needed stars to exist first.'},
                {"text": "Hydrogen dates to the universe's start; iron needed stars first", "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s26',
            "band": 'standard',
            "text": "Why does calling a galaxy a 'barred spiral' say more than just calling it 'roughly round'?",
            "options": [
                {"text": 'It names a real structure — a bar with spiral arms', "correct": True},
                {"text": 'It says the galaxy has no measurable width', "correct": False, "why": 'A barred spiral is a shape description, not a claim about having no size.'},
                {"text": 'It says every galaxy shares this exact same shape', "correct": False, "why": 'Galaxies come in several shapes; naming one marks it out from the others.'},
                {"text": 'It says the galaxy contains no gas between stars', "correct": False, "why": 'A barred spiral typically has plenty of gas along its arms; the term describes shape.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s27',
            "band": 'standard',
            "text": "A pupil argues the Milky Way is 'mostly empty space', so it cannot really hold two hundred billion stars. What is wrong with that reasoning?",
            "options": [
                {"text": 'The reasoning is sound, so the star count is wrong', "correct": False, "why": 'The star count is not the mistake; it is a well-measured, separate figure.'},
                {"text": 'Emptiness and a huge star count are not in conflict', "correct": True},
                {"text": "It is wrong because the Milky Way is not mostly empty space, contrary to the pupil's premise", "correct": False, "why": 'The galaxy genuinely is mostly empty space between stars; that part is correct.'},
                {"text": 'The claim of two hundred billion stars must be wrong', "correct": False, "why": 'Nothing in the reasoning shows the star count itself is wrong.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s28',
            "band": 'standard',
            "text": 'A chart plots five objects of wildly different sizes using a scale where each step is ten times the last. What would an ordinary straight-line scale do instead?',
            "options": [
                {"text": 'Show every object exactly as clearly, just spaced out differently', "correct": False, "why": 'The smallest bars would shrink to nothing next to the largest, not merely space out.'},
                {"text": 'Remove the Milky Way and Andromeda from the chart', "correct": False, "why": 'It is the SMALLEST objects that vanish on such a scale, not the largest.'},
                {"text": 'Shrink the smallest bars away to nothing', "correct": True},
                {"text": 'Leave the chart looking exactly the same either way', "correct": False, "why": 'The numbers stay the same, but their spacing on the chart depends on the scale chosen.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s29',
            "band": 'standard',
            "text": 'A newly forming star system is found to contain iron and gold. What does that show about the material it formed from?',
            "options": [
                {"text": 'It must be one of the very first systems to form', "correct": False, "why": 'Gold and iron show the opposite: this system formed relatively late, after earlier stars had died.'},
                {"text": 'The material can be traced back to the Big Bang and to nothing that happened afterwards', "correct": False, "why": 'The Big Bang produced little beyond hydrogen; both elements needed events long afterwards.'},
                {"text": 'The material formed the instant the star itself came together, all in one moment', "correct": False, "why": 'Iron and gold predate the new system; earlier stars made them long before it formed.'},
                {"text": 'It came from remains of earlier stars, not plain hydrogen alone', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-s30',
            "band": 'standard',
            "text": "Andromeda is described as roughly twice the Milky Way's width but only about five times its star count. What does that suggest about the two galaxies?",
            "options": [
                {"text": "Andromeda's stars must be packed more tightly, given how the two figures compare", "correct": True},
                {"text": 'The two figures must contradict each other', "correct": False, "why": 'Width and star count are two separate measurements with no rule forcing the same ratio.'},
                {"text": 'Width and star count are simply unrelated numbers for any galaxy anyone might study', "correct": False, "why": 'They are not unrelated in general; here the figures do suggest something about packing.'},
                {"text": "Andromeda's stars are spread more thinly, matching its extra width exactly", "correct": False, "why": 'Doubling the width of a disc gives four times the area, and five times the stars in four times the area is tighter packing, not thinner.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h10',
            "band": 'harder',
            "text": "A pupil argues: 'The Sun is halfway through its life, so in another 4.6 billion years it will look and behave exactly as it does today.' What is the flaw?",
            "options": [
                {"text": 'Halfway through says nothing about how it changes as fuel runs low', "correct": True},
                {"text": 'The lifetime estimate rests on no real evidence', "correct": False, "why": "The estimate rests on how fast a star of the Sun's mass burns through fuel — the flaw lies elsewhere."},
                {"text": 'The Sun is not halfway through its life', "correct": False, "why": '4.6 billion out of about ten billion years genuinely is close to the midpoint.'},
                {"text": 'Stars stay the same for their whole lives', "correct": False, "why": 'Stars change substantially as fuel runs down, especially near the end of their lives.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h11',
            "band": 'harder',
            "text": "The Sun has completed roughly twenty orbits of the Milky Way's centre in 4.6 billion years. What does that imply about a galactic orbit compared with an Earth year?",
            "options": [
                {"text": 'A galactic orbit lasts exactly twenty Earth years', "correct": False, "why": 'Twenty is the NUMBER OF ORBITS, not the length of one orbit in years.'},
                {"text": 'A galactic orbit lasts roughly 230 million Earth years', "correct": True},
                {"text": 'A galactic orbit is a similar length to an Earth year', "correct": False, "why": 'An Earth year is roughly 230 million times shorter than one galactic orbit.'},
                {"text": 'The two kinds of orbit are not really comparable', "correct": False, "why": 'Both are orbits with a definite period, so their lengths compare directly.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h12',
            "band": 'harder',
            "text": "A pupil says the Milky Way cannot be 'mostly empty space' if a supermassive black hole sits at its centre. Why is that reasoning wrong?",
            "options": [
                {"text": 'A galaxy with a black hole in it is no longer really a galaxy', "correct": False, "why": 'A central black hole is normal for large spiral galaxies; it does not change what counts as one.'},
                {"text": 'The black hole does not sit at the true centre', "correct": False, "why": "The black hole genuinely sits at the galaxy's centre; the objection fails for a different reason."},
                {"text": 'A black hole is still tiny beside the gaps between stars', "correct": True},
                {"text": 'Mass and emptiness cannot both describe one object', "correct": False, "why": 'They are not in conflict: a small massive object can sit inside an overwhelmingly empty structure.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h13',
            "band": 'harder',
            "text": "Andromeda's faint smudge of light was once assumed to be a nearby gas cloud inside the Milky Way. What kind of evidence was needed to overturn that assumption?",
            "options": [
                {"text": 'Proof that the smudge contained hydrogen', "correct": False, "why": 'Both a gas cloud and a galaxy of stars show hydrogen; that alone settles nothing.'},
                {"text": 'A brighter photograph, taken with a stronger telescope', "correct": False, "why": 'A brighter image alone does not settle distance; the distance measurement did.'},
                {"text": 'A vote among astronomers on the better explanation', "correct": False, "why": 'Questions like this are settled by measurement, not by a vote on which idea sounds better.'},
                {"text": 'A distance measurement, placing it far beyond the Milky Way', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h14',
            "band": 'harder',
            "text": 'A rocky planet orbits a star that contains iron and gold. What does that imply about stars existing before this system formed?',
            "options": [
                {"text": 'An earlier star must have lived and scattered heavier elements', "correct": True},
                {"text": 'The planet made these elements itself, later on', "correct": False, "why": 'A rocky planet has no fusion process; it simply collects elements already present.'},
                {"text": 'This system must be one of the first to have formed', "correct": False, "why": 'Gold and iron show the opposite: this system formed late, after earlier stars had already died.'},
                {"text": "The star's own fusion made every element by itself", "correct": False, "why": "An ordinary star's fusion stops at iron; gold needs a far more violent earlier event."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h15',
            "band": 'harder',
            "text": 'A pupil claims that because Proxima Centauri gives out so little light, it must be a young star still warming up. Why is that reasoning flawed?',
            "options": [
                {"text": 'Stars do not really have an age to speak of', "correct": False, "why": 'Stars do have well-defined ages; the flaw is linking dimness specifically to youth.'},
                {"text": 'Its size and mass set brightness, not its age', "correct": True},
                {"text": 'A red dwarf cannot really be as dim as claimed', "correct": False, "why": 'Red dwarfs genuinely are among the dimmest true stars; the flaw is elsewhere.'},
                {"text": 'The dimmest stars are, as a rule, the youngest ones', "correct": False, "why": 'Dimness is not a sign of youth; a small star stays dim throughout a long life.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h16',
            "band": 'harder',
            "text": 'Two stars share the same surface temperature and colour. One is a red supergiant, one a red dwarf. What must differ between them?',
            "options": [
                {"text": 'One of the two class names must simply be wrong', "correct": False, "why": 'Both really are red-coloured stars; a supergiant and a dwarf can share that colour.'},
                {"text": 'Nothing else can differ, once colour matches', "correct": False, "why": 'Colour reveals temperature alone; two very different-sized stars can still share it.'},
                {"text": 'Their sizes and total light output differ hugely', "correct": True},
                {"text": 'Their basic chemical make-up, quite dramatically', "correct": False, "why": 'Both are still mostly hydrogen and helium, like nearly every star.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h17',
            "band": 'harder',
            "text": "A newly found galaxy is roughly Andromeda's width but with about a fifth of its star count. What does that suggest, compared with Andromeda?",
            "options": [
                {"text": 'It cannot really be a galaxy, holding so few stars', "correct": False, "why": "A galaxy is defined by a bound collection of stars, not by matching another one's count."},
                {"text": 'The star count must simply be a mistake', "correct": False, "why": 'Similar-width galaxies need not share a star count; packing can genuinely differ.'},
                {"text": 'It must in truth be smaller than Andromeda', "correct": False, "why": 'The width has been measured and matches; the star count is the real difference to explain.'},
                {"text": 'Its stars must be spread more thinly for that width', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h18',
            "band": 'harder',
            "text": 'The heaviest elements form mainly in collisions between neutron stars, themselves the collapsed remains of exploded stars. What does that set as a minimum age for the gold on Earth?',
            "options": [
                {"text": 'Older than the Sun — needing earlier stars to live, explode and collide', "correct": True},
                {"text": 'Exactly the age of the universe, since gold has existed since the Big Bang', "correct": False, "why": 'Gold did not exist at the Big Bang; only hydrogen and a little helium did.'},
                {"text": 'No older than the Sun, since it formed alongside the rest of the solar system', "correct": False, "why": 'It has to be older: it was already present in the material the solar system formed from.'},
                {"text": 'This information cannot set any minimum age', "correct": False, "why": "The chain of events described sets a clear lower bound on the gold's age."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h19',
            "band": 'harder',
            "text": "A pupil argues: 'The Milky Way is 100 000 light years across and Andromeda is 200 000, so Andromeda must have twice the stars.' What is wrong with that step?",
            "options": [
                {"text": "Andromeda is not really twice the Milky Way's width", "correct": False, "why": 'The widths given are accepted as roughly right; the flaw is elsewhere in the step.'},
                {"text": 'Star count does not scale simply with width', "correct": True},
                {"text": 'Doubling the width should double the star count, as a general rule for any galaxy', "correct": False, "why": "Andromeda holds roughly five times the Milky Way's stars for double the width, not two times."},
                {"text": 'Galaxy star counts are not the kind of thing that can be sensibly compared', "correct": False, "why": 'Star counts compare perfectly well; the flaw is assuming a fixed simple ratio to width.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h20',
            "band": 'harder',
            "text": "The Sun sits about halfway out from the galaxy's centre, and that DISTANCE stays roughly fixed. Explain why its position relative to the centre still keeps changing.",
            "options": [
                {"text": "The distance changes a great deal year to year, unlike the question's own premise", "correct": False, "why": 'Over a human lifetime the distance is effectively fixed; the premise given holds.'},
                {"text": 'The black hole itself drifts around the galaxy', "correct": False, "why": 'It is the Sun doing the orbiting here, around a centre that anchors the rotation.'},
                {"text": 'The Sun keeps orbiting, so its DIRECTION from the centre keeps sweeping round', "correct": True},
                {"text": 'Its relationship to the centre is completely fixed', "correct": False, "why": 'An orbit means the direction from the centre steadily changes, even at a fixed distance.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h21',
            "band": 'harder',
            "text": 'Red dwarfs like Proxima Centauri are the dimmest true stars known. What follows about how common they are?',
            "options": [
                {"text": 'They are just as rare as bright supergiants', "correct": False, "why": 'Star types are not equally frequent; some kinds vastly outnumber others.'},
                {"text": 'They must be the rarest kind, since faintness suggests few exist', "correct": False, "why": "Dimness is a property of a star's output, not a count of how many exist."},
                {"text": 'Brightness and how common a type is cannot ever be compared', "correct": False, "why": 'They can be compared, and here they point opposite ways: dim, yet extremely numerous.'},
                {"text": 'They are, despite that, the most common kind of star in the galaxy', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h22',
            "band": 'harder',
            "text": 'An axis is marked 1, 10, 100, 1000, 10 000 and 100 000, each mark the same distance from the next. Is that a logarithmic or a straight-line scale?',
            "options": [
                {"text": 'Logarithmic, since each mark is ten times the last', "correct": True},
                {"text": 'It depends on what is being measured', "correct": False, "why": 'The pattern of the numbers alone identifies it, whatever quantity is being measured.'},
                {"text": 'Straight-line, since the labels rise by equal steps', "correct": False, "why": 'The labels rise by equal MULTIPLES — ten times at every step — not by equal amounts, and that is what marks a log scale.'},
                {"text": 'Neither — a real scale shows every value in between', "correct": False, "why": 'Skipping values in between is normal for either kind; the pattern shown decides the type.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h23',
            "band": 'harder',
            "text": 'A distant moon around another planet is so far off that even a large telescope shows only a single point of light, like a star. Would that point still twinkle?',
            "options": [
                {"text": 'Yes, but that is simply because moons sit closer than any star does', "correct": False, "why": 'Distance from Earth is not deciding this; appearing as a point source is what causes the twinkle.'},
                {"text": 'Yes — a point source of light gets shifted about by moving air', "correct": True},
                {"text": "No — reflected light cannot be disturbed by moving air the way a star's can", "correct": False, "why": 'The atmosphere disturbs light on the way to your eye regardless of where it first came from.'},
                {"text": 'No — twinkling is a property true stars alone show', "correct": False, "why": 'Twinkling is caused by our own atmosphere acting on a point source, not by being a star.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h24',
            "band": 'harder',
            "text": 'Which had to happen first: a massive star exploding and scattering carbon into space, or that carbon becoming part of a living thing?',
            "options": [
                {"text": 'Neither — both happen at the same universal moment', "correct": False, "why": 'These events are separated by enormous stretches of time and space, not one moment.'},
                {"text": 'The order between them cannot be known', "correct": False, "why": 'The order follows directly from what each event needs: release before uptake.'},
                {"text": 'The explosion, since the carbon must exist first', "correct": True},
                {"text": 'The living thing, since life triggers a star to explode', "correct": False, "why": "Living things have no influence on a distant star's explosion; the causal order runs the other way."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h25',
            "band": 'harder',
            "text": 'A newly studied star is found to hold almost no elements heavier than helium. What does that suggest about when it formed?',
            "options": [
                {"text": "It must share the Sun's exact formation time", "correct": False, "why": 'Stars forming at different times draw on different mixtures, as heavier elements build up over time.'},
                {"text": 'Very recently, since young stars lack time to build up heavier elements', "correct": False, "why": 'A star forms from material already scattered nearby; it does not build elements just by existing.'},
                {"text": 'This tells you nothing about when it formed', "correct": False, "why": "The mix of elements present is exactly the kind of clue astronomers use to judge a star's age."},
                {"text": 'Very early, before earlier stars had scattered heavier elements', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h26',
            "band": 'harder',
            "text": "Suppose a spacecraft crossed the galaxy in a straight line, passing a star roughly every four light years. Roughly how many stars would it pass crossing the Milky Way's full 100 000-light-year width?",
            "options": [
                {"text": 'About 25 000 stars', "correct": True},
                {"text": 'About 4, the spacing figure itself', "correct": False, "why": 'That is just the spacing given, not how many times it fits across the whole width.'},
                {"text": 'About 2 500 000 stars', "correct": False, "why": 'That is a hundred times too many — 100 000 shared out in fours cannot come to more than 25 000.'},
                {"text": 'About 400 stars, roughly', "correct": False, "why": 'That divides 100 000 by 250 rather than by four, far too small a result.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h27',
            "band": 'harder',
            "text": "Everything astronomers could see was once assumed to be the whole universe, until Andromeda proved otherwise. What general lesson does that suggest for today's estimate of two trillion galaxies?",
            "options": [
                {"text": 'That mistake could not happen again in any new form', "correct": False, "why": 'Mistaking the limits of current observation for the limits of reality could happen again.'},
                {"text": "Today's estimate may need revising as observation improves", "correct": True},
                {"text": 'The current estimate should be treated as final', "correct": False, "why": 'The Andromeda story shows the opposite: treating a picture as complete was the earlier mistake.'},
                {"text": 'Nothing can be known about the universe with any confidence', "correct": False, "why": 'Plenty is known with good confidence; the point is about staying open to revision.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h28',
            "band": 'harder',
            "text": "The Sun is about 1.4 million km across, and Neptune's orbit about 9 billion km across. Roughly how many Suns, lined up edge to edge, would span Neptune's orbit?",
            "options": [
                {"text": 'About 6.5 Suns', "correct": False, "why": 'That treats the two distances as almost equal, when one is thousands of times the other.'},
                {"text": 'About 650 000 Suns', "correct": False, "why": 'That divides by 14 000 km rather than 1.4 million km, a hundred times too many.'},
                {"text": 'About 6500 Suns', "correct": True},
                {"text": 'About 65 Suns', "correct": False, "why": 'That divides by 140 million rather than 1.4 million, a hundred times too few.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h29',
            "band": 'harder',
            "text": 'Betelgeuse is far more massive than the Sun yet shines a cooler red, while the Sun shines a hotter yellow-white. Explain why greater mass does not mean a hotter surface here.',
            "options": [
                {"text": 'The Sun must be the more massive of the two stars', "correct": False, "why": 'The Sun is far less massive than Betelgeuse; being hotter does not require more mass.'},
                {"text": 'Colour has no link to temperature for any star', "correct": False, "why": 'Colour is a real guide to temperature; the issue is that mass alone does not fix it.'},
                {"text": 'Betelgeuse cannot be more massive than the Sun, given how much cooler it shines', "correct": False, "why": 'Betelgeuse genuinely is far more massive; the flaw is assuming mass alone sets temperature.'},
                {"text": "Colour depends on a star's stage of life, not mass alone", "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-04-h30',
            "band": 'harder',
            "text": 'Stars P and Q sit the same distance from Earth. P looks far brighter than Q. A pupil concludes P is the more massive star. What is the gap in that reasoning?',
            "options": [
                {"text": 'Brightness depends on more than mass, so it cannot prove which star is more massive', "correct": True},
                {"text": 'The two stars are not, in truth, the same distance from Earth as the question claims', "correct": False, "why": 'The question fixes the distance as equal; the gap lies in what brightness alone can prove.'},
                {"text": 'At equal distance, the brighter star must be the more massive one of the pair', "correct": False, "why": 'Output depends on more than mass, so equal distance does not settle mass by itself.'},
                {"text": 'Brightness at equal distance says nothing whatsoever about either star', "correct": False, "why": 'It does tell you P gives out more light than Q; it simply cannot prove greater mass.'},
            ],
            "figure": None,
        },
]
