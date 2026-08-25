"""P7 L7 — Why things look coloured (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-07-why-things-look-coloured.dc.html`.

Her page wins outright. The red-jumper-under-green hook, the
five-objects-by-four-lamps bench, the twenty-cell grid and all four rungs
are hers.

── ⚖️ MRB-204 · NO BLOCK. A CONTRAST HAS NOTHING TO CALCULATE ───────

── ⚖️ RULED · "ALMOST BLACK", NEVER "BLACK" ─────────────────────────

Every state where a surface has nothing to send back reads *almost
black*, and her legal line says why: real dyes and real lamps are broad
bands, so a real red object under a real green lamp looks very dark
rather than perfectly black. The word is load-bearing and is not a hedge
to be tidied. The one place the page says plain *black* is the black card
itself, which absorbs almost everything under any lamp.

── ⚖️ THE SEEN COLOUR IS COMPUTED, NEVER AUTHORED PER CELL ──────────

Twenty states — five objects by four lamps — and the answer in every one
of them is the intersection of what the lamp CONTAINS with what the
surface REFLECTS. Computing it is what makes the note true in all twenty
by construction, including the three states nobody would think to author:
a white shirt under white light, a black card under any lamp, and the two
where the intersection is empty for two different reasons.

── ⚠️ HER FLAG 10 · HUE IS PART OF THE MESSAGE, AND IT IS NEVER ALONE ─

The object rectangle is filled with the computed seen-colour and the
outgoing ray is drawn in it — and every one of those states also names
the colour as a WORD in the readout tiles, in the caption and in the
note. When nothing comes back the ray is drawn dashed and grey as well as
being called *nothing comes back*: two channels, always.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-lamp · s-grid · s-ladder

⚠️ **`s-grid` TICKS AT THE GATE.** Marked by the bench through
`band_anchor` / `band_at`.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-25  an object has a colour, and the light just lets you see it
    LIGHT-26  a red filter turns white light red
    LIGHT-27  the lamp's colour and the object's colour mix on the surface
    LIGHT-28  you cannot see red under a green lamp — the eye is what fails

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 3 and 2.
"""

