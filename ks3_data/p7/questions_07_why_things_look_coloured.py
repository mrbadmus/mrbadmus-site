"""P7 lesson 07 — Why things look coloured: twelve questions (MRB-223).

Written against Design's page. The red-jumper-under-green hook, the
five-by-four bench and the twenty-cell grid are hers.

The discriminations, in the order the lesson builds them:

  · colour is what a surface DOES to the light landing on it
    (`LIGHT-25`);
  · a filter SUBTRACTS; it never converts one colour into another
    (`LIGHT-26`);
  · nothing mixes on the surface — what you see is an intersection, not a
    blend (`LIGHT-27`);
  · when a red object under a green lamp goes dark, the failure is in the
    LIGHT and not in the eye (`LIGHT-28`) — the harder band sits here.

⚠️ HER FLAG 10 IS HONOURED IN THE BANK TOO: every question here is
answerable from the WORDS alone. No option depends on seeing a hue.

⚠️ "ALMOST BLACK", NEVER "BLACK", wherever a surface has nothing to send
back. Her legal line explains it and it is not a hedge to be tidied.

⚠️ POSITION IS AUTHORED — 3,0,2,1 · 2,3,1,0 · 0,1,2,3, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. This lesson has no
worked example: it is a contrast and nothing in it is quantitative.
"""

