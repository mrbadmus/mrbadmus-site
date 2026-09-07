"""P7 lesson 04 — Lenses and images: twelve questions (MRB-223).

Written against Design's page. The shoebox hook, the three-control
pinhole bench and the two lens diagrams are hers.

The discriminations, in the order the lesson builds them:

  · the inversion is where straight lines GO, and nothing flips anything
    (`LIGHT-13`);
  · the hole width moves the blur and the brightness and NOT the size
    (`LIGHT-14`);
  · a longer box makes a BIGGER picture, not a smaller one (`LIGHT-15`);
  · straight lines are exactly why a wider hole blurs (`LIGHT-16`) — the
    harder band sits here.

⚠️ POSITION IS AUTHORED — 3,1,2,0 · 1,3,0,2 · 0,2,3,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. This lesson has no
worked example: her FLAG 4 leaves the image-height product out because
`LGT.04` says qualitative, and nothing was invented to fill a block.
"""

UNIT = "P7"
LESSON = "lenses-and-images"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-04-e01",
        "band": "easier",
        "text": "The picture on the screen of a pinhole camera is…",
        "options": [
            {"text": "the right way up and the right way round",
             "correct": False,
             "why": "The rays cross at the hole, so both are reversed."},
            {"text": "the right way up but reversed left to right",
             "correct": False,
             "why": "Both are reversed together, because the crossing "
                    "happens in every direction at once."},
            {"text": "upside down but the right way round", "correct": False,
             "why": "Left and right swap too. The crossing does not pick "
                    "one direction."},
            {"text": "upside down and reversed left to right",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e02",
        "band": "easier",
        "text": "A convex lens is one that…",
        "options": [
            {"text": "is flat on both sides", "correct": False,
             "why": "A flat sheet of glass shifts a ray sideways and brings "
                    "nothing to a point."},
            {"text": "bulges outwards on both sides", "correct": True},
            {"text": "is hollowed inwards on both sides", "correct": False,
             "why": "That is a concave lens, which spreads rays apart "
                    "instead of bringing them together."},
            {"text": "has a small hole through the middle", "correct": False,
             "why": "That is a pinhole, and it is what a lens exists to "
                    "replace."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e03",
        "band": "easier",
        "text": "Making the hole in a pinhole camera narrower makes the "
                "picture…",
        "options": [
            {"text": "bigger and brighter", "correct": False,
             "why": "Narrowing the hole changes neither the size nor the "
                    "direction of brightness you expect: it lets LESS light "
                    "in."},
            {"text": "smaller and dimmer", "correct": False,
             "why": "Dimmer is right and smaller is not. The size does not "
                    "depend on the hole at all."},
            {"text": "sharper and dimmer", "correct": True},
            {"text": "sharper and brighter", "correct": False,
             "why": "That would be having it both ways, and it is exactly "
                    "the bargain a pinhole cannot make. A lens can."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e04",
        "band": "easier",
        "text": "What does focusing mean?",
        "options": [
            {"text": "Bringing all the light that left one point of an "
                     "object back to one point on the screen",
             "correct": True},
            {"text": "Making the picture brighter by letting more light in",
             "correct": False,
             "why": "That is what a wider opening does. Focusing is about "
                    "where the light lands."},
            {"text": "Turning the picture the right way up",
             "correct": False,
             "why": "A lens does not do that. The picture in a camera and "
                    "on your retina are both upside down."},
            {"text": "Blocking all but one ray from each point of the "
                     "object, so that only one can land", "correct": False,
             "why": "That is what a pinhole does, and it is the opposite "
                    "approach: it throws light away rather than gathering "
                    "it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-04-s01",
        "band": "standard",
        "text": "An object is moved twice as far from a pinhole camera, "
                "with the box unchanged. The picture becomes…",
        "options": [
            {"text": "twice as tall", "correct": False,
             "why": "Moving the object AWAY makes the picture smaller. "
                    "Lengthening the box is what makes it taller."},
            {"text": "half as tall", "correct": True},
            {"text": "the same height, because the box has not changed",
             "correct": False,
             "why": "Both distances matter. The picture height follows the "
                    "box length divided by the object distance."},
            {"text": "four times as tall", "correct": False,
             "why": "Doubling one distance halves the height. Nothing here "
                    "squares."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s02",
        "band": "standard",
        "text": "The hole of a pinhole camera is widened from 1 mm to "
                "3 mm. Which reading does NOT change?",
        "options": [
            {"text": "How blurred each point is", "correct": False,
             "why": "The blur grows with the hole — that is the price of "
                    "the extra light."},
            {"text": "How much light gets in", "correct": False,
             "why": "About nine times as much, because it follows the area "
                    "of the hole."},
            {"text": "How sharp the edges of the picture look",
             "correct": False,
             "why": "The edges soften as the blur grows. It is the same "
                    "reading described in words."},
            {"text": "The height of the picture", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s03",
        "band": "standard",
        "text": "Why does a wider hole blur the picture, given that light "
                "still travels in straight lines?",
        "options": [
            {"text": "Because a whole bundle of straight rays from each "
                     "point now gets through, and they land in slightly "
                     "different places", "correct": True},
            {"text": "Because the light bends as it squeezes past the edges "
                     "of a wide hole, and the wider the hole the more of it "
                     "bends", "correct": False,
             "why": "Bending at an edge is a real effect and it is not this "
                    "one — it matters for very NARROW holes, not wide "
                    "ones."},
            {"text": "Because more light makes the picture too bright to "
                     "see clearly", "correct": False,
             "why": "Brightness and sharpness are separate. A bright sharp "
                    "picture is exactly what a lens gives you."},
            {"text": "Because the rays cross more than once on the way to "
                     "the screen", "correct": False,
             "why": "They cross once, at the hole, whatever its width."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s04",
        "band": "standard",
        "text": "What does a convex lens do that a pinhole cannot?",
        "options": [
            {"text": "Turn the picture the right way up", "correct": False,
             "why": "It does not. The rays still cross, so the picture is "
                    "still inverted."},
            {"text": "Make the picture bigger without moving the object or "
                     "lengthening the box", "correct": False,
             "why": "Size is set by the distances, with a lens as with a "
                    "hole."},
            {"text": "Let a wide opening be used and still bring each point "
                     "back to a point", "correct": True},
            {"text": "Work without any light at all", "correct": False,
             "why": "A lens gathers light. With none arriving there is "
                    "nothing to gather."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-04-h01",
        "band": "harder",
        "text": "On a sunny day the gaps between leaves cast round bright "
                "patches on the ground rather than leaf-shaped ones. Why?",
        "options": [
            {"text": "Each gap is acting as a pinhole and the round patch "
                     "is a picture of the Sun", "correct": True},
            {"text": "The leaves scatter the light into circles",
             "correct": False,
             "why": "Scattering would blur the patch out, not give it a "
                    "sharp round edge."},
            {"text": "Sunlight is naturally circular in cross-section",
             "correct": False,
             "why": "Sunlight fills the whole sky. The shape comes from the "
                    "Sun being round and the gap acting as a hole."},
            {"text": "The ground refracts the light into a disc, because a "
                     "rough surface rounds off any shape that lands on it",
             "correct": False,
             "why": "Nothing enters the ground. The patch is formed before "
                    "the light lands."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h02",
        "band": "harder",
        "text": "During a partial solar eclipse those same patches become "
                "crescent-shaped. What does that show about them?",
        "options": [
            {"text": "That the leaves have moved into a crescent "
                     "arrangement", "correct": False,
             "why": "The leaves are unchanged. The patches change with the "
                    "Sun."},
            {"text": "That the light is bending round the Moon",
             "correct": False,
             "why": "Light travels in straight lines here. Nothing bends "
                    "round the Moon."},
            {"text": "That each patch really is a picture of the Sun, so it "
                     "takes whatever shape the Sun has", "correct": True},
            {"text": "That the eclipse changes the colour and shape of "
                     "sunlight itself, so everything lit by it takes that "
                     "shape", "correct": False,
             "why": "The Sun's light is the same light. What has changed is "
                    "how much of the Sun's disc is visible."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h03",
        "band": "harder",
        "text": "A photographer in poor light opens the aperture wide and "
                "the background goes soft while the subject stays sharp. "
                "How does that compare with a pinhole?",
        "options": [
            {"text": "It is the same effect: a wide opening always blurs "
                     "everything equally", "correct": False,
             "why": "A lens is focused on ONE distance, so what happens "
                    "depends on where a thing is. A pinhole has no such "
                    "distance."},
            {"text": "It shows a lens does not really focus at all",
             "correct": False,
             "why": "It shows the opposite: something is exactly in focus, "
                    "which is why everything else is not."},
            {"text": "A pinhole would have kept the background sharp "
                     "because it lets in less light, and the less light a "
                     "picture is made from the sharper it is",
             "correct": False,
             "why": "It would keep the background as sharp as everything "
                    "else — but the reason is the ray selection, not the "
                    "amount of light."},
            {"text": "A pinhole's blur grows with the hole and does not "
                     "depend on distance; a lens is sharp at one distance "
                     "and softer away from it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h04",
        "band": "harder",
        "text": "A student proposes making a pinhole camera sharper and "
                "sharper by making the hole smaller and smaller. Where does "
                "this run out?",
        "options": [
            {"text": "It never runs out — the smaller the hole, the sharper "
                     "the picture, and there is no size at which that stops "
                     "being true", "correct": False,
             "why": "It stops improving, and past a point it gets worse. "
                    "There is a best hole size for any box."},
            {"text": "The picture gets so dim that there is nothing left to "
                     "look at, and very narrow holes start to spread the "
                     "light again", "correct": True},
            {"text": "The picture starts coming out the right way up",
             "correct": False,
             "why": "Nothing about the hole size changes the crossing. It "
                    "stays inverted."},
            {"text": "The picture shrinks until it disappears",
             "correct": False,
             "why": "The size never depends on the hole. Only the object "
                    "distance and the box length set it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-04-e05",
        "band": "easier",
        "text": "Light travels in…",
        "options": [            {"text": "whichever direction the eye is looking", "correct": False,
             "why": "The eye receives light; it does not steer it."},
            {"text": "curves that follow the shape of the room",
             "correct": False,
             "why": "If it curved round obstacles there would be no sharp "
                    "shadows."},
            {"text": "circles around a source", "correct": False,
             "why": "It spreads outwards from a source, but each ray runs "
                    "straight."},
            {"text": "straight lines, in every direction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e06",
        "band": "easier",
        "text": "Widening the hole of a pinhole camera makes the picture…",
        "options": [
            {"text": "brighter and sharper", "correct": False,
             "why": "It is brighter, but overlapping patches of light make it "
                    "blurred, not sharper."},
            {"text": "brighter and blurrier", "correct": True},
            {"text": "dimmer and sharper", "correct": False,
             "why": "That is what NARROWING the hole does."},
            {"text": "bigger and brighter", "correct": False,
             "why": "The size is set by the object's distance and the box's "
                    "length, not by the hole."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e07",
        "band": "easier",
        "text": "A convex lens brings all the rays leaving one point of an "
                "object to…",
        "options": [
            {"text": "one point on the screen", "correct": True},
            {"text": "a spread of points across the whole screen",
             "correct": False,
             "why": "That is what a wide pinhole does, and it is why a wide "
                    "pinhole blurs."},
            {"text": "the edge of the screen", "correct": False,
             "why": "Where the point lands depends on where the object point "
                    "is, not on the edge."},
            {"text": "a point in front of the lens", "correct": False,
             "why": "The rays are brought together beyond the lens, on the "
                    "screen side."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-04-s05",
        "band": "standard",
        "text": "A pinhole box giving a 20 mm picture is made three times as "
                "long, with the object left where it was. The picture becomes…",
        "options": [
            {"text": "60 mm tall", "correct": True},
            {"text": "20 mm tall, because the object has not moved",
             "correct": False,
             "why": "The box length is one of the two things that set the "
                    "size, and it has changed."},
            {"text": "about 7 mm tall", "correct": False,
             "why": "A longer box gives a BIGGER picture, not a smaller one."},
            {"text": "60 mm tall and the right way up", "correct": False,
             "why": "The height is right, but the rays still cross at the "
                    "hole, so it stays inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s06",
        "band": "standard",
        "text": "The object in front of a pinhole camera is moved closer, "
                "with the box unchanged. What happens to the picture?",
        "options": [
            {"text": "It gets smaller", "correct": False,
             "why": "Moving closer makes the picture larger, as it does with "
                    "any camera."},
            {"text": "It gets bigger", "correct": True},
            {"text": "It stays the same size but gets brighter",
             "correct": False,
             "why": "It does get brighter, but the size changes as well."},
            {"text": "It turns the right way up", "correct": False,
             "why": "The rays still cross at the hole whatever the distance, "
                    "so it stays inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s07",
        "band": "standard",
        "text": "Which change makes a pinhole picture brighter without "
                "changing its size?",
        "options": [
            {"text": "Making the box longer", "correct": False,
             "why": "That makes the picture bigger and dimmer, so the size "
                    "does change."},
            {"text": "Moving the object closer", "correct": False,
             "why": "That makes the picture bigger too, so the size does not "
                    "hold still."},
            {"text": "Widening the hole", "correct": True},
            {"text": "Using a brighter screen", "correct": False,
             "why": "The screen does not add light; it only shows what "
                    "arrives on it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-04-h05",
        "band": "harder",
        "text": "A convex lens replaces the pinhole in the same box. What "
                "changes, and what stays the same?",
        "options": [
            {"text": "It becomes bright and sharp at once, and stays upside "
                     "down",
             "correct": True},
            {"text": "It becomes bright and sharp at once, and turns the "
                     "right way up",
             "correct": False,
             "why": "The rays still cross on their way to the screen, so the "
                    "picture is still inverted."},
            {"text": "It becomes sharper but dimmer, and stays upside down",
             "correct": False,
             "why": "The lens gathers a wide beam, so it is brighter than a "
                    "pinhole, not dimmer."},
            {"text": "Nothing changes, because light still travels in "
                     "straight lines",
             "correct": False,
             "why": "It does, but the lens refracts each ray, which is "
                    "exactly what a pinhole cannot do."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h06",
        "band": "harder",
        "text": "A 100 mm pinhole box gives a 25 mm picture of an object 1000 "
                "mm tall. How far away is the object?",
        "options": [
            {"text": "250 mm", "correct": False,
             "why": "That is 25 × 10, which does not follow from the "
                    "proportion between the two pairs."},
            {"text": "4000 mm", "correct": True},
            {"text": "2500 mm", "correct": False,
             "why": "That is 25 × 100, and the object height has been left "
                    "out."},
            {"text": "40 mm", "correct": False,
             "why": "That is a hundred times too small — the object is much "
                    "further away than the box is long."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h07",
        "band": "harder",
        "text": "A wide hole blurs the picture, but a wide lens does not. "
                "Why?",
        "options": [
            {"text": "Because a lens is smaller than the hole it replaces",
             "correct": False,
             "why": "A camera lens is usually much wider, which is the whole "
                    "point of using one."},
            {"text": "Because a lens lets less light through, so there is "
                     "less to blur",
             "correct": False,
             "why": "It lets far more through, and the picture is brighter "
                    "for it."},
            {"text": "Because a lens refracts every ray from one object point "
                     "back to one screen point",
             "correct": True},
            {"text": "Because a lens makes light travel in curves rather than "
                     "straight lines",
             "correct": False,
             "why": "Each ray still runs straight; the lens changes its "
                    "direction at the glass."},
        ],
        "figure": None,
    },
]
