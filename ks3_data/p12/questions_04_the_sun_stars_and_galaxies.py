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
]