UNIT = "P7"
LESSON = "why-things-look-coloured"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-07-e01",
        "band": "easier",
        "text": "A green leaf in white light looks green because it…",
        "options": [
            {"text": "gives out green light of its own", "correct": False,
             "why": "A leaf is not a light source. In a dark room it "
                    "disappears."},
            {"text": "absorbs the green and reflects the rest",
             "correct": False,
             "why": "That is the wrong way round. What reaches your eye is "
                    "what it REFLECTS."},
            {"text": "turns white light into green light", "correct": False,
             "why": "Nothing converts one colour into another. The green "
                    "was in the white light already."},
            {"text": "reflects the green frequencies and absorbs the rest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e02",
        "band": "easier",
        "text": "A white shirt is put under a red lamp in a room with no "
                "other light. It looks…",
        "options": [
            {"text": "red", "correct": True},
            {"text": "white", "correct": False,
             "why": "It can only send back what arrives, and only red is "
                    "arriving."},
            {"text": "almost black", "correct": False,
             "why": "A white surface reflects everything, so the red comes "
                    "straight back."},
            {"text": "pink", "correct": False,
             "why": "Pink would need some white light as well, and there is "
                    "none in the room."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e03",
        "band": "easier",
        "text": "A black card absorbs almost everything that lands on it. "
                "Under a blue lamp it looks…",
        "options": [
            {"text": "blue", "correct": False,
             "why": "That is what a WHITE surface does. Black card absorbs "
                    "the blue instead of reflecting it."},
            {"text": "white", "correct": False,
             "why": "Nothing can look white unless it is sending back a "
                    "great deal of light, and this sends back almost none."},
            {"text": "black", "correct": True},
            {"text": "grey", "correct": False,
             "why": "Grey would mean a fair amount coming back. Almost "
                    "nothing does."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e04",
        "band": "easier",
        "text": "What happens to the light a coloured surface does not "
                "reflect?",
        "options": [
            {"text": "It bounces back to the lamp", "correct": False,
             "why": "Bouncing back is reflecting. This is the part that "
                    "does not."},
            {"text": "It is absorbed, and its energy warms the surface very "
                     "slightly", "correct": True},
            {"text": "It is destroyed", "correct": False,
             "why": "Energy is not destroyed. It ends up warming the "
                    "material."},
            {"text": "It changes into the colour the surface does reflect",
             "correct": False,
             "why": "Nothing converts one frequency into another at an "
                    "ordinary surface."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-07-s01",
        "band": "standard",
        "text": "A green bag is put under a red lamp in a room with no "
                "other light. What does it look like, and why?",
        "options": [
            {"text": "Green, because that is the colour of the bag",
             "correct": False,
             "why": "Green is what it does in white light. Under a red lamp "
                    "there is no green arriving to reflect."},
            {"text": "Yellow, because red and green make yellow",
             "correct": False,
             "why": "Nothing is being mixed. The bag can only send back "
                    "light that arrives."},
            {"text": "Almost black, because no green is arriving and it "
                     "absorbs the red that is", "correct": True},
            {"text": "Red, because any object takes on the colour of the "
                     "lamp shining on it", "correct": False,
             "why": "That is true of a WHITE surface. This one absorbs red "
                    "rather than reflecting it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s02",
        "band": "standard",
        "text": "A red filter is held in front of a white lamp. What does "
                "the filter do?",
        "options": [
            {"text": "Turns the white light into red light",
             "correct": False,
             "why": "It converts nothing. The red was in the white light "
                    "already."},
            {"text": "Adds red to the light that passes through",
             "correct": False,
             "why": "Nothing is added, which is why the light coming out is "
                    "always dimmer than the light going in."},
            {"text": "Reflects everything except the red", "correct": False,
             "why": "A filter mostly absorbs what it does not pass, which "
                    "is why stage lighting gels get warm."},
            {"text": "Lets the red through and absorbs the rest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s03",
        "band": "standard",
        "text": "Which object looks the same under a red lamp, a green lamp "
                "and a blue one?",
        "options": [
            {"text": "A white shirt, which reflects every frequency about "
                     "equally", "correct": False,
             "why": "A white surface takes the colour of whatever is "
                    "lighting it, so it changes with every lamp."},
            {"text": "A black card, because it absorbs almost everything "
                     "whatever arrives", "correct": True},
            {"text": "A red jumper, which reflects the red frequencies",
             "correct": False,
             "why": "It looks red under the red lamp and almost black under "
                    "the other two."},
            {"text": "A blue book, which reflects the blue frequencies",
             "correct": False,
             "why": "It looks blue under the blue lamp and almost black "
                    "under the other two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s04",
        "band": "standard",
        "text": "Why does a black jumper get hotter in sunlight than a "
                "white one?",
        "options": [
            {"text": "Because it absorbs almost all the light that lands on "
                     "it, and that energy has to go somewhere",
             "correct": True},
            {"text": "Because black attracts sunlight", "correct": False,
             "why": "Nothing attracts light. The same amount lands on "
                    "both."},
            {"text": "Because black wool is a thicker material",
             "correct": False,
             "why": "The two jumpers can be identical apart from the dye, "
                    "and the black one still gets hotter."},
            {"text": "Because white reflects the heat and black reflects "
                     "the light, and heat and light are two different "
                     "things arriving", "correct": False,
             "why": "Both are reflecting or absorbing the same light. Black "
                    "reflects very little of it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-07-h01",
        "band": "harder",
        "text": "A red filter and a green filter are stacked in front of a "
                "white lamp. What comes out, and why?",
        "options": [
            {"text": "Almost nothing, because each filter absorbs what the "
                     "other lets through", "correct": True},
            {"text": "Yellow light, because red and green add together to "
                     "give yellow light", "correct": False,
             "why": "Mixing red and green LIGHT gives yellow. Stacking "
                    "filters subtracts instead of adding."},
            {"text": "Red light, because the first filter in the stack "
                     "decides", "correct": False,
             "why": "The green filter then absorbs that red, because red is "
                    "not what it passes."},
            {"text": "White light, because the two filters cancel each "
                     "other out", "correct": False,
             "why": "Filters do not undo each other. Each one takes away "
                    "more."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h02",
        "band": "harder",
        "text": "A supermarket lights its meat counter with lamps that put "
                "out extra red. What is the physics, and what is the "
                "objection?",
        "options": [
            {"text": "The lamp dyes the meat redder, which is a chemical "
                     "change nobody has agreed to", "correct": False,
             "why": "Nothing about the meat changes. Only the light "
                    "arriving does."},
            {"text": "More red is available to reflect, so the meat looks "
                     "redder — and the shopper is being shown something "
                     "daylight would not show", "correct": True},
            {"text": "The extra red is absorbed, so the meat looks darker "
                     "and therefore fresher", "correct": False,
             "why": "Meat reflects red rather than absorbing it, which is "
                    "why more red makes it look redder, not darker."},
            {"text": "There is no physics in it — it is only a matter of "
                     "taste in lighting, and any lamp would show the same "
                     "meat the same way", "correct": False,
             "why": "There is: what you see depends on what is in the light "
                    "as well as on the surface, and the lamp changes one of "
                    "the two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h03",
        "band": "harder",
        "text": "Chlorophyll absorbs red and blue strongly and reflects "
                "green. What does the colour of a leaf tell you about "
                "photosynthesis?",
        "options": [
            {"text": "That green light drives photosynthesis best",
             "correct": False,
             "why": "Green is the part the leaf is throwing away, so it is "
                    "the part it uses least."},
            {"text": "That leaves make green light as a waste product",
             "correct": False,
             "why": "Leaves make no light at all. They reflect the green "
                    "that arrives."},
            {"text": "That green is the part of sunlight the leaf is worst "
                     "at using, and it is thrown away", "correct": True},
            {"text": "That a leaf reflects every colour equally, like a "
                     "white surface, and simply looks green in green "
                     "light", "correct": False,
             "why": "Then it would look white, and take the colour of "
                    "whatever lamp was on it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h04",
        "band": "harder",
        "text": "Under sodium street lamps, which put out light of almost "
                "one colour, a red car and a blue car both look nearly "
                "black. What does that show?",
        "options": [
            {"text": "That the paint changes colour at night",
             "correct": False,
             "why": "The paint is unchanged. Park under a white lamp and "
                    "both colours come straight back."},
            {"text": "That eyes cannot see colour at low light levels, "
                     "which is the whole explanation and has nothing to do "
                     "with what the lamp is putting out", "correct": False,
             "why": "The eye does lose colour in very dim light, and here "
                    "the street is bright — what is missing is the "
                    "frequencies, not the brightness."},
            {"text": "That sodium lamps absorb the colours before they "
                     "reach the cars", "correct": False,
             "why": "A lamp gives light out; it does not absorb on the way. "
                    "It simply never put those frequencies out."},
            {"text": "That colour depends on the light as much as on the "
                     "surface, and a lamp with almost nothing in it leaves "
                     "almost nothing to reflect", "correct": True},
        ],
        "figure": None,
    },
]
