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
    {
        "id": "p7-06-e01",
        "band": "easier",
        "text": "White light is…",
        "options": [
            {"text": "a colour of its own, made by the Sun", "correct": False,
             "why": "It is not one colour. A prism separates it into every "
             "visible frequency."},
            {"text": "a mixture of light of every visible frequency", "correct": True},
            {"text": "light with no frequency at all", "correct": False,
             "why": "Every light wave has a frequency. White light has all of "
             "the visible ones at once."},
            {"text": "light that has had its colours removed", "correct": False,
             "why": "Removing colours is what a filter does, and it leaves you "
             "with a colour rather than white."},
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
             "why": "If glass made colour, a second piece would make more. It "
             "does the opposite."},
            {"text": "Nothing at all", "correct": False,
             "why": "The light is not absorbed. It is put back together."},
            {"text": "The same band of colours, further apart", "correct": False,
             "why": "An inverted prism bends each colour BACK by the amount "
             "the first one bent it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s01",
        "band": "standard",
        "text": "Why does a prism separate the colours of white light?",
        "options": [
            {"text": "Because refraction depends slightly on frequency, so the "
             "higher frequencies are bent a little further",
             "correct": True},
            {"text": "Because the glass adds a colour of its own to each part "
             "of the beam as it goes through",
             "correct": False,
             "why": "Nothing is added. Send red light in on its own and red "
             "comes out."},
            {"text": "Because the beam is split into parts by the two sharp "
             "edges of the prism",
             "correct": False,
             "why": "The whole beam fans out, not just its edges, and it "
             "happens in the body of the glass."},
            {"text": "Because each colour travels at a different speed through "
             "the air on the far side, so they spread apart",
             "correct": False,
             "why": "Air treats all the visible colours very nearly the same. "
             "The separation happens in the glass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s02",
        "band": "standard",
        "text": "Only red light is sent into the prism. What comes out?",
        "options": [
            {"text": "A full band of colours, because a prism always makes a "
             "spectrum",
             "correct": False,
             "why": "A prism sorts what arrives. With one colour arriving "
             "there is nothing to sort."},
            {"text": "White light, because the colours recombine inside the "
             "glass",
             "correct": False,
             "why": "You cannot get white out of red. Nothing is created."},
            {"text": "Red light, shifted sideways and not fanned out", "correct": True},
            {"text": "Nothing, because red is bent least and misses the screen", "correct": False,
             "why": "Being bent least still means being bent. It lands on the "
             "screen like any other colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s03",
        "band": "standard",
        "text": "Blue and red light together are sent into a prism. What "
                 "appears on the screen?",
        "options": [
            {"text": "A full spectrum, because the prism fills in the missing "
             "colours",
             "correct": False,
             "why": "Nothing appears that was not sent in. There are no "
             "yellows or greens in the beam to separate out."},
            {"text": "Two separated patches, with the red bent less than the "
             "blue",
             "correct": True},
            {"text": "One purple patch, because blue and red mix", "correct": False,
             "why": "The prism separates rather than mixes, so the two arrive "
             "in different places."},
            {"text": "Two separated patches, with the blue bent less than the "
             "red",
             "correct": False,
             "why": "Blue has the higher frequency of the two, so it is bent "
             "MORE."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s04",
        "band": "standard",
        "text": "Which statement about the visible spectrum is right?",
        "options": [
            {"text": "It has exactly seven separate colours, with a sharp "
             "boundary between each pair",
             "correct": False,
             "why": "Seven is a historical count. There are no boundaries "
             "anywhere in it."},
            {"text": "It is a set of six separate kinds of light, one for each "
             "of the names",
             "correct": False,
             "why": "The six names are labels along one continuous band, not "
             "six different things."},
            {"text": "It runs from violet at the lowest frequency up to red at "
             "the very highest",
             "correct": False,
             "why": "That is the right band the wrong way round: red is the "
             "lowest visible frequency and violet the highest."},
            {"text": "It changes smoothly, and the names are places along it "
             "rather than separate things",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h01",
        "band": "harder",
        "text": "Newton put a card with a small hole in the fanned beam so "
                 "that only the green part passed on to a second prism. The green came "
                 "out green. What did that show?",
        "options": [
            {"text": "That green light is a mixture of the other colours, "
             "waiting to be separated by a second prism",
             "correct": False,
             "why": "If it were, the second prism would have separated it and "
             "it did not."},
            {"text": "That a prism only works on white light", "correct": False,
             "why": "It refracts every colour. It simply has nothing to "
             "separate when one colour arrives."},
            {"text": "That the colours in the fanned beam are not mixtures and "
             "cannot be broken down further",
             "correct": True},
            {"text": "That the second prism was faulty", "correct": False,
             "why": "It behaved exactly as the first one did. The result is "
             "the finding, not a fault."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h02",
        "band": "harder",
        "text": "Radio waves, visible light and X-rays are all the same kind "
                 "of wave. What separates them?",
        "options": [
            {"text": "Their speed in a vacuum, which rises from radio to X-rays", "correct": False,
             "why": "All of them travel at 300 000 000 m/s in a vacuum. That "
             "is one of the things that makes them one family."},
            {"text": "Their frequency, and nothing else", "correct": True},
            {"text": "Whether they need a material to travel through", "correct": False,
             "why": "None of them needs one. All cross a vacuum."},
            {"text": "Whether they are transverse or longitudinal", "correct": False,
             "why": "All of them are transverse."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h03",
        "band": "harder",
        "text": "A rainbow always has red on the outside of the arc and violet "
                 "on the inside, in every rainbow anybody has ever seen. Why is the "
                 "order fixed?",
        "options": [
            {"text": "Because raindrops always fall in the same arrangement", "correct": False,
             "why": "Raindrops fall at random. Each one acts on its own."},
            {"text": "Because the Sun is always in the same place relative to a "
             "rainbow, and that fixes which colour lands on top",
             "correct": False,
             "why": "That is why you see one at all — it does not decide which "
             "colour ends up where."},
            {"text": "Because the eye always sorts colours into that order", "correct": False,
             "why": "The eye reports what arrives. The sorting happened in the "
             "water."},
            {"text": "Because the order follows frequency, which is a property "
             "of the light and does not vary from drop to drop",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h04",
        "band": "harder",
        "text": "A thin film of oil on a wet road shows bands of colour, and "
                 "no prism is involved. What does that tell you about the colours in "
                 "white light?",
        "options": [
            {"text": "That white light contains them all along, and more than "
             "one arrangement can separate them",
             "correct": True},
            {"text": "That the oil is coloured to begin with, and the water "
             "washes it out into separate bands",
             "correct": False,
             "why": "The same oil in a bottle is not coloured. It is the thin "
             "film that does it."},
            {"text": "That oil turns white light into coloured light as the "
             "light passes through it",
             "correct": False,
             "why": "That would be making colour, which nothing does. The "
             "colours were in the light already."},
            {"text": "That the road itself is reflecting different colours from "
             "different places on it",
             "correct": False,
             "why": "The bands move when you move, so they are not properties "
             "of particular spots on the road."},
        ],
        "figure": None,
    },
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
            {"text": "it adds a different colour at each face", "correct": False,
             "why": "It adds nothing; a second prism turns the colours back "
             "into white."},
            {"text": "higher frequencies are refracted a little more than lower "
             "ones",
             "correct": True},
            {"text": "lower frequencies are refracted a little more than higher "
             "ones",
             "correct": False,
             "why": "That is the wrong way round: violet is bent further than "
             "red."},
            {"text": "the coloured edges of the glass tint the beam", "correct": False,
             "why": "The glass is clear throughout, and a clear prism gives "
             "the same spectrum."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e07",
        "band": "easier",
        "text": "The band of colours a prism throws onto a screen is called a…",
        "options": [
            {"text": "reflection", "correct": False,
             "why": "Reflection is light bouncing off a surface, not the "
             "fanned-out band."},
            {"text": "spectrum", "correct": True},
            {"text": "normal", "correct": False,
             "why": "The normal is the construction line at right angles to a "
             "surface."},
            {"text": "filter", "correct": False,
             "why": "A filter removes some frequencies; the band itself is the "
             "spectrum."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s05",
        "band": "standard",
        "text": "Only green light is shone into a prism. What comes out?",
        "options": [
            {"text": "A full spectrum, because a prism always makes one", "correct": False,
             "why": "It can only separate what is there, and only one "
             "frequency has been sent in."},
            {"text": "White light, because the colours recombine", "correct": False,
             "why": "Recombining needs all the frequencies, and only green was "
             "supplied."},
            {"text": "Nothing, because a prism only works on white light", "correct": False,
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
            {"text": "Because it carries the least energy of the colours", "correct": False,
             "why": "Higher frequencies carry more, and in any case it is the "
             "refraction that places it."},
            {"text": "Because it enters the prism at a different angle from the "
             "rest",
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
            {"text": "That the second prism removes the colours", "correct": False,
             "why": "Nothing is removed; the frequencies are brought back "
             "together and arrive as a mixture."},
            {"text": "That white light is a mixture and the prism only sorts it", "correct": True},
            {"text": "That the first prism made colours and the second "
             "destroyed them",
             "correct": False,
             "why": "Neither makes nor destroys anything; both simply refract "
             "what arrives."},
            {"text": "That a prism works only in one direction", "correct": False,
             "why": "Both prisms refract in the same way; it is their "
             "orientation that recombines the beam."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h05",
        "band": "harder",
        "text": "Why is a spectrum a continuous band rather than seven "
                 "separate stripes?",
        "options": [
            {"text": "Because the screen is too rough to show the gaps", "correct": False,
             "why": "A better screen shows the same continuous band; there are "
             "no gaps to reveal."},
            {"text": "Because seven colours overlap and fill the spaces between "
             "them",
             "correct": False,
             "why": "There are not seven underlying colours; the frequencies "
             "run smoothly from end to end."},
            {"text": "Because the frequencies change smoothly, and the seven "
             "names are a convention",
             "correct": True},
            {"text": "Because the prism cannot separate the colours completely", "correct": False,
             "why": "It separates them perfectly well; there is simply no "
             "natural place to draw a line."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h06",
        "band": "harder",
        "text": "A second prism is placed the SAME way up as the first, in the "
                 "fanned beam. What happens?",
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
            {"text": "Because glass can only bend certain colours", "correct": False,
             "why": "It refracts every frequency; the amount simply differs "
             "between them."},
            {"text": "Because the prism absorbs any colour it cannot bend", "correct": False,
             "why": "Very little is absorbed, and nothing is filtered out by "
             "the shape of the glass."},
            {"text": "Because a prism can only work once on any beam", "correct": False,
             "why": "A second prism refracts the beam again quite happily, as "
             "the recombining experiment shows."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e08",
        "band": "easier",
        "text": "Which colour of visible light sits exactly between yellow and "
                 "blue in the spectrum?",
        "options": [
            {"text": "Green", "correct": True},
            {"text": "Orange", "correct": False,
             "why": "Orange sits between red and yellow, at the other end of "
             "that section of the band."},
            {"text": "Violet", "correct": False,
             "why": "Violet is at the far high-frequency end, well past blue."},
            {"text": "Red", "correct": False,
             "why": "Red is at the far low-frequency end, well past yellow."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e09",
        "band": "easier",
        "text": "Which two colours in the spectrum sit next to each other?",
        "options": [
            {"text": "Yellow and green",
             "correct": True},
            {"text": "Red and blue",
             "correct": False,
             "why": "Several colours sit between red and blue in the band."},
            {"text": "Red and violet",
             "correct": False,
             "why": "Red and violet are at opposite ends of the whole band."},
            {"text": "Orange and blue",
             "correct": False,
             "why": "Yellow and green sit between orange and blue."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e10",
        "band": "easier",
        "text": "What is the vocabulary word for 'how many vibrations of a "
                 "wave arrive each second'?",
        "options": [
            {"text": "Dispersion", "correct": False,
             "why": "Dispersion is the fanning apart of colours, not a count "
             "of vibrations."},
            {"text": "Spectrum", "correct": False,
             "why": "A spectrum is the band of colours, not a measurement of "
             "vibration."},
            {"text": "Frequency", "correct": True},
            {"text": "Refraction", "correct": False,
             "why": "Refraction is the bending of light at a boundary, not a "
             "count of vibrations."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e11",
        "band": "easier",
        "text": "Two narrow beams of light look different colours, one red "
                "and one blue. Which property of the light do they differ "
                "in?",
        "options": [
            {"text": "How far it has travelled",
             "correct": False,
             "why": "Distance travelled does not change a light wave's "
             "frequency or its colour."},
            {"text": "How bright the source is",
             "correct": False,
             "why": "Brightness is about how much light there is, not which "
             "colour it is."},
            {"text": "Which prism it has passed through",
             "correct": False,
             "why": "A prism sorts colours that are already there; it does "
             "not decide what colour a frequency is."},
            {"text": "Its frequency",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e12",
        "band": "easier",
        "text": "A prism fans white light apart into a band of colours. "
                "Where does the fanning actually happen?",
        "options": [
            {"text": "In the air beyond the prism, once the colours have "
             "room to spread out",
             "correct": False,
             "why": "The colours are already travelling in different "
             "directions as they leave the glass; air treats all of them "
             "very nearly alike."},
            {"text": "At the two sharp edges of the prism, which is where "
             "the colours come off",
             "correct": False,
             "why": "The whole beam fans out, not only its edges, and the "
             "glass is colourless all the way through."},
            {"text": "On the screen, which sorts the colours as they land "
             "on it",
             "correct": False,
             "why": "A screen only shows where light arrives; the rays were "
             "already separated before they reached it."},
            {"text": "Inside the glass, where each frequency is slowed and "
             "bent by a different amount",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e13",
        "band": "easier",
        "text": "To recombine a fanned-out beam back into white light, how "
                "must the second prism be placed?",
        "options": [
            {"text": "The other way up",
             "correct": True},
            {"text": "The same way up as the first",
             "correct": False,
             "why": "That spreads the colours further apart instead of "
             "bringing them back together."},
            {"text": "At a right angle to the first",
             "correct": False,
             "why": "Turning the second prism upside down is what bends "
             "each colour back; turning it sideways does not."},
            {"text": "Its orientation makes no difference",
             "correct": False,
             "why": "Only turning it the other way up brings the colours "
             "back together."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e14",
        "band": "easier",
        "text": "Which colour sits immediately next to red, within the visible "
                 "spectrum?",
        "options": [
            {"text": "Yellow", "correct": False,
             "why": "Yellow is separated from red by orange."},
            {"text": "Green", "correct": False,
             "why": "Green sits further along, well past orange and yellow."},
            {"text": "Orange", "correct": True},
            {"text": "Violet", "correct": False,
             "why": "Violet is at the very opposite end of the visible band "
             "from red."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e15",
        "band": "easier",
        "text": "A prism bends every colour of white light on entry. What "
                "is true of the lowest-frequency colours?",
        "options": [
            {"text": "They pass through without being bent at all, and are "
             "only slowed inside",
             "correct": False,
             "why": "Every colour is bent on entering the glass; none "
             "passes through unrefracted."},
            {"text": "They are bent the most of all",
             "correct": False,
             "why": "The higher-frequency colours are bent the most, not "
             "the lower ones."},
            {"text": "How much they bend has no connection whatsoever to "
             "their own particular frequency",
             "correct": False,
             "why": "The whole reason for dispersion is that the bend does "
             "depend on frequency."},
            {"text": "They are still bent, just by a smaller amount than "
             "higher frequencies",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e16",
        "band": "easier",
        "text": "Which list gives the colours of the spectrum in order, "
                "starting from the lowest frequency?",
        "options": [
            {"text": "Violet, blue, green, yellow, orange, red",
             "correct": False,
             "why": "That is the same band listed from the highest "
             "frequency downwards; the lowest visible frequency is red, not "
             "violet."},
            {"text": "Green, blue, violet, red, orange, yellow",
             "correct": False,
             "why": "This starts in the middle of the band and jumps back; "
             "the spectrum runs continuously from one end to the other."},
            {"text": "Red, yellow, orange, green, violet, blue",
             "correct": False,
             "why": "Orange lies between red and yellow, and violet lies "
             "beyond blue; two pairs here are swapped."},
            {"text": "Red, orange, yellow, green, blue, violet",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e17",
        "band": "easier",
        "text": "Only blue light is shone into a prism, with nothing else "
                 "present. What comes out the other side?",
        "options": [
            {"text": "Blue light, refracted but not spread into a fan", "correct": True},
            {"text": "A full rainbow of colours", "correct": False,
             "why": "A prism has nothing to sort when only one colour arrives."},
            {"text": "White light", "correct": False,
             "why": "White light needs every frequency present; only blue was "
             "supplied."},
            {"text": "No light, since a prism blocks single colours", "correct": False,
             "why": "A prism refracts light of any colour; it does not block "
             "it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e18",
        "band": "easier",
        "text": "What must be true of two colours for a prism to bend them "
                "by different amounts?",
        "options": [
            {"text": "They must be different colours of paint, not light",
             "correct": False,
             "why": "Refraction acts on light, and it is light of different "
             "frequencies that a prism bends by different amounts."},
            {"text": "They must enter the prism through different faces",
             "correct": False,
             "why": "All the colours in a beam enter through the same face, "
             "together."},
            {"text": "They must have different frequencies",
             "correct": True},
            {"text": "They must be travelling at different speeds before "
             "entering",
             "correct": False,
             "why": "All the colours are travelling at the same speed "
             "before they reach the glass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e19",
        "band": "easier",
        "text": "Which of these best describes the boundary between yellow and "
                 "green in the spectrum?",
        "options": [
            {"text": "A sharp line with nothing in between", "correct": False,
             "why": "There is no sharp line anywhere in the spectrum."},
            {"text": "A change in speed, with no change in colour", "correct": False,
             "why": "The visible change is the colour changing; nothing else "
             "marks a boundary."},
            {"text": "A gap with no light present at that point", "correct": False,
             "why": "The band is continuous; no frequency within it is "
             "missing."},
            {"text": "A gradual change, with no real boundary at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e20",
        "band": "easier",
        "text": "Which pair of colours are both near the middle of the visible "
                 "spectrum, not at either end?",
        "options": [
            {"text": "Yellow and green", "correct": True},
            {"text": "Red and violet", "correct": False,
             "why": "Red and violet are the two extreme ends of the visible "
             "band, not the middle."},
            {"text": "Red and orange", "correct": False,
             "why": "Both of these sit at the low-frequency end, not the "
             "middle."},
            {"text": "Blue and violet", "correct": False,
             "why": "Both of these sit at the high-frequency end, not the "
             "middle."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e21",
        "band": "easier",
        "text": "What is true of all the colours in white light as they "
                "enter a glass prism?",
        "options": [
            {"text": "None of them change speed until they leave the glass",
             "correct": False,
             "why": "Every colour slows down the moment it enters the "
             "glass, not only when it leaves."},
            {"text": "They all slow down by exactly the same amount",
             "correct": False,
             "why": "If they all slowed by the same amount there would be "
             "no separation and no spectrum."},
            {"text": "Only the higher frequencies slow down",
             "correct": False,
             "why": "Every colour slows down on entering glass; the higher "
             "frequencies simply slow a little more."},
            {"text": "All of them slow down, though not all by the same "
             "amount",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e22",
        "band": "easier",
        "text": "A beam containing only yellow light enters a prism. What "
                "is seen on the screen?",
        "options": [
            {"text": "A full band of colours, as with any beam",
             "correct": False,
             "why": "A prism can only sort colours that are present; only "
             "yellow was sent in."},
            {"text": "White light",
             "correct": False,
             "why": "Recombining into white needs every frequency present, "
             "not just one."},
            {"text": "Yellow light, refracted but not fanned out",
             "correct": True},
            {"text": "Nothing, because yellow cancels out in the middle of "
             "the band",
             "correct": False,
             "why": "Sitting in the middle of the band has no effect on "
             "whether yellow is refracted; it is refracted like any other "
             "colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e23",
        "band": "easier",
        "text": "Which best describes red light on its own, compared with "
                 "white light?",
        "options": [
            {"text": "White light with all of its other colours taken out again "
             "by reflection",
             "correct": False,
             "why": "Nothing is removed by reflection here; red light on its "
             "own simply is one narrow band of frequencies."},
            {"text": "Exactly the same mixture as white light, just dimmer", "correct": False,
             "why": "White light is a mixture of every frequency; red on its "
             "own is a single narrow band, not a dimmer mixture."},
            {"text": "A mixture of red and orange, blended together", "correct": False,
             "why": "Red light on its own is one narrow band of frequencies, "
             "not a blend of two."},
            {"text": "One narrow band of frequencies, rather than a mixture of "
             "all of them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e24",
        "band": "easier",
        "text": "Dispersion happens because the amount of bending depends "
                "on frequency. What would happen if it did not?",
        "options": [
            {"text": "White light would pass through a prism with no fan of "
             "colours",
             "correct": True},
            {"text": "White light would fan out even more than it already "
             "does",
             "correct": False,
             "why": "Removing the frequency-dependence would remove the "
             "fanning altogether, not increase it."},
            {"text": "Just the lowest frequencies would be affected by this "
             "change",
             "correct": False,
             "why": "If bending did not depend on frequency, no frequency "
             "would be treated differently from any other."},
            {"text": "The prism would add colours instead of separating "
             "them",
             "correct": False,
             "why": "A prism never adds colours in any case; the question "
             "is only about whether the same colours fan apart."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e25",
        "band": "easier",
        "text": "A spectrum is shown by sending light from a ray box "
                "through a prism onto a screen. Why is a narrow beam used "
                "rather than a wide one?",
        "options": [
            {"text": "Because a wide beam cannot be refracted by glass at "
             "all",
             "correct": False,
             "why": "Glass refracts a beam of any width; how wide it is "
             "makes no difference to whether it bends."},
            {"text": "Because a wide beam would be too bright for a screen "
             "to show anything",
             "correct": False,
             "why": "A brighter band is easier to see, not impossible; what "
             "spoils a wide beam is the overlapping, not the brightness."},
            {"text": "Because a narrow beam contains fewer colours, which "
             "makes them easier to sort",
             "correct": False,
             "why": "Narrowing a beam removes no frequencies at all; white "
             "light of any width still contains every one of them."},
            {"text": "Because the colours from a wide beam overlap on the "
             "screen and blur the band",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e26",
        "band": "easier",
        "text": "White light is sent through a prism and nothing else is "
                "put in the beam afterwards. What is seen on the screen?",
        "options": [
            {"text": "The beam recombines into white by itself in the air",
             "correct": False,
             "why": "Recombining needs a second prism, placed the other way "
             "up; nothing happens by itself."},
            {"text": "The fan of colours disappears completely, leaving the "
             "screen blank",
             "correct": False,
             "why": "The fanned band stays exactly as it is until something "
             "else acts on it."},
            {"text": "The fanned band of colours lands on the screen as it "
             "is",
             "correct": True},
            {"text": "The beam becomes invisible",
             "correct": False,
             "why": "The refracted light still reaches the screen and is "
             "still visible as a coloured band."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e27",
        "band": "easier",
        "text": "A prism is set up so that no light enters it at all. What "
                "appears on the screen?",
        "options": [
            {"text": "A faint spectrum appears on it anyway",
             "correct": False,
             "why": "With no light entering, nothing is being refracted or "
             "separated."},
            {"text": "White light",
             "correct": False,
             "why": "White light on the screen would need white light "
             "entering the prism in the first place."},
            {"text": "A single beam of just one colour, refracted sideways",
             "correct": False,
             "why": "A single colour on the screen would need a single "
             "colour entering; here nothing is entering at all."},
            {"text": "Nothing — no light reaches the screen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e28",
        "band": "easier",
        "text": "Which of these correctly completes: dispersion happens "
                 "because a prism bends…",
        "options": [
            {"text": "differently for each frequency", "correct": True},
            {"text": "every frequency by the same amount", "correct": False,
             "why": "Bending every frequency by the same amount would produce "
             "no fan at all."},
            {"text": "the colours it happens to be coloured with itself", "correct": False,
             "why": "An ordinary prism is colourless glass and bends every "
             "frequency that reaches it."},
            {"text": "light when it happens to be white light", "correct": False,
             "why": "A prism bends any colour of light that enters it, not "
             "only white light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e29",
        "band": "easier",
        "text": "A prism bends red light by a certain amount. What does it "
                "do to violet light, from the same beam?",
        "options": [
            {"text": "Bends it by the same amount as red",
             "correct": False,
             "why": "If every colour bent equally there would be no "
             "spectrum at all."},
            {"text": "Leaves it completely unbent",
             "correct": False,
             "why": "Violet is refracted just like every other colour "
             "reaching the prism."},
            {"text": "Bends it by a smaller amount than red",
             "correct": False,
             "why": "Violet has the higher frequency of the two, so it is "
             "the one bent more."},
            {"text": "Bends it by a greater amount than red",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-e30",
        "band": "easier",
        "text": "Which single word names the whole continuous band of colours "
                 "white light contains?",
        "options": [
            {"text": "A ray", "correct": False,
             "why": "A ray is a single narrow line of light, not a whole band "
             "of colours."},
            {"text": "A beam", "correct": False,
             "why": "A beam is a stream of light of any colour, not the name "
             "for the coloured band itself."},
            {"text": "Spectrum", "correct": True},
            {"text": "A shade", "correct": False,
             "why": "A shade names one particular colour, not the whole "
             "continuous band of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s08",
        "band": "standard",
        "text": "A ray box shines a beam of white light into a triangular "
                 "glass prism. Which single property of the light decides how much each "
                 "part of the beam is bent?",
        "options": [
            {"text": "Its frequency", "correct": True},
            {"text": "Its brightness", "correct": False,
             "why": "Brightness affects how much light there is, not the angle "
             "it is bent through."},
            {"text": "Its direction before it entered the prism", "correct": False,
             "why": "Every colour in the beam enters at the same angle; what "
             "differs afterwards is due to frequency, not entry direction."},
            {"text": "How long the beam has been switched on", "correct": False,
             "why": "Duration has no effect on how a beam of light is bent by "
             "glass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s09",
        "band": "standard",
        "text": "Two beams enter separate prisms: one is white light, the "
                "other is red light only. Which beam produces a wider band "
                "of colour on its screen?",
        "options": [
            {"text": "The red beam, because red is the colour a prism bends "
             "the most",
             "correct": False,
             "why": "Red is bent the least of the visible colours, and "
             "there is only one colour in this beam to bend at all."},
            {"text": "The white beam, since it contains every frequency to "
             "separate",
             "correct": True},
            {"text": "Both produce exactly the same width of band, "
             "regardless of colour content",
             "correct": False,
             "why": "The red beam has only one frequency in it, so there is "
             "nothing for the prism to spread into a band."},
            {"text": "Neither beam produces any band",
             "correct": False,
             "why": "The white beam fans out into a full spectrum on its "
             "screen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s10",
        "band": "standard",
        "text": "A prism disperses white light into a spectrum. If the prism "
                 "were replaced with one made of a different type of glass, what would "
                 "most likely change?",
        "options": [
            {"text": "Nothing would change", "correct": False,
             "why": "Different glasses refract light by different amounts, so "
             "the exact spread of the spectrum can differ."},
            {"text": "The order of the colours would reverse", "correct": False,
             "why": "The order always runs from red to violet by frequency, "
             "regardless of the glass used."},
            {"text": "How far the spectrum spreads out", "correct": True},
            {"text": "White light would stop being a mixture of frequencies", "correct": False,
             "why": "What white light is made of does not depend on which "
             "prism it later passes through."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s11",
        "band": "standard",
        "text": "A student sends only violet light into a prism, and "
                 "separately sends only red light into an identical prism. Which beam "
                 "is bent through the larger angle?",
        "options": [
            {"text": "Neither — all colours are bent by the same angle", "correct": False,
             "why": "The whole point of dispersion is that different colours "
             "bend by different angles."},
            {"text": "It depends on how bright each beam is", "correct": False,
             "why": "Brightness plays no part in how much a colour is bent; "
             "frequency does."},
            {"text": "The red beam, since red sits at the front of the band", "correct": False,
             "why": "Position in a list has no physical effect; violet has the "
             "higher frequency and is bent more."},
            {"text": "The violet beam, because violet has the higher frequency", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s12",
        "band": "standard",
        "text": "A prism separates white light into a spectrum on a screen. A "
                 "student blocks out everything except the green part with a card. What "
                 "colour reaches a second screen behind the card?",
        "options": [
            {"text": "Green, unchanged", "correct": True},
            {"text": "White, because blocking colours recombines them", "correct": False,
             "why": "Blocking most of the beam removes light; it does not "
             "recombine what is left into white."},
            {"text": "A full new spectrum, spreading out again", "correct": False,
             "why": "Only a single colour has been let through the card, so "
             "there is nothing left to separate further."},
            {"text": "No light, since the card blocks everything", "correct": False,
             "why": "The card has a gap that lets the green part through; it "
             "does not block that part."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s13",
        "band": "standard",
        "text": "White light passes through a glass prism and splits into a "
                "spectrum. How widely are the colours actually spread as "
                "they leave the prism?",
        "options": [
            {"text": "So widely that red and violet leave in nearly opposite "
                     "directions",
             "correct": False,
             "why": "Textbook drawings fan the colours out like this to make "
                    "them easy to see. Real glass spreads them by only a "
                    "couple of degrees."},
            {"text": "By only a couple of degrees between red and violet",
             "correct": True},
            {"text": "Not at all: the colours only separate when they hit a "
                     "screen",
             "correct": False,
             "why": "The colours separate in the prism, because glass slows "
                    "each colour by a different amount. A screen only shows "
                    "where they have gone."},
            {"text": "By exactly 60°, the angle of the prism",
             "correct": False,
             "why": "The prism's angle helps set how far the light bends, "
                    "but the spread between red and violet is far smaller: a "
                    "couple of degrees."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s14",
        "band": "standard",
        "text": "A prism bends red light by a certain small angle. Does "
                "yellow light from the same beam bend by a different angle?",
        "options": [
            {"text": "No — yellow and red bend by identical angles",
             "correct": False,
             "why": "Every distinct frequency is bent by a slightly "
             "different amount; yellow and red are not identical."},
            {"text": "No — violet and red are the only two that ever differ",
             "correct": False,
             "why": "Every colour differs slightly from its neighbours; the "
             "effect is not limited to just two."},
            {"text": "Yes — yellow bends slightly more, being higher in "
             "frequency",
             "correct": True},
            {"text": "Yes — yellow bends less, despite having a higher "
             "frequency",
             "correct": False,
             "why": "A higher frequency means a slightly greater bend, not "
             "a smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s15",
        "band": "standard",
        "text": "White light and a mixture of just blue and red light are each "
                 "sent through separate, identical prisms. What differs about their "
                 "bands on the screen?",
        "options": [
            {"text": "Nothing — both produce an identical six-colour band", "correct": False,
             "why": "Only the frequencies present in a beam can appear; the "
             "blue-and-red beam has no yellow or green to show."},
            {"text": "The blue-and-red band shows colours that white light "
             "itself does not contain",
             "correct": False,
             "why": "A prism never adds colours; the blue-and-red band can "
             "only show what it was given."},
            {"text": "The white band shows two colours, the other shows six", "correct": False,
             "why": "That is the two beams swapped round — the wider mixture "
             "is what produces more separated colours."},
            {"text": "The white band is a full spectrum; the other is just two "
             "separated patches",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s16",
        "band": "standard",
        "text": "A prism bends every colour of a beam on entering the glass, "
                 "and bends it again on leaving. Why are two bends needed to see a "
                 "clear spectrum?",
        "options": [
            {"text": "Each bend adds to the separation, fanning the colours "
             "apart enough to see",
             "correct": True},
            {"text": "The second bend separates the colours; the first just "
             "slows the light down",
             "correct": False,
             "why": "Both bends contribute; separation begins as soon as the "
             "colours travel at different speeds inside the glass."},
            {"text": "The first bend cancels the second, until a screen is "
             "added",
             "correct": False,
             "why": "The two bends work in the same direction, adding to the "
             "total spread rather than cancelling."},
            {"text": "Two bends are not needed; one bend gives the full effect", "correct": False,
             "why": "A single bend on its own gives a much smaller separation "
             "than the two together produce."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s17",
        "band": "standard",
        "text": "Which set of colours from a spectrum, when their light is "
                 "recombined, would fail to reproduce true white?",
        "options": [
            {"text": "All six named colours together", "correct": False,
             "why": "Recombining all six, as a full spectrum, is exactly how "
             "the second prism restores white."},
            {"text": "Just two of the six, such as red and green alone", "correct": True},
            {"text": "The full continuous spectrum, exactly as it left the "
             "first prism",
             "correct": False,
             "why": "The full continuous spectrum is precisely what recombines "
             "into white."},
            {"text": "Any set of colours, since a second prism restores white "
             "regardless",
             "correct": False,
             "why": "A second prism can only recombine the frequencies it is "
             "given; two colours alone cannot recreate every frequency of "
             "white."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s18",
        "band": "standard",
        "text": "A ray box sends in 'blue and red' light. A second prism, "
                "correctly inverted, is placed in the fanned beam. What "
                "colour patch appears on the final screen?",
        "options": [
            {"text": "One white patch",
             "correct": False,
             "why": "White needs every visible frequency; only blue and red "
             "were sent in."},
            {"text": "Green",
             "correct": False,
             "why": "No green was present in the original beam, and a prism "
             "cannot introduce a colour that was not there."},
            {"text": "A pinky-purple patch",
             "correct": True},
            {"text": "Two separate patches, still apart",
             "correct": False,
             "why": "The correctly inverted second prism brings the two "
             "colours back together into one patch, rather than leaving "
             "them separated."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s19",
        "band": "standard",
        "text": "Newton passed light through a first prism, then let only the "
                 "green part through a hole in a card, then through a second prism. The "
                 "green stayed green. What did this show?",
        "options": [
            {"text": "That the first prism failed to separate the colours "
             "properly that time",
             "correct": False,
             "why": "The first prism worked exactly as expected — the green "
             "part was there to select in the first place."},
            {"text": "That green light is impossible to bend with any prism", "correct": False,
             "why": "The green light was bent by both prisms; it is refracted "
             "just like every colour."},
            {"text": "That white light is not a mixture in the first place", "correct": False,
             "why": "Selecting one already-separated colour and finding it "
             "unchanged supports the opposite conclusion — white light is a "
             "mixture."},
            {"text": "That the colours making up white light cannot be split "
             "any further",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s20",
        "band": "standard",
        "text": "What would you expect to see if a beam containing only red "
                 "and green light, no blue, were sent through a prism?",
        "options": [
            {"text": "Two separated patches, red and green", "correct": True},
            {"text": "A single yellow patch, since red and green mix to give "
             "yellow",
             "correct": False,
             "why": "A prism separates colours; it does not mix red and green "
             "light together."},
            {"text": "A full spectrum including blue and violet", "correct": False,
             "why": "No blue or violet was present in the beam, so none can "
             "appear on the screen."},
            {"text": "White light, because two colours together make white", "correct": False,
             "why": "White needs every visible frequency present, not just "
             "two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s21",
        "band": "standard",
        "text": "A student says: 'the colours must already be sorted by "
                "frequency inside the white beam, in a queue, waiting to "
                "come out.' What is wrong with this idea?",
        "options": [
            {"text": "Nothing; the colours really do travel in a sorted "
             "queue inside the beam",
             "correct": False,
             "why": "The frequencies travel together, mixed, until "
             "refraction separates them; nothing is queued up beforehand."},
            {"text": "The frequencies travel mixed together; refraction is "
             "what separates them",
             "correct": True},
            {"text": "White light does not contain multiple frequencies",
             "correct": False,
             "why": "White light is explicitly a mixture of every visible "
             "frequency, travelling together."},
            {"text": "The colours are already sorted by the surrounding air "
             "before ever reaching the prism",
             "correct": False,
             "why": "Air treats all the visible frequencies very nearly "
             "alike; the separating happens inside the glass, by "
             "refraction."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s22",
        "band": "standard",
        "text": "A green filter and the green part of a prism's spectrum "
                "both end up as green light. What is the key difference in "
                "how each one arrives at green?",
        "options": [
            {"text": "There is no difference; both of them work by adding "
             "green to the light",
             "correct": False,
             "why": "Neither one adds green; a filter subtracts other "
             "colours and a prism sorts what is already there."},
            {"text": "A filter bends light; a prism absorbs it",
             "correct": False,
             "why": "That reverses the two devices' jobs — a prism bends "
             "light and a filter mostly absorbs what it does not pass."},
            {"text": "A filter removes every colour but green; a prism "
             "bends green out instead",
             "correct": True},
            {"text": "A prism works with green light passing through it, a "
             "filter with white light instead",
             "correct": False,
             "why": "A prism refracts every colour, and a filter can be any "
             "colour, not only green or white."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s23",
        "band": "standard",
        "text": "A prism spreads white light into a spectrum on a screen 2 m "
                 "away. If the screen were moved further back, what would you expect?",
        "options": [
            {"text": "The spectrum would disappear completely", "correct": False,
             "why": "The refracted rays keep travelling in straight lines and "
             "will still reach a more distant screen."},
            {"text": "The order of the colours would reverse", "correct": False,
             "why": "The order of colours by frequency does not depend on how "
             "far away the screen is."},
            {"text": "The spectrum would turn back into white light", "correct": False,
             "why": "Distance travelled afterwards does not recombine colours; "
             "only a second prism, correctly placed, can do that."},
            {"text": "The band of colours would spread out even wider", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s24",
        "band": "standard",
        "text": "A prism bends blue light by a larger angle than red light. "
                 "What can you conclude about the speed of blue light inside the glass, "
                 "compared with red's speed there?",
        "options": [
            {"text": "Blue light travels more slowly inside the glass than red "
             "does",
             "correct": True},
            {"text": "Blue light travels faster inside the glass than red does", "correct": False,
             "why": "A larger bend at the boundary corresponds to a bigger "
             "change in speed, meaning blue slows down more, not less."},
            {"text": "Both travel at exactly the same speed inside the glass", "correct": False,
             "why": "If both slowed by the same amount, they would bend by the "
             "same amount too, and there would be no separation."},
            {"text": "Speed inside the glass cannot be linked to the bend", "correct": False,
             "why": "The size of the bend at a boundary is directly related to "
             "how much the light's speed changes there."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s25",
        "band": "standard",
        "text": "A prism is turned upside down compared with how it usually "
                 "sits, but light still travels straight through it. What changes about "
                 "the spectrum produced?",
        "options": [
            {"text": "No spectrum forms in this orientation", "correct": False,
             "why": "Turning the prism over does not stop it refracting light; "
             "a spectrum still forms."},
            {"text": "The band forms flipped, colours reversed top to bottom", "correct": True},
            {"text": "The band forms the same way, with red staying higher up", "correct": False,
             "why": "Turning the whole prism over reverses which side red and "
             "violet end up on."},
            {"text": "The colours stop separating by frequency, and separate by "
             "brightness instead",
             "correct": False,
             "why": "Frequency is still what decides the amount of bending, "
             "whichever way the prism is turned."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s26",
        "band": "standard",
        "text": "A prism separates white light. Which of the following would "
                 "you expect not to change the pattern of colours, only how bright it "
                 "is?",
        "options": [
            {"text": "Changing which type of glass the prism is made from", "correct": False,
             "why": "Different glasses bend light by different amounts, which "
             "changes how spread out the pattern is."},
            {"text": "Turning the prism to a completely different angle to the "
             "beam",
             "correct": False,
             "why": "The angle at which light strikes the prism affects how "
             "much it is refracted overall."},
            {"text": "Using a brighter lamp with the same range of frequencies", "correct": True},
            {"text": "Replacing white light with just two of its component "
             "colours",
             "correct": False,
             "why": "Removing frequencies from the input beam changes which "
             "colours can appear on the screen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s27",
        "band": "standard",
        "text": "A prism is lit with white light, and a card with a narrow "
                 "slit lets only violet light through before the screen. What would you "
                 "expect if this violet were sent through another identical prism?",
        "options": [
            {"text": "It would separate into red through violet all over again", "correct": False,
             "why": "Only one frequency has been selected by the slit; a prism "
             "has nothing further to separate from a single colour."},
            {"text": "It would turn back into white light", "correct": False,
             "why": "Recombining into white needs every frequency present; "
             "only violet has been selected here."},
            {"text": "It would turn green, since violet sits next to green on "
             "the far side of the band",
             "correct": False,
             "why": "A prism does not change one colour into another; the "
             "light stays violet, only refracted."},
            {"text": "It would come out still violet, simply refracted again", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s28",
        "band": "standard",
        "text": "A rainbow forms with red on the outside of the arc and violet "
                 "on the inside. Which single property of sunlight decides this fixed "
                 "order?",
        "options": [
            {"text": "Frequency", "correct": True},
            {"text": "The height of the Sun in the sky", "correct": False,
             "why": "The Sun's height affects whether you see a rainbow at "
             "all, not which colour ends up on which side."},
            {"text": "The distance the light has travelled to reach the "
             "raindrop",
             "correct": False,
             "why": "Distance travelled does not change a colour's frequency "
             "or how much it is refracted."},
            {"text": "The size of the raindrop it passes through", "correct": False,
             "why": "The order of colours by frequency is the same in any size "
             "of raindrop."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s29",
        "band": "standard",
        "text": "A student claims a prism 'chooses' to bend violet more "
                "because violet is a 'stronger' colour. What is the actual "
                "physical reason violet bends more than red?",
        "options": [
            {"text": "There is no physical reason; it is simply a rule to "
             "memorise",
             "correct": False,
             "why": "There is a physical reason: violet slows a little more "
             "than red on entering the glass, because of its higher "
             "frequency."},
            {"text": "Violet has a higher frequency, so it is refracted "
             "slightly more by the glass",
             "correct": True},
            {"text": "Violet light carries more energy, and more energetic "
             "light avoids bending",
             "correct": False,
             "why": "Violet is in fact bent more, not less, despite "
             "carrying more energy per photon at that frequency."},
            {"text": "Violet is closer to ultraviolet, which the glass is "
             "designed to reflect away",
             "correct": False,
             "why": "An ordinary glass prism is not designed to reflect any "
             "particular colour; it refracts every visible frequency "
             "reaching it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-s30",
        "band": "standard",
        "text": "A student says a prism can turn any colour of light into "
                "any other colour, given enough time. Which experiment most "
                "directly disproves this?",
        "options": [
            {"text": "Timing how long light takes to cross the glass",
             "correct": False,
             "why": "Timing the crossing says nothing about whether colours "
             "can be converted into each other."},
            {"text": "Measuring the exact angle of the prism",
             "correct": False,
             "why": "The angle of the prism affects how much the light "
             "spreads, not whether one colour becomes another."},
            {"text": "Recombining a fanned spectrum with a second, inverted "
             "prism",
             "correct": True},
            {"text": "Shining light through the prism in complete darkness",
             "correct": False,
             "why": "Darkness around the prism does not test whether "
             "colours convert into each other."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h08",
        "band": "harder",
        "text": "A student argues that since a prism 'sorts' colours, it must "
                 "act like a sieve that lets some colours through faster and blocks "
                 "others. What is wrong with the sieve idea?",
        "options": [
            {"text": "Every colour passes through; none is blocked, only "
             "refracted differently",
             "correct": True},
            {"text": "A sieve would let more light through overall, and a prism "
             "dims the beam instead",
             "correct": False,
             "why": "A prism does dim the beam very slightly, by reflection at "
             "its surfaces, but that is not why the sieve idea is wrong."},
            {"text": "Sieves work with solids, and light is not a solid", "correct": False,
             "why": "The problem with the analogy is about what happens to "
             "each colour, not about the general category of solids."},
            {"text": "A sieve cannot be made of glass, just of mesh", "correct": False,
             "why": "The material a sieve is made from is not the issue; the "
             "issue is that nothing is blocked or filtered out."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h09",
        "band": "harder",
        "text": "Two prisms, A and B, are made of different types of glass. "
                 "The same white beam produces a wider spectrum from A than from B. "
                 "What can you conclude?",
        "options": [
            {"text": "Prism A bends every colour by exactly the same amount, "
             "more than B does",
             "correct": False,
             "why": "If every colour bent by the same amount there would be no "
             "spread at all, in either prism."},
            {"text": "Prism A's glass separates the frequencies by a greater "
             "amount than B's does",
             "correct": True},
            {"text": "Prism B is not a proper prism, given the smaller spread", "correct": False,
             "why": "A prism is still a prism whatever the size of the spread "
             "it produces; the type of glass affects the degree of separation, "
             "not whether it happens."},
            {"text": "The white light entering prism A contained more "
             "frequencies than that entering B",
             "correct": False,
             "why": "Both beams were white light, containing the same range of "
             "frequencies; the glass, not the source, is what differs here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h10",
        "band": "harder",
        "text": "A pinhole with no lens or prism can also spread sunlight "
                "into faint fringes of colour at its edges. Does this "
                "contradict the account of dispersion as refraction that "
                "depends on frequency?",
        "options": [
            {"text": "Yes — dispersion should only ever happen inside a "
             "prism",
             "correct": False,
             "why": "Refraction depending on frequency is not something "
             "only prisms do; raindrops and thin oil films separate colours "
             "too."},
            {"text": "Yes — a pinhole should show no colour effects of any "
             "kind",
             "correct": False,
             "why": "Colour fringes at a small enough opening are a real, "
             "separate effect, not addressed by the prism account either "
             "way."},
            {"text": "No — refraction bending more at higher frequencies "
             "does not rule out other effects",
             "correct": True},
            {"text": "No — a pinhole and a prism are the same piece of "
             "equipment, doing the same optical job",
             "correct": False,
             "why": "A pinhole and a prism work by entirely different "
             "means; a pinhole has no glass and no refracting surfaces "
             "shaped like a prism."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h11",
        "band": "harder",
        "text": "A designer wants a prism that spreads white light into the "
                "widest possible spectrum at a fixed screen distance. What "
                "property should they look for in the glass?",
        "options": [
            {"text": "The glass with the highest transparency available, so "
             "as much light as possible can get through",
             "correct": False,
             "why": "Transparency affects how much light is lost, not how "
             "much the frequencies separate from each other."},
            {"text": "The heaviest glass available, since heavier materials "
             "bend light more",
             "correct": False,
             "why": "Weight is not what determines refraction; the "
             "material's optical properties are, regardless of how heavy "
             "the glass is."},
            {"text": "Any ordinary glass, since the spread stays the same "
             "regardless of glass used",
             "correct": False,
             "why": "The exact spread depends on the glass: different "
             "glasses separate the frequencies by different amounts."},
            {"text": "Glass in which higher frequencies are refracted by a "
             "noticeably larger amount than lower ones",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h12",
        "band": "harder",
        "text": "The visible spectrum spans roughly one octave, about a "
                "doubling of frequency from red to violet. Human hearing, "
                "for comparison, stops at about 20 000 Hz. What is the "
                "point of putting the two side by side?",
        "options": [
            {"text": "Both senses only respond to a narrow slice of a much "
             "wider range that exists in nature",
             "correct": True},
            {"text": "Both senses detect exactly the same underlying range "
             "of frequencies, just measured in different units",
             "correct": False,
             "why": "Sound and light are different kinds of wave, and their "
             "frequency ranges are not directly comparable in this way."},
            {"text": "Hearing and sight both stop working completely above "
             "20 000 Hz",
             "correct": False,
             "why": "20 000 Hz is roughly the upper limit of human hearing; "
             "it says nothing about the limit of sight, which is governed "
             "by a completely different range."},
            {"text": "The comparison shows that light waves and sound waves "
             "travel at exactly the same speed",
             "correct": False,
             "why": "The comparison is about the range of frequencies each "
             "sense responds to, not about the speed either wave travels "
             "at."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h13",
        "band": "harder",
        "text": "Ultraviolet, visible light and infrared are part of one "
                 "continuous family, differing only in frequency. Where does "
                 "ultraviolet sit relative to violet light?",
        "options": [
            {"text": "Below red, at an even lower frequency", "correct": False,
             "why": "That position is where infrared sits, not ultraviolet."},
            {"text": "Just above violet, slightly higher", "correct": True},
            {"text": "In the middle of the visible band, near green", "correct": False,
             "why": "Ultraviolet is entirely outside the visible band, past "
             "its highest-frequency end."},
            {"text": "It has no fixed position; it depends which prism is used", "correct": False,
             "why": "Frequency ranges of the electromagnetic family do not "
             "shift depending on which prism happens to be used."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h14",
        "band": "harder",
        "text": "A student claims: 'if I could build a prism with zero "
                "thickness, I could still get a full spectrum from it.' "
                "Evaluate this claim.",
        "options": [
            {"text": "Correct, because thickness plays no part in "
             "dispersion",
             "correct": False,
             "why": "A prism with no thickness would give the light no "
             "glass to travel through, and no opportunity for the "
             "frequencies to separate."},
            {"text": "Correct, because a prism's colour, not its thickness, "
             "disperses light",
             "correct": False,
             "why": "An ordinary prism is colourless; dispersion comes from "
             "refraction as light crosses into and out of the glass, which "
             "needs some thickness to have an effect."},
            {"text": "False — the separating effect builds up as light "
             "travels through the glass",
             "correct": True},
            {"text": "False, because a prism must be exactly triangular to "
             "work, of any size",
             "correct": False,
             "why": "The triangular shape helps show the effect clearly on "
             "a screen; the physical requirement for dispersion is "
             "refraction at a boundary, not any particular shape."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h15",
        "band": "harder",
        "text": "Which statement correctly links a colour's frequency to "
                "how much a prism bends it?",
        "options": [
            {"text": "Lower frequency means a larger bend, in every "
             "material",
             "correct": False,
             "why": "In an ordinary glass prism the relationship runs the "
             "other way: higher frequency means a larger bend."},
            {"text": "The size of the bend has nothing to do with "
             "frequency, just the prism's angle",
             "correct": False,
             "why": "The prism's angle affects the overall geometry, but "
             "which colour bends most is decided by frequency."},
            {"text": "All frequencies bend equally, and the fan is created "
             "afterwards by the screen",
             "correct": False,
             "why": "The screen does not create anything; it simply shows "
             "where the already-separated rays land."},
            {"text": "Higher frequency means a larger bend, since the light "
             "slows more entering glass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h16",
        "band": "harder",
        "text": "A student mixes red, green and blue light together, not "
                "paint, and shines the mixture through a prism. What would "
                "you expect to see on the screen?",
        "options": [
            {"text": "Three separated patches: red, green and blue, each in "
             "its usual position along the band",
             "correct": True},
            {"text": "A single white patch, since mixing three colours of "
             "light gives white before it reaches the prism",
             "correct": False,
             "why": "Mixing does not happen inside the prism; the mixed "
             "beam still contains three distinct frequencies for the prism "
             "to separate."},
            {"text": "A single blended patch, refracted as though the "
             "mixture were one colour of its own",
             "correct": False,
             "why": "The prism refracts each frequency separately, by its "
             "own amount, so the three do not stay blended together on the "
             "screen."},
            {"text": "Six separated patches, since a prism produces six "
             "every time",
             "correct": False,
             "why": "A prism only separates the frequencies actually "
             "present in the beam; only three were supplied here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h17",
        "band": "harder",
        "text": "Dispersion is explained in terms of frequency rather than "
                "in terms of colour names. Why is frequency the more "
                "fundamental quantity here?",
        "options": [
            {"text": "Because colour names are used in English, and "
             "frequency avoids that problem",
             "correct": False,
             "why": "While colour names do vary between languages, the "
             "deeper reason is that frequency is the actual physical "
             "property responsible for the bending, in any language."},
            {"text": "Because frequency is the real property behind the "
             "bend; the name is only a label",
             "correct": True},
            {"text": "Because 'red' and 'violet' correspond to no real "
             "physical difference",
             "correct": False,
             "why": "The names do correspond to genuine differences in "
             "frequency; the point is only that frequency, not the label, "
             "causes the bending."},
            {"text": "Because frequency changes every time light passes "
             "through a different prism",
             "correct": False,
             "why": "A given beam's frequency does not change from prism to "
             "prism; what changes is how much that frequency happens to be "
             "bent."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h18",
        "band": "harder",
        "text": "Why does recombining a full spectrum with a second prism "
                "prove more about white light than simply asserting that "
                "'white light contains all the colours'?",
        "options": [
            {"text": "Because assertions are not trustworthy in science, "
             "while experiments are",
             "correct": False,
             "why": "The point is not a general rule about assertions "
             "versus experiments; it is about what this particular "
             "experiment shows."},
            {"text": "Because assertion alone cannot rule out the prism "
             "producing the colour; recombination does",
             "correct": True},
            {"text": "Because recombination is simply easier to demonstrate "
             "to an audience",
             "correct": False,
             "why": "Ease of demonstration is not the reason it carries "
             "more scientific weight; what matters is what the result "
             "actually rules out."},
            {"text": "Because assertion and experiment are equally strong "
             "here, and neither adds anything the other lacks",
             "correct": False,
             "why": "The experiment adds something an assertion cannot: a "
             "direct test of whether the prism is creating or merely "
             "sorting the colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h19",
        "band": "harder",
        "text": "A rainbow, the underside of a CD reflecting light, and a "
                 "prism's spectrum are three different ways of splitting white light "
                 "into colour. What do all three share, physically?",
        "options": [
            {"text": "All three rely on refraction happening twice, once "
             "entering and once leaving a transparent material",
             "correct": False,
             "why": "A CD splits colour by reflecting off a fine ridged "
             "surface, not by refracting through a transparent material — the "
             "shared feature must be something more general."},
            {"text": "All three separate frequencies already present in the "
             "white light, rather than creating new ones",
             "correct": True},
            {"text": "All three work with sunlight alone, and fail with an "
             "artificial lamp",
             "correct": False,
             "why": "None of the three methods requires sunlight specifically; "
             "any light containing the right mixture of frequencies would "
             "work."},
            {"text": "All three require the light to pass through at least one "
             "prism",
             "correct": False,
             "why": "A rainbow uses raindrops and a CD uses its ridged "
             "surface; neither involves an actual prism."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h20",
        "band": "harder",
        "text": "A student wants to test whether a blue-tinted glass prism "
                "produces the same spectrum as a colourless one of the same "
                "shape. What should they expect?",
        "options": [
            {"text": "An identical full spectrum, since the glass's own "
             "tint makes no real difference to the outcome",
             "correct": False,
             "why": "Blue-tinted glass absorbs some frequencies as light "
             "passes through it, unlike ordinary colourless glass."},
            {"text": "No light would pass through the tinted glass",
             "correct": False,
             "why": "Tinted glass still transmits its own colour; it does "
             "not block every frequency."},
            {"text": "A spectrum missing some of the frequencies the tint "
             "absorbs, rather than the full range",
             "correct": True},
            {"text": "The tinted glass would add extra colours not present "
             "in the original beam",
             "correct": False,
             "why": "A material can only remove or pass on frequencies that "
             "arrive; it cannot add frequencies that were not there."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h21",
        "band": "harder",
        "text": "Is it correct to say that a prism 'creates' the colour "
                 "violet?",
        "options": [
            {"text": "Yes, because no violet light exists until it passes "
             "through a prism",
             "correct": False,
             "why": "Violet light exists in ordinary white light before it "
             "ever reaches a prism; the prism only makes it visible as a "
             "separate band."},
            {"text": "Yes, because the prism supplies the energy needed to "
             "produce violet",
             "correct": False,
             "why": "The prism supplies no energy to the light at all; it only "
             "changes the direction each frequency travels in."},
            {"text": "No — violet is already in white light; the prism only "
             "separates it",
             "correct": True},
            {"text": "No, because violet does not exist as a real frequency of "
             "light",
             "correct": False,
             "why": "Violet is a genuine, distinct frequency of visible light, "
             "at the high-frequency end of the band."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h22",
        "band": "harder",
        "text": "Two identical prisms are set up so light passes through both, "
                 "correctly, to recombine into white — but a thick piece of red glass "
                 "sits between them, absorbing everything but red. What comes out at "
                 "the end?",
        "options": [
            {"text": "White light, since the second prism restores white "
             "regardless of what happens in between",
             "correct": False,
             "why": "The second prism can only recombine whatever frequencies "
             "actually reach it; here, most of them have already been absorbed "
             "by the red glass."},
            {"text": "Red light only", "correct": True},
            {"text": "A spectrum missing just violet", "correct": False,
             "why": "Red glass close to a full spectrum blocks far more than "
             "just violet; nearly every colour but red is absorbed."},
            {"text": "No light, since the red glass blocks everything", "correct": False,
             "why": "Red glass lets red light through; it absorbs the other "
             "colours, not all of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h23",
        "band": "harder",
        "text": "A prism separates white light into a spectrum. If you could "
                 "somehow slow down only the red light extra, without affecting any "
                 "other colour, what would happen to the pattern on the screen?",
        "options": [
            {"text": "Nothing would change; frequency, not speed inside the "
             "glass, affects the pattern",
             "correct": False,
             "why": "The whole reason different colours end up in different "
             "places is that they are slowed by different amounts inside the "
             "glass — speed and bending are directly linked."},
            {"text": "Red would then bend by a larger angle, moving further "
             "from its usual position",
             "correct": True},
            {"text": "All the colours would swap the amount they usually bend "
             "by",
             "correct": False,
             "why": "Slowing only the red light does not affect the other "
             "colours' speeds or their existing bends."},
            {"text": "The spectrum would become narrower overall", "correct": False,
             "why": "Extra bending for one colour alone would spread that "
             "colour further from the rest, not compress the whole band."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h24",
        "band": "harder",
        "text": "Which historical fact about the number of named colours in "
                "the spectrum is correct, and what does it show about the "
                "names themselves?",
        "options": [
            {"text": "Newton chose seven to match a musical scale — a "
             "convention, not a boundary",
             "correct": True},
            {"text": "Newton discovered exactly seven distinct wavelengths, "
             "and no others exist",
             "correct": False,
             "why": "The spectrum is continuous; Newton's seven names are a "
             "convention, not a discovery of seven distinct wavelengths."},
            {"text": "Scientists later proved there are just three true "
             "colours",
             "correct": False,
             "why": "No three colours are more 'true' than the rest; the "
             "band is continuous, and the names are labels along it."},
            {"text": "Every language in the world uses the same seven names "
             "for the spectrum",
             "correct": False,
             "why": "Different languages divide the same continuous band up "
             "differently, which is part of why the names are a convention."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h25",
        "band": "harder",
        "text": "A student says: 'because a prism bends blue more than red, "
                "blue light must be heavier than red light.' What is the "
                "flaw in this reasoning?",
        "options": [
            {"text": "There is no flaw; heavier light bends more in every "
             "material",
             "correct": False,
             "why": "Light has no mass in the sense the student means, and "
             "'heaviness' plays no part in how a prism separates colours."},
            {"text": "It confuses frequency, which affects bending, with an "
             "unused idea of 'heaviness'",
             "correct": True},
            {"text": "It is flawed simply because red, not blue, should be "
             "called the heavier colour instead",
             "correct": False,
             "why": "The problem is not which colour is called heavier; it "
             "is that heaviness explains nothing about the bending at all."},
            {"text": "It is flawed because blue and red bend by the same "
             "amount",
             "correct": False,
             "why": "Blue is genuinely bent more than red — the reasoning's "
             "conclusion happens to point the right way, but for a mistaken "
             "reason."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h26",
        "band": "harder",
        "text": "A beam containing only blue and red light is sent through "
                "a prism. On the screen, no colour at all lands between the "
                "two places the light reaches. What causes that empty "
                "space?",
        "options": [
            {"text": "The prism actively removes the missing colours from "
             "the beam",
             "correct": False,
             "why": "The prism removes nothing; it can only separate the "
             "frequencies that were sent into it."},
            {"text": "There is no real gap; it is an illusion caused by "
             "contrast",
             "correct": False,
             "why": "The gap is genuinely empty of light, because no yellow "
             "or green frequency was present in the beam to land there."},
            {"text": "No frequency between blue and red was in the original "
             "beam",
             "correct": True},
            {"text": "The screen itself is faulty in that particular region",
             "correct": False,
             "why": "The screen behaves the same everywhere; what differs "
             "is simply whether any light lands on a given part of it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h27",
        "band": "harder",
        "text": "Two students each set up a ray box and a prism. One "
                "reports the red end of their spectrum on the left, the "
                "other on the right. Can both results be correct?",
        "options": [
            {"text": "No — red must appear on the left, in every correct "
             "setup",
             "correct": False,
             "why": "Which side red ends up on depends on how the equipment "
             "happens to be arranged, not on any fixed rule about left and "
             "right."},
            {"text": "Yes — the order by frequency is fixed; only the "
             "starting side depends on the setup",
             "correct": True},
            {"text": "No — just one of them can be measuring a real "
             "spectrum",
             "correct": False,
             "why": "Both benches can show a genuine, correctly-ordered "
             "spectrum; only the physical orientation of their equipment "
             "differs."},
            {"text": "Yes — because the order of colours by frequency "
             "changes from one prism to the next",
             "correct": False,
             "why": "The order by frequency is fixed — red then orange then "
             "yellow and so on; it is only the starting side that can "
             "differ."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h28",
        "band": "harder",
        "text": "A prism and a diffraction grating, a surface with many fine, "
                 "closely-spaced lines, can both split white light into a spectrum, by "
                 "different means. What must be true of both, regardless of mechanism?",
        "options": [
            {"text": "Both must be made of exactly the same kind of glass", "correct": False,
             "why": "A diffraction grating does not need to be glass at all, "
             "and need not match a prism's material."},
            {"text": "Both must treat different frequencies differently, to "
             "separate them",
             "correct": True},
            {"text": "Both must add extra colours not present in the light "
             "beforehand",
             "correct": False,
             "why": "Neither device adds colours; both work by separating "
             "frequencies that were already present."},
            {"text": "Both must slow every frequency down by exactly the same "
             "amount",
             "correct": False,
             "why": "Treating every frequency identically would give no "
             "separation at all, whichever device were used."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h29",
        "band": "harder",
        "text": "Considering the whole lesson, which sentence best captures "
                 "why 'the prism adds colour' is such a persistent misconception?",
        "options": [
            {"text": "Because a colourless object producing colour looks, at a "
             "glance, like its source",
             "correct": True},
            {"text": "Because prisms are themselves subtly coloured objects, "
             "which is what misleads people",
             "correct": False,
             "why": "An ordinary prism is made of colourless glass; the "
             "misconception persists despite this, not because of it."},
            {"text": "Because most people have not seen a prism in real life", "correct": False,
             "why": "The misconception is widespread even among people who "
             "have seen a prism demonstrated, which is why the second-prism "
             "experiment is needed to settle it."},
            {"text": "Because school lessons rarely mention prisms", "correct": False,
             "why": "The persistence of the idea is about how convincing the "
             "visual effect looks, not about how often prisms are taught."},
        ],
        "figure": None,
    },
    {
        "id": "p7-06-h30",
        "band": "harder",
        "text": "Summarising the whole lesson in one sentence, which statement "
                 "is the most accurate?",
        "options": [
            {"text": "A prism manufactures new colours from plain glass, by a "
             "process still not fully understood",
             "correct": False,
             "why": "Nothing about the process is mysterious or manufactures "
             "anything; a prism sorts frequencies that were already present, "
             "by refraction."},
            {"text": "White light is a mixture of every visible frequency, and "
             "a prism sorts it by frequency",
             "correct": True},
            {"text": "Colour is a property added to light when it strikes an "
             "object such as a prism",
             "correct": False,
             "why": "Colour, as a light wave's frequency, is a property of the "
             "light itself before it ever meets a prism."},
            {"text": "A prism's function is to make white light brighter by "
             "concentrating it into a narrower beam",
             "correct": False,
             "why": "A prism spreads the light out into a wider band on a "
             "screen; it does not concentrate it into a narrower beam."},
        ],
        "figure": None,
    },
]
