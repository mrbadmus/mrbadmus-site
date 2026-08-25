"""P7 lesson 05 — The eye and the camera: twelve questions (MRB-223).

Written against Design's page. The dark-room hook, the two-instrument
bench and the five-job table are hers.

The discriminations, in the order the lesson builds them:

  · an eye RECEIVES and sends nothing out (`LIGHT-17`);
  · the pupil is a small part of dark adaptation and the retina is the
    big part (`LIGHT-18`);
  · the retina ABSORBS, it does not focus (`LIGHT-19`);
  · the iris sets how WIDE and a shutter sets how LONG (`LIGHT-20`) — the
    harder band sits here, with the energy chain from source to absorber.

⚠️ POSITION IS AUTHORED — 2,0,1,3 · 1,2,3,0 · 3,0,2,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. This lesson has no
worked example: it is a system lesson and nothing in it is quantitative.
"""

UNIT = "P7"
LESSON = "the-eye-and-the-camera"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-05-e01",
        "band": "easier",
        "text": "Which part of the eye sets how much light gets in?",
        "options": [
            {"text": "The retina", "correct": False,
             "why": "The retina absorbs the light at the back. It has no "
                    "say in how much arrives."},
            {"text": "The lens", "correct": False,
             "why": "The lens decides where the light lands, not how much "
                    "of it comes in."},
            {"text": "The iris, by changing the size of the pupil",
             "correct": True},
            {"text": "The optic nerve, which lets the signal through",
             "correct": False,
             "why": "The optic nerve carries the signal away after the "
                    "light has been absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e02",
        "band": "easier",
        "text": "In a camera, the part that matches the retina is the…",
        "options": [
            {"text": "sensor", "correct": True},
            {"text": "lens", "correct": False,
             "why": "The camera's lens matches the eye's lens. Both handle "
                    "the light before it lands."},
            {"text": "aperture", "correct": False,
             "why": "The aperture matches the pupil: both decide how much "
                    "light gets in."},
            {"text": "shutter", "correct": False,
             "why": "The shutter decides how LONG light is let in. The eye "
                    "has no part that does that."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e03",
        "band": "easier",
        "text": "Photosensitive means…",
        "options": [
            {"text": "giving out light of its own", "correct": False,
             "why": "That is a light SOURCE. A photosensitive surface "
                    "receives."},
            {"text": "changed by light", "correct": True},
            {"text": "transparent to light", "correct": False,
             "why": "A transparent thing lets light through unchanged, "
                    "which is nearly the opposite."},
            {"text": "reflecting light without absorbing any",
             "correct": False,
             "why": "A photosensitive surface has to absorb the light "
                    "before anything can happen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e04",
        "band": "easier",
        "text": "You cannot see anything in a room with no light in it at "
                "all. Why?",
        "options": [
            {"text": "Because your pupils cannot open wide enough",
             "correct": False,
             "why": "A fully open pupil still receives nothing if nothing "
                    "is arriving."},
            {"text": "Because your eyes need a moment to send out enough "
                     "light", "correct": False,
             "why": "Eyes send nothing out at all. They only receive."},
            {"text": "Because the retina stops working in the dark",
             "correct": False,
             "why": "The retina gets MORE sensitive in the dark, not less. "
                    "It simply has nothing to absorb."},
            {"text": "Because seeing needs light to arrive at your eye, and "
                     "none is", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-05-s01",
        "band": "standard",
        "text": "Light is absorbed by the retina. What happens next?",
        "options": [
            {"text": "The light is reflected back out through the pupil",
             "correct": False,
             "why": "Absorbed light does not leave again. That is what "
                    "absorbed means."},
            {"text": "Its energy causes a chemical change in the rod and "
                     "cone cells, which sets off electrical signals",
             "correct": True},
            {"text": "The retina focuses it more sharply", "correct": False,
             "why": "The focusing was done by the cornea and the lens "
                    "before the light arrived."},
            {"text": "It is turned back into light and sent along the optic "
                     "nerve to the brain", "correct": False,
             "why": "What travels along the optic nerve is an electrical "
                    "signal, not light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s02",
        "band": "standard",
        "text": "A camera and an eye both have to focus on near and far "
                "things. How does the eye do it?",
        "options": [
            {"text": "By moving the retina backwards and forwards",
             "correct": False,
             "why": "The retina is fixed. That is precisely why the eye "
                    "cannot use the camera's method."},
            {"text": "By opening and closing the pupil", "correct": False,
             "why": "The pupil sets how much light comes in, not where it "
                    "lands."},
            {"text": "By changing the shape of its own lens", "correct": True},
            {"text": "By sliding the whole lens closer to the retina",
             "correct": False,
             "why": "That is the camera's method. The eye's lens does not "
                    "move along the eyeball."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s03",
        "band": "standard",
        "text": "Stepping from bright sun into a dim hall, you see almost "
                "nothing at first and then more and more. Which is the "
                "bigger effect?",
        "options": [
            {"text": "The pupil widening, which is nearly all of it",
             "correct": False,
             "why": "The pupil widens in about a second and lets in perhaps "
                    "ten times as much. The other effect is thousands of "
                    "times."},
            {"text": "The lens getting fatter to gather more light",
             "correct": False,
             "why": "The lens changes shape to FOCUS, not to gather. It "
                    "does not affect how much light comes in."},
            {"text": "The brain filling in the shape of the room",
             "correct": False,
             "why": "You genuinely see more detail, and detail cannot be "
                    "filled in from nothing."},
            {"text": "The retina becoming far more sensitive as its pigment "
                     "rebuilds", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s04",
        "band": "standard",
        "text": "Where does the energy carried by the light end up when you "
                "look at a lit page?",
        "options": [
            {"text": "In the retina, where it drives a chemical change",
             "correct": True},
            {"text": "In the lens, which stores it until it is needed",
             "correct": False,
             "why": "The lens passes the light on. Nothing is stored in "
                    "it."},
            {"text": "Back out of the pupil, having done its job",
             "correct": False,
             "why": "Very little leaves again. What is absorbed is what "
                    "makes seeing possible."},
            {"text": "In the page, which is why reading warms it up",
             "correct": False,
             "why": "The page absorbs some, and the light that reaches your "
                    "eye is the light it did NOT absorb."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-05-h01",
        "band": "harder",
        "text": "A camera can freeze a fast-moving bird with a very short "
                "shutter time. The eye has no shutter. What does that tell "
                "you about the two systems?",
        "options": [
            {"text": "That an eye cannot see moving objects at all",
             "correct": False,
             "why": "It plainly can. What it cannot do is choose a very "
                    "short exposure."},
            {"text": "That the eye's pupil must be doing the shutter's job",
             "correct": False,
             "why": "The pupil sets how WIDE the opening is, not how long "
                    "it is open. Those are different controls."},
            {"text": "That the two do not do the same five jobs after all, "
                     "since one of them has a control the other lacks",
             "correct": False,
             "why": "They do. Timing is a sixth job the camera has and the "
                    "eye does not."},
            {"text": "That the camera has one control the eye lacks, and it "
                     "is about how long rather than how much",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h02",
        "band": "harder",
        "text": "Photographic film, a camera sensor, a retina and a solar "
                "cell are all doing the same physics. What is it?",
        "options": [
            {"text": "Light carries energy from a source to an absorber, "
                     "and at the absorber that energy makes something "
                     "happen", "correct": True},
            {"text": "All four give out light again after absorbing it, "
                     "which is how the signal gets passed on",
             "correct": False,
             "why": "None of them re-emits light. Each turns the absorbed "
                    "energy into something else."},
            {"text": "All four focus light to a point", "correct": False,
             "why": "Focusing is the lens's job in front of them. A solar "
                    "cell has no lens at all."},
            {"text": "All four produce an electrical signal directly",
             "correct": False,
             "why": "Film and the retina start with a CHEMICAL change. Only "
                    "the sensor and the cell are electrical straight away."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h03",
        "band": "harder",
        "text": "A cat's eyes seem to glow in headlights. Does this show "
                "that eyes send light out?",
        "options": [
            {"text": "Yes — the glow is light the cat is producing",
             "correct": False,
             "why": "Cover the headlights and the glow stops instantly, "
                    "which a light source would not do."},
            {"text": "Yes, but only in cats, which is why people's eyes do "
                     "not do it", "correct": False,
             "why": "People's eyes reflect too — that is what red-eye in a "
                    "flash photograph is. The cat's mirror layer just makes "
                    "it stronger."},
            {"text": "No — a mirror-like layer behind the retina is sending "
                     "the headlights' own light back out", "correct": True},
            {"text": "No — the glow is refraction in the cornea",
             "correct": False,
             "why": "Refraction bends light on the way in; it does not send "
                    "it back towards the driver."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h04",
        "band": "harder",
        "text": "Camera makers quote how wide the opening can be, in "
                "millimetres. The eye's pupil is much narrower. Why is the "
                "eye not much worse in dim light?",
        "options": [
            {"text": "Because the eye's lens is far more powerful, so it "
                     "gathers light the pupil never let in", "correct": False,
             "why": "A lens can only work with the light that got through "
                    "the opening. It cannot gather what was blocked."},
            {"text": "Because the eye is a smaller instrument overall, and "
                     "its absorbing surface is closer, and its retina can "
                     "become thousands of times more sensitive",
             "correct": True},
            {"text": "Because the eye can hold its pupil open for longer "
                     "than a camera can hold its shutter, and a longer "
                     "opening always gathers more", "correct": False,
             "why": "A camera can hold a shutter open for minutes. Time is "
                    "the camera's advantage, not the eye's."},
            {"text": "Because eyes work at night by a different mechanism "
                     "that does not need light", "correct": False,
             "why": "There is no such mechanism. In a room with no light at "
                    "all an eye sees nothing."},
        ],
        "figure": None,
    },
]
