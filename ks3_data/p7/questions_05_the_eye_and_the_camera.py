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
    {
        "id": "p7-05-e01",
        "band": "easier",
        "text": "Which part of the eye sets how much light gets in?",
        "options": [
            {"text": "The retina", "correct": False,
             "why": "The retina absorbs the light at the back. It has no say "
             "in how much arrives."},
            {"text": "The lens", "correct": False,
             "why": "The lens decides where the light lands, not how much of "
             "it comes in."},
            {"text": "The iris, by changing the size of the pupil", "correct": True},
            {"text": "The optic nerve, which lets the signal through", "correct": False,
             "why": "The optic nerve carries the signal away after the light "
             "has been absorbed."},
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
             "why": "The camera's lens matches the eye's lens. Both handle the "
             "light before it lands."},
            {"text": "aperture", "correct": False,
             "why": "The aperture matches the pupil: both decide how much "
             "light gets in."},
            {"text": "shutter", "correct": False,
             "why": "The shutter decides how LONG light is let in. The eye has "
             "no part that does that."},
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
             "why": "A transparent thing lets light through unchanged, which "
             "is nearly the opposite."},
            {"text": "reflecting light without absorbing any", "correct": False,
             "why": "A photosensitive surface has to absorb the light before "
             "anything can happen."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e04",
        "band": "easier",
        "text": "You cannot see anything in a room with no light in it at all. "
                 "Why?",
        "options": [
            {"text": "Because your pupils cannot open wide enough", "correct": False,
             "why": "A fully open pupil still receives nothing if nothing is "
             "arriving."},
            {"text": "Because your eyes need a moment to send out enough light", "correct": False,
             "why": "Eyes send nothing out at all. They only receive."},
            {"text": "Because the retina stops working in the dark", "correct": False,
             "why": "The retina gets MORE sensitive in the dark, not less. It "
             "simply has nothing to absorb."},
            {"text": "Because seeing needs light to arrive at your eye, and "
             "none is",
             "correct": True},
        ],
        "figure": None,
    },
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
            {"text": "Its energy causes a chemical change in the rod and cone "
             "cells, which sets off electrical signals",
             "correct": True},
            {"text": "The retina focuses it more sharply before passing it on "
             "to the optic nerve behind",
             "correct": False,
             "why": "The focusing was done by the cornea and the lens before "
             "the light arrived. The retina absorbs; it does not focus."},
            {"text": "It is turned back into light again and sent along the "
             "optic nerve to the brain",
             "correct": False,
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
            {"text": "By moving the retina backwards and forwards", "correct": False,
             "why": "The retina is fixed. That is precisely why the eye cannot "
             "use the camera's method."},
            {"text": "By opening and closing the pupil", "correct": False,
             "why": "The pupil sets how much light comes in, not where it "
             "lands."},
            {"text": "By changing the shape of its own lens", "correct": True},
            {"text": "By sliding the whole lens closer to the retina", "correct": False,
             "why": "That is the camera's method. The eye's lens does not move "
             "along the eyeball."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s03",
        "band": "standard",
        "text": "Stepping from bright sun into a dim hall, you see almost "
                 "nothing at first and then more and more. Which is the bigger effect?",
        "options": [
            {"text": "The pupil widening, which lets in nearly all the extra "
             "light",
             "correct": False,
             "why": "The pupil widens in about a second and lets in perhaps "
             "ten times as much. The other effect is thousands of times."},
            {"text": "The lens getting fatter so that it gathers more of the "
             "light",
             "correct": False,
             "why": "The lens changes shape to FOCUS, not to gather. It does "
             "not affect how much light comes in."},
            {"text": "The brain filling in the shape of the room from memory", "correct": False,
             "why": "You genuinely see more detail, and detail cannot be "
             "filled in from nothing."},
            {"text": "The retina becoming far more sensitive as its pigment "
             "rebuilds",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s04",
        "band": "standard",
        "text": "Where does the energy carried by the light end up when you "
                 "look at a lit page?",
        "options": [
            {"text": "In the retina, where it drives a chemical change", "correct": True},
            {"text": "In the lens, which stores it until it is needed", "correct": False,
             "why": "The lens passes the light on. Nothing is stored in it."},
            {"text": "Back out of the pupil, having done its job", "correct": False,
             "why": "Very little leaves again. What is absorbed is what makes "
             "seeing possible."},
            {"text": "In the page, which is why reading warms it up", "correct": False,
             "why": "The page absorbs some, and the light that reaches your "
             "eye is the light it did NOT absorb."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h01",
        "band": "harder",
        "text": "A camera can freeze a fast-moving bird with a very short "
                 "shutter time. The eye has no shutter. What does that tell you about "
                 "the two systems?",
        "options": [
            {"text": "That an eye cannot see moving objects at all", "correct": False,
             "why": "It plainly can. What it cannot do is choose a very short "
             "exposure."},
            {"text": "That the eye's pupil must be doing the shutter's job", "correct": False,
             "why": "The pupil sets how WIDE the opening is, not how long it "
             "is open. Those are different controls."},
            {"text": "That the two do not do the same five jobs after all, "
             "since one of them has a control the other lacks",
             "correct": False,
             "why": "They do. Timing is a sixth job the camera has and the eye "
             "does not."},
            {"text": "That the camera has one control the eye lacks, and it is "
             "about how long rather than how much",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h02",
        "band": "harder",
        "text": "Photographic film, a camera sensor, a retina and a solar cell "
                 "are all doing the same physics. What is it?",
        "options": [
            {"text": "Light carries energy from a source to an absorber, and at "
             "the absorber that energy makes something happen",
             "correct": True},
            {"text": "All four give out light again after they have absorbed "
             "it, which is how the signal gets passed along",
             "correct": False,
             "why": "None of them re-emits light. Each turns the absorbed "
             "energy into something else."},
            {"text": "All four focus the light to a point, which is what makes "
             "a sharp picture possible",
             "correct": False,
             "why": "Focusing is the lens's job in front of them. A solar cell "
             "has no lens at all."},
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
        "text": "A cat's eyes seem to glow in headlights. Does this show that "
                 "eyes send light out?",
        "options": [
            {"text": "Yes — the glow is light the cat is producing itself, "
             "using energy from the food it eats",
             "correct": False,
             "why": "Cover the headlights and the glow stops instantly, which "
             "a light source would not do."},
            {"text": "Yes, but only in cats, which is why people's eyes never "
             "glow back in headlights",
             "correct": False,
             "why": "People's eyes reflect too — that is what red-eye in a "
             "flash photograph is. The cat's mirror layer just makes it "
             "stronger."},
            {"text": "No — a mirror-like layer behind the retina is sending the "
             "headlights' own light back out",
             "correct": True},
            {"text": "No — the glow is refraction in the cornea sending the "
             "beam back to the driver",
             "correct": False,
             "why": "Refraction bends light on the way in; it does not send it "
             "back towards the driver."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h04",
        "band": "harder",
        "text": "Camera makers quote how wide the opening can be, in "
                 "millimetres. The eye's pupil is much narrower. Why is the eye not "
                 "much worse in dim light?",
        "options": [
            {"text": "Because the eye's lens is far more powerful than a "
             "camera's, so it gathers light the pupil never let in",
             "correct": False,
             "why": "A lens can only work with the light that got through the "
             "opening. It cannot gather what was blocked."},
            {"text": "Because the eye is a smaller instrument overall, and its "
             "absorbing surface is closer, and its retina can become thousands "
             "of times more sensitive",
             "correct": True},
            {"text": "Because the eye can hold its pupil open for far longer "
             "than a camera can hold its shutter open, and a longer opening "
             "always gathers more light",
             "correct": False,
             "why": "A camera can hold a shutter open for minutes. Time is the "
             "camera's advantage, not the eye's."},
            {"text": "Because eyes work at night by a different mechanism that "
             "does not need light at all",
             "correct": False,
             "why": "There is no such mechanism. In a room with no light at "
             "all an eye sees nothing."},
        ],
        "figure": None,
    },
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
             "why": "The cornea is at the front and does some of the focusing; "
             "the picture forms at the back."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e06",
        "band": "easier",
        "text": "The pupil of the eye is…",
        "options": [
            {"text": "the opening that the iris makes bigger or smaller", "correct": True},
            {"text": "the coloured muscle around the opening", "correct": False,
             "why": "That is the iris. The pupil is the gap in the middle of "
             "it."},
            {"text": "the lens that focuses the light", "correct": False,
             "why": "The lens sits behind the pupil and does the focusing."},
            {"text": "the layer that absorbs the light at the back", "correct": False,
             "why": "That is the retina, at the far end of the eye."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e07",
        "band": "easier",
        "text": "Light carries energy from a source to…",
        "options": [
            {"text": "the eye only", "correct": False,
             "why": "Any absorber will do — a camera sensor, a solar cell or a "
             "dark wall."},
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
    {
        "id": "p7-05-s05",
        "band": "standard",
        "text": "In bright sunshine, what does the iris do to the pupil?",
        "options": [
            {"text": "It makes it larger, to see more detail", "correct": False,
             "why": "In bright light the opening is made SMALLER, to let less "
             "in."},
            {"text": "It makes it smaller, so less light gets in", "correct": True},
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
            {"text": "By moving the sensor closer to the subject", "correct": False,
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
            {"text": "Because the pupils cannot open far enough in an hour", "correct": False,
             "why": "They open within seconds, and no opening helps when there "
             "is nothing arriving."},
            {"text": "Because there is no light for the retina to absorb", "correct": True},
            {"text": "Because the eyes have stopped sending out rays", "correct": False,
             "why": "Eyes never send anything out; they only receive."},
            {"text": "Because the lens cannot focus in the dark", "correct": False,
             "why": "The lens works as usual; there is simply nothing to bring "
             "to a focus."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h05",
        "band": "harder",
        "text": "What happens to the energy of the light the retina absorbs?",
        "options": [
            {"text": "It is reflected back out through the pupil", "correct": False,
             "why": "Reflected light would leave again; absorbed light is what "
             "triggers the response."},
            {"text": "It is stored in the retina until the eye is next closed", "correct": False,
             "why": "Nothing stores it; the change happens as the light "
             "arrives."},
            {"text": "It causes a chemical change in cells, which sets off "
             "nerve signals",
             "correct": True},
            {"text": "It is turned into an electrical signal directly, with no "
             "chemistry",
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
            {"text": "Because moving a lens cannot focus light at all", "correct": False,
             "why": "It focuses perfectly well — every camera works that way."},
            {"text": "Because the eye's lens is fixed and cannot change at all", "correct": False,
             "why": "If it could not change, the eye could not switch between "
             "near and far objects."},
            {"text": "Because the retina moves instead, taking the lens's place", "correct": False,
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
             "why": "The lens is what inverts it; nothing after that turns the "
             "light round again."},
            {"text": "Because the retina is curved, which cancels the inversion", "correct": False,
             "why": "Curvature keeps the picture sharp across the retina; it "
             "does not flip it."},
            {"text": "Because the brain interprets the signals, and the physics "
             "is unchanged",
             "correct": True},
            {"text": "Because the eye is upside down inside the head", "correct": False,
             "why": "Turning the whole eye over would not undo an inversion "
             "produced by its own lens."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e08",
        "band": "easier",
        "text": "In a camera, what plays the same role as the eye's tough "
                "outer coat, keeping light out except through the opening?",
        "options": [
            {"text": "The camera's lens, which blocks stray light around "
             "its edges",
             "correct": False,
             "why": "The lens focuses the light that gets in; it is not "
             "what keeps the rest out."},
            {"text": "The camera's sensor, once it has been exposed",
             "correct": False,
             "why": "The sensor absorbs light after it has already entered "
             "— too late to be keeping anything out."},
            {"text": "The body of the camera",
             "correct": True},
            {"text": "The camera's shutter, when it is closed",
             "correct": False,
             "why": "The shutter controls timing, not the general "
             "light-tight casing around the whole camera."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e09",
        "band": "easier",
        "text": "Which two parts of the eye work together to bend light to a "
                 "point at the back?",
        "options": [
            {"text": "The iris and the pupil", "correct": False,
             "why": "The iris and pupil control how much light gets in, not "
             "where it lands."},
            {"text": "The retina and the optic nerve", "correct": False,
             "why": "Those two come after the light has already been focused — "
             "one absorbs it, one carries the signal away."},
            {"text": "The cornea and the lens", "correct": True},
            {"text": "The pupil and the retina", "correct": False,
             "why": "The pupil is an opening, not something that bends light, "
             "and the retina only absorbs what arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e10",
        "band": "easier",
        "text": "A camera does the cornea-and-lens bending job of the eye "
                "with how many parts?",
        "options": [
            {"text": "Just one — the lens",
             "correct": True},
            {"text": "Two, a front lens and a back lens",
             "correct": False,
             "why": "The bending job in front of the sensor is done by a "
             "single lens in an ordinary camera."},
            {"text": "Three, one for each colour",
             "correct": False,
             "why": "Splitting into colours is what a prism does, not what "
             "a focusing lens does."},
            {"text": "None — the sensor does the bending itself",
             "correct": False,
             "why": "A sensor absorbs light; it has no power to bend it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e11",
        "band": "easier",
        "text": "An eye and a camera both make two kinds of adjustment. "
                "What are they?",
        "options": [
            {"text": "How fast the picture forms, and how large it is",
             "correct": False,
             "why": "Neither instrument adjusts picture size this way; the "
             "true two are about light amount and focus."},
            {"text": "How the picture is stored, and how it is viewed",
             "correct": False,
             "why": "Storage and viewing come after the image has been "
             "formed; neither is an adjustment made while the picture is "
             "being caught."},
            {"text": "How the light travels in a straight line, and how it "
             "reflects",
             "correct": False,
             "why": "Both instruments rely on straight-line travel and "
             "reflection from objects, but neither ADJUSTS those things."},
            {"text": "How much light gets in, and where the picture comes "
             "into focus",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e12",
        "band": "easier",
        "text": "Which control can a camera have that an eye has no "
                "equivalent of at all?",
        "options": [
            {"text": "A control over how wide the opening is",
             "correct": False,
             "why": "The eye has exactly this — the iris controls the "
             "pupil's width."},
            {"text": "A control over how sharp the picture is",
             "correct": False,
             "why": "The eye focuses too, by changing the shape of its "
             "lens."},
            {"text": "A control over how LONG the opening stays open",
             "correct": True},
            {"text": "A control over how much light is absorbed at the back",
             "correct": False,
             "why": "Both the retina and a sensor simply absorb whatever "
             "light reaches them; neither has a separate control for this."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e13",
        "band": "easier",
        "text": "Roughly how much more light does a fully open pupil let "
                "in, compared with a tightly constricted one?",
        "options": [
            {"text": "About twice as much",
             "correct": False,
             "why": "The change is bigger than that: going from a tightly "
             "closed pupil to a fully open one lets in roughly ten times as "
             "much."},
            {"text": "About a hundred times as much",
             "correct": False,
             "why": "Widening the pupil is a far smaller change than that; "
             "the huge gain in the dark comes from the retina's own "
             "sensitivity instead."},
            {"text": "About ten times as much",
             "correct": True},
            {"text": "No more — pupil size does not affect how much light "
             "gets in",
             "correct": False,
             "why": "A wider opening lets more light through; that is "
             "exactly what the pupil widening is for."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e14",
        "band": "easier",
        "text": "Roughly how long does it take for the retina to become "
                "fully adapted to darkness?",
        "options": [
            {"text": "It stays exactly as sensitive as before",
             "correct": False,
             "why": "A fully dark-adapted eye does exist, and it is "
             "thousands of times more sensitive than one that has just come "
             "indoors."},
            {"text": "Less than a second",
             "correct": False,
             "why": "That is roughly how fast the pupil itself widens; the "
             "retina's own adjustment takes much longer."},
            {"text": "About a day",
             "correct": False,
             "why": "Dark adaptation happens within one sitting in a dark "
             "room, not over the course of a day."},
            {"text": "Several minutes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e15",
        "band": "easier",
        "text": "In a real eye, which single part does most of the focusing — "
                 "more than the lens itself?",
        "options": [
            {"text": "The retina", "correct": False,
             "why": "The retina absorbs the focused light; it plays no part in "
             "bending it."},
            {"text": "The iris", "correct": False,
             "why": "The iris controls how much light gets in, not how it is "
             "focused."},
            {"text": "The optic nerve", "correct": False,
             "why": "The optic nerve only carries the signal onward, after "
             "focusing is finished."},
            {"text": "The cornea", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e16",
        "band": "easier",
        "text": "In old cameras that used film rather than a digital "
                "sensor, what absorbed the light to make the picture?",
        "options": [
            {"text": "The lens",
             "correct": False,
             "why": "The lens focuses the light onto the film; the film is "
             "what absorbs it."},
            {"text": "The shutter",
             "correct": False,
             "why": "The shutter only controls how long light is let "
             "through, not what absorbs it."},
            {"text": "The photographic film",
             "correct": True},
            {"text": "The viewfinder",
             "correct": False,
             "why": "A viewfinder is for the photographer to look through; "
             "no picture is recorded there."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e17",
        "band": "easier",
        "text": "What kind of change does light cause in photographic film?",
        "options": [
            {"text": "An electrical change, exactly like a digital sensor", "correct": False,
             "why": "That is how a digital sensor responds. Film responds "
             "chemically instead."},
            {"text": "No change — film simply reflects the light back", "correct": False,
             "why": "Film would show no picture if it merely reflected; the "
             "image comes from a genuine change in it."},
            {"text": "A chemical change", "correct": True},
            {"text": "A change in temperature that is read off afterwards", "correct": False,
             "why": "The image comes from a chemical change in the film's "
             "compounds, not from a temperature reading."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e18",
        "band": "easier",
        "text": "Why is looking directly at very bright sources such as the "
                "Sun especially dangerous for the retina?",
        "options": [
            {"text": "Because it is a part of the body a doctor finds hard "
             "to examine",
             "correct": False,
             "why": "Plenty about the eye can be checked by a doctor; the "
             "real danger is that the retinal damage itself cannot be "
             "undone."},
            {"text": "Because it makes the pupil close completely, which "
             "damages the iris",
             "correct": False,
             "why": "The pupil narrows but never closes completely, and "
             "that narrowing is not what causes the injury."},
            {"text": "Because it changes the shape of the lens permanently",
             "correct": False,
             "why": "The danger from a very bright source is to the retina "
             "at the back, not to the shape of the lens."},
            {"text": "Because the damage happens painlessly and does not "
             "heal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e19",
        "band": "easier",
        "text": "A camera's aperture is opened and closed by its blades. "
                "Which eye part does the equivalent job?",
        "options": [
            {"text": "The lens",
             "correct": False,
             "why": "The lens focuses the light that has already got in."},
            {"text": "The retina",
             "correct": False,
             "why": "The retina absorbs light at the back; it plays no part "
             "in controlling the opening."},
            {"text": "The iris",
             "correct": True},
            {"text": "The cornea",
             "correct": False,
             "why": "The cornea is at the very front and helps with "
             "focusing, not with the size of the opening."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e20",
        "band": "easier",
        "text": "A camera's motor slides its lens backwards and forwards to "
                 "focus. Which eye part changes shape to do the equivalent job?",
        "options": [
            {"text": "The retina, at the very back", "correct": False,
             "why": "The retina is fixed in place at the back of the eye and "
             "does not change shape to focus."},
            {"text": "The cornea, at the very front", "correct": False,
             "why": "The cornea's own shape is fixed; the lens behind it is "
             "what the eye adjusts."},
            {"text": "The iris, around the pupil", "correct": False,
             "why": "The iris changes the size of the pupil, not the sharpness "
             "of the picture."},
            {"text": "The eye's own lens", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e21",
        "band": "easier",
        "text": "Which of these correctly matches a camera part to the eye "
                 "part that does the same job?",
        "options": [
            {"text": "Shutter — pupil", "correct": False,
             "why": "The shutter controls timing; the part that matches the "
             "pupil is the aperture."},
            {"text": "Body — lens", "correct": False,
             "why": "The camera body matches the eye's outer coat and iris, "
             "not its lens."},
            {"text": "Sensor — retina", "correct": True},
            {"text": "Aperture — cornea", "correct": False,
             "why": "The aperture matches the pupil, which sets how much light "
             "gets in. The cornea's job is focusing."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e22",
        "band": "easier",
        "text": "A retina turns absorbed light into a signal using rod and "
                "cone cells. What kind of change happens in those cells "
                "first?",
        "options": [
            {"text": "No change — the cells simply pass the light straight "
             "through",
             "correct": False,
             "why": "The cells absorb the light rather than passing it "
             "through, and that absorption is what triggers the signal."},
            {"text": "An electrical change, straight away",
             "correct": False,
             "why": "That is how a camera sensor responds. In the eye, a "
             "chemical change comes first."},
            {"text": "A change in colour that the brain then reads",
             "correct": False,
             "why": "The cells do not change colour; they undergo a "
             "chemical change that triggers a nerve signal."},
            {"text": "A chemical change",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e23",
        "band": "easier",
        "text": "What travels from the retina to the brain along the optic "
                "nerve?",
        "options": [
            {"text": "Light itself",
             "correct": False,
             "why": "Light is absorbed at the retina and goes no further. "
             "What travels onward is a signal, not light."},
            {"text": "A chemical, carried in the blood",
             "correct": False,
             "why": "The optic nerve carries an electrical signal, not a "
             "chemical substance."},
            {"text": "An electrical signal",
             "correct": True},
            {"text": "A copy of the picture, unaltered",
             "correct": False,
             "why": "Nothing like a picture travels along a nerve; what "
             "travels is an electrical signal, already converted from the "
             "chemical change in the retina."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e24",
        "band": "easier",
        "text": "Which of these is something BOTH an eye and a camera do?",
        "options": [
            {"text": "Store many pictures for looking at later",
             "correct": False,
             "why": "That is not one of the five jobs the two share; it is "
             "a separate feature some cameras happen to have."},
            {"text": "Send out their own light to illuminate a scene",
             "correct": False,
             "why": "Neither instrument sends light out. Both only receive "
             "it."},
            {"text": "Print a copy of the picture automatically",
             "correct": False,
             "why": "Printing plays no part in either instrument's job in "
             "this comparison."},
            {"text": "Absorb light at the back and turn it into a signal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e25",
        "band": "easier",
        "text": "Behind the opening, an eye and a camera both use the same "
                "kind of lens to bring the rays to a point. Which kind is "
                "it?",
        "options": [
            {"text": "A concave lens, in both",
             "correct": False,
             "why": "A concave lens spreads rays apart, so neither "
             "instrument could gather the light to a point at the back with "
             "one."},
            {"text": "A flat sheet of clear glass, in both",
             "correct": False,
             "why": "A flat sheet lets the rays carry straight on without "
             "bringing them together, so no sharp picture would form."},
            {"text": "A convex lens in the camera, but no lens at all in "
             "the eye",
             "correct": False,
             "why": "The eye has a lens of its own behind the pupil, "
             "working together with the cornea in front of it."},
            {"text": "A convex lens, in both",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e26",
        "band": "easier",
        "text": "What is the vocabulary word for 'changed by light', used to "
                 "describe both a retina and a camera sensor?",
        "options": [
            {"text": "Reflective", "correct": False,
             "why": "Reflective describes bouncing light back, not being "
             "changed by it."},
            {"text": "Refractive", "correct": False,
             "why": "Refractive describes bending light, which is the lens's "
             "job, not the absorber's."},
            {"text": "Photosensitive", "correct": True},
            {"text": "Luminous", "correct": False,
             "why": "Luminous describes something that gives out its own "
             "light, which neither a retina nor a sensor does."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e27",
        "band": "easier",
        "text": "A camera and an eye are both instruments for catching a "
                "picture, but they did not arise from the same process. "
                "Roughly how far apart in time did the two arise?",
        "options": [
            {"text": "About forty years",
             "correct": False,
             "why": "The gap is on a far longer, evolutionary timescale: "
             "eyes were working for a very long time before anyone built a "
             "machine."},
            {"text": "They arose at the same time",
             "correct": False,
             "why": "One is a product of evolution and the other of "
             "engineering, built long after, so they did not arise "
             "together."},
            {"text": "About four thousand years",
             "correct": False,
             "why": "That undercounts the scale by many orders of magnitude "
             "— the comparison is evolutionary."},
            {"text": "About four hundred million years",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e28",
        "band": "easier",
        "text": "Which part of a camera is the one that absorbs the light?",
        "options": [
            {"text": "The lens",
             "correct": False,
             "why": "The lens focuses the light onto the sensor; the sensor "
             "is what absorbs it."},
            {"text": "The aperture",
             "correct": False,
             "why": "The aperture only controls how much light gets in; it "
             "does not absorb the picture-forming light."},
            {"text": "The body",
             "correct": False,
             "why": "The body's job is to keep out stray light, not to "
             "absorb the picture-forming light."},
            {"text": "The sensor",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e29",
        "band": "easier",
        "text": "What is the eye's equivalent of a camera's aperture blades "
                 "opening and closing?",
        "options": [
            {"text": "The lens changing shape", "correct": False,
             "why": "That changes focus, not the size of the opening."},
            {"text": "The retina responding to light", "correct": False,
             "why": "The retina absorbs light; it plays no part in the size of "
             "the opening."},
            {"text": "The cornea bending light", "correct": False,
             "why": "The cornea is involved in focusing, not in controlling "
             "the opening's size."},
            {"text": "The iris opening and closing the pupil", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-e30",
        "band": "easier",
        "text": "Which of the eye's two responses to a darker room can a "
                 "camera copy?",
        "options": [
            {"text": "Neither of them", "correct": False,
             "why": "A camera's aperture opening wider is a genuine match for "
             "one of the two responses."},
            {"text": "The retina becoming more sensitive", "correct": False,
             "why": "This is the chemical response of rod and cone cells, and "
             "it is the one a plain camera has nothing to match."},
            {"text": "The pupil widening", "correct": True},
            {"text": "Both of them equally well", "correct": False,
             "why": "A camera can widen its aperture like a pupil, but has "
             "nothing to match the retina's chemical increase in sensitivity."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s08",
        "band": "standard",
        "text": "A photographer uses a camera with a wide-open aperture and "
                "a fast shutter to freeze a hummingbird's wings. Which eye "
                "control does the aperture setting match?",
        "options": [
            {"text": "The shutter, setting how long light is let in",
             "correct": False,
             "why": "That is a different control on the same camera, "
             "matched by nothing in the eye."},
            {"text": "The retina's sensitivity",
             "correct": False,
             "why": "Retinal sensitivity changes over minutes, not with a "
             "quick camera setting."},
            {"text": "The lens shape, setting the focus",
             "correct": False,
             "why": "Aperture controls the amount of light, not where the "
             "picture comes into focus."},
            {"text": "The iris, setting how much light gets in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s09",
        "band": "standard",
        "text": "A pupil widens from about 2 mm in bright sunlight to about "
                "8 mm on a moonless night. What is this widening mainly "
                "for?",
        "options": [
            {"text": "To sharpen the picture, which would otherwise blur in "
             "the dark",
             "correct": False,
             "why": "Sharpening the picture is the lens's job, done by "
             "changing shape, not by the pupil's width."},
            {"text": "To warm the eye up slightly in the cold night air, "
             "keeping it working",
             "correct": False,
             "why": "Pupil size has nothing to do with temperature; it is "
             "entirely about the amount of light."},
            {"text": "To protect the retina from bright light",
             "correct": False,
             "why": "Protecting the retina from bright light is what a "
             "NARROW pupil does; here the pupil is widening because light "
             "is scarce."},
            {"text": "To let more of the little available light reach the "
             "retina",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s10",
        "band": "standard",
        "text": "The camera's aperture varies far more, in millimetres, "
                "than the eye's pupil does across the same range of "
                "brightness. What is the reason?",
        "options": [
            {"text": "Because a camera has to work in total darkness and an "
             "eye rarely does",
             "correct": False,
             "why": "Both instruments are being compared across the exact "
             "same range of light levels."},
            {"text": "Because millimetres mean something different for "
             "glass than for a pupil",
             "correct": False,
             "why": "The unit is the same physical width in both cases."},
            {"text": "Because the camera is a bigger instrument doing the "
             "same job",
             "correct": True},
            {"text": "Because the camera's lens is much heavier and needs a "
             "bigger opening to move it",
             "correct": False,
             "why": "The size of the opening is about how much light gets "
             "in, not about supporting the weight of the lens."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s11",
        "band": "standard",
        "text": "Film cameras and digital cameras share the same first step in "
                 "forming a picture but differ afterwards. What is the difference?",
        "options": [
            {"text": "Film responds electrically; a sensor responds chemically", "correct": False,
             "why": "It is the other way round: film's response is chemical "
             "and a sensor's is electrical."},
            {"text": "Film works with black-and-white light; a sensor works "
             "with colour",
             "correct": False,
             "why": "Colour film exists and works by the same chemical "
             "principle; the real difference is what happens to the response "
             "afterwards."},
            {"text": "There is no real difference; the two work identically all "
             "the way through, from start to finish",
             "correct": False,
             "why": "They agree at the very first step but diverge afterwards, "
             "in whether the record is kept as a chemical change or converted "
             "electrically."},
            {"text": "Film keeps its record chemically; a sensor turns its "
             "response into an electrical signal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s12",
        "band": "standard",
        "text": "A student says a camera could replicate everything an eye "
                "does in darkness if it just had a wide enough aperture. "
                "What is missing from this claim?",
        "options": [
            {"text": "It ignores the retina's own rise in sensitivity",
             "correct": True},
            {"text": "It ignores that camera lenses are made of glass "
             "rather than a flexible material",
             "correct": False,
             "why": "The material of the lens has nothing to do with "
             "sensitivity in darkness."},
            {"text": "It ignores that a wide aperture can blur the picture",
             "correct": False,
             "why": "Blurring is a separate problem altogether; the real "
             "gap is the retina's own chemical rise in sensitivity."},
            {"text": "Nothing is missing — the claim is entirely correct",
             "correct": False,
             "why": "An aperture only copies the pupil's widening; it "
             "cannot copy the retina's much larger increase in sensitivity."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s13",
        "band": "standard",
        "text": "Which statement correctly compares the speed of the two "
                "responses to a sudden change from bright to dark?",
        "options": [
            {"text": "Both happen at the same speed, within about a second",
             "correct": False,
             "why": "The pupil widens in about a second, but the retina's "
             "adjustment takes several minutes — very different speeds."},
            {"text": "The pupil widens in about a second; the retina takes "
             "minutes",
             "correct": True},
            {"text": "The retina adapts in about a second; the pupil takes "
             "several minutes to widen",
             "correct": False,
             "why": "That is the two responses swapped round. The pupil is "
             "the fast one."},
            {"text": "Neither response has a fixed speed; both vary "
             "randomly",
             "correct": False,
             "why": "Both have fairly definite time-scales: about a second "
             "for the pupil, several minutes for the retina."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s14",
        "band": "standard",
        "text": "Two instruments focus by completely different mechanical "
                "means, yet a sharp picture forms in each. What must both "
                "mechanisms achieve?",
        "options": [
            {"text": "Both involve physically moving the whole instrument "
             "closer to the subject",
             "correct": False,
             "why": "Neither method moves the whole instrument; the eye "
             "changes lens shape and the camera moves its own lens "
             "internally."},
            {"text": "Both require a physical shutter to complete the focus",
             "correct": False,
             "why": "A shutter controls how long light is let in; it is not "
             "involved in the focus adjustment."},
            {"text": "Both end with the sharp picture landing exactly on "
             "the absorbing surface",
             "correct": True},
            {"text": "Both change how much light is let in, not just where "
             "it lands",
             "correct": False,
             "why": "Focusing is entirely about where the picture lands; "
             "the amount of light is controlled separately, by the iris or "
             "aperture."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s15",
        "band": "standard",
        "text": "A camera's aperture and an eye's pupil are measured at "
                "five brightness levels, from a moonless night to bright "
                "sunlight. How do the two widths compare?",
        "options": [
            {"text": "The aperture is narrower than the pupil at every "
             "level",
             "correct": False,
             "why": "It is the other way round at every one of the five "
             "levels — the aperture is always the wider of the two."},
            {"text": "The aperture is wider than the pupil at every level",
             "correct": True},
            {"text": "The two are exactly equal at every level",
             "correct": False,
             "why": "The two widths differ at every level, and the camera's "
             "is always the larger of the two."},
            {"text": "Sometimes the aperture is wider and sometimes the "
             "pupil is, depending on the brightness",
             "correct": False,
             "why": "The camera's aperture is the wider of the two at every "
             "level, not only at some of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s16",
        "band": "standard",
        "text": "A rod or cone cell responds to light with a chemical change. "
                 "What happens immediately after that?",
        "options": [
            {"text": "The chemical change sets off an electrical signal", "correct": True},
            {"text": "The chemical simply stays in the cell, unused", "correct": False,
             "why": "The chemical change is what triggers the nerve signal; it "
             "does not simply sit there."},
            {"text": "The cell reflects the light back out through the pupil", "correct": False,
             "why": "Absorbed light does not leave again; that is what "
             "absorption means."},
            {"text": "The cell changes colour permanently", "correct": False,
             "why": "The cells do not permanently change colour; they respond "
             "and reset, ready to respond again."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s17",
        "band": "standard",
        "text": "Which of these is the correct order of events when light from "
                 "a lamp reaches the retina?",
        "options": [
            {"text": "An electrical signal, then a chemical change, then "
             "absorption",
             "correct": False,
             "why": "That runs the sequence backwards — absorption has to "
             "happen first."},
            {"text": "Absorption, then a chemical change, then an electrical "
             "signal",
             "correct": True},
            {"text": "A chemical change, then absorption, then an electrical "
             "signal",
             "correct": False,
             "why": "The chemical change is caused BY absorption, so "
             "absorption must come first."},
            {"text": "An electrical signal straight away, with no chemical step", "correct": False,
             "why": "That describes a camera sensor. In the eye a chemical "
             "change always comes first."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s18",
        "band": "standard",
        "text": "A student says a camera's sensor and an eye's retina are "
                 "'basically the same thing'. What is the one genuine difference "
                 "between them?",
        "options": [
            {"text": "The sensor is at the front of the camera; the retina is "
             "at the front of the eye",
             "correct": False,
             "why": "Both sit at the BACK of their instrument, where the "
             "focused light lands."},
            {"text": "The sensor absorbs light; the retina reflects it", "correct": False,
             "why": "Both absorb the light that reaches them. Neither "
             "instrument's absorbing surface reflects it."},
            {"text": "The sensor responds electrically straight away; the "
             "retina responds chemically first",
             "correct": True},
            {"text": "There is no difference at all — they work identically", "correct": False,
             "why": "They share the same basic role but differ in whether the "
             "very first response is chemical or electrical."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s19",
        "band": "standard",
        "text": "You are warned never to look at a laser, at a welding arc "
                "or at the Sun. What do all three have in common, in terms "
                "of the physics of light and the eye?",
        "options": [
            {"text": "They are all coloured light rather than white light",
             "correct": False,
             "why": "A welding arc and sunlight are not simply coloured; "
             "the shared danger is brightness, not colour."},
            {"text": "They all involve a chemical reaction rather than "
             "light",
             "correct": False,
             "why": "All three are bright light sources; the risk described "
             "is to a light-absorbing retina."},
            {"text": "They affect the pupil, not the retina",
             "correct": False,
             "why": "The danger described is specifically to the retina at "
             "the back of the eye, not to the pupil."},
            {"text": "They can all damage the retina permanently",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s20",
        "band": "standard",
        "text": "Which comparison correctly matches how the eye and camera "
                 "each finish focusing light?",
        "options": [
            {"text": "The eye reshapes a flexible lens; the camera slides a "
             "rigid one",
             "correct": True},
            {"text": "Both slide a lens forward and back along a fixed track", "correct": False,
             "why": "Only the camera moves its lens this way; the eye instead "
             "reshapes a flexible lens."},
            {"text": "The eye slides its lens; the camera reshapes its own", "correct": False,
             "why": "That is the two methods swapped — the camera's glass lens "
             "cannot be reshaped."},
            {"text": "Neither instrument can adjust focus once built", "correct": False,
             "why": "Both instruments constantly adjust focus — that is the "
             "whole point of this part of the comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s21",
        "band": "standard",
        "text": "A camera set to a very wide aperture, in a well-lit room, "
                "over-exposes the picture — it comes out too bright. Which "
                "eye response, working normally, avoids the same problem in "
                "bright light?",
        "options": [
            {"text": "The retina becoming less sensitive",
             "correct": False,
             "why": "The retina becomes MORE sensitive in the dark; it does "
             "not dim itself separately in bright light."},
            {"text": "The iris narrowing the pupil",
             "correct": True},
            {"text": "The lens changing its shape",
             "correct": False,
             "why": "Reshaping the lens is for focus, not for controlling "
             "brightness."},
            {"text": "The optic nerve carrying a weaker signal",
             "correct": False,
             "why": "The optic nerve simply carries whatever signal it "
             "receives; it does not adjust the amount of light entering."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s22",
        "band": "standard",
        "text": "Why does an eye have no need for anything like a camera's "
                 "shutter?",
        "options": [
            {"text": "Because the eye is not exposed to any light in a dark "
             "room",
             "correct": False,
             "why": "The eye is constantly receiving light whenever it is "
             "open; a shutter is about controlling duration, which the eye "
             "never needed."},
            {"text": "Because the iris already does the shutter's exact job", "correct": False,
             "why": "The iris controls how MUCH light enters, not how LONG — "
             "that is a different control entirely."},
            {"text": "Because the retina works continuously, not in one timed "
             "exposure",
             "correct": True},
            {"text": "Because the pupil closes completely between one glance "
             "and the next",
             "correct": False,
             "why": "The pupil never closes completely; it simply narrows or "
             "widens."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s23",
        "band": "standard",
        "text": "A supermarket camera and a human eye are both watching the "
                 "same well-lit aisle. Which of the following is something only the "
                 "CAMERA does?",
        "options": [
            {"text": "Focus the incoming light with a lens", "correct": False,
             "why": "The eye also focuses light with a lens, alongside its "
             "cornea."},
            {"text": "Absorb light at the back and produce a signal", "correct": False,
             "why": "Both instruments do this — the eye chemically, the camera "
             "electrically."},
            {"text": "Control how much light gets in", "correct": False,
             "why": "The eye also controls this, using its iris and pupil."},
            {"text": "Set a fixed exposure time with a shutter", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s24",
        "band": "standard",
        "text": "Two students disagree about dark adaptation. One says it is "
                 "'just the pupil opening'. What is wrong with that claim?",
        "options": [
            {"text": "It ignores the much larger change in the retina's own "
             "sensitivity",
             "correct": True},
            {"text": "Nothing is wrong — the pupil opening is the whole of dark "
             "adaptation",
             "correct": False,
             "why": "Pupil opening is only the smaller, faster part; the "
             "retina's own sensitivity change is much bigger."},
            {"text": "It ignores that the lens also gets bigger in the dark", "correct": False,
             "why": "The lens changes shape to focus; it does not grow bigger, "
             "and this is not part of dark adaptation."},
            {"text": "It ignores that the cornea closes over in the dark", "correct": False,
             "why": "The cornea does not close; nothing about it changes with "
             "brightness."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s25",
        "band": "standard",
        "text": "Which statement about the eye's outer coat and a camera's "
                 "body is correct?",
        "options": [
            {"text": "Both are transparent, letting light through everywhere", "correct": False,
             "why": "Neither is transparent everywhere — light is meant to "
             "enter only through the pupil or the aperture."},
            {"text": "Both exist to keep light out except through one "
             "controlled opening",
             "correct": True},
            {"text": "Both focus the light before it reaches the lens", "correct": False,
             "why": "Focusing is the job of the cornea and lens, or the "
             "camera's lens — not the outer casing."},
            {"text": "The camera's body alone has this job; the eye has no "
             "equivalent",
             "correct": False,
             "why": "The eye's tough outer coat and iris do the equivalent "
             "job, keeping light out except through the pupil."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s26",
        "band": "standard",
        "text": "Why does a solar cell, mentioned alongside the retina and "
                 "camera sensor, not need a lens the way an eye or camera does?",
        "options": [
            {"text": "Because sunlight cannot be focused by a lens", "correct": False,
             "why": "Sunlight is focused by lenses all the time — for example, "
             "in a camera or a magnifying glass."},
            {"text": "Because solar cells are transparent, so light passes "
             "straight through them",
             "correct": False,
             "why": "A solar cell absorbs light to work at all; it is not "
             "transparent."},
            {"text": "Because a solar cell is not trying to form a sharp "
             "picture, only to collect energy",
             "correct": True},
            {"text": "Because a lens would block too much light from reaching "
             "it",
             "correct": False,
             "why": "A lens does not block the light it focuses; the real "
             "reason is that a solar cell has no need to form a picture."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s27",
        "band": "standard",
        "text": "A student claims that because a camera sensor gives an "
                "electrical signal 'straight away', it must be simpler than "
                "an eye. What does the eye-and-camera comparison actually "
                "show?",
        "options": [
            {"text": "That the camera is simpler because it has fewer parts "
             "overall",
             "correct": False,
             "why": "The comparison runs over the same five jobs in both "
             "instruments; neither is said to have fewer parts than the "
             "other."},
            {"text": "That the eye does not use absorption to see",
             "correct": False,
             "why": "The eye absorbs light at the retina, exactly as a "
             "camera sensor does — that is one of the five shared jobs."},
            {"text": "That electrical signals travel faster than chemical "
             "ones, in any device that carries either kind",
             "correct": False,
             "why": "No general claim about signal speeds is being made; "
             "only how the retina and the sensor first respond to the light "
             "they absorb."},
            {"text": "That the first step is the real difference here",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s28",
        "band": "standard",
        "text": "A camera's aperture and shutter are two separate controls. "
                 "Which pair of eye responses to darkness are ALSO two separate things, "
                 "rather than one?",
        "options": [
            {"text": "The pupil widening and the retina becoming more sensitive", "correct": True},
            {"text": "The lens focusing and the cornea focusing", "correct": False,
             "why": "These work together as one combined focusing action, not "
             "as two separate controls like the aperture and shutter."},
            {"text": "The iris opening and the iris closing", "correct": False,
             "why": "That is one control moving in two directions, not two "
             "separate controls like the camera's two settings."},
            {"text": "The optic nerve firing and the brain receiving the signal", "correct": False,
             "why": "These are stages in one signal pathway, not two "
             "independent controls like the camera's two settings."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s29",
        "band": "standard",
        "text": "Film cameras and digital cameras use the same "
                 "lens-and-opening system but differ at the absorbing surface. What is "
                 "genuinely shared between the two?",
        "options": [
            {"text": "Both record the picture directly as an electrical signal", "correct": False,
             "why": "Only the digital sensor does this. Film records a "
             "chemical change instead."},
            {"text": "Both focus the incoming light with a lens before it is "
             "absorbed",
             "correct": True},
            {"text": "Neither one needs a shutter", "correct": False,
             "why": "Both types of camera use a shutter to control how long "
             "light is let in."},
            {"text": "Both absorb light using a chemical reaction", "correct": False,
             "why": "That is true of film; a digital sensor's response is "
             "electrical, not chemical."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-s30",
        "band": "standard",
        "text": "A very old photograph found in an attic has faded because its "
                 "chemical record has slowly broken down over decades. What does this "
                 "tell you about how film originally worked?",
        "options": [
            {"text": "That film gave an electrical signal that has since "
             "discharged",
             "correct": False,
             "why": "Film's original response was chemical, not electrical; "
             "there is no charge to discharge."},
            {"text": "That the chemical record can itself change further over "
             "time",
             "correct": True},
            {"text": "That film pictures were not built to last, even when new", "correct": False,
             "why": "A fresh photograph is a stable, readable record; fading "
             "is a slow change happening over many years, not a sign it was "
             "never fixed."},
            {"text": "That the camera's lens had degraded, not the film", "correct": False,
             "why": "A degraded lens would blur a NEW photograph; a fading OLD "
             "photograph points to the film's own chemical record changing "
             "over time."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h08",
        "band": "harder",
        "text": "A defender of the idea that eyes emit something points out "
                "that in a photograph taken with a flash, a cat's eyes glow "
                "even brighter than in headlights. Does this support the "
                "idea that eyes emit light?",
        "options": [
            {"text": "Yes, because a flash that bright proves the glow must "
             "come from inside the eye",
             "correct": False,
             "why": "A brighter glow simply means more light was available "
             "to reflect back; the flash is the source, not the eye."},
            {"text": "No — a stronger source reflecting off the same layer "
             "gives a stronger reflection",
             "correct": True},
            {"text": "Yes, because even without any light source present a "
             "cat's eyes still glow faintly in a dark room",
             "correct": False,
             "why": "In a genuinely dark room a cat's eyes do not glow at "
             "all — there has to be light arriving to reflect."},
            {"text": "No, because cats do not have retinas like humans",
             "correct": False,
             "why": "Cats do have retinas; the mirror-like layer behind "
             "theirs is an extra structure, not a replacement for one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h09",
        "band": "harder",
        "text": "A camera sensor and a retina both eventually produce an "
                 "electrical signal, but only one of them does so directly. What does "
                 "this difference actually cost the eye?",
        "options": [
            {"text": "Nothing — the two methods are equally fast", "correct": False,
             "why": "An extra chemical step takes time; the eye's route is not "
             "as fast as a direct electrical response."},
            {"text": "A small delay, because a chemical step has to happen "
             "before the electrical one",
             "correct": True},
            {"text": "The ability to see in colour, which the direct electrical "
             "method provides",
             "correct": False,
             "why": "Colour vision in the eye comes from different cone cell "
             "types, not from the chemical-versus-electrical distinction."},
            {"text": "The ability to focus, since chemical detectors cannot be "
             "focused onto",
             "correct": False,
             "why": "Focusing happens before the light is absorbed, at the "
             "lens, and is unaffected by what the absorbing surface then does "
             "with it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h10",
        "band": "harder",
        "text": "Which single sentence best explains why both a retina and "
                "a solar cell need to absorb light rather than reflect it, "
                "to do their job?",
        "options": [
            {"text": "Because reflected light carries away the very energy "
             "each of them is meant to make use of",
             "correct": True},
            {"text": "Because reflection happens with visible light, and "
             "both devices work with other kinds too",
             "correct": False,
             "why": "Both a retina and a solar cell are being compared on "
             "visible light here, and this reason plays no part in either."},
            {"text": "Because absorbing surfaces are dark in colour",
             "correct": False,
             "why": "Colour is not the reason; a solar cell absorbs "
             "strongly regardless of how it looks, and the point is about "
             "using the light's energy."},
            {"text": "Because reflection uses more energy than absorption "
             "does",
             "correct": False,
             "why": "Reflection uses none of the light's energy at all; it "
             "is absorption that takes energy up."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h11",
        "band": "harder",
        "text": "A pinhole camera has no lens at all, just a tiny hole. It "
                 "still forms an upside-down picture on the wall opposite. What does "
                 "this tell you about the need for a lens in an eye or a camera?",
        "options": [
            {"text": "That a lens is not strictly needed for some kind of "
             "picture, though it gives a sharper one",
             "correct": True},
            {"text": "That the pinhole camera must have an invisible lens "
             "hidden inside it",
             "correct": False,
             "why": "A pinhole camera genuinely has no lens; a small enough "
             "hole alone can form a dim image."},
            {"text": "That the eye and a real camera could also work with no "
             "lens and no loss of quality",
             "correct": False,
             "why": "A pinhole image is far dimmer and less sharp than a "
             "lens-formed one; the lens is what the eye and a real camera rely "
             "on for a bright, sharp picture."},
            {"text": "That pictures are formed by absorption alone, and "
             "focusing plays no part in any of it",
             "correct": False,
             "why": "The pinhole still relies on light travelling in straight "
             "lines to form its picture; a lens is a separate, better way of "
             "directing light to a point."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h12",
        "band": "harder",
        "text": "Sunburn, photosynthesis and seeing are three examples of the "
                 "same underlying physics. What is the one thing all three definitely "
                 "have in common?",
        "options": [
            {"text": "Light delivers energy to an absorber", "correct": True},
            {"text": "All three involve a lens focusing light to a point", "correct": False,
             "why": "Neither skin nor a leaf has a lens; only the eye in this "
             "trio focuses light before it lands."},
            {"text": "All three produce an electrical signal", "correct": False,
             "why": "Sunburn is chemical damage to skin, not an electrical "
             "signal; only vision in this trio involves nerve signals."},
            {"text": "All three happen in direct sunlight", "correct": False,
             "why": "Photosynthesis and vision both work perfectly well under "
             "a lamp; sunlight is not required for any of the three."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h13",
        "band": "harder",
        "text": "A very short-sighted student says: 'my eyes must be worse "
                "at controlling light than a camera, since I need glasses.' "
                "Is this reasoning sound?",
        "options": [
            {"text": "Yes — needing glasses proves the iris is not working "
             "properly",
             "correct": False,
             "why": "Short sight is about where the picture lands relative "
             "to the retina, not about how much light the iris lets in."},
            {"text": "No — glasses are about focusing sharply on the "
             "retina, not the amount of light entering",
             "correct": True},
            {"text": "Yes — a camera rarely needs any equivalent "
             "correction, so cameras are simply the better instrument",
             "correct": False,
             "why": "Cameras are adjusted and serviced too; needing "
             "correction is not unique to eyes."},
            {"text": "No, because the eye has no lens of its own that could "
             "be blamed for any of the blurring",
             "correct": False,
             "why": "The eye does have its own lens, working alongside the "
             "cornea; it is exactly this focusing system that a "
             "short-sighted eye gets wrong."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h14",
        "band": "harder",
        "text": "A fully dark-adapted eye is thousands of times more "
                "sensitive than one that has just come indoors. A camera "
                "sensor's sensitivity, by contrast, is normally fixed by "
                "its settings before a photo is taken. What follows from "
                "this difference?",
        "options": [
            {"text": "That a camera cannot take a usable photo in the dark",
             "correct": False,
             "why": "A camera can still work in the dark by using a longer "
             "exposure or a wider aperture; sensitivity being fixed is not "
             "the same as being unusable."},
            {"text": "That the eye's sensitivity adjusts itself over time; "
             "a camera's has to be set in advance",
             "correct": True},
            {"text": "That cameras and eyes have exactly the same range of "
             "sensitivity, in every lighting condition",
             "correct": False,
             "why": "The eye's own thousands-fold change is a range no "
             "ordinary camera setting reproduces automatically."},
            {"text": "That a camera's sensor becomes damaged if used in low "
             "light",
             "correct": False,
             "why": "Low light does a sensor no harm at all; the point here "
             "is about how each instrument's sensitivity is controlled."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h15",
        "band": "harder",
        "text": "Photographic film, a retina and a solar cell all rely on "
                 "absorption. Why couldn't any of them work if the material were "
                 "instead perfectly transparent?",
        "options": [
            {"text": "Because it lets light straight through instead of taking "
             "up its energy",
             "correct": True},
            {"text": "Because transparent materials are generally too thin to "
             "hold a chemical reaction",
             "correct": False,
             "why": "Thickness is not the issue; a transparent material simply "
             "does not stop the light."},
            {"text": "Because transparent materials reflect all the light that "
             "reaches them",
             "correct": False,
             "why": "A transparent material mostly transmits light through, "
             "rather than reflecting it."},
            {"text": "Because light cannot enter a transparent material", "correct": False,
             "why": "Light enters a transparent material perfectly easily — "
             "that is exactly why it passes through rather than being "
             "absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h16",
        "band": "harder",
        "text": "Two students argue about whether a mirror could ever replace "
                 "a retina. Which statement settles it?",
        "options": [
            {"text": "A mirror reflects almost all the light, so almost none is "
             "absorbed",
             "correct": True},
            {"text": "A mirror absorbs light just as well as a retina does, so "
             "it would work equally well",
             "correct": False,
             "why": "A mirror is built specifically to reflect, not absorb; a "
             "retina has to absorb to produce any signal at all."},
            {"text": "A mirror could replace a retina if it were curved the "
             "right way",
             "correct": False,
             "why": "Curving a mirror changes where light goes, not whether it "
             "is absorbed; a mirror still reflects almost everything."},
            {"text": "A mirror and a retina do exactly the same job already", "correct": False,
             "why": "A retina absorbs light to generate a signal; a mirror "
             "sends light away again, which is the opposite behaviour."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h17",
        "band": "harder",
        "text": "The cornea does most of an eye's focusing, more than the "
                "lens does — yet the lens is the part that makes fine "
                "adjustments for near and far objects. Why is a fixed, "
                "powerful cornea combined with an adjustable, weaker lens a "
                "sensible arrangement?",
        "options": [
            {"text": "It is not sensible; a single adjustable part would "
             "work better",
             "correct": False,
             "why": "Splitting the work is not a flaw: one part does most "
             "of the fixed bending and the other makes the small adjustment "
             "that keeps changing."},
            {"text": "Because the cornea is the part that bends light; the "
             "lens plays no part in it",
             "correct": False,
             "why": "The lens does genuinely bend light too — it does the "
             "fine focusing that changes with distance."},
            {"text": "Splitting the job leaves only the small, fine "
             "adjustment to the part that keeps changing",
             "correct": True},
            {"text": "Because the cornea is inside the eye and needs "
             "protecting by the lens in front of it",
             "correct": False,
             "why": "The cornea is at the very front of the eye, in front "
             "of the lens, not protected behind it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h18",
        "band": "harder",
        "text": "A student argues that because both a retina and a camera "
                "sensor 'turn light into a signal', there is no real "
                "difference worth studying between an eye and a camera. "
                "What is the strongest objection to this?",
        "options": [
            {"text": "There is a genuine difference in the first step",
             "correct": True},
            {"text": "Cameras cannot produce any signal, so the comparison "
             "itself is meaningless",
             "correct": False,
             "why": "Cameras clearly do produce a signal, from the sensor; "
             "that is one of the five shared jobs in the comparison."},
            {"text": "Eyes produce a picture rather than any signal",
             "correct": False,
             "why": "The retina produces an electrical signal, which is "
             "what travels along the optic nerve to the brain."},
            {"text": "There is no objection to make; the student is right "
             "that no real difference exists",
             "correct": False,
             "why": "Several real differences are described — the "
             "chemical-versus-electrical first step, dark adaptation, and "
             "how each one focuses."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h19",
        "band": "harder",
        "text": "At what point does light from a lamp finally stop being "
                "light and become something else, in the chain that ends "
                "with a chemical change in the retina?",
        "options": [
            {"text": "The moment it reflects off the object being looked at",
             "correct": False,
             "why": "Reflected light is still light; it only changes form "
             "once it is absorbed."},
            {"text": "The moment it is absorbed by the rod and cone cells",
             "correct": True},
            {"text": "The moment it passes through the pupil",
             "correct": False,
             "why": "Passing through an opening does not change light in "
             "any way — it is still travelling as light."},
            {"text": "The moment it is refracted by the cornea",
             "correct": False,
             "why": "Refraction bends light's path; it does not convert it "
             "into anything else."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h20",
        "band": "harder",
        "text": "Why can a camera's aperture and an eye's pupil be given in "
                "the same unit — millimetres — even though a camera is a "
                "manufactured object and an eye is a living one?",
        "options": [
            {"text": "Because both are simply openings with a physical "
             "width",
             "correct": True},
            {"text": "Because manufactured and living things share the same "
             "units in physics",
             "correct": False,
             "why": "Units depend on what is being measured, not on what "
             "kind of thing is doing the measuring; here it happens to be a "
             "width in both cases."},
            {"text": "Because the eye is itself a kind of camera built "
             "entirely from glass",
             "correct": False,
             "why": "The eye's lens and other parts are living tissue, not "
             "glass; only the underlying physics of focusing is shared with "
             "a camera."},
            {"text": "Because millimetres are used for round openings",
             "correct": False,
             "why": "Millimetres measure any length; there is nothing "
             "special about round openings."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h21",
        "band": "harder",
        "text": "Of a camera's three main controls — its aperture, its shutter "
                 "speed and its lens position — which one controls how WIDE the opening "
                 "is, rather than how long it stays open or where the picture focuses?",
        "options": [
            {"text": "Shutter speed", "correct": False,
             "why": "Shutter speed sets how LONG the opening stays open, not "
             "how wide it is."},
            {"text": "The aperture", "correct": True},
            {"text": "The lens's position", "correct": False,
             "why": "Moving the lens changes where the picture is sharp, not "
             "the width of the opening."},
            {"text": "None of them — width is fixed on every camera", "correct": False,
             "why": "The aperture is specifically the adjustable control for "
             "the width of the opening."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h22",
        "band": "harder",
        "text": "A student says: 'A camera copies an eye perfectly, because it "
                 "has all five of the same parts.' What is the flaw in this claim, "
                 "considering the whole lesson?",
        "options": [
            {"text": "The methods often differ, as with absorption", "correct": True},
            {"text": "It ignores that a camera has no lens", "correct": False,
             "why": "A camera clearly has a lens, doing the same bending job "
             "as the eye's cornea and lens together."},
            {"text": "It ignores that the eye has no equivalent of a camera's "
             "body",
             "correct": False,
             "why": "The eye's tough outer coat and iris do the equivalent job "
             "of keeping light out except through the pupil."},
            {"text": "It is not flawed — the two instruments work in identical "
             "ways at every step",
             "correct": False,
             "why": "Several steps differ in method even though the underlying "
             "jobs match, such as the chemical-versus-electrical first "
             "response."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h23",
        "band": "harder",
        "text": "A camera's shutter is a control with no equivalent in the "
                "eye. Suppose a future artificial eye were built with a "
                "shutter-like control. What would it let the eye do that it "
                "currently cannot?",
        "options": [
            {"text": "See in a completely dark room with no light source "
             "present anywhere in it",
             "correct": False,
             "why": "A shutter controls duration of exposure to existing "
             "light; it cannot create a picture with no light present at "
             "all."},
            {"text": "Choose how long light is let in, rather than "
             "receiving it continuously",
             "correct": True},
            {"text": "Focus on near and far objects",
             "correct": False,
             "why": "Focusing is already handled by the eye's own lens "
             "changing shape; a shutter has nothing to do with focus."},
            {"text": "Control how much light gets in",
             "correct": False,
             "why": "The iris already does this; a shutter's job is timing, "
             "not amount."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h24",
        "band": "harder",
        "text": "A student notices that a fully dilated pupil, about 8 mm "
                "across, is still much narrower than a camera's widest "
                "aperture, about 50 mm, at the same darkness. Does this "
                "mean the eye is a worse instrument in the dark?",
        "options": [
            {"text": "Yes, definitely — a narrower opening means a worse "
             "instrument",
             "correct": False,
             "why": "The eye compensates with its retina's huge sensitivity "
             "increase, which the raw opening width does not capture."},
            {"text": "No — the retina's own rise in sensitivity makes up "
             "much of the difference",
             "correct": True},
            {"text": "Yes, because a smaller eye cannot see as well as a "
             "bigger camera in any conditions",
             "correct": False,
             "why": "The comparison here is specifically about DARK "
             "conditions, where the retina's sensitivity plays a large part "
             "that size alone does not decide."},
            {"text": "No, because millimetre measurements are not "
             "comparable between a camera and an eye",
             "correct": False,
             "why": "Both are genuine physical widths in millimetres and "
             "can be compared directly; the real answer is about the "
             "retina's added sensitivity."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h25",
        "band": "harder",
        "text": "A simplified cross-section of an eye leaves out several "
                "real structures and reduces others to a single line. Why "
                "does that not undermine the comparison the drawing is "
                "there to make?",
        "options": [
            {"text": "Because the point is about the shared five jobs, not "
             "every real structure",
             "correct": True},
            {"text": "Because none of the missing structures are real — "
             "they were invented for the diagram",
             "correct": False,
             "why": "The missing structures, such as the retina in full "
             "anatomical detail, are entirely real; they are simplified in "
             "the drawing, not invented."},
            {"text": "Because a simplified diagram need not be accurate "
             "about anything in it",
             "correct": False,
             "why": "The diagram is still accurate about the five shared "
             "jobs and how the light travels; it simplifies detail rather "
             "than being generally inaccurate."},
            {"text": "Because the eye being described is not a real human "
             "eye",
             "correct": False,
             "why": "The eye in the comparison is a genuine, if simplified, "
             "human eye, and the camera beside it is a genuine camera."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h26",
        "band": "harder",
        "text": "A rival model claims a camera and an eye share six jobs, not "
                 "five, by also counting 'choosing how long to expose the picture' as "
                 "shared. What is wrong with counting this as shared?",
        "options": [
            {"text": "Nothing is wrong; both instruments already do this "
             "equally well",
             "correct": False,
             "why": "The eye has no timing control at all — this is exactly "
             "the extra control described elsewhere as unique to the camera."},
            {"text": "Only the camera can control how long light is let in", "correct": True},
            {"text": "The eye has this control instead, through the retina's "
             "chemical sensitivity",
             "correct": False,
             "why": "Retinal sensitivity is about how strongly the eye "
             "responds, not about timing a fixed exposure the way a shutter "
             "does."},
            {"text": "Neither instrument can control timing in any way", "correct": False,
             "why": "A camera's shutter is exactly a timing control; only the "
             "eye lacks one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h27",
        "band": "harder",
        "text": "Which single physical process underlies photographic film, "
                "a camera sensor, a retina and a solar cell alike?",
        "options": [
            {"text": "Refraction, the bending of light at a boundary",
             "correct": False,
             "why": "Refraction is bending light on the way in, done by "
             "lenses; none of these four devices is doing the bending."},
            {"text": "Absorption, converting light's energy into another "
             "form",
             "correct": True},
            {"text": "Reflection, sending light back the way it came",
             "correct": False,
             "why": "None of the four works by sending light back out; each "
             "one is built to take it in instead."},
            {"text": "Dispersion, the fanning apart of a beam's colours",
             "correct": False,
             "why": "Dispersion is the fanning apart of colours by a prism, "
             "which plays no part in any of these four absorbing devices."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h28",
        "band": "harder",
        "text": "A designer proposes replacing a camera's glass lens with a "
                 "flexible material that muscles could squeeze fatter or "
                 "thinner. What would this let the camera do that it "
                 "currently cannot?",
        "options": [
            {"text": "Focus by reshaping in place, with no moving parts", "correct": True},
            {"text": "Absorb light directly, with no separate sensor", "correct": False,
             "why": "Reshaping the lens changes how light is focused; it does "
             "not remove the need for something to absorb the focused light."},
            {"text": "See colours it currently cannot see", "correct": False,
             "why": "Colour response depends on the sensor, not on how the "
             "lens is shaped or moved."},
            {"text": "Work without any aperture", "correct": False,
             "why": "Controlling how much light gets in is a separate job from "
             "focusing, and would still need doing regardless of the lens "
             "material."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h29",
        "band": "harder",
        "text": "A photographer says that a very bright studio flash makes "
                 "their camera's aperture setting almost irrelevant. Is that a fair "
                 "thing to say?",
        "options": [
            {"text": "No — the aperture still decides how much light reaches "
             "the sensor",
             "correct": True},
            {"text": "Yes — once there is enough light, the size of the opening "
             "no longer matters",
             "correct": False,
             "why": "A narrower or wider opening always changes how much light "
             "gets through, regardless of how bright the source is."},
            {"text": "Yes — bright flashes bypass the aperture entirely and "
             "reach the sensor directly",
             "correct": False,
             "why": "All light entering the camera has to pass through the "
             "same opening; nothing bypasses it."},
            {"text": "No, because a flash works with cameras that have no "
             "aperture",
             "correct": False,
             "why": "The flash is simply a very bright light source; the "
             "camera's aperture still controls it exactly as with any other "
             "light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-05-h30",
        "band": "harder",
        "text": "An eye and a camera arose by completely different "
                "processes, at completely different times, yet share the "
                "same five jobs. Which statement best captures why that is "
                "significant rather than a coincidence?",
        "options": [
            {"text": "Because the same physics of light constrains any "
             "solution to the same problem",
             "correct": True},
            {"text": "Because both were designed by the same people, "
             "working at much the same time as each other",
             "correct": False,
             "why": "The eye was not designed by anybody, and it was doing "
             "its job long before the first camera was built."},
            {"text": "Because it is simply a coincidence with no "
             "explanation available",
             "correct": False,
             "why": "There is an explanation, and it is the opposite of "
             "coincidence: the shared jobs follow from the physics of light "
             "itself."},
            {"text": "Because cameras were deliberately built by studying "
             "the inside of an eye in great detail",
             "correct": False,
             "why": "What the two share is the physics they both have to "
             "obey, not a camera design copied from anatomy."},
        ],
        "figure": None,
    },
]
