# -*- coding: utf-8 -*-
"""Why things look coloured (colours and filters), in the lean shape.
Spec table: docs/lessons/wave2/ks3-why-things-look-coloured.md."""

LESSON = {
    "slug": "why-things-look-coloured",
    "start": {
        "setup": "A green lamp is the only light in a room. A white shirt looks green. Then someone "
                 "walks in wearing a red jumper.",
        "question": "If you had to guess, what colour does the red jumper look now?",
        "options": [
            ("Almost black",
             "Right. A red jumper can only reflect red light, and a green lamp gives none."),
            ("Still red",
             "It looks red in daylight. Under a green lamp, no red light arrives, so it looks almost black."),
        ],
        "answer": 0,
    },
    "words": ["reflect", "absorb", "filter"],
    "word_defs": {
        "reflect": "To send light back from a surface.",
        "absorb": "To take in light. Its energy warms the material slightly.",
        "filter": "A coloured sheet that lets its own colour through and absorbs the other colours.",
    },
    "knowledge": [
        {"kind": "card", "title": "Seeing colour",
         "body": [{"figure": "p7-colour-white"},
                  "White light has every colour in it. These diagrams show three: red, green and blue.",
                  "A coloured object reflects its own colour and absorbs the other colours.",
                  "A red jumper reflects red light and absorbs the rest.",
                  "Only the red light reaches your eye, so the jumper looks red."]},
        {"kind": "card", "title": "White and black objects",
         "body": ["A white object reflects all colours, so it looks white in white light.",
                  "Under coloured light, a white object looks the colour of the light.",
                  "A black object absorbs all colours, so it looks black under any light.",
                  "Absorbed light warms an object. This is why dark clothes get hot in the sun."]},
        {"kind": "card", "title": "Coloured light on a coloured object",
         "body": [{"figure": "p7-colour-green"},
                  "You only see a colour that is in the light and that the object reflects.",
                  "A green lamp gives out only green light.",
                  "A red jumper absorbs green light, and no red light arrives for it to reflect.",
                  "Almost no light reaches your eye, so the jumper looks almost black."]},
        {"kind": "reveal", "title": "What each object looks like",
         "cols": ["Under red light", "Under green light"],
         "rows": [
             ("White shirt", "Red", "Green"),
             ("Red jumper", "Red", "Almost black"),
             ("Green bag", "Almost black", "Green"),
             ("Blue book", "Almost black", "Almost black"),
             ("Black card", "Black", "Black"),
         ]},
        {"kind": "card", "title": "Filters",
         "body": [{"figure": "p7-filter-red"},
                  "A filter lets light of its own colour through. It absorbs the other colours.",
                  "A red filter in white light lets only red light through.",
                  "It does not turn light red. It takes the other colours away.",
                  "So the light that comes out is dimmer than the light that goes in."]},
        {"kind": "card", "title": "Using filters to change how things look",
         "body": [{"figure": "p7-filter-two"},
                  "With a green filter on a white lamp, only green light shines out.",
                  "Objects then look the way they do under a green lamp.",
                  "Red light cannot get through a green filter.",
                  "So a red filter and a green filter together block almost all light."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("An object has its own colour, and light just lets you see it.",
              "The colour you see depends on the light as well as the object.", "LIGHT-25"),
             ("A red filter turns white light red.",
              "A red filter absorbs every colour except red.", "LIGHT-26"),
             ("The colour of the lamp and the colour of the object mix on the surface.",
              "Nothing mixes. You see only the colours that arrive and are reflected.", "LIGHT-27"),
             ("Under a green lamp, your eye cannot pick up the red of the jumper.",
              "No red light reaches your eye, because the lamp gives none to reflect.", "LIGHT-28"),
             ("A red filter and a green filter together let yellow light through.",
              "Together they block almost all light."),
         ]}]},
    ],
    "key_fact": "An object looks the colour of the light it reflects, and absorbs the other colours. "
                "A filter lets its own colour through and absorbs the rest.",
    "deeper": [
        {"kind": "card", "title": "Why leaves are green",
         "body": ["Chlorophyll in leaves absorbs red and blue light for photosynthesis.",
                  "It reflects green light, so leaves look green."]},
        {"kind": "card", "title": "Why it is almost black",
         "body": ["Real dyes reflect a little of many colours.",
                  "Real lamps give out a spread of colours, not one exact colour.",
                  "So an object hardly ever looks perfectly black. We say almost black."]},
        {"kind": "card", "title": "Stage lights",
         "body": ["Stage lights shine through coloured filters called gels.",
                  "A gel absorbs the colours it does not let through, so it gets warm."]},
    ],
    "try": None,
    "ks4_becomes": "Colour filters, and how objects reflect, absorb and transmit different colours.",
    "connects": {
        "Reflection: mirrors and scattering": "Rough surfaces scatter the light they reflect in all directions.",
        "Leaves built for the job": "Leaves absorb red and blue light, and reflect green.",
        "Waves on water: what a wave is": "Light is a wave, and each colour has its own frequency.",
    },
    "figures": [
        {"id": "p7-colour-white", "kind": "diagram", "status": "drawn", "art": "p7-coloured-object",
         "title": "A red jumper in white light",
         "desc": "White light, shown as a red ray, a green ray and a blue ray, each named, shines down "
                 "onto a red jumper. Only the red ray is reflected up to an eye on the right. The "
                 "green and blue rays stop at the jumper. Words under the jumper say it absorbs green "
                 "and blue. Words by the eye say it looks red.",
         "caption": "Only the reflected red light reaches the eye.",
         "data": {"lamp": "White light", "rays": ["red", "green", "blue"], "object": "red jumper",
                  "object_hue": "#C0452B", "reflects": ["red"], "absorbed": "absorbs green and blue",
                  "seen": "looks red"}},
        {"id": "p7-colour-green", "kind": "diagram", "status": "drawn", "art": "p7-coloured-object",
         "title": "A red jumper under green light",
         "desc": "Green light, shown as one green ray, named, shines down onto a red jumper. The ray "
                 "stops at the jumper and no ray goes to the eye on the right. Words under the jumper "
                 "say it absorbs green. Words by the eye say it looks almost black.",
         "caption": "No light is reflected to the eye.",
         "data": {"lamp": "Green light only", "rays": ["green"], "object": "red jumper",
                  "object_hue": "#C0452B", "reflects": ["red"], "absorbed": "absorbs green",
                  "seen": "looks almost black"}},
        {"id": "p7-filter-red", "kind": "diagram", "status": "drawn", "art": "p7-filters",
         "title": "White light through a red filter",
         "desc": "White light, shown as a red ray, a green ray and a blue ray, each named, travels to "
                 "the right into a red filter. The green and blue rays stop at the filter. Only the "
                 "red ray comes out of the other side, labelled red light only.",
         "caption": "The filter absorbs green and blue. Only red gets through.",
         "data": {"lamp": "White light", "rays": ["red", "green", "blue"], "filters": ["red"],
                  "result": ["red light only"]}},
        {"id": "p7-filter-two", "kind": "diagram", "status": "drawn", "art": "p7-filters",
         "title": "White light through a red filter and then a green filter",
         "desc": "White light, shown as a red ray, a green ray and a blue ray, each named, goes into a "
                 "red filter. Only the red ray comes out. It goes on into a green filter and stops "
                 "there. Nothing comes out of the green filter. The label says almost no light gets "
                 "through.",
         "caption": "The red filter lets through only red. The green filter absorbs red.",
         "data": {"lamp": "White light", "rays": ["red", "green", "blue"], "filters": ["red", "green"],
                  "result": ["almost no", "light gets", "through"]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Nothing mixes. The book absorbs the red light, so almost no light leaves it.",
            1: "The book can only reflect blue light that arrives. Under a red lamp, none arrives.",
            2: "A white object looks the colour of the lamp. A blue book absorbs red.",
        },
        "apply": {
            0: "Nothing changes in the shirt. Under white light it looks white again at once.",
            1: "The shirt reflects every colour. It looks green because only green light arrives.",
            3: "Under a red lamp, the same shirt looks red. The colour comes from the lamp.",
        },
    },
}
