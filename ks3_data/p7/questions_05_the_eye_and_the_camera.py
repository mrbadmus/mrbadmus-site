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
            {"text": "The light is reflected back out through the pupil and "
                     "lost, so nothing is left behind in the eye",
             "correct": False,
             "why": "Absorbed light does not leave again. That is what "
                    "absorbed means."},
            {"text": "Its energy causes a chemical change in the rod and "
                     "cone cells, which sets off electrical signals",
             "correct": True},
            {"text": "The retina focuses it more sharply before passing it "
                     "on to the optic nerve behind", "correct": False,
             "why": "The focusing was done by the cornea and the lens "
                    "before the light arrived. The retina absorbs; it does "
                    "not focus."},
            {"text": "It is turned back into light again and sent along the "
                     "optic nerve to the brain", "correct": False,
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
            {"text": "The pupil widening, which lets in nearly all the "
                     "extra light", "correct": False,
             "why": "The pupil widens in about a second and lets in perhaps "
                    "ten times as much. The other effect is thousands of "
                    "times."},
            {"text": "The lens getting fatter so that it gathers more of "
                     "the light", "correct": False,
             "why": "The lens changes shape to FOCUS, not to gather. It "
                    "does not affect how much light comes in."},
            {"text": "The brain filling in the shape of the room from "
                     "memory", "correct": False,
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
            {"text": "All four give out light again after they have "
                     "absorbed it, which is how the signal gets passed "
                     "along", "correct": False,
             "why": "None of them re-emits light. Each turns the absorbed "
                    "energy into something else."},
            {"text": "All four focus the light to a point, which is what "
                     "makes a sharp picture possible", "correct": False,
             "why": "Focusing is the lens's job in front of them. A solar "
                    "cell has no lens at all."},
            {"text": "All four produce an electrical signal directly, with "
                     "nothing happening in between",
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
            {"text": "Yes — the glow is light the cat is producing itself, "
                     "using energy from the food it eats",
             "correct": False,
             "why": "Cover the headlights and the glow stops instantly, "
                    "which a light source would not do."},
            {"text": "Yes, but only in cats, which is why people's eyes "
                     "never glow back in headlights", "correct": False,
             "why": "People's eyes reflect too — that is what red-eye in a "
                    "flash photograph is. The cat's mirror layer just makes "
                    "it stronger."},
            {"text": "No — a mirror-like layer behind the retina is sending "
                     "the headlights' own light back out", "correct": True},
            {"text": "No — the glow is refraction in the cornea sending "
                     "the beam back to the driver",
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
            {"text": "Because the eye's lens is far more powerful than a "
                     "camera's, so it gathers light the pupil never let in",
             "correct": False,
             "why": "A lens can only work with the light that got through "
                    "the opening. It cannot gather what was blocked."},
            {"text": "Because the eye is a smaller instrument overall, and "
                     "its absorbing surface is closer, and its retina can "
                     "become thousands of times more sensitive",
             "correct": True},
            {"text": "Because the eye can hold its pupil open for far "
                     "longer than a camera can hold its shutter open, and a "
                     "longer opening always gathers more light",
             "correct": False,
             "why": "A camera can hold a shutter open for minutes. Time is "
                    "the camera's advantage, not the eye's."},
            {"text": "Because eyes work at night by a different mechanism "
                     "that does not need light at all", "correct": False,
             "why": "There is no such mechanism. In a room with no light at "
                    "all an eye sees nothing."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-05-e05",
        "band": "easier",
        "text": "The lens of the eye focuses light onto the…",
        "options": [
            {"text": "iris", "correct": False,
             "why": "The iris is the coloured ring that controls the opening; "
                    "it does not receive the picture."},
            {"text": "pupil", "correct": False,
             "why": "The pupil is the opening light passes through on its way "
                    "in."},
            {"text": "retina", "correct": True},
            {"text": "cornea", "correct": False,
             "why": "The cornea is at the front and does some of the "
                    "focusing; the picture forms at the back."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e06",
        "band": "easier",
        "text": "The pupil of the eye is…",
        "options": [
            {"text": "the opening that the iris makes bigger or smaller",
             "correct": True},
            {"text": "the coloured muscle around the opening", "correct": False,
             "why": "That is the iris. The pupil is the gap in the middle of "
                    "it."},
            {"text": "the lens that focuses the light", "correct": False,
             "why": "The lens sits behind the pupil and does the focusing."},
            {"text": "the layer that absorbs the light at the back",
             "correct": False,
             "why": "That is the retina, at the far end of the eye."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e07",
        "band": "easier",
        "text": "Light carries energy from a source to…",
        "options": [            {"text": "the eye only", "correct": False,
             "why": "Any absorber will do — a camera sensor, a solar cell or "
                    "a dark wall."},
            {"text": "another source", "correct": False,
             "why": "A source gives light out; the energy ends up somewhere "
                    "that takes it in."},
            {"text": "the air it passes through", "correct": False,
             "why": "Clear air absorbs almost none of it; the light passes "
                    "straight on."},
            {"text": "an absorber", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-05-s05",
        "band": "standard",
        "text": "In bright sunshine, what does the iris do to the pupil?",
        "options": [
            {"text": "It makes it larger, to see more detail",
             "correct": False,
             "why": "In bright light the opening is made SMALLER, to let less "
                    "in."},
            {"text": "It makes it smaller, so less light gets in",
             "correct": True},
            {"text": "It closes it completely for a moment", "correct": False,
             "why": "It never shuts entirely; it narrows to a small opening."},
            {"text": "Nothing — the pupil is a fixed size", "correct": False,
             "why": "It changes size constantly, which is easy to watch in a "
                    "mirror."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s06",
        "band": "standard",
        "text": "How does a camera focus on something nearer than what it was "
                "focused on before?",
        "options": [
            {"text": "By changing the shape of its lens", "correct": False,
             "why": "That is how the EYE does it; a glass lens cannot change "
                    "shape."},
            {"text": "By moving its lens", "correct": True},
            {"text": "By moving the sensor closer to the subject",
             "correct": False,
             "why": "The sensor is fixed at the back of the body; the lens is "
                    "what moves."},
            {"text": "By opening the aperture wider", "correct": False,
             "why": "That changes how much light gets in, not where the "
                    "picture is sharp."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s07",
        "band": "standard",
        "text": "Why can you still see nothing in a completely dark room even "
                "after waiting an hour?",
        "options": [
            {"text": "Because the pupils cannot open far enough in an hour",
             "correct": False,
             "why": "They open within seconds, and no opening helps when "
                    "there is nothing arriving."},
            {"text": "Because there is no light for the retina to absorb",
             "correct": True},
            {"text": "Because the eyes have stopped sending out rays",
             "correct": False,
             "why": "Eyes never send anything out; they only receive."},
            {"text": "Because the lens cannot focus in the dark",
             "correct": False,
             "why": "The lens works as usual; there is simply nothing to "
                    "bring to a focus."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-05-h05",
        "band": "harder",
        "text": "What happens to the energy of the light the retina absorbs?",
        "options": [
            {"text": "It is reflected back out through the pupil",
             "correct": False,
             "why": "Reflected light would leave again; absorbed light is "
                    "what triggers the response."},
            {"text": "It is stored in the retina until the eye is next "
                     "closed",
             "correct": False,
             "why": "Nothing stores it; the change happens as the light "
                    "arrives."},
            {"text": "It causes a chemical change in cells, which sets off "
                     "nerve signals",
             "correct": True},
            {"text": "It is turned into an electrical signal directly, with "
                     "no chemistry",
             "correct": False,
             "why": "That is a camera sensor. In the eye a chemical change "
                    "comes first."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h06",
        "band": "harder",
        "text": "Why does the eye change the SHAPE of its lens rather than "
                "moving it, as a camera does?",
        "options": [
            {"text": "Because the eye's lens is flexible and held in place by "
                     "muscles",
             "correct": True},
            {"text": "Because moving a lens cannot focus light at all",
             "correct": False,
             "why": "It focuses perfectly well — every camera works that "
                    "way."},
            {"text": "Because the eye's lens is fixed and cannot change at "
                     "all",
             "correct": False,
             "why": "If it could not change, the eye could not switch between "
                    "near and far objects."},
            {"text": "Because the retina moves instead, taking the lens's "
                     "place",
             "correct": False,
             "why": "The retina is fixed at the back of the eye and does not "
                    "move."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h07",
        "band": "harder",
        "text": "The picture on the retina is upside down. Why does the world "
                "not look upside down?",
        "options": [
            {"text": "Because the lens turns it back the right way before it "
                     "lands",
             "correct": False,
             "why": "The lens is what inverts it; nothing after that turns "
                    "the light round again."},
            {"text": "Because the retina is curved, which cancels the "
                     "inversion",
             "correct": False,
             "why": "Curvature keeps the picture sharp across the retina; it "
                    "does not flip it."},
            {"text": "Because the brain interprets the signals, and the "
                     "physics is unchanged",
             "correct": True},
            {"text": "Because the eye is upside down inside the head",
             "correct": False,
             "why": "Turning the whole eye over would not undo an inversion "
                    "produced by its own lens."},
        ],
        "figure": None,
    },
]
