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
    {
        "id": "p7-07-e01",
        "band": "easier",
        "text": "A green leaf in white light looks green because it…",
        "options": [
            {"text": "gives out green light of its own", "correct": False,
             "why": "A leaf is not a light source. In a dark room it "
             "disappears."},
            {"text": "absorbs the green and reflects the rest", "correct": False,
             "why": "That is the wrong way round. What reaches your eye is "
             "what it REFLECTS."},
            {"text": "turns white light into green light", "correct": False,
             "why": "Nothing converts one colour into another. The green was "
             "in the white light already."},
            {"text": "reflects the green frequencies and absorbs the rest", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e02",
        "band": "easier",
        "text": "A white shirt is put under a red lamp in a room with no other "
                 "light. It looks…",
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
             "why": "That is what a WHITE surface does. Black card absorbs the "
             "blue instead of reflecting it."},
            {"text": "white", "correct": False,
             "why": "Nothing can look white unless it is sending back a great "
             "deal of light, and this sends back almost none."},
            {"text": "black", "correct": True},
            {"text": "grey", "correct": False,
             "why": "Grey would mean a fair amount coming back. Almost nothing "
             "does."},
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
             "why": "Bouncing back is reflecting. This is the part that does "
             "not."},
            {"text": "It is absorbed, and its energy warms the surface very "
             "slightly",
             "correct": True},
            {"text": "It is destroyed", "correct": False,
             "why": "Energy is not destroyed. It ends up warming the material."},
            {"text": "It changes into the colour the surface does reflect", "correct": False,
             "why": "Nothing converts one frequency into another at an "
             "ordinary surface."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s01",
        "band": "standard",
        "text": "A green bag is put under a red lamp in a room with no other "
                 "light. What does it look like, and why?",
        "options": [
            {"text": "Green, because that is the colour of the bag", "correct": False,
             "why": "Green is what it does in white light. Under a red lamp "
             "there is no green arriving to reflect."},
            {"text": "Yellow, because red and green make yellow", "correct": False,
             "why": "Nothing is being mixed. The bag can only send back light "
             "that arrives."},
            {"text": "Almost black, because no green is arriving and it absorbs "
             "the red that is",
             "correct": True},
            {"text": "Red, because any object takes on the colour of the lamp "
             "shining on it",
             "correct": False,
             "why": "That is true of a WHITE surface. This one absorbs red "
             "rather than reflecting it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s02",
        "band": "standard",
        "text": "A red filter is held in front of a white lamp. What does the "
                 "filter do?",
        "options": [
            {"text": "Turns the white light into red light", "correct": False,
             "why": "It converts nothing. The red was in the white light "
             "already."},
            {"text": "Adds red to the light that passes through", "correct": False,
             "why": "Nothing is added, which is why the light coming out is "
             "always dimmer than the light going in."},
            {"text": "Reflects everything except the red", "correct": False,
             "why": "A filter mostly absorbs what it does not pass, which is "
             "why stage lighting gels get warm."},
            {"text": "Lets the red through and absorbs the rest", "correct": True},
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
             "equally",
             "correct": False,
             "why": "A white surface takes the colour of whatever is lighting "
             "it, so it changes with every lamp."},
            {"text": "A black card, because it absorbs almost everything "
             "whatever arrives",
             "correct": True},
            {"text": "A red jumper, which reflects the red frequencies", "correct": False,
             "why": "It looks red under the red lamp and almost black under "
             "the other two."},
            {"text": "A blue book, which reflects the blue frequencies", "correct": False,
             "why": "It looks blue under the blue lamp and almost black under "
             "the other two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s04",
        "band": "standard",
        "text": "Why does a black jumper get hotter in sunlight than a white "
                 "one?",
        "options": [
            {"text": "Because it absorbs almost all the light that lands on it, "
             "and that energy has to go somewhere",
             "correct": True},
            {"text": "Because black attracts sunlight", "correct": False,
             "why": "Nothing attracts light. The same amount lands on both."},
            {"text": "Because black wool is a thicker material", "correct": False,
             "why": "The two jumpers can be identical apart from the dye, and "
             "the black one still gets hotter."},
            {"text": "Because white reflects the heat and black reflects the "
             "light, and heat and light are two different things arriving",
             "correct": False,
             "why": "Both are reflecting or absorbing the same light. Black "
             "reflects very little of it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h01",
        "band": "harder",
        "text": "A red filter and a green filter are stacked in front of a "
                 "white lamp. What comes out, and why?",
        "options": [
            {"text": "Almost nothing, because each filter absorbs what the "
             "other lets through",
             "correct": True},
            {"text": "Yellow light, because red and green add together to give "
             "yellow light",
             "correct": False,
             "why": "Mixing red and green LIGHT gives yellow. Stacking filters "
             "subtracts instead of adding."},
            {"text": "Red light, because the first filter in the stack decides", "correct": False,
             "why": "The green filter then absorbs that red, because red is "
             "not what it passes."},
            {"text": "White light, because the two filters cancel each other "
             "out",
             "correct": False,
             "why": "Filters do not undo each other. Each one takes away more."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h02",
        "band": "harder",
        "text": "A supermarket lights its meat counter with lamps that put out "
                 "extra red. What is the physics, and what is the objection?",
        "options": [
            {"text": "The lamp dyes the meat redder, which is a chemical change "
             "nobody has agreed to",
             "correct": False,
             "why": "Nothing about the meat changes. Only the light arriving "
             "does."},
            {"text": "More red is available to reflect, so the meat looks "
             "redder — and the shopper is being shown something daylight would "
             "not show",
             "correct": True},
            {"text": "The extra red is absorbed, so the meat looks darker and "
             "therefore fresher",
             "correct": False,
             "why": "Meat reflects red rather than absorbing it, which is why "
             "more red makes it look redder, not darker."},
            {"text": "There is no physics in it — it is only a matter of taste "
             "in lighting, and any lamp would show the same meat the same way",
             "correct": False,
             "why": "There is: what you see depends on what is in the light as "
             "well as on the surface, and the lamp changes one of the two."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h03",
        "band": "harder",
        "text": "Chlorophyll absorbs red and blue strongly and reflects green. "
                 "What does the colour of a leaf tell you about photosynthesis?",
        "options": [
            {"text": "That green light drives photosynthesis best", "correct": False,
             "why": "Green is the part the leaf is throwing away, so it is the "
             "part it uses least."},
            {"text": "That leaves make green light as a waste product", "correct": False,
             "why": "Leaves make no light at all. They reflect the green that "
             "arrives."},
            {"text": "That green is the part of sunlight the leaf is worst at "
             "using, and it is thrown away",
             "correct": True},
            {"text": "That a leaf reflects every colour equally, like a white "
             "surface, and simply looks green in green light",
             "correct": False,
             "why": "Then it would look white, and take the colour of whatever "
             "lamp was on it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h04",
        "band": "harder",
        "text": "Under sodium street lamps, which put out light of almost one "
                 "colour, a red car and a blue car both look nearly black. What does "
                 "that show?",
        "options": [
            {"text": "That the paint changes colour at night", "correct": False,
             "why": "The paint is unchanged. Park under a white lamp and both "
             "colours come straight back."},
            {"text": "That eyes cannot see colour at low light levels, which is "
             "the whole explanation and has nothing to do with what the lamp is "
             "putting out",
             "correct": False,
             "why": "The eye does lose colour in very dim light, and here the "
             "street is bright — what is missing is the frequencies, not the "
             "brightness."},
            {"text": "That sodium lamps absorb the colours before they reach "
             "the cars",
             "correct": False,
             "why": "A lamp gives light out; it does not absorb on the way. It "
             "simply never put those frequencies out."},
            {"text": "That colour depends on the light as much as on the "
             "surface, and a lamp with almost nothing in it leaves almost "
             "nothing to reflect",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e05",
        "band": "easier",
        "text": "A red apple in white light looks red because it…",
        "options": [
            {"text": "turns the white light into red light", "correct": False,
             "why": "Nothing converts one colour into another; the red was "
             "already in the white light."},
            {"text": "absorbs red light and reflects the rest", "correct": False,
             "why": "Then the red would never reach your eye, and the apple "
             "would look blue-green."},
            {"text": "gives out red light of its own", "correct": False,
             "why": "An apple is not a source; in a dark room it gives out "
             "nothing at all."},
            {"text": "reflects red light and absorbs the rest", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e06",
        "band": "easier",
        "text": "A white object under a blue lamp, in a room with no other "
                 "light, looks…",
        "options": [
            {"text": "white, because white objects always look white", "correct": False,
             "why": "There is no white light arriving; only blue is available "
             "to reflect."},
            {"text": "blue", "correct": True},
            {"text": "black", "correct": False,
             "why": "A white surface reflects whatever arrives, so it sends "
             "the blue back and is clearly visible."},
            {"text": "yellow, the opposite of blue", "correct": False,
             "why": "Nothing produces the opposite colour; only what arrives "
             "can be reflected."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e07",
        "band": "easier",
        "text": "Absorbing light warms an object slightly. Which surface warms "
                 "most in the same sunlight?",
        "options": [
            {"text": "A white one, because it reflects the most", "correct": False,
             "why": "Reflected light carries its energy away again, so a white "
             "surface warms least."},
            {"text": "A shiny silver one, because metal takes in heat quickly", "correct": False,
             "why": "A shiny surface reflects most of what lands on it, so "
             "little is absorbed."},
            {"text": "A black one, because it absorbs almost all of it", "correct": True},
            {"text": "They all warm equally, because the sunlight is the same", "correct": False,
             "why": "The light arriving is the same; how much each surface "
             "keeps is what differs."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s05",
        "band": "standard",
        "text": "A blue book is put under a blue lamp, in a room with no other "
                 "light. What does it look like?",
        "options": [
            {"text": "Black, because the lamp and the book are the same colour", "correct": False,
             "why": "Matching is exactly what makes it visible: the blue "
             "arriving is the blue it reflects."},
            {"text": "White, because the two blues add together", "correct": False,
             "why": "Colours of light do not add on a surface; the book "
             "reflects the blue that lands on it."},
            {"text": "Blue, as it does in white light", "correct": True},
            {"text": "Green, because the two colours mix on the surface", "correct": False,
             "why": "Nothing mixes on the surface. It reflects what it "
             "reflects."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s06",
        "band": "standard",
        "text": "Why does a red car look almost black under a street lamp "
                 "giving out only green light?",
        "options": [
            {"text": "Because the green light turns the red paint black", "correct": False,
             "why": "The paint is unchanged; what has changed is the light "
             "arriving at it."},
            {"text": "Because the eye cannot see red at night", "correct": False,
             "why": "The eye is fine; there is simply no red light coming back "
             "from the car."},
            {"text": "Because there is no red light arriving for it to reflect", "correct": True},
            {"text": "Because red paint reflects green light very weakly, so "
             "the car glows faintly green",
             "correct": False,
             "why": "It absorbs the green rather than reflecting it, which is "
             "why it looks nearly black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s07",
        "band": "standard",
        "text": "What does a green filter do to white light?",
        "options": [
            {"text": "It turns the white light green", "correct": False,
             "why": "It makes nothing green; it removes everything that is "
             "not."},
            {"text": "It lets green through and absorbs the rest", "correct": True},
            {"text": "It reflects green and lets the rest through", "correct": False,
             "why": "A filter is judged by what passes THROUGH it, and that is "
             "the green."},
            {"text": "It adds green to whatever passes through it", "correct": False,
             "why": "Nothing is added; a filter can only take frequencies "
             "away."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h05",
        "band": "harder",
        "text": "Under a yellow lamp a white page looks yellow and a black one "
                 "still looks black. Explain both.",
        "options": [
            {"text": "White reflects whatever arrives; black absorbs almost all "
             "of it either way",
             "correct": True},
            {"text": "White adds yellow to the light; black cannot add anything", "correct": False,
             "why": "No surface adds anything to light. Both only reflect or "
             "absorb."},
            {"text": "The yellow lamp bleaches the white page and not the black "
             "one",
             "correct": False,
             "why": "Nothing is bleached; the page looks yellow only while the "
             "lamp is on."},
            {"text": "Black is not really a colour, so nothing happens to it", "correct": False,
             "why": "Something does happen: it absorbs nearly all the light "
             "and warms slightly."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h06",
        "band": "harder",
        "text": "Two jumpers look identical in a shop and clearly different in "
                 "daylight. What is the explanation?",
        "options": [
            {"text": "The daylight has changed the dye in one of the jumpers", "correct": False,
             "why": "Take them back inside and they match again, so nothing "
             "has been changed."},
            {"text": "Daylight is brighter, and brighter light always reveals "
             "more colours",
             "correct": False,
             "why": "Brightness alone does not do it; a bright lamp missing "
             "certain frequencies still hides the difference."},
            {"text": "They reflect different mixes, and the shop's light lacks "
             "the frequencies that separate them",
             "correct": True},
            {"text": "The eye adjusts to shop lighting and stops telling "
             "colours apart",
             "correct": False,
             "why": "A camera photographs the same match indoors, so it is the "
             "light rather than the eye."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h07",
        "band": "harder",
        "text": "A stage lamp gives out only red light onto a set painted in "
                 "red, green and white. What does the audience see?",
        "options": [
            {"text": "All three areas red, because the lamp is red", "correct": False,
             "why": "The green area absorbs red, so it cannot look red — it "
             "goes almost black."},
            {"text": "Red areas red, green areas almost black, white areas red", "correct": True},
            {"text": "Red areas red, green areas green, white areas white", "correct": False,
             "why": "Green and white can only reflect what arrives, and only "
             "red is arriving."},
            {"text": "Red areas black, green areas red, white areas red", "correct": False,
             "why": "A red surface under red light reflects it strongly, so it "
             "looks its brightest, not black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e08",
        "band": "easier",
        "text": "What is the vocabulary word for 'to take light in at a "
                 "surface, rather than send it back'?",
        "options": [
            {"text": "Reflect", "correct": False,
             "why": "Reflecting is sending light back, the opposite of taking "
             "it in."},
            {"text": "Refract", "correct": False,
             "why": "Refracting is bending light at a boundary, not taking it "
             "in."},
            {"text": "Absorb", "correct": True},
            {"text": "Transmit", "correct": False,
             "why": "Transmitting is letting light pass through, not taking it "
             "in."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e09",
        "band": "easier",
        "text": "What does a filter do to the light passing through it?",
        "options": [
            {"text": "Adds its own colour to the light passing through",
             "correct": False,
             "why": "A filter never adds anything; it only takes "
             "frequencies away."},
            {"text": "Makes every colour brighter",
             "correct": False,
             "why": "Light leaving a filter is always dimmer than light "
             "entering it, not brighter."},
            {"text": "Reflects every colour except its own",
             "correct": False,
             "why": "A filter mostly absorbs what it does not pass, rather "
             "than reflecting it."},
            {"text": "Lets its own colour through and absorbs the rest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e10",
        "band": "easier",
        "text": "Why is light leaving a coloured filter always dimmer than the "
                 "light that went in?",
        "options": [
            {"text": "Because the filter absorbs the frequencies it does not "
             "let through",
             "correct": True},
            {"text": "Because glass dims any light passing through it", "correct": False,
             "why": "Plain, clear glass lets nearly all frequencies through "
             "with very little dimming."},
            {"text": "Because filters convert light into heat, so less comes "
             "out",
             "correct": False,
             "why": "Only the absorbed part becomes heat; what passes through "
             "is unaffected."},
            {"text": "Because a filter reflects most of the light straight back", "correct": False,
             "why": "A filter mostly absorbs what it does not pass; it does "
             "not mainly reflect it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e11",
        "band": "easier",
        "text": "Under a lamp supplying only blue light, which becomes "
                "almost black: a white shirt or a green bag?",
        "options": [
            {"text": "The green bag, since blue is not a frequency it "
             "reflects",
             "correct": True},
            {"text": "The white shirt, since it absorbs blue strongly",
             "correct": False,
             "why": "A white shirt reflects blue too — that is exactly why "
             "it changes to match whatever lamp is on it, rather than going "
             "dark."},
            {"text": "Neither — both look their usual colour under any lamp",
             "correct": False,
             "why": "The green bag depends on green being present; with "
             "none supplied, it has nothing left to reflect."},
            {"text": "Both, since blue light makes every surface look dark",
             "correct": False,
             "why": "The white shirt reflects blue strongly and looks blue, "
             "not dark."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e12",
        "band": "easier",
        "text": "A blue book keeps its usual blue colour under a blue lamp, "
                "but not under a red one. What does this pair of results "
                "tell you about the book?",
        "options": [
            {"text": "That the book contains two different dyes, one for "
             "each lamp",
             "correct": False,
             "why": "A single reflecting behaviour explains both results: "
             "the book reflects blue and absorbs red, without needing two "
             "dyes."},
            {"text": "That the book's colour is decided entirely by the "
             "observer's eyes, not the book",
             "correct": False,
             "why": "The same book gives consistently different results "
             "depending on the lamp, which points to a property of the book "
             "and the light, not the eye."},
            {"text": "That red lamps are dimmer than blue ones",
             "correct": False,
             "why": "Lamp brightness is not being compared here; both "
             "results follow from which frequencies the book itself "
             "reflects."},
            {"text": "That the book reflects blue frequencies specifically, "
             "and has little red to reflect",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e13",
        "band": "easier",
        "text": "Light lands on an opaque coloured surface. Other than "
                "being reflected, what can happen to it?",
        "options": [
            {"text": "It can be absorbed",
             "correct": True},
            {"text": "It can turn into a different colour of light",
             "correct": False,
             "why": "A surface does not convert one frequency into another; "
             "it only reflects or absorbs what arrives."},
            {"text": "It can disappear without trace, its energy gone "
             "completely",
             "correct": False,
             "why": "Energy is not destroyed; absorbed light's energy stays "
             "in the material and warms it."},
            {"text": "It can bounce back as sound",
             "correct": False,
             "why": "Light and sound are different kinds of wave; a surface "
             "does not turn one into the other."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e14",
        "band": "easier",
        "text": "A white object and a black object are placed under the "
                "same green lamp. Which one warms up more?",
        "options": [
            {"text": "The black object, since it absorbs almost all the "
             "green",
             "correct": True},
            {"text": "The white object, because it works hard to reflect "
             "the green",
             "correct": False,
             "why": "Reflecting light does not warm a surface; absorbing it "
             "does, and white reflects almost all the green."},
            {"text": "Neither — colour has no effect on warming",
             "correct": False,
             "why": "How much a surface absorbs directly decides how much "
             "it warms; colour is exactly what decides that."},
            {"text": "Both warm by exactly the same amount",
             "correct": False,
             "why": "The white surface reflects most of the green away, so "
             "it absorbs and warms far less."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e15",
        "band": "easier",
        "text": "What happens to the energy of the light a surface absorbs?",
        "options": [
            {"text": "It vanishes completely", "correct": False,
             "why": "Energy cannot vanish; it stays in the material and warms "
             "it."},
            {"text": "It is sent back out as a different colour", "correct": False,
             "why": "An ordinary surface does not convert absorbed light into "
             "a new colour of light."},
            {"text": "It stays in the material and warms it slightly", "correct": True},
            {"text": "It travels on through the object unchanged", "correct": False,
             "why": "Light that passes through unchanged has been transmitted, "
             "not absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e16",
        "band": "easier",
        "text": "Which of these is a source of light, rather than something "
                "that can only send back the light landing on it?",
        "options": [
            {"text": "A red jumper under a bright lamp",
             "correct": False,
             "why": "A jumper only sends back light that arrives; in a room "
             "with no light in it, it shows nothing at all."},
            {"text": "A mirror in a well-lit room",
             "correct": False,
             "why": "A mirror reflects light extremely well but produces "
             "none of its own, which is why it shows nothing in the dark."},
            {"text": "A lamp that is switched on",
             "correct": True},
            {"text": "A white shirt in bright sunlight",
             "correct": False,
             "why": "A white shirt sends back nearly all the light that "
             "lands on it, but it gives out none of its own."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e17",
        "band": "easier",
        "text": "What has to be true of the light in a room before a green "
                "bag can look green?",
        "options": [
            {"text": "The light must be white, and nothing else will do",
             "correct": False,
             "why": "A green lamp on its own makes it look green too; what "
             "matters is that green is present, not that everything is."},
            {"text": "The light must be bright enough to bring the dye's "
             "colour out",
             "correct": False,
             "why": "The dye reflects green and absorbs the rest at any "
             "brightness; nothing about the bag has to be brought out."},
            {"text": "The light must contain green frequencies",
             "correct": True},
            {"text": "The light must have no red in it at all",
             "correct": False,
             "why": "Red can be present and simply absorbed by the bag; "
             "what decides the appearance is whether green is there to be "
             "reflected."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e18",
        "band": "easier",
        "text": "Which of these correctly completes: a filter can only…",
        "options": [
            {"text": "add colours that were not present before",
             "correct": False,
             "why": "A filter never adds a colour; it can only take "
             "frequencies away."},
            {"text": "make light brighter than it started",
             "correct": False,
             "why": "Light leaving a filter is always dimmer than light "
             "entering it."},
            {"text": "reflect every colour equally",
             "correct": False,
             "why": "A filter mostly absorbs the colours it does not let "
             "through, rather than reflecting them."},
            {"text": "take frequencies away from the light passing through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e19",
        "band": "easier",
        "text": "A white shirt changes from looking green to looking red "
                "when the room's lamp is switched. What has changed about "
                "the shirt itself?",
        "options": [
            {"text": "Its dye has been permanently altered by the green "
             "light",
             "correct": False,
             "why": "Switching the lamp back to white shows the shirt is "
             "unchanged; nothing about the dye is altered."},
            {"text": "Its fibres have rearranged to reflect a new colour",
             "correct": False,
             "why": "Nothing physically rearranges in the fabric; only the "
             "light arriving has changed."},
            {"text": "It has absorbed the green and released red instead",
             "correct": False,
             "why": "A surface does not convert one absorbed colour into a "
             "different reflected one."},
            {"text": "Nothing about the shirt has changed at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e20",
        "band": "easier",
        "text": "A red jumper is moved from a white-lit room into a room "
                "lit only by red light. What happens to how it looks?",
        "options": [
            {"text": "It becomes darker, since red rooms are dimmer than "
             "white ones",
             "correct": False,
             "why": "Going dark under a coloured lamp happens to surfaces "
             "that do NOT reflect that colour; a red jumper reflects red "
             "strongly in both rooms."},
            {"text": "It turns almost black, since it needs a mix of "
             "colours to be seen",
             "correct": False,
             "why": "The jumper strongly reflects the one colour that is "
             "present, red, so it stays clearly visible."},
            {"text": "It looks essentially the same shade of red in both "
             "rooms",
             "correct": True},
            {"text": "It turns white, since red combined with red gives "
             "white",
             "correct": False,
             "why": "Combining a colour with itself does not give white; "
             "white needs every visible frequency present."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e21",
        "band": "easier",
        "text": "A blue book looks blue under white light and also blue "
                "under a blue-only lamp, though the room is far dimmer "
                "under the single-colour lamp. Why does it still look "
                "clearly blue rather than almost black?",
        "options": [
            {"text": "Because the book is producing its own light to "
             "compensate for the dim room",
             "correct": False,
             "why": "The book is not a light source; whatever it shows "
             "depends only on reflecting the light supplied to it."},
            {"text": "Because blue objects are immune to changes in "
             "brightness",
             "correct": False,
             "why": "No object is immune to brightness; the book would look "
             "dimmer overall in a dimmer room, though it would remain blue "
             "as long as some blue light is present."},
            {"text": "Because dimness has no effect on colour, just on how "
             "loud a room seems",
             "correct": False,
             "why": "Dimness is about light, not sound; the book stays "
             "visibly blue because its reflected colour matches what little "
             "light is present."},
            {"text": "Because blue is exactly the frequency the dim lamp "
             "supplies",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e22",
        "band": "easier",
        "text": "What does it mean to say that a surface looks 'almost "
                "black'?",
        "options": [
            {"text": "What a surface looks like when it reflects every "
             "frequency about equally",
             "correct": False,
             "why": "That describes white, not almost black."},
            {"text": "A colour a surface has permanently, regardless of the "
             "light on it",
             "correct": False,
             "why": "Almost black depends on the light arriving; the same "
             "surface looks its usual colour under the right lamp."},
            {"text": "What a surface looks like in complete darkness",
             "correct": False,
             "why": "Almost black describes a lit surface with little to "
             "reflect, not the absence of any light at all."},
            {"text": "What a surface looks like when almost nothing it can "
             "reflect is arriving",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e23",
        "band": "easier",
        "text": "Why is 'almost black' the honest description, rather than "
                "'black', for a surface with nothing matching to reflect?",
        "options": [
            {"text": "Because real dyes and lamps are broad, not exact",
             "correct": True},
            {"text": "Because black does not exist as a colour",
             "correct": False,
             "why": "Black card genuinely does look black; the point is "
             "only about coloured surfaces under a mismatched lamp."},
            {"text": "Because 'black' is not an allowed word in this "
             "account",
             "correct": False,
             "why": "Black is a perfectly ordinary word here, used for "
             "black card itself."},
            {"text": "Because the surface is changing colour slightly",
             "correct": False,
             "why": "Nothing about the surface changes; the small amount of "
             "light reaching the eye is what varies."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e24",
        "band": "easier",
        "text": "A green bag sends back green light and takes in the other "
                "frequencies landing on it. What happens to those other "
                "frequencies, physically?",
        "options": [
            {"text": "It is destroyed",
             "correct": False,
             "why": "Energy cannot be destroyed; it stays in the material "
             "and warms it slightly."},
            {"text": "It is reflected back a second time",
             "correct": False,
             "why": "Reflected light leaves immediately; only absorbed "
             "light stays and warms the material."},
            {"text": "It is absorbed, warming the bag slightly",
             "correct": True},
            {"text": "It changes into green light before leaving",
             "correct": False,
             "why": "Absorbed frequencies are not converted into the "
             "reflected colour; they are simply taken up as warmth."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e25",
        "band": "easier",
        "text": "A stage lighting gel, a coloured filter, is used under a "
                "bright lamp for a long show and becomes noticeably warm. "
                "Why?",
        "options": [
            {"text": "Because it reflects almost all the light back at the "
             "lamp",
             "correct": False,
             "why": "A filter mostly transmits its own colour and absorbs "
             "the rest; it does not mainly reflect light back."},
            {"text": "Because the lamp heats the gel directly through the "
             "air, with no light involved",
             "correct": False,
             "why": "The warming comes from light being absorbed in the gel "
             "itself, not from heat travelling across the air to it."},
            {"text": "Because coloured plastics warm up in the dark "
             "regardless",
             "correct": False,
             "why": "The gel warms because of the light landing on it, not "
             "simply because it is dark around it."},
            {"text": "Because it absorbs the frequencies it does not "
             "transmit, and that energy warms it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e26",
        "band": "easier",
        "text": "Which best describes what a black card does to light "
                "landing on it, whatever colour that light is?",
        "options": [
            {"text": "Reflects almost all of it",
             "correct": False,
             "why": "That describes a white surface, not black card."},
            {"text": "Turns it black before sending it back",
             "correct": False,
             "why": "A surface cannot change the colour of light; it can "
             "only reflect or absorb what arrives."},
            {"text": "Transmits almost all of it straight through",
             "correct": False,
             "why": "Black card is opaque; light does not pass straight "
             "through it."},
            {"text": "Absorbs almost all of it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e27",
        "band": "easier",
        "text": "A red jumper and a green bag are both lit by the same "
                "white lamp. What do they have in common?",
        "options": [
            {"text": "Both reflect every frequency about equally, which is "
             "what makes each of them visible",
             "correct": False,
             "why": "That describes a white surface; each of these reflects "
             "mainly one colour and absorbs the others."},
            {"text": "Both absorb everything that lands on them and look "
             "black",
             "correct": False,
             "why": "Each reflects its own colour strongly, which is why it "
             "is visible in that colour, not black."},
            {"text": "Each reflects one main frequency, absorbing the rest",
             "correct": True},
            {"text": "Neither reflects nor absorbs anything",
             "correct": False,
             "why": "Every ordinary surface either reflects or absorbs the "
             "light landing on it; these two are no exception."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e28",
        "band": "easier",
        "text": "A white shirt under a red lamp and a red jumper under a "
                "red lamp are compared. What do you notice?",
        "options": [
            {"text": "Both look red, though for slightly different reasons",
             "correct": True},
            {"text": "The shirt looks red; the jumper looks black",
             "correct": False,
             "why": "The jumper reflects red strongly too, so it looks red "
             "under a red lamp, not black."},
            {"text": "Neither looks red, since red lamps make everything "
             "look black",
             "correct": False,
             "why": "A red lamp makes a surface look red whenever that "
             "surface can reflect red, which both of these can."},
            {"text": "The jumper looks red; the shirt looks white",
             "correct": False,
             "why": "There is no white light arriving in this scenario, so "
             "the shirt cannot look white."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e29",
        "band": "easier",
        "text": "Which object would you expect to look the same colour under a "
                 "red lamp, a green lamp and a blue lamp?",
        "options": [
            {"text": "A red jumper", "correct": False,
             "why": "It looks red under the red lamp and almost black under "
             "the other two."},
            {"text": "A green bag", "correct": False,
             "why": "It looks green under the green lamp and almost black "
             "under the other two."},
            {"text": "A black card", "correct": True},
            {"text": "A white shirt", "correct": False,
             "why": "A white surface takes on the colour of whatever lamp is "
             "lighting it, so it changes with each one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-e30",
        "band": "easier",
        "text": "What is the vocabulary term for a piece of coloured glass "
                "or plastic placed in front of a lamp to change which "
                "frequencies pass on?",
        "options": [
            {"text": "A lamp",
             "correct": False,
             "why": "A lamp is a light source; it does not describe "
             "something light passes through."},
            {"text": "A mirror",
             "correct": False,
             "why": "A mirror reflects light of every colour; it does not "
             "selectively absorb some and pass others."},
            {"text": "A filter",
             "correct": True},
            {"text": "A lens",
             "correct": False,
             "why": "A lens bends light to focus it; it does not "
             "selectively absorb colours."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s08",
        "band": "standard",
        "text": "A green bag and a blue book are compared under a lamp "
                "supplying only blue light. Which one looks closer to its "
                "usual white-light colour?",
        "options": [
            {"text": "The blue book, since blue is exactly the frequency it "
             "reflects",
             "correct": True},
            {"text": "The green bag, since green and blue are similar "
             "colours",
             "correct": False,
             "why": "Similarity of hue does not help; only the frequencies "
             "actually reflected matter, and the bag does not reflect blue."},
            {"text": "Both look equally close to their usual colour",
             "correct": False,
             "why": "Only the book's reflected frequency, blue, matches "
             "what the lamp supplies; the bag's does not."},
            {"text": "Neither — colour is unaffected by which lamp is used",
             "correct": False,
             "why": "Both objects' appearance clearly depends on which "
             "frequencies the lamp supplies, as their very different "
             "results here show."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s09",
        "band": "standard",
        "text": "A blue book and a black card are compared under a lamp "
                 "supplying only red light. Which one looks almost black?",
        "options": [
            {"text": "Just the black card", "correct": False,
             "why": "The blue book also has no blue arriving to reflect under "
             "this lamp, so it looks almost black too."},
            {"text": "Just the blue book", "correct": False,
             "why": "Black card absorbs nearly everything under any lamp, "
             "including this one, so it also looks almost black."},
            {"text": "Both", "correct": True},
            {"text": "Neither — both keep their usual colour under any lamp", "correct": False,
             "why": "Both lack anything to reflect under a red-only lamp: the "
             "book has no blue available, and the card reflects almost nothing "
             "regardless."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s10",
        "band": "standard",
        "text": "A white shirt is placed under a lamp giving out only green "
                "light, then the lamp is switched to red. What happens to "
                "the shirt's appearance?",
        "options": [
            {"text": "It stays exactly the same colour throughout",
             "correct": False,
             "why": "A white shirt reflects whatever arrives, so its "
             "appearance changes with the lamp."},
            {"text": "It changes from red to green",
             "correct": False,
             "why": "That is the two lamp colours the wrong way round for "
             "this sequence."},
            {"text": "It changes from black to white",
             "correct": False,
             "why": "A white shirt is never black under any single-colour "
             "lamp; it always reflects strongly."},
            {"text": "It changes from green to red",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s11",
        "band": "standard",
        "text": "A black card and a red jumper are both placed under a "
                "green lamp. What do they have in common in this light?",
        "options": [
            {"text": "Both look almost black, for different reasons",
             "correct": True},
            {"text": "Both reflect the green strongly",
             "correct": False,
             "why": "The black card absorbs almost everything, including "
             "green; only the jumper's situation differs from this."},
            {"text": "Both warm up by exactly the same amount",
             "correct": False,
             "why": "The two absorb different amounts of the arriving "
             "green, so they do not warm equally."},
            {"text": "Neither one absorbs any of the light landing on it",
             "correct": False,
             "why": "Both absorb most of the green; that is exactly why "
             "they look almost black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s12",
        "band": "standard",
        "text": "Two filters, one green and one blue, are placed one after "
                "another in a beam of white light. Roughly how bright is "
                "the light that finally emerges, compared with the original "
                "beam?",
        "options": [
            {"text": "Exactly as bright, since filters do not affect "
             "brightness",
             "correct": False,
             "why": "Each filter absorbs the frequencies it does not pass, "
             "so the beam becomes dimmer at each stage."},
            {"text": "Completely unchanged in colour, just slightly dimmer",
             "correct": False,
             "why": "With almost no overlap between green and blue, very "
             "little colour survives either filter in sequence, not just a "
             "slight dimming."},
            {"text": "Brighter, since stacking two filters concentrates the "
             "light that gets through both of them",
             "correct": False,
             "why": "Filters remove light; they do not concentrate or add "
             "to it."},
            {"text": "Much dimmer, since each filter absorbs what the other "
             "lets through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s13",
        "band": "standard",
        "text": "A red jumper is compared under two lamps, one red and one "
                "green. Under which lamp does the jumper absorb more of the "
                "light landing on it?",
        "options": [
            {"text": "The green lamp, since it cannot reflect the green "
             "arriving",
             "correct": True},
            {"text": "The red lamp, since red things absorb red strongly",
             "correct": False,
             "why": "The jumper reflects red strongly; that is why it looks "
             "red under a red lamp, not why it absorbs more."},
            {"text": "Both equally, since the jumper's dye is fixed",
             "correct": False,
             "why": "The dye is fixed, but how much it can reflect depends "
             "on which frequencies are actually arriving."},
            {"text": "Neither — a red jumper does not absorb any light",
             "correct": False,
             "why": "It absorbs whatever frequencies it does not reflect, "
             "under any lamp."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s14",
        "band": "standard",
        "text": "A student says a white shirt under a red lamp 'becomes "
                "red'. What is the more accurate way to describe this?",
        "options": [
            {"text": "The shirt has turned red, and will stay that colour "
             "afterwards too",
             "correct": False,
             "why": "Switching the lamp back to white shows the shirt is "
             "still white; nothing about the fabric changed."},
            {"text": "The shirt has absorbed the red and is now glowing",
             "correct": False,
             "why": "A white surface reflects red rather than absorbing it, "
             "which is why it looks red and not black."},
            {"text": "The shirt reflects the only frequency present; the "
             "fabric is unchanged",
             "correct": True},
            {"text": "The red lamp has dyed the shirt for as long as it "
             "stays on, and the colour washes out afterwards",
             "correct": False,
             "why": "No dye is added and nothing needs washing out; the "
             "shirt simply reflects whatever colour of light happens to "
             "reach it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s15",
        "band": "standard",
        "text": "Two identical white lamps are compared, one plain and one "
                "with a red filter in front of it. How does a black card "
                "look under each?",
        "options": [
            {"text": "White under the plain lamp, red under the filtered "
             "one",
             "correct": False,
             "why": "Black card absorbs nearly everything under any lamp; "
             "it does not turn white or red."},
            {"text": "Black under the plain lamp, red under the filtered "
             "one",
             "correct": False,
             "why": "Even with a filter changing which frequency arrives, "
             "the black card still absorbs nearly all of it."},
            {"text": "Grey under the plain lamp, black under the filtered "
             "one",
             "correct": False,
             "why": "Absorbing nearly everything gives black, not grey, and "
             "that is true under both lamps here."},
            {"text": "Black under both, since it absorbs nearly everything "
             "either way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s16",
        "band": "standard",
        "text": "Which of these correctly explains why a coloured filter "
                "dims the light passing through it?",
        "options": [
            {"text": "It reflects most of the light straight back towards "
             "the source",
             "correct": False,
             "why": "A filter mostly absorbs what it does not transmit; it "
             "does not mainly reflect light back."},
            {"text": "It spreads the light out over a wider area",
             "correct": False,
             "why": "A filter changes which frequencies pass through, not "
             "how widely the beam spreads."},
            {"text": "It slows the light down, which reduces its brightness",
             "correct": False,
             "why": "Slowing light changes its speed, not how much of it "
             "gets through a filter."},
            {"text": "It absorbs every frequency except the one it lets "
             "through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s17",
        "band": "standard",
        "text": "A red car is parked under a sodium street lamp that gives "
                "out almost one single frequency of orange-yellow light. "
                "What would you expect?",
        "options": [
            {"text": "The car looks bright red, since red lamps and red "
             "cars match well",
             "correct": False,
             "why": "A sodium lamp is not a red lamp; its narrow "
             "orange-yellow output does not match red particularly well."},
            {"text": "The car looks close to its usual colour, since orange "
             "is next to red",
             "correct": False,
             "why": "Being close in the spectrum is not the same as "
             "matching; the car can only reflect frequencies genuinely "
             "present."},
            {"text": "The car looks duller, since much of what it normally "
             "reflects is missing",
             "correct": True},
            {"text": "The car looks exactly as it does in daylight, since "
             "sodium lamps are as bright as the Sun",
             "correct": False,
             "why": "Brightness is not the issue; the range of frequencies "
             "the lamp puts out is what has narrowed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s18",
        "band": "standard",
        "text": "A white object and a black object are placed side by side "
                "under a blue lamp. Which one looks brighter to an "
                "observer?",
        "options": [
            {"text": "The white object, since it reflects almost all of the "
             "blue arriving",
             "correct": True},
            {"text": "The black object, since dark objects stand out under "
             "coloured light",
             "correct": False,
             "why": "Standing out is not the same as being bright; the "
             "black object reflects almost none of the blue arriving."},
            {"text": "Both look equally bright, since brightness depends on "
             "the lamp alone",
             "correct": False,
             "why": "How much of the arriving light is reflected also "
             "matters, and that is very different for these two surfaces."},
            {"text": "Neither is visible without white light present",
             "correct": False,
             "why": "Both are visible under the blue lamp; the white one "
             "strongly reflects it and the black one does not."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s19",
        "band": "standard",
        "text": "A green bag and a blue book are both placed under a lamp "
                "giving out only red light. What do you expect to see?",
        "options": [
            {"text": "Both look almost black, since neither reflects red",
             "correct": True},
            {"text": "The bag looks green and the book looks blue, as in "
             "white light",
             "correct": False,
             "why": "Neither green nor blue is arriving in this room; each "
             "surface can only reflect what actually arrives."},
            {"text": "Both look red, since red light dominates a scene",
             "correct": False,
             "why": "Looking red would need each surface to reflect red, "
             "and neither of these does."},
            {"text": "The bag looks red and the book stays blue",
             "correct": False,
             "why": "Neither surface reflects red; both absorb it and look "
             "almost black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s20",
        "band": "standard",
        "text": "Which single sentence best summarises what decides the "
                "colour you see on an ordinary object?",
        "options": [
            {"text": "The object's own fixed colour, which stays the same "
             "whatever light falls on it",
             "correct": False,
             "why": "The colour changes with the light available, as a red "
             "jumper looking almost black under green light shows."},
            {"text": "Whichever colour the eye happens to prefer at the "
             "time of looking",
             "correct": False,
             "why": "The eye reports what arrives; preference plays no part "
             "in which frequencies are reflected."},
            {"text": "Whatever is present in the light and not absorbed by "
             "the surface",
             "correct": True},
            {"text": "The brightness of the lamp, regardless of its colour",
             "correct": False,
             "why": "Brightness affects how much light there is; which "
             "colours can be seen depends on which frequencies are present."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s21",
        "band": "standard",
        "text": "A red filter is placed in front of a lamp that gives out only "
                 "green light. What comes through the filter?",
        "options": [
            {"text": "Red light, because the filter produces its own colour", "correct": False,
             "why": "A filter cannot produce a colour that was never present; "
             "it can only pass on frequencies that arrive."},
            {"text": "Green light, dimmed slightly", "correct": False,
             "why": "A red filter passes red and absorbs other colours; with "
             "no red arriving, there is very little left to pass."},
            {"text": "Almost no light, since no red is present to pass", "correct": True},
            {"text": "White light, since filters restore missing colours", "correct": False,
             "why": "A filter never restores anything; it only ever removes "
             "frequencies it does not pass."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s22",
        "band": "standard",
        "text": "A white shirt and a black card are both placed in a "
                "completely dark room, with no lamp switched on at all. "
                "What do you see?",
        "options": [
            {"text": "The shirt looks white and the card looks black, as "
             "normal",
             "correct": False,
             "why": "With no light in the room, nothing is arriving for "
             "either surface to reflect, so neither is visible."},
            {"text": "The card looks blacker than the shirt, so it becomes "
             "visible first",
             "correct": False,
             "why": "Neither surface can be seen with no light present, "
             "whatever colour it normally is."},
            {"text": "The shirt glows faintly white in the dark",
             "correct": False,
             "why": "A shirt is not a light source; it can only reflect "
             "light that arrives, and none is arriving."},
            {"text": "Neither is visible, because there is no light for "
             "either to reflect",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s23",
        "band": "standard",
        "text": "A green bag reflects only green light. Under which of these "
                 "lamps would it reflect the least light overall?",
        "options": [
            {"text": "A white lamp", "correct": False,
             "why": "White light contains green among its frequencies, so "
             "plenty is available to reflect."},
            {"text": "A green lamp", "correct": False,
             "why": "A green lamp supplies exactly the frequency the bag can "
             "reflect, so it reflects strongly."},
            {"text": "A red lamp", "correct": True},
            {"text": "Any lamp — the amount reflected stays the same", "correct": False,
             "why": "How much is reflected depends entirely on how much of the "
             "reflectable frequency is present in the light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s24",
        "band": "standard",
        "text": "A red jumper is lit first by a lamp giving out only green "
                "light, and then by a white lamp with a green filter over "
                "it. How does it look under each?",
        "options": [
            {"text": "Red under the filtered lamp, because a filter only "
             "tints the light passing through",
             "correct": False,
             "why": "A filter does not tint what passes; it absorbs the "
             "frequencies it does not pass, so only green leaves it."},
            {"text": "Green under the filtered lamp, because the jumper "
             "picks up the filter's colour",
             "correct": False,
             "why": "A red jumper absorbs green rather than reflecting it, "
             "so it cannot look green under either arrangement."},
            {"text": "Brighter under the filtered lamp, because a filter "
             "adds green to the beam",
             "correct": False,
             "why": "A filter never adds anything, and light leaving one is "
             "always dimmer than the light that went in."},
            {"text": "Almost black under both, since only green is arriving "
             "either way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s25",
        "band": "standard",
        "text": "A student mixes red paint and green paint together and "
                "gets a muddy brown colour. Does this contradict what "
                "happens when red and green LIGHT are mixed?",
        "options": [
            {"text": "Yes — mixing colours gives the same result, whether "
             "paint or light",
             "correct": False,
             "why": "Paint and light mix in different ways; paints "
             "subtract, absorbing more between them, while lights of "
             "different colours can add together."},
            {"text": "No — paint and light are made of the same thing, so "
             "the colours must match",
             "correct": False,
             "why": "They are not the same thing: paints subtract by "
             "absorbing more between them, while lights of different "
             "colours add together."},
            {"text": "Yes — this shows that light cannot be a mixture of "
             "frequencies",
             "correct": False,
             "why": "The claim about light is unaffected by how paint "
             "happens to mix; they are separate physical processes."},
            {"text": "No — paint and light combine by different processes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s26",
        "band": "standard",
        "text": "A white object is described as one that reflects all the "
                "visible frequencies about equally. What follows for how it "
                "looks under a lamp with only two of those frequencies "
                "present?",
        "options": [
            {"text": "It looks white regardless, since it is a white object",
             "correct": False,
             "why": "Looking white needs every frequency present; with only "
             "two available, only those two can be reflected."},
            {"text": "It absorbs both frequencies completely, since it is "
             "designed for white light alone",
             "correct": False,
             "why": "A white surface reflects strongly whatever frequencies "
             "are available; it does not specially absorb an incomplete "
             "set."},
            {"text": "It looks black, since white objects fail without a "
             "full set of frequencies",
             "correct": False,
             "why": "The object can still reflect the two frequencies that "
             "are present; it does not fail to reflect at all."},
            {"text": "It reflects only those two frequencies, and looks "
             "whatever colour results",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s27",
        "band": "standard",
        "text": "A lamp is found to give out a narrow band of yellow-green "
                 "light rather than true white light. Which object's appearance would "
                 "be least affected by this discovery?",
        "options": [
            {"text": "A red jumper", "correct": False,
             "why": "A red jumper depends heavily on red being present, which "
             "this lamp barely supplies."},
            {"text": "A blue book", "correct": False,
             "why": "A blue book depends heavily on blue being present, which "
             "this narrow lamp does not supply."},
            {"text": "A black card", "correct": True},
            {"text": "A white shirt", "correct": False,
             "why": "A white shirt's appearance depends entirely on which "
             "frequencies the lamp actually supplies, so a narrow lamp changes "
             "it a great deal."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s28",
        "band": "standard",
        "text": "A white shirt, a black card and three objects that reflect "
                "only red, only green or only blue are lit by a lamp giving "
                "out violet light alone. Which pair would look most alike "
                "in brightness?",
        "options": [
            {"text": "The red jumper and the green bag",
             "correct": False,
             "why": "Neither reflects violet, but this does not make them "
             "look alike to each other in any special way beyond both being "
             "dim."},
            {"text": "The white shirt and the black card",
             "correct": False,
             "why": "The white shirt would still reflect any violet present "
             "far more strongly than the black card would."},
            {"text": "There is no way to compare them without a real prism",
             "correct": False,
             "why": "The comparison only needs each object's known "
             "reflecting behaviour and the lamp's frequency, not a prism."},
            {"text": "The black card and any of the coloured objects",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s29",
        "band": "standard",
        "text": "A dye maker claims their new red dye 'produces' red light, "
                "rather than merely reflecting it. How could you test this "
                "claim simply?",
        "options": [
            {"text": "Shine red light on it alone and see if it looks red",
             "correct": False,
             "why": "Looking red under a red lamp is also exactly what a "
             "normal reflecting dye would do; it does not distinguish the "
             "two claims."},
            {"text": "Wash the fabric and see if the dye survives",
             "correct": False,
             "why": "Whether a dye survives washing has nothing to do with "
             "whether it produces or reflects light."},
            {"text": "Compare its exact shade of red to a colour chart",
             "correct": False,
             "why": "Matching a shade says nothing about whether the colour "
             "is produced or merely reflected."},
            {"text": "Put the dyed fabric in a dark room and see if it "
             "glows",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-s30",
        "band": "standard",
        "text": "Two students disagree about a green bag under a red lamp. "
                "One says it looks a dark reddish colour rather than pure "
                "black. Which explanation fits?",
        "options": [
            {"text": "Real dyes and lamps are broad bands, so a little red "
             "still gets reflected",
             "correct": True},
            {"text": "The bag is quietly reflecting a little red as well as "
             "its usual green",
             "correct": False,
             "why": "The reason is that the lamp and the dye are both broad "
             "bands of frequencies, not that the bag specially reflects "
             "red."},
            {"text": "The student's eyes are adjusting to the red light and "
             "inventing colour",
             "correct": False,
             "why": "The physical reason involves the dye and the lamp "
             "being broad bands; nothing about the eye is needed to explain "
             "it."},
            {"text": "The bag has slightly faded, letting more colours "
             "through than it used to",
             "correct": False,
             "why": "Fading plays no part in it; the broad-band nature of "
             "real dyes and real lamps does."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h08",
        "band": "harder",
        "text": "A manufacturer claims a fabric dye is 'pure', reflecting "
                "only one exact frequency and absorbing everything else "
                "completely. Under a lamp supplying a broad but not exact "
                "match to that frequency, what would you expect?",
        "options": [
            {"text": "It would look duller than under ideal matching light, "
             "but not black",
             "correct": True},
            {"text": "The fabric would look completely black, since no "
             "exact match is present",
             "correct": False,
             "why": "A broad-band lamp still supplies some light close to "
             "the reflected frequency, which a real dye reflects at least "
             "partially."},
            {"text": "The fabric would look exactly as bright as under "
             "perfectly matching light",
             "correct": False,
             "why": "A broad lamp not exactly matching the dye's frequency "
             "supplies less of what the dye reflects, so it looks duller."},
            {"text": "The fabric would glow with its own colour regardless "
             "of the lamp",
             "correct": False,
             "why": "An ordinary dyed fabric is not a light source; it "
             "depends entirely on what is arriving to reflect."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h09",
        "band": "harder",
        "text": "A designer wants a fabric that looks identical whatever "
                "colour lamp it is placed under. What property should the "
                "fabric have?",
        "options": [
            {"text": "It should absorb every visible frequency about "
             "equally, like black card",
             "correct": True},
            {"text": "It should reflect every visible frequency about "
             "equally, like a white surface",
             "correct": False,
             "why": "A white-type surface changes colour with every "
             "different lamp, since it reflects whatever is given to it — "
             "the opposite of staying the same."},
            {"text": "It should be dyed a single strong colour, like a pure "
             "red",
             "correct": False,
             "why": "A strongly single-coloured object looks very different "
             "under lamps that do or do not supply that colour."},
            {"text": "It should be transparent, letting all light pass "
             "straight through",
             "correct": False,
             "why": "A transparent object is not what is being lit and "
             "viewed in this comparison; nothing about it addresses looking "
             "the same under different lamps."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h10",
        "band": "harder",
        "text": "A red jumper under a green lamp can be explained using "
                "absorption and reflection alone, with no mention of the "
                "eye adjusting. Why is leaving the eye out of it justified "
                "here?",
        "options": [
            {"text": "Because the eye plays no part in vision here",
             "correct": False,
             "why": "The eye clearly matters for seeing anything; the point "
             "is narrower — that this particular failure to see red is "
             "about the light, not the eye."},
            {"text": "The failure to see red is about which frequencies are "
             "present, not the eye",
             "correct": True},
            {"text": "Because the lamp itself contains a hidden mechanism "
             "that blinds the eye to red",
             "correct": False,
             "why": "Nothing about a green lamp affects the eye directly; "
             "it simply supplies no red frequency to be reflected."},
            {"text": "Because eyes cannot detect red under any "
             "circumstances",
             "correct": False,
             "why": "Eyes detect red perfectly well whenever red light "
             "actually reaches them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h11",
        "band": "harder",
        "text": "A student argues that since a black object 'absorbs light', "
                 "and absorbing usually means keeping something, black objects should "
                 "get progressively brighter over time as they store up light. What is "
                 "wrong with this?",
        "options": [
            {"text": "Nothing is wrong; black objects do get brighter with "
             "prolonged exposure",
             "correct": False,
             "why": "Black objects do not store visible light; the absorbed "
             "energy is converted to warmth and does not accumulate as stored "
             "light."},
            {"text": "The absorbed energy is converted to warmth, not stored as "
             "light",
             "correct": True},
            {"text": "Black objects do not absorb anything", "correct": False,
             "why": "Black objects are defined here precisely by absorbing "
             "almost everything landing on them."},
            {"text": "White objects can store energy, but black ones cannot", "correct": False,
             "why": "White objects absorb very little in the first place, "
             "since they mostly reflect; storing absorbed light is not how "
             "either type behaves."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h12",
        "band": "harder",
        "text": "A banana skin reflects the red and green frequencies "
                "strongly and absorbs the blue. What would it look like "
                "under a lamp giving out only blue light?",
        "options": [
            {"text": "Yellow, exactly as it looks in white light",
             "correct": False,
             "why": "Looking yellow needs red and green light to be "
             "arriving, and under a blue lamp neither of them is present."},
            {"text": "Almost black, because the only light arriving is the "
             "one it absorbs",
             "correct": True},
            {"text": "Blue, because an object takes on the colour of the "
             "lamp lighting it",
             "correct": False,
             "why": "That is what a white surface does. This skin absorbs "
             "blue rather than reflecting it."},
            {"text": "Green, because green is one of the frequencies it can "
             "reflect",
             "correct": False,
             "why": "It can only reflect a frequency that is actually "
             "arriving, and no green is being supplied by this lamp."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h13",
        "band": "harder",
        "text": "A blue book looks almost black under both a red lamp and a "
                 "green lamp, but looks blue under a blue lamp and under white light. "
                 "What single fact about the book explains all three results at once?",
        "options": [
            {"text": "It reflects only the blue frequencies and absorbs the "
             "rest",
             "correct": True},
            {"text": "It reflects every frequency except blue", "correct": False,
             "why": "That would make it look nearly white under most lamps and "
             "dark specifically under blue, which is the opposite of what is "
             "described."},
            {"text": "It changes which frequencies it reflects depending on the "
             "lamp",
             "correct": False,
             "why": "A surface's reflecting behaviour is treated as fixed; "
             "what changes between these results is only the light arriving."},
            {"text": "It absorbs everything under every lamp without exception", "correct": False,
             "why": "If it absorbed everything, it would look black under "
             "white light and under the blue lamp too, not blue."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h14",
        "band": "harder",
        "text": "Two objects, A and B, both look almost black under a red "
                "lamp. Under a white lamp, A looks green and B looks blue. "
                "What can you conclude about how A and B will look under a "
                "green lamp?",
        "options": [
            {"text": "A will look green, and B will look almost black",
             "correct": True},
            {"text": "Both will look almost black under the green lamp too",
             "correct": False,
             "why": "A reflects green, so a green lamp supplies exactly "
             "what A can reflect — it will look green, not black."},
            {"text": "Both will look green under the green lamp",
             "correct": False,
             "why": "B reflects blue, not green, so a green lamp supplies "
             "nothing B can reflect."},
            {"text": "A will look almost black, and B will look green",
             "correct": False,
             "why": "That swaps the two objects' behaviour — A is the one "
             "that reflects green here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h15",
        "band": "harder",
        "text": "A theatre uses a single-colour lamp for a scene so that "
                "certain props seem to vanish against the background. What "
                "property must the vanishing props share with the "
                "background?",
        "options": [
            {"text": "They must be the exact same object, physically joined "
             "together",
             "correct": False,
             "why": "The props and background remain physically separate; "
             "what matters is what each one reflects, not whether they are "
             "joined."},
            {"text": "They must both absorb almost all of the lamp's single "
             "frequency",
             "correct": True},
            {"text": "They must both be painted with the exact same brand "
             "of paint",
             "correct": False,
             "why": "What decides the effect is which frequencies each "
             "surface reflects, not the paint brand."},
            {"text": "They must both be black to start with, in white light",
             "correct": False,
             "why": "An object that is a strong colour in white light can "
             "still seem to vanish if that colour is absent from the lamp, "
             "as a red object does under green light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h16",
        "band": "harder",
        "text": "A designer wants warning tape to look bright and colourful "
                 "under both daylight and the narrow orange-yellow light of sodium "
                 "street lamps at night. What property should the tape's reflecting "
                 "behaviour have?",
        "options": [
            {"text": "It should reflect just one single, narrow frequency", "correct": False,
             "why": "A single narrow frequency risks matching only one of the "
             "two lighting conditions, not both."},
            {"text": "It should reflect a broad range, including some near the "
             "sodium output",
             "correct": True},
            {"text": "It should absorb almost everything, like black card", "correct": False,
             "why": "Absorbing almost everything gives a dark, not bright, "
             "appearance under any lamp."},
            {"text": "It should change its reflecting behaviour automatically "
             "depending on the lamp",
             "correct": False,
             "why": "Ordinary materials do not change what they reflect "
             "depending on the light; the fixed reflecting behaviour is what "
             "has to suit both conditions."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h17",
        "band": "harder",
        "text": "Why is 'the light and the surface together decide the "
                "colour you see' a more complete account than 'the object "
                "has a colour'?",
        "options": [
            {"text": "Because 'the object has a colour' is simply false in "
             "every situation",
             "correct": False,
             "why": "In white light, calling a red jumper 'red' is a "
             "perfectly reasonable shorthand; the fuller account is needed "
             "to explain what happens under other lamps."},
            {"text": "The fuller account explains cases the simpler one "
             "cannot",
             "correct": True},
            {"text": "Because objects do not exist independently of light",
             "correct": False,
             "why": "Objects certainly exist without light; the point is "
             "about what colour they appear, which needs light to be "
             "present."},
            {"text": "Because just some objects have colours, and others do "
             "not",
             "correct": False,
             "why": "Every object has a fixed reflecting behaviour, "
             "described as its colour in white light; the account applies "
             "to all of them."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h18",
        "band": "harder",
        "text": "A pupil argues: 'colour cannot really be about reflection, "
                "because mirrors reflect almost everything and mirrors are "
                "not white.' What is the flaw in this argument?",
        "options": [
            {"text": "Mirrors do not reflect light",
             "correct": False,
             "why": "Reflecting light is exactly what a mirror does; that "
             "is not in dispute."},
            {"text": "A mirror reflects in an ordered way, not by "
             "scattering",
             "correct": True},
            {"text": "White objects do not reflect light either, just "
             "mirrors do",
             "correct": False,
             "why": "A white surface reflects strongly too; the difference "
             "from a mirror is how the reflected light is scattered, not "
             "whether reflection happens."},
            {"text": "Colour is unrelated to reflection, so the pupil is "
             "correct",
             "correct": False,
             "why": "Colour depends entirely on which frequencies a surface "
             "reflects; the objection about mirrors does not undo that."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h19",
        "band": "harder",
        "text": "A pigment absorbs blue and green strongly and reflects red "
                "weakly. Compare how it would look under a red lamp and "
                "under a white lamp of the same overall brightness.",
        "options": [
            {"text": "Duller under the red lamp, since weak reflection of a "
             "single available colour gives less light than a mixture",
             "correct": False,
             "why": "The red lamp puts all of its output into red, so more "
             "red is available there than in a white lamp of the same total "
             "brightness."},
            {"text": "Brighter under the red lamp, since more red is "
             "available there for it to reflect",
             "correct": True},
            {"text": "Identical in both cases, since the pigment's own weak "
             "reflection is what matters most",
             "correct": False,
             "why": "How much of the relevant frequency is arriving still "
             "changes the total amount reflected, even for a "
             "weakly-reflecting pigment."},
            {"text": "Completely black under the red lamp, since a weak "
             "reflector reflects nothing",
             "correct": False,
             "why": "Reflecting weakly still means reflecting some light, "
             "not none; the pigment would show a dim red, not black."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h20",
        "band": "harder",
        "text": "A restorer examines an old painting under a lamp missing a "
                 "narrow band of yellow frequencies. Which pigments are most at risk of "
                 "being misjudged?",
        "options": [
            {"text": "Pigments that strongly reflect frequencies far from that "
             "missing band",
             "correct": False,
             "why": "Those pigments are barely affected, since the light they "
             "depend on is still present."},
            {"text": "Pigments that depend heavily on that missing yellow band", "correct": True},
            {"text": "Just pigments that are pure black or pure white", "correct": False,
             "why": "Black and white are the least affected in general, since "
             "black reflects almost nothing regardless and white reflects "
             "whatever remains."},
            {"text": "No pigments are at risk, since paintings are lit "
             "correctly",
             "correct": False,
             "why": "The scenario is precisely about a lamp with a gap in it, "
             "which can mislead judgement of any pigment depending on that "
             "gap."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h21",
        "band": "harder",
        "text": "Two surfaces, X and Y, look identical shades of orange under "
                 "a shop's lighting, but X looks noticeably more red and Y more yellow "
                 "in daylight. What must be true of their reflecting behaviour?",
        "options": [
            {"text": "X and Y must reflect exactly the same frequencies as each "
             "other",
             "correct": False,
             "why": "If they reflected identically, they would also match in "
             "daylight, which they do not."},
            {"text": "X and Y reflect different mixtures that just happen to "
             "look alike here",
             "correct": True},
            {"text": "The shop's lighting must be adding a matching orange tint "
             "to both surfaces",
             "correct": False,
             "why": "A lamp does not add colour to a surface; it only supplies "
             "which frequencies are available to be reflected."},
            {"text": "X and Y must be made of the exact same dye", "correct": False,
             "why": "The same dye would match under every lighting, including "
             "daylight, which is not what happens here."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h22",
        "band": "harder",
        "text": "A costume designer is warned that what looks right under "
                "the rehearsal room's lamps might not look right under the "
                "stage lights. What is the underlying reason?",
        "options": [
            {"text": "Rehearsal rooms and stages are different sizes, which "
             "changes how colour works",
             "correct": False,
             "why": "Room size has nothing to do with which frequencies a "
             "lamp supplies or a fabric reflects."},
            {"text": "Different lamps supply different mixtures, so the "
             "same costume reflects differently",
             "correct": True},
            {"text": "Costumes change their own dye chemically between "
             "rehearsal and performance",
             "correct": False,
             "why": "Nothing about a costume's dye changes on its own; what "
             "changes is the light falling on it."},
            {"text": "Actors move differently under stage lights, which "
             "affects how colours appear",
             "correct": False,
             "why": "Movement affects nothing about which frequencies are "
             "present or reflected; the lighting itself is what differs."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h23",
        "band": "harder",
        "text": "A black card looks black in a completely dark room, and "
                "looks black again under a bright white lamp. What is "
                "genuinely different between the two situations?",
        "options": [
            {"text": "Nothing at all is different; the card is simply black "
             "in both",
             "correct": False,
             "why": "Under the lamp the card is absorbing a great deal of "
             "light and warming very slightly; in the dark there is nothing "
             "arriving for it to absorb."},
            {"text": "Under the lamp it absorbs light and warms slightly; "
             "in the dark nothing arrives at all",
             "correct": True},
            {"text": "In the dark the card reflects more of the little "
             "light there is, which is why it still looks black",
             "correct": False,
             "why": "Reflecting more would make it look lighter rather than "
             "black, and in a dark room there is no light there to reflect."},
            {"text": "Under the lamp the card gives out a small amount of "
             "light of its own, too faint to see",
             "correct": False,
             "why": "A card is not a light source at any brightness; all it "
             "ever does is reflect or absorb the light that arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h24",
        "band": "harder",
        "text": "Which of these would most convincingly demonstrate that "
                 "colour is not a fixed property of an object, to someone who doubts "
                 "it?",
        "options": [
            {"text": "Showing the object under a single lamp and describing its "
             "colour",
             "correct": False,
             "why": "A single observation cannot show that the colour changes "
             "with the light, since nothing is being varied."},
            {"text": "Showing the object under several lamps and comparing "
             "results",
             "correct": True},
            {"text": "Describing the object's colour from memory, without it "
             "present",
             "correct": False,
             "why": "A memory of one viewing shows nothing about how the "
             "object behaves under different light."},
            {"text": "Measuring the object's weight before and after being lit", "correct": False,
             "why": "Weight has no connection to which frequencies a surface "
             "reflects or absorbs."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h25",
        "band": "harder",
        "text": "A pupil claims that because a red filter and a red jumper "
                 "both 'show' red, they must work by the exact same physical process. "
                 "Evaluate this claim.",
        "options": [
            {"text": "The claim is correct; filters and dyed surfaces work "
             "identically",
             "correct": False,
             "why": "A filter transmits its colour and absorbs the rest; a "
             "jumper reflects its colour and absorbs the rest — related "
             "processes, but not the same one."},
            {"text": "The claim is false, because filters absorb light and "
             "jumpers do not absorb anything",
             "correct": False,
             "why": "Jumpers absorb too — that is exactly how they can look "
             "almost black under the wrong lamp."},
            {"text": "Both absorb what they do not pass on, but one transmits "
             "its colour and the other reflects it",
             "correct": True},
            {"text": "The claim is false, because filters work with white light "
             "alone and jumpers work with any light",
             "correct": False,
             "why": "Both a filter and a jumper respond to whatever "
             "frequencies actually arrive, whatever the source."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h26",
        "band": "harder",
        "text": "A pupil says: 'if colour depends on the light as well as "
                "the surface, then nothing really has a colour at all.' "
                "What is the best reply?",
        "options": [
            {"text": "It would agree completely; no object has any colour "
             "in any sense",
             "correct": False,
             "why": "An object's reflecting behaviour — reflects red, "
             "absorbs the rest — is a real, fixed property of it, even "
             "though the appearance depends on the light as well."},
            {"text": "Reflecting behaviour is fixed; appearance depends on "
             "the light",
             "correct": True},
            {"text": "It would say colour is entirely random and "
             "unpredictable",
             "correct": False,
             "why": "Colour can be predicted exactly, once both the light "
             "and the surface are known; nothing about it is random."},
            {"text": "It would say just white and black objects have real "
             "colours",
             "correct": False,
             "why": "Every object has a fixed, describable reflecting "
             "behaviour, not only the white and black ones."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h27",
        "band": "harder",
        "text": "Two rooms are lit by lamps both described as 'white', but "
                "one is slightly warmer, more towards red, and the other "
                "slightly cooler, more towards blue. Would a red jumper "
                "necessarily look identical in both rooms?",
        "options": [
            {"text": "Yes, because 'white' means an identical, exact "
             "mixture of frequencies",
             "correct": False,
             "why": "Two lamps can both reasonably be called white while "
             "still differing slightly in their exact mixture, exactly as "
             "this scenario describes."},
            {"text": "No — the jumper reflects red strongly, so a warmer "
             "white could make it look more vivid",
             "correct": True},
            {"text": "Yes, because a red jumper is completely unaffected by "
             "anything except pure red or pure green light",
             "correct": False,
             "why": "The jumper responds to whatever mixture of frequencies "
             "is present, including subtle differences between two whites."},
            {"text": "No, because the jumper actively detects which room it "
             "is in and adjusts its colour",
             "correct": False,
             "why": "A jumper has no mechanism for detecting anything; it "
             "simply reflects whatever frequencies happen to reach it."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h28",
        "band": "harder",
        "text": "A pupil suggests that instead of 'reflect' and 'absorb', "
                "we could just as well say a surface 'chooses' which "
                "colours to show. What is the problem with 'chooses'?",
        "options": [
            {"text": "There is no problem; 'chooses' is exactly as accurate "
             "as 'reflects'",
             "correct": False,
             "why": "'Chooses' suggests an active decision, when the "
             "process is a fixed physical response to whatever light "
             "happens to arrive."},
            {"text": "'Chooses' wrongly suggests a decision, when a surface "
             "just reflects or absorbs",
             "correct": True},
            {"text": "'Chooses' is a completely meaningless word with no "
             "dictionary definition",
             "correct": False,
             "why": "The word has a perfectly ordinary meaning; the issue "
             "is that it names the wrong kind of process for what a surface "
             "does."},
            {"text": "'Chooses' is wrong just for black and white objects, "
             "not coloured ones",
             "correct": False,
             "why": "The same objection applies to every object, not only "
             "the black and white ones."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h29",
        "band": "harder",
        "text": "A critic argues that 'the light and the surface together "
                "decide colour' cannot be tested, since you can never "
                "observe a surface with no light on it at all. How would "
                "you respond?",
        "options": [
            {"text": "The critic is right; the claim cannot be tested in "
             "any way",
             "correct": False,
             "why": "It can be tested directly, by keeping one surface and "
             "comparing how it looks under several different single-colour "
             "lamps."},
            {"text": "You can test it by fixing the surface and changing "
             "only the lamp",
             "correct": True},
            {"text": "You would need to remove the surface entirely to test "
             "the claim",
             "correct": False,
             "why": "Removing the surface would leave nothing to reflect "
             "anything; the test needs the same surface kept constant while "
             "the light varies."},
            {"text": "The claim applies just to imaginary, not real, "
             "surfaces",
             "correct": False,
             "why": "The objects it is tested on are ordinary real "
             "materials — a shirt, a jumper, a bag, a book and a card."},
        ],
        "figure": None,
    },
    {
        "id": "p7-07-h30",
        "band": "harder",
        "text": "What single physical idea explains how every ordinary "
                "object looks, under every possible lamp, at once?",
        "options": [
            {"text": "Colour is decided by what is in the light and what "
             "the surface reflects",
             "correct": True},
            {"text": "That every object quietly contains every colour, "
             "released under the right lamp",
             "correct": False,
             "why": "Nothing is released or contained secretly; a surface's "
             "reflecting behaviour is fixed, and what changes is only which "
             "frequencies the lamp supplies."},
            {"text": "That black objects are simply broken versions of "
             "white ones",
             "correct": False,
             "why": "Black and white differ in how much they absorb versus "
             "reflect; neither is a broken version of the other."},
            {"text": "That lamps physically dye anything they shine on",
             "correct": False,
             "why": "A lamp changes nothing about a surface permanently; "
             "take the object to a different lamp and its usual behaviour "
             "returns."},
        ],
        "figure": None,
    },
]
