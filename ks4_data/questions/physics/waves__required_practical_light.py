"""Physics · Waves — required-practical-light (AQA 8463 Required practical activity 9, physics
only: the reflection of light by different types of surface and the refraction of light by
different substances). Drafted 14 Nov 2026.

Twelve rows, authored in bank order: positions 0–3 easier, 4–7 standard, 8–11 harder. Audience
as ks4_data.classify() derives it: first taught in the Triple Foundation block, so tier
"foundation" and triple_only True. Nothing leans on an (HT only) statement: why light refracts
(a change of speed) stays out. No stem leans on a drawing; the one data row gives its numbers in
the stem.

The rows walk the practical: apparatus, variables, the tracing method, accuracy, safety, the
expected results and reading made-up data.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-required-practical-light-e01",
        "subtopic_slug": "required-practical-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the piece of apparatus used to measure the angles in this practical.",
        "options": [
            "A metre rule",
            "A ray box",
            "A protractor",
            "A stopwatch",
        ],
        "correct_index": 2,
        "why": "A protractor measures angles. The ray box makes the narrow ray, and a ruler draws "
               "the lines.",
    },
    {
        "id": "ks4-required-practical-light-e02",
        "subtopic_slug": "required-practical-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the line that every angle in this practical is measured from.",
        "options": [
            "The normal",
            "The edge of the paper",
            "The side of the block",
            "The surface of the mirror",
        ],
        "correct_index": 0,
        "why": "Every angle of incidence, reflection and refraction is measured from the normal, "
               "the line at 90° to the surface.",
    },
    {
        "id": "ks4-required-practical-light-e03",
        "subtopic_slug": "required-practical-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light hits a plane mirror with an angle of incidence of 40°. State the "
                "angle of reflection the student should measure.",
        "options": [
            "20°",
            "50°",
            "80°",
            "40°",
        ],
        "correct_index": 3,
        "why": "For a plane mirror the angle of reflection equals the angle of incidence: 40°.",
    },
    {
        "id": "ks4-required-practical-light-e04",
        "subtopic_slug": "required-practical-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the main hazard from the ray box in this practical.",
        "options": [
            "Its light is radioactive",
            "Its lamp gets hot",
            "It gives out X-rays",
            "It makes a loud noise",
        ],
        "correct_index": 1,
        "why": "The lamp in a ray box gets hot, so do not touch the housing and let it cool "
               "before moving it.",
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-required-practical-light-s01",
        "subtopic_slug": "required-practical-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student shines a ray into a glass block at several angles of incidence and "
                "measures each angle of refraction. Identify the independent variable.",
        "options": [
            "The angle of refraction",
            "The angle of incidence",
            "The size of the glass block",
            "The brightness of the ray box",
        ],
        "correct_index": 1,
        "why": "The independent variable is the one the student chooses and changes: the angle "
               "of incidence. The angle of refraction is measured, so it is the dependent "
               "variable.",
    },
    {
        "id": "ks4-required-practical-light-s02",
        "subtopic_slug": "required-practical-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the student marks each ray with two crosses placed far apart.",
        "options": [
            "So the ray box does not get too hot to touch",
            "So the ray is brighter where it is marked on the paper",
            "So the angle of refraction comes out bigger each time",
            "So the line drawn through them has an accurate direction",
        ],
        "correct_index": 3,
        "why": "With the crosses far apart, a small error in placing one cross makes only a small "
               "error in the direction of the line, so the angle is measured more accurately.",
    },
    {
        "id": "ks4-required-practical-light-s03",
        "subtopic_slug": "required-practical-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ray of light enters a rectangular glass block from air with an angle of "
                "incidence of 50°. Identify the angle of refraction the student is most likely "
                "to measure.",
        "options": [
            "31°",
            "50°",
            "65°",
            "0°",
        ],
        "correct_index": 0,
        "why": "Light entering glass bends towards the normal, so the angle of refraction is "
               "smaller than 50°. Only a ray along the normal has 0°.",
    },
    {
        "id": "ks4-required-practical-light-s04",
        "subtopic_slug": "required-practical-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student shines a ray of light at a sheet of white paper instead of a mirror. "
                "Describe what she sees.",
        "options": [
            "One clear reflected ray at an equal angle",
            "No single reflected ray: the light is scattered",
            "The ray passes straight through the paper",
            "The ray bends towards the normal in the paper",
        ],
        "correct_index": 1,
        "why": "The surface of the paper is rough, so the light is scattered in many directions. "
               "This is diffuse reflection: there is no single reflected ray.",
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-required-practical-light-h01",
        "subtopic_slug": "required-practical-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student shines a ray into a glass block and into a box of water, each with an "
                "angle of incidence of 40°. The angle of refraction is 25° in the glass and 29° "
                "in the water. Identify the correct conclusion.",
        "options": [
            "The water bends the light more than the glass does",
            "Both substances bend the light by the same amount",
            "The glass bends the light more than the water does",
            "Neither substance bends the light at this angle",
        ],
        "correct_index": 2,
        "why": "The smaller angle of refraction is in the glass, so the ray turned further "
               "towards the normal there. Glass bends the light more than water does.",
    },
    {
        "id": "ks4-required-practical-light-h02",
        "subtopic_slug": "required-practical-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student measures the angle of reflection from a plane mirror five times for an "
                "angle of incidence of 30°: 30°, 31°, 29°, 30° and 42°. Identify the result "
                "that should be checked.",
        "options": [
            "42°",
            "29°",
            "31°",
            "30°",
        ],
        "correct_index": 0,
        "why": "The angle of reflection should equal the angle of incidence, 30°. Four results "
               "are within 1° of it; 42° is far from the rest, so it is anomalous and should be "
               "checked or repeated.",
    },
    {
        "id": "ks4-required-practical-light-h03",
        "subtopic_slug": "required-practical-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student wants to compare how much glass and water refract light. Identify the "
                "variable she must keep the same for a fair comparison.",
        "options": [
            "The substance the ray enters",
            "The angle of refraction",
            "The angle of incidence",
            "The order she tests them in",
        ],
        "correct_index": 2,
        "why": "To compare the substances she changes the substance and measures the angle of "
               "refraction, so the angle of incidence must be the same for both.",
    },
    {
        "id": "ks4-required-practical-light-h04",
        "subtopic_slug": "required-practical-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student cannot see the ray inside the glass block clearly. Explain how she can "
                "still find the angle of refraction.",
        "options": [
            "Take it as equal to the angle of incidence every time",
            "Use a wider beam so that the ray is easier to see",
            "Measure the angle between the ray and the side of the block",
            "Join where the ray enters to where it leaves, then measure",
        ],
        "correct_index": 3,
        "why": "The ray travels in a straight line inside the block. Mark where it enters and "
               "where it leaves, take the block away, join the two points and measure the angle "
               "between that line and the normal.",
    },
]
