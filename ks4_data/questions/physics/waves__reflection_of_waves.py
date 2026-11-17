"""Physics · Waves — reflection-of-waves (AQA 8463 4.6.1.3, physics only). Drafted 14 Nov 2026.

Twelve rows, authored in bank order: positions 0–3 easier, 4–7 standard, 8–11 harder
(ks4_data.load_pool emits the first four of each band at positions 0–11). Audience as
ks4_data.classify() derives it: the subtopic is first taught in the Triple Foundation block, so
tier "foundation" and triple_only True, and nothing here leans on an (HT only) statement (the
"varies with wavelength" line of 4.6.2.2 stays out). No stem leans on a drawing.

The distractors come from the usual errors: measuring the angle from the mirror rather than the
normal, taking the angle between the two rays, treating reflect / absorb / transmit as one-only,
and thinking absorbed energy vanishes.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-reflection-of-waves-e01",
        "subtopic_slug": "reflection-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to a wave that is reflected at a boundary.",
        "options": [
            "It passes on into the second material",
            "It bounces back from the boundary",
            "Its energy is taken in by the material",
            "It stops moving when it reaches the boundary",
        ],
        "correct_index": 1,
        "why": "A reflected wave bounces back into the material it came from. Passing on is "
               "transmission, and the material taking in the energy is absorption.",
    },
    {
        "id": "ks4-reflection-of-waves-e02",
        "subtopic_slug": "reflection-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a wave being transmitted at a boundary between two "
                "materials.",
        "options": [
            "It bounces back into the first material",
            "Its energy is absorbed by the second material",
            "It passes through into the second material",
            "It changes into a different type of wave entirely",
        ],
        "correct_index": 2,
        "why": "A transmitted wave passes on through the boundary into the second material.",
    },
    {
        "id": "ks4-reflection-of-waves-e03",
        "subtopic_slug": "reflection-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the line drawn at 90° to a mirror at the point where a ray of light meets it.",
        "options": [
            "The incident ray",
            "The reflected ray",
            "The boundary line",
            "The normal",
        ],
        "correct_index": 3,
        "why": "The normal is drawn at 90° to the surface where the ray meets it. The angles of "
               "incidence and reflection are both measured from it.",
    },
    {
        "id": "ks4-reflection-of-waves-e04",
        "subtopic_slug": "reflection-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light hits a plane mirror with an angle of incidence of 25°. State the "
                "angle of reflection.",
        "options": [
            "25°",
            "50°",
            "65°",
            "155°",
        ],
        "correct_index": 0,
        "why": "The angle of reflection equals the angle of incidence, both measured from the "
               "normal: 25°.",
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-reflection-of-waves-s01",
        "subtopic_slug": "reflection-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light meets a plane mirror. The angle between the ray and the surface of "
                "the mirror is 20°. Determine the angle of reflection.",
        "options": [
            "20°",
            "40°",
            "70°",
            "160°",
        ],
        "correct_index": 2,
        "why": "Angles are measured from the normal, which is at 90° to the mirror. The angle of "
               "incidence is 90° − 20° = 70°, and the angle of reflection equals it: 70°.",
    },
    {
        "id": "ks4-reflection-of-waves-s02",
        "subtopic_slug": "reflection-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Light shines onto a sheet of clear window glass. Describe what happens to the "
                "light at the glass.",
        "options": [
            "Most is reflected and a small part is transmitted",
            "Most is transmitted and a small part is reflected",
            "Most is absorbed and a small part is transmitted",
            "All of it is transmitted and none of it is reflected",
        ],
        "correct_index": 1,
        "why": "You can see through a window, so most of the light is transmitted, and you can "
               "see a faint reflection in it, so a little is reflected. Clear glass absorbs very "
               "little.",
    },
    {
        "id": "ks4-reflection-of-waves-s03",
        "subtopic_slug": "reflection-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pupil draws a ray diagram for a plane mirror. He measures the angle of "
                "incidence and the angle of reflection from the surface of the mirror. Explain "
                "what he should have done.",
        "options": [
            "Measured both angles from the normal, at 90° to the mirror",
            "Measured both angles from the incoming ray instead",
            "Measured only the angle of reflection, from the mirror",
            "Added the two angles together and halved the total",
        ],
        "correct_index": 0,
        "why": "The angle of incidence and the angle of reflection are both measured from the "
               "normal, the line at 90° to the mirror, never from the surface.",
    },
    {
        "id": "ks4-reflection-of-waves-s04",
        "subtopic_slug": "reflection-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a room with bare walls and a hard floor echoes more than the same "
                "room with thick curtains and a carpet.",
        "options": [
            "Hard surfaces absorb more sound; soft materials reflect more",
            "Sound travels faster in a room with curtains and carpets",
            "Curtains and carpets transmit the sound back into the room",
            "Hard surfaces reflect more sound; soft materials absorb more",
        ],
        "correct_index": 3,
        "why": "An echo is reflected sound. Hard, flat surfaces reflect most of the sound that "
               "reaches them, while curtains and carpets absorb more of it, so less is "
               "reflected.",
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-reflection-of-waves-h01",
        "subtopic_slug": "reflection-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light reflects from a plane mirror. The angle between the incoming ray "
                "and the reflected ray is 100°. Determine the angle of incidence.",
        "options": [
            "100°",
            "80°",
            "50°",
            "40°",
        ],
        "correct_index": 2,
        "why": "The angle between the two rays is the angle of incidence plus the angle of "
               "reflection. These are equal, so the angle of incidence is 100° ÷ 2 = 50°.",
    },
    {
        "id": "ks4-reflection-of-waves-h02",
        "subtopic_slug": "reflection-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wave meets the boundary between two different materials. Explain why the "
                "reflected wave carries less energy than the incoming wave.",
        "options": [
            "Reflection makes the wave travel faster, so it carries less energy",
            "Part of the wave is transmitted or absorbed at the boundary",
            "Energy is destroyed every time a wave is reflected at a boundary",
            "Reflection always makes the wavelength of the wave longer",
        ],
        "correct_index": 1,
        "why": "At most boundaries only part of the wave is reflected. The rest is transmitted "
               "into the second material or absorbed by it, so the reflected wave carries only "
               "part of the energy.",
    },
    {
        "id": "ks4-reflection-of-waves-h03",
        "subtopic_slug": "reflection-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light travels along the normal and hits a plane mirror. Describe the "
                "path of the reflected ray.",
        "options": [
            "It reflects along the surface of the mirror",
            "It reflects at 45° on the other side of the normal",
            "It passes through the mirror without reflecting",
            "It reflects straight back along the normal",
        ],
        "correct_index": 3,
        "why": "Along the normal the angle of incidence is 0°. The angle of reflection is also "
               "0°, so the ray goes straight back the way it came.",
    },
    {
        "id": "ks4-reflection-of-waves-h04",
        "subtopic_slug": "reflection-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sound reaches a wall. Most of the sound is reflected and a little is absorbed. "
                "Explain what happens to the energy of the absorbed sound.",
        "options": [
            "It is transferred to the wall, which warms very slightly",
            "It is destroyed, because energy is lost at a boundary",
            "It is carried back into the room as part of the echo",
            "It makes the wall give out a louder sound of its own",
        ],
        "correct_index": 0,
        "why": "Energy is never destroyed. Absorbed sound transfers its energy to the wall's "
               "thermal store, so the wall warms by a tiny amount. The echo is the reflected "
               "part only.",
    },
]
