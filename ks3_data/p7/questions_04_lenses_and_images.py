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

    # ── MRB-338 night 3 · easier ───────────────────────────────────────
    {
        "id": "p7-04-e08",
        "band": "easier",
        "text": "Does a convex lens turn a picture the right way up?",
        "options": [
            {"text": "No — the rays always cross, so the picture stays "
                     "upside down", "correct": True},
            {"text": "Yes — focusing the rays also turns the picture the "
                     "right way up", "correct": False,
             "why": "Focusing brings each point back together; it does "
                    "nothing about which way up the picture is."},
            {"text": "Yes, but only for very wide lenses", "correct": False,
             "why": "The width of the lens changes brightness and "
                    "sharpness, not whether the picture is inverted."},
            {"text": "It depends on how far the screen is from the lens",
             "correct": False,
             "why": "Screen distance changes the picture's size and "
                    "sharpness, not whether the rays have crossed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e09",
        "band": "easier",
        "text": "A pinhole selects one ray from each object point; a lens…",
        "options": [
            {"text": "selects two rays from each point instead of one",
             "correct": False,
             "why": "A lens does not limit itself to two rays — it "
                    "collects a whole wide bundle from each point."},
            {"text": "collects a wide bundle of rays from each point and "
                     "brings them back together", "correct": True},
            {"text": "blocks every single ray except the one travelling "
                     "exactly along the normal direction", "correct": False,
             "why": "A lens lets a wide spread of rays through and bends "
                    "each one so they meet again, rather than blocking "
                    "most of them."},
            {"text": "removes the need for any rays to reach the screen at all", "correct": False,
             "why": "Rays still have to reach the screen for a picture "
                    "to form; a lens simply manages many more of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e10",
        "band": "easier",
        "text": "Each separate point on a brightly lit object throws its "
                "light out…",
        "options": [
            {"text": "only towards whichever hole or lens happens to be "
                     "nearest to it", "correct": False,
             "why": "The light leaves in all directions; a hole simply "
                    "catches the one ray that happens to be aimed at it."},
            {"text": "as a single narrow beam, pointing straight ahead of "
                     "the object", "correct": False,
             "why": "A lit object is not a beam source. Only a laser "
                    "sends light out as one narrow beam."},
            {"text": "in every direction", "correct": True},
            {"text": "only once a lens has been put in front of it to "
                     "start the light off", "correct": False,
             "why": "The object throws light out whether or not a lens is "
                    "there; a lens only redirects light that already is."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e11",
        "band": "easier",
        "text": "Widening or narrowing a pinhole camera's hole changes the "
                "blur and the brightness. Does it change the picture's "
                "position or size?",
        "options": [
            {"text": "It changes the size but not the position",
             "correct": False,
             "why": "The hole width changes neither of these — only the "
                    "blur and the brightness."},
            {"text": "Yes — a wider hole always makes the picture sit "
                     "higher on the screen", "correct": False,
             "why": "Where the picture falls on the screen is set by the "
                    "object and the box, not by the hole's width."},
            {"text": "Yes — a wider hole always makes the picture "
                     "bigger", "correct": False,
             "why": "Picture size is set by the object's distance and "
                    "the box's length; the hole's width does not enter "
                    "into it."},
            {"text": "No — the hole width never changes either the "
                     "position or the size", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e12",
        "band": "easier",
        "text": "Why must the inside of a pinhole camera's box be dark?",
        "options": [
            {"text": "So that the only light landing on the screen is the "
                     "light that came in through the hole", "correct": True},
            {"text": "So that the light is slowed down a little on its "
                     "way across the box to the screen", "correct": False,
             "why": "Nothing inside the box changes the light's speed; "
                    "the air inside is the same as the air outside."},
            {"text": "So that the hole can be widened without the picture "
                     "blurring", "correct": False,
             "why": "How blurred the picture is depends on the hole's "
                    "width alone; a dark interior does nothing to it."},
            {"text": "So that the picture comes out bigger than it "
                     "otherwise would", "correct": False,
             "why": "The picture's size is set by the object's distance "
                    "and the box's length, not by how dark it is inside."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e13",
        "band": "easier",
        "text": "Does a pinhole camera need a lens to form a picture?",
        "options": [
            {"text": "Yes — without a lens no picture can form at all",
             "correct": False,
             "why": "A small hole on its own forms a picture perfectly "
                    "well, just a dimmer and less sharp one than a lens "
                    "gives."},
            {"text": "No — a small hole on its own is always enough",
             "correct": True},
            {"text": "Yes, but only if the hole is extremely wide",
             "correct": False,
             "why": "Even a very narrow hole forms a picture; a lens is "
                    "not required at any hole width."},
            {"text": "No, but it needs a mirror instead", "correct": False,
             "why": "No mirror is used in a pinhole camera; light passes "
                    "straight through the hole to the screen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e14",
        "band": "easier",
        "text": "What forms the picture in the simplest kind of camera, "
                "using no lens or mirror at all?",
        "options": [
            {"text": "A coating of silver on the inside of the box",
             "correct": False,
             "why": "No coating is needed; a plain hole in an otherwise "
                    "dark box is enough."},
            {"text": "A curved sheet of glass", "correct": False,
             "why": "That describes a lens, which this simplest kind of "
                    "camera does not use."},
            {"text": "A single small hole", "correct": True},
            {"text": "A battery-powered light sensor", "correct": False,
             "why": "No electronics are involved; the picture forms "
                    "purely from light travelling in straight lines."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e15",
        "band": "easier",
        "text": "In a pinhole camera, what is the screen's job?",
        "options": [
            {"text": "To narrow the hole automatically so that the "
                     "picture comes out sharper", "correct": False,
             "why": "The hole itself sets the sharpness; the screen only "
                    "shows the result."},
            {"text": "To bend the light back the way it came",
             "correct": False,
             "why": "The screen does not reflect the light back out; it "
                    "simply shows the picture the light has already "
                    "formed."},
            {"text": "To create the light that forms the picture",
             "correct": False,
             "why": "The screen makes no light of its own; it shows the "
                    "light arriving from the object."},
            {"text": "To show the picture formed by the light that "
                     "crosses at the hole", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e16",
        "band": "easier",
        "text": "Does a pinhole camera's picture reverse left-to-right as "
                "well as turning upside down?",
        "options": [
            {"text": "Yes — both always happen together", "correct": True},
            {"text": "No — only up and down are swapped",
             "correct": False,
             "why": "The crossing at the hole happens in every direction "
                    "at once, so left and right swap too."},
            {"text": "No — only left and right are swapped",
             "correct": False,
             "why": "Up and down are swapped as well; both directions "
                    "reverse together."},
            {"text": "It depends on which way round the object is facing",
             "correct": False,
             "why": "Both reversals happen for any object, whichever "
                    "way it faces."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e17",
        "band": "easier",
        "text": "Moving the object further from a pinhole camera, with the "
                "box unchanged, makes the picture…",
        "options": [
            {"text": "bigger", "correct": False,
             "why": "Moving further away makes the picture smaller, not "
                    "bigger — moving closer is what enlarges it."},
            {"text": "smaller", "correct": True},
            {"text": "the same size, but dimmer", "correct": False,
             "why": "The size changes too, not just the brightness."},
            {"text": "the right way up instead of upside down",
             "correct": False,
             "why": "Object distance changes the picture's size, not "
                    "whether it is inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e18",
        "band": "easier",
        "text": "Making a pinhole camera's box longer, with everything else "
                "unchanged, makes the picture…",
        "options": [
            {"text": "sharper", "correct": False,
             "why": "Sharpness is set by the hole width, not by the box "
                    "length."},
            {"text": "smaller", "correct": False,
             "why": "A longer box makes the picture bigger, not "
                    "smaller."},
            {"text": "bigger", "correct": True},
            {"text": "the right way up", "correct": False,
             "why": "Box length changes size, not whether the picture is "
                    "inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e19",
        "band": "easier",
        "text": "Compared with a similarly sized pinhole, does a lens "
                "usually let in more or less light while staying sharp?",
        "options": [
            {"text": "It depends only on the colour of the object being "
                     "photographed", "correct": False,
             "why": "The object's colour does not decide how much light "
                    "gets through the opening."},
            {"text": "Less — lenses always let in less light than a "
                     "pinhole of the same size", "correct": False,
             "why": "A lens is exactly what lets a WIDER, brighter "
                    "opening be used without losing sharpness."},
            {"text": "Exactly the same amount, always", "correct": False,
             "why": "A lens can be made much wider than a pinhole while "
                    "keeping the picture sharp, letting in more light."},
            {"text": "More — a lens can use a much wider opening and "
                     "still stay sharp", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e20",
        "band": "easier",
        "text": "Why should you never look directly at the Sun through a "
                "lens?",
        "options": [
            {"text": "A lens focuses sunlight to a point hot enough to "
                     "damage the eye", "correct": True},
            {"text": "The lens might crack from the heat of the "
                     "sunlight", "correct": False,
             "why": "The real danger is to the EYE, not to the lens "
                    "itself."},
            {"text": "Sunlight becomes a different colour after passing "
                     "through a lens", "correct": False,
             "why": "The colour of the light is not what makes this "
                    "dangerous — the concentrated heat at the focus is."},
            {"text": "A lens makes the Sun look much further away than it "
                     "really is", "correct": False,
             "why": "Apparent distance is not the danger here; the real "
                    "hazard is the concentrated heat a lens produces."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e21",
        "band": "easier",
        "text": "According to the safety guidance for this equipment, "
                "which of these are all unsafe ways to look at the Sun?",
        "options": [
            {"text": "Only directly with your eyes — a lens or a pinhole "
                     "camera make it safe", "correct": False,
             "why": "A lens and a pinhole camera are both named as unsafe "
                    "too, not just looking with the naked eye."},
            {"text": "Directly with your eyes, through a lens, and "
                     "through a pinhole camera", "correct": True},
            {"text": "Only through a lens — the eyes and a pinhole "
                     "camera are both safe", "correct": False,
             "why": "Looking directly with the eyes, or through a "
                    "pinhole camera, are both named as unsafe as well."},
            {"text": "None of these — a lens actually makes looking at the Sun "
                     "safer", "correct": False,
             "why": "A lens makes looking at the Sun MORE dangerous, by "
                    "focusing the light to a damaging point."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e22",
        "band": "easier",
        "text": "Does eye damage from looking at sunlight focused by a "
                "lens happen painfully, so you would know to stop?",
        "options": [
            {"text": "Yes, but only after several minutes",
             "correct": False,
             "why": "There is no pain at any point during the damage, "
                    "immediate or delayed."},
            {"text": "Yes — it causes immediate, sharp pain",
             "correct": False,
             "why": "The damage happens painlessly, which is exactly why "
                    "the warning has to be given in advance."},
            {"text": "No — it is never painful while it happens",
             "correct": True},
            {"text": "It depends on how bright the Sun is that day",
             "correct": False,
             "why": "The painlessness does not depend on how bright the "
                    "day happens to be."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e23",
        "band": "easier",
        "text": "Does eye damage from looking at focused sunlight heal "
                "over time?",
        "options": [
            {"text": "It heals faster in bright light than in dim light",
             "correct": False,
             "why": "It does not heal in either case — the damage is "
                    "permanent."},
            {"text": "Yes — it always heals within a few days",
             "correct": False,
             "why": "This kind of damage does not heal at all, which is "
                    "exactly why the warning is so serious."},
            {"text": "Yes, as long as you rest your eyes afterwards",
             "correct": False,
             "why": "Resting the eyes does not reverse damage of this "
                    "kind; it does not heal."},
            {"text": "No — it never heals", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e24",
        "band": "easier",
        "text": "Which two things set the size of a pinhole camera's "
                "picture?",
        "options": [
            {"text": "How far away the object is, and how long the box "
                     "is", "correct": True},
            {"text": "The hole's width and the screen's colour",
             "correct": False,
             "why": "Neither of these sets the size; the hole affects "
                    "blur and brightness, and the screen's colour "
                    "affects nothing about the picture's size."},
            {"text": "How bright the object is, and how dark the room "
                     "is", "correct": False,
             "why": "Brightness of the object or the room changes how "
                    "easily the picture is seen, not how big it is."},
            {"text": "The hole's width and the object's colour",
             "correct": False,
             "why": "Neither the hole's width nor the object's colour "
                    "sets the picture's size."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e25",
        "band": "easier",
        "text": "Do both a pinhole camera and a camera using a lens form "
                "their picture on a screen?",
        "options": [
            {"text": "No — only the pinhole camera actually needs a screen at "
                     "all", "correct": False,
             "why": "A lens camera also needs a screen, or sensor, for "
                    "the focused rays to land on."},
            {"text": "Yes — both need a screen for the picture to land "
                     "on", "correct": True},
            {"text": "No — only the lens camera uses a screen",
             "correct": False,
             "why": "A pinhole camera needs a screen too, for the "
                    "crossed rays to fall on."},
            {"text": "No — neither one needs a screen at all",
             "correct": False,
             "why": "Both kinds of camera need somewhere for the light "
                    "to land and form a visible picture."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e26",
        "band": "easier",
        "text": "True or false: light travelling in straight lines is why "
                "a pinhole picture comes out inverted.",
        "options": [
            {"text": "False — the inversion is caused by the box's "
                     "material absorbing some of the light",
             "correct": False,
             "why": "Absorption in the box has nothing to do with why "
                    "the picture is inverted."},
            {"text": "False — the inversion happens because the hole "
                     "reverses the light like a mirror", "correct": False,
             "why": "No mirror or reversal happens at the hole itself; "
                    "the rays simply carry on in the straight line they "
                    "were already travelling in."},
            {"text": "True", "correct": True},
            {"text": "True — and it is also why the picture comes out the same "
                     "size as the object", "correct": False,
             "why": "The first half is right and the second is not: the "
                    "picture's size is set by the object's distance and "
                    "the box's length, and is rarely the object's size."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e27",
        "band": "easier",
        "text": "Does widening a pinhole change how many rays from each "
                "object point reach the screen?",
        "options": [
            {"text": "It depends on the colour of the object's light",
             "correct": False,
             "why": "The number of rays getting through depends on the "
                    "hole's width, not on the colour of the light."},
            {"text": "No — exactly one ray always gets through, however "
                     "wide the hole is", "correct": False,
             "why": "A wider hole lets a whole bundle of rays from each "
                    "point through, not just the single ray a narrow "
                    "hole selects."},
            {"text": "No — widening the hole stops any rays getting through at "
                     "all", "correct": False,
             "why": "Widening the hole lets MORE rays through, not "
                    "fewer — that is exactly why the picture brightens."},
            {"text": "Yes — a small bundle of rays gets through, not "
                     "only the single one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e28",
        "band": "easier",
        "text": "Is the round patch of light under a tree on a sunny day a "
                "picture of the leaves, or of something else?",
        "options": [
            {"text": "A picture of the Sun", "correct": True},
            {"text": "A picture of the leaves themselves", "correct": False,
             "why": "The gaps between the leaves act as the pinholes; "
                    "the round shape comes from the Sun, not from the "
                    "shape of the leaves."},
            {"text": "A picture of the tree's whole shadow",
             "correct": False,
             "why": "The shadow is the dark shape the tree blocks; the "
                    "bright round patch is a separate effect from the "
                    "gaps acting as pinholes."},
            {"text": "Nothing in particular — the shape is completely "
                     "random", "correct": False,
             "why": "The round shape is not random; it consistently "
                    "matches the round shape of the Sun."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e29",
        "band": "easier",
        "text": "Does a pinhole camera's picture ever come out the right "
                "way up, for any hole size or box length?",
        "options": [
            {"text": "Yes, if the hole is made wide enough",
             "correct": False,
             "why": "Widening the hole changes the blur and brightness, "
                    "not whether the picture is inverted."},
            {"text": "No — it is always inverted, whatever the hole size "
                     "or box length", "correct": True},
            {"text": "Yes, if the box is made short enough",
             "correct": False,
             "why": "Shortening the box changes the picture's size, not "
                    "whether it is inverted."},
            {"text": "Yes, if the object itself is deliberately turned "
                     "upside down first", "correct": False,
             "why": "Turning the object upside down would simply make "
                    "an already-inverted picture look the right way up "
                    "by coincidence — the crossing at the hole itself "
                    "still inverts it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-e30",
        "band": "easier",
        "text": "Does a convex lens replace the need for a screen?",
        "options": [
            {"text": "Yes, because a lens produces its own light source",
             "correct": False,
             "why": "A lens produces no light of its own; it only "
                    "refracts light that is already there."},
            {"text": "Yes — the lens itself displays the finished picture "
                     "directly, with no screen needed at all",
             "correct": False,
             "why": "A lens only bends light to bring it to a focus; "
                    "the picture still needs a screen to land on."},
            {"text": "No — the lens focuses the light, but a screen is "
                     "always still needed to show the picture",
             "correct": True},
            {"text": "It depends on how curved the lens is",
             "correct": False,
             "why": "However curved the lens, a screen is still needed "
                    "for the focused rays to land on and be seen."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p7-04-s08",
        "band": "standard",
        "text": "Bringing an object in to half its original distance, "
                "keeping the same box, changes the picture's height "
                "to…",
        "options": [
            {"text": "twice as tall", "correct": True},
            {"text": "half as tall", "correct": False,
             "why": "Moving the object CLOSER makes the picture bigger, "
                    "not smaller."},
            {"text": "the same height", "correct": False,
             "why": "Object distance is one of the two things that set "
                    "the picture's height."},
            {"text": "four times as tall", "correct": False,
             "why": "Halving the distance doubles the height; nothing "
                    "here squares the change."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s09",
        "band": "standard",
        "text": "Shortening a pinhole box to half its length, without "
                "moving the object at all, leaves the picture…",
        "options": [
            {"text": "twice as tall", "correct": False,
             "why": "A SHORTER box gives a smaller picture, not a bigger "
                    "one."},
            {"text": "half as tall", "correct": True},
            {"text": "the same height", "correct": False,
             "why": "Box length is one of the two things that set the "
                    "picture's height."},
            {"text": "a quarter as tall", "correct": False,
             "why": "Halving the box length halves the height; nothing "
                    "here squares the change."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s10",
        "band": "standard",
        "text": "A pinhole camera's box length is doubled, and the object "
                "is also moved to twice its original distance. What "
                "happens to the picture's height?",
        "options": [
            {"text": "It becomes four times as tall", "correct": False,
             "why": "The two changes work against each other here, not "
                    "with each other — they cancel out rather than "
                    "combining."},
            {"text": "It doubles", "correct": False,
             "why": "Doubling the box length alone would double the "
                    "height, but doubling the distance at the same time "
                    "halves it back again."},
            {"text": "It stays exactly the same", "correct": True},
            {"text": "It shrinks to a quarter of its original height",
             "correct": False,
             "why": "The two effects exactly cancel out, leaving the "
                    "height unchanged rather than shrinking it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s11",
        "band": "standard",
        "text": "A pinhole's diameter is doubled. Roughly how many times "
                "brighter does the picture become, given that brightness "
                "follows the area of the hole?",
        "options": [
            {"text": "About twice as bright", "correct": False,
             "why": "Brightness follows the AREA of the hole, which "
                    "grows with the square of the diameter, not the "
                    "diameter itself."},
            {"text": "No brighter at all, since only the sharpness changes", "correct": False,
             "why": "Brightness changes a great deal with hole size; it "
                    "is the picture's SIZE that stays the same, not its "
                    "brightness."},
            {"text": "About eight times as bright", "correct": False,
             "why": "Doubling the diameter squares to four, not eight — "
                    "check the area calculation again."},
            {"text": "About four times as bright", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s12",
        "band": "standard",
        "text": "A photographer using a pinhole camera wants a brighter "
                "picture WITHOUT any change in sharpness. Is this "
                "possible by adjusting the hole alone?",
        "options": [
            {"text": "No — brightness and sharpness are linked through "
                     "the hole size, so changing one changes the other",
             "correct": True},
            {"text": "Yes — widening the hole always brightens the picture "
                     "without ever affecting its sharpness at all", "correct": False,
             "why": "Widening the hole brightens the picture but also "
                    "blurs it — the two effects come together."},
            {"text": "Yes — narrowing the hole brightens the picture "
                     "while sharpening it", "correct": False,
             "why": "Narrowing the hole sharpens the picture, but it "
                    "dims it rather than brightening it."},
            {"text": "It is impossible to change brightness at all using the "
                     "hole", "correct": False,
             "why": "The hole is exactly what controls brightness; "
                    "widening or narrowing it changes how much light "
                    "gets through."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s13",
        "band": "standard",
        "text": "Why can a lens camera take a bright AND sharp photo in "
                "dim light, where a pinhole camera cannot?",
        "options": [
            {"text": "The lens makes the dim light brighter by adding "
                     "energy of its own", "correct": False,
             "why": "A lens adds no energy of its own; it only refracts "
                    "the light that is already arriving."},
            {"text": "The lens focuses a wide bundle of rays from each "
                     "point back to one point, so a wide opening does "
                     "not cost any sharpness", "correct": True},
            {"text": "The lens narrows the field of view so less light "
                     "is needed overall", "correct": False,
             "why": "Field of view is not what solves the pinhole's "
                    "trade-off — bringing a wide bundle back to a point "
                    "is."},
            {"text": "The lens removes the need for the picture to be "
                     "inverted, which frees up the light that would otherwise "
                     "be lost as the rays cross", "correct": False,
             "why": "The picture is still inverted with a lens; "
                    "inversion has no connection to how much light "
                    "reaches the screen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s14",
        "band": "standard",
        "text": "A pinhole box is 200 mm long and produces a 50 mm picture "
                "of an object 2000 mm away. How tall is the object?",
        "options": [
            {"text": "5000 mm", "correct": False,
             "why": "That is ten times too tall — check which figures "
                    "are multiplied and which are divided."},
            {"text": "200 mm", "correct": False,
             "why": "That confuses the object's height with the box "
                    "length given in the question."},
            {"text": "500 mm", "correct": True},
            {"text": "50 mm", "correct": False,
             "why": "That is the picture's height, not the real "
                    "object's height, which is much greater at this "
                    "distance."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s15",
        "band": "standard",
        "text": "Which change would make a pinhole picture SMALLER: "
                "moving the object closer, or shortening the box?",
        "options": [
            {"text": "Moving the object closer", "correct": False,
             "why": "Moving closer makes the picture BIGGER, not "
                    "smaller — shortening the box is the one that "
                    "shrinks it."},
            {"text": "Neither change affects the picture's size at all",
             "correct": False,
             "why": "Both object distance and box length are among the "
                    "two things that do set the picture's size."},
            {"text": "Both changes make the picture bigger",
             "correct": False,
             "why": "Shortening the box makes the picture smaller, "
                    "while moving closer makes it bigger — they do not "
                    "act the same way."},
            {"text": "Shortening the box", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s16",
        "band": "standard",
        "text": "An object's distance from a pinhole camera is HALVED "
                "while the box length is DOUBLED, both at once. What "
                "happens to the picture's height?",
        "options": [
            {"text": "It becomes four times as tall", "correct": True},
            {"text": "It stays the same", "correct": False,
             "why": "Both changes here act to make the picture BIGGER, "
                    "so they do not cancel out this time."},
            {"text": "It becomes twice as tall", "correct": False,
             "why": "Both effects combine here rather than only one "
                    "acting alone — halving the distance and doubling "
                    "the box each double the height on their own."},
            {"text": "It shrinks to a quarter of its original height",
             "correct": False,
             "why": "Both changes act to enlarge the picture, not to "
                    "shrink it, since the object is now closer and the "
                    "box is longer."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s17",
        "band": "standard",
        "text": "Sunlight through small gaps in a woven cycling pannier "
                "bag casts small bright dots on the ground. Are these "
                "dots pictures of the gaps, or of the Sun?",
        "options": [
            {"text": "Pictures of the gaps' own shapes, whatever shape "
                     "they happen to be", "correct": False,
             "why": "The dots consistently come out round, matching the "
                    "Sun's shape, whatever shape the gaps themselves "
                    "are."},
            {"text": "Pictures of the Sun, since each small gap acts as "
                     "a pinhole", "correct": True},
            {"text": "Pictures of the weave pattern of the whole bag",
             "correct": False,
             "why": "Each dot is a separate small picture formed by one "
                    "gap, not a picture of the bag's overall weave."},
            {"text": "Not pictures of anything — just scattered "
                     "sunlight with no particular shape", "correct": False,
             "why": "The consistently round shape shows these are "
                    "genuine pinhole pictures of the round Sun, not "
                    "random scattered light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s18",
        "band": "standard",
        "text": "A pinhole camera's screen is moved further from the hole, "
                "with nothing else changed. Does this behave like "
                "lengthening the box?",
        "options": [
            {"text": "No — only physically extending the box's own solid walls "
                     "counts as truly lengthening it",
             "correct": False,
             "why": "What actually matters is the hole-to-screen "
                    "distance itself, however that distance is achieved."},
            {"text": "No — moving the screen has no effect on the picture at "
                     "all", "correct": False,
             "why": "Moving the screen further from the hole does "
                    "change the picture — it behaves exactly like "
                    "lengthening the box."},
            {"text": "Yes — the box length that matters is only the "
                     "distance from the hole to the screen", "correct": True},
            {"text": "It behaves like widening the hole instead",
             "correct": False,
             "why": "Widening the hole changes blur and brightness; "
                    "moving the screen further away changes the "
                    "picture's size, which is what a longer box does."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s19",
        "band": "standard",
        "text": "A student increases both the object's distance and "
                "widens the hole at the same time. Which property "
                "changes because of the distance change, and which "
                "changes because of the hole change?",
        "options": [
            {"text": "Both changes affect only the blur and brightness, "
                     "and neither affects the height", "correct": False,
             "why": "The distance change affects the picture's height, "
                    "not its blur or brightness."},
            {"text": "The picture's height changes because of the hole; "
                     "its blur and brightness change because of the "
                     "distance", "correct": False,
             "why": "That swaps the two controls round — height is set "
                    "by object distance and box length, while blur and "
                    "brightness are set by the hole."},
            {"text": "Both changes affect only the height, and neither "
                     "affects blur or brightness", "correct": False,
             "why": "The hole change affects blur and brightness, not "
                    "the picture's height at all."},
            {"text": "The picture's height changes because of the "
                     "distance; its blur and brightness change because "
                     "of the hole", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s20",
        "band": "standard",
        "text": "Why does an eclipse-projector box, a pinhole box aimed "
                "at the Sun, usually need to be fairly long to show a "
                "decent-sized picture?",
        "options": [
            {"text": "Because the picture's height always depends on the "
                     "box length, and the Sun is an extremely distant "
                     "object", "correct": True},
            {"text": "Because a longer box lets more sunlight in "
                     "through the hole", "correct": False,
             "why": "The amount of light getting in depends on the "
                    "hole's width, not on how long the box is."},
            {"text": "Because a longer box is needed to keep the "
                     "picture the right way up", "correct": False,
             "why": "Box length changes the picture's size, not "
                    "whether it is inverted — it stays inverted "
                    "whatever the length."},
            {"text": "Because the Sun's light genuinely needs the extra "
                     "distance inside the box to slow down enough to be "
                     "properly seen", "correct": False,
             "why": "Light does not need to slow down to be seen; the "
                    "box length simply sets how big the picture comes "
                    "out."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s21",
        "band": "standard",
        "text": "An object 400 mm tall stands 800 mm from a pinhole "
                "camera with a 150 mm long box. How tall is the "
                "picture?",
        "options": [
            {"text": "150 mm", "correct": False,
             "why": "That copies the box length directly rather than "
                    "using it in the ratio with the object's height and "
                    "distance."},
            {"text": "75 mm", "correct": True},
            {"text": "7.5 mm", "correct": False,
             "why": "That is ten times too small — check the "
                    "multiplication and division in the ratio again."},
            {"text": "800 mm", "correct": False,
             "why": "That is the object's distance, not the picture's "
                    "height, which comes out much smaller than this."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s22",
        "band": "standard",
        "text": "Which setup would give the LARGEST picture: an object "
                "very close with a very long box, or an object very "
                "close with a very short box?",
        "options": [
            {"text": "Both give exactly the same size of picture",
             "correct": False,
             "why": "Box length is one of the two things that set the "
                    "picture's size, so a longer box gives a bigger "
                    "picture."},
            {"text": "Object very close, very short box",
             "correct": False,
             "why": "A short box gives a smaller picture than a long "
                    "one, even with the object equally close in both "
                    "cases."},
            {"text": "Object very close, very long box", "correct": True},
            {"text": "Neither can be compared without knowing the hole "
                     "size too", "correct": False,
             "why": "Hole size affects blur and brightness, not the "
                    "picture's size, so it is not needed to compare "
                    "these two setups."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s23",
        "band": "standard",
        "text": "A student wants a SHARPER pinhole picture without losing "
                "any brightness. Is there a hole-width change that "
                "achieves both at once?",
        "options": [
            {"text": "Yes, by choosing exactly the right box length "
                     "instead of changing the hole", "correct": False,
             "why": "Box length does not affect sharpness at all; only "
                    "the hole width controls the blur."},
            {"text": "Yes — narrowing the hole down always sharpens the "
                     "picture and brightens it together at the very "
                     "same time, whatever box length happens to be "
                     "used", "correct": False,
             "why": "Narrowing the hole sharpens the picture but dims "
                    "it — the two effects pull in opposite directions."},
            {"text": "Yes — widening the hole always sharpens and "
                     "brightens the picture together", "correct": False,
             "why": "Widening the hole brightens the picture but blurs "
                    "it, rather than sharpening it as well."},
            {"text": "No — narrowing always sharpens but dims, and "
                     "widening always brightens but blurs; a lens would "
                     "be needed to get both at once", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s24",
        "band": "standard",
        "text": "Which property of a pinhole picture NEVER changes, "
                "whatever you adjust about the hole width, box length "
                "or object distance?",
        "options": [
            {"text": "That the picture is inverted — it never comes out "
                     "the right way up", "correct": True},
            {"text": "How bright the picture is", "correct": False,
             "why": "Brightness changes with the hole width, so it is "
                    "not something that stays fixed."},
            {"text": "How sharp the picture is", "correct": False,
             "why": "Sharpness changes with the hole width too, so it "
                    "is not fixed either."},
            {"text": "How big the picture is", "correct": False,
             "why": "Size changes with both the box length and the "
                    "object's distance, so it is not fixed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s25",
        "band": "standard",
        "text": "A pinhole camera gives an 80 mm picture. The hole is "
                "then narrowed to a quarter of its original width. What "
                "happens to the picture's height?",
        "options": [
            {"text": "It shrinks to 20 mm", "correct": False,
             "why": "Hole width does not set the picture's height at "
                    "all; only the object's distance and the box's "
                    "length do."},
            {"text": "It stays at 80 mm", "correct": True},
            {"text": "It shrinks to 40 mm", "correct": False,
             "why": "Narrowing the hole changes the blur and "
                    "brightness, not the height, which stays at 80 mm."},
            {"text": "It becomes sharper but also taller", "correct": False,
             "why": "It does become sharper, but the height itself does "
                    "not change at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s26",
        "band": "standard",
        "text": "Which of these would work best as an improvised pinhole "
                "camera screen: a sheet of foil, a sheet of greaseproof "
                "paper, or a mirror?",
        "options": [
            {"text": "A sheet of foil", "correct": False,
             "why": "Foil is opaque and shiny, so it would not let the "
                    "picture be seen from the other side."},
            {"text": "A mirror", "correct": False,
             "why": "A mirror would reflect the light away rather than "
                    "letting a picture be seen through it."},
            {"text": "A sheet of greaseproof paper", "correct": True},
            {"text": "All three would work equally well",
             "correct": False,
             "why": "Only a translucent material like greaseproof paper "
                    "lets the picture be seen from the far side."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s27",
        "band": "standard",
        "text": "A camera obscura (a room-sized pinhole camera) can have "
                "a hole several centimetres across and still give a "
                "recognisable, if soft, picture. Why does that work "
                "despite the hole being far wider than a shoebox "
                "pinhole?",
        "options": [
            {"text": "Rooms are naturally dimmer than shoeboxes, which "
                     "cancels out the extra blur", "correct": False,
             "why": "Dimness and blur are separate properties; being "
                    "dim does not cancel out or reduce blur."},
            {"text": "A room-sized hole does not really let any extra rays "
                     "through at all, compared with a much smaller "
                     "pinhole-sized hole", "correct": False,
             "why": "A wider hole genuinely does let more rays through "
                    "from each object point — the room's great length "
                    "is what keeps the picture usable despite this."},
            {"text": "The room's walls absorb the extra blur before it "
                     "reaches the screen", "correct": False,
             "why": "Walls do not selectively absorb blur; the "
                    "picture's usability comes from the room's great "
                    "length, not from anything the walls do."},
            {"text": "The room's much longer box length keeps the blur "
                     "small compared with the huge overall picture it "
                     "produces", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s28",
        "band": "standard",
        "text": "Would doubling an object's HEIGHT, keeping the same "
                "distance and box length, change the picture's height?",
        "options": [
            {"text": "Yes — a taller object produces a taller picture, "
                     "at the same distance and box length", "correct": True},
            {"text": "No — only the object's own distance and the "
                     "box's length ever affect the picture's height",
             "correct": False,
             "why": "The object's own height matters too — a taller "
                    "object produces a taller picture, all else being "
                    "equal."},
            {"text": "No — the picture's height is fixed once the hole "
                     "size is chosen", "correct": False,
             "why": "The hole size sets blur and brightness, not the "
                    "picture's height, which does depend on the "
                    "object's own height."},
            {"text": "It would make the picture the right way up "
                     "instead of inverted", "correct": False,
             "why": "Changing the object's height affects the "
                    "picture's SIZE, not whether it is inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s29",
        "band": "standard",
        "text": "A student says shortening the box makes the picture "
                "BOTH smaller and sharper at once, since 'the light has "
                "less distance to spread out.' Evaluate this using what "
                "actually controls sharpness.",
        "options": [
            {"text": "The student is completely right — shortening the "
                     "box always sharpens the picture as well as "
                     "shrinking it", "correct": False,
             "why": "Sharpness is set by the hole width alone; changing "
                    "only the box length leaves the blur unaffected."},
            {"text": "The picture does get smaller, but sharpness is "
                     "controlled by the hole width, not the box length "
                     "— shortening the box does not by itself sharpen "
                     "it", "correct": True},
            {"text": "The student is wrong about the size too — shortening the "
                     "box actually makes the picture bigger", "correct": False,
             "why": "Shortening the box does make the picture smaller, "
                    "as the student says — it is the claim about "
                    "sharpness that is wrong."},
            {"text": "Neither the size nor the sharpness changes when "
                     "the box is shortened", "correct": False,
             "why": "The size genuinely does change with box length; it "
                    "is only the sharpness claim that is mistaken here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-s30",
        "band": "standard",
        "text": "Does changing a pinhole camera's box length affect the "
                "picture's size only, or its brightness too?",
        "options": [
            {"text": "Brightness only — box length has no effect on "
                     "size", "correct": False,
             "why": "Box length is one of the two things that set the "
                    "picture's size, so it plainly does affect it."},
            {"text": "Size only — box length has no effect on brightness at "
                     "all, since the hole alone decides how much light gets in", "correct": False,
             "why": "A longer box spreads the same amount of light over "
                    "a bigger picture, which does dim it as well as "
                    "enlarging it."},
            {"text": "Both — a longer box makes the picture bigger AND "
                     "dimmer, since the same light spreads over a "
                     "bigger area", "correct": True},
            {"text": "Neither — only the hole width affects size or "
                     "brightness", "correct": False,
             "why": "Box length affects both size and brightness "
                    "together; the hole affects blur and brightness, "
                    "not size."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "p7-04-h08",
        "band": "harder",
        "text": "An object 500 mm tall, 1000 mm from a pinhole camera, "
                "gives a 40 mm picture. What is the box length?",
        "options": [
            {"text": "80 mm", "correct": True},
            {"text": "800 mm", "correct": False,
             "why": "That is ten times too long — check which figures "
                    "are multiplied and which are divided in the "
                    "ratio."},
            {"text": "8 mm", "correct": False,
             "why": "That is ten times too short for the same reason, "
                    "the other way round."},
            {"text": "500 mm", "correct": False,
             "why": "That copies the object's height directly rather "
                    "than working out the box length from the ratio."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h09",
        "band": "harder",
        "text": "A physics teacher says a camera obscura room works 'by "
                "exactly the same physics' as a shoebox pinhole camera, "
                "just bigger. A student objects that the room's hole is "
                "millions of times wider, so 'it can't really be the "
                "same thing.' Who is closer to being right?",
        "options": [
            {"text": "The student — a wider hole means a genuinely different "
                     "physical process is taking place",
             "correct": False,
             "why": "The same underlying mechanism, rays crossing at a "
                    "hole, applies whatever the hole's width — only how "
                    "sharp, bright or big the result is changes with "
                    "scale."},
            {"text": "The teacher — the underlying mechanism, straight "
                     "rays crossing at a hole, is identical at any "
                     "scale; only the specific numbers differ",
             "correct": True},
            {"text": "Neither — camera obscura rooms actually use lenses, not "
                     "pinholes at all", "correct": False,
             "why": "A true camera obscura room uses a plain hole, just "
                    "as a shoebox pinhole camera does."},
            {"text": "Both are equally wrong, since neither device really "
                     "forms a picture at that scale",
             "correct": False,
             "why": "A camera obscura room genuinely does form a "
                    "recognisable picture, following exactly the same "
                    "rules as a small pinhole camera."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h10",
        "band": "harder",
        "text": "A pinhole picture is 30 mm tall from an object 600 mm "
                "tall. The same box is then used to photograph a second "
                "object twice as tall as the first, from twice the "
                "distance. What is the new picture height?",
        "options": [
            {"text": "15 mm — halved", "correct": False,
             "why": "Doubling the distance alone would halve the "
                    "picture, but doubling the height at the same time "
                    "doubles it back again."},
            {"text": "60 mm — doubled", "correct": False,
             "why": "Doubling the object's height alone would double "
                    "the picture, but doubling the distance at the same "
                    "time halves it back again."},
            {"text": "30 mm — unchanged", "correct": True},
            {"text": "120 mm — four times as tall", "correct": False,
             "why": "The two changes here work against each other, not "
                    "with each other — they cancel rather than "
                    "combining."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h11",
        "band": "harder",
        "text": "For a FIXED box length, does a wider hole always "
                "increase the ABSOLUTE blur, in millimetres, regardless "
                "of which box length is being used?",
        "options": [
            {"text": "It cannot be predicted without knowing the "
                     "object's colour", "correct": False,
             "why": "Colour plays no part in how much a pinhole picture "
                    "blurs; the hole width and box length are what "
                    "matter."},
            {"text": "No — a wider hole only increases the blur for "
                     "very short boxes", "correct": False,
             "why": "Widening the hole increases the blur whatever the "
                    "fixed box length happens to be, not only for short "
                    "boxes."},
            {"text": "No — the blur is fixed by the object's distance, "
                     "not by the hole width", "correct": False,
             "why": "It is the hole width that sets the blur; the "
                    "object's distance affects the picture's overall "
                    "size instead."},
            {"text": "Yes — at a fixed box length, widening the hole "
                     "always increases the blur", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h12",
        "band": "harder",
        "text": "Brightness scales with the SQUARE of the hole's width. "
                "Widening a hole from 1 mm to 4 mm increases brightness "
                "by a factor of 16. Does this match the area-squared "
                "rule?",
        "options": [
            {"text": "Yes — 4 squared is 16, matching the rule exactly",
             "correct": True},
            {"text": "No — the width only quadrupled, so brightness "
                     "should only quadruple too", "correct": False,
             "why": "Brightness follows the SQUARE of the width, not "
                    "the width itself, so a factor of 4 in width gives "
                    "a factor of 16 in brightness."},
            {"text": "No — doubling the width should double the "
                     "brightness only, giving a factor of 8 overall",
             "correct": False,
             "why": "The width increased by a factor of 4, not simply "
                    "doubled, and the rule squares that factor to get "
                    "16."},
            {"text": "It cannot be checked without knowing the box "
                     "length used", "correct": False,
             "why": "Brightness from the hole's area-squared rule does "
                    "not depend on the box length at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h13",
        "band": "harder",
        "text": "A student says the pinhole's brightness-versus-"
                "sharpness trade-off means NO camera can ever be both "
                "bright and sharp. What corrects this overgeneralised "
                "claim?",
        "options": [
            {"text": "Nothing at all corrects it — the trade-off is a "
                     "genuinely fundamental limit that applies to every single "
                     "possible camera design ever built",
             "correct": False,
             "why": "The trade-off is specific to a plain pinhole; a "
                    "lens is precisely the device that gets around it."},
            {"text": "A convex lens breaks exactly this trade-off, "
                     "letting a wide, bright opening still bring each "
                     "point back to a single sharp point", "correct": True},
            {"text": "The trade-off only applies to cameras used "
                     "outdoors, not indoors", "correct": False,
             "why": "Indoor or outdoor use makes no difference to "
                    "whether a pinhole faces this trade-off — only "
                    "adding a lens changes that."},
            {"text": "The trade-off can be avoided simply by using a "
                     "much bigger box, with no lens needed",
             "correct": False,
             "why": "A bigger box changes the picture's size, not the "
                    "underlying brightness-versus-sharpness trade-off "
                    "at the hole itself."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h14",
        "band": "harder",
        "text": "A pinhole box is 100 mm long and gives a 20 mm picture "
                "of an object 1000 mm tall. The box is then extended to "
                "250 mm, with nothing else changed. What is the new "
                "picture height?",
        "options": [
            {"text": "500 mm", "correct": False,
             "why": "That is ten times too tall for a box only 2.5 "
                    "times as long as before."},
            {"text": "20 mm", "correct": False,
             "why": "The box length has changed, and the picture's "
                    "height changes with it — it does not stay at its "
                    "original value."},
            {"text": "50 mm", "correct": True},
            {"text": "25 mm", "correct": False,
             "why": "That undershoots the correct scaling from the "
                    "original 20 mm picture by the 2.5× box change."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h15",
        "band": "harder",
        "text": "A student argues a wider hole always makes the picture "
                "blurrier because it lets in light from a WIDER area of "
                "the object (a bigger field of view). Is field of view "
                "the right explanation for blur?",
        "options": [
            {"text": "It is impossible to say without measuring the "
                     "object's own brightness", "correct": False,
             "why": "The object's brightness affects how easily the "
                    "picture is seen, not the mechanism behind the "
                    "blur."},
            {"text": "Yes — a wider hole genuinely captures a noticeably "
                     "bigger field of view from the object, and that is "
                     "exactly why it blurs the picture",
             "correct": False,
             "why": "Field of view is set by the box's overall "
                    "geometry, not by hole width — blur comes from "
                    "rays leaving one point landing in several places."},
            {"text": "No — hole width has no connection to blur at all, which "
                     "is set purely by the box length",
             "correct": False,
             "why": "Hole width is exactly what sets the blur; box "
                    "length affects the picture's size instead."},
            {"text": "No — the blur comes from a bundle of rays FROM "
                     "THE SAME object point spreading across the "
                     "screen, not from a wider field of view",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h16",
        "band": "harder",
        "text": "An object's distance is already very large, like a "
                "distant star. Does doubling this already-huge distance "
                "change the picture noticeably?",
        "options": [
            {"text": "No — the change to an already tiny ratio of box "
                     "length to distance is negligible in practice",
             "correct": True},
            {"text": "Yes — doubling any distance always halves the "
                     "picture's height by a noticeable amount",
             "correct": False,
             "why": "The RULE always applies, but starting from an "
                    "already enormous distance, doubling it changes an "
                    "already tiny, hard-to-notice picture by a "
                    "negligible further amount."},
            {"text": "No — distances beyond a certain size stop affecting the "
                     "picture at all, by a fixed rule",
             "correct": False,
             "why": "There is no such fixed cut-off distance; the "
                    "relationship holds at every distance, it is just "
                    "that the effect of doubling an already-huge "
                    "distance is small in practice."},
            {"text": "Yes — stars are a special case where the usual size rule "
                     "does not apply at all", "correct": False,
             "why": "The same size rule applies to a star as to any "
                    "other object; it is simply that the effect becomes "
                    "hard to notice at such extreme distances."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h17",
        "band": "harder",
        "text": "A pinhole camera's box length is TRIPLED, and at the "
                "same time the object is moved to HALF its original "
                "distance. Overall, by what factor does the picture's "
                "height change?",
        "options": [
            {"text": "1.5 times bigger", "correct": False,
             "why": "That only accounts for one of the two changes, not "
                    "both combined."},
            {"text": "6 times bigger", "correct": True},
            {"text": "3 times bigger", "correct": False,
             "why": "That only accounts for the box-length change; "
                    "halving the distance also doubles the height on "
                    "top of that."},
            {"text": "9 times bigger", "correct": False,
             "why": "That would be tripling combined with tripling "
                    "again, not tripling combined with a distance "
                    "halved."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h18",
        "band": "harder",
        "text": "A designer wants a pinhole camera that is bright and "
                "gives a large picture, using a wide hole and a long "
                "box. Will the long box undo the wide hole's benefit "
                "for SHARPNESS?",
        "options": [
            {"text": "Yes, but only if the box is longer than the "
                     "object's own distance", "correct": False,
             "why": "There is no such threshold; box length simply "
                    "does not affect blur, at any length."},
            {"text": "Yes — a longer box always makes any existing blur "
                     "considerably worse", "correct": False,
             "why": "Box length changes the picture's size, not its "
                    "sharpness — the blur stays set by the hole width "
                    "alone."},
            {"text": "No — box length does not affect blur at all, so "
                     "combining it with a wide hole leaves the blur no "
                     "worse than the wide hole alone already causes",
             "correct": True},
            {"text": "It is impossible to predict without also knowing "
                     "the object's colour", "correct": False,
             "why": "Colour has no bearing on blur, which depends "
                    "purely on the hole width here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h19",
        "band": "harder",
        "text": "An object is moved to THREE TIMES its distance, and the "
                "box is made THREE TIMES shorter, both at once. By what "
                "single factor does the picture's height change?",
        "options": [
            {"text": "It shrinks to a sixth of its original height",
             "correct": False,
             "why": "The two factors of 3 multiply together to give a "
                    "ninth, not simply add to give a sixth."},
            {"text": "It shrinks to a third of its original height",
             "correct": False,
             "why": "That only accounts for one of the two changes; "
                    "both the distance and the box length are working "
                    "to shrink it here."},
            {"text": "It stays exactly the same, since the two changes "
                     "cancel out", "correct": False,
             "why": "These two changes both shrink the picture, rather "
                    "than one enlarging it while the other shrinks it — "
                    "they do not cancel here."},
            {"text": "It shrinks to a ninth of its original height",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h20",
        "band": "harder",
        "text": "A pinhole camera makes an image of a candle on its screen. "
                "Which light forms the image?",
        "options": [
            {"text": "A narrow beam from every point on the candle, straight "
                     "through the hole",
             "correct": True},
            {"text": "Only two rays: one from the top of the candle and one "
                     "from the bottom",
             "correct": False,
             "why": "Diagrams often draw just those two rays to keep things "
                    "clear. In fact every point on the candle sends light "
                    "through the hole, so every point appears in the image."},
            {"text": "Only light from the flame, because the rest of the "
                     "candle gives out no light",
             "correct": False,
             "why": "The rest of the candle reflects light from the flame "
                    "and the room. That light goes through the hole too, so "
                    "the whole candle appears."},
            {"text": "Rays that bend as they pass through the hole, so that "
                     "they cross over",
             "correct": False,
             "why": "Light travels in straight lines through the hole. The "
                    "image is upside down because light from the top travels "
                    "down through it, not because it bends."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h21",
        "band": "harder",
        "text": "A student says: 'Since the picture is inverted, if I "
                "turn the WHOLE camera upside down, the picture should "
                "come out the right way up.' Are they right?",
        "options": [
            {"text": "Yes — physically turning the whole camera "
                     "cancels out the inversion caused by the rays "
                     "crossing at the hole", "correct": False,
             "why": "The rays still cross inside the camera in exactly "
                    "the same relative way, whichever way the whole "
                    "camera is oriented in the room."},
            {"text": "No — turning the whole camera does not change "
                     "the relative geometry between object, hole and "
                     "screen at all", "correct": True},
            {"text": "Yes, but only if the object is also turned upside "
                     "down at the same time", "correct": False,
             "why": "Turning both the camera and the object together "
                    "still leaves their relative geometry, and so the "
                    "inversion, completely unchanged."},
            {"text": "It depends on which way round the hole itself is "
                     "facing", "correct": False,
             "why": "The hole's facing direction does not change the "
                    "relative geometry between object, hole and screen "
                    "that causes the inversion."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h22",
        "band": "harder",
        "text": "A pinhole camera's box length is doubled, and a second "
                "screen is also kept at the ORIGINAL, shorter distance "
                "so two pictures are captured at once. Compare the two "
                "pictures' heights.",
        "options": [
            {"text": "The nearer screen's picture is twice as tall as "
                     "the further screen's", "correct": False,
             "why": "It is the FURTHER screen that catches the taller "
                    "picture, since the ray bundle keeps spreading with "
                    "distance from the hole."},
            {"text": "Both pictures are exactly the same height",
             "correct": False,
             "why": "The ray bundle from each object point keeps "
                    "spreading further from the hole, so a screen "
                    "twice as far away catches a picture twice as tall."},
            {"text": "The further screen's picture is twice as tall as "
                     "the nearer screen's", "correct": True},
            {"text": "The comparison cannot be made without also "
                     "knowing the hole's width", "correct": False,
             "why": "Hole width affects blur and brightness, not the "
                    "ratio between the two picture heights here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h23",
        "band": "harder",
        "text": "A student wants to use the ratio between picture "
                "height, box length, object height and object distance "
                "to work out the height of a tall building across a "
                "street, by photographing it with a homemade pinhole "
                "camera. Is this a genuinely usable method in "
                "principle?",
        "options": [
            {"text": "Yes, but only if the building is measured at "
                     "night rather than during the day", "correct": False,
             "why": "Time of day makes no difference to whether the "
                    "ratio method works; it depends only on the "
                    "geometry involved."},
            {"text": "No — the ratio only works for very small, nearby "
                     "objects, never for something as large as a "
                     "building", "correct": False,
             "why": "The same ratio applies whatever the object's real "
                    "size, from a candle flame to a building."},
            {"text": "No — a pinhole camera can never be used to "
                     "measure anything about a real object's size",
             "correct": False,
             "why": "The ratio between picture height, box length, "
                    "object height and distance is exactly the tool "
                    "needed to work out a real object's height."},
            {"text": "Yes, in principle — knowing the box length, the "
                     "picture height and the building's distance lets "
                     "you rearrange the ratio to find its real height",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h24",
        "band": "harder",
        "text": "A pinhole camera aimed at the Moon gives an extremely "
                "tiny picture, a fraction of a millimetre tall, even "
                "with a fairly long box. What does this suggest about "
                "the ratio of the Moon's height to its distance, "
                "compared with a nearby object?",
        "options": [
            {"text": "It must be a very small ratio — the Moon's real "
                     "size is enormous, but at its enormous distance "
                     "the ratio works out tiny", "correct": True},
            {"text": "It must be a very large ratio, since the Moon is "
                     "such an enormous object", "correct": False,
             "why": "The Moon's huge size is outweighed by its far "
                    "greater distance, giving a small ratio overall, "
                    "not a large one."},
            {"text": "The ratio cannot be worked out at all for objects as far "
                     "away as the Moon, since too little of their light "
                     "reaches a pinhole to form a picture", "correct": False,
             "why": "The same ratio idea applies at any distance; the "
                    "tiny resulting picture is exactly the evidence "
                    "that the ratio is small here."},
            {"text": "It shows the ratio rule stops applying beyond "
                     "the Earth's atmosphere", "correct": False,
             "why": "The rule is a matter of straight-line ray geometry, "
                    "not of atmosphere, so it continues to apply beyond "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h25",
        "band": "harder",
        "text": "A student assumes that since 'longer box = bigger "
                "picture', every possible box length works equally "
                "well in practice. What real-world limitation "
                "eventually stops simply making the box longer and "
                "longer?",
        "options": [
            {"text": "Beyond a certain length, the rule about size "
                     "simply stops being true", "correct": False,
             "why": "The size rule itself keeps holding at any box "
                    "length; it is the picture's BRIGHTNESS that "
                    "eventually becomes the practical limit."},
            {"text": "The picture eventually becomes too dim to see "
                     "or use, since the same light spreads over an "
                     "ever-bigger area", "correct": True},
            {"text": "A longer box eventually turns the picture the "
                     "right way up, ruining the setup", "correct": False,
             "why": "The picture stays inverted at any box length; "
                    "orientation is never the limiting factor here."},
            {"text": "There is genuinely no real-world limitation at all; "
                     "boxes can be made any length whatsoever with no downside", "correct": False,
             "why": "Dimness genuinely does become a practical problem "
                    "as the box gets longer and longer, spreading the "
                    "same light thinner."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h26",
        "band": "harder",
        "text": "A pinhole camera's box length is increased by 20%, "
                "with nothing else changed. By roughly what percentage "
                "does the picture's height increase?",
        "options": [
            {"text": "By about 4%, since the effect is squared",
             "correct": False,
             "why": "Picture height depends directly on box length, "
                    "not on its square, so the percentage change "
                    "matches rather than being squared."},
            {"text": "By about 40%, since the effect doubles",
             "correct": False,
             "why": "The height is directly proportional to the box "
                    "length, so a 20% increase in length gives a 20% "
                    "increase in height, not double that."},
            {"text": "By about 20% too", "correct": True},
            {"text": "Not at all — only the object's distance affects the "
                     "picture's height", "correct": False,
             "why": "Box length is one of the two things that set the "
                    "height, alongside the object's distance."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h27",
        "band": "harder",
        "text": "A student claims a convex lens must be transparent, "
                "since 'anything opaque could never focus light.' Using "
                "what a lens actually needs to do, is the student's point "
                "correct?",
        "options": [
            {"text": "Yes, and any lens that is even slightly less than "
                     "perfectly transparent cannot focus light at all",
             "correct": False,
             "why": "Real lenses are never mathematically perfect and "
                    "still focus light well; near-total transparency is "
                    "what is actually needed, not mathematical "
                    "perfection."},
            {"text": "No — a lens can be completely opaque and still "
                     "focus light perfectly well", "correct": False,
             "why": "An opaque material blocks light rather than "
                    "letting it through, so it could not refract or "
                    "focus anything at all."},
            {"text": "No — transparency is irrelevant to a lens; only "
                     "its curved shape matters", "correct": False,
             "why": "The curved shape sets HOW the light bends, but the "
                    "light still has to get through the material in the "
                    "first place, which needs transparency."},
            {"text": "Yes, in essence — a lens must let nearly all the "
                     "light through to refract and focus it, since "
                     "blocking the light leaves nothing to bring to a "
                     "point", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h28",
        "band": "harder",
        "text": "A studio softbox has a large diffusing panel in front "
                "of the bulb, rather than a small bright point. Would a "
                "pinhole camera give a SHARPER or BLURRIER picture of "
                "this panel than of a small bare bulb, using the same "
                "hole and box?",
        "options": [
            {"text": "Neither — sharpness per point does not depend on "
                     "the size of the light source; the panel is just a "
                     "bigger picture made of equally blurred points",
             "correct": True},
            {"text": "Blurrier — a bigger glowing surface always makes "
                     "the whole picture more blurred than a small point "
                     "source does", "correct": False,
             "why": "Each point on the panel is imaged with the same "
                    "blur as a single bare bulb would be; a bigger "
                    "source is not blurrier per point, just bigger "
                    "overall."},
            {"text": "Sharper — a bigger light source always produces a "
                     "sharper picture than a small point does",
             "correct": False,
             "why": "The blur for each individual point is set purely "
                    "by the hole width, regardless of how big the "
                    "overall light source is."},
            {"text": "It cannot be predicted without knowing the "
                     "colour of the panel's light", "correct": False,
             "why": "Colour has no bearing on the geometric blur here; "
                    "the hole width is what sets it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h29",
        "band": "harder",
        "text": "A studio flash (a very brief burst of light) and a bare "
                "bulb of the same total brightness are each "
                "photographed with the same pinhole camera. Does the "
                "flash's much shorter duration predict any difference "
                "in the SHARPNESS of the two pictures?",
        "options": [
            {"text": "Yes — a briefer flash always produces a sharper "
                     "picture than a longer-lasting bulb", "correct": False,
             "why": "The geometric blur described here depends on the "
                    "hole width and the box's geometry, not on how long "
                    "the source is lit for."},
            {"text": "No — sharpness is set by the hole width and "
                     "geometry, never by how long the light source "
                     "shines for", "correct": True},
            {"text": "Yes — a longer-lasting bulb always produces a "
                     "sharper picture than a brief flash", "correct": False,
             "why": "Duration of the light source does not set this "
                    "kind of blur; the hole width and geometry do."},
            {"text": "It cannot be predicted at all without knowing exactly "
                     "how many milliseconds the brief flash lasts", "correct": False,
             "why": "The exact duration is not needed here, since "
                    "duration is not what controls this geometric blur "
                    "at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-04-h30",
        "band": "harder",
        "text": "Would a MOVING object photographed by a pinhole camera "
                "show extra blur beyond the usual geometric blur this "
                "topic describes, and if so, why?",
        "options": [
            {"text": "Yes, but only because a moving object always "
                     "widens the effective hole itself", "correct": False,
             "why": "The object's motion does not change the hole's own "
                    "width at all; it introduces a genuinely different "
                    "kind of blur instead."},
            {"text": "No — the hole width is the only thing that can ever "
                     "cause any blur in a pinhole picture at all",
             "correct": False,
             "why": "A moving object introduces its own separate "
                    "source of blur, on top of whatever geometric blur "
                    "the hole width already produces."},
            {"text": "Yes — motion blur is a separate kind of blur, "
                     "caused by the object shifting position while the "
                     "picture is forming, unlike the geometric blur "
                     "from the hole", "correct": True},
            {"text": "No — motion has no effect on a picture unless the "
                     "camera itself is also moving", "correct": False,
             "why": "A moving OBJECT alone, even with a perfectly still "
                    "camera, can introduce motion blur as it shifts "
                    "position while the picture forms."},
        ],
        "figure": None,
    },
]
