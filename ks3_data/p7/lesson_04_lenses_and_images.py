"""P7 L4 — Lenses and images (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-04-lenses-and-images.dc.html`.

Her page wins outright. The shoebox hook, the three-control pinhole
bench, the two lens diagrams and all four rungs are hers.

── ⚖️ HER FLAG 4 · THIS PAGE COMPUTES AND CARRIES NO BLOCK ──────────

`h_image = h_object × (v ÷ u)` is a genuine product and would take a
triangle cleanly. She leaves it out for two reasons and states both:
`LGT.04` says *qualitative* for the convex lens, the pinhole clause
carries no arithmetic at all, and a triangle over three lengths invites
MAGNIFICATION, which is GCSE. The bench prints its working in the
readout's sub-line instead — `300 mm × v ÷ u`, line by line.

**"This is the one place in the two units where a reviewer might
reasonably want a block that is not there."** Her sentence, passed
through unresolved. It is Mide's call, not a lane's.

── ⚖️ RULED · THE HOLE WIDTH DOES NOT MOVE THE PICTURE HEIGHT, AND THE
      NOTE SAYS SO IN EVERY STATE ─────────────────────────────────────

`LIGHT-14` is *a bigger hole makes a bigger picture*, and the bench is
built to kill it: all three hole notes quote the live picture height and
say in terms that it did not change. A bench that only reported the blur
would leave the belief standing, because a student would see something
grow and attribute it to the control they moved.

⚠️ **THE BLUR IS THE STROKE WIDTH OF THE PICTURE ARROW**, to the same
scale as the heights, with a two-pixel minimum so the sharpest setting
still draws. Two channels: the drawn thickness and the millimetre
reading beside it.

── ⚖️ THE TWO ARROW HEIGHTS ARE TO ONE SCALE; THE AXIS IS NOT ────────

Her drawing says so on its own face — *"DISTANCES ALONG THE AXIS ARE
COMPRESSED — THE TWO ARROW HEIGHTS ARE TO ONE SCALE"* — and the hole is
placed along the axis at `OX + (IX − OX) / (1 + v/u)` so that the drawn
rays stay straight at any ratio. The ratio between the arrows is
therefore exactly right and the distances are not, which is the only way
to fit 2000 mm and 50 mm on one line.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-camera · s-lens · s-ladder

⚠️ **`s-lens` TICKS AT THE GATE.** Marked by the bench through
`band_anchor` / `band_at`, as on `p7-03`.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-13  the pinhole flips the picture, so a lens flips it back
    LIGHT-14  a bigger hole makes a bigger picture
    LIGHT-15  a longer box spreads the light out, so the picture shrinks
    LIGHT-16  a wider hole cannot blur it, because light goes in straight
              lines

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 1 and 0.

⊕ **HER `verdict` STRING IS COMPUTED AND NEVER DISPLAYED.** Design's
`lessonVals()` builds `verdict` — "sharp, and dim" / "a working
compromise" / "bright, and blurred" — and her fourth tile prints the
fixed sentence "Upside down, and left for right" instead. Recorded in
the run report as a notes-vs-drawing finding; the drawing was measured
and the tile is hers.
"""

