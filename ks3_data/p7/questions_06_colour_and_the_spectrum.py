"""P7 lesson 06 — Colour and the spectrum: twelve questions (MRB-223).

Written against Design's page. The prism hook, the ray-box bench with its
second prism and the spectrum band are hers.

The discriminations, in the order the lesson builds them:

  · the prism SORTS what was already there (`LIGHT-21`);
  · the spectrum is continuous and the names are ours (`LIGHT-22`);
  · higher frequency means a BIGGER bend, not a smaller one
    (`LIGHT-23`);
  · the effect happens in the body of the glass, not at a coloured edge
    (`LIGHT-24`) — the harder band sits here.

⚠️ HER FLAG 10 IS HONOURED IN THE BANK TOO: every question here is
answerable from the WORDS alone. No option depends on seeing a hue.

⚠️ POSITION IS AUTHORED — 1,3,2,0 · 0,2,1,3 · 2,1,3,0, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. This lesson has no
worked example: the statute says "qualitative only" in terms.
"""

UNIT = "P7"
LESSON = "colour-and-the-spectrum"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-06-e01",
        "band": "easier",
        "text": "White light is…",
        "options": [
            {"text": "a colour of its own, made by the Sun",
             "correct": False,
             "why": "It is not one colour. A prism separates it into every "
                    "visible frequency."},
            {"text": "a mixture of light of every visible frequency",
             "correct": True},
            {"text": "light with no frequency at all", "correct": False,
             "why": "Every light wave has a frequency. White light has all "
                    "of the visible ones at once."},
            {"text": "light that has had its colours removed",
             "correct": False,
             "why": "Removing colours is what a filter does, and it leaves "
                    "you with a colour rather than white."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e02",
        "band": "easier",
        "text": "The fanning apart of the colours by a prism is called…",
        "options": [
            {"text": "reflection", "correct": False,
             "why": "Reflection is light bouncing back off a surface."},
            {"text": "absorption", "correct": False,
             "why": "Absorption is light being taken in and not coming out "
                    "again."},
            {"text": "scattering", "correct": False,
             "why": "Scattering sends rays in all directions at a rough "
                    "surface. A prism sorts them in an order."},
            {"text": "dispersion", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e03",
        "band": "easier",
        "text": "Which colour of visible light has the lowest frequency?",
        "options": [
            {"text": "Violet", "correct": False,
             "why": "Violet is at the other end: it has the highest visible "
                    "frequency."},
            {"text": "Green", "correct": False,
             "why": "Green sits in the middle of the band."},
            {"text": "Red", "correct": True},
            {"text": "White", "correct": False,
             "why": "White is not one frequency. It is all of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e04",
        "band": "easier",
        "text": "A second prism, the other way up, is put in the fanned-out "
                "beam. What lands on the screen?",
        "options": [
            {"text": "One white patch", "correct": True},
            {"text": "Twice as many colours", "correct": False,
             "why": "If glass made colour, a second piece would make more. "
                    "It does the opposite."},
            {"text": "Nothing at all", "correct": False,
             "why": "The light is not absorbed. It is put back together."},
            {"text": "The same band of colours, further apart",
             "correct": False,
             "why": "An inverted prism bends each colour BACK by the amount "
                    "the first one bent it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-06-s01",
        "band": "standard",
        "text": "Why does a prism separate the colours of white light?",
        "options": [
            {"text": "Because refraction depends slightly on frequency, so "
                     "the higher frequencies are bent a little further",
             "correct": True},
            {"text": "Because the glass adds a colour of its own to each "
                     "part of the beam as it goes through", "correct": False,
             "why": "Nothing is added. Send red light in on its own and red "
                    "comes out."},
            {"text": "Because the beam is split into parts by the two sharp "
                     "edges of the prism", "correct": False,
             "why": "The whole beam fans out, not just its edges, and it "
                    "happens in the body of the glass."},
            {"text": "Because each colour travels at a different speed "
                     "through the air on the far side, so they spread "
                     "apart", "correct": False,
             "why": "Air treats all the visible colours very nearly the "
                    "same. The separation happens in the glass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s02",
        "band": "standard",
        "text": "Only red light is sent into the prism. What comes out?",
        "options": [
            {"text": "A full band of colours, because a prism always makes "
                     "a spectrum", "correct": False,
             "why": "A prism sorts what arrives. With one colour arriving "
                    "there is nothing to sort."},
            {"text": "White light, because the colours recombine inside the "
                     "glass", "correct": False,
             "why": "You cannot get white out of red. Nothing is created."},
            {"text": "Red light, shifted sideways and not fanned out",
             "correct": True},
            {"text": "Nothing, because red is bent least and misses the "
                     "screen", "correct": False,
             "why": "Being bent least still means being bent. It lands on "
                    "the screen like any other colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s03",
        "band": "standard",
        "text": "Blue and red light together are sent into a prism. What "
                "appears on the screen?",
        "options": [
            {"text": "A full spectrum, because the prism fills in the "
                     "missing colours", "correct": False,
             "why": "Nothing appears that was not sent in. There are no "
                    "yellows or greens in the beam to separate out."},
            {"text": "Two separated patches, with the red bent less than "
                     "the blue", "correct": True},
            {"text": "One purple patch, because blue and red mix",
             "correct": False,
             "why": "The prism separates rather than mixes, so the two "
                    "arrive in different places."},
            {"text": "Two separated patches, with the blue bent less than "
                     "the red", "correct": False,
             "why": "Blue has the higher frequency of the two, so it is "
                    "bent MORE."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s04",
        "band": "standard",
        "text": "Which statement about the visible spectrum is right?",
        "options": [
            {"text": "It has exactly seven separate colours, with a sharp "
                     "boundary between each pair", "correct": False,
             "why": "Seven is a historical count. There are no boundaries "
                    "anywhere in it."},
            {"text": "It is a set of six separate kinds of light, one for "
                     "each of the names", "correct": False,
             "why": "The six names are labels along one continuous band, "
                    "not six different things."},
            {"text": "It runs from violet at the lowest frequency up to red "
                     "at the very highest", "correct": False,
             "why": "That is the right band the wrong way round: red is the "
                    "lowest visible frequency and violet the highest."},
            {"text": "It changes smoothly, and the names are places along "
                     "it rather than separate things", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-06-h01",
        "band": "harder",
        "text": "Newton put a card with a small hole in the fanned beam so "
                "that only the green part passed on to a second prism. The "
                "green came out green. What did that show?",
        "options": [
            {"text": "That green light is a mixture of the other colours, "
                     "waiting to be separated by a second prism",
             "correct": False,
             "why": "If it were, the second prism would have separated it "
                    "and it did not."},
            {"text": "That a prism only works on white light",
             "correct": False,
             "why": "It refracts every colour. It simply has nothing to "
                    "separate when one colour arrives."},
            {"text": "That the colours in the fanned beam are not mixtures "
                     "and cannot be broken down further", "correct": True},
            {"text": "That the second prism was faulty", "correct": False,
             "why": "It behaved exactly as the first one did. The result is "
                    "the finding, not a fault."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h02",
        "band": "harder",
        "text": "Radio waves, visible light and X-rays are all the same "
                "kind of wave. What separates them?",
        "options": [
            {"text": "Their speed in a vacuum, which rises from radio to "
                     "X-rays", "correct": False,
             "why": "All of them travel at 300 000 000 m/s in a vacuum. "
                    "That is one of the things that makes them one family."},
            {"text": "Their frequency, and nothing else", "correct": True},
            {"text": "Whether they need a material to travel through",
             "correct": False,
             "why": "None of them needs one. All cross a vacuum."},
            {"text": "Whether they are transverse or longitudinal",
             "correct": False,
             "why": "All of them are transverse."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h03",
        "band": "harder",
        "text": "A rainbow always has red on the outside of the arc and "
                "violet on the inside, in every rainbow anybody has ever "
                "seen. Why is the order fixed?",
        "options": [
            {"text": "Because raindrops always fall in the same "
                     "arrangement", "correct": False,
             "why": "Raindrops fall at random. Each one acts on its own."},
            {"text": "Because the Sun is always in the same place relative "
                     "to a rainbow, and that fixes which colour lands on "
                     "top", "correct": False,
             "why": "That is why you see one at all — it does not decide "
                    "which colour ends up where."},
            {"text": "Because the eye always sorts colours into that order",
             "correct": False,
             "why": "The eye reports what arrives. The sorting happened in "
                    "the water."},
            {"text": "Because the order follows frequency, which is a "
                     "property of the light and does not vary from drop to "
                     "drop", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h04",
        "band": "harder",
        "text": "A thin film of oil on a wet road shows bands of colour, "
                "and no prism is involved. What does that tell you about "
                "the colours in white light?",
        "options": [
            {"text": "That white light contains them all along, and more "
                     "than one arrangement can separate them",
             "correct": True},
            {"text": "That the oil is coloured to begin with, and the water "
                     "washes it out into separate bands", "correct": False,
             "why": "The same oil in a bottle is not coloured. It is the "
                    "thin film that does it."},
            {"text": "That oil turns white light into coloured light as the "
                     "light passes through it", "correct": False,
             "why": "That would be making colour, which nothing does. The "
                    "colours were in the light already."},
            {"text": "That the road itself is reflecting different colours "
                     "from different places on it", "correct": False,
             "why": "The bands move when you move, so they are not "
                    "properties of particular spots on the road."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-06-e05",
        "band": "easier",
        "text": "Which colour of visible light has the highest frequency?",
        "options": [
            {"text": "Red", "correct": False,
             "why": "Red is at the LOW-frequency end of the visible range."},
            {"text": "Green", "correct": False,
             "why": "Green sits in the middle; there are higher frequencies "
                    "beyond it."},
            {"text": "Violet", "correct": True},
            {"text": "White", "correct": False,
             "why": "White is not one frequency at all — it is a mixture of "
                    "all of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e06",
        "band": "easier",
        "text": "A prism separates the colours of white light because…",
        "options": [
            {"text": "it adds a different colour at each face",
             "correct": False,
             "why": "It adds nothing; a second prism turns the colours back "
                    "into white."},
            {"text": "higher frequencies are refracted a little more than "
                     "lower ones",
             "correct": True},
            {"text": "lower frequencies are refracted a little more than "
                     "higher ones",
             "correct": False,
             "why": "That is the wrong way round: violet is bent further than "
                    "red."},
            {"text": "the coloured edges of the glass tint the beam",
             "correct": False,
             "why": "The glass is clear throughout, and a clear prism gives "
                    "the same spectrum."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e07",
        "band": "easier",
        "text": "The band of colours a prism throws onto a screen is called "
                "a…",
        "options": [
            {"text": "reflection", "correct": False,
             "why": "Reflection is light bouncing off a surface, not the "
                    "fanned-out band."},
            {"text": "spectrum", "correct": True},
            {"text": "normal", "correct": False,
             "why": "The normal is the construction line at right angles to a "
                    "surface."},
            {"text": "filter", "correct": False,
             "why": "A filter removes some frequencies; the band itself is "
                    "the spectrum."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-06-s05",
        "band": "standard",
        "text": "Only green light is shone into a prism. What comes out?",
        "options": [            {"text": "A full spectrum, because a prism always makes one",
             "correct": False,
             "why": "It can only separate what is there, and only one "
                    "frequency has been sent in."},
            {"text": "White light, because the colours recombine",
             "correct": False,
             "why": "Recombining needs all the frequencies, and only green "
                    "was supplied."},
            {"text": "Nothing, because a prism only works on white light",
             "correct": False,
             "why": "It refracts any light that enters it, whatever its "
                    "colour."},
            {"text": "Green light, bent as a single beam", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s06",
        "band": "standard",
        "text": "Why does violet land furthest from where the undeviated beam "
                "would have gone?",
        "options": [
            {"text": "Because it is the highest frequency, so it is refracted "
                     "most",
             "correct": True},
            {"text": "Because it is the lowest frequency, so it is refracted "
                     "most",
             "correct": False,
             "why": "Violet is the highest visible frequency, and red the "
                    "lowest."},
            {"text": "Because it carries the least energy of the colours",
             "correct": False,
             "why": "Higher frequencies carry more, and in any case it is the "
                    "refraction that places it."},
            {"text": "Because it enters the prism at a different angle from "
                     "the rest",
             "correct": False,
             "why": "All the colours arrive together at the same angle; they "
                    "part inside the glass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s07",
        "band": "standard",
        "text": "A second prism the other way up turns the fanned beam back "
                "into white. What does that show?",
        "options": [
            {"text": "That the second prism removes the colours",
             "correct": False,
             "why": "Nothing is removed; the frequencies are brought back "
                    "together and arrive as a mixture."},
            {"text": "That white light is a mixture and the prism only sorts "
                     "it",
             "correct": True},
            {"text": "That the first prism made colours and the second "
                     "destroyed them",
             "correct": False,
             "why": "Neither makes nor destroys anything; both simply refract "
                    "what arrives."},
            {"text": "That a prism works only in one direction",
             "correct": False,
             "why": "Both prisms refract in the same way; it is their "
                    "orientation that recombines the beam."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-06-h05",
        "band": "harder",
        "text": "Why is a spectrum a continuous band rather than seven "
                "separate stripes?",
        "options": [
            {"text": "Because the screen is too rough to show the gaps",
             "correct": False,
             "why": "A better screen shows the same continuous band; there "
                    "are no gaps to reveal."},
            {"text": "Because seven colours overlap and fill the spaces "
                     "between them",
             "correct": False,
             "why": "There are not seven underlying colours; the frequencies "
                    "run smoothly from end to end."},
            {"text": "Because the frequencies change smoothly, and the seven "
                     "names are a convention",
             "correct": True},
            {"text": "Because the prism cannot separate the colours "
                     "completely",
             "correct": False,
             "why": "It separates them perfectly well; there is simply no "
                    "natural place to draw a line."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h06",
        "band": "harder",
        "text": "A second prism is placed the SAME way up as the first, in "
                "the fanned beam. What happens?",
        "options": [
            {"text": "The colours recombine into white", "correct": False,
             "why": "Recombining needs the second prism turned the other way "
                    "up, so that it bends the colours back together."},
            {"text": "The spectrum spreads further apart", "correct": True},
            {"text": "The beam passes through unchanged", "correct": False,
             "why": "It refracts every frequency again, so the beam cannot "
                    "come out unaltered."},
            {"text": "The order of the colours is reversed", "correct": False,
             "why": "Violet is bent most by both prisms, so it stays at the "
                    "same end of the band."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h07",
        "band": "harder",
        "text": "Why can a prism never produce a colour that was not in the "
                "light to begin with?",
        "options": [
            {"text": "Because a prism only separates the frequencies already "
                     "arriving",
             "correct": True},
            {"text": "Because glass can only bend certain colours",
             "correct": False,
             "why": "It refracts every frequency; the amount simply differs "
                    "between them."},
            {"text": "Because the prism absorbs any colour it cannot bend",
             "correct": False,
             "why": "Very little is absorbed, and nothing is filtered out by "
                    "the shape of the glass."},
            {"text": "Because a prism can only work once on any beam",
             "correct": False,
             "why": "A second prism refracts the beam again quite happily, as "
                    "the recombining experiment shows."},
        ],
        "figure": None,
    },
]
