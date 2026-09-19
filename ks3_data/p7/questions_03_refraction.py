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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-03-e05",
        "band": "easier",
        "text": "Light leaving glass and going out into air bends…",
        "options": [
            {"text": "towards the normal", "correct": False,
             "why": "That is what happens on the way IN, when the light slows "
                    "down."},
            {"text": "away from the normal", "correct": True},
            {"text": "not at all, whatever angle it leaves at",
             "correct": False,
             "why": "It carries straight on only if it leaves along the "
                    "normal."},
            {"text": "straight back into the glass", "correct": False,
             "why": "That is reflection, and it is a different behaviour from "
                    "refraction."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e06",
        "band": "easier",
        "text": "What happens to the speed of light when it goes from air "
                "into water?",
        "options": [            {"text": "It speeds up, because water is clearer than air",
             "correct": False,
             "why": "Clearness is not the test. A denser transparent material "
                    "slows light down."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "If it did, there would be no refraction at all — and a "
                    "straw in water clearly looks bent."},
            {"text": "It stops until it is bent", "correct": False,
             "why": "It never stops; it simply travels more slowly through "
                    "the water."},
            {"text": "It slows down as it enters", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e07",
        "band": "easier",
        "text": "Refraction happens because light…",
        "options": [
            {"text": "is pushed sideways by the material", "correct": False,
             "why": "Nothing pushes it. The change of direction follows from "
                    "the change of speed."},
            {"text": "bounces off the surface of the material",
             "correct": False,
             "why": "That is reflection. Refraction is what happens to the "
                    "light that goes IN."},
            {"text": "is absorbed and then given out again in a new direction",
             "correct": False,
             "why": "Absorbed light does not come out again as a ray; "
                    "refracted light passes through."},
            {"text": "changes speed as it enters a different material",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e08",
        "band": "easier",
        "text": "A ray enters a glass block exactly along the normal. What "
                "happens to its direction?",
        "options": [
            {"text": "It carries straight on", "correct": True},
            {"text": "It bends towards the normal", "correct": False,
             "why": "It is already along the normal, so there is no angle to "
                    "bend towards."},
            {"text": "It bends away from the normal", "correct": False,
             "why": "That happens on leaving a denser material at an angle, "
                    "not on arriving straight on."},
            {"text": "It reflects straight back out", "correct": False,
             "why": "A little is reflected at any surface, but the ray in "
                    "question passes into the glass."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-03-s05",
        "band": "standard",
        "text": "A ray enters water from air at 30° to the normal. Which "
                "describes the refracted ray?",
        "options": [
            {"text": "It bends away from the normal, to more than 30°",
             "correct": False,
             "why": "That is what happens leaving a denser material, not "
                    "entering one."},
            {"text": "It bends towards the normal, to less than 30°",
             "correct": True},
            {"text": "It carries on at exactly 30°", "correct": False,
             "why": "Only a ray along the normal keeps its direction; this "
                    "one arrives at an angle."},
            {"text": "It reflects back into the air at 30°", "correct": False,
             "why": "Some does reflect, but the refracted ray is the part "
                    "that enters the water."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s06",
        "band": "standard",
        "text": "Why does a swimming pool look shallower than it really is?",
        "options": [
            {"text": "Because the water magnifies the bottom of the pool",
             "correct": False,
             "why": "Things do look larger, but what raises the bottom is the "
                    "direction the light leaves in."},
            {"text": "Because water is denser, so the bottom really is closer "
                     "to the surface",
             "correct": False,
             "why": "The pool's depth is unchanged; only where the bottom "
                    "APPEARS to be has changed."},
            {"text": "Because light from the bottom bends away from the "
                     "normal on leaving",
             "correct": True},
            {"text": "Because the surface of the water reflects the bottom "
                     "upwards",
             "correct": False,
             "why": "You are seeing light that came THROUGH the surface, not "
                    "light reflected from it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s07",
        "band": "standard",
        "text": "A ray passes from glass out into air at an angle. Which way "
                "does it bend, and what happens to its speed?",
        "options": [
            {"text": "Towards the normal, and it slows down", "correct": False,
             "why": "Both halves are the wrong way round; that is what "
                    "happens going the other way."},
            {"text": "Away from the normal, and it slows down",
             "correct": False,
             "why": "The direction is right but the speed is not: light goes "
                    "faster in air than in glass."},
            {"text": "Towards the normal, and it speeds up", "correct": False,
             "why": "The speed is right, but a ray leaving a denser material "
                    "bends AWAY from the normal."},
            {"text": "Away from the normal, and it speeds up", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s08",
        "band": "standard",
        "text": "A student says water bends light because it is thicker and "
                "pushes the ray sideways. What is right?",
        "options": [
            {"text": "The light changes speed at the boundary, and that is "
                     "what changes its direction",
             "correct": True},
            {"text": "The student is right, which is why thicker liquids bend "
                     "light more",
             "correct": False,
             "why": "Denser materials do bend light more, but nothing pushes "
                    "the ray; the speed change does it."},
            {"text": "The water heats the light, which makes it curve",
             "correct": False,
             "why": "Nothing about the temperature of the water is involved "
                    "in refraction."},
            {"text": "The light is reflected many times inside the water",
             "correct": False,
             "why": "Refracted light travels straight through the water in "
                    "one new direction."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-03-h05",
        "band": "harder",
        "text": "Why does a straw look broken only at the water surface, and "
                "straight above and below it?",
        "options": [
            {"text": "Because the straw is really bent at that point by the "
                     "water pressure",
             "correct": False,
             "why": "Lift it out and it is perfectly straight, so nothing has "
                    "bent."},
            {"text": "Because the water is deepest at the surface",
             "correct": False,
             "why": "The surface is the shallowest place there is; depth is "
                    "not what matters."},
            {"text": "Because the change of speed happens only at the "
                     "boundary between the two materials",
             "correct": True},
            {"text": "Because the light is reflected off the surface at that "
                     "point",
             "correct": False,
             "why": "Some is reflected, but the broken look comes from the "
                    "light that passes through and bends."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h06",
        "band": "harder",
        "text": "A ray enters glass at 60° to the normal, and another at 20°. "
                "Which is bent through the larger angle?",
        "options": [
            {"text": "The 20° ray, because it is closer to the normal",
             "correct": False,
             "why": "The closer to the normal it arrives, the less it bends; "
                    "along the normal it does not bend at all."},
            {"text": "The 60° ray, arriving furthest from the normal",
             "correct": True},
            {"text": "Both bend by the same amount, because it is the same "
                     "glass",
             "correct": False,
             "why": "The glass is the same, but how much a ray bends depends "
                    "on the angle it arrives at."},
            {"text": "Neither bends, because both are entering the same "
                     "material",
             "correct": False,
             "why": "Entering a different material at an angle is exactly "
                    "when bending happens."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h07",
        "band": "harder",
        "text": "Light slows down in glass. Does a pulse take longer to cross "
                "5 cm of glass than 5 cm of air?",
        "options": [
            {"text": "No — it makes up the time by bending",
             "correct": False,
             "why": "Bending changes direction, not the time taken over a "
                    "given path."},
            {"text": "No — light always takes the same time over the same "
                     "distance",
             "correct": False,
             "why": "It takes the same time only in the same material; the "
                    "speed differs between materials."},
            {"text": "Yes, because it is travelling more slowly through the "
                     "glass",
             "correct": True},
            {"text": "Yes, but only if the ray enters at an angle",
             "correct": False,
             "why": "The slowing happens whatever the angle, including "
                    "straight along the normal."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h08",
        "band": "harder",
        "text": "Why is there no refraction at a boundary between two "
                "materials in which light travels at the same speed?",
        "options": [
            {"text": "Because the two materials must be the same material",
             "correct": False,
             "why": "They can be quite different substances and still happen "
                    "to carry light at the same speed."},
            {"text": "Because light cannot cross such a boundary at all",
             "correct": False,
             "why": "It crosses perfectly well — it simply carries straight "
                    "on."},
            {"text": "Because with no speed change there is nothing to bend "
                     "the ray",
             "correct": True},
            {"text": "Because the boundary reflects all of the light instead",
             "correct": False,
             "why": "Almost none is reflected there; the light goes through "
                    "undeviated."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ───────────────────────────────────────
    {
        "id": "p7-03-e09",
        "band": "easier",
        "text": "For transparent materials, 'denser' describes one "
                "that…",
        "options": [
            {"text": "slows light down more than another material does",
             "correct": True},
            {"text": "looks darker in colour than another material",
             "correct": False,
             "why": "Colour is not what the word refers to here — how "
                    "much a material slows light down is."},
            {"text": "weighs more per bottle than another liquid",
             "correct": False,
             "why": "Ordinary weight is not what decides how much a "
                    "transparent material bends light."},
            {"text": "reflects more light than it lets through",
             "correct": False,
             "why": "A denser transparent material still lets almost all "
                    "the light through; it is not becoming a mirror."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e10",
        "band": "easier",
        "text": "Of water, perspex and glass, which one slows light down "
                "the LEAST?",
        "options": [
            {"text": "Perspex", "correct": False,
             "why": "Perspex slows light more than water does, though "
                    "less than glass."},
            {"text": "Water", "correct": True},
            {"text": "Glass", "correct": False,
             "why": "Glass slows light the most of the three, not the "
                    "least."},
            {"text": "All three slow it down by the same amount",
             "correct": False,
             "why": "The three materials slow light by different "
                    "amounts, which is why they bend a ray by different "
                    "amounts too."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e11",
        "band": "easier",
        "text": "Of water, perspex and glass, which one bends a ray "
                "arriving at the same angle the MOST?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "Water bends the ray the least of the three, since it "
                    "slows light the least."},
            {"text": "Perspex", "correct": False,
             "why": "Perspex bends the ray more than water but less than "
                    "glass."},
            {"text": "Glass", "correct": True},
            {"text": "None of them bend a ray by different amounts",
             "correct": False,
             "why": "They do bend a ray by different amounts, because "
                    "they slow light down by different amounts."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e12",
        "band": "easier",
        "text": "Past a certain steep angle, light travelling inside glass "
                "cannot escape into the air at all and is reflected back "
                "inside instead. What is this effect called?",
        "options": [
            {"text": "Diffuse scattering at a rough surface",
             "correct": False,
             "why": "Diffuse scattering is light bouncing off a rough "
                    "surface in many directions, a different effect "
                    "entirely."},
            {"text": "Dispersion", "correct": False,
             "why": "Dispersion is white light being split into colours "
                    "by a prism, not light being trapped inside a "
                    "material."},
            {"text": "Absorption", "correct": False,
             "why": "Absorbed light does not come back out again at all; "
                    "here the light is reflected back inside the glass."},
            {"text": "Total internal reflection", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e13",
        "band": "easier",
        "text": "What keeps light bouncing along inside an optical fibre, "
                "even round gentle bends?",
        "options": [
            {"text": "Total internal reflection at the wall of the fibre",
             "correct": True},
            {"text": "A thin layer of silver coating the inside of the "
                     "fibre", "correct": False,
             "why": "No metal coating is needed at all — the trapping "
                    "happens because of the glass-to-air boundary itself."},
            {"text": "The light being refracted into sound at each bend",
             "correct": False,
             "why": "Light does not turn into sound at any point along "
                    "the fibre."},
            {"text": "Magnets built into the fibre's casing",
             "correct": False,
             "why": "Nothing magnetic is involved in trapping light "
                    "inside an optical fibre."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e14",
        "band": "easier",
        "text": "Refracted light makes a submerged object appear somewhere "
                "it is not. What does the eye do that causes this?",
        "options": [
            {"text": "It allows for the bending automatically, but "
                     "slightly overdoes the correction it applies",
             "correct": False,
             "why": "The eye makes no correction at all, large or small. "
                    "It simply takes the light as it arrives."},
            {"text": "It assumes the light reached it in a straight line",
             "correct": True},
            {"text": "It times how long the light took to arrive and "
                     "works the position back from that", "correct": False,
             "why": "The eye cannot time light. All it registers is the "
                    "direction the light was travelling when it arrived."},
            {"text": "It watches the object shift as the water moves, and "
                     "settles on the average position", "correct": False,
             "why": "The object does not shift, and the effect is there "
                    "on perfectly still water with nothing moving."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e15",
        "band": "easier",
        "text": "Light travels at about 197 000 000 m/s inside glass, "
                "compared with 300 000 000 m/s in a vacuum. Which "
                "statement fits these figures?",
        "options": [
            {"text": "Glass makes light travel faster than in a vacuum",
             "correct": False,
             "why": "197 000 000 is a smaller number than 300 000 000, so "
                    "the light is slower, not faster, inside the glass."},
            {"text": "The two figures show light barely changes speed at "
                     "all", "correct": False,
             "why": "A drop from 300 000 000 to 197 000 000 m/s is a "
                    "substantial change, not a barely noticeable one."},
            {"text": "Light slows down noticeably when it enters glass",
             "correct": True},
            {"text": "Glass has no effect on the speed of light passing "
                     "through it", "correct": False,
             "why": "The figures show a clear drop in speed, so glass "
                    "plainly does affect it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e16",
        "band": "easier",
        "text": "Light travels at about 226 000 000 m/s inside water. Is "
                "this faster or slower than light in a vacuum?",
        "options": [
            {"text": "It depends on the colour of the water",
             "correct": False,
             "why": "Water's colour is not what these figures are "
                    "describing; they are simply the speed of light "
                    "travelling through it."},
            {"text": "Faster", "correct": False,
             "why": "226 000 000 is smaller than the vacuum figure of "
                    "300 000 000 m/s, so it is slower, not faster."},
            {"text": "Exactly the same", "correct": False,
             "why": "The two figures are clearly different numbers, so "
                    "the speed has changed."},
            {"text": "Slower", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e17",
        "band": "easier",
        "text": "What actually CAUSES light to bend when it crosses into a "
                "new material at an angle?",
        "options": [
            {"text": "The change in its speed as it crosses the boundary",
             "correct": True},
            {"text": "A magnetic pull from the new material",
             "correct": False,
             "why": "No magnetism is involved in refraction at all."},
            {"text": "The colour of the light changing as it crosses",
             "correct": False,
             "why": "The colour of the light stays the same; it is the "
                    "speed that changes and causes the bending."},
            {"text": "The new material physically pushing the ray "
                     "sideways", "correct": False,
             "why": "Nothing pushes the ray sideways; the bend follows "
                    "from the change of speed plus the angle of arrival."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e18",
        "band": "easier",
        "text": "Optical fibres are laid in huge numbers under the oceans "
                "in order to…",
        "options": [
            {"text": "carry an electric current more cheaply than copper "
                     "cables can", "correct": False,
             "why": "A fibre carries pulses of light, not an electric "
                    "current; no current flows along the glass at all."},
            {"text": "carry telephone and internet signals as pulses of "
                     "light", "correct": True},
            {"text": "magnify distant objects, in the way a telescope "
                     "does", "correct": False,
             "why": "A fibre guides light from one end to the other; it "
                    "does nothing to enlarge whatever is at the far end."},
            {"text": "make light of their own along their whole length, "
                     "so that no source is needed", "correct": False,
             "why": "A fibre makes no light at all; every pulse it "
                    "carries is fired in at one end by a source."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e19",
        "band": "easier",
        "text": "Does light speed up or slow down when it leaves a denser "
                "material and enters a less dense one?",
        "options": [
            {"text": "It keeps exactly the same speed", "correct": False,
             "why": "Crossing between materials of different density "
                    "changes the speed of the light."},
            {"text": "It slows down further", "correct": False,
             "why": "Slowing further happens entering a MORE dense "
                    "material, not a less dense one."},
            {"text": "It speeds up", "correct": True},
            {"text": "It stops briefly before continuing", "correct": False,
             "why": "Light never stops at a boundary; it changes speed "
                    "instantly as it crosses."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e20",
        "band": "easier",
        "text": "A prism splits white light into a band of colours. What is "
                "this splitting called?",
        "options": [
            {"text": "Reflection", "correct": False,
             "why": "Reflection is light bouncing off a surface, not "
                    "being split into colours as it passes through."},
            {"text": "Total internal reflection", "correct": False,
             "why": "That is light being trapped inside a material at a "
                    "steep angle, not being split into colours."},
            {"text": "Absorption", "correct": False,
             "why": "Absorbed light does not come back out at all, let "
                    "alone spread into colours."},
            {"text": "Dispersion", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e21",
        "band": "easier",
        "text": "Are refraction and reflection the same process?",
        "options": [
            {"text": "No — refraction is a change of direction on "
                     "entering a new material, and reflection is light "
                     "bouncing back off a surface", "correct": True},
            {"text": "Yes — both involve light bouncing straight back the "
                     "way it came", "correct": False,
             "why": "Refracted light continues on INTO the new material; "
                    "it does not bounce back."},
            {"text": "Yes — both only happen when light crosses into a "
                     "new transparent material", "correct": False,
             "why": "Reflection can happen at an opaque surface too, "
                    "where nothing is being crossed into at all."},
            {"text": "No — reflection only happens with sound, never with "
                     "light", "correct": False,
             "why": "Light reflects too — off mirrors, water and countless "
                    "other surfaces."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e22",
        "band": "easier",
        "text": "Is total internal reflection an example of reflection or "
                "of refraction?",
        "options": [
            {"text": "Refraction, because it happens at the boundary of "
                     "a transparent material, wherever that boundary "
                     "happens to be", "correct": False,
             "why": "Happening at a transparent boundary is not enough on "
                    "its own; the ray here is turned BACK rather than "
                    "carried on through."},
            {"text": "Reflection, even though it happens at a transparent "
                     "boundary rather than a mirror", "correct": True},
            {"text": "Neither — it is a completely separate process from "
                     "both", "correct": False,
             "why": "It is a genuine case of reflection, just one that "
                    "happens at a transparent boundary rather than at an "
                    "ordinary mirror."},
            {"text": "Both equally, since the light both bends and "
                     "bounces at once", "correct": False,
             "why": "The ray is turned back the way it partly came, which "
                    "is reflection, not a bend continuing onward."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e23",
        "band": "easier",
        "text": "Sending a beam from air into a block of perspex at an "
                "angle, which way does it bend?",
        "options": [
            {"text": "away from the normal", "correct": False,
             "why": "That happens on LEAVING perspex, when the light "
                    "speeds up again."},
            {"text": "along the surface of the perspex", "correct": False,
             "why": "The ray carries on into the perspex; it does not "
                    "travel along the boundary."},
            {"text": "towards the normal", "correct": True},
            {"text": "back the way it came", "correct": False,
             "why": "That would be reflection, and only a small part of "
                    "the light does that."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e24",
        "band": "easier",
        "text": "True or false: every colour of light bends by exactly the "
                "same amount entering a glass block.",
        "options": [
            {"text": "False — in fact red light always bends more than "
                     "every other colour", "correct": False,
             "why": "It is blue light that bends slightly more than red, "
                    "not the other way round."},
            {"text": "True — colour has no effect whatsoever on how much "
                     "light bends", "correct": False,
             "why": "Colour makes a small but real difference: blue "
                    "light bends a little more than red light does."},
            {"text": "True, but only for light entering water rather "
                     "than glass", "correct": False,
             "why": "The small colour difference in bending happens in "
                    "any transparent material, glass included."},
            {"text": "False — different colours bend by very slightly "
                     "different amounts", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e25",
        "band": "easier",
        "text": "In diagrams of refraction, both the angle in the first "
                "material and the angle in the second material are "
                "measured from…",
        "options": [
            {"text": "the normal", "correct": True},
            {"text": "the boundary between the two materials",
             "correct": False,
             "why": "Both angles are measured from the normal, not from "
                    "the boundary line itself."},
            {"text": "the edge of the ray box", "correct": False,
             "why": "The ray box is just the source of the ray; angles "
                    "are measured from the normal at the boundary."},
            {"text": "whichever line looks most convenient to the "
                     "person drawing it", "correct": False,
             "why": "The normal is always used, so that everyone measures "
                    "the same angle in the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e26",
        "band": "easier",
        "text": "Does light change speed on entering a new material along "
                "the normal, even though it does not bend?",
        "options": [
            {"text": "No — with no bending there is no speed change "
                     "either", "correct": False,
             "why": "The speed changes at every angle of arrival, "
                    "including exactly along the normal — only the "
                    "bending needs an angle."},
            {"text": "Yes — the speed still changes, only the direction "
                     "stays the same", "correct": True},
            {"text": "No — speed only changes if the ray happens to "
                     "bend by more than about 10° or so", "correct": False,
             "why": "There is no such threshold; the speed changes "
                    "whatever the angle, even at 0°."},
            {"text": "It is impossible to say for certain without "
                     "measuring it very carefully and directly",
             "correct": False,
             "why": "The lesson's own facts settle this: light slows down "
                    "in a denser material at any angle of arrival."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e27",
        "band": "easier",
        "text": "Light crossing from a less dense material into a more "
                "dense one always…",
        "options": [
            {"text": "keeps the same speed but changes colour",
             "correct": False,
             "why": "Its colour is unaffected; it is the speed that "
                    "changes, not the colour."},
            {"text": "speeds up", "correct": False,
             "why": "Speeding up happens crossing the OTHER way, from a "
                    "denser material into a less dense one."},
            {"text": "slows down", "correct": True},
            {"text": "reflects completely, with none of it getting "
                     "through", "correct": False,
             "why": "Most of the light carries on through into the new "
                    "material; only a small fraction is reflected."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e28",
        "band": "easier",
        "text": "For a ray to visibly bend at a boundary, in what way must "
                "it arrive?",
        "options": [
            {"text": "Passing through a specially shaped lens first "
                     "before reaching the boundary", "correct": False,
             "why": "No lens is needed for ordinary refraction at a flat "
                    "boundary between two materials."},
            {"text": "Travelling extremely fast", "correct": False,
             "why": "Speed is not the condition here; it is the angle "
                    "the ray arrives at."},
            {"text": "Coloured red or blue only", "correct": False,
             "why": "Any colour of light refracts at a boundary; colour "
                    "is not the deciding factor."},
            {"text": "At an angle to the normal, never straight along it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e29",
        "band": "easier",
        "text": "True or false: refraction can only happen when light "
                "moves from a gas into a liquid.",
        "options": [
            {"text": "False — it happens between any two materials in which "
                     "light travels at different speeds, whatever their states "
                     "of matter",
             "correct": True},
            {"text": "True — a gas and a liquid are the only pair of "
                     "states of matter it can ever work between, "
                     "whatever the two materials happen to be",
             "correct": False,
             "why": "Refraction also happens between two solids, or a "
                    "liquid and a solid, whenever their speeds for light "
                    "differ."},
            {"text": "True — refraction needs a change of state to occur "
                     "at all", "correct": False,
             "why": "No change of state is needed; the materials simply "
                    "stay as they are while the light crosses between "
                    "them."},
            {"text": "False — refraction only ever happens inside a "
                     "single material", "correct": False,
             "why": "Refraction happens exactly AT the boundary between "
                    "two different materials, not inside just one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-e30",
        "band": "easier",
        "text": "Fired directly along the normal into a perspex block, "
                "does the ray change direction at all?",
        "options": [
            {"text": "It bends towards the normal", "correct": False,
             "why": "It is already travelling along the normal, so there "
                    "is no angle for it to bend towards."},
            {"text": "It carries straight on", "correct": True},
            {"text": "It bends away from the normal", "correct": False,
             "why": "That happens leaving a denser material at an angle, "
                    "not arriving along the normal."},
            {"text": "It splits into two separate rays", "correct": False,
             "why": "A single ray entering along the normal stays a "
                    "single ray; it does not split in two."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p7-03-s09",
        "band": "standard",
        "text": "Put water, perspex and glass in order from LEAST bending "
                "to MOST bending, for rays arriving at the same angle.",
        "options": [
            {"text": "Water, perspex, glass", "correct": True},
            {"text": "Glass, perspex, water", "correct": False,
             "why": "That is the order reversed; glass bends the most, "
                    "not the least."},
            {"text": "Perspex, water, glass", "correct": False,
             "why": "Water bends light less than perspex does, so water "
                    "should come first."},
            {"text": "All three bend a ray by the same amount",
             "correct": False,
             "why": "They bend a ray by different amounts, since they "
                    "slow light down by different amounts."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s10",
        "band": "standard",
        "text": "Light travels at about 197 000 000 m/s in glass and "
                "300 000 000 m/s in a vacuum. Roughly what fraction of "
                "its vacuum speed is that?",
        "options": [
            {"text": "About a half", "correct": False,
             "why": "Half of 300 000 000 would be 150 000 000, "
                    "noticeably less than the actual 197 000 000 m/s."},
            {"text": "About two thirds", "correct": True},
            {"text": "About a quarter", "correct": False,
             "why": "A quarter of 300 000 000 is 75 000 000, far below "
                    "the actual figure."},
            {"text": "About nine tenths", "correct": False,
             "why": "Nine tenths of 300 000 000 would be 270 000 000, "
                    "well above the actual figure."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s11",
        "band": "standard",
        "text": "Light travels at about 226 000 000 m/s in water and "
                "201 000 000 m/s in perspex. Which is faster, light in "
                "water or light in perspex?",
        "options": [
            {"text": "They are exactly the same speed", "correct": False,
             "why": "The two figures given are clearly different from "
                    "one another."},
            {"text": "Light in perspex", "correct": False,
             "why": "226 000 000 is a bigger number than 201 000 000, so "
                    "water is the faster of the two."},
            {"text": "Light in water", "correct": True},
            {"text": "It cannot be worked out from these figures",
             "correct": False,
             "why": "Comparing two given speeds directly tells you which "
                    "is larger — no further information is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s12",
        "band": "standard",
        "text": "A ray travels straight along the normal through a glass "
                "block, so it does not bend at all. Does it still take "
                "longer to cross the block than the same length of path "
                "would take in air?",
        "options": [
            {"text": "It is impossible to know without also knowing the "
                     "colour of the ray", "correct": False,
             "why": "The given speeds for glass and air settle this "
                    "without needing to know the ray's colour."},
            {"text": "No — with no bending, there is no change in "
                     "travel time either", "correct": False,
             "why": "The ray has genuinely slowed down inside the "
                    "glass, which alone makes the crossing take longer."},
            {"text": "No — glass is transparent, so light crosses it "
                     "just as quickly as it crosses air", "correct": False,
             "why": "Glass slows light down significantly, whatever its "
                    "transparency; the crossing takes measurably longer."},
            {"text": "Yes — it has slowed down inside the glass, even though "
                     "it never bent", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s13",
        "band": "standard",
        "text": "Two identical rays enter two glass blocks at the same "
                "angle: one block is thin, the other much thicker. Which "
                "block shifts its ray sideways by more on the far side?",
        "options": [
            {"text": "The thick block", "correct": True},
            {"text": "The thin block", "correct": False,
             "why": "A shorter path through the block gives less "
                    "distance for the sideways shift to build up."},
            {"text": "Both shift the ray sideways by exactly the same "
                     "amount", "correct": False,
             "why": "The thicker block gives the bent ray a longer path "
                    "to travel before it reaches the far face, producing "
                    "a bigger sideways shift."},
            {"text": "Neither block shifts the ray sideways at all",
             "correct": False,
             "why": "A ray crossing at an angle through a parallel-sided "
                    "block always emerges shifted sideways from its "
                    "original line."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s14",
        "band": "standard",
        "text": "A ray enters water at 40° and refracts to 30° inside. If "
                "the same ray instead entered glass at 40°, would the "
                "angle inside be more or less than 30°?",
        "options": [
            {"text": "More than 30°, since glass is more transparent than "
                     "water", "correct": False,
             "why": "Transparency is not what decides the amount of "
                    "bending; how much the material slows light does."},
            {"text": "Less than 30°, since glass bends the ray more than "
                     "water does", "correct": True},
            {"text": "Exactly 30°, since the incidence angle is the same "
                     "in both cases", "correct": False,
             "why": "The incidence angle being the same does not mean "
                    "the refracted angle will match — that also depends "
                    "on the material."},
            {"text": "It cannot bend at all in glass, since glass is a "
                     "solid", "correct": False,
             "why": "Glass being a solid does not stop it refracting "
                    "light; solids refract light just as liquids do."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s15",
        "band": "standard",
        "text": "Why does a lifeguard need to allow for refraction when "
                "judging exactly where a swimmer is under the water?",
        "options": [
            {"text": "Because the swimmer's own movement makes them hard "
                     "to track", "correct": False,
             "why": "The apparent shift in position happens even for a "
                    "swimmer holding perfectly still."},
            {"text": "Because water magnifies the swimmer, making them "
                     "look bigger than they are", "correct": False,
             "why": "Size is not the issue here; it is the APPARENT "
                    "POSITION of the swimmer that is shifted by "
                    "refraction."},
            {"text": "Because light from the swimmer bends on leaving "
                     "the water, making them appear in a different "
                     "position than they really are", "correct": True},
            {"text": "Because water absorbs most of the light reflected "
                     "from the swimmer", "correct": False,
             "why": "Absorption would make the swimmer harder to see, "
                    "not shift where they appear to be."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s16",
        "band": "standard",
        "text": "A spear-fisher aims directly at the visual position of a "
                "fish underwater and misses. Should they aim above or "
                "below that apparent position to compensate for "
                "refraction, and why?",
        "options": [
            {"text": "Above it, because water magnifies the fish upward "
                     "as well as sideways", "correct": False,
             "why": "Magnification is not the effect at work here; it is "
                    "a shift in apparent DEPTH caused by the light "
                    "bending."},
            {"text": "Above it, because refraction genuinely makes the "
                     "fish look lower down than it really is under the "
                     "water", "correct": False,
             "why": "Refraction makes the fish appear NEARER the "
                    "surface, not further from it, so aiming above would "
                    "make the miss worse."},
            {"text": "Neither — the fish's apparent position is always "
                     "exactly correct", "correct": False,
             "why": "Refraction genuinely shifts where the fish appears "
                    "to be, which is exactly why the first shot missed."},
            {"text": "Below it, because refraction makes the fish look "
                     "higher and closer to the surface than it really is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s17",
        "band": "standard",
        "text": "A laser is shone through the glass wall of a fish tank "
                "into the water inside. At how many boundaries does it "
                "refract before reaching the water?",
        "options": [
            {"text": "Two — once entering the glass, and again entering "
                     "the water", "correct": True},
            {"text": "One — only at the glass-to-water boundary",
             "correct": False,
             "why": "The ray also crosses from air into the glass first, "
                    "which is a boundary of its own."},
            {"text": "None — glass and water are both transparent, so no "
                     "bending happens", "correct": False,
             "why": "Being transparent does not stop refraction; both "
                    "boundaries here involve a genuine change of speed."},
            {"text": "Three — the ray also refracts once inside the "
                     "glass itself, away from any boundary",
             "correct": False,
             "why": "Refraction happens AT a boundary between two "
                    "materials, not partway through travelling within "
                    "one uniform material."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s18",
        "band": "standard",
        "text": "Which would cause a bigger, more direct change in how "
                "much a ray bends at a glass boundary: increasing the "
                "angle of incidence, or switching to a different colour "
                "of light?",
        "options": [
            {"text": "Switching the colour of the light used always has "
                     "a far bigger overall effect than changing the "
                     "incidence angle", "correct": False,
             "why": "Colour affects bending only very slightly; the "
                    "angle of incidence is by far the stronger, more "
                    "direct control."},
            {"text": "Increasing the angle of incidence causes a much bigger, "
                     "more direct change than switching colour ever does", "correct": True},
            {"text": "Neither has any effect on the amount of bending at "
                     "all", "correct": False,
             "why": "Both do have some effect — the angle a large one, "
                    "and colour a small one."},
            {"text": "Both always cause exactly the same amount of "
                     "change, whatever the situation", "correct": False,
             "why": "The angle of incidence produces a far bigger change "
                    "than switching colour does."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s19",
        "band": "standard",
        "text": "A ray crosses from air into water at 25°, bending towards "
                "the normal. It then continues travelling through the "
                "water in a straight line, without hitting anything "
                "else. Does it bend again on its own?",
        "options": [
            {"text": "Yes, but only if the water is unusually deep",
             "correct": False,
             "why": "Depth makes no difference here — a ray in one "
                    "uniform material travels in a straight line, "
                    "whatever the distance."},
            {"text": "Yes — it keeps bending gradually the further it "
                     "travels through the water", "correct": False,
             "why": "Refraction happens once, at the boundary; a ray "
                    "travelling on through one uniform material keeps "
                    "going in a straight line."},
            {"text": "No — a ray only bends AT a boundary between two "
                     "different materials, not while travelling through "
                     "one uniform material", "correct": True},
            {"text": "It depends on the colour of the ray",
             "correct": False,
             "why": "Colour affects how much a ray bends AT a boundary, "
                    "not whether it keeps bending afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s20",
        "band": "standard",
        "text": "Light takes roughly 1.5 times as long to cross a given "
                "thickness of glass as the same thickness of air, since "
                "glass slows it to about two thirds of its speed. Why "
                "does a SLOWER speed lead to a LONGER time for the same "
                "distance?",
        "options": [
            {"text": "There is no real underlying connection between "
                     "speed and time in this situation at all — it "
                     "simply happens to work out that way by "
                     "coincidence", "correct": False,
             "why": "Time equals distance divided by speed is a genuine, "
                    "reliable relationship, not a coincidence."},
            {"text": "Because slower light has further to travel than "
                     "faster light does", "correct": False,
             "why": "The distance — the thickness of the material — is "
                    "the same in both cases; only the speed differs."},
            {"text": "Because a slower ray has to bend more times before "
                     "it reaches the far side", "correct": False,
             "why": "The ray bends only once, on entering; how many "
                    "times it bends does not change the crossing time."},
            {"text": "Because time taken equals the distance divided by "
                     "the speed, so a smaller speed gives a bigger time "
                     "for the same distance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s21",
        "band": "standard",
        "text": "A student says a ray bends towards the normal both "
                "entering AND leaving a glass block. Are they right?",
        "options": [
            {"text": "No — it bends towards the normal entering, and "
                     "away from the normal leaving", "correct": True},
            {"text": "Yes — the direction of bending is always towards "
                     "the normal, whichever way the ray is travelling",
             "correct": False,
             "why": "Leaving a denser material, the ray speeds up and "
                    "bends AWAY from the normal, not towards it."},
            {"text": "No — it bends away from the normal on both "
                     "occasions instead", "correct": False,
             "why": "Entering the denser glass, the ray slows down and "
                    "bends TOWARDS the normal, not away from it."},
            {"text": "It depends entirely on the colour of the ray",
             "correct": False,
             "why": "Colour makes only a very slight difference to the "
                    "amount of bending, not to which way it bends "
                    "entering or leaving."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s22",
        "band": "standard",
        "text": "Which ray would bend the LEAST on entering glass from "
                "air: one arriving at 5° to the normal, or one at 60° to "
                "the normal?",
        "options": [
            {"text": "The one at 60°", "correct": False,
             "why": "Arriving closer to the normal, at 5°, gives the "
                    "smaller bend, not the larger angle of 60°."},
            {"text": "The one at 5°", "correct": True},
            {"text": "Both bend by exactly the same amount",
             "correct": False,
             "why": "How much a ray bends depends on the angle it "
                    "arrives at, so these two would not bend equally."},
            {"text": "Neither bends at all, since both are entering the "
                     "same glass", "correct": False,
             "why": "Both rays do bend, since both arrive at an angle "
                    "other than exactly along the normal."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s23",
        "band": "standard",
        "text": "Speeds in millions of m/s: vacuum 300, water 226, "
                "perspex 201, glass 197. Which pair of these materials "
                "would show the SMALLEST difference in bending for the "
                "same incidence angle?",
        "options": [
            {"text": "Water and perspex", "correct": False,
             "why": "Their speeds differ by 25 million m/s, a bigger "
                    "gap than the closest pair here."},
            {"text": "Water and glass", "correct": False,
             "why": "Their speeds differ by 29 million m/s, the biggest "
                    "gap of the three pairs."},
            {"text": "Perspex and glass", "correct": True},
            {"text": "All three pairs would differ by the same amount",
             "correct": False,
             "why": "The three gaps between the given speeds are not "
                    "equal to one another."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s24",
        "band": "standard",
        "text": "A ray entering glass at 50° bends to 30° inside — a 20° "
                "change. Would a ray entering at a smaller angle, say "
                "20°, bend by more than, less than, or exactly 20°?",
        "options": [
            {"text": "It cannot bend at all below 50°", "correct": False,
             "why": "A ray bends at any non-zero angle of incidence, not "
                    "only at or above 50°."},
            {"text": "Exactly 20°, since the material has not changed",
             "correct": False,
             "why": "The material staying the same does not mean every "
                    "incidence angle gives the same-sized bend — smaller "
                    "angles give smaller bends."},
            {"text": "More than 20°, since smaller angles always bend "
                     "more", "correct": False,
             "why": "Smaller angles of incidence give SMALLER bends, not "
                    "bigger ones — right down to no bend at all along "
                    "the normal."},
            {"text": "Less than 20°", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s25",
        "band": "standard",
        "text": "A laser fires one pulse into a block of air and, at the "
                "same angle, another pulse into an equal thickness of "
                "water. Which pulse crosses its material first?",
        "options": [
            {"text": "The pulse through the air", "correct": True},
            {"text": "The pulse through the water", "correct": False,
             "why": "Water slows light down compared with air, so this "
                    "pulse takes longer to cross the same thickness."},
            {"text": "Both arrive at exactly the same moment",
             "correct": False,
             "why": "Since the two materials slow light by different "
                    "amounts, the crossing times are not equal."},
            {"text": "Neither pulse can be timed, since they are "
                     "travelling through different materials",
             "correct": False,
             "why": "Both pulses have a well-defined speed in their own "
                    "material, so both crossing times can be compared."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s26",
        "band": "standard",
        "text": "Why does the same glass block bend red light very "
                "slightly less than blue light?",
        "options": [
            {"text": "Red light is somehow physically heavier than blue "
                     "light, which is supposed to make it harder for "
                     "the glass to bend", "correct": False,
             "why": "Light has no weight in this sense; the small "
                    "difference comes from a tiny difference in speed, "
                    "not weight."},
            {"text": "Different colours travel at very slightly "
                     "different speeds in glass, and blue is slowed a "
                     "little more than red", "correct": True},
            {"text": "Blue light always travels in straight lines, "
                     "unlike red light", "correct": False,
             "why": "Both colours travel in straight lines between "
                    "boundaries; both refract at a boundary too, just "
                    "by very slightly different amounts."},
            {"text": "Glass reflects red light instead of letting it "
                     "through", "correct": False,
             "why": "Almost all the red light passes through the glass, "
                    "just as the blue light does — it is simply bent by "
                    "a very slightly smaller amount."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s27",
        "band": "standard",
        "text": "A ray travels from glass into water, both transparent, "
                "with water less dense than glass. Does it speed up or "
                "slow down, and which way does it bend?",
        "options": [
            {"text": "It speeds up but does not bend at all, since both "
                     "materials are transparent", "correct": False,
             "why": "Both being transparent does not stop the bending — "
                    "the two materials still slow light by different "
                    "amounts."},
            {"text": "It slows down further and bends towards the "
                     "normal", "correct": False,
             "why": "Moving into the LESS dense water, the ray speeds "
                    "up rather than slowing down further."},
            {"text": "It always speeds up and bends away from the normal",
             "correct": True},
            {"text": "It slows down and bends away from the normal",
             "correct": False,
             "why": "The bending direction here is right, but the speed "
                    "increases moving into the less dense water, rather "
                    "than decreasing."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s28",
        "band": "standard",
        "text": "One transparent material is 'optically denser' than "
                "another if it slows light down more. Which would you "
                "expect the optically denser one to do to a ray arriving "
                "at the same angle?",
        "options": [
            {"text": "Bend it less than the other material would",
             "correct": False,
             "why": "A material that slows light MORE produces a bigger "
                    "bend, not a smaller one, at the same angle."},
            {"text": "Reflect the ray completely rather than letting it "
                     "through", "correct": False,
             "why": "Being denser does not stop the light passing "
                    "through; most of it still crosses into the material."},
            {"text": "Have no effect on the angle of the ray at all",
             "correct": False,
             "why": "Slowing light down at an angle is exactly what "
                    "causes bending in the first place."},
            {"text": "Bend it more than the other material would",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s29",
        "band": "standard",
        "text": "A ray travelling inside a glass block reaches the "
                "glass-to-air surface at a shallow angle to the normal, "
                "well short of the angle at which total internal "
                "reflection begins. What happens to most of the light?",
        "options": [
            {"text": "Most of it passes out into the air, bent further "
                     "from the normal than it was inside", "correct": True},
            {"text": "All of it is reflected back inside, because the ray "
                     "began its journey inside the glass", "correct": False,
             "why": "Starting inside the glass is not enough on its own; "
                    "the angle has to be steep enough before the light is "
                    "trapped."},
            {"text": "It is absorbed at the surface, so almost none of it "
                     "travels on at all", "correct": False,
             "why": "A clean glass-to-air surface absorbs very little; "
                    "almost all of the light carries on out into the air."},
            {"text": "It passes out without bending, because it is "
                     "leaving the glass rather than entering it",
             "correct": False,
             "why": "Leaving a denser material at an angle bends the ray; "
                    "only a ray along the normal passes out undeviated."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-s30",
        "band": "standard",
        "text": "Light slows from about 300 000 000 m/s in air to about "
                "226 000 000 m/s in water. Roughly by what fraction does "
                "its speed drop?",
        "options": [
            {"text": "By about a half", "correct": False,
             "why": "Half of 300 000 000 would be 150 000 000, well "
                    "below the actual water speed of 226 000 000 m/s."},
            {"text": "By about a quarter", "correct": True},
            {"text": "By about a tenth", "correct": False,
             "why": "A tenth of 300 000 000 is only 30 000 000, a "
                    "smaller drop than the actual figures show."},
            {"text": "It does not drop at all, since water is "
                     "transparent", "correct": False,
             "why": "The two figures are clearly different, showing a "
                    "genuine drop in speed on entering water."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "p7-03-h09",
        "band": "harder",
        "text": "A ray enters a glass block at 50° and is measured "
                "bending to 30° inside. If the SAME ray were instead "
                "fired into a much THICKER block of the SAME glass at "
                "the same 50°, would the angle inside change?",
        "options": [
            {"text": "No — the angle of refraction depends on the "
                     "incidence angle and the material, not on how "
                     "thick the block is", "correct": True},
            {"text": "Yes — a noticeably thicker block of the same "
                     "glass would bend the ray to a smaller angle once "
                     "it is inside", "correct": False,
             "why": "Thickness changes how far the bent ray travels "
                    "before reaching the far face, not the angle it "
                    "bends to at the first surface."},
            {"text": "Yes — a thicker block would bend the ray to a "
                     "larger angle inside", "correct": False,
             "why": "The angle of refraction is set at the point of "
                    "entry, by the incidence angle and the material — "
                    "the thickness beyond that point makes no "
                    "difference to it."},
            {"text": "It cannot be predicted without knowing the "
                     "colour of the ray", "correct": False,
             "why": "Colour makes only a tiny difference to the bend; "
                    "block thickness makes none to the angle at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h10",
        "band": "harder",
        "text": "A student claims that since a ray bends 20° entering "
                "glass at 50°, it must bend exactly 10° entering at "
                "25° — half the angle giving half the bend. Evaluate "
                "this.",
        "options": [
            {"text": "The claim is exactly right in every case, because "
                     "the amount of bending is always directly and "
                     "exactly proportional to the incidence angle",
             "correct": False,
             "why": "The relationship between the two angles is more "
                    "complicated than simple direct proportion; halving "
                    "the incidence angle need not exactly halve the "
                    "bend."},
            {"text": "Not necessarily — smaller angles give smaller "
                     "bends in general, but the exact relationship is "
                     "not a simple straight proportion like halving",
             "correct": True},
            {"text": "The claim is wrong the other way round — smaller "
                     "angles actually produce BIGGER bends",
             "correct": False,
             "why": "Smaller angles of incidence give smaller bends, "
                    "down to no bend at all along the normal — the "
                    "general trend the student describes is correct."},
            {"text": "There is no relationship at all between the "
                     "incidence angle and how much a ray bends",
             "correct": False,
             "why": "There plainly is a relationship — a bigger angle "
                    "of incidence generally produces a bigger bend."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h11",
        "band": "harder",
        "text": "A pulse crosses 20 cm of water and a separate pulse "
                "crosses 20 cm of glass. Which takes longer, and why?",
        "options": [
            {"text": "Both pulses take exactly the same amount of time "
                     "to cross, since both materials involved are "
                     "transparent", "correct": False,
             "why": "Being transparent does not mean two materials slow "
                    "light by the same amount — glass and water give "
                    "different speeds."},
            {"text": "The water pulse takes slightly longer, because "
                     "water is denser than glass", "correct": False,
             "why": "Water is the LESS dense of the two here — it slows "
                    "light less than glass does, so its pulse crosses "
                    "faster, not slower."},
            {"text": "The glass pulse takes slightly longer, because "
                     "glass slows light more than water does",
             "correct": True},
            {"text": "Neither pulse can really be timed accurately, "
                     "since 20 cm is much too short a distance to "
                     "measure well", "correct": False,
             "why": "The distance being short does not prevent a "
                    "genuine difference in crossing time between the "
                    "two materials."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h12",
        "band": "harder",
        "text": "Two students argue about whether refraction can happen "
                "between two SOLIDS, such as glass and perspex pressed "
                "together, rather than only between a solid and air. "
                "Who is right?",
        "options": [
            {"text": "Refraction never happens at all between two "
                     "transparent solids pressed together, only ever "
                     "between a transparent material and an opaque one",
             "correct": False,
             "why": "Both materials at a refracting boundary need to be "
                    "transparent enough to let light through — being "
                    "solid is not what rules it out."},
            {"text": "Refraction can only happen when one of the two "
                     "materials is a gas, such as air", "correct": False,
             "why": "Refraction needs a change of speed at a boundary, "
                    "which can occur between two solids just as it does "
                    "between a solid and a gas."},
            {"text": "Refraction can only happen when one of the two "
                     "materials is a liquid", "correct": False,
             "why": "A liquid is not required; a glass-to-perspex "
                    "boundary between two solids can refract light too."},
            {"text": "Refraction happens at any boundary between two "
                     "materials where light travels at different "
                     "speeds, whatever states of matter they are",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h13",
        "band": "harder",
        "text": "Moving from perspex into glass — the denser of the "
                "two — what happens to a ray's speed, and to its "
                "direction relative to the normal?",
        "options": [
            {"text": "It slows down further and bends towards the "
                     "normal", "correct": True},
            {"text": "It speeds up and bends away from the normal",
             "correct": False,
             "why": "Moving into the MORE dense glass, the ray slows "
                    "down further rather than speeding up."},
            {"text": "It slows down further but does not bend, since "
                     "both materials are solids", "correct": False,
             "why": "Both being solids does not prevent bending; the "
                    "ray still bends because the two materials slow "
                    "light by different amounts."},
            {"text": "It speeds up and bends towards the normal",
             "correct": False,
             "why": "The bending direction here is wrong for a ray "
                    "entering a MORE dense material — it should bend "
                    "towards the normal while also slowing further, not "
                    "speeding up."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h14",
        "band": "harder",
        "text": "A textbook claims total internal reflection only happens "
                "in glass. Is this accurate?",
        "options": [
            {"text": "Yes — glass is the only material with the right "
                     "properties for it", "correct": False,
             "why": "Total internal reflection can occur at a boundary "
                    "involving water, perspex or many other transparent "
                    "materials too, not glass alone."},
            {"text": "No — it can happen at the boundary of any "
                     "sufficiently dense transparent material and a "
                     "less dense one, given a steep enough angle",
             "correct": True},
            {"text": "No — it actually only happens in water, never in "
                     "glass at all", "correct": False,
             "why": "It can happen at a glass boundary too, given a "
                    "steep enough angle — glass is in fact the most "
                    "familiar example, as in optical fibres."},
            {"text": "Yes, because only glass is transparent enough for "
                     "the effect to occur", "correct": False,
             "why": "Many transparent materials besides glass, "
                    "including water and perspex, are transparent "
                    "enough for the same effect."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h15",
        "band": "harder",
        "text": "A designer proposes making an optical fibre out of "
                "ordinary window glass, reasoning that 'glass bends "
                "light, so any glass will do.' What is missing from "
                "this reasoning?",
        "options": [
            {"text": "Window glass cannot bend light at all, unlike "
                     "specially made optical fibres", "correct": False,
             "why": "Ordinary window glass does refract light; the "
                    "missing ingredient is the fibre's SHAPE, not "
                    "whether the glass itself can bend light."},
            {"text": "Nothing at all is missing here — merely being "
                     "able to bend light is enough on its own to "
                     "guarantee trapping it completely inside any fibre "
                     "shape whatsoever, however it is made",
             "correct": False,
             "why": "Ordinary refraction alone lets most light straight "
                    "through a boundary; trapping it needs a steep "
                    "enough angle for total internal reflection "
                    "specifically."},
            {"text": "Not every arrangement traps light by total "
                     "internal reflection — the fibre's shape has to "
                     "ensure light hits the inner wall at a steep "
                     "enough angle", "correct": True},
            {"text": "Optical fibres actually work using reflection off "
                     "an internal metal coating, not refraction at all",
             "correct": False,
             "why": "No metal coating is used; the trapping relies on "
                    "total internal reflection at the glass-to-air "
                    "boundary itself."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h16",
        "band": "harder",
        "text": "Explain why an optical fibre continues to trap light "
                "even when it is bent round a gentle curve.",
        "options": [
            {"text": "Bending the fibre slows the light down enough "
                     "that it can no longer escape", "correct": False,
             "why": "It is the STEEP ANGLE to the local normal that "
                    "keeps the light trapped, not a change in its speed "
                    "caused by the bend."},
            {"text": "Bending the fibre switches the process from total "
                     "internal reflection to ordinary mirror reflection "
                     "instead", "correct": False,
             "why": "The process stays total internal reflection "
                    "throughout the bend; no metal or coating is "
                    "introduced by curving the fibre."},
            {"text": "The light briefly leaves the fibre at the bend "
                     "and re-enters further along", "correct": False,
             "why": "The light stays inside the fibre the whole way, "
                    "provided the bend is not too sharp for the angle "
                    "to remain steep enough."},
            {"text": "At the curve, the ray still strikes the inner "
                     "wall at a steep angle to the LOCAL normal, which "
                     "curves with the fibre, so total internal "
                     "reflection keeps happening", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h17",
        "band": "harder",
        "text": "A student says: 'Since a mirror and total internal "
                "reflection both send light back the way it partly "
                "came, they must be the same physical process.' Are "
                "they the same?",
        "options": [
            {"text": "No — a mirror reflects via a coated surface at "
                     "any angle, while total internal reflection is a "
                     "refraction-related effect that only happens past "
                     "a steep enough angle, with no coating involved",
             "correct": True},
            {"text": "Yes — both rely on a metal or silvered coating to "
                     "send the light back", "correct": False,
             "why": "Total internal reflection needs no coating at all "
                    "— it happens purely at a transparent boundary, "
                    "unlike an ordinary mirror."},
            {"text": "Yes — both happen at every possible angle of "
                     "incidence, without exception", "correct": False,
             "why": "An ordinary mirror reflects at any angle, but "
                    "total internal reflection only occurs past a "
                    "sufficiently steep angle — that is a genuine "
                    "difference between them."},
            {"text": "No — a mirror only works with visible light, "
                     "while total internal reflection only works with "
                     "radio waves", "correct": False,
             "why": "Both effects work with visible light; the real "
                    "difference between them is the mechanism, not "
                    "which kind of wave is involved."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h18",
        "band": "harder",
        "text": "Light takes about 1.5 times as long to cross a "
                "thickness of glass as the same thickness of air. A "
                "pulse takes 2 nanoseconds to cross a slab of air. "
                "Roughly how long would the same-thickness slab of "
                "glass take?",
        "options": [
            {"text": "About 2 nanoseconds", "correct": False,
             "why": "That ignores the extra time glass adds compared "
                    "with air, treating the two as identical."},
            {"text": "About 3 nanoseconds", "correct": True},
            {"text": "About 1.3 nanoseconds", "correct": False,
             "why": "That divides by 1.5 rather than multiplying by it "
                    "— glass should take LONGER than air, not less."},
            {"text": "About 4 nanoseconds", "correct": False,
             "why": "That doubles the air time and adds a bit more, "
                    "rather than simply multiplying by the given 1.5."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h19",
        "band": "harder",
        "text": "A ray enters water at exactly 0° (along the normal) and "
                "a second ray enters at 89° (nearly grazing). A student "
                "says both slow down by the same amount, since it is "
                "the same water. Are they right about the SLOWING, even "
                "though the BENDING differs hugely?",
        "options": [
            {"text": "No — the ray at 0° does not slow down at all, "
                     "since it does not bend", "correct": False,
             "why": "A ray along the normal slows down exactly as much "
                    "as any other ray entering the water — only its "
                    "bending is absent, not its slowing."},
            {"text": "No — the ray at 89° slows down far more than the "
                     "one at 0°, because it bends so much more",
             "correct": False,
             "why": "The final speed inside the water depends only on "
                    "the material — both rays end up travelling at the "
                    "same speed once inside, whatever their entry angle."},
            {"text": "Yes — the speed inside the water depends only on "
                     "the material, not on the angle of arrival; only "
                     "the amount of bending depends on the angle",
             "correct": True},
            {"text": "It cannot be compared, since one ray bends and "
                     "the other does not", "correct": False,
             "why": "Both rays end up at the same speed inside the "
                    "water regardless of how much either one bent on "
                    "the way in."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h20",
        "band": "harder",
        "text": "Which is the better analogy for why light bends "
                "entering a denser material at an angle: (a) a wheel "
                "rolling from hard pavement onto soft grass at an angle "
                "veers because one side slows before the other, or "
                "(b) a ball bouncing off a wall bounces because it hits "
                "something solid?",
        "options": [
            {"text": "Neither analogy has anything useful to say about "
                     "refraction", "correct": False,
             "why": "The wheel-on-grass analogy is a genuinely useful "
                    "picture of one side of the beam slowing before the "
                    "other."},
            {"text": "(b) — it genuinely captures the underlying change "
                     "of speed that is what causes refraction to happen",
             "correct": False,
             "why": "A bounce off a wall describes REFLECTION, a "
                    "completely different process with no change of "
                    "speed involved."},
            {"text": "Both are equally good analogies for refraction",
             "correct": False,
             "why": "The bouncing-ball analogy describes reflection, "
                    "not the differential slowing that actually causes "
                    "refraction."},
            {"text": "(a) — it captures the differential slowing across "
                     "the ray that actually causes the bend", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h21",
        "band": "harder",
        "text": "A ray crosses air into glass (bending towards the "
                "normal) then glass back into air (bending away from "
                "the normal), through a block with faces that are NOT "
                "parallel, unlike a rectangular block. Does the final "
                "ray necessarily end up travelling parallel to the "
                "original one?",
        "options": [
            {"text": "No — the sideways-shift-but-same-direction result "
                     "relies specifically on the two faces being "
                     "parallel; with non-parallel faces the two bends "
                     "do not cancel out", "correct": True},
            {"text": "Yes — the two bends always cancel out however the "
                     "faces of the block are shaped", "correct": False,
             "why": "The cancellation only works because a rectangular "
                    "block's two faces are parallel; a differently "
                    "shaped block changes the outcome."},
            {"text": "Yes, because glass always bends a ray back to its "
                     "original direction eventually, whatever the "
                     "block's shape", "correct": False,
             "why": "It is the parallel arrangement of the two faces "
                    "that produces this result, not a general property "
                    "of glass."},
            {"text": "No — with non-parallel faces the ray is instead "
                     "totally internally reflected and never leaves the "
                     "block", "correct": False,
             "why": "Total internal reflection depends on the angle at "
                    "the exit face, not simply on whether the two faces "
                    "are parallel."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h22",
        "band": "harder",
        "text": "A student calculates that since glass slows light to "
                "two thirds of its speed in air, light in glass must "
                "also be two thirds as 'bright' or 'powerful' as it "
                "was in air. What is wrong with this reasoning?",
        "options": [
            {"text": "The reasoning is entirely correct, since speed and "
                     "brightness always change together in step",
             "correct": False,
             "why": "Speed and brightness are separate physical "
                    "properties; one changing does not force the other "
                    "to change by the same fraction."},
            {"text": "Speed and brightness are different properties; slowing "
                     "down never dims the light",
             "correct": True},
            {"text": "The error is that light actually gets brighter, "
                     "not dimmer, as it slows down", "correct": False,
             "why": "Slowing down does not make light brighter either — "
                    "the two properties simply are not linked in this "
                    "way."},
            {"text": "There is no error at all; this is exactly how "
                     "brightness is defined in physics", "correct": False,
             "why": "Brightness is about how much light energy is "
                    "present, not about how fast the light is "
                    "travelling."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h23",
        "band": "harder",
        "text": "A ray enters a glass hemisphere aimed exactly at its "
                "curved centre, travelling along a radius of the "
                "curved surface. Does it bend on entering that curved "
                "surface?",
        "options": [
            {"text": "No — and it does not slow down either, since it "
                     "is aimed at the centre", "correct": False,
             "why": "It still slows down on entering the denser glass; "
                    "only the bending is absent here, exactly as with a "
                    "flat surface along the normal."},
            {"text": "Yes — any curved surface bends every ray that "
                     "meets it, whatever direction it arrives from",
             "correct": False,
             "why": "A ray travelling exactly along a radius meets a "
                    "curved surface at 0° to the LOCAL normal there, so "
                    "it does not bend, just as on a flat surface."},
            {"text": "No — travelling along a radius means it arrives "
                     "exactly along the local normal at that point, so "
                     "it passes straight through, though it still slows",
             "correct": True},
            {"text": "Yes, because curved surfaces have no single normal "
                     "to measure an angle from at all", "correct": False,
             "why": "A curved surface has a well-defined LOCAL normal at "
                    "every point — here that local normal happens to "
                    "line up exactly with the ray."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h24",
        "band": "harder",
        "text": "A student compares two DIFFERENT glass blocks by firing "
                "a ray into the first at 10° and into the second at "
                "70°, concluding the second block is 'more refractive' "
                "because it bends more. What is the flaw in comparing "
                "two materials using different incidence angles?",
        "options": [
            {"text": "The flaw is that 10° and 70° are both too small "
                     "to produce any measurable bending",
             "correct": False,
             "why": "Both angles are well away from 0° and would "
                    "produce clearly measurable bending in either "
                    "material."},
            {"text": "There is no flaw — a bigger bend at any angle "
                     "always proves the material is more refractive",
             "correct": False,
             "why": "A bigger incidence angle alone produces a bigger "
                    "bend, whatever the material, so this comparison "
                    "does not isolate the material's own effect."},
            {"text": "The flaw is that refraction cannot be compared "
                     "between two different materials at all",
             "correct": False,
             "why": "Materials can be fairly compared for how much they "
                    "refract — but only if the incidence angle is kept "
                    "the same for both."},
            {"text": "A bigger angle alone produces more bending "
                     "regardless of material, so the incidence angle "
                     "must be kept the SAME to fairly compare two "
                     "materials", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h25",
        "band": "harder",
        "text": "A ray crosses several parallel layers in sequence — air, "
                "a thin layer of water, then glass, then back into air "
                "— through a block shaped so all the interfaces are "
                "parallel to each other. Does the ray's FINAL overall "
                "direction differ from its original one?",
        "options": [
            {"text": "No — because every interface is parallel to the "
                     "others, the bends all cancel out in direction, "
                     "leaving the ray shifted sideways but travelling "
                     "the same way it started", "correct": True},
            {"text": "Yes — each extra layer adds its own permanent "
                     "change of direction that does not cancel out",
             "correct": False,
             "why": "As long as every interface stays parallel to the "
                    "others, the bends cancel out in direction exactly "
                    "as they do for a single parallel-sided block."},
            {"text": "Yes, because passing through more than one "
                     "material always changes the final direction",
             "correct": False,
             "why": "It is the PARALLEL arrangement of the interfaces "
                    "that matters, not simply how many materials are "
                    "crossed."},
            {"text": "No — because after passing through so many "
                     "boundaries the ray undergoes total internal "
                     "reflection instead", "correct": False,
             "why": "Total internal reflection depends on the angle at "
                    "each specific boundary, not on how many parallel "
                    "layers have already been crossed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h26",
        "band": "harder",
        "text": "Water gives a speed of about 226 000 000 m/s and "
                "perspex about 201 000 000 m/s. Roughly what percentage "
                "slower is light in perspex than in water?",
        "options": [
            {"text": "About 1.1%", "correct": False,
             "why": "That is ten times too small a percentage for the "
                    "gap between the two given figures."},
            {"text": "About 11%", "correct": True},
            {"text": "About 25 million percent, since that is the raw "
                     "difference in m/s", "correct": False,
             "why": "The raw difference in m/s is not itself a "
                    "percentage; it must be compared with the water "
                    "speed to get one."},
            {"text": "About 88%", "correct": False,
             "why": "That is roughly perspex's speed AS a percentage of "
                    "water's, not the percentage DROP between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h27",
        "band": "harder",
        "text": "A colleague claims that any material bending light a "
                "great deal must also absorb a great deal, so "
                "transparency and strong refraction are automatically "
                "in conflict. Are they right?",
        "options": [
            {"text": "Yes, because bending light always uses up some of "
                     "its energy through absorption", "correct": False,
             "why": "Bending light through refraction does not itself "
                    "require absorbing it; a material can refract "
                    "strongly while absorbing very little."},
            {"text": "Yes — the two properties always trade off "
                     "directly against one another in absolutely every "
                     "material", "correct": False,
             "why": "Diamond is both highly transparent and strongly "
                    "refractive, showing the two properties are not "
                    "automatically linked."},
            {"text": "No — a material can be highly transparent and "
                     "still bend light substantially, as diamond does",
             "correct": True},
            {"text": "No — but only because absorption and transparency "
                     "are actually exactly the same underlying property",
             "correct": False,
             "why": "Absorption and transparency are opposite ends of "
                    "the same property, but bending strength (how much "
                    "a material refracts) is a separate property from "
                    "both."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h28",
        "band": "harder",
        "text": "A student measures a new material's refraction, firing "
                "a ray in at 40° and reading 25° inside. Repeating at "
                "the same 40° a second time gives 27° instead. What "
                "does this small difference most likely suggest?",
        "options": [
            {"text": "One of the two readings must be a completely "
                     "different material entirely", "correct": False,
             "why": "A small discrepancy of a couple of degrees is "
                    "typical of measurement uncertainty, not evidence "
                    "the material itself changed."},
            {"text": "The material's refractive behaviour has genuinely "
                     "changed between the two trials", "correct": False,
             "why": "A transparent material's refracting properties do "
                    "not spontaneously change between two trials moments "
                    "apart; small reading differences are far more "
                    "likely."},
            {"text": "The speed of light itself must have changed "
                     "slightly between the two readings", "correct": False,
             "why": "The speed of light in a given material is a fixed "
                    "property; it does not fluctuate between repeated "
                    "readings like this."},
            {"text": "Ordinary measurement uncertainty, such as reading "
                     "the protractor or aligning the ray, rather than a "
                     "genuine change in the material's behaviour",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h29",
        "band": "harder",
        "text": "Would you expect a liquid that carries sound very "
                "quickly to also bend light more than one that carries "
                "sound slowly?",
        "options": [
            {"text": "Not necessarily — a material's sound speed and "
                     "how much it refracts light are unrelated "
                     "properties", "correct": True},
            {"text": "Yes — a liquid's sound speed always predicts how "
                     "much it will refract light", "correct": False,
             "why": "Sound and light travel by entirely different "
                    "mechanisms, so one speed does not reliably predict "
                    "the other."},
            {"text": "Yes, because both sound and light are simply "
                     "types of the same wave", "correct": False,
             "why": "Sound and light are very different kinds of wave — "
                    "one needs a material to travel through and the "
                    "other does not."},
            {"text": "No — a faster sound speed in a liquid always "
                     "means noticeably less bending of light, without "
                     "any exception at all", "correct": False,
             "why": "There is no reliable link either way between a "
                    "material's sound speed and how much it refracts "
                    "light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-03-h30",
        "band": "harder",
        "text": "A student argues that because total internal reflection "
                "'looks like' ordinary mirror reflection from inside "
                "the fibre, an optical fibre must actually contain tiny "
                "mirrors along its length. What is wrong with this "
                "reasoning?",
        "options": [
            {"text": "Nothing is wrong — looking like a mirror from the "
                     "inside proves that tiny mirrors must genuinely be "
                     "present", "correct": False,
             "why": "Appearing similar from the inside does not mean "
                    "the same physical mechanism is at work — no "
                    "coating is present in an ordinary optical fibre."},
            {"text": "No mirrors or coatings are involved at all — the "
                     "trapping happens purely because of the boundary's "
                     "refractive properties at a steep enough angle",
             "correct": True},
            {"text": "The fibre does contain mirrors, but only at the "
                     "two very end faces, not along its length",
             "correct": False,
             "why": "No mirrors are needed anywhere along the fibre; "
                    "the trapping relies entirely on total internal "
                    "reflection at the glass-to-air boundary."},
            {"text": "Fibres actually work by refraction alone, with no "
                     "reflection of any kind taking place",
             "correct": False,
             "why": "Total internal reflection genuinely is a form of "
                    "reflection — the flaw is assuming it needs a "
                    "physical mirror, not that no reflection occurs."},
        ],
        "figure": None,
    },
]
