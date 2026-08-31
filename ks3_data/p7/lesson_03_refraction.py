"""P7 L3 — Refraction (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-03-refraction.dc.html`.

Her page wins outright. The broken-straw hook, the ray-into-a-block
bench, the apparent-depth figure and all four rungs are hers.

── ⚖️ MRB-204 · NO BLOCK, AND THE STATUTE IS WHY ────────────────────

Snell's law and refractive index are GCSE. `LGT.04b` is qualitative, so
there is no relationship to put in a triangle and nothing was invented to
have something to put in one. The bench computes the angle inside the
block from the material's index and prints it; the arithmetic is the
instrument's, not the student's.

── ⚖️ RULED · THE ZERO-ANGLE STATE IS ITS OWN BRANCH ────────────────

A ray along the normal SLOWS and does not bend. That is not a special
case of a bend, it is the state that proves the mechanism: slowing on its
own bends nothing, and it takes an angle for one edge of the beam to
reach the slower material first. Design gives it its own note and its own
verdict word — *"Straight on, but slower"* — and the ghost line is not
drawn there, because there is nothing to compare against.

⚠️ A bench that printed "bends towards the normal" at 0° would be
teaching `LIGHT-10` in the readout it exists to kill.

── ⚖️ THE THREE MATERIALS ARE IN INDEX ORDER, AND THAT IS THE PATTERN ─

Water 1.33, perspex 1.49, glass 1.52. Her closing sentence on the glass
note says it out loud: *"Slower material, bigger bend — that pattern
holds all the way through this topic."*

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-block · s-inout · s-ladder

⚠️ **`s-inout` TICKS AT THE GATE, BEFORE THE BENCH IS DONE.** Design's
`DONE` gives it `s.gate !== null` while `s-block` needs the gate AND a
control touched. The bench marks it through `band_anchor` / `band_at`,
the P4/P6 mechanism — `mirrors` would tick it late, and the rail manifest
derives no mirror here because her two expressions differ.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-09  the straw really does bend in water
    LIGHT-10  light bends because water is thicker and pushes it sideways
    LIGHT-11  light speeds up in glass, because glass is clearer than air
    LIGHT-12  light only slows down when it bends

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 3 and 2.
"""

