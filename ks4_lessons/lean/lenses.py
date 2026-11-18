# -*- coding: utf-8 -*-
"""Lenses, in the lean shape. LEGACY record: the Design batch-2 page keeps its ladder (Ks4Ladder)
and practice set, so their question ids survive. Spec table: ks4-lenses.md (AQA 8463 4.6.2.5,
physics only, all tiers). TF TH only.

The practice set reads the route's quiz list (K.bank), and Rung 1 is the quiz item whose stem
contains "magnifying glass" (K.find): that stem is kept verbatim, and no other quiz stem says
"magnifying glass".

Figures: focusFig (the two lens symbols, the principal focus and the focal length) is drawn by the
page always. benchFig and buildFig drew only through the (removed) lens bench and ray-diagram
builder, so logic_edits fix each to one finished ray diagram: benchFig = convex lens, object
15 cm away, between F and 2F (real, magnified image); buildFig = convex lens, object 6 cm away inside F (the
magnifying glass, virtual image). A concave lens image needs a new figure: fig:concave-lens-image
(BRIEF-WAVES.md, Figures wanted). The lens symbols in lensSym() are AQA's: a line with arrowheads
pointing outwards for convex and inwards for concave (to be checked against 8463 p65 by the
examiner). "as on the equation sheet" is right here: magnification is on the sheet."""

LESSON = {
    "slug": "lenses",
    "start": {
        "setup": "You look at a window across the room through a magnifying glass held at arm's "
                 "length.",
        "question": "If you had to guess, is the window the right way up or upside down?",
        "options": [
            ("The right way up",
             "Upside down, and smaller. The same lens held close to a page makes the words "
             "bigger and the right way up."),
            ("Upside down",
             "Upside down, and smaller. The same lens held close to a page makes the words "
             "bigger and the right way up."),
        ],
        "answer": 1,
    },
    "words": ["convex lens", "concave lens", "principal focus", "focal length"],
    "knowledge": [
        {"kind": "card", "title": "How a lens works",
         "body": ["A lens forms an image by refracting light.",
                  {"points": [
                      "A convex lens is thicker in the middle. It brings rays of light together.",
                      "A concave lens is thinner in the middle. It spreads rays of light apart.",
                  ]}]},
        {"kind": "card", "title": "The principal focus",
         "body": ["In a convex lens, parallel rays of light are brought to a focus at the "
                  "principal focus. The distance from the lens to the principal focus is called "
                  "the focal length.",
                  "A concave lens spreads parallel rays apart. They seem to come from a principal "
                  "focus on the side the light comes from.",
                  {"slot": "legacy-fig:focusFig"},
                  "The figure shows the symbol for each lens that you use in ray diagrams."]},
        {"kind": "card", "title": "A ray diagram for a convex lens",
         "body": ["F is the principal focus. 2F is twice the focal length from the lens.",
                  {"points": [
                      "Ray 1 leaves the top of the object parallel to the axis. After the lens it "
                      "passes through the principal focus.",
                      "Ray 2 leaves the top of the object and passes straight through the centre "
                      "of the lens without bending.",
                      "Ray 3, if you need it, passes through F on the object's side. After the "
                      "lens it travels parallel to the axis.",
                      "The top of the image is where the rays meet.",
                  ]},
                  {"slot": "legacy-fig:benchFig"},
                  "Here the object is between F and 2F, so the image is real, inverted and "
                  "magnified."]},
        {"kind": "reveal", "title": "Where the object is, and the image you get",
         "cols": ["The image from a convex lens"],
         "rows": [
             ("Object beyond 2F", "Real, inverted, diminished"),
             ("Object at 2F", "Real, inverted, the same size"),
             ("Object between F and 2F", "Real, inverted, magnified"),
             ("Object at F", "No image: the rays leave the lens parallel"),
             ("Object between F and the lens", "Virtual, upright, magnified"),
         ]},
        {"kind": "card", "title": "Real and virtual images",
         "body": [{"points": [
             "A real image forms where rays of light really meet. It can be shown on a screen.",
             "A virtual image forms where rays only seem to come from. It cannot be shown on a "
             "screen.",
         ]},
             "The image produced by a convex lens can be either real or virtual. With the object "
             "inside F, the rays spread apart after the lens. Traced back as dashed lines, they "
             "meet on the object's side: this is how a magnifying glass works.",
             {"slot": "legacy-fig:buildFig"}]},
        {"kind": "card", "title": "Concave lenses",
         "body": ["The image produced by a concave lens is always virtual.",
                  "It is upright and diminished, on the same side of the lens as the object.",
                  {"slot": "fig:concave-lens-image"}]},
        {"kind": "card", "title": "Magnification",
         "body": ["magnification = image height ÷ object height",
                  "Magnification is a ratio and so has no units.",
                  "Image height and object height should both be measured in either mm or cm.",
                  "This equation is on the equation sheet.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Magnification is measured in cm.",
              "Magnification is a ratio, so it has no units."),
             ("An image 2.6 cm tall from an object 4.0 mm tall: 2.6 ÷ 4.0.",
              "Put both heights in the same unit first: 26 mm ÷ 4.0 mm."),
             ("A concave lens can form a real image.",
              "The image produced by a concave lens is always virtual."),
         ]}]},
    ],
    "key_fact": "A lens forms an image by refracting light. A convex lens brings parallel rays to "
                "a focus at the principal focus, and the distance from the lens to the principal "
                "focus is the focal length. A convex lens can form a real or a virtual image, a "
                "concave lens always forms a virtual image, and magnification = image height ÷ "
                "object height.",
    "deeper": [
        {"kind": "card", "title": "Investigating magnification",
         "body": ["Use a convex lens to form a sharp image of a lamp on a screen. Measure the image "
                  "height and the object height, then calculate the magnification.",
                  "Repeat with a range of convex lenses."]},
        {"kind": "card", "title": "Other names",
         "body": ["A convex lens is also called a converging lens. A concave lens is also called a "
                  "diverging lens."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Complete</strong> a ray diagram: use a ruler, draw two rays from the top of "
             "the object, and put an arrow on each.",
             "<strong>Compare</strong> convex and concave lenses: say what each does to rays, and "
             "the kind of image each forms.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-2",
        "logic_edits": [
            ("benchFig: ready ? K.fig(this.scene(lens, u, { rays: shown ? [1, 2, 3] : [], "
             "showImg: shown, anim: shown }), '') : null,",
             "benchFig: ready ? K.fig(this.scene('cx', 15, { rays: [1, 2, 3], showImg: true, "
             "anim: false }), '') : null,"),
            ("buildFig: ready ? K.fig(this.scene('cx', figStep.u, { rays: figStep.rays, showImg: "
             "figStep.showImg, anim: false, extra: cExtra }), '') : null,",
             "buildFig: ready ? K.fig(this.scene('cx', 6, { rays: [1, 2, 3], showImg: true, "
             "anim: false }), '') : null,"),
        ],
    },
}