LESSON = {
    "slug":  "lenses-and-images",
    "title": "Lenses and images",
    "discipline": "physics",
    "unit": "Light",
    "family": "MODEL",

    "covers": ["KS3.P.LGT.04c"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["refraction"],
    "assumes": [],
    "references": ["light-travels", "waves-on-water"],
    "ks4_links": [],

    "meta_description": "A hole in a box makes a picture and makes a bad "
                        "bargain doing it: sharp or bright, never both. A "
                        "lens refuses the bargain.",

    "big_question": "A hole in a box makes a picture, and it makes a bad "
                    "bargain doing it: sharp or bright, never both. A lens is "
                    "the piece of glass that refuses the bargain.",

    "rail": [
        {"anchor": "s-hook",   "short": "PINHOLE",
         "label": "A box with a pin-prick", "done_when": "committed"},
        {"anchor": "s-camera", "short": "CAMERA",
         "label": "Pinhole camera",        "done_when": "gate_and_a_control"},
        {"anchor": "s-lens",   "short": "LENS",
         "label": "What a lens does",      "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A box with a pin-prick in it shows you the world upside "
                 "down.",
        "prompt": "Take a shoebox, make one clean pin-prick in one end and "
                  "stretch greaseproof paper across the other. Point the "
                  "pin-prick at a bright window. A picture of the window "
                  "appears on the paper, in colour, and it is upside down and "
                  "the wrong way round.",
        "commit": "There is no lens, no glass and nothing electrical in the "
                  "box. Why is the picture inverted?",
        "options": [
            "The hole turns the light round as it squeezes through",
            "Light from the top of the window is heading downwards as it "
            "reaches the hole, and keeps going downwards",
            "The greaseproof paper shows the picture from behind, so it looks "
            "reversed both ways at once",
            "The light bounces off the inside of the box before it lands",
        ],
        "answer": 1,
        "reveal": "Straight lines, and nothing else. To get through the hole "
                  "at all, light from the top of the window has to be "
                  "travelling downwards — so it carries on downwards and "
                  "lands low on the screen. Light from the bottom is "
                  "travelling upwards and lands high. The two cross at the "
                  "hole, and everything in between crosses with them.",
    },

    "misconceptions": [
        {"id": "LIGHT-13",
         "statement": "The pinhole flips the picture over, so a lens must "
                      "flip it back.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "LIGHT-14",
         "statement": "A bigger hole makes a bigger picture.",
         "elicited_by": "s-ladder",
         "confronted_by": "camera"},
        {"id": "LIGHT-15",
         "statement": "A longer box spreads the light out, so the picture "
                      "gets smaller.",
         "elicited_by": "camera",
         "confronted_by": "camera"},
        {"id": "LIGHT-16",
         "statement": "A wider hole cannot blur the picture, because light "
                      "travels in straight lines.",
         "elicited_by": "s-ladder",
         "confronted_by": "lens-pair"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Light travels in straight lines, and every point on a "
                 "bright object throws light out in every direction. The hole "
                 "is what makes the picture: out of the whole spray of light "
                 "leaving the top of the window, only the one ray aimed at "
                 "the hole gets through, and it carries on in a straight line "
                 "to a single place on the screen. Because it was heading "
                 "downwards to reach the hole, it keeps heading downwards "
                 "afterwards, and lands near the bottom. Light from the "
                 "bottom of the window does the reverse. The rays cross at "
                 "the hole, and the picture arrives inverted."},
        {"type": "explainer",
         "text": "A pinhole camera has one problem, and it is a trap you "
                 "cannot get out of. A smaller hole picks out one ray per "
                 "point and gives a sharp picture, but lets very little light "
                 "through, so the picture is dim. A bigger hole lets more "
                 "light through and is brighter, but now a whole small bundle "
                 "of rays gets through from each point and lands as a patch "
                 "rather than a point, so the picture blurs."},
        {"type": "explainer",
         "text": "A <strong>convex lens</strong> — one that bulges outwards — "
                 "breaks the trap. It refracts every ray in the bundle by "
                 "just the right amount to bring them all back together at "
                 "one place, so a wide opening can be used and the picture is "
                 "bright <em>and</em> sharp. A pinhole selects one ray and "
                 "throws the rest away; a lens collects them and puts them "
                 "back together. That is what <strong>focusing</strong> "
                 "means."},

        # ── #s-camera · a pinhole camera and a lit object 300 mm tall ──
        {"type": "pinhole-camera",
         "id": "camera",
         "anchor": "s-camera",
         "eyebrow": "At the bench · a pinhole camera and a lit object 300 mm "
                    "tall",
         "heading": "Three things to change. Two of them fight each other.",
         "head_counter": {"format": "All three controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A lit object 300 mm tall in front of a box with one hole "
                   "in it and a screen at the back. Set how far away the "
                   "object is, how long the box is, and how wide the hole is.",
         "gate": {
             "prompt": "Commit first. The box is made twice as long and "
                       "nothing else is touched. What happens to the picture "
                       "on the screen?",
             "options": [
                 "The picture is twice as tall, and dimmer",
                 "The picture is half as tall, and brighter",
                 "The picture is the same size and sharper",
                 "The picture is twice as tall and twice as bright",
             ],
             "answer": 0,
         },
         "object_mm": 300,
         "u": {"label": "How far away the object is",
               "min": 200, "max": 2000, "step": 100, "start": 600},
         "v": {"label": "How long the box is",
               "min": 50, "max": 300, "step": 25, "start": 150},
         "hole_label": "How wide the hole is",
         "holes": [
             {"id": "h03", "label": "0.3 mm", "d": 0.3,
              "note": "The narrowest hole picks out very nearly one ray from "
                      "each point of the object, so the picture is as sharp "
                      "as this camera gets: {blur} mm of blur across a "
                      "picture {img} mm tall. It is also the darkest setting "
                      "there is. Widen the hole to 3 mm and about a hundred "
                      "times as much light comes in — and the blur goes to "
                      "{blurwide} mm, while the picture height stays at {img} "
                      "mm."},
             {"id": "h1", "label": "1 mm", "d": 1,
              "note": "A 1 mm hole lets in about eleven times the light of "
                      "the narrowest one and blurs each point over {blur} mm "
                      "on a picture {img} mm tall. That is the trade this "
                      "camera cannot escape, and it is why lenses exist. Note "
                      "that neither hole setting moved the picture height: "
                      "only the {u} mm to the object and the {v} mm box "
                      "length do that."},
             {"id": "h3", "label": "3 mm", "d": 3,
              "note": "The widest hole lets in about a hundred times the "
                      "light of the narrowest, and pays for it: each point of "
                      "the object now lands as a patch {blur} mm across on a "
                      "picture only {img} mm tall, which is {pct}% of the "
                      "whole picture height. The height itself has not "
                      "changed at all — close the hole back to 0.3 mm and it "
                      "is still {img} mm."},
         ],
         "start_hole": 1,
         "object_label": "OBJECT 300 mm TALL",
         "screen_label": "SCREEN",
         "axis_note": "DISTANCES ALONG THE AXIS ARE COMPRESSED — THE TWO "
                      "ARROW HEIGHTS ARE TO ONE SCALE",
         "readouts": [
             {"id": "img", "label": "Picture height on the screen", "sub": "—"},
             {"id": "blur", "label": "How blurred each point is", "sub": "—"},
             {"id": "bright", "label": "How much light gets in",
              "sub": "against the narrowest hole"},
             {"id": "updown", "label": "Which way up",
              "value": "Upside down, and left for right",
              "sub": "at every setting"},
         ],
         "band_anchor": "s-lens",
         "band_at": 1},

        # ── #s-lens · what a convex lens does that a hole cannot ──────
        {"type": "light-band",
         "id": "lens-pair",
         "anchor": "s-lens",
         "eyebrow": "The figure",
         "heading": "What a convex lens does that a hole cannot",
         "pair": [
             {"id": "focus", "shape": "focus",
              "title": "Parallel rays, brought to one point",
              "aria_label": "Five parallel rays arriving at a lens that "
                            "bulges on both sides. Each is refracted and all "
                            "five cross at a single point beyond it, marked "
                            "as the focus.",
              "focus_label": "FOCUS",
              "body": "Every ray is refracted twice, going in and coming out, "
                      "and the shape of the glass is chosen so that all of "
                      "them arrive at the same place. The wider the lens, the "
                      "more light it gathers — and the picture stays sharp."},
             {"id": "image", "shape": "image",
              "title": "An object, and its picture",
              "aria_label": "An upright arrow on the left, three rays leaving "
                            "its tip and passing through a lens, meeting "
                            "again on the right where an inverted arrow is "
                            "drawn on a screen.",
              "body": "All the light leaving one point of the object and "
                      "passing anywhere through the lens is brought back to "
                      "one point on the screen. The rays still cross, so the "
                      "picture is still upside down — a lens fixes the "
                      "brightness and the sharpness, not the inversion."},
         ],
         "close": "A pinhole throws away almost all the light in order to be "
                  "sharp. A lens keeps it and puts it back in the right "
                  "place. That is the whole reason eyes and cameras have "
                  "lenses in them and not pin-pricks."},

        {"type": "key-fact", "ref": "pinhole-and-lens"},

        {"type": "misconception", "id": "think-the-pinhole-flips",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-pinhole-flips",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-13",
         "statements": [
             {"quote": "The pinhole flips the picture over, so a lens must "
                       "flip it back.",
              "targets": "LIGHT-13",
              "body": [
                  "Nothing does any flipping. The rays from the top of the "
                  "object are travelling downwards when they reach the hole, "
                  "so they carry on downwards afterwards and land low on the "
                  "screen; the rays from the bottom are travelling upwards "
                  "and land high. The inversion is just where straight lines "
                  "go. A lens changes how much light gets through and where "
                  "it lands, and does nothing about that crossing — which is "
                  "why the picture inside a camera and the picture on the "
                  "back of your eye are both upside down.",
              ]},
             {"quote": "A bigger hole makes a bigger picture.",
              "targets": "LIGHT-14",
              "body": [
                  "It makes a brighter and blurrier one, and leaves the size "
                  "exactly where it was. Only two things set the size: how "
                  "far away the object is, and how long the box is. The bench "
                  "above will show you — change the hole from the narrowest "
                  "to the widest and the picture height reading does not move "
                  "at all, while the blur reading grows tenfold. Size and "
                  "sharpness are set by different controls, and the commonest "
                  "way to get this wrong is to assume that the one you can "
                  "see changing is the one doing the work.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "pinhole-and-lens",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Light travels in straight lines, so the rays from the top "
                 "and bottom of an object cross at a pinhole and the picture "
                 "on the screen is upside down. A narrow hole gives a sharp "
                 "but dim picture and a wide one a bright but blurred "
                 "picture. A convex lens refracts all the rays from one point "
                 "of the object back to one point on the screen, so a wide "
                 "opening can be both bright and sharp — but the rays still "
                 "cross, so the picture is still inverted."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 0.
    "ladder": {
        "recall": {
            "q": "A pinhole camera gives a picture 40 mm tall. The box is "
                 "then made twice as long, with the object left exactly where "
                 "it was. What is the new picture height?",
            "options": [
                "20 mm — a longer box spreads the light further, so the "
                "picture shrinks",
                "80 mm",
                "40 mm — the box length does not affect the size, only the "
                "brightness",
                "160 mm — doubling the length doubles both the height and "
                "the width, so the picture is four times as big",
            ],
            "answer": 1,
            "feedback": {
                0: "The rays keep going in straight lines from the hole, so "
                   "they get further apart the further they travel. Twice "
                   "the distance means twice the separation, and twice the "
                   "height.",
                2: "Box length is one of the two things that set the size. "
                   "What it also does is spread the same light over a bigger "
                   "picture, so the picture does get dimmer as well.",
                3: "Four times the area, but the question asked for the "
                   "height, and the height simply doubles.",
            },
            "title": "Rung 1 · Apply the rule"},
        "apply": {
            "q": "A pinhole picture is too dim to see clearly, so a student "
                 "widens the hole. Which statement is right?",
            "options": [
                "More light gets in and the picture brightens, but each "
                "point of the object now lands as a patch instead of a "
                "point, so it blurs — and its size does not change.",
                "The picture gets brighter and bigger, because a bigger hole "
                "lets through a bigger view.",
                "The picture gets brighter and stays exactly as sharp, "
                "because light still travels in straight lines, and a "
                "straight line from a point can only ever land in one "
                "place.",
                "Nothing changes, because the same object is sending out the "
                "same amount of light.",
            ],
            "answer": 0,
            "feedback": {
                1: "Size is set by the object distance and the box length. "
                   "Widening the hole changes how much light comes through "
                   "each point of the picture, not where the picture lands.",
                2: "Light does still travel in straight lines, and that is "
                   "the problem: a whole bundle of straight rays from one "
                   "point now gets through, and they land in slightly "
                   "different places.",
                3: "The object is, and the hole decides how much of it gets "
                   "in. Widen the hole from 0.3 mm to 3 mm and about a "
                   "hundred times as much light comes through.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why the picture in a pinhole camera is upside down, "
                 "using the idea that light travels in straight lines.",
            "field_label": "Your explanation",
            "placeholder": "Light leaves the top of the object in all "
                           "directions, but…",
            "success": [
                "Says each point of the object sends light out in all "
                "directions.",
                "Says only the ray aimed at the hole gets through from each "
                "point.",
                "Says the ray from the top of the object is travelling "
                "downwards as it reaches the hole.",
                "Says it carries straight on and lands near the bottom of "
                "the screen, and the ray from the bottom does the reverse.",
                "Says the rays cross at the hole, which is why the whole "
                "picture is inverted.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Eyes and cameras could have been built with a pinhole "
                 "instead of a lens, and none of them are. Explain what a "
                 "convex lens gives them that a pinhole cannot, and name one "
                 "thing that stays the same either way.",
            "field_label": "Your answer",
            "placeholder": "A pinhole has to be narrow to be sharp, which "
                           "means…",
            "success": [
                "Says a pinhole has to be narrow to be sharp, and a narrow "
                "hole lets in very little light.",
                "Says a wide hole is bright but blurred, so a pinhole cannot "
                "be both.",
                "Says a convex lens refracts all the rays from one point of "
                "the object back to a single point.",
                "Says that lets a wide opening be used, so the picture is "
                "bright and sharp at the same time.",
                "Says the picture is still upside down, because the rays "
                "still cross.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Light travels in straight lines, so rays from the top and "
                "bottom of an object cross at a pinhole and the picture on "
                "the screen is inverted. Its size is set by how far away the "
                "object is and how long the box is, and by nothing else. A "
                "narrow hole is sharp and dim; a wide one is bright and "
                "blurred. A convex lens refracts all the rays leaving one "
                "point of the object back to a single point on the screen, so "
                "a wide opening gives a picture that is bright and sharp at "
                "once — and still upside down.",

    "stretch": [
        {"id": "two-answers-to-one-focusing-problem",
         "type": "explainer",
         "text": "Where the picture lands depends on how far away the object "
                 "is, which is a problem for anything that has to look at "
                 "near and far things with the same lens. A camera solves it "
                 "by moving the lens backwards and forwards until the picture "
                 "falls exactly on the sensor. Your eye cannot do that, "
                 "because the retina is a fixed distance behind the lens, so "
                 "it changes the lens instead: a ring of muscle squeezes the "
                 "lens fatter to look at something close and lets it go "
                 "thinner for something far away. The same job, two "
                 "completely different engineering answers, and the fact that "
                 "reading for hours is tiring is a muscle in your eye "
                 "complaining."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "convex lens",
         "definition": "A lens that bulges outwards and brings the rays from "
                       "one point of an object back together at one point."},
        {"term": "focusing",
         "definition": "Bringing all the light that left one point of an "
                       "object back to a single point on the screen."},
        {"term": "inverted",
         "definition": "Upside down, and left for right. Any picture made by "
                       "rays crossing is inverted."},
    ],

    "tutor": {
        "anchor": "s-camera",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a pinhole camera to work out the picture size for?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Ray diagrams for converging and diverging lenses, focal "
                   "length and magnification, real and virtual images, and "
                   "correcting short and long sight.",

    "convention_note": "The bench is a teaching model. The two arrow heights "
                       "are drawn to one scale, so the ratio between the "
                       "picture and the object is exactly right; distances "
                       "along the axis are compressed to fit the width, and "
                       "the hole is placed so that the drawn rays remain "
                       "straight. The blur is drawn as the thickness of the "
                       "picture arrow, to the same scale as the heights, with "
                       "a minimum thickness so that the sharpest setting "
                       "still draws. Brightness is quoted as a comparison "
                       "with the narrowest hole and follows the area of the "
                       "hole, which ignores losses in the box and the "
                       "spreading of the picture over a larger screen. The "
                       "object is treated as evenly lit and 300 mm tall "
                       "throughout, and the screen as a flat surface at the "
                       "back of the box.",

    "ws": ["measurement"],
}
