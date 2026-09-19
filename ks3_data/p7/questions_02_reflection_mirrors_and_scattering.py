"""P7 lesson 02 — Reflection: mirrors and scattering: twelve questions.

Written against Design's page. The mirror-and-paper hook, the four
surfaces and the worked example are hers.

The discriminations, in the order the lesson builds them:

  · the law holds on EVERY surface, however rough (`LIGHT-05`);
  · both angles are measured from the NORMAL, never from the surface
    (`LIGHT-06`);
  · how much comes back and whether the pattern survives are DIFFERENT
    questions (`LIGHT-07`);
  · shiny is not smooth — crumpled foil settles it (`LIGHT-08`) — and the
    harder band sits here.

⚠️ POSITION IS AUTHORED — 1,2,3,0 · 3,0,1,2 · 2,3,0,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated, nor is the worked
example's figure (a ray at 20° to the mirror surface).
"""

UNIT = "P7"
LESSON = "reflection-mirrors-and-scattering"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-02-e01",
        "band": "easier",
        "text": "The normal in a ray diagram is…",
        "options": [
            {"text": "the surface the ray lands on", "correct": False,
             "why": "The surface is what the normal is drawn at right "
                    "angles to. They are two different lines."},
            {"text": "a line drawn at right angles to the surface where the "
                     "ray lands", "correct": True},
            {"text": "the reflected ray", "correct": False,
             "why": "The reflected ray is light. The normal is a "
                    "construction line, drawn to measure from."},
            {"text": "the ordinary or usual path light takes when nothing "
                     "gets in its way", "correct": False,
             "why": "It is a geometry word, not an everyday one — it means "
                    "perpendicular."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e02",
        "band": "easier",
        "text": "A ray hits a plane mirror at 35° to the normal. What is "
                "the angle of reflection?",
        "options": [
            {"text": "55°", "correct": False,
             "why": "That is the angle to the mirror surface. Both angles "
                    "in the rule are measured from the normal."},
            {"text": "70°", "correct": False,
             "why": "Seventy is the angle between the two rays. The angle "
                    "of reflection is from the normal to one of them."},
            {"text": "35°", "correct": True},
            {"text": "0°", "correct": False,
             "why": "A ray only leaves along the normal if it arrived along "
                    "the normal."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e03",
        "band": "easier",
        "text": "Reflection at a smooth surface, where parallel rays stay "
                "parallel, is called…",
        "options": [
            {"text": "diffuse scattering", "correct": False,
             "why": "Diffuse scattering is the rough-surface case, where "
                    "the rays leave in all directions."},
            {"text": "refraction", "correct": False,
             "why": "Refraction is bending on entering a new material, not "
                    "bouncing off a surface."},
            {"text": "absorption", "correct": False,
             "why": "Absorption is the light that does not leave at all."},
            {"text": "specular reflection", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e04",
        "band": "easier",
        "text": "Why can you see a sheet of white paper from anywhere in a "
                "room?",
        "options": [
            {"text": "Because it scatters the light that lands on it in all "
                     "directions", "correct": True},
            {"text": "Because it gives out light of its own",
             "correct": False,
             "why": "Paper is not a source. Take every lamp out of the room "
                    "and it disappears."},
            {"text": "Because it reflects every ray straight back where it "
                     "came from", "correct": False,
             "why": "Then only somebody standing where the lamp is could "
                    "see it."},
            {"text": "Because white surfaces bend light towards the "
                     "viewer", "correct": False,
             "why": "Nothing bends light towards a viewer. The rays leave "
                    "in every direction and some of them happen to reach "
                    "you."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-02-s01",
        "band": "standard",
        "text": "A ray arrives at a sheet of rough card at 40° to the "
                "normal of the card as a whole. What happens to that one "
                "ray?",
        "options": [
            {"text": "It leaves at a random angle, because a rough surface "
                     "scatters at random", "correct": False,
             "why": "Nothing about reflection is random. The ray obeys the "
                    "law exactly at the facet it lands on."},
            {"text": "It is absorbed, because a rough surface has no smooth "
                     "face to reflect from", "correct": False,
             "why": "Every tiny facet is smooth, and rough surfaces reflect "
                    "a great deal — white card sends back most of what "
                    "lands on it."},
            {"text": "It leaves at 40° to the normal of the card as a "
                     "whole, as a mirror would", "correct": False,
             "why": "It leaves at 40° to the normal of its own tiny facet, "
                    "which points somewhere else. That is why the fan "
                    "spreads."},
            {"text": "It leaves at 40° from the normal of the tiny facet it "
                     "actually landed on", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s02",
        "band": "standard",
        "text": "Matt black card and white paper are both rough. What is "
                "different about them?",
        "options": [
            {"text": "The black card absorbs most of the light, so very "
                     "little leaves it in any direction", "correct": True},
            {"text": "The black card is smooth on the scale of light, so it "
                     "reflects specularly and shows an image",
             "correct": False,
             "why": "Matt means rough. If it were smooth you would see "
                    "yourself in it, as you can in black gloss paint."},
            {"text": "The black card scatters the light more widely",
             "correct": False,
             "why": "Both scatter over the same range. The difference is "
                    "how much is left to scatter."},
            {"text": "The black card breaks the law of reflection",
             "correct": False,
             "why": "Nothing breaks it. What the card does is absorb, which "
                    "happens before any reflecting."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s03",
        "band": "standard",
        "text": "A ray strikes a mirror at 15° to the mirror surface. What "
                "is the angle of incidence?",
        "options": [
            {"text": "15°", "correct": False,
             "why": "That is the angle to the SURFACE. The angle of "
                    "incidence is measured from the normal."},
            {"text": "75°", "correct": True},
            {"text": "105°", "correct": False,
             "why": "That adds the 15° to the 90° of the normal instead of "
                    "taking it away."},
            {"text": "30°", "correct": False,
             "why": "Thirty is twice the given angle, which is the angle "
                    "between the incoming ray and the reflected one when "
                    "each is 15° from the mirror."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s04",
        "band": "standard",
        "text": "Why does a puddle show a reflection of the sky and a dry "
                "pavement does not?",
        "options": [
            {"text": "Because water reflects more light than stone does, and "
                     "the brighter a surface is the better an image it "
                     "shows", "correct": False,
             "why": "Water reflects rather little at a steep angle, and how "
                    "MUCH comes back is not what decides whether an image "
                    "forms. What decides it is whether the arrangement of "
                    "the rays survives."},
            {"text": "Because the pavement absorbs the sky's light",
             "correct": False,
             "why": "A pale pavement is bright, so plenty leaves it. What "
                    "leaves is scattered."},
            {"text": "Because the water surface is smooth on the scale of "
                     "light, so the arrangement of the rays survives",
             "correct": True},
            {"text": "Because water bends light and stone does not",
             "correct": False,
             "why": "Water does refract light going into it, and the "
                    "reflection you see is about the surface, not the "
                    "inside."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-02-h01",
        "band": "harder",
        "text": "Two mirrors meet at right angles. A ray hits the first at "
                "30° to its normal. What happens after it reflects off the "
                "second?",
        "options": [
            {"text": "It is absorbed in the corner", "correct": False,
             "why": "Mirrors reflect at both surfaces. Nothing about a "
                    "corner absorbs."},
            {"text": "It leaves at 30° to the first mirror's normal, on the "
                     "same side it arrived", "correct": False,
             "why": "That describes one reflection. After two, the "
                    "direction has been reversed."},
            {"text": "It leaves travelling back parallel to the direction "
                     "it came in on", "correct": True},
            {"text": "It leaves at 60° to its original direction",
             "correct": False,
             "why": "Two mirrors at right angles turn a ray through 180°, "
                    "whatever angle it arrived at. That is what makes a "
                    "corner reflector useful."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h02",
        "band": "harder",
        "text": "A cinema screen is deliberately made matt rather than "
                "glossy. Why?",
        "options": [
            {"text": "Because a matt surface reflects more of the "
                     "projector's light", "correct": False,
             "why": "A glossy screen reflects at least as much. The "
                    "question is where it goes."},
            {"text": "Because a glossy screen would absorb the picture",
             "correct": False,
             "why": "Gloss and absorption are different properties. Black "
                    "gloss absorbs; white gloss does not."},
            {"text": "Because a matt screen refracts the light towards the "
                     "audience, and refraction is what spreads a picture "
                     "out", "correct": False,
             "why": "Nothing is refracted at a screen. The light is "
                    "reflected, and the question is in how many "
                    "directions."},
            {"text": "Because it scatters the light to every seat, while a "
                     "glossy screen would send the beam to one place",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h03",
        "band": "harder",
        "text": "A satellite dish for radio waves can be a metal mesh with "
                "centimetre holes and still work as a mirror. Why does that "
                "not work for light?",
        "options": [
            {"text": "Because a surface acts as a mirror only when it is "
                     "smooth compared with the wavelength, and light's is a "
                     "few ten-thousandths of a millimetre", "correct": True},
            {"text": "Because radio waves are not really reflected — they "
                     "pass through the metal and are given out again on the "
                     "far side, which a mesh does better than a sheet",
             "correct": False,
             "why": "They reflect, at the same law and for the same reason "
                    "light does."},
            {"text": "Because metal reflects radio waves and absorbs light",
             "correct": False,
             "why": "Polished metal is one of the best mirrors there is for "
                    "light. The mesh is what makes the difference."},
            {"text": "Because radio waves travel more slowly, so the holes "
                     "have time to fill", "correct": False,
             "why": "All electromagnetic waves travel at the same speed in "
                    "a vacuum. What differs is the wavelength."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h04",
        "band": "harder",
        "text": "Sitting in a lit room at night, you can see yourself in "
                "the window; from outside, someone sees into the room "
                "instead. Explain what the glass is doing.",
        "options": [
            {"text": "The glass is a mirror on one side only and a plain "
                     "window on the other, which is what one-way glass "
                     "means", "correct": False,
             "why": "Ordinary window glass behaves identically on both "
                    "sides. What differs is how much light is arriving on "
                    "each of them."},
            {"text": "Reflecting a little and letting most through — and "
                     "indoors the little that reflects beats the darkness "
                     "outside", "correct": True},
            {"text": "Absorbing the light that arrives from outside, so "
                     "almost none of it gets into the room",
             "correct": False,
             "why": "Glass absorbs very little; that is what makes it a "
                    "window. If it absorbed the outside light, nobody could "
                    "see out by day either."},
            {"text": "Refracting the room's own light back into the room, "
                     "which is why you appear in the glass",
             "correct": False,
             "why": "Refraction bends light through the glass, it does not "
                    "send it back. What sends it back is reflection at the "
                    "surface."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-02-e05",
        "band": "easier",
        "text": "The angle of incidence is measured from…",
        "options": [            {"text": "the surface of the mirror", "correct": False,
             "why": "Measuring from the mirror gives the complement of the "
                    "angle wanted; the normal is the reference line."},
            {"text": "the reflected ray", "correct": False,
             "why": "The two rays are compared with the normal, not with each "
                    "other."},
            {"text": "the edge of the mirror", "correct": False,
             "why": "Where the mirror ends has nothing to do with the angle "
                    "a ray arrives at."},
            {"text": "the normal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e06",
        "band": "easier",
        "text": "A ray strikes a plane mirror at 50° to the normal. What is "
                "the angle of reflection?",
        "options": [
            {"text": "40°", "correct": False,
             "why": "That is the angle to the mirror SURFACE, not to the "
                    "normal."},
            {"text": "100°", "correct": False,
             "why": "That doubles it; the two angles are equal, not added."},
            {"text": "50°", "correct": True},
            {"text": "0°", "correct": False,
             "why": "A ray reflects straight back only when it arrives along "
                    "the normal."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e07",
        "band": "easier",
        "text": "Reflection from a rough surface, where rays leave in every "
                "direction, is called…",
        "options": [
            {"text": "specular reflection", "correct": False,
             "why": "Specular reflection is what a smooth surface gives, "
                    "keeping parallel rays parallel."},
            {"text": "refraction", "correct": False,
             "why": "Refraction is light bending as it enters a different "
                    "material, not bouncing off one."},
            {"text": "dispersion", "correct": False,
             "why": "Dispersion is a prism fanning colours apart, which is a "
                    "different effect."},
            {"text": "diffuse scattering", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e08",
        "band": "easier",
        "text": "Does a rough surface obey the law of reflection?",
        "options": [
            {"text": "Yes — every tiny facet obeys it, each with its own "
                     "normal",
             "correct": True},
            {"text": "No — rough surfaces break the law", "correct": False,
             "why": "No surface breaks it. What differs is that the facets "
                    "point in many directions."},
            {"text": "Yes, but only for light arriving straight on",
             "correct": False,
             "why": "It holds at every angle, on every facet, however the "
                    "light arrives."},
            {"text": "No — rough surfaces absorb light rather than reflect "
                     "it",
             "correct": False,
             "why": "White paper is rough and reflects most of the light, "
                    "which is why it looks bright."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-02-s05",
        "band": "standard",
        "text": "A ray strikes a plane mirror at 20° to the mirror SURFACE. "
                "What is the angle of reflection?",
        "options": [
            {"text": "20°", "correct": False,
             "why": "That is the angle to the surface. The angle of "
                    "reflection is measured from the normal."},
            {"text": "70°", "correct": True},
            {"text": "40°", "correct": False,
             "why": "That doubles the angle to the surface, which is not what "
                    "the law says."},
            {"text": "160°", "correct": False,
             "why": "That subtracts from 180°, which is not how either angle "
                    "is found."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s06",
        "band": "standard",
        "text": "Why can this page be seen from every seat in a room?",
        "options": [
            {"text": "Because it gives out light of its own", "correct": False,
             "why": "Paper is not a source; in a dark room it cannot be seen "
                    "at all."},
            {"text": "Because it is smooth enough to reflect light straight "
                     "back to each seat",
             "correct": False,
             "why": "A smooth surface sends light one way only, which is why "
                    "a mirror cannot be read from every seat."},
            {"text": "Because its rough surface scatters light in every "
                     "direction",
             "correct": True},
            {"text": "Because white surfaces bend light towards the reader",
             "correct": False,
             "why": "Bending light is refraction, which happens on entering a "
                    "material, not on reflecting from one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s07",
        "band": "standard",
        "text": "A mirror and a sheet of white paper are lit equally. Which "
                "sends back more light altogether?",
        "options": [
            {"text": "The mirror, by a very large margin", "correct": False,
             "why": "Both send back most of what lands on them; the mirror "
                    "sends it all one way instead."},
            {"text": "The paper, because it looks brighter from everywhere",
             "correct": False,
             "why": "It looks bright from everywhere because it spreads the "
                    "light out, not because there is more of it."},
            {"text": "About the same — they differ in which directions it "
                     "goes",
             "correct": True},
            {"text": "Neither — both absorb almost all of it", "correct": False,
             "why": "Both reflect most of it; a surface that absorbed almost "
                    "everything would look black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s08",
        "band": "standard",
        "text": "Why does a polished car bonnet show a reflection while a "
                "matt one does not?",
        "options": [
            {"text": "Because polish makes the surface smooth, so parallel "
                     "rays stay parallel",
             "correct": True},
            {"text": "Because polish makes the paint reflect more light "
                     "altogether",
             "correct": False,
             "why": "Both reflect a similar amount; it is the arrangement of "
                    "the rays that changes."},
            {"text": "Because matt paint absorbs all the light that lands on "
                     "it",
             "correct": False,
             "why": "A matt white bonnet is clearly visible, so it is "
                    "reflecting plenty."},
            {"text": "Because polish bends the light towards the eye",
             "correct": False,
             "why": "Bending on entering a material is refraction, and no "
                    "light enters the paint here."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-02-h05",
        "band": "harder",
        "text": "A ray arrives at a mirror exactly along the normal. What is "
                "the angle of reflection, and where does the ray go?",
        "options": [
            {"text": "90°, and it travels along the mirror surface",
             "correct": False,
             "why": "90° to the normal is along the surface, and no reflected "
                    "ray does that."},
            {"text": "0°, and it goes straight back the way it came",
             "correct": True},
            {"text": "0°, and it passes straight through the mirror",
             "correct": False,
             "why": "The angle is right, but a mirror reflects rather than "
                    "transmits."},
            {"text": "180°, and it is turned right around", "correct": False,
             "why": "The reflected ray does reverse, but the ANGLE from the "
                    "normal is zero."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h06",
        "band": "harder",
        "text": "A mirror is turned through 10° while the incoming ray stays "
                "put. By how much does the reflected ray turn?",
        "options": [
            {"text": "10°, the same as the mirror", "correct": False,
             "why": "Turning the mirror changes the normal by 10°, and both "
                    "angles shift, so the ray turns further."},
            {"text": "5°, half as much as the mirror", "correct": False,
             "why": "The effect is doubled, not halved: both the incidence "
                    "and reflection angles change."},
            {"text": "0°, because the incoming ray has not moved",
             "correct": False,
             "why": "The normal has moved, and the reflected ray is measured "
                    "from the normal."},
            {"text": "20°, twice as much as the mirror", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h07",
        "band": "harder",
        "text": "The Moon gives out no light of its own, yet it is one of the "
                "brightest things in the night sky. Why?",
        "options": [
            {"text": "Because it stores sunlight during the day and releases "
                     "it at night",
             "correct": False,
             "why": "Nothing stores light. What we see is sunlight arriving "
                    "and being scattered at that moment."},
            {"text": "Because it scatters sunlight landing on it back towards "
                     "us",
             "correct": True},
            {"text": "Because it is a smooth mirror reflecting the Sun "
                     "exactly",
             "correct": False,
             "why": "Its surface is rough dust, which is why the whole disc "
                    "is lit rather than one bright dot."},
            {"text": "Because it is much closer than the stars, so its light "
                     "is stronger",
             "correct": False,
             "why": "Being close helps, but the Moon still has to be "
                    "reflecting light rather than making it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h08",
        "band": "harder",
        "text": "A student says only shiny things reflect light. What is the "
                "strongest counter-example?",
        "options": [
            {"text": "A polished mirror, which reflects almost everything",
             "correct": False,
             "why": "That agrees with the student rather than testing them — "
                    "a mirror is shiny."},
            {"text": "A black card, which reflects a small amount",
             "correct": False,
             "why": "It is a fair example, but a weak one: very little comes "
                    "back from it."},
            {"text": "A pane of clear glass, which lets light through",
             "correct": False,
             "why": "Transmission is a different behaviour, so it does not "
                    "settle the question about reflecting."},
            {"text": "A matt white wall, which reflects most of the light",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ───────────────────────────────────────
    {
        "id": "p7-02-e09",
        "band": "easier",
        "text": "What does a plane mirror's image look like, compared with "
                "the object in front of it?",
        "options": [
            {"text": "The same size, and the same way up", "correct": True},
            {"text": "Smaller, and upside down", "correct": False,
             "why": "A plane mirror image is neither shrunk nor flipped "
                    "upside down — only certain curved mirrors do that."},
            {"text": "Larger, and reversed top to bottom", "correct": False,
             "why": "A flat mirror does not magnify or turn an image "
                    "upside down."},
            {"text": "The same size, but always blurred", "correct": False,
             "why": "A flat, clean mirror gives a sharp image, not a "
                    "blurred one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e10",
        "band": "easier",
        "text": "How far behind a plane mirror does your image appear to "
                "be, compared with how far you stand in front of it?",
        "options": [
            {"text": "Exactly twice as far behind as you stand in front",
             "correct": False,
             "why": "The two distances are equal, not doubled — as far "
                    "behind as you are in front."},
            {"text": "Always exactly as far behind as you stand in front",
             "correct": True},
            {"text": "Always exactly one whole metre behind the glass "
                     "surface", "correct": False,
             "why": "The image distance changes with your own distance "
                    "from the mirror; it is not a fixed one metre."},
            {"text": "Half as far behind as you stand in front",
             "correct": False,
             "why": "The distances match exactly; the image is not closer "
                    "to the glass than you are."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e11",
        "band": "easier",
        "text": "A mirror image is called virtual because…",
        "options": [
            {"text": "it fades away if you look at it for too long",
             "correct": False,
             "why": "A mirror image does not fade with time; it stays as "
                    "long as the object and light are there."},
            {"text": "it can only be seen using a computer or a screen",
             "correct": False,
             "why": "You see it with your own eye, directly, with no "
                    "screen or computer involved."},
            {"text": "no light actually comes from behind the mirror",
             "correct": True},
            {"text": "it is not really there at all, in any sense",
             "correct": False,
             "why": "The image is a genuine, well-defined optical effect — "
                    "just one with no light converging at that spot."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e12",
        "band": "easier",
        "text": "Does a plane mirror swap your left and right hand over?",
        "options": [
            {"text": "No — a plane mirror reverses nothing at all",
             "correct": False,
             "why": "One direction genuinely is reversed: the one running "
                    "towards and away from the glass."},
            {"text": "Yes — left and right are always swapped by any "
                     "mirror", "correct": False,
             "why": "It is the near-and-far direction that gets reversed, "
                    "not left and right."},
            {"text": "Yes, but only for very large mirrors",
             "correct": False,
             "why": "The size of the mirror makes no difference to which "
                    "direction gets reversed."},
            {"text": "No — it reverses the direction towards and away "
                     "from the mirror instead", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e13",
        "band": "easier",
        "text": "Why does writing held up to a mirror look backwards?",
        "options": [
            {"text": "Because you had to turn the page round to face the "
                     "glass, and turning it swapped its left and right",
             "correct": True},
            {"text": "Because ink reflects light differently from paper",
             "correct": False,
             "why": "The type of ink makes no difference to which way the "
                    "writing looks."},
            {"text": "Because the mirror scrambles the letters at random",
             "correct": False,
             "why": "Nothing is scrambled — every letter reflects perfectly "
                    "correctly, in its exact place."},
            {"text": "Because mirrors always print text in reverse",
             "correct": False,
             "why": "A mirror does not print or generate any text at all — "
                    "it only reflects the light that reaches it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e14",
        "band": "easier",
        "text": "In a ray diagram, every ray of light should be drawn with…",
        "options": [
            {"text": "a colour matching the surface it lands on",
             "correct": False,
             "why": "The colour of the drawn line is not what a ray diagram "
                    "needs to show — its direction is."},
            {"text": "an arrow showing which way the light is travelling",
             "correct": True},
            {"text": "a curve, since light bends slightly at every "
                     "surface", "correct": False,
             "why": "A ray is drawn as a straight line; light travels in "
                    "straight lines between surfaces."},
            {"text": "a dashed line, to separate it from the normal",
             "correct": False,
             "why": "It is the normal that is drawn as a construction "
                    "line; the ray itself is a solid line with an arrow."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e15",
        "band": "easier",
        "text": "The law of reflection states that…",
        "options": [
            {"text": "the reflected ray always leaves along the surface "
                     "of the mirror", "correct": False,
             "why": "The reflected ray leaves at whatever angle the law "
                    "gives, not always flat along the surface."},
            {"text": "the angle of reflection is always twice the angle "
                     "of incidence", "correct": False,
             "why": "The two angles are equal to each other, not one "
                    "double the other."},
            {"text": "the angle of reflection equals the angle of "
                     "incidence, both measured from the normal",
             "correct": True},
            {"text": "the angle of reflection equals the angle of "
                     "incidence, but from the surface", "correct": False,
             "why": "Both angles are measured from the normal, never from "
                    "the surface itself."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e16",
        "band": "easier",
        "text": "A matt black surface left in strong sunlight tends to feel "
                "warm. Why?",
        "options": [
            {"text": "It generates its own heat by reflecting light",
             "correct": False,
             "why": "Reflecting light does not generate heat; the warmth "
                    "here comes from a different process entirely."},
            {"text": "It reflects sunlight straight back at the Sun",
             "correct": False,
             "why": "A matt surface scatters what little it reflects in "
                    "all directions, not back towards the Sun."},
            {"text": "It scatters all the sunlight landing on it equally",
             "correct": False,
             "why": "A matt black surface absorbs most of the light, "
                    "rather than scattering all of it away again."},
            {"text": "It absorbs most of the sunlight landing on it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e17",
        "band": "easier",
        "text": "Crumpled kitchen foil still reflects most of the light "
                "landing on it, even though it shows no clear image. What "
                "does this tell you?",
        "options": [
            {"text": "That being shiny is not the same as being smooth",
             "correct": True},
            {"text": "That foil is a poor reflector overall",
             "correct": False,
             "why": "Foil reflects almost as much light as a flat mirror "
                    "does; it is a very good reflector."},
            {"text": "That crumpling turns a reflector into an absorber",
             "correct": False,
             "why": "Crumpled foil still sends back nearly all the light; "
                    "it has not started absorbing it instead."},
            {"text": "That only flat surfaces can ever be shiny",
             "correct": False,
             "why": "The crumpled foil itself is the shiny surface here, "
                    "and it is not flat."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e18",
        "band": "easier",
        "text": "A smooth sheet of black glass, like a phone screen, can "
                "still show a faint reflection. What does this show about "
                "smoothness and colour?",
        "options": [
            {"text": "Colour decides whether a surface can show a "
                     "reflection, and black glass is an exception",
             "correct": False,
             "why": "It is smoothness that decides whether a pattern "
                    "survives, whatever colour the surface is."},
            {"text": "Smoothness, never colour, decides whether a "
                     "pattern of light survives as an image",
             "correct": True},
            {"text": "Black surfaces always reflect more light than "
                     "lighter-coloured ones", "correct": False,
             "why": "A dark surface generally reflects LESS light overall "
                    "than a pale one — colour affects the amount, not "
                    "whether an image forms."},
            {"text": "Glass can only ever show a reflection if it is "
                     "perfectly clear", "correct": False,
             "why": "The glass here is black and opaque, not clear, and "
                    "still shows a faint reflection."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e19",
        "band": "easier",
        "text": "Light that is neither reflected nor scattered by a surface "
                "has been…",
        "options": [
            {"text": "converted into sound", "correct": False,
             "why": "Light and sound do not turn into one another at a "
                    "surface."},
            {"text": "refracted through the surface", "correct": False,
             "why": "Refraction is bending light on entering a new "
                    "material, a different process from what happens at "
                    "an opaque surface."},
            {"text": "absorbed", "correct": True},
            {"text": "sent back out invisibly", "correct": False,
             "why": "Light that is absorbed does not leave the surface "
                    "again at all, visibly or otherwise."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e20",
        "band": "easier",
        "text": "The normal in a ray diagram is drawn at what angle to the "
                "surface?",
        "options": [
            {"text": "45°", "correct": False,
             "why": "That is a common angle for a RAY to arrive at, but "
                    "not the angle the normal itself makes with the "
                    "surface."},
            {"text": "0°, lying flat along the surface", "correct": False,
             "why": "A line lying flat along the surface would not be at "
                    "right angles to it, which is what a normal must be."},
            {"text": "180°", "correct": False,
             "why": "That would point back along the surface the other "
                    "way, still not at right angles to it."},
            {"text": "90°", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e21",
        "band": "easier",
        "text": "Is the normal in a ray diagram a real ray of light?",
        "options": [
            {"text": "No — it is a construction line, drawn to measure "
                     "angles from", "correct": True},
            {"text": "Yes — it is the ray that arrives exactly straight "
                     "on", "correct": False,
             "why": "The normal is drawn at every point, whatever angle "
                    "the real ray arrives at — it is not itself a ray."},
            {"text": "Yes — it is the reflected ray, drawn dashed",
             "correct": False,
             "why": "The reflected ray is real light, drawn as a solid "
                    "line with its own arrow; the normal is a separate, "
                    "dashed construction line."},
            {"text": "No — it only appears in diagrams of curved mirrors",
             "correct": False,
             "why": "A normal is drawn at a flat mirror too, at the exact "
                    "point where the ray lands."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e22",
        "band": "easier",
        "text": "Is moonlight light that the Moon makes for itself?",
        "options": [
            {"text": "Yes — the Moon glows faintly on its own, like a very "
                     "dim lamp", "correct": False,
             "why": "The Moon has no light source of its own; every bit of "
                    "moonlight started out as sunlight."},
            {"text": "No — it is sunlight that the Moon's surface "
                     "scatters back towards us", "correct": True},
            {"text": "Yes — it stores up sunlight during the day and "
                     "releases it at night", "correct": False,
             "why": "Nothing is stored. What we see is sunlight being "
                    "scattered at that very moment."},
            {"text": "No — it is starlight bouncing off the Moon, not "
                     "sunlight", "correct": False,
             "why": "The Sun is what lights the Moon; starlight is far too "
                    "faint to explain how bright the Moon looks."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e23",
        "band": "easier",
        "text": "The angle between an incoming beam and the normal of a "
                "flat mirror it strikes is 60°. What angle does the "
                "reflected beam make with that normal?",
        "options": [
            {"text": "30°", "correct": False,
             "why": "That is the angle to the mirror surface, not to the "
                    "normal."},
            {"text": "0°", "correct": False,
             "why": "A ray reflects straight back only if it arrives "
                    "exactly along the normal."},
            {"text": "60°", "correct": True},
            {"text": "120°", "correct": False,
             "why": "That doubles the given angle, which is not what the "
                    "law of reflection says."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e24",
        "band": "easier",
        "text": "Looking at a flat mirror, a beam makes an angle of 10° "
                "with the mirror's own surface. Work out the angle of "
                "incidence.",
        "options": [
            {"text": "10°", "correct": False,
             "why": "That is the angle to the surface, not to the normal, "
                    "which is what the angle of incidence is measured "
                    "from."},
            {"text": "100°", "correct": False,
             "why": "That adds the 10° to the 90° of the normal instead "
                    "of taking it away."},
            {"text": "20°", "correct": False,
             "why": "That doubles the given angle rather than subtracting "
                    "it from 90°."},
            {"text": "80°", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e25",
        "band": "easier",
        "text": "A ray arrives at a mirror exactly along the normal, at 0° "
                "to it. Where does the reflected ray go?",
        "options": [
            {"text": "Straight back the way it came", "correct": True},
            {"text": "Along the surface of the mirror", "correct": False,
             "why": "A ray only travels along the surface if it arrives "
                    "at 90° to the normal, not 0°."},
            {"text": "It cannot reflect at all from that angle",
             "correct": False,
             "why": "Every angle of incidence, including 0°, gives a "
                    "well-defined reflected ray."},
            {"text": "In a random direction, since there is no clear "
                     "angle to measure", "correct": False,
             "why": "The angle is perfectly well defined — 0° from the "
                    "normal — and the reflected ray follows the law "
                    "exactly, like any other."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e26",
        "band": "easier",
        "text": "Do mirrors create their own light?",
        "options": [
            {"text": "Yes — that is why a room looks brighter with a "
                     "mirror in it than without one", "correct": False,
             "why": "A mirror redirects existing light rather than adding "
                    "any new light of its own to the room."},
            {"text": "No — they only redirect light that is already "
                     "arriving on them", "correct": True},
            {"text": "Yes, but only very dim, silvery light",
             "correct": False,
             "why": "A mirror gives out no light at all by itself; every "
                    "bit you see reflected in it came from somewhere "
                    "else first."},
            {"text": "No — and a mirror in a completely dark room shows a "
                     "faint reflection anyway", "correct": False,
             "why": "With no light arriving on it at all, a mirror in a "
                    "totally dark room shows nothing whatsoever."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e27",
        "band": "easier",
        "text": "White paper reflects most of the light landing on it, yet "
                "shows no image of anything. Why not?",
        "options": [
            {"text": "Because it does not really reflect the light at all",
             "correct": False,
             "why": "It does reflect most of the light — that is exactly "
                    "why it looks bright."},
            {"text": "Because paper absorbs almost everything that lands "
                     "on it", "correct": False,
             "why": "White paper absorbs very little; that is why it "
                    "looks so bright rather than dark."},
            {"text": "Because its rough surface always scatters the light "
                     "in all directions, destroying the pattern",
             "correct": True},
            {"text": "Because paper is simply not shiny enough to ever "
                     "form any kind of visible reflection whatsoever",
             "correct": False,
             "why": "How much comes back is not the issue here — the "
                    "issue is whether the pattern of the rays survives."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e28",
        "band": "easier",
        "text": "Specular reflection happens at ___ surfaces, and diffuse "
                "scattering happens at ___ surfaces.",
        "options": [
            {"text": "rough … smooth", "correct": False,
             "why": "The pairing here is the wrong way round."},
            {"text": "bright … dark", "correct": False,
             "why": "Brightness is about how much light a surface sends "
                    "back, not about whether it is smooth or rough."},
            {"text": "shiny … dull", "correct": False,
             "why": "Shiny and dull describe how much light comes back, "
                    "not whether the surface is smooth or rough."},
            {"text": "smooth … rough", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e29",
        "band": "easier",
        "text": "Does the size of a plane mirror's image change depending "
                "on how far away you stand from the mirror?",
        "options": [
            {"text": "No — it stays the same size as you, wherever you "
                     "stand", "correct": True},
            {"text": "Yes — the image gets bigger the further you stand "
                     "away", "correct": False,
             "why": "The image stays exactly your own size, however far "
                    "you stand back."},
            {"text": "Yes — the image gets smaller the closer you stand",
             "correct": False,
             "why": "Standing closer does not shrink the image; it "
                    "remains the same size as you."},
            {"text": "It depends on how bright the room is",
             "correct": False,
             "why": "Brightness changes how easily you can see the "
                    "image, not the size the mirror makes it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-e30",
        "band": "easier",
        "text": "Which pair of surfaces reflects a broadly similar total "
                "amount of light, despite looking very different?",
        "options": [
            {"text": "A mirror and a sheet of matt black card",
             "correct": False,
             "why": "These two differ hugely in how much light they send "
                    "back — the mirror reflects far more."},
            {"text": "A mirror and a sheet of white paper", "correct": True},
            {"text": "White paper and matt black card", "correct": False,
             "why": "White paper reflects most of the light landing on "
                    "it; black card absorbs most of it — these differ "
                    "greatly."},
            {"text": "Matt black card and crumpled foil", "correct": False,
             "why": "Foil reflects almost all the light landing on it; "
                    "black card absorbs almost all of it — a huge "
                    "difference."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p7-02-s09",
        "band": "standard",
        "text": "A beam meets a flat mirror, making an angle of 28° with "
                "the surface of the mirror itself. What is the angle "
                "between the incoming beam and the reflected beam?",
        "options": [
            {"text": "124°", "correct": True},
            {"text": "62°", "correct": False,
             "why": "That is the angle of incidence, found correctly from "
                    "90° − 28°, but the two rays sit one on each side of "
                    "the normal, so the angle between them is twice it."},
            {"text": "56°", "correct": False,
             "why": "That doubles the 28° given to the surface, without "
                    "first converting it to an angle from the normal."},
            {"text": "28°", "correct": False,
             "why": "That is the angle to the mirror surface itself, "
                    "which is neither ray's angle from the normal nor the "
                    "angle between the two rays."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s10",
        "band": "standard",
        "text": "A ray strikes a mirror at 55° to the normal. What is the "
                "angle between the incoming ray and the reflected ray?",
        "options": [
            {"text": "55°", "correct": False,
             "why": "That is the angle each ray makes with the normal, "
                    "not the angle between the two rays themselves."},
            {"text": "110°", "correct": True},
            {"text": "35°", "correct": False,
             "why": "That is 90° minus 55°, the angle to the mirror "
                    "surface — not the angle between the two rays."},
            {"text": "180°", "correct": False,
             "why": "That would mean the reflected ray goes straight back "
                    "the way it came, which only happens at 0° incidence."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s11",
        "band": "standard",
        "text": "Two mirrors are set up facing each other, parallel and a "
                "few centimetres apart. What do you see looking into one "
                "of them?",
        "options": [
            {"text": "A single, ordinary reflection of yourself, exactly "
                     "as with one mirror", "correct": False,
             "why": "The second mirror reflects the first mirror's image "
                    "too, producing far more than a single reflection."},
            {"text": "Nothing at all, since the two mirrors cancel each "
                     "other out", "correct": False,
             "why": "Mirrors do not cancel one another; light keeps "
                    "bouncing between them instead."},
            {"text": "A repeating series of reflections, trailing off "
                     "into the distance", "correct": True},
            {"text": "A single image, but coloured differently from the "
                     "real object", "correct": False,
             "why": "Reflection does not change colour; what multiplies "
                    "here is the number of images, not their colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s12",
        "band": "standard",
        "text": "Standing 2 m away from a flat mirror, how large is the "
                "total gap between you and your reflection?",
        "options": [
            {"text": "2 m", "correct": False,
             "why": "That is only your distance to the glass; the image "
                    "sits a further 2 m beyond that."},
            {"text": "8 m", "correct": False,
             "why": "That is twice too far — the image is only as far "
                    "behind the glass as you are in front of it."},
            {"text": "1 m", "correct": False,
             "why": "That halves the true separation rather than doubling "
                    "your distance to the mirror."},
            {"text": "4 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s13",
        "band": "standard",
        "text": "You are standing in front of a mirror and step 1 m closer "
                "to it. How does the distance between you and your image "
                "change?",
        "options": [
            {"text": "It decreases by 2 m", "correct": True},
            {"text": "It only decreases by 1 m", "correct": False,
             "why": "Both your distance to the mirror AND the image's "
                    "distance behind it shrink by 1 m each, so the total "
                    "change is more than 1 m."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Moving closer to the mirror always brings your image "
                    "closer to you too."},
            {"text": "It increases by 2 m", "correct": False,
             "why": "Stepping closer to the mirror brings the image "
                    "closer, not further away."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s14",
        "band": "standard",
        "text": "At night, a greenhouse window shows a faint reflection of "
                "the room as well as letting the plants be seen from "
                "outside. What is happening at the glass?",
        "options": [
            {"text": "The glass is switching between reflecting and "
                     "letting light through, moment by moment",
             "correct": False,
             "why": "Both happen continuously and at the same time, not "
                    "by switching back and forth."},
            {"text": "The glass is reflecting a little light and letting "
                     "most of it through, both at once", "correct": True},
            {"text": "The glass only reflects on the inside face and only "
                     "transmits on the outside face", "correct": False,
             "why": "Ordinary glass behaves the same on both faces; it "
                    "reflects and transmits at both surfaces alike."},
            {"text": "The glass is absorbing the room's light and giving "
                     "it back out as a reflection", "correct": False,
             "why": "Glass absorbs very little light; the faint image "
                    "comes from a small amount being reflected, not "
                    "absorbed and reissued."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s15",
        "band": "standard",
        "text": "A matt black wall and a mirror both face the same lamp for "
                "an hour. Which gets noticeably warmer, and why?",
        "options": [
            {"text": "The mirror, because it reflects the most light and "
                     "so absorbs the most energy", "correct": False,
             "why": "Reflecting light is the opposite of absorbing it; a "
                    "surface that reflects almost everything absorbs "
                    "almost nothing."},
            {"text": "Neither — absorbing light never produces any "
                     "warming at all", "correct": False,
             "why": "Absorbed light energy does warm a surface; that is "
                    "exactly why the matt black wall heats up."},
            {"text": "The black wall, because it absorbs most of the "
                     "light landing on it", "correct": True},
            {"text": "Both equally, since they receive the same amount "
                     "of light from the lamp", "correct": False,
             "why": "Receiving the same light is not the same as "
                    "absorbing the same amount — one surface reflects "
                    "most of it away."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s16",
        "band": "standard",
        "text": "A whiteboard can be read from almost any seat in a room, "
                "but a mirror hung in the same spot could only be read "
                "from one narrow position. Why the difference?",
        "options": [
            {"text": "Writing behaves differently on a rough surface than "
                     "it does on a smooth one", "correct": False,
             "why": "The writing itself is unaffected either way; it is "
                    "how the surface scatters or redirects the light that "
                    "differs."},
            {"text": "The whiteboard is much brighter overall than any "
                     "mirror could be", "correct": False,
             "why": "A mirror can reflect just as much light overall; "
                    "the difference is in the directions it goes, not "
                    "the total amount."},
            {"text": "A mirror image can be read by only one specific "
                     "person standing in exactly the right spot at any "
                     "moment, according to a strict rule of optics",
             "correct": False,
             "why": "Several people standing in the mirror's one "
                    "reflected direction at once could all read it; there "
                    "is no such rule."},
            {"text": "The whiteboard's rough surface scatters light to "
                     "every seat; the mirror sends it in one specific "
                     "direction only", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s17",
        "band": "standard",
        "text": "Why do interior designers sometimes hang a large mirror "
                "on the wall of a small room?",
        "options": [
            {"text": "The mirror's virtual image extends the apparent "
                     "space behind the wall, making the room look bigger",
             "correct": True},
            {"text": "The mirror physically pushes the wall backwards, "
                     "which increases the floor area", "correct": False,
             "why": "Nothing about the wall's real position changes; "
                    "only the appearance of the space does."},
            {"text": "The mirror doubles the amount of furniture that "
                     "will fit in the room", "correct": False,
             "why": "The real floor area for furniture is unchanged; "
                    "only what the room looks like from the eye changes."},
            {"text": "The mirror removes the need for a light source in "
                     "the room", "correct": False,
             "why": "A mirror only redirects existing light; the room "
                    "still needs a real light source."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s18",
        "band": "standard",
        "text": "A driver adjusts a flat wing mirror, turning it by 5°. By "
                "how much does the direction of the reflected view "
                "change?",
        "options": [
            {"text": "5°, the same as the mirror", "correct": False,
             "why": "Turning the mirror changes the normal by 5°, and "
                    "both the incidence and reflection angles shift, so "
                    "the reflected direction turns further than that."},
            {"text": "10°, twice as much as the mirror", "correct": True},
            {"text": "2.5°, half as much as the mirror", "correct": False,
             "why": "The effect is doubled rather than halved: the "
                    "reflected direction turns by twice the mirror's own "
                    "rotation."},
            {"text": "0°, because the car itself has not moved",
             "correct": False,
             "why": "The mirror's own rotation is what matters here, not "
                    "whether the car has moved."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s19",
        "band": "standard",
        "text": "For a school demonstration needing the best possible "
                "mirror, which of these would work least well: polished "
                "steel, white paper, or crumpled foil?",
        "options": [
            {"text": "Polished steel", "correct": False,
             "why": "Polished steel is both shiny and smooth, which makes "
                    "it an excellent mirror."},
            {"text": "Crumpled foil", "correct": False,
             "why": "Foil reflects a great deal of light, though its "
                    "crumpling stops it forming a clear image either."},
            {"text": "White paper", "correct": True},
            {"text": "All three would work equally well as a mirror",
             "correct": False,
             "why": "Only the smooth, shiny surface — polished steel — "
                    "shows a genuine image; the others do not."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s20",
        "band": "standard",
        "text": "A photograph is printed once on matt paper and once on "
                "glossy paper. Tilted under a lamp, which shows a "
                "reflection of the lamp itself?",
        "options": [
            {"text": "The matt print, because matt paper reflects more "
                     "light overall", "correct": False,
             "why": "Matt and glossy paper reflect broadly similar "
                    "amounts of light; the difference is in how smooth "
                    "the surface is, not how much bounces off."},
            {"text": "Neither — printed photographs of any kind can "
                     "never show a reflection of anything nearby",
             "correct": False,
             "why": "A sufficiently smooth, glossy surface can and does "
                    "show a reflection, just as a mirror does."},
            {"text": "Both equally, since they show the same photograph",
             "correct": False,
             "why": "What the photograph shows is irrelevant here — it "
                    "is the surface finish, matt or glossy, that decides "
                    "whether a reflection forms."},
            {"text": "The glossy print, because its smoother surface "
                     "keeps the pattern of the light together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s21",
        "band": "standard",
        "text": "A ray starts by hitting a mirror exactly along the normal, "
                "at 0°. The mirror is then tilted by 15°, with the ray "
                "kept fixed. What is the new angle of incidence?",
        "options": [
            {"text": "15°", "correct": True},
            {"text": "0°, unchanged", "correct": False,
             "why": "Tilting the mirror changes the direction of its "
                    "normal, so the angle between the fixed ray and the "
                    "new normal is no longer zero."},
            {"text": "30°, twice the tilt", "correct": False,
             "why": "The angle of INCIDENCE changes by exactly the "
                    "mirror's own tilt; it is the REFLECTED ray's "
                    "direction that turns by twice as much."},
            {"text": "75°", "correct": False,
             "why": "That subtracts the tilt from 90° instead of simply "
                    "taking the new angle as the tilt itself."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s22",
        "band": "standard",
        "text": "Which of these is the odd one out for showing a clear "
                "image of what is in front of it: a still pond, a window "
                "at a shallow angle, polished chrome, or frosted glass?",
        "options": [
            {"text": "A still pond", "correct": False,
             "why": "Still water is smooth on the scale of light and "
                    "shows a clear reflection."},
            {"text": "Frosted glass", "correct": True},
            {"text": "Polished chrome", "correct": False,
             "why": "Polished chrome is both shiny and smooth, giving one "
                    "of the clearest reflections there is."},
            {"text": "A window at a shallow angle", "correct": False,
             "why": "Ordinary window glass is smooth, and at a shallow "
                    "angle it reflects a visible image alongside letting "
                    "light through."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s23",
        "band": "standard",
        "text": "A room has a lamp and a large mirror on one wall. Does "
                "the mirror make the room brighter overall, or simply "
                "redirect the light that is already there?",
        "options": [
            {"text": "It makes the room noticeably brighter overall, "
                     "since mirrors genuinely add extra light of their "
                     "own", "correct": False,
             "why": "A mirror produces no light of its own; it only "
                    "redirects light that the lamp already provides."},
            {"text": "It makes the room dimmer overall, by absorbing "
                     "some of the lamp's light", "correct": False,
             "why": "A mirror reflects almost all the light landing on "
                    "it, absorbing very little."},
            {"text": "It only redirects the existing light, rather than "
                     "adding any new light to the room", "correct": True},
            {"text": "It has no effect on the light in the room at all",
             "correct": False,
             "why": "The mirror does change where the light goes, sending "
                    "some of it in a new direction — it simply adds no "
                    "extra light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s24",
        "band": "standard",
        "text": "Identical torches shine on a white wall and on a mirror "
                "from the same distance. To someone standing well to the "
                "side, not directly in the mirror's reflected beam, which "
                "patch looks brighter?",
        "options": [
            {"text": "The mirror's patch, since a mirror always reflects "
                     "more light than a wall", "correct": False,
             "why": "A mirror can reflect a similar or greater fraction "
                    "of the light, but nearly all of it goes in ONE "
                    "direction that misses a side-on viewer."},
            {"text": "Neither is visible at all from the side",
             "correct": False,
             "why": "The scattered light from the wall does reach a "
                    "side-on viewer, so that patch remains clearly "
                    "visible."},
            {"text": "Both look equally bright to the side-on viewer",
             "correct": False,
             "why": "The wall scatters light to the side; the mirror "
                    "sends almost none of its reflected light that way, "
                    "so the two do not look equally bright."},
            {"text": "The white wall's patch", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s25",
        "band": "standard",
        "text": "The angle between an incident ray and its reflected ray "
                "is measured as 80°. What is the angle of incidence?",
        "options": [
            {"text": "40°", "correct": True},
            {"text": "80°", "correct": False,
             "why": "That is the angle between the two rays, not the "
                    "angle either one makes with the normal."},
            {"text": "160°", "correct": False,
             "why": "That doubles the angle between the rays instead of "
                    "halving it."},
            {"text": "10°", "correct": False,
             "why": "That divides 80° by eight rather than by two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s26",
        "band": "standard",
        "text": "A mirror is angled so that a horizontal laser beam is "
                "reflected to travel straight downward — a 90° turn. What "
                "is the angle of incidence on the mirror?",
        "options": [
            {"text": "90°", "correct": False,
             "why": "A ray at 90° to the normal would travel along the "
                    "mirror surface, not turn through a clean right angle."},
            {"text": "45°", "correct": True},
            {"text": "0°", "correct": False,
             "why": "A ray along the normal reflects straight back the "
                    "way it came, giving no turn at all, let alone a "
                    "right angle."},
            {"text": "180°", "correct": False,
             "why": "An angle of incidence cannot exceed 90°, since "
                    "beyond that it would no longer be striking the "
                    "front of the mirror."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s27",
        "band": "standard",
        "text": "A student polishes a piece of black card until it looks "
                "glossy. Does this make the card reflect noticeably more "
                "light overall, or mainly change HOW it reflects?",
        "options": [
            {"text": "It reflects noticeably more light overall, since "
                     "polishing always increases reflectivity a great "
                     "deal", "correct": False,
             "why": "The black pigment still absorbs most of the light "
                    "regardless of polish; the total reflected barely "
                    "changes."},
            {"text": "Polishing has no effect on black card of any kind",
             "correct": False,
             "why": "Polishing does change something: the small fraction "
                    "of light it does reflect now keeps its pattern, "
                    "giving a faint glossy sheen."},
            {"text": "It mainly changes HOW the card reflects — towards "
                     "specular rather than diffuse — while still "
                     "absorbing most of the light", "correct": True},
            {"text": "It turns the card into an absorber that reflects "
                     "nothing whatsoever", "correct": False,
             "why": "A polished black surface still reflects a small but "
                    "real fraction of the light, enough to show a dim "
                    "reflection."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s28",
        "band": "standard",
        "text": "A ray reflects off two mirrors set exactly at right "
                "angles to each other, striking the first at 50° to its "
                "normal. At what angle does it strike the SECOND mirror, "
                "measured from that mirror's own normal?",
        "options": [
            {"text": "50°", "correct": False,
             "why": "The two mirrors are at right angles to each other, "
                    "so the angle at the second mirror is not simply the "
                    "same as at the first."},
            {"text": "90°", "correct": False,
             "why": "A ray striking at 90° to a normal would be running "
                    "along that mirror's surface, not landing on it at a "
                    "real angle."},
            {"text": "140°", "correct": False,
             "why": "That adds the two figures together rather than "
                    "using the right-angle relationship between the two "
                    "mirrors."},
            {"text": "40°", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s29",
        "band": "standard",
        "text": "A cyclist's rear reflector is built from many tiny flat "
                "mirrors set in groups of three, each group meeting at "
                "right angles. Why does this help a driver see it, from "
                "wherever the car happens to be on the road?",
        "options": [
            {"text": "Because mirrors meeting at right angles return a "
                     "ray along its own incoming path, so each driver's "
                     "own headlights come back to that driver",
             "correct": True},
            {"text": "Because a great many tiny mirrors absorb far less "
                     "of the headlight beam than one large flat mirror "
                     "of the same area would", "correct": False,
             "why": "Absorption is not what the right-angled groups "
                    "change; the direction the light is sent back in is."},
            {"text": "Because a reflector built from tiny mirrors stores "
                     "light during the day and glows on its own at night",
             "correct": False,
             "why": "A reflector stores nothing and makes no light of its "
                    "own; every bit you see came from a headlight a "
                    "moment earlier."},
            {"text": "Because the tiny mirrors are set at random angles, "
                     "so they scatter the beam thinly in every direction "
                     "at once, as a rough surface does", "correct": False,
             "why": "Random angles would spread the beam thinly and waste "
                    "most of it; the groups are set at right angles on "
                    "purpose, to send it back concentrated."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-s30",
        "band": "standard",
        "text": "Which would send at least some reflected light to almost "
                "every direction, including to a pedestrian standing well "
                "to the side: a car's chrome wing mirror, or its matt "
                "dashboard shelf?",
        "options": [
            {"text": "The chrome wing mirror, since it reflects far more "
                     "light overall", "correct": False,
             "why": "The mirror reflects a great deal of light, but "
                    "nearly all of it goes in one specific direction, "
                    "not to every position around it."},
            {"text": "The matt dashboard shelf", "correct": True},
            {"text": "Neither — both send reflected light in only one "
                     "fixed direction", "correct": False,
             "why": "A rough, matt surface scatters its reflected light "
                    "in many directions at once, unlike a smooth mirror."},
            {"text": "Both equally, since they are lit by the same "
                     "sunlight", "correct": False,
             "why": "Being lit the same way does not mean they send the "
                    "reflected light the same way; one scatters it "
                    "widely and the other does not."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "p7-02-h09",
        "band": "harder",
        "text": "A periscope uses two flat mirrors, both at 45°, one above "
                "the other and parallel to each other. Why does the final "
                "view come out travelling in the same direction as it "
                "went in, rather than turned around?",
        "options": [
            {"text": "Because the two 45° reflections turn the ray by 90° "
                     "in opposite senses, so the net turn cancels out",
             "correct": True},
            {"text": "Because two reflections always cancel each other "
                     "out completely, whatever the angles involved",
             "correct": False,
             "why": "That is only true for this particular parallel "
                    "arrangement — a corner reflector, for instance, "
                    "reverses the ray instead."},
            {"text": "Because the second mirror refracts the light back "
                     "the other way", "correct": False,
             "why": "Both surfaces in a periscope are mirrors, working "
                    "purely by reflection; no refraction is involved."},
            {"text": "Because light naturally straightens itself out "
                     "again after two bounces", "correct": False,
             "why": "Nothing about light 'straightens itself'; the "
                    "outcome follows directly from the geometry of the "
                    "two 45° reflections."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h10",
        "band": "harder",
        "text": "Two mirrors meeting at exactly 90° return a ray along "
                "its own incoming path, whatever angle it arrives at. "
                "Does this still hold if the two mirrors instead meet at "
                "80°?",
        "options": [
            {"text": "Yes — any two flat mirrors will always reverse a "
                     "ray completely, regardless of the angle set "
                     "between them", "correct": False,
             "why": "Returning the ray along its own path is a special "
                    "result that depends on the mirrors meeting at "
                    "exactly 90°."},
            {"text": "No — at 80° the ray is still turned through a "
                     "fixed amount, but not the full half-turn needed to "
                     "send it back along its own path", "correct": True},
            {"text": "No — at any angle other than 90° the light is "
                     "absorbed rather than reflected", "correct": False,
             "why": "Each mirror still reflects the ray perfectly well at "
                    "80°; what changes is the overall outgoing direction, "
                    "not whether reflection happens at all."},
            {"text": "Yes, but only for rays that arrive along the "
                     "normal of the first mirror", "correct": False,
             "why": "The 90° reversal result holds for EVERY incoming "
                    "angle, not just one particular one — that is what "
                    "makes it special."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h11",
        "band": "harder",
        "text": "A ray hits a mirror at 20° to the normal. The mirror is "
                "then rotated by 10° so as to INCREASE the angle of "
                "incidence. What is the new angle of reflection, and by "
                "how much has the reflected ray itself turned from its "
                "original direction?",
        "options": [
            {"text": "New angle 10°; the reflected ray has turned by 20°",
             "correct": False,
             "why": "Rotating the mirror to INCREASE the incidence angle "
                    "raises it above 20°, not below it."},
            {"text": "New angle 30°; the reflected ray has turned by 10°",
             "correct": False,
             "why": "The angle of incidence does change by the mirror's "
                    "own 10° rotation, but the REFLECTED ray's direction "
                    "turns by twice that amount."},
            {"text": "New angle 30°; the reflected ray has turned by 20°",
             "correct": True},
            {"text": "New angle 20°, unchanged; the reflected ray has "
                     "turned by 10°", "correct": False,
             "why": "Rotating the mirror changes the direction of its "
                    "normal, which does change the angle of incidence — "
                    "it cannot stay at 20°."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h12",
        "band": "harder",
        "text": "A student claims that since crumpled foil reflects about "
                "88% of the light landing on it, almost as much as a 95% "
                "mirror, it should show an image nearly as good as a "
                "mirror's. Evaluate this claim.",
        "options": [
            {"text": "The claim is right, since the two percentages are "
                     "so close together", "correct": False,
             "why": "Whether an image forms depends on smoothness, not "
                    "on how much light comes back — and foil is far less "
                    "smooth than a flat mirror."},
            {"text": "The claim is right, but only because foil is a "
                     "metal and mirrors usually are too", "correct": False,
             "why": "What a mirror is made of is not the deciding factor "
                    "— its flat, smooth shape is."},
            {"text": "The claim is wrong, because crumpled foil in "
                     "practice actually reflects far less than the "
                     "stated 88% once it has been crumpled up tightly",
             "correct": False,
             "why": "The 88% figure for crumpled foil is correct; the "
                    "flaw in the claim lies elsewhere."},
            {"text": "The claim is wrong: forming an image depends on "
                     "smoothness, and crumpled foil is shiny but not "
                     "smooth, however much light it reflects",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h13",
        "band": "harder",
        "text": "To show that 'how much light comes back' and 'whether an "
                "image forms' are independent properties, which "
                "comparison makes the point better: mirror versus matt "
                "black card, or mirror versus crumpled foil?",
        "options": [
            {"text": "Mirror versus crumpled foil, since they reflect a "
                     "similar amount of light yet differ hugely in image "
                     "quality", "correct": True},
            {"text": "Mirror versus matt black card, since they differ "
                     "the most overall", "correct": False,
             "why": "That pair differs in BOTH properties at once — "
                    "amount reflected and image quality — so it cannot "
                    "show the two are independent of each other."},
            {"text": "Neither comparison can show anything about these "
                     "two properties", "correct": False,
             "why": "The mirror-versus-foil comparison genuinely isolates "
                    "image quality while holding the reflected amount "
                    "roughly constant."},
            {"text": "Mirror versus matt black card, because both are "
                     "smooth surfaces", "correct": False,
             "why": "Matt black card is rough, not smooth — that is "
                    "exactly why it shows no image, on top of absorbing "
                    "most of the light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h14",
        "band": "harder",
        "text": "A ray reflects off two mirrors in sequence, each of which "
                "reflects 95% of the light landing on it. Roughly what "
                "percentage of the original light remains after both "
                "reflections?",
        "options": [
            {"text": "About 95%", "correct": False,
             "why": "That ignores the second reflection's own loss "
                    "entirely, as if only one mirror were involved."},
            {"text": "About 90%", "correct": True},
            {"text": "About 190%, since the two 95% figures are added "
                     "together", "correct": False,
             "why": "Percentages of the remaining light are multiplied "
                    "together here, not added — you cannot end up with "
                    "more light than you started with."},
            {"text": "About 45%, since only half the light gets through "
                     "two reflections", "correct": False,
             "why": "That treats each mirror as if it lost half the "
                    "light, when in fact each one keeps 95% of what it "
                    "receives."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h15",
        "band": "harder",
        "text": "A textbook diagram deliberately exaggerates how rough a "
                "sheet of paper's surface looks, to make the scattering "
                "of light easier to see. Does exaggerating the drawn "
                "roughness change the underlying science being shown?",
        "options": [
            {"text": "Yes — an exaggerated diagram means the law of "
                     "reflection no longer applies at each facet",
             "correct": False,
             "why": "The law of reflection applies at every facet "
                    "regardless of how large or small it is drawn."},
            {"text": "Yes — a more exaggerated drawing means the paper "
                     "itself scatters light more strongly in reality",
             "correct": False,
             "why": "How the paper is drawn has no effect on the real "
                    "paper's own properties, whatever the diagram looks "
                    "like."},
            {"text": "No — each drawn facet still obeys the same law of "
                     "reflection; the exaggeration is only for clarity",
             "correct": True},
            {"text": "It is impossible to know without measuring the "
                     "real paper directly", "correct": False,
             "why": "The underlying law being illustrated does not "
                    "depend on the scale of the drawing at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h16",
        "band": "harder",
        "text": "A light meter held exactly where a mirror's reflected "
                "beam is aimed reads far higher than one held at the same "
                "spot facing a sheet of white paper instead. Does this "
                "show the mirror reflects more light overall than the "
                "paper?",
        "options": [
            {"text": "Yes — a higher single reading always means more "
                     "total light is being reflected", "correct": False,
             "why": "A single-spot reading tells you about that one "
                    "direction only, not the total light reflected in "
                    "every direction."},
            {"text": "Yes, because paper always reflects far less total "
                     "light than any mirror does", "correct": False,
             "why": "White paper and a mirror reflect broadly similar "
                    "TOTAL amounts of light; they differ chiefly in "
                    "which directions it goes."},
            {"text": "It cannot show anything useful at all, since "
                     "ordinary light meters are simply not designed to "
                     "compare a mirror directly with a sheet of paper in "
                     "this particular kind of experiment", "correct": False,
             "why": "A light meter can compare readings perfectly well — "
                    "the issue is what a SINGLE reading is able to tell "
                    "you, not the instrument itself."},
            {"text": "No — the mirror concentrates a similar total amount "
                     "of light into only one direction, while the paper "
                     "spreads a similar total over every direction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h17",
        "band": "harder",
        "text": "A student says a mirror image being 'virtual' makes it "
                "somehow less real or less useful than an image cast onto "
                "a screen. Evaluate this using what virtual actually "
                "means.",
        "options": [
            {"text": "The student is wrong — 'virtual' only means no "
                     "light actually converges at that point, not that "
                     "the image is any less real or useful", "correct": True},
            {"text": "The student is right — a virtual image is only a "
                     "trick of the eye and has no genuine optical "
                     "existence of its own, however carefully you look "
                     "for it", "correct": False,
             "why": "A virtual image is a completely real, well-defined "
                    "optical effect, precisely predictable from the law "
                    "of reflection — not merely a trick."},
            {"text": "The student is right, because a virtual image "
                     "cannot be photographed by a camera", "correct": False,
             "why": "A camera can photograph a virtual image perfectly "
                    "well — a photo of yourself in a mirror is a common "
                    "example."},
            {"text": "The student is wrong, because a virtual image is "
                     "actually brighter than one cast onto a screen",
             "correct": False,
             "why": "Brightness is not what the word 'virtual' refers to "
                    "at all — it is about whether light truly converges "
                    "at the image's location."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h18",
        "band": "harder",
        "text": "A person retreats from 1.5 m away from a flat mirror to "
                "4 m away from it. Work out how much bigger the total "
                "gap to their reflection has become.",
        "options": [
            {"text": "By 2.5 m", "correct": False,
             "why": "That is only the change in YOUR distance to the "
                    "mirror; the image's own distance behind it changes "
                    "by the same amount too, doubling the effect."},
            {"text": "By 5 m", "correct": True},
            {"text": "By 8 m", "correct": False,
             "why": "That is the new total separation on its own, not "
                    "the INCREASE from the original 3 m separation."},
            {"text": "It has not changed, since a mirror image is always "
                     "the same distance away", "correct": False,
             "why": "The image's distance from you depends directly on "
                    "your own distance from the mirror, and that has "
                    "changed here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h19",
        "band": "harder",
        "text": "Standing between two facing mirrors produces a seemingly "
                "endless corridor of reflections, each one looking "
                "smaller and dimmer further down. A plane mirror always "
                "makes a same-size image, so why do the repeated images "
                "appear to shrink?",
        "options": [
            {"text": "Because each successive reflection down the "
                     "corridor is genuinely and physically a smaller "
                     "image than the one before it, however the mirrors "
                     "themselves are made or arranged", "correct": False,
             "why": "Every individual reflection is still the same "
                    "actual size as its object — what changes is how far "
                    "away each one appears to be."},
            {"text": "Because mirrors lose their reflective power the "
                     "more times light bounces off them in a row",
             "correct": False,
             "why": "A mirror's own reflectivity does not wear out "
                    "during a single viewing — each bounce simply loses "
                    "a small, steady fraction of the light."},
            {"text": "Because each bounce is of an image that is further "
                     "away, and a same-size object further away looks "
                     "smaller and is dimmer after losing a little light "
                     "at each imperfect reflection", "correct": True},
            {"text": "Because the corridor effect is a complete illusion "
                     "with no real explanation in terms of light",
             "correct": False,
             "why": "It follows directly from ordinary reflection: real "
                    "geometry (distance) and a small real loss of light "
                    "at every bounce, nothing mysterious."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h20",
        "band": "harder",
        "text": "A shiny satin bedsheet and a rough cotton bedsheet, both "
                "white, sit near a bedside lamp. Which would you expect "
                "to show at least a faint, blurred sheen of the lamp, "
                "given that 'shiny' and 'smooth' are different "
                "properties?",
        "options": [
            {"text": "The cotton sheet, since rougher weaves reflect "
                     "more light overall", "correct": False,
             "why": "A rough weave scatters light in every direction "
                    "rather than showing any kind of sheen; roughness "
                    "does not increase the total light reflected either."},
            {"text": "Both equally, since they are the same colour of "
                     "white", "correct": False,
             "why": "Colour is not the deciding factor here; it is how "
                    "smooth the weave of each fabric is."},
            {"text": "Neither — fabric of any kind can never show any "
                     "kind of reflection, however tightly it is woven",
             "correct": False,
             "why": "A sufficiently smooth woven surface, like satin, can "
                    "show a soft sheen; smoothness is what matters, not "
                    "whether the material is a fabric."},
            {"text": "The satin sheet, whose smoother weave keeps some "
                     "of the pattern of the light together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h21",
        "band": "harder",
        "text": "A crumpled foil ball sparkles brightly from almost every "
                "direction in sunlight, while a flat sheet of the same "
                "foil only sparkles brightly from one direction. Explain "
                "the difference using the idea of many small flat facets.",
        "options": [
            {"text": "The crumpled ball has facets angled every which "
                     "way, so some facet is almost always angled to "
                     "reflect the Sun towards your eye, wherever you "
                     "stand", "correct": True},
            {"text": "Crumpling turns the foil into a rough, dull "
                     "surface that absorbs the sunlight instead of "
                     "reflecting it", "correct": False,
             "why": "The crumpled foil still reflects a great deal of "
                    "light — that is exactly why it sparkles so "
                    "brightly."},
            {"text": "The flat sheet reflects less light overall than "
                     "the crumpled ball does", "correct": False,
             "why": "Both forms of the same foil reflect a similarly "
                    "high fraction of the light; what differs is the "
                    "spread of directions it goes in."},
            {"text": "The crumpled ball is simply bigger, so it catches "
                     "more sunlight to reflect", "correct": False,
             "why": "Size is not the point being made here; it is the "
                    "VARIETY of facet angles on the crumpled surface."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h22",
        "band": "harder",
        "text": "A ray hits a mirror at 42° to the normal. The mirror is "
                "then rotated, with the ray kept fixed, until that same "
                "ray now strikes it exactly along the normal. Through "
                "what angle was the mirror rotated?",
        "options": [
            {"text": "84°, twice the original angle", "correct": False,
             "why": "Doubling is the rule for how far the REFLECTED "
                    "ray's direction turns, not for how far the mirror "
                    "itself must be rotated."},
            {"text": "42°", "correct": True},
            {"text": "21°, half the original angle", "correct": False,
             "why": "The mirror's own rotation matches the change needed "
                    "in the angle of incidence directly — it is not "
                    "halved."},
            {"text": "90°, since the ray must now be along the normal",
             "correct": False,
             "why": "Only the CHANGE in angle needs to be rotated "
                    "through, which is the original 42°, not a full 90°."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h23",
        "band": "harder",
        "text": "Light reflects off a mirror (95% reflected) and then off "
                "a sheet of white paper (80% of what reaches it "
                "reflected) before reaching your eye. Starting with 100 "
                "units of light at the source, roughly how many units "
                "reach your eye, ignoring any other losses?",
        "options": [
            {"text": "15 units, from 95% minus 80%", "correct": False,
             "why": "Subtracting the two percentages does not represent "
                    "what happens at two separate reflecting surfaces in "
                    "sequence."},
            {"text": "175 units, since 95% and 80% are added together",
             "correct": False,
             "why": "You cannot end up with more light than you started "
                    "with — the two fractions are multiplied, not added."},
            {"text": "76 units", "correct": True},
            {"text": "95 units, since only the first, larger loss "
                     "matters", "correct": False,
             "why": "The second surface loses some light too — 20% of "
                    "whatever reaches it — and that loss has to be "
                    "included as well."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h24",
        "band": "harder",
        "text": "A student says a smooth black phone screen is 'still "
                "basically a mirror, just tinted black.' Is calling it a "
                "mirror accurate, given what genuinely makes a smooth "
                "black surface different from a smooth white one?",
        "options": [
            {"text": "No — a phone screen only appears to reflect an "
                     "image because of its internal electronics and "
                     "backlight actively generating one, not because of "
                     "anything to do with its glass surface, which by "
                     "itself could never do this", "correct": False,
             "why": "The reflection comes from the smooth glass surface "
                    "itself, and appears whether the screen is switched "
                    "on or off."},
            {"text": "No — dark surfaces cannot ever act as mirrors, "
                     "regardless of how smooth they are", "correct": False,
             "why": "A smooth dark surface, such as a phone screen, "
                    "genuinely does show a faint but real reflection."},
            {"text": "Yes, because black surfaces always reflect more "
                     "light than pale ones of the same smoothness",
             "correct": False,
             "why": "A dark surface generally reflects LESS light "
                    "overall than a pale one of the same smoothness — "
                    "colour affects the amount, not whether it forms an "
                    "image."},
            {"text": "Yes — smoothness, not colour, is what lets a "
                     "pattern of light survive as an image; the black "
                     "screen reflects less light than a white gloss "
                     "surface but still shows a faint, genuine image",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h25",
        "band": "harder",
        "text": "A furniture maker sands a plank until it looks matt, then "
                "applies clear varnish, after which it looks glossy and "
                "shows a faint reflection. Has the wood itself become "
                "smooth, or is something else doing the reflecting?",
        "options": [
            {"text": "The wood grain underneath is still rough at a "
                     "small scale; it is the varnish's own smooth, "
                     "transparent surface layer that does the reflecting",
             "correct": True},
            {"text": "Sanding to matt already made the wood perfectly "
                     "smooth, and the varnish simply darkens the colour",
             "correct": False,
             "why": "A matt finish is, by definition, rough on the scale "
                    "of light — sanding to matt does not achieve the "
                    "smoothness needed for a reflection."},
            {"text": "The varnish soaks into the wood and rearranges its "
                     "fibres to be perfectly flat", "correct": False,
             "why": "Varnish forms a coating on TOP of the wood rather "
                    "than rearranging the fibres underneath it."},
            {"text": "Neither the wood nor the varnish is genuinely "
                     "smooth at all; the faint reflection you see is "
                     "simply an illusion created by the varnish's own "
                     "dark colour", "correct": False,
             "why": "The varnish layer genuinely is smooth enough to "
                    "reflect specularly — this is a real optical effect, "
                    "not a trick of colour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h26",
        "band": "harder",
        "text": "Room A has white walls (rough, about 80% reflective); "
                "Room B has mirrored walls (smooth, about 95% "
                "reflective). Both are lit by identical lamps. A student "
                "claims Room B must be noticeably brighter everywhere. "
                "Evaluate this, considering where the reflected light in "
                "each room actually goes.",
        "options": [
            {"text": "The claim is right, since a higher percentage "
                     "reflected always means brighter everywhere",
             "correct": False,
             "why": "Room A's rough walls scatter their slightly lower "
                    "percentage in every direction, spreading brightness "
                    "evenly, unlike Room B's mirrors."},
            {"text": "The claim does not follow: Room B's mirrors send "
                     "light in specific directions set by geometry, so "
                     "some spots could even be dimmer than in Room A, "
                     "despite the higher percentage reflected",
             "correct": True},
            {"text": "The claim is wrong, because mirrored walls in a "
                     "room like this one actually absorb considerably "
                     "more of the lamp's light overall than ordinary "
                     "white-painted walls ever do, whatever their "
                     "geometry", "correct": False,
             "why": "Mirrored walls absorb LESS light than white walls "
                    "here, not more — that is exactly why they reflect a "
                    "higher percentage."},
            {"text": "Both rooms will be exactly the same brightness "
                     "everywhere, since the lamps are identical",
             "correct": False,
             "why": "How a surface scatters or redirects the light — not "
                    "just the lamp itself — affects how the brightness "
                    "is spread through each room."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h27",
        "band": "harder",
        "text": "A polished chrome door handle shows a clear reflection, "
                "while the powder-coated (matt) door right next to it "
                "shows none — even though both started out as the same "
                "metal. What does this comparison prove about what makes "
                "something act like a mirror?",
        "options": [
            {"text": "It proves that chrome plating must be made from a "
                     "fundamentally different chemical element entirely "
                     "from the ordinary metal hidden underneath the "
                     "powder-coated paint", "correct": False,
             "why": "The base metal is described as the same in both "
                    "cases; chrome plating and powder coating are surface "
                    "treatments, not different underlying metals."},
            {"text": "It proves that only chrome, among all metals, can "
                     "ever be polished into a mirror", "correct": False,
             "why": "Many metals can be polished to act as mirrors; "
                    "chrome is simply the one used here, not the only "
                    "one capable of it."},
            {"text": "It isolates the surface finish as the deciding "
                     "factor, since the same starting metal gives "
                     "completely different results depending on how it "
                     "is finished", "correct": True},
            {"text": "It shows that powder coating makes a surface "
                     "smoother than polishing does", "correct": False,
             "why": "It is the opposite: the powder-coated door is "
                    "matt (rough), while the polished chrome handle is "
                    "the smooth one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h28",
        "band": "harder",
        "text": "Two students disagree about how a submarine periscope "
                "works: one says refraction, the other says reflection. "
                "Who is right, and what is the giveaway in how it is "
                "built?",
        "options": [
            {"text": "Refraction — because the periscope uses a long "
                     "tube full of a different transparent material",
             "correct": False,
             "why": "A periscope tube is simply air inside; there is no "
                    "change of transparent material for light to bend "
                    "through."},
            {"text": "Neither — a periscope works using diffuse "
                     "scattering rather than either process",
             "correct": False,
             "why": "Diffuse scattering would destroy the clear, upright "
                    "image a periscope needs; its two smooth mirrors "
                    "give specular reflection instead."},
            {"text": "Both equally — a periscope relies on refraction "
                     "and reflection happening at exactly the same time",
             "correct": False,
             "why": "No bending of the light as it changes material "
                    "takes place anywhere in a simple two-mirror "
                    "periscope."},
            {"text": "Reflection — the two mirrors set at 45° with an "
                     "air gap show the law of reflection applied twice, "
                     "with no change of material involved", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h29",
        "band": "harder",
        "text": "A ray reflects off a mirror at 65° to the normal, then off "
                "a second mirror set exactly at right angles to the "
                "first. At what angle does it leave the second mirror, "
                "and in what overall direction relative to its original "
                "path?",
        "options": [
            {"text": "25° from the second mirror's normal; travelling "
                     "back exactly parallel to its original path, "
                     "reversed", "correct": True},
            {"text": "65° from the second mirror's normal; travelling "
                     "off at a completely new, unrelated angle",
             "correct": False,
             "why": "The right-angle relationship between the two "
                    "mirrors means the angle at the second one is not "
                    "simply the same as at the first."},
            {"text": "25° from the second mirror's normal; travelling on "
                     "in the same direction as it started, merely shifted "
                     "sideways", "correct": False,
             "why": "A right-angle corner reflector sends the ray "
                    "straight back the way it came, not onward in the "
                    "same direction."},
            {"text": "155° from the second mirror's normal; direction "
                     "cannot be determined without more information",
             "correct": False,
             "why": "An angle of incidence cannot exceed 90°, and the "
                    "right-angle corner reflector's overall behaviour is "
                    "fully determined by geometry alone."},
        ],
        "figure": None,
    },
    {
        "id": "p7-02-h30",
        "band": "harder",
        "text": "A scientist wants to know whether a new material is "
                "'smooth enough to act as a mirror' for a particular use. "
                "Why is it not enough to simply judge how shiny the "
                "material looks to the naked eye?",
        "options": [
            {"text": "Because the naked eye can never detect any "
                     "reflection at all, whatever the surface",
             "correct": False,
             "why": "The eye detects reflected light constantly — that "
                    "is how anything is seen — so this is not the real "
                    "limitation here."},
            {"text": "Because 'smooth enough' is judged relative to the "
                     "wavelength of whatever wave will be reflected, and "
                     "the eye cannot tell that from appearance alone",
             "correct": True},
            {"text": "Because shininess is a purely chemical property "
                     "that has nothing to do with light at all",
             "correct": False,
             "why": "Shininess is very much about light — how much of it "
                    "bounces back — the issue is that it says nothing "
                    "about smoothness relative to a given wavelength."},
            {"text": "Because a material's colour always determines "
                     "whether it is smooth enough to reflect a given "
                     "wave", "correct": False,
             "why": "Colour and roughness relative to a wavelength are "
                    "two separate properties; one does not fix the "
                    "other."},
        ],
        "figure": None,
    },
]