LESSON = {
    "slug":  "refraction",
    "title": "Refraction",
    "discipline": "physics",
    "unit": "Light",
    "family": "PROCESS",

    "covers": ["KS3.P.LGT.04b"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["reflection-mirrors-and-scattering"],
    "assumes": [],
    "references": ["light-travels", "colour-and-the-spectrum",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "A straw in a glass of water is straight and looks "
                        "broken. The light bent; your brain assumed it had "
                        "not.",

    "big_question": "A straw in a glass of water is straight and looks "
                    "broken. Every part of that illusion is doing exactly "
                    "what it should — including your brain, which is making "
                    "the only reasonable assumption available to it.",

    "rail": [
        {"anchor": "s-hook",   "short": "STRAW",
         "label": "The broken straw",   "done_when": "committed"},
        {"anchor": "s-block",  "short": "BLOCK",
         "label": "Ray into a block",   "done_when": "gate_and_a_control"},
        {"anchor": "s-inout",  "short": "WHY",
         "label": "Why it looks broken", "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The straw that is not broken.",
        "prompt": "A straw standing in a glass of water looks snapped in two "
                  "at the surface, and the part under the water looks shorter "
                  "and shifted sideways. Lift it out and it is perfectly "
                  "straight. Nothing has been done to the straw at all.",
        "commit": "What has happened between the straw and your eye?",
        "options": [
            "The water has bent the straw",
            "The light from the submerged part changed direction as it left "
            "the water",
            "The water magnifies the lower half, so it looks a different size",
            "The surface of the water reflects the top half down onto the "
            "bottom half",
        ],
        "answer": 1,
        "reveal": "Light leaving the submerged part speeds up as it crosses "
                  "back into the air, and it changes direction as it does so. "
                  "Your brain then does the only sensible thing and assumes "
                  "the light came straight to you, which puts the lower half "
                  "of the straw somewhere it is not. The straw is straight; "
                  "the ray is the thing that bent.",
    },

    "misconceptions": [
        {"id": "LIGHT-09",
         "statement": "The straw really does bend in water.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "LIGHT-10",
         "statement": "Light bends because water is thicker and pushes it "
                      "sideways.",
         "elicited_by": "block",
         "confronted_by": "s-think"},
        {"id": "LIGHT-11",
         "statement": "Light speeds up when it enters glass, because glass is "
                      "clearer than air.",
         "elicited_by": "s-ladder",
         "confronted_by": "block"},
        {"id": "LIGHT-12",
         "statement": "Light only slows down when it bends, so a ray that "
                      "carries straight on has not changed speed.",
         "elicited_by": "block",
         "confronted_by": "block"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Light travels fastest in a vacuum, and almost as fast in "
                 "air. Send it into water, perspex or glass and it slows down "
                 "— in glass to about two thirds of its speed in air. That "
                 "slowing is the whole cause of what follows."},
        {"type": "explainer",
         "text": "If the light arrives along the normal, straight on, it "
                 "slows and carries on in the same direction. If it arrives "
                 "at an angle to the normal, one side of the beam reaches the "
                 "slower material before the other, and the beam swings "
                 "round: it <strong>bends towards the normal</strong> on the "
                 "way in. Coming out of the other side it speeds up again and "
                 "<strong>bends away from the normal</strong> by the same "
                 "amount, so the ray leaving a parallel-sided block travels "
                 "in the original direction but shifted sideways. Bending "
                 "light like this on going from one material to another is "
                 "called <strong>refraction</strong>."},
        {"type": "explainer",
         "text": "Your eye and brain assume light has come in a straight "
                 "line, because it almost always has. Refracted light breaks "
                 "that assumption, and the straw appears where the straight "
                 "line would have started rather than where it is."},

        # ── #s-block · a ray box and a rectangular block ───────────────
        {"type": "refraction-block",
         "id": "block",
         "anchor": "s-block",
         "eyebrow": "At the bench · a ray box and a rectangular block",
         "heading": "Send one ray in. Watch where it goes.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A narrow ray from a ray box enters a parallel-sided block "
                   "through its flat face, with the normal drawn in. Set the "
                   "angle it arrives at, and set what the block is made of.",
         "gate": {
             "prompt": "Commit first. A ray is aimed straight at the block, "
                       "exactly along the normal. What does it do on "
                       "entering?",
             "options": [
                 "It slows down and carries straight on",
                 "It slows down and bends towards the normal",
                 "It carries on at exactly the same speed, because it was not "
                 "bent",
                 "It bounces straight back out of the block",
             ],
             "answer": 0,
         },
         "inc": {"label": "Angle from the normal in air",
                 "min": 0, "max": 70, "step": 5, "start": 45},
         "mat_label": "What the block is",
         "normal_label": "NORMAL",
         "air_label": "AIR",
         # Design's own three, in index order, with her speeds already
         # rounded to the figures her captions quote.
         "materials": [
             {"id": "water", "label": "Water", "n": 1.33, "v": 226000000,
              "caption": "WATER — LIGHT SLOWS TO ABOUT 226 000 000 m/s",
              "note": "Water slows light the least of the three here, so it "
                      "bends the ray the least. It is also the case you meet "
                      "most: every swimming pool that looks shallower than it "
                      "is, and every fish that is not quite where it appears, "
                      "is this."},
             {"id": "perspex", "label": "Perspex", "n": 1.49, "v": 201000000,
              "caption": "PERSPEX — LIGHT SLOWS TO ABOUT 201 000 000 m/s",
              "note": "Perspex slows light more than water does and bends the "
                      "ray further at the same angle of arrival. It is the "
                      "block most often used at the bench because it is hard "
                      "to break."},
             {"id": "glass", "label": "Glass", "n": 1.52, "v": 197000000,
              "caption": "GLASS — LIGHT SLOWS TO ABOUT 197 000 000 m/s",
              "note": "Glass is the slowest here, at about two thirds of the "
                      "speed of light in air, and bends the ray the most. "
                      "Slower material, bigger bend — that pattern holds all "
                      "the way through this topic."},
         ],
         "start_mat": 2,
         "readouts": [
             {"id": "inc", "label": "Angle in the air", "sub": "from the "
              "normal"},
             {"id": "ref", "label": "Angle inside the block",
              "sub": "from the normal"},
             {"id": "speed", "label": "Speed of light inside",
              "sub": "against 300 000 000 m/s in a vacuum"},
             {"id": "verdict", "label": "What the ray does"},
         ],
         "band_anchor": "s-inout",
         "band_at": 1,
         # Two branch tails, and the zero-angle one is the load-bearing
         # state: slowing on its own bends nothing.
         "branch_tail": {
             "straight": " Your ray is aimed straight along the normal, so it "
                         "slows to about {speed} m/s and carries on in "
                         "exactly the same direction. Slowing on its own does "
                         "not bend anything; move the angle off zero and the "
                         "bending starts.",
             "bent": " Your ray arrives at {inc}° to the normal and runs "
                     "through the block at {ref}° — {delta}° closer to the "
                     "normal. It leaves the far face at {inc}° again, so it "
                     "ends up travelling in its original direction but "
                     "shifted across, which is the dashed line to compare it "
                     "with.",
         },
         "verdicts": {"straight": "Straight on, but slower",
                      "bent": "Bends towards the normal"}},

        # ── #s-inout · why the straw looks broken ─────────────────────
        {"type": "light-band",
         "id": "apparent-depth",
         "anchor": "s-inout",
         "eyebrow": "The figure",
         "heading": "Why the straw looks broken",
         "straw": {
             "aria_label": "A glass of water seen from the side. A straw runs "
                           "from above the surface down to the bottom. A ray "
                           "leaves the submerged end, bends away from the "
                           "normal as it leaves the water, and reaches an "
                           "eye. A dashed line continues that ray straight "
                           "backwards to a point higher and closer than the "
                           "real end, which is where the end appears to be.",
             "surface_label": "WATER SURFACE",
             "normal_label": "NORMAL",
             "eye_label": "EYE",
             "looks_label": "WHERE IT LOOKS",
             "is_label": "WHERE IT IS"},
         "close": "Light leaves the submerged end of the straw, speeds up as "
                  "it leaves the water and bends away from the normal. Your "
                  "eye and brain trace it back in a straight line, because "
                  "light almost always has come in a straight line — and the "
                  "straight line starts higher up and closer in than the real "
                  "end. The straw is not bent. The rule your brain is using "
                  "is."},

        {"type": "key-fact", "ref": "refraction-is-a-change-of-speed"},

        {"type": "misconception", "id": "think-the-straw-bends",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-straw-bends",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-09",
         "statements": [
             {"quote": "The straw really does bend in water.",
              "targets": "LIGHT-09",
              "body": [
                  "Lift it out and it is straight; put a ruler in and the "
                  "ruler is straight when you take it out too. Nothing "
                  "mechanical has happened. What changes is the path the "
                  "light takes from the submerged part to your eye — it bends "
                  "as it leaves the water — and your brain, which has no way "
                  "of knowing that, follows the ray backwards in a straight "
                  "line to a place the straw is not. Every trick of this kind "
                  "is the same trick: the light bent, and the assumption that "
                  "it did not is what produces the illusion.",
              ]},
             {"quote": "Light bends because water is thicker and pushes it "
                       "sideways.",
              "targets": "LIGHT-10",
              "body": [
                  "Nothing pushes it. Light slows in water because of how it "
                  "interacts with the material, and the bending follows from "
                  "the slowing plus the angle: one edge of the beam reaches "
                  "the slower material before the other, so the whole beam "
                  "swings round — the same way a trolley with one stiff wheel "
                  "veers. Send the ray in exactly along the normal and both "
                  "edges arrive together, so it slows just as much and does "
                  "not bend at all. If thickness pushed light aside, the "
                  "straight-on ray would bend too.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "refraction-is-a-change-of-speed",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Light slows down when it enters a denser transparent "
                 "material and speeds up when it leaves. Arriving along the "
                 "normal it carries straight on; arriving at an angle it "
                 "bends towards the normal on the way in and away from the "
                 "normal on the way out. That bending is refraction, and it "
                 "is why a straw in water looks broken: the eye traces the "
                 "light back in a straight line it did not take."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 2.
    "ladder": {
        "recall": {
            "q": "A ray of light passes from air into a glass block, arriving "
                 "at 40° to the normal. Which describes what happens?",
            "options": [
                "It slows down and bends away from the normal, so the angle "
                "inside the glass is more than 40°.",
                "It speeds up and bends towards the normal, because glass is "
                "clearer than air.",
                "It carries straight on and only slows down, because the "
                "block has flat parallel sides.",
                "It slows down and bends towards the normal, so the angle "
                "inside the glass is less than 40°.",
            ],
            "answer": 3,
            "feedback": {
                0: "Bending away from the normal is what happens on the way "
                   "out, when the light speeds up. Going into a slower "
                   "material, it bends towards the normal.",
                1: "Light is fastest in a vacuum and slower in any material. "
                   "Glass slows it to about two thirds of its speed in air, "
                   "and clarity is a separate matter from speed.",
                2: "Flat parallel sides mean the ray leaves travelling in "
                   "its original direction, shifted sideways. It still bends "
                   "at each face; the two bends cancel in direction, not in "
                   "position.",
            },
            "title": "Rung 1 · Apply the rule"},
        "apply": {
            "q": "A ray is aimed at a glass block exactly along the normal, "
                 "arriving straight on. What happens?",
            "options": [
                "It bends towards the normal, because all light entering "
                "glass is refracted.",
                "It carries straight on at exactly the same speed, because "
                "it has not been bent.",
                "It slows down inside the glass and carries straight on "
                "without bending.",
                "It reflects straight back out, because it hits the surface "
                "square on.",
            ],
            "answer": 2,
            "feedback": {
                0: "Refraction is a change of direction, and here there is "
                   "none. The light does slow down; it is the angle that "
                   "gives it a direction to swing towards, and at 0° there "
                   "is no angle.",
                1: "The speed always drops on entering glass, whatever the "
                   "angle. Bending is a consequence of the slowing plus an "
                   "angle, not the other way round.",
                3: "A little is always reflected at a surface, but most of "
                   "it goes in. Arriving square on is the one case with no "
                   "bending at all.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why a straw standing in a glass of water looks "
                 "broken at the surface, using the words refraction, normal "
                 "and straight line.",
            "field_label": "Your explanation",
            "placeholder": "Light leaves the part of the straw under the "
                           "water and…",
            "success": [
                "Says light leaves the submerged part of the straw and "
                "travels up to the surface.",
                "Says it speeds up as it leaves the water and bends away "
                "from the normal.",
                "Names that bending as refraction.",
                "Says the eye and brain trace the light back in a straight "
                "line.",
                "Says that straight line starts at a different place from "
                "the real end of the straw, so the submerged part appears "
                "shifted.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A swimming pool with a flat bottom always looks shallower "
                 "than it is, and the effect is stronger when you look at the "
                 "far end of the pool than when you look straight down at "
                 "your feet. Explain both parts.",
            "field_label": "Your answer",
            "placeholder": "Light from the bottom of the pool…",
            "success": [
                "Says light from the bottom of the pool bends away from the "
                "normal as it leaves the water.",
                "Says the eye traces the light back in a straight line to a "
                "point higher than the real bottom.",
                "Says that makes the bottom appear closer to the surface, so "
                "the pool looks shallower.",
                "Says looking straight down means the light leaves along the "
                "normal, or close to it.",
                "Says light along the normal is not bent, so the effect is "
                "smallest looking straight down and grows as the angle "
                "grows.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Light slows down on entering a denser transparent material "
                "and speeds up on leaving it. Arriving along the normal it "
                "carries straight on; arriving at an angle it bends towards "
                "the normal going in and away from the normal coming out. "
                "That change of direction is refraction. Because the eye "
                "traces light back in a straight line, refracted light makes "
                "objects appear where they are not: a straw looks broken and "
                "a pool looks shallower than it is.",

    "stretch": [
        {"id": "total-internal-reflection",
         "type": "explainer",
         "text": "Push the angle far enough going the other way — from glass "
                 "or water out into air — and the bending runs out of room. "
                 "Past a certain angle the ray cannot escape at all and is "
                 "reflected back inside instead, which is called total "
                 "internal reflection. It is what makes an optical fibre "
                 "work: light fired into a thin glass thread keeps striking "
                 "the inside of the wall at a steep angle and keeps bouncing "
                 "back in, all the way along, even round bends. Almost all "
                 "long-distance internet traffic is doing that at this "
                 "moment."},
        {"id": "refraction-depends-on-colour",
         "type": "explainer",
         "text": "Refraction also depends slightly on colour, because the "
                 "different colours in white light travel at slightly "
                 "different speeds in glass. Blue is slowed a little more "
                 "than red and so bends a little more, and a triangular block "
                 "turns that tiny difference into a spread of colours across "
                 "a wall."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "refraction",
         "definition": "The change of direction of light when it crosses "
                       "from one material into another at an angle, caused by "
                       "the change in its speed."},
        {"term": "normal",
         "definition": "The line at right angles to the surface where the ray "
                       "meets it. Both angles are measured from it."},
        {"term": "denser",
         "definition": "Used here of a transparent material that slows light "
                       "more. Glass slows it more than water does."},
    ],

    "tutor": {
        "anchor": "s-block",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a ray, an angle and a material, and want to know where "
                "it goes?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Ray diagrams for refraction at a boundary, the refractive "
                   "index, total internal reflection and the critical angle, "
                   "and optical fibres.",

    "convention_note": "The bench is a teaching model. The angles are "
                       "calculated and drawn to scale for a typical sample of "
                       "each material with light of an average visible "
                       "colour; real values shift slightly with the colour of "
                       "the light and with the exact composition of the glass "
                       "or perspex. Speeds are rounded. Some light is "
                       "reflected at every surface as well as refracted, and "
                       "the drawing leaves that out to keep one ray to "
                       "follow. The block is treated as having exactly "
                       "parallel faces, which is what makes the emerging ray "
                       "parallel to the original. In the straw figure the "
                       "angles are not to scale: the ray leaving the water is "
                       "drawn much flatter than water really bends it, so "
                       "that the bend and the line your brain draws back can "
                       "both be seen on one small picture. The bench above is "
                       "the one to measure.",

    "ws": ["measurement"],
}
