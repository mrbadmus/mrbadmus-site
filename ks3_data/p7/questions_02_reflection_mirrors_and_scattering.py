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
]