LESSON = {
    "slug":  "why-things-look-coloured",
    "title": "Why things look coloured",
    "discipline": "physics",
    "unit": "Light",
    "family": "CONTRAST",

    "covers": ["KS3.P.LGT.03b", "KS3.P.LGT.06b"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["colour-and-the-spectrum"],
    "assumes": [],
    "references": ["reflection-mirrors-and-scattering",
                   "leaves-built-for-the-job", "waves-on-water"],
    "ks4_links": [],

    "meta_description": "A red jumper under a green lamp is still a red "
                        "jumper and looks almost black. Colour is something "
                        "an object does, not something it has.",

    "big_question": "A red jumper under a green lamp is still a red jumper "
                    "and looks almost black. Colour turns out not to be "
                    "something an object has, but something it does to the "
                    "light that lands on it.",

    "rail": [
        {"anchor": "s-hook",   "short": "JUMPER",
         "label": "Red jumper, green room", "done_when": "committed"},
        {"anchor": "s-lamp",   "short": "BENCH",
         "label": "One lamp, five objects", "done_when": "gate_and_a_control"},
        {"anchor": "s-grid",   "short": "GRID",
         "label": "Every combination",      "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Take a red jumper into a room lit only in green.",
        "prompt": "A disco lamp fitted with a deep green filter is the only "
                  "light in the room. A white shirt looks green. A green bag "
                  "looks green. A red jumper looks almost black, and so does "
                  "a blue one.",
        "commit": "Nothing has been done to the jumper. Why has it stopped "
                  "being red?",
        "options": [
            "The green light has changed the dye in the jumper",
            "There is no red light in the room for the jumper to reflect, and "
            "it absorbs the green",
            "Red and green mix on the jumper to give something close to "
            "black, the way paints do",
            "Your eyes cannot see red under a green light",
        ],
        "answer": 1,
        "reveal": "A red jumper is not carrying redness around with it. It "
                  "has a dye that reflects the red frequencies and absorbs "
                  "the others, and it can only reflect what arrives. Under a "
                  "green lamp no red arrives, and the green that does is "
                  "exactly what the dye absorbs — so almost no light leaves "
                  "the surface at all.",
    },

    "misconceptions": [
        {"id": "LIGHT-25",
         "statement": "An object has a colour, and the light just lets you "
                      "see it.",
         "elicited_by": "lamp",
         "confronted_by": "s-think"},
        {"id": "LIGHT-26",
         "statement": "A red filter turns white light red.",
         "confronted_by": "s-think"},
        {"id": "LIGHT-27",
         "statement": "The lamp's colour and the object's colour mix on the "
                      "surface to give what you see.",
         "elicited_by": "s-hook",
         "confronted_by": "lamp"},
        {"id": "LIGHT-28",
         "statement": "You cannot see red under a green lamp because the eye "
                      "stops being able to, not because the light is not "
                      "there.",
         "elicited_by": "s-hook",
         "confronted_by": "colour-grid"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An object that is not itself a source of light has no "
                 "colour of its own to give off. What it does is take the "
                 "light that lands on it and split it three ways: some is "
                 "<strong>reflected</strong> back — scattered in all "
                 "directions, if the surface is rough — some is "
                 "<strong>absorbed</strong>, its energy taken up by the "
                 "material, and some may be transmitted through. What reaches "
                 "your eye is only the reflected part, and the colour you see "
                 "is the colour of <em>that</em>."},
        {"type": "explainer",
         "text": "A red jumper is red in white light because it absorbs most "
                 "of the other frequencies and reflects mostly the red ones. "
                 "Notice what that means: the red has to be in the light in "
                 "the first place. Put the same jumper under a green lamp and "
                 "there is no red arriving to reflect, and the green that is "
                 "arriving is exactly what the dye is good at absorbing. "
                 "Almost nothing leaves the surface, so it looks nearly "
                 "black."},
        {"type": "explainer",
         "text": "A white object reflects all frequencies about equally, so "
                 "it takes on the colour of whatever is lighting it. A black "
                 "object absorbs nearly all of them, whatever they are, which "
                 "is why it stays black under any lamp — and why it warms up "
                 "in sunlight, since the absorbed energy has to go "
                 "somewhere."},

        # ── #s-lamp · one dark room, one lamp, five objects ───────────
        {"type": "colour-bench",
         "id": "lamp",
         "anchor": "s-lamp",
         "eyebrow": "At the bench · one dark room, one lamp, five objects",
         "heading": "Change the object. Change the light. Two different "
                    "questions.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A single lamp with a filter in a room with no other "
                   "light, and one object under it. Set what the object is, "
                   "and set what colour the lamp is putting out.",
         "gate": {
             "prompt": "Commit first. A red jumper is put under a lamp giving "
                       "out only green light. What does it look like?",
             "options": [
                 "Red, because it is a red jumper",
                 "Almost black, because no red is arriving and it absorbs the "
                 "green that is",
                 "Green, because objects take the colour of the lamp on them",
                 "Yellow, because red and green together make yellow",
             ],
             "answer": 1,
         },
         "obj_label": "The object",
         "lamp_label": "The light falling on it",
         "lamp_glyph_label": "LAMP",
         "eye_label": "EYE",
         "objects": [
             {"id": "white", "label": "White shirt",
              "reflects": ["red", "green", "blue"], "hex": "#F2ECDD",
              "desc": "reflects all the visible frequencies about equally"},
             {"id": "redj", "label": "Red jumper", "reflects": ["red"],
              "hex": "#C0452B",
              "desc": "reflects the red frequencies and absorbs the rest"},
             {"id": "greenb", "label": "Green bag", "reflects": ["green"],
              "hex": "#3F7F42",
              "desc": "reflects the green frequencies and absorbs the rest"},
             {"id": "blueb", "label": "Blue book", "reflects": ["blue"],
              "hex": "#39599B",
              "desc": "reflects the blue frequencies and absorbs the rest"},
             {"id": "black", "label": "Black card", "reflects": [],
              "hex": "#1C1A18",
              "desc": "absorbs almost every frequency that lands on it"},
         ],
         "start_object": 1,
         "lamps": [
             {"id": "white", "label": "White",
              "has": ["red", "green", "blue"], "hex": "#F2ECDD",
              "word": "White light"},
             {"id": "red", "label": "Red", "has": ["red"], "hex": "#D9563A",
              "word": "Red light only"},
             {"id": "green", "label": "Green", "has": ["green"],
              "hex": "#5BA45C", "word": "Green light only"},
             {"id": "blue", "label": "Blue", "has": ["blue"],
              "hex": "#4F7DC4", "word": "Blue light only"},
         ],
         "start_lamp": 0,
         # The three primaries the bench computes with, each with the word it
         # is called by and the hex the object rectangle takes when that is
         # what leaves. Hue is never the only channel; the word is always
         # printed beside it.
         "seen": [
             {"id": "red", "word": "Red", "hex": "#C0452B"},
             {"id": "green", "word": "Green", "hex": "#3F7F42"},
             {"id": "blue", "word": "Blue", "hex": "#39599B"},
         ],
         "nothing_hex": "#151312",
         "white_hex": "#F2ECDD",
         "readouts": [
             {"id": "in", "label": "Falling on the object"},
             {"id": "out", "label": "Reflected back"},
             {"id": "abs", "label": "Absorbed",
              "sub": "its energy warms the object slightly"},
             {"id": "seen", "label": "What you see"},
         ],
         # Three branches, keyed to what the surface can send back: nothing,
         # everything, or some of it.
         "branches": {
             "nothing": "Nothing that arrives can leave. {lampword} is "
                        "falling on a surface that {desc}, so the {abs} is "
                        "absorbed and its energy warms the object very "
                        "slightly. With no light coming back to your eye it "
                        "looks almost black — not because it is black, but "
                        "because the light it needs is not in the room. "
                        "Switch the lamp to white and it looks {white_again}",
             "everything": "This surface {desc}, and white light contains all "
                           "of them, so all of it comes back and it looks "
                           "white. That is why a white object is the one that "
                           "always shows you the colour of the lamp: put a "
                           "green lamp on it and it looks green, because "
                           "green is now all there is to send back.",
             "some": "{lampword} is falling on a surface that {desc}. The "
                     "{out} is reflected and reaches your eye{absclause}, so "
                     "it looks {seenlower}. Nothing about the object changed "
                     "to make that happen — what you see is whatever is both "
                     "present in the light and not absorbed by the surface.",
         },
         "band_anchor": "s-grid",
         "band_at": 1},

        # ── #s-grid · every object under every lamp ───────────────────
        {"type": "light-band",
         "id": "colour-grid",
         "anchor": "s-grid",
         "eyebrow": "The figure",
         "heading": "Every object under every lamp",
         "table": {
             "aria_label": "A table of five objects against three lightings — "
                           "white light, a red lamp and a green lamp — giving "
                           "the colour each one looks. A white shirt takes "
                           "the colour of the lamp; a red jumper is almost "
                           "black under green; a blue book is almost black "
                           "under both coloured lamps; black card stays "
                           "black.",
             "columns": ["The object", "In white light", "Under a red lamp",
                         "Under a green lamp"],
             "rows": [
                 ["White shirt — reflects almost everything",
                  "White", "Red", "Green"],
                 ["Red jumper — reflects red, absorbs the rest",
                  "Red", "Red", "Almost black"],
                 ["Green bag — reflects green, absorbs the rest",
                  "Green", "Almost black", "Green"],
                 ["Blue book — reflects blue, absorbs the rest",
                  "Blue", "Almost black", "Almost black"],
                 ["Black card — absorbs almost everything",
                  "Black", "Black", "Black"],
             ],
         },
         "close": "Read across a row and you are changing the light. Read "
                  "down a column and you are changing the object. Every cell "
                  "is the same one-line rule: what you see is what is both "
                  "<em>present in the light</em> and <em>not absorbed by the "
                  "surface</em>. Where those two do not overlap, the answer "
                  "is black."},

        {"type": "key-fact", "ref": "colour-is-what-a-surface-does"},

        {"type": "misconception", "id": "think-an-object-has-a-colour",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-an-object-has-a-colour",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-25",
         "statements": [
             {"quote": "An object has a colour, and the light just lets you "
                       "see it.",
              "targets": "LIGHT-25",
              "body": [
                  "Colour is a relationship between three things — the light "
                  "arriving, the surface, and your eye — and not a property "
                  "sitting in the object waiting to be revealed. What a red "
                  "jumper actually has is a dye that absorbs most frequencies "
                  "and reflects the red ones, and that is a fact about what "
                  "it does rather than about what it is. Change the light and "
                  "the answer changes with it. This is not a trick of the "
                  "disco lamp: the same jumper looks slightly different under "
                  "a supermarket strip light, a candle and midday sunlight, "
                  "because those three are not putting out the same mixture.",
              ]},
             {"quote": "A red filter turns white light red.",
              "targets": "LIGHT-26",
              "body": [
                  "It removes everything else. A filter is a subtracter: it "
                  "lets its own colour through and absorbs the rest, which is "
                  "why the light coming out of one is always dimmer than the "
                  "light going in, and why stacking a red filter and a green "
                  "one gives you almost nothing rather than yellow. The "
                  "energy that does not come out has not been converted into "
                  "red — it has been absorbed by the filter, which is why "
                  "stage lighting gels get warm.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "colour-is-what-a-surface-does",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "The colour of an object is what it does to the light "
                 "landing on it: the frequencies it reflects reach your eye "
                 "and the rest are absorbed, their energy warming it "
                 "slightly. What you see is only what is both present in the "
                 "light and reflected by the surface. A red object under a "
                 "green lamp looks almost black because there is no red "
                 "arriving to reflect, and a white object takes the colour of "
                 "whatever is lighting it."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 2.
    "ladder": {
        "recall": {
            "q": "A blue book is put under a lamp giving out only red light, "
                 "in a room with no other light. What does it look like?",
            "options": [
                "Purple, because red light mixed with a blue book gives "
                "purple.",
                "Blue, because the book is blue whatever light is on it.",
                "Red, because objects take on the colour of the light that "
                "shines on them.",
                "Almost black, because the only light arriving is red and "
                "the book absorbs red.",
            ],
            "answer": 3,
            "feedback": {
                0: "Nothing is being mixed. The book can only send back "
                   "light that arrives, and the only light arriving is red, "
                   "which this cover absorbs.",
                1: "Blue is what the cover does in white light, where blue "
                   "is available to reflect. Under a red lamp there is no "
                   "blue arriving for it to send back.",
                2: "That is true of a white object, which reflects "
                   "everything. A blue book absorbs red rather than "
                   "reflecting it, so almost nothing leaves the surface.",
            },
            "title": "Rung 1 · Apply the rule"},
        "apply": {
            "q": "A white shirt looks green under a green lamp. Which "
                 "statement is right?",
            "options": [
                "The green light has dyed the shirt green for as long as the "
                "lamp is on.",
                "White light contains green, so the shirt was already partly "
                "green.",
                "A white surface reflects all frequencies about equally, so "
                "it sends back whatever arrives — and only green is "
                "arriving.",
                "The shirt looks green because green is the only colour the "
                "human eye can see in dim light.",
            ],
            "answer": 2,
            "feedback": {
                0: "Nothing has changed about the shirt. Switch the lamp to "
                   "white and it looks white again immediately, because what "
                   "changed was the light and not the fabric.",
                1: "That confuses the light with the surface. The shirt "
                   "reflects all frequencies; which ones it can reflect "
                   "depends entirely on which ones are sent to it.",
                3: "The verdict is right and the reason is invented. The "
                   "shirt would look red under a red lamp and blue under a "
                   "blue one, at the same brightness.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why a red jumper looks red in white light and "
                 "almost black under a green lamp, using the words reflect "
                 "and absorb.",
            "field_label": "Your explanation",
            "placeholder": "In white light, every frequency lands on the "
                           "jumper, and…",
            "success": [
                "Says white light contains all the visible frequencies.",
                "Says the jumper reflects the red frequencies and absorbs "
                "the others.",
                "Says the reflected red light is what reaches the eye, so it "
                "looks red.",
                "Says a green lamp sends only green light, and there is no "
                "red arriving to reflect.",
                "Says the jumper absorbs the green that does arrive, so "
                "almost nothing leaves it and it looks black.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A supermarket lights its meat counter with lamps that put "
                 "out extra red, and clothes shops are careful to light "
                 "changing rooms with something close to daylight. Explain "
                 "the physics behind both choices, and say why a shopper "
                 "might reasonably object to the first one.",
            "field_label": "Your answer",
            "placeholder": "What you see depends on what is in the light as "
                           "well as on the surface…",
            "success": [
                "Says what you see depends on which frequencies are in the "
                "light as well as on what the surface reflects.",
                "Says extra red in the lamp means more red is available for "
                "the meat to reflect, so it looks redder and fresher.",
                "Says daylight contains all frequencies fairly evenly, so a "
                "garment reflects the same mixture it would outdoors.",
                "Says that is why a colour chosen under shop lighting can "
                "look different in the street.",
                "Gives a reasoned objection: the lighting changes how the "
                "meat appears without changing the meat, so the shopper is "
                "being shown something the daylight would not show.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "An object that is not a source of light reflects some of the "
                "frequencies landing on it and absorbs the rest, and the "
                "energy it absorbs warms it slightly. What you see is only "
                "the reflected part, so the colour of an object depends on "
                "the light as well as on the surface: it is whatever is both "
                "present in the light and not absorbed. A red object under a "
                "green lamp looks almost black, a white object takes the "
                "colour of the lamp, and a black object absorbs nearly "
                "everything and stays black.",

    "stretch": [
        {"id": "colour-as-absorption-in-biology",
         "type": "explainer",
         "text": "Once colour is understood as absorption, a lot of biology "
                 "reads differently. A leaf is green because chlorophyll "
                 "absorbs red and blue strongly and reflects green — in other "
                 "words, green is the part of sunlight the plant is worst at "
                 "using, and it is thrown away. Flowers advertise with "
                 "frequencies their pollinators can see, and many of them "
                 "carry ultraviolet patterns that guide bees to the nectar "
                 "and are completely invisible to us. And a polar bear is not "
                 "white: its hairs are hollow and colourless, and scatter "
                 "every frequency that lands on them."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "absorb",
         "definition": "To take light in at a surface rather than send it "
                       "back. The energy stays in the material and warms it "
                       "slightly."},
        {"term": "filter",
         "definition": "Something that lets its own colour through and "
                       "absorbs the rest. A filter subtracts; it never adds."},
        {"term": "almost black",
         "definition": "What a surface looks when almost nothing it can "
                       "reflect is arriving. Real dyes and real lamps are "
                       "broad bands, so the perfect case does not occur."},
    ],

    "tutor": {
        "anchor": "s-lamp",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got an object and a coloured lamp, and want to work out what "
                "it will look like?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Absorption, transmission and reflection at a surface for "
                   "different frequencies, colour filters, and why objects "
                   "appear black under some illuminations.",

    "convention_note": "The bench is a teaching model and deliberately "
                       "simplified. Real light and real dyes involve the "
                       "whole continuous spectrum rather than three separate "
                       "colours: a red jumper reflects a band of frequencies "
                       "around red and some of its neighbours rather than red "
                       "alone, and a red lamp puts out a band rather than a "
                       "single frequency, so a real red object under a real "
                       "green lamp looks very dark rather than perfectly "
                       "black. Almost black is therefore the honest answer "
                       "and is used throughout. The colours on screen can "
                       "only approximate the light being described. The room "
                       "is treated as having no other light in it, which is "
                       "what makes the effect this strong; in a room with any "
                       "white light left, every object shows some of its "
                       "usual colour.",

    "ws": ["measurement"],
}
