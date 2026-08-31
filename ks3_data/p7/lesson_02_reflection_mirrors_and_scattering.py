"""P7 L2 — Reflection: mirrors and scattering (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-02-reflection-mirrors-and-scattering.dc.html`.

Her page wins outright. The mirror-and-paper hook, the four-surface ray
bench, the beam, the single worked example and all four rungs are hers.

── ⚖️ MRB-204 · AN EQUALITY TAKES A BEAM, NOT A TRIANGLE ────────────

`r = i` is neither a product nor a sum. Design draws it as two bars of
identical length with an equals sign and **no cover buttons**, following
the `p1-08` ruling: a balance has nothing to cover, because covering one
side asks a question whose answer is written on the other side.

⊕ The engine's beam is the `p1-08` / `c2-06` pan balance rather than her
two stacked bars. Same family, same claim, our drawing — and the aria
description therefore describes OURS. See `DEPARTURES-P7.md`.

── ⚖️ RULED · ONE WORKED EXAMPLE AND ONE ATTEMPT QUESTION ────────────

Design's README says it in terms: *"p7-02 keeps a single example and a
single question: its quantities are angles in degrees, so conversion
cannot arise and the C step reads as the no-conversion case."*

`ks3_art.kit.r_cfifa_attempt` refuses fewer than two questions, because
on every other CFIFA page the second question is where the conversion
lives. The payload therefore declares `one_question_because`, which lifts
that single check and nothing else. **A second question was not
invented**: it would have been content nobody drew, in a block whose
whole point is that the student meets Design's own scenario.

── ⚖️ THE FOUR SURFACES ARE THE ARGUMENT, AND FOIL IS THE HINGE ──────

Mirror, white paper, crumpled foil, matt black card. Foil is the case
that separates SHINY from SMOOTH in one object: it sends back 88% and
still shows no image. Her rung 2 distractor D — *"Paper is not shiny
enough"* — is answered by it directly.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-ray · s-beam · s-ladder

⚠️ **MRB-208** — the `s-beam` id goes on the attempt panel, because
Design's own `DONE` for it reads `s.buildOpen`.

⊕ **HER RAIL LABEL SAID "four steps" AND THE BLOCK BELOW IT IS FIVE.**
See `DEPARTURES-P7.md` row 1.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-05  rough surfaces break the law of reflection
    LIGHT-06  angles in reflection are measured from the mirror
    LIGHT-07  the mirror sends back far more light than the paper does
    LIGHT-08  only shiny surfaces can reflect light

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 0 and 1. See `lesson_01`'s note for the ruling.
"""

