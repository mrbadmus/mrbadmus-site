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
]
