"""P7 L5 — The eye and the camera (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-05-the-eye-and-the-camera.dc.html`.

Her page wins outright. The dark-room hook, the two-instrument bench, the
five-job table and all four rungs are hers.

── ⚖️ HER FLAG 8 · ONE BENCH, TWO INSTRUMENTS, AND IT IS DELIBERATE ──

An eye and a camera, switched by a toggle that redraws the whole
cross-section — the body, the opening, the lens, the back surface and the
inverted picture arrow. It brushes against "one practical per bench" and
she says why it stands: **the comparison IS the lesson**, the toggle
names which instrument is drawn, and a student is never left with two
answers to *describe the apparatus*. Built as drawn. She asks a reviewer
to ratify it or ask for two figures instead; that is Mide's call.

── ⚖️ RULED · EVERY BRANCH NAMES BOTH OPENINGS AT THE SAME LIGHT LEVEL ─

Her note for the eye quotes the camera's aperture at the same brightness,
and the camera's quotes the pupil. Without that the bench would be two
independent readings and the comparison — the whole point — would be left
for the student to make from memory of a state they can no longer see.

── ⚖️ SAFEGUARDING, IN THE RULED SLOT ───────────────────────────────

The eye is the student's own body, retinal damage is painless at the time
and does not heal, and the hard prohibition — never the Sun, never a
welding arc, never a laser — stays where Design put it, on the page. The
block goes through the engine's `safeguarding_note`: one quiet
`.ks3-legal` foot line above the legal line, NEVER a callout, which is
the treatment §8.10 rules for it.

⚠️ **THE NUMBER IS NOT TAKEN UP.** Childline, 0800 1111, free,
confidential, open at any hour, no name needed — the same service and the
same digits the B5 and P6 lessons already carry. This closes the third of
the three pages Design's audit finding 6.4 names; `p6-08` and `p6-09` are
P6's and are already live.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-eye · s-parts · s-ladder

⚠️ **`s-parts` TICKS AT THE GATE.** Marked by the bench through
`band_anchor` / `band_at`.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-17  your eyes send something out in order to see
    LIGHT-18  in a dark room your pupils open, and that is why you can see
    LIGHT-19  the retina focuses the light, the way a lens does
    LIGHT-20  a camera's shutter does the same job as the iris

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 2 and 3.
"""