LESSON = {
    "slug":  "reflection-mirrors-and-scattering",
    "title": "Reflection: mirrors and scattering",
    "discipline": "physics",
    "unit": "Light",
    "family": "MODEL",

    "covers": ["KS3.P.LGT.03a", "KS3.P.LGT.04a"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["light-travels"],
    "assumes": [],
    "references": ["echoes-reflection-and-absorption",
                   "why-things-look-coloured", "waves-on-water"],
    "ks4_links": [],

    "meta_description": "A mirror and a sheet of paper send back about the "
                        "same amount of light and obey the same rule. Only "
                        "one of them shows you your face.",

    "big_question": "A mirror and a sheet of paper send back about the same "
                    "amount of light and obey exactly the same rule. Only one "
                    "of them shows you your face, and the reason is the "
                    "surface rather than the rule.",

    "rail": [
        {"anchor": "s-hook",   "short": "PAPER",
         "label": "Mirror and paper",         "done_when": "committed"},
        {"anchor": "s-ray",    "short": "RAY",
         "label": "Ray box and four surfaces",
         "done_when": "gate_and_a_control"},
        {"anchor": "s-beam",   "short": "FIFA",
         "label": "The beam and five steps",  "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",           "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two white surfaces. One shows your face.",
        "prompt": "A mirror and a sheet of white paper both send back almost "
                  "all the light that falls on them. Hold either up to a "
                  "window and the room brightens. Only one of them shows you "
                  "your own face.",
        "commit": "What is different about what the light does at the two "
                  "surfaces?",
        "options": [
            "The paper does not really reflect light — it makes its own, "
            "which is why a room brightens",
            "The mirror keeps the rays in the arrangement they arrived in; "
            "the paper scrambles them",
            "The mirror sends back far more light than the paper does, and "
            "paper keeps most of it back",
            "The paper absorbs the image and sends back only the brightness, "
            "so no face can survive",
        ],
        "answer": 1,
        "reveal": "Both surfaces send back most of the light, and both obey "
                  "the law of reflection at every single point. The "
                  "difference is the surface itself. A mirror is smooth, so "
                  "parallel rays stay parallel and the arrangement of the "
                  "light survives — and the arrangement is the image. Paper "
                  "is rough, so each ray leaves at its own angle and the "
                  "arrangement is gone.",
    },

    "misconceptions": [
        {"id": "LIGHT-05",
         "statement": "Rough surfaces break the law of reflection.",
         "elicited_by": "ray",
         "confronted_by": "s-think"},
        {"id": "LIGHT-06",
         "statement": "Angles in reflection are measured from the mirror.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "LIGHT-07",
         "statement": "The mirror sends back far more light than the paper "
                      "does.",
         "elicited_by": "s-hook",
         "confronted_by": "ray"},
        {"id": "LIGHT-08",
         "statement": "Only shiny surfaces can reflect light.",
         "elicited_by": "s-ladder",
         "confronted_by": "ray"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every ray that meets a surface obeys the same rule. Draw a "
                 "line at right angles to the surface where the ray lands — "
                 "that line is called the <strong>normal</strong> — and "
                 "measure both angles from it. Then the <strong>angle of "
                 "reflection equals the angle of incidence</strong>, always, "
                 "on every surface, however rough."},
        {"type": "explainer",
         "text": "What changes between a mirror and a sheet of paper is not "
                 "the rule but the surface. A mirror is smooth on the scale "
                 "of light, so the normal points the same way everywhere and "
                 "a set of parallel rays comes off still parallel: the "
                 "pattern survives, and the pattern is the image. That is "
                 "<strong>specular reflection</strong>. Paper is rough on "
                 "that scale, so every tiny facet has its own normal pointing "
                 "a different way. Each ray still reflects correctly, and the "
                 "set of them leaves in all directions with the pattern "
                 "destroyed. That is <strong>diffuse scattering</strong>, and "
                 "it is why you can see the paper from anywhere in the room "
                 "and cannot see yourself in it."},
        {"type": "explainer",
         "text": "Some of the light is neither reflected nor scattered but "
                 "<strong>absorbed</strong>, its energy taken up by the "
                 "surface. A matt black card is rough like paper and absorbs "
                 "most of what lands on it, so very little leaves in any "
                 "direction at all."},
        # ── ⚖️ RULED 30 Aug 2026 · THE PLANE MIRROR IMAGE ──────────────
        #
        # `covers` claims LGT.04a, imaging in mirrors, and nothing on the
        # page delivered it. The near/far wording is load-bearing and is
        # not to be "tidied" into the usual left-right sentence: a plane
        # mirror does NOT swap left and right, and "lateral inversion" is a
        # label rather than a reason. Turning the page round is what swaps
        # its left and right; the mirror reverses only the axis pointing at
        # it. No figure — P7 has no drawer for one.
        {"type": "explainer",
         "text": "Stand a mirror up and look at yourself. The image is the "
                 "same size as you and the same way up, and it sits as far "
                 "behind the glass as you are in front of it. Nothing is "
                 "there: no light comes from behind the mirror. Your eye "
                 "follows the reflected rays back along the straight lines "
                 "they arrived on, and the image is where those lines meet. "
                 "That is what <strong>virtual</strong> means. The one axis "
                 "a plane mirror does reverse is the one running towards it "
                 "and away from it — near and far. Writing looks backwards "
                 "because you had to turn the page round to face the glass, "
                 "and turning it is what swapped its left and right."},

        # ── #s-ray · a ray box, a protractor and four surfaces ─────────
        {"type": "ray-surface",
         "id": "ray",
         "anchor": "s-ray",
         "eyebrow": "At the bench · a ray box, a protractor and four surfaces",
         "heading": "One rule. Four different results.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A single narrow ray from a ray box lands on a surface, "
                   "with the normal drawn in at the point where it lands. Set "
                   "the angle it comes in at, and set what it lands on.",
         "gate": {
             "prompt": "Commit first. A ray hits a mirror at 30° to the "
                       "normal. The mirror is swapped for a sheet of white "
                       "paper and the ray comes in at exactly the same 30°. "
                       "What happens to the angle of reflection of that one "
                       "ray?",
             "options": [
                 "It is still 30° — the rule holds on every surface",
                 "It becomes random, because paper scatters light",
                 "It becomes 0°, because paper sends light straight back out",
                 "There is no angle of reflection, because paper absorbs the "
                 "ray",
             ],
             "answer": 0,
         },
         "inc": {"label": "Angle from the normal",
                 "min": 0, "max": 80, "step": 5, "start": 40},
         "surf_label": "What it lands on",
         "normal_label": "NORMAL",
         # Design's own four, in her order. `spread` is the half-fan in
         # degrees (0 draws ONE reflected ray, anything else draws five);
         # `back` is the percentage that leaves again; `profile` chooses the
         # drawn surface — flat, wavy or faceted.
         "surfaces": [
             {"id": "mirror", "label": "Plane mirror", "spread": 0,
              "back": 95, "profile": "flat",
              "kind": "Specular — the pattern survives",
              "caption": "PLANE MIRROR — SMOOTH ON THE SCALE OF LIGHT",
              "note": "A mirror is smooth enough that the normal points the "
                      "same way everywhere on it, so a set of parallel rays "
                      "leaves still parallel and the arrangement of the light "
                      "is preserved. That preserved arrangement is what an "
                      "image is."},
             {"id": "paper", "label": "White paper", "spread": 34,
              "back": 80, "profile": "wavy",
              "kind": "Diffuse — the pattern is lost",
              "caption": "WHITE PAPER — ROUGH ON THE SCALE OF LIGHT",
              "note": "Paper sends back nearly as much light as a mirror, "
                      "which is why it looks bright, and scatters it in every "
                      "direction, which is why it shows no image. Every one "
                      "of those scattered rays has still obeyed the law of "
                      "reflection at its own tiny facet."},
             {"id": "foil", "label": "Crumpled foil", "spread": 20,
              "back": 88, "profile": "faceted",
              "kind": "Diffuse — the pattern is lost",
              "caption": "CRUMPLED FOIL — SHINY BUT NOT FLAT",
              "note": "Foil is the case that separates shiny from smooth. The "
                      "metal reflects almost everything, so it stays bright, "
                      "but the crumpling gives every patch a different normal "
                      "and the reflection breaks into a jumble of bright "
                      "fragments rather than one image."},
             {"id": "black", "label": "Matt black card", "spread": 34,
              "back": 6, "profile": "wavy",
              "kind": "Diffuse, and mostly absorbed",
              "caption": "MATT BLACK CARD — ROUGH AND ABSORBING",
              "note": "Black card is rough like paper, so what does leave is "
                      "scattered in every direction — but almost nothing "
                      "leaves. Most of the arriving light is absorbed and its "
                      "energy ends up warming the card very slightly, which "
                      "is why black surfaces in sunlight get hot."},
         ],
         "readouts": [
             {"id": "inc", "label": "Angle of incidence",
              "sub": "measured from the normal"},
             {"id": "ref", "label": "Angle of reflection",
              "sub": "measured from the normal"},
             {"id": "back", "label": "Roughly how much leaves again",
              "sub": "the rest is absorbed"},
             {"id": "verdict", "label": "How the rays leave"},
         ],
         # One branch per surface, each closing with the live angle and the
         # live fraction. Her sentence, her order.
         "branch_tail": " Your ray comes in at {inc}° from the normal and "
                        "every reflected ray here leaves at {inc}° from the "
                        "normal of the facet it hit; about {back}% of the "
                        "light leaves again and the rest is absorbed."},

        {"type": "formula",
         "id": "reflection-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Angle of reflection = angle of incidence",
         "support": ["Both measured from the normal",
                     # ⊕ REGISTER ROW 4. Hers reads "Two bars of the same
                     # length, always … whatever one bar reads, the other
                     # reads too" — a sentence about HER two-bars drawing.
                     # The figure on this page is the engine's pan balance
                     # (row 3), so the sentence names what is drawn.
                     "Two sides that always balance. Nothing is being "
                     "added up here and nothing is being shared out, so there "
                     "is nothing to cover: whatever one side reads, the other "
                     "reads too.",
                     "i · angle of incidence, from the normal · °",
                     "r · angle of reflection, from the normal · °"],
         # ⚖️ MRB-204 · AN EQUALITY, so a BEAM and NO cover buttons. The aria
         # describes the beam this engine draws, not the two stacked bars
         # Design drew — an accessible description of a different picture is
         # worse than one of this one (the P6 precedent).
         "figure": {
             "shape": "balance",
             "aria_label": "A balance beam, dead level. In the left pan, i — "
                           "the angle the ray arrives at, measured from the "
                           "normal. In the right pan, r — the angle it leaves "
                           "at, measured from the same normal. The two are "
                           "always equal, so the beam never tips.",
             "pans": {"left": "i", "right": "r"},
             "caption": "always equal"}},

        {"type": "worked-example", "id": "cfifa-reflect-p7"},
        {"type": "check", "id": "your-turn-reflect", "anchor": "s-beam"},

        {"type": "key-fact", "ref": "reflection-law-and-surface"},

        {"type": "misconception", "id": "think-rough-breaks-the-law",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-reflect-p7",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A ray strikes a plane mirror at 20° to the mirror "
                    "surface. What is the angle of reflection?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Angles are angles — nothing here can "
                                  "arrive in the wrong size. Your turn "
                                  "below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "20° stays 20° · 90° stays 90°",
              "note": "Both angles are in degrees and the rule compares them "
                      "directly, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "r = i, both measured from the normal",
              "note": "The rule is an equality, so the two angles are always "
                      "the same number."},
             {"letter": "I", "label": "Insert",
              "line": "i = 90° − 20°",
              "note": "The 20° given is to the mirror surface, and the normal "
                      "is at right angles to that surface."},
             {"letter": "F", "label": "Fine-tune",
              "line": "90 − 20 = 70, so i = 70°",
              "note": "Degrees taken from degrees leave degrees."},
             {"letter": "A", "label": "Answer", "line": "r = 70°",
              "note": "Seventy degrees from the normal, which is 20° from the "
                      "mirror on the other side."},
         ]},

        {"id": "your-turn-reflect",
         "kind": "p7-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # ⚖️ ONE QUESTION, AND THE HELPER IS TOLD WHY. Design's page carries
         # one, because a conversion cannot arise between two angles in
         # degrees, and her README says so. See `kit.r_cfifa_attempt`.
         "one_question_because":
             "Design's p7-02 carries ONE question, and her README states the "
             "reason: the quantities are angles in degrees, so a conversion "
             "cannot arise and the C step reads as the no-conversion case. "
             "The second question on every other CFIFA page is the "
             "conversion one, and inventing one here would be inventing "
             "content nobody drew.",
         # The bench opens at 40° from the normal.
         "rest": {"inc": "40", "comp": "50"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your ray arrives at {inc}° from the normal.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "the angle is already in degrees",
                   "note": "The protractor reads in degrees and the rule "
                           "compares degrees with degrees, so there is "
                           "nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "r = i, both from the normal",
                   "note": "An equality: whatever the incoming angle is, the "
                           "reflected one matches it."},
                  {"letter": "I", "label": "Insert",
                   "line": "i = {inc}°",
                   "note": "Read from the protractor on the bench, measured "
                           "from the dashed normal."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "r = {inc}°, so the ray leaves at {comp}° to the "
                           "surface",
                   "note": "The normal is at right angles to the surface, so "
                           "the two angles add to 90°."},
                  {"letter": "A", "label": "Answer",
                   "line": "r = {inc}°",
                   "note": "On the far side of the normal from the incoming "
                           "ray, and the same on any of the four surfaces."},
              ],
              "close": "The five lines above give {inc}°, which is the angle "
                       "the bench above is drawing."},
         ]},

        {"id": "think-rough-breaks-the-law",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-05",
         "statements": [
             {"quote": "Rough surfaces break the law of reflection.",
              "targets": "LIGHT-05",
              "body": [
                  "Not one ray disobeys it. Zoom in far enough on a sheet of "
                  "paper and it is a landscape of fibres, each facet flat and "
                  "each with its own normal pointing wherever that facet "
                  "happens to face. A ray landing on one of them reflects at "
                  "exactly the angle it arrived at, measured from that "
                  "facet’s normal — and because the facets point every which "
                  "way, the rays that started off parallel finish scattered. "
                  "The law holds perfectly. What is lost is the arrangement, "
                  "and the arrangement was the image.",
              ]},
             {"quote": "Angles in reflection are measured from the mirror.",
              "targets": "LIGHT-06",
              "body": [
                  "They are measured from the normal, the line drawn at right "
                  "angles to the surface, and it is a convention worth being "
                  "fussy about because it is the one that keeps working. A "
                  "ray at 20° to the mirror is at 70° to the normal, and if "
                  "you quote 20° as the angle of incidence every later answer "
                  "is wrong by the same amount. Measuring from the normal "
                  "also survives being taken to a curved mirror, where there "
                  "is no single surface to measure from, and to refraction in "
                  "the next lesson, where the two materials meet at one "
                  "point.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "reflection-law-and-surface",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "The angle of reflection equals the angle of incidence, both "
                 "measured from the normal — the line at right angles to the "
                 "surface. On a smooth surface parallel rays stay parallel "
                 "and the pattern survives as an image, which is specular "
                 "reflection. On a rough surface every facet has its own "
                 "normal, so the rays leave in all directions and the pattern "
                 "is lost, which is diffuse scattering. Some light is "
                 "absorbed at every surface."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A ray strikes a plane mirror at 25° to the mirror surface. "
                 "What is the angle of reflection?",
            "options": [
                "65°",
                "25° — the angle of reflection equals the angle given",
                "50° — double the angle, because the ray turns through both "
                "angles",
                "115° — add the 25° on to the 90° of the normal",
            ],
            "answer": 0,
            "feedback": {
                1: "The rule is right and the angle given is the wrong one. "
                   "The 25° is measured from the mirror; angles of incidence "
                   "and reflection are measured from the normal, which makes "
                   "it 65°.",
                2: "Fifty degrees is the angle between the incoming and "
                   "outgoing rays when each is 25° from the normal. It is "
                   "not the angle of reflection, which is measured from the "
                   "normal to one ray.",
                3: "The normal is at 90° to the mirror, so a ray 25° from "
                   "the mirror is 25° short of the normal, not 25° past it. "
                   "Take it away rather than adding it.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "You can see a sheet of white paper from anywhere in the "
                 "room but cannot see your face in it. Which statement is "
                 "right?",
            "options": [
                "Paper does not obey the law of reflection, which is why the "
                "rays come off in random directions rather than at the "
                "angle they arrived at.",
                "Its rough surface gives every facet a different normal, so "
                "rays that arrive parallel leave in all directions — each "
                "one still obeying the law of reflection.",
                "Paper absorbs almost all the light, so there is too little "
                "left to form an image.",
                "Paper is not shiny enough, and only shiny surfaces can "
                "reflect light.",
            ],
            "answer": 1,
            "feedback": {
                0: "Every single ray obeys it exactly. What varies is the "
                   "direction each facet faces, and therefore the direction "
                   "of each normal.",
                2: "White paper sends back most of what lands on it, which "
                   "is why it looks bright. Absorption is what makes black "
                   "card dark, not what stops paper showing a face.",
                3: "Crumpled kitchen foil is thoroughly shiny and still "
                   "shows no image. Shiny is about how much comes back; "
                   "smooth is about whether the pattern survives, and those "
                   "are different things.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why a mirror shows an image and a sheet of white "
                 "paper does not, using the words normal, parallel and "
                 "scattering.",
            "field_label": "Your explanation",
            "placeholder": "At every point the angle of reflection…",
            "success": [
                "Says the law of reflection holds at both surfaces: the "
                "angle of reflection equals the angle of incidence from the "
                "normal.",
                "Says a mirror is smooth, so the normal points the same way "
                "all over it.",
                "Says parallel rays therefore leave the mirror still "
                "parallel, and that preserved arrangement is the image.",
                "Says paper is rough, so each tiny facet has its own normal "
                "pointing a different way.",
                "Says the rays are therefore scattered in all directions and "
                "the arrangement is lost.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A wet road at night is dangerous to drive on partly "
                 "because it reflects headlights very differently from a dry "
                 "one. Explain what changes when the road is wet, and why "
                 "oncoming drivers are dazzled by long streaks of light.",
            "field_label": "Your answer",
            "placeholder": "A dry road surface is rough, so…",
            "success": [
                "Says a dry road is rough, so it scatters headlight beams in "
                "all directions.",
                "Says scattering sends a little light to every driver and "
                "lets the road surface itself be seen.",
                "Says water fills the roughness and leaves a smooth surface.",
                "Says the smooth surface reflects specularly, sending the "
                "beam mostly in one direction rather than scattering it.",
                "Says an oncoming driver in that direction receives a great "
                "deal of the light at once, while the road surface itself "
                "becomes hard to make out.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "The angle of reflection equals the angle of incidence, both "
                "measured from the normal — the line at right angles to the "
                "surface at the point where the ray lands. A smooth surface "
                "keeps parallel rays parallel, so the arrangement of the "
                "light survives and an image forms: specular reflection. A "
                "rough surface gives every facet its own normal, so the rays "
                "leave in every direction and the arrangement is lost: "
                "diffuse scattering. At every surface some light is absorbed "
                "instead.",

    "stretch": [
        {"id": "almost-everything-is-scattering",
         "type": "explainer",
         "text": "Almost everything you can see is being seen by diffuse "
                 "scattering. Only a handful of objects — mirrors, still "
                 "water, polished metal, glass at a glancing angle — reflect "
                 "specularly, and those are precisely the ones that show you "
                 "something other than themselves. A room lit by a single "
                 "lamp is visible in every corner because every rough surface "
                 "in it is scattering light in all directions at once, which "
                 "is also why the shadows are soft."},
        {"id": "smooth-compared-with-the-wavelength",
         "type": "explainer",
         "text": "Smooth is a comparison with the wavelength of light, not "
                 "with your finger. Visible light has a wavelength of a few "
                 "ten-thousandths of a millimetre, so a surface has to be "
                 "flat to well within that to act as a mirror. Radio waves "
                 "have wavelengths measured in metres, and a wire mesh with "
                 "centimetre holes is a perfect mirror to them — which is why "
                 "a satellite dish can be a grid rather than a solid sheet, "
                 "and why the door of a microwave oven has a metal grid you "
                 "can see straight through."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "normal",
         "definition": "The line drawn at right angles to a surface where a "
                       "ray lands. Both angles are measured from it, never "
                       "from the surface."},
        {"term": "specular reflection",
         "definition": "Reflection at a surface smooth enough that parallel "
                       "rays leave still parallel, so the arrangement of the "
                       "light survives as an image."},
        {"term": "diffuse scattering",
         "definition": "Reflection at a rough surface, where every facet has "
                       "its own normal and the rays leave in all directions "
                       "with the arrangement lost."},
    ],

    "tutor": {
        "anchor": "s-ray",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got an angle and a surface, and want to know where the ray "
                "goes?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Ray diagrams for plane and curved mirrors, virtual "
                   "images, specular and diffuse reflection at a boundary, "
                   "and the relationship between surface roughness and "
                   "wavelength.",

    "convention_note": "The bench is a teaching model. Angles are drawn to "
                       "scale from the normal and the law of reflection is "
                       "applied exactly. The percentages of light leaving "
                       "again are round teaching figures for a typical "
                       "surface of each kind and depend on the colour of the "
                       "light and the angle it arrives at. The scattered fans "
                       "are drawn as five rays spread over a fixed angle so "
                       "the spread can be seen; a real rough surface sends "
                       "light out over the whole half-space above it, and the "
                       "number and spacing of the drawn rays carry no "
                       "information. The surface profiles are drawn far "
                       "rougher than any of these materials really are, since "
                       "paper is rough only on the scale of the wavelength of "
                       "light.",

    "ws": ["measurement"],
}
