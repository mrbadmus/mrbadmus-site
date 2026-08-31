"""P7 lesson 03 — Refraction: twelve questions (MRB-223).

Written against Design's page. The broken-straw hook, the ray-into-a-block
bench and the apparent-depth figure are hers.

The discriminations, in the order the lesson builds them:

  · the straw is straight and the LIGHT bent (`LIGHT-09`);
  · nothing pushes the light — the bend follows from the slowing plus an
    angle (`LIGHT-10`);
  · light SLOWS in glass, it does not speed up (`LIGHT-11`);
  · a ray along the normal slows and does not bend, so slowing and
    bending are not the same thing (`LIGHT-12`) — the harder band sits
    here.

⚠️ POSITION IS AUTHORED — 0,3,1,2 · 2,1,0,3 · 3,2,1,0, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. This lesson has no
worked example: `LGT.04b` is qualitative and nothing was invented to fill
a block.
"""

UNIT = "P7"
LESSON = "refraction"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-03-e01",
        "band": "easier",
        "text": "Refraction is…",
        "options": [
            {"text": "the change of direction of light when it crosses into "
                     "a different material at an angle", "correct": True},
            {"text": "the bouncing of light off a surface, so that it comes "
                     "back into the material it was in", "correct": False,
             "why": "That is reflection. Refraction happens to the light "
                    "that goes IN."},
            {"text": "the taking up of light by a surface, so that none of "
                     "it ever leaves the surface again", "correct": False,
             "why": "That is absorption, and the light does not come out "
                    "again at all."},
            {"text": "the splitting of white light into the band of colours "
                     "a prism spreads out",
             "correct": False,
             "why": "That is dispersion, which is a consequence of "
                    "refraction rather than the same thing."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e02",
        "band": "easier",
        "text": "Light travelling from air into glass…",
        "options": [
            {"text": "speeds up", "correct": False,
             "why": "Light is fastest in a vacuum and slower in any "
                    "material. Nothing speeds it up."},
            {"text": "keeps exactly the same speed", "correct": False,
             "why": "It drops to about two thirds of its speed in air, and "
                    "that drop is the cause of the bending."},
            {"text": "stops at the surface", "correct": False,
             "why": "Most of it goes straight in; that is what makes glass "
                    "transparent."},
            {"text": "slows down", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e03",
        "band": "easier",
        "text": "A ray going from air into water at an angle bends…",
        "options": [
            {"text": "away from the normal", "correct": False,
             "why": "That is what happens coming OUT, when the light speeds "
                    "up again."},
            {"text": "towards the normal", "correct": True},
            {"text": "along the surface", "correct": False,
             "why": "The ray carries on into the water. It does not run "
                    "along the boundary."},
            {"text": "straight back the way it came", "correct": False,
             "why": "That would be reflection, and only a small part of the "
                    "light does that."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e04",
        "band": "easier",
        "text": "A straw in a glass of water looks broken at the surface. "
                "What is actually bent?",
        "options": [
            {"text": "The straw", "correct": False,
             "why": "Lift it out and it is perfectly straight. Nothing has "
                    "happened to the straw."},
            {"text": "The glass", "correct": False,
             "why": "The glass is unchanged, and the effect happens just as "
                    "well in a plain beaker or a pond."},
            {"text": "The path the light takes to your eye", "correct": True},
            {"text": "Nothing — it is an illusion in your eye alone",
             "correct": False,
             "why": "Something real does bend: the ray. Your eye then does "
                    "the reasonable thing and assumes it did not."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-03-s01",
        "band": "standard",
        "text": "A ray enters a parallel-sided glass block at an angle and "
                "comes out of the far side. How does the ray leaving "
                "compare with the ray arriving?",
        "options": [
            {"text": "It travels at a bigger angle to the original "
                     "direction, because it has been bent twice",
             "correct": False,
             "why": "The two bends are equal and opposite, so they cancel "
                    "in direction."},
            {"text": "It travels along exactly the same line",
             "correct": False,
             "why": "The direction is the same and the line is not: the ray "
                    "has been shifted sideways."},
            {"text": "It travels in the same direction, shifted sideways",
             "correct": True},
            {"text": "It travels back towards the ray box", "correct": False,
             "why": "That would need a mirror at the far face. The light "
                    "goes on through."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s02",
        "band": "standard",
        "text": "The same ray enters water, then perspex, then glass, each "
                "time at 45° to the normal. In which is it bent most?",
        "options": [
            {"text": "Water, because it is the thinnest of the three",
             "correct": False,
             "why": "Thinness is not the property that matters, and water "
                    "slows light the LEAST of the three, so it bends it "
                    "least."},
            {"text": "Glass, because it slows the light the most",
             "correct": True},
            {"text": "Perspex, because it is used at the bench",
             "correct": False,
             "why": "Perspex is used because it does not shatter. Its index "
                    "sits between the other two."},
            {"text": "All three the same, because the angle in was the "
                     "same", "correct": False,
             "why": "The angle in is only half of it. How much the material "
                    "slows the light is the other half."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s03",
        "band": "standard",
        "text": "Standing on a bank, a fish looks nearer the surface than "
                "it is. Why?",
        "options": [
            {"text": "Light from the fish bends away from the normal as it "
                     "leaves the water, and your eye traces it back in a "
                     "straight line", "correct": True},
            {"text": "The water magnifies the fish, so it looks closer",
             "correct": False,
             "why": "Magnification would change its size. What changes is "
                    "where it seems to be."},
            {"text": "The fish is swimming higher than it looks",
             "correct": False,
             "why": "The fish is where it is. What is misleading is the "
                    "route the light took."},
            {"text": "Light slows in water, so it arrives a moment late, and "
                     "anything seen late is seen where it used to be rather "
                     "than where it is", "correct": False,
             "why": "Arriving a fraction later does not change the "
                    "direction it arrives from. The change of direction is "
                    "what does it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s04",
        "band": "standard",
        "text": "Why does a ray aimed exactly along the normal not bend at "
                "all?",
        "options": [
            {"text": "Because light along the normal does not slow down, and "
                     "bending is caused by the slowing, so with no slowing "
                     "there is no bend", "correct": False,
             "why": "It slows exactly as much as any other ray. The slowing "
                    "is not what is missing."},
            {"text": "Because the glass is thinnest along the normal",
             "correct": False,
             "why": "The block is the same all over, and a thicker block "
                    "would shift the ray further without bending it more."},
            {"text": "Because the surface reflects it instead",
             "correct": False,
             "why": "A little is always reflected, at any angle. Most of it "
                    "goes in."},
            {"text": "Because both edges of the beam reach the slower "
                     "material at the same moment, so there is nothing to "
                     "swing it round", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-03-h01",
        "band": "harder",
        "text": "A coin sits at the bottom of an empty mug, just hidden by "
                "the rim. Water is poured in and the coin appears. Why?",
        "options": [
            {"text": "The water floats the coin closer to the rim",
             "correct": False,
             "why": "A coin does not float, and the effect works with the "
                    "coin taped down."},
            {"text": "The water magnifies the coin until it is big enough "
                     "to see past the rim, in the way a curved lens makes "
                     "an object look larger", "correct": False,
             "why": "Its apparent size barely changes. What changes is the "
                    "direction the light arrives from."},
            {"text": "The water reflects the coin up over the rim",
             "correct": False,
             "why": "Reflection at the surface sends light back DOWN into "
                    "the mug, away from your eye."},
            {"text": "Light from the coin bends away from the normal as it "
                     "leaves the water, so a ray that would have hit the "
                     "rim now clears it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h02",
        "band": "harder",
        "text": "A student says refraction proves light is a stream of "
                "particles being pulled sideways by the glass. What is the "
                "strongest evidence against that?",
        "options": [
            {"text": "Light is never bent at all, so there is nothing to "
                     "explain", "correct": False,
             "why": "It plainly is bent — the bench draws it, and a "
                    "protractor measures it."},
            {"text": "Glass is not magnetic, so it could not pull anything",
             "correct": False,
             "why": "A pull need not be magnetic, so this rules nothing "
                    "out."},
            {"text": "A ray arriving along the normal slows just as much "
                     "and is not pulled aside at all", "correct": True},
            {"text": "Light bends away from the normal on the way out, "
                     "which a pull could not do", "correct": False,
             "why": "A pull towards the glass would explain that as well, "
                    "by pulling the ray back as it left."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h03",
        "band": "harder",
        "text": "A swimming pool looks shallower from the side of the pool "
                "than it does looking straight down. Why is the effect "
                "bigger at a glancing angle?",
        "options": [
            {"text": "Because the water is deeper at the far end",
             "correct": False,
             "why": "The pool has a flat bottom in the question, and the "
                    "effect happens over a flat one."},
            {"text": "Because the bend grows with the angle to the normal, "
                     "and looking straight down is looking along the "
                     "normal", "correct": True},
            {"text": "Because light travels further through the water at a "
                     "glancing angle, so it slows more and is bent more on "
                     "the way", "correct": False,
             "why": "How far it travels changes the time, not the "
                    "direction. The bend is set at the surface."},
            {"text": "Because the surface is rougher at the far end",
             "correct": False,
             "why": "A ripple blurs the picture. The apparent-depth effect "
                    "is there on perfectly still water."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h04",
        "band": "harder",
        "text": "Light inside an optical fibre keeps striking the wall at a "
                "steep angle to the normal and never escapes. Which "
                "statement fits that?",
        "options": [
            {"text": "Past a certain angle the light cannot leave the glass "
                     "at all and is reflected back inside", "correct": True},
            {"text": "The glass wall absorbs the light and gives it out "
                     "again on the inside", "correct": False,
             "why": "Absorbing and re-emitting would lose the signal within "
                    "centimetres. Nothing is absorbed at the wall."},
            {"text": "The light is travelling too fast to escape",
             "correct": False,
             "why": "Speed is not what decides it. The angle to the normal "
                    "is."},
            {"text": "The fibre is a mirror on the inside, so the law of "
                     "reflection does not apply", "correct": False,
             "why": "The law of reflection is exactly what does apply. "
                    "There is no silvering: it is the glass-to-air boundary "
                    "doing it."},
        ],
        "figure": None,
    },
]