LESSON = {
    "slug":  "the-eye-and-the-camera",
    "title": "The eye and the camera",
    "discipline": "physics",
    "unit": "Light",
    "family": "SYSTEM",

    "covers": ["KS3.P.LGT.04d", "KS3.P.LGT.05"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["lenses-and-images"],
    "assumes": [],
    "references": ["why-things-look-coloured", "the-photosynthesis-reaction",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "An eye and a camera have the same five parts doing "
                        "the same five jobs. That is not a coincidence — it "
                        "is what the physics of light leaves you.",

    "big_question": "Two instruments, built four hundred million years apart "
                    "by completely different processes, and they have the "
                    "same five parts doing the same five jobs. That is not a "
                    "coincidence — it is what the physics of light leaves "
                    "you.",

    "rail": [
        {"anchor": "s-hook",   "short": "DARK",
         "label": "Waiting in the dark",  "done_when": "committed"},
        {"anchor": "s-eye",    "short": "BENCH",
         "label": "Eye and camera",       "done_when": "gate_and_a_control"},
        {"anchor": "s-parts",  "short": "PARTS",
         "label": "Same jobs, two parts", "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Walk into a dark room and you cannot see. Wait a minute and "
                 "you can.",
        "prompt": "Nothing in the room has changed. No lamp has been switched "
                  "on, no curtain opened. The same very small amount of light "
                  "is arriving as when you walked in.",
        "commit": "What has changed in the minute you waited?",
        # ⊕ MRB-297, 1 Sep 2026 — distractor 3 widened. The correct option
        # was the longest by 5, which is a tell below the gate's constant
        # as well as at it. The balance now holds at 1.
        "options": [
            "Your pupils have opened wider, and that is the whole of it",
            "Your pupils opened, and the retina itself has also become far "
            "more sensitive",
            "Your eyes have started sending out a little light of their own",
            "Your brain has learned the shape of the whole room and is "
            "filling in the rest",
        ],
        "answer": 1,
        "reveal": "Two things happen and they are wildly different sizes. The "
                  "pupil widens within a second or so, letting in perhaps ten "
                  "times as much light. Then, over several minutes, the "
                  "pigment in the rod cells of your retina rebuilds after "
                  "being bleached by the daylight outside, and a fully "
                  "dark-adapted eye is thousands of times more sensitive than "
                  "one that has just come in. A camera can copy the first and "
                  "has nothing to match the second.",
    },

    "misconceptions": [
        {"id": "LIGHT-17",
         "statement": "Your eyes send something out in order to see.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "LIGHT-18",
         "statement": "In a dark room your pupils open, and that is why you "
                      "can eventually see.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "LIGHT-19",
         "statement": "The retina focuses the light, the way a lens does.",
         "elicited_by": "s-ladder",
         "confronted_by": "eye-camera-parts"},
        {"id": "LIGHT-20",
         "statement": "A camera's shutter does the same job as the iris.",
         "elicited_by": "s-ladder",
         "confronted_by": "eye-camera-parts"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An eye and a camera are built to do the same job with the "
                 "same physics. Light from a source — the Sun, a lamp, a "
                 "screen — reflects off the things around you and some of it "
                 "arrives at an opening. A <strong>convex lens</strong> "
                 "behind that opening refracts the rays so that all the light "
                 "from one point of the scene lands at one point at the back. "
                 "There, something <strong>photosensitive</strong> — "
                 "sensitive to light — absorbs it."},
        {"type": "explainer",
         "text": "This is where the energy goes. Light carries energy from a "
                 "source to an absorber, and at the absorber it does "
                 "something. In your <strong>retina</strong> it is absorbed "
                 "by pigment molecules in the rod and cone cells and causes a "
                 "<strong>chemical</strong> change in them, which sets off an "
                 "electrical signal along the optic nerve. In a camera it is "
                 "absorbed by a sensor and produces an "
                 "<strong>electrical</strong> signal directly. Older cameras "
                 "used film, where the light caused a chemical change in "
                 "silver compounds — the same effect as in the eye, kept "
                 "rather than sent on."},
        {"type": "explainer",
         "text": "The two also do the same two adjustments in different ways. "
                 "Both control how much light gets in — the eye with the "
                 "<strong>iris</strong> opening and closing the "
                 "<strong>pupil</strong>, the camera with an adjustable "
                 "<strong>aperture</strong>. And both keep the picture in "
                 "focus — the camera by moving its lens, the eye by changing "
                 "the shape of its own."},

        # ── #s-eye · the same scene, two instruments ──────────────────
        {"type": "eye-camera",
         "id": "eye",
         "anchor": "s-eye",
         "eyebrow": "At the bench · the same scene, two instruments",
         "heading": "One scene. Two ways of catching it.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "The same scene at the same brightness, looked at by an "
                   "eye and by a camera. Choose which one you are looking "
                   "inside, and set how bright it is.",
         "gate": {
             "prompt": "Commit first. You step from bright sunlight into a "
                       "dim room. What does the pupil of your eye do, and "
                       "why?",
             "options": [
                 "It opens wider, to let more of the little light there is "
                 "reach the retina",
                 "It closes down, to protect the retina from the change",
                 "It stays the same size, and the lens changes shape instead",
                 "It opens wider, so the eye can send more light out into the "
                 "room",
             ],
             "answer": 0,
         },
         "sys_label": "Which instrument",
         "light_label": "How bright the scene is",
         "scene_label": "THE SCENE",
         # Design's own five light levels, with a typical pupil diameter and
         # a typical aperture width in millimetres at each.
         "levels": [
             {"id": "night", "label": "A moonless night",
              "lux": "about 0.001 lux", "eye": 8.0, "cam": 50},
             {"id": "dim", "label": "A dim room",
              "lux": "about 20 lux", "eye": 6.0, "cam": 25},
             {"id": "indoor", "label": "An indoor room",
              "lux": "about 300 lux", "eye": 4.5, "cam": 12},
             {"id": "overcast", "label": "An overcast day",
              "lux": "about 5000 lux", "eye": 3.0, "cam": 6},
             {"id": "sun", "label": "Bright sunlight",
              "lux": "about 50 000 lux", "eye": 2.0, "cam": 3},
         ],
         "start_level": 2,
         "systems": [
             {"id": "eye", "label": "Your eye", "key": "eye",
              "stop_name": "the pupil, opened by the iris",
              "focus": "Muscles squeeze the lens fatter or let it go thinner",
              "absorb": "The retina — a chemical change in rod and cone "
                        "cells, then nerve signals",
              "absorb_name": "RETINA",
              "caption": "THE EYE — CORNEA, IRIS AND PUPIL, LENS, RETINA",
              "tail": "That signal starts as a chemical change in the rod and "
                      "cone cells."},
             {"id": "camera", "label": "A camera", "key": "cam",
              "stop_name": "the aperture, opened by blades",
              "focus": "A motor slides the whole lens backwards or forwards",
              "absorb": "The sensor — an electrical signal, straight away",
              "absorb_name": "SENSOR",
              "caption": "A CAMERA — BODY, APERTURE, LENS, SENSOR",
              "tail": "That signal is electrical from the moment the light "
                      "lands."},
         ],
         "readouts": [
             {"id": "light", "label": "How bright the scene is", "sub": "—"},
             {"id": "stop", "label": "How wide the opening is", "sub": "—"},
             {"id": "focus", "label": "How it keeps the picture sharp"},
             {"id": "absorb",
              "label": "What absorbs the light, and what it becomes"},
         ],
         # Her two branches, each naming BOTH openings at the current level,
         # then one shared middle and the instrument's own closing clause.
         "branches": {
             "eye": "In {level} the iris holds the pupil at about {mine} mm "
                    "across. A camera looking at the same scene opens its "
                    "aperture to about {other} mm, because it is a bigger "
                    "instrument doing the same job.",
             "camera": "In {level} this camera opens its aperture to about "
                       "{mine} mm. An eye looking at the same scene holds its "
                       "pupil at about {other} mm.",
         },
         "branch_middle": " Either way the opening is only the doorway: the "
                          "lens still has to put the rays back together at "
                          "the back, and the {absorb} still has to absorb the "
                          "light and turn it into a signal. ",
         "band_anchor": "s-parts",
         "band_at": 1},

        # ── #s-parts · same five jobs, two sets of parts ──────────────
        {"type": "light-band",
         "id": "eye-camera-parts",
         "anchor": "s-parts",
         "eyebrow": "The figure",
         "heading": "Same five jobs, two sets of parts",
         "table": {
             "aria_label": "A table of five jobs an eye and a camera both "
                           "do, with the part that does each job in each "
                           "instrument. The last row is the absorber: the "
                           "retina, where a chemical change sets off nerve "
                           "signals, against the sensor, which gives an "
                           "electrical signal straight away.",
             "columns": ["The job", "In the eye", "In a camera"],
             "rows": [
                 ["Keep the light out except through the opening",
                  "The tough white outer coat, and the iris",
                  "The body of the camera"],
                 ["Control how much gets in",
                  "The iris, opening and closing the pupil",
                  "The aperture, opened and closed by blades"],
                 ["Bring the rays back to a point",
                  "The cornea and the lens together", "The lens"],
                 ["Focus on near and far things",
                  "Muscles change the shape of the lens",
                  "A motor moves the lens back and forth"],
                 ["Absorb the light and turn it into a signal",
                  "The retina: rod and cone cells, a chemical change, then "
                  "nerve signals",
                  "The sensor: an electrical signal, straight away"],
             ],
         },
         "close": "The last row is the one this lesson is really about. Light "
                  "carries energy from a source to an absorber, and at the "
                  "absorber that energy is used to make something happen — a "
                  "chemical change in a retina or in photographic film, an "
                  "electrical signal in a camera sensor or a solar cell. A "
                  "picture is the record of where that energy landed."},

        {"type": "key-fact", "ref": "eye-and-camera-same-five-jobs"},

        {"type": "misconception", "id": "think-eyes-send-something-out",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-eyes-send-something-out",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-17",
         "statements": [
             {"quote": "Your eyes send something out in order to see.",
              "targets": "LIGHT-17",
              "body": [
                  "They receive and nothing more. Light leaves a source, "
                  "bounces off an object and arrives at your eye, which is "
                  "exactly why a room with no light in it shows you nothing "
                  "however hard you stare — there is nothing arriving. Cats’ "
                  "eyes appear to glow at night because a mirror-like layer "
                  "behind the retina sends headlight beams back out again, "
                  "not because the cat is producing anything. The idea that "
                  "sight is something the eye projects is an old and very "
                  "persistent one, and every dark room disproves it.",
              ]},
             {"quote": "In a dark room your pupils open, and that is why you "
                       "can eventually see.",
              "targets": "LIGHT-18",
              "body": [
                  "Opening the pupil is part of it and much the smaller part, "
                  "and it happens in about a second. Waiting a minute or two "
                  "in the dark gives you something far bigger: the pigment in "
                  "the rod cells of your retina rebuilds itself after being "
                  "bleached by bright light, and a fully dark-adapted eye is "
                  "thousands of times more sensitive than one that has just "
                  "come indoors. The pupil is the aperture; dark adaptation "
                  "is the retina being made more sensitive, and only one of "
                  "those has anything a camera can copy.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "eye-and-camera-same-five-jobs",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An eye and a camera both let light through an opening, "
                 "focus it with a convex lens and absorb it at the back. Both "
                 "control how much gets in — the iris opening the pupil, the "
                 "aperture opening in a camera — and both keep the picture "
                 "sharp, the eye by changing the shape of its lens and the "
                 "camera by moving its lens. Light carries energy from a "
                 "source to an absorber: in the retina it causes a chemical "
                 "change in rod and cone cells which sets off nerve signals, "
                 "and in a camera sensor it produces an electrical signal."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "Which pair of parts do the same job in an eye and in a "
                 "camera?",
            "options": [
                "The retina and the lens — both bring the light to a point "
                "at the back.",
                "The iris and the shutter — both open to let a picture "
                "through.",
                "The pupil and the aperture — both set how much light is let "
                "in.",
                "The optic nerve and the lens — both carry the picture "
                "inwards.",
            ],
            "answer": 2,
            "feedback": {
                0: "The retina is the absorber, not a focuser. Its opposite "
                   "number is the camera sensor; the eye’s lens is matched "
                   "by the camera’s lens.",
                1: "The iris changes the size of the opening; a shutter "
                   "controls how long it stays open. The camera part that "
                   "matches the iris is the aperture.",
                3: "The optic nerve carries a signal after the light has "
                   "been absorbed; the lens handles the light before it "
                   "lands. Different ends of the chain.",
            },
            "title": "Rung 1 · Match the parts"},
        "apply": {
            "q": "A student says you can see a book in a dark room because "
                 "your eyes send out rays that reach it. Which statement is "
                 "right?",
            "options": [
                "The student is right, and it is why cats’ eyes glow in the "
                "dark.",
                "Eyes send out rays, but they are too weak to reach anything "
                "more than a metre or so away, which is why a distant "
                "object in a dark room stays invisible however hard you "
                "stare.",
                "You cannot see the book because your pupils are not wide "
                "enough, not because there is no light.",
                "Eyes only receive. Light has to come from a source, reflect "
                "off the book and arrive at the eye — which is why a room "
                "with no light in it shows nothing at all.",
            ],
            "answer": 3,
            "feedback": {
                0: "Cats’ eyes appear to glow because a mirror-like layer "
                   "behind the retina reflects light that arrived from "
                   "outside, usually headlights. Nothing is being produced.",
                1: "They send nothing out at any distance. If they did, a "
                   "completely dark room would be visible, and it is not.",
                2: "The verdict about not seeing is right and the reason is "
                   "wrong. A fully open pupil in a room with no light still "
                   "receives nothing, because there is nothing to receive.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Trace the journey of the light from a lamp to a signal in "
                 "your brain when you look at a red apple, naming what "
                 "happens at the pupil, the lens and the retina.",
            "field_label": "Your explanation",
            "placeholder": "Light leaves the lamp and…",
            "success": [
                "Says light leaves the lamp and reflects off the apple.",
                "Says some of that reflected light enters the eye through "
                "the pupil, whose size the iris sets.",
                "Says the lens refracts the rays so that light from each "
                "point of the apple meets at one point on the retina.",
                "Says the retina absorbs the light and its energy causes a "
                "chemical change in the rod and cone cells.",
                "Says that sets off electrical signals which travel along "
                "the optic nerve to the brain.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A camera and an eye both have to focus on something close "
                 "and then on something far away. Explain how each one does "
                 "it, and say why the eye cannot use the camera’s method.",
            "field_label": "Your answer",
            "placeholder": "A camera focuses by…",
            "success": [
                "Says a camera moves its lens closer to or further from the "
                "sensor.",
                "Says the eye changes the shape of its lens instead, making "
                "it fatter for close objects.",
                "Says muscles inside the eye do that squeezing.",
                "Says the retina is at a fixed distance behind the lens, so "
                "the eye cannot move the lens to suit.",
                "Says both methods have the same purpose: putting the sharp "
                "picture exactly on the absorbing surface.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "An eye and a camera both admit light through a controlled "
                "opening, focus it with a convex lens and absorb it at the "
                "back. The iris sets the size of the pupil and the aperture "
                "does the same job in a camera; the eye focuses by changing "
                "the shape of its lens and a camera by moving its lens. Light "
                "carries energy from a source to an absorber, and at the "
                "absorber it makes something happen: a chemical change in the "
                "rod and cone cells of the retina, which sets off nerve "
                "signals, or an electrical signal directly in a camera "
                "sensor.",

    "stretch": [
        {"id": "light-causing-a-chemical-change",
         "type": "explainer",
         "text": "Light causing a chemical change is not only how you see. "
                 "Photographic film worked by light breaking down silver "
                 "compounds in an emulsion, and the developing process made "
                 "that invisible change visible. Photosynthesis is the same "
                 "idea on an industrial scale: light absorbed by chlorophyll "
                 "drives a chemical reaction that builds sugars. Sunburn is "
                 "light absorbed by skin causing chemical damage to the "
                 "molecules in it. In every case the light delivers energy "
                 "from the source to an absorber, and the absorber does "
                 "something with it."},
    ],

    "support": [],

    # ⚖️ SAFEGUARDING · the engine's `safeguarding_note` slot, which renders
    # as ONE quiet `.ks3-legal` foot line above the legal line — never a
    # callout. Design's words, character for character, and her hard
    # prohibition stays on the page where she put it.
    "safeguarding_note": "Never look directly at the Sun, at a welding arc or "
                         "into a laser, even briefly — the damage is to the "
                         "retina, it is painless at the time, and it does not "
                         "heal. If your sight changes, or something feels "
                         "wrong with an eye, that is worth telling someone "
                         "the same day. You can talk to a doctor, a school "
                         "nurse or any adult you trust. Childline is free, "
                         "confidential and open at any hour, on 0800 1111, "
                         "and you do not have to give your name.",

    "vocabulary": [
        {"term": "pupil",
         "definition": "The opening in the middle of the iris that light "
                       "passes through. The iris makes it wider or narrower."},
        {"term": "retina",
         "definition": "The light-absorbing surface at the back of the eye. "
                       "Its rod and cone cells turn absorbed light into nerve "
                       "signals."},
        {"term": "photosensitive",
         "definition": "Changed by light. A retina and a camera sensor are "
                       "both photosensitive; so was photographic film."},
    ],

    "tutor": {
        "anchor": "s-eye",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check which part of an eye matches which part of a "
                "camera?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The structure of the eye in detail, accommodation, short "
                   "and long sight and their correction with lenses, and the "
                   "transfer of energy by light to chemical and electrical "
                   "stores.",

    "convention_note": "The bench is a teaching model. The pupil and aperture "
                       "widths are typical values for a healthy adult eye and "
                       "for one ordinary camera lens, and both vary widely "
                       "between individuals, with age and between cameras; "
                       "the eye figures are given as diameters and the camera "
                       "figures as the width of the opening in the lens "
                       "rather than as f-numbers. The light levels are "
                       "order-of-magnitude figures in lux and are meant for "
                       "comparison, not measurement. The drawings are "
                       "simplified cross-sections: the eye’s cornea does most "
                       "of the focusing and is not drawn separately, and the "
                       "retina, optic nerve, shutter and mirror are left out "
                       "or reduced to one line. Both pictures at the back are "
                       "inverted, as they are in life.",

    "ws": ["measurement"],
}
