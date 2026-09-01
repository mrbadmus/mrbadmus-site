"""P7 L6 — Colour and the spectrum (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-06-colour-and-the-spectrum.dc.html`.

Her page wins outright. The prism hook, the ray-box bench with its
optional second prism, the spectrum band and all four rungs are hers.

── ⚖️ MRB-204 · NO BLOCK, AND THE STATUTE SAYS SO IN TERMS ──────────

`LGT.06` reads *white light and prisms (qualitative only)*. There is no
relationship to draw, and none was invented.

── ⚖️ RULED · THE SECOND PRISM IS THE EXPERIMENT THAT SETTLES IT ─────

`LIGHT-21` is *the prism adds the colour*, and it does not die by being
contradicted. It dies when a second prism the other way up puts the
colours back into white: if glass made colour, a second piece would make
more of it, and it makes less. Newton did exactly this experiment for
exactly this reason, and the control is on the bench rather than in a
sentence.

⚠️ **THE SINGLE-COLOUR INPUTS ARE NOT FILLER.** Red only and green only
are the states that prove nothing is added: one colour in, the same
colour out, shifted sideways and no fan at all. Blue-and-red is the third
kind of state — two separated bands with no yellows or greens between
them, because there were none in the beam.

── ⚠️ HER FLAG 10 · HUE IS PART OF THE MESSAGE HERE ─────────────────

Colour is the subject, so it cannot be avoided. Every state also carries
the colour AS A WORD in the readout tiles and in the note, and both
marked rungs are answerable from the words alone. The legal line declares
the screen colours as approximations of spectral colours.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-prism · s-band · s-ladder

⚠️ **`s-band` TICKS AT THE GATE.** Marked by the bench through
`band_anchor` / `band_at`.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-21  the prism adds the colour to the light
    LIGHT-22  a rainbow has seven colours with lines between them
    LIGHT-23  high-frequency light is bent the least by a prism
    LIGHT-24  the colours come off the coloured edges of the prism

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 0 and 1.
"""

LESSON = {
    "slug":  "colour-and-the-spectrum",
    "title": "Colour and the spectrum",
    "discipline": "physics",
    "unit": "Light",
    "family": "MODEL",

    "covers": ["KS3.P.LGT.06a"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["the-eye-and-the-camera"],
    "assumes": [],
    "references": ["refraction", "hearing-and-auditory-range",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "A piece of plain, colourless glass throws a band of "
                        "every colour there is onto a wall. It is not making "
                        "any of them.",

    "big_question": "A piece of plain, colourless glass throws a band of "
                    "every colour there is onto a wall. It is not making any "
                    "of them.",

    "rail": [
        {"anchor": "s-hook",   "short": "PRISM",
         "label": "A band on the wall", "done_when": "committed"},
        {"anchor": "s-prism",  "short": "BENCH",
         "label": "Ray box and prism",  "done_when": "gate_and_a_control"},
        {"anchor": "s-band",   "short": "BAND",
         "label": "The band",           "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "White light is not a colour. It is all of them at once.",
        "prompt": "A triangular block of glass in a beam of white sunlight "
                  "throws a band of colour across the wall behind it — red at "
                  "one end, violet at the other, and every shade in between "
                  "with no gaps.",
        "commit": "Where did the colours come from?",
        "options": [
            "The glass added them — that is what a prism does",
            "They were all in the white light already, and the prism "
            "separated them",
            "The white light was turned into coloured light by passing "
            "through glass",
            "The colours came off the coloured edges of the prism",
        ],
        "answer": 1,
        "reveal": "They were there the whole time. White light is every "
                  "visible frequency arriving together, and a prism bends the "
                  "higher frequencies slightly further than the lower ones, "
                  "so they arrive at the wall in different places. The proof "
                  "is a second prism the other way up: it puts them back "
                  "together into white.",
    },

    "misconceptions": [
        {"id": "LIGHT-21",
         "statement": "The prism adds the colour to the light.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "LIGHT-22",
         "statement": "A rainbow has seven colours with lines between them.",
         "confronted_by": "s-think"},
        {"id": "LIGHT-23",
         "statement": "High-frequency light is bent the least by a prism.",
         "elicited_by": "s-ladder",
         "confronted_by": "spectrum-band"},
        {"id": "LIGHT-24",
         "statement": "The colours come off the coloured edges of the prism.",
         "elicited_by": "s-hook",
         "confronted_by": "prism"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "What we call white light is a mixture of light of every "
                 "visible frequency arriving together. Each frequency is seen "
                 "as a different colour: the lowest frequencies of visible "
                 "light look red, the highest look violet, and the familiar "
                 "band of red, orange, yellow, green, blue and violet runs "
                 "between them. The band is called a "
                 "<strong>spectrum</strong>, and it is continuous — the six "
                 "names are places along it rather than six separate things."},
        {"type": "explainer",
         "text": "A prism separates them because refraction depends slightly "
                 "on frequency. All the colours slow down on entering the "
                 "glass, but the higher frequencies slow a little more than "
                 "the lower ones, so violet is bent a little further than "
                 "red. One bend on the way in, another on the way out, and by "
                 "the time the light reaches the wall the colours have fanned "
                 "apart. That fanning is called "
                 "<strong>dispersion</strong>."},
        {"type": "explainer",
         "text": "Nothing has been added to the light and nothing has been "
                 "made. Put a second prism the other way up in the fanned-out "
                 "beam and the colours come back together into white. The "
                 "prism sorts; it does not manufacture."},

        # ── #s-prism · a ray box, a prism and a white screen ──────────
        {"type": "prism-bench",
         "id": "prism",
         "anchor": "s-prism",
         "eyebrow": "At the bench · a ray box, a prism and a white screen",
         "heading": "Send white light in. Sort what comes out.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A narrow beam of white light through a triangular glass "
                   "prism onto a screen. Set what goes in, and set whether a "
                   "second prism is placed in the beam on the far side.",
         "gate": {
             "prompt": "Commit first. A prism spreads white light into a band "
                       "of colour on a screen. Where were the colours before "
                       "the light reached the prism?",
             "options": [
                 "They were not there yet — the glass makes them",
                 "They were all in the white light already, mixed together",
                 "They were in the screen, and the prism brings them out",
                 "They form in the air between the prism and the screen",
             ],
             "answer": 1,
         },
         "in_label": "What goes into the prism",
         "second_label": "A second prism, the other way up",
         "screen_label": "SCREEN",
         # Design's own four inputs. `keys` is which of the six rays leave
         # the prism, in her order; `colour` is the drawn beam colour going
         # in and, where the second prism recombines it, coming out.
         "inputs": [
             {"id": "white", "label": "White light",
              "keys": ["R", "O", "Y", "G", "B", "V"], "word": "White light",
              "sub": "every visible frequency at once",
              "least": "Red", "most": "Violet", "colour": "#F2ECDD",
              "two_screen": "One white patch — the colours put back "
                            "together",
              "two_beam": "white light again"},
             {"id": "red", "label": "Red only", "keys": ["R"],
              "word": "Red only", "sub": "one narrow band of frequencies",
              "least": "Red", "most": "Red", "colour": "#D9563A"},
             {"id": "green", "label": "Green only", "keys": ["G"],
              "word": "Green only", "sub": "one narrow band of frequencies",
              "least": "Green", "most": "Green", "colour": "#5BA45C"},
             {"id": "bluered", "label": "Blue and red", "keys": ["R", "B"],
              "word": "Blue and red together",
              "sub": "two separated bands, no yellows or greens",
              "least": "Red", "most": "Blue", "colour": "#9A647A",
              "two_screen": "One patch of pinky-purple — the two colours "
                            "put back together, and still no yellow or "
                            "green",
              "two_beam": "one pinky-purple beam, with no yellow and no "
                          "green anywhere in it"},
         ],
         "second": [{"id": "no", "label": "No second prism", "on": False},
                    {"id": "yes", "label": "Second prism in", "on": True}],
         "readouts": [
             {"id": "in", "label": "Going into the prism", "sub": "—"},
             {"id": "least", "label": "Bent the least",
              "sub": "the lowest frequency present"},
             {"id": "most", "label": "Bent the most",
              "sub": "the highest frequency present"},
             {"id": "screen", "label": "On the screen"},
         ],
         "captions": {
             "one": "ONE PRISM — WHAT COMES OUT LANDS ON THE SCREEN",
             "two": "TWO PRISMS — THE SECOND ONE INVERTED"},
         # Three branches, keyed to what is actually happening: a
         # single-colour input has nothing to separate, a recombined beam is
         # the experiment that settles it, and a dispersed one names both
         # ends of the fan.
         "branches": {
             "single": "{word} is a single narrow band of frequencies, so "
                       "there is nothing for the prism to separate: the beam "
                       "is refracted, shifted sideways and arrives on the "
                       "screen the same colour it started. Nothing was added, "
                       "and with only one colour going in there is nothing "
                       "for a second prism to put back together either. Send "
                       "white light in instead and six rays leave the same "
                       "piece of glass.",
             "recombined": "The second prism, the other way up, bends each "
                           "colour back by the same amount the first one bent "
                           "it, and they arrive at the screen together as "
                           "{arrives}. That is the experiment that settles "
                           "it: if glass made colour, a second piece would "
                           "make more of it. It makes less.",
             "dispersed": "{word} goes in and {n} separated colours come out, "
                          "with {least} bent least and {most} bent most. "
                          "Nothing appears that was not sent in — with blue "
                          "and red going in there are no yellows or greens on "
                          "the screen, because there were none in the beam. "
                          "Put the second prism in and the same colours run "
                          "back together.",
         },
         "band_anchor": "s-band",
         "band_at": 1},

        # ── #s-band · the band, and which end is which ────────────────
        {"type": "light-band",
         "id": "spectrum-band",
         "anchor": "s-band",
         "eyebrow": "The figure",
         "heading": "The band, and which end is which",
         "spectrum": {
             "aria_label": "A continuous band of colour running from red at "
                           "the left to violet at the right, with the six "
                           "names marked along it. Below it, an arrow "
                           "labelled frequency increasing to the right and an "
                           "arrow labelled bent further by a prism, also to "
                           "the right.",
             "segments": [
                 {"name": "RED", "hex": "#D9563A"},
                 {"name": "ORANGE", "hex": "#DE8A3C"},
                 {"name": "YELLOW", "hex": "#D8C24A"},
                 {"name": "GREEN", "hex": "#5BA45C"},
                 {"name": "BLUE", "hex": "#4F7DC4"},
                 {"name": "VIOLET", "hex": "#8567B5"},
             ],
             "arrows": ["Frequency increases this way",
                        "A prism bends it further this way"]},
         "close": "The two arrows point the same way, and that is the whole "
                  "of dispersion: the higher the frequency, the more the "
                  "prism bends it. The six names are handy labels on a band "
                  "that has no joins in it — between yellow and green there "
                  "is no line, only a gradual change, and how many names a "
                  "language uses for it is a matter of custom."},

        {"type": "key-fact", "ref": "white-light-is-a-mixture"},

        {"type": "misconception", "id": "think-the-prism-adds-colour",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-prism-adds-colour",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-21",
         "statements": [
             {"quote": "The prism adds the colour to the light.",
              "targets": "LIGHT-21",
              "body": [
                  "It sorts what was already there. Nothing about the prism "
                  "is coloured, and the same block of glass turns a red beam "
                  "into a red patch — no extra colours appear from anywhere. "
                  "The strongest evidence is the second prism: put it the "
                  "other way up in the fanned-out beam and the colours run "
                  "back together into a white patch. If the glass were making "
                  "colour, a second piece of it would make more, not less. "
                  "Newton did exactly this experiment for exactly this "
                  "reason.",
              ]},
             {"quote": "A rainbow has seven colours with lines between them.",
              "targets": "LIGHT-22",
              "body": [
                  "It has as many as you can distinguish, and there are no "
                  "lines anywhere. The spectrum is continuous: frequency "
                  "changes smoothly from one end to the other and so does the "
                  "colour, with no boundary between yellow and green any more "
                  "than there is a boundary between warm and hot. Seven is a "
                  "historical count — Newton wanted the number to match the "
                  "notes of a musical scale, which is why indigo is on the "
                  "list at all — and different languages divide the same band "
                  "up differently. What is real is the frequency; the names "
                  "are ours.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "white-light-is-a-mixture",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "White light is a mixture of every visible frequency "
                 "arriving together, and each frequency is seen as a "
                 "different colour. A prism separates them because higher "
                 "frequencies are refracted a little more than lower ones, so "
                 "violet bends further than red and the beam fans out into a "
                 "continuous spectrum. That fanning is dispersion. A second "
                 "prism the other way up recombines the colours into white, "
                 "which shows the prism sorts light rather than making "
                 "colour."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "White light passes through a prism and fans out onto a "
                 "screen. Which colour lands closest to where the undeviated "
                 "beam would have gone, and why?",
            "options": [
                "Red, because it has the lowest frequency of the visible "
                "colours and is refracted the least.",
                "Violet, because it has the highest frequency and "
                "high-frequency light is bent least.",
                "Green, because it is in the middle of the spectrum and so "
                "is deflected least.",
                "They all land in the same place, because refraction is the "
                "same for every colour.",
            ],
            "answer": 0,
            "feedback": {
                1: "Violet is bent the most, not the least. Higher frequency "
                   "means a slightly greater slowing in the glass, and a "
                   "slightly bigger bend.",
                2: "Green sits in the middle of the fan, not at the "
                   "undeviated position. The least-bent colour is the one at "
                   "the low-frequency end, which is red.",
                3: "If it were the same for every colour there would be no "
                   "fan at all and no spectrum. The whole effect exists "
                   "because the bend depends slightly on frequency.",
            },
            "title": "Rung 1 · Apply the rule"},
        "apply": {
            "q": "A student says the prism must be adding the colours, "
                 "because white light goes in and coloured light comes out. "
                 "Which statement is right?",
            "options": [
                "The student is right — the glass is what makes the colours, "
                "which is why plain glass is used and not coloured glass.",
                "A second prism the other way up in the fanned beam "
                "recombines the colours into white, which shows they were in "
                "the white light all along.",
                "The prism does not add colour, but it does turn some of the "
                "white light into red and violet as it passes through.",
                "The colours come from the surface of the glass, which is "
                "why only the edges of the beam are coloured.",
            ],
            "answer": 1,
            "feedback": {
                0: "Then a second piece of glass would make yet more colour, "
                   "and it does the opposite: it puts them back together "
                   "into white.",
                2: "Turning white into red is still making colour, and it "
                   "does not happen. Send red light in on its own and red "
                   "comes out; nothing new is ever produced.",
                3: "The whole beam fans out, not just its edges, and the "
                   "effect happens in the body of the glass where the light "
                   "slows. Nothing about the surface is coloured.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain how a prism produces a spectrum from white light, "
                 "using the words frequency, refraction and dispersion.",
            "field_label": "Your explanation",
            "placeholder": "White light is a mixture of…",
            "success": [
                "Says white light is a mixture of light of every visible "
                "frequency.",
                "Says all of it slows down and refracts on entering the "
                "glass.",
                "Says higher frequencies are refracted slightly more than "
                "lower ones.",
                "Says violet is therefore bent furthest and red least, so "
                "the colours fan apart.",
                "Names that fanning as dispersion, and says the prism "
                "separates rather than creates.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A rainbow appears when the Sun is behind you and rain is "
                 "falling in front of you, and red is always on the outside "
                 "of the arc. Explain what each raindrop is doing, and why "
                 "the order of the colours is the same in every rainbow.",
            "field_label": "Your answer",
            "placeholder": "Sunlight enters each raindrop and…",
            "success": [
                "Says sunlight enters each raindrop and is refracted on the "
                "way in.",
                "Says it is reflected off the inside of the back of the drop "
                "and refracted again on the way out.",
                "Says the refraction separates the colours, because higher "
                "frequencies bend more.",
                "Says the light comes back towards the Sun’s side, which is "
                "why the Sun has to be behind you.",
                "Says the order is fixed because it follows frequency, which "
                "is a property of the light and does not vary from drop to "
                "drop.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "White light is a mixture of light of every visible "
                "frequency, and each frequency is seen as a different colour "
                "— the lowest visible frequencies red, the highest violet. A "
                "prism refracts higher frequencies slightly more than lower "
                "ones, so the colours fan apart into a continuous spectrum; "
                "that fanning is dispersion. A second prism the other way up "
                "recombines them into white, which shows the prism separates "
                "light rather than creating colour.",

    "stretch": [
        {"id": "the-visible-band-is-a-narrow-strip",
         "type": "explainer",
         "text": "The visible band is a narrow strip of something much wider. "
                 "Below red in frequency come infrared, microwaves and radio "
                 "waves; above violet come ultraviolet, X-rays and gamma "
                 "rays. All of them are the same kind of wave as light, all "
                 "travel at 300 000 000 m/s in a vacuum, and the only thing "
                 "separating them is frequency. Our eyes respond to about one "
                 "octave of it — roughly a doubling of frequency from red to "
                 "violet — and are blind to everything else, in exactly the "
                 "way our ears stop at 20 000 Hz."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "spectrum",
         "definition": "The continuous band of colours white light contains, "
                       "running from red at the lowest visible frequency to "
                       "violet at the highest."},
        {"term": "dispersion",
         "definition": "The fanning apart of the colours in white light, "
                       "because a prism refracts higher frequencies slightly "
                       "more than lower ones."},
        {"term": "frequency",
         "definition": "How many vibrations of the wave arrive each second. "
                       "For light it is what decides the colour."},
    ],

    "tutor": {
        "anchor": "s-prism",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check which colour a prism bends furthest, and why?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The electromagnetic spectrum in full, the wave equation "
                   "applied to light, and the properties and uses of each "
                   "region.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Never look directly at the Sun — not with your eyes, not "
                   "through a lens, not through a pinhole camera. A lens "
                   "gathers sunlight to a point hot enough to scorch paper, "
                   "and it will do the same to the back of your eye. The "
                   "damage is painless while it happens and it does not heal.",

    "convention_note": "The bench is a teaching model. The prism angles and "
                       "the spread of the fan are drawn for clarity rather "
                       "than calculated: real dispersion through a glass "
                       "prism is a spread of a couple of degrees, far "
                       "narrower than the drawing, and the exact spread "
                       "depends on the glass. The colours are drawn as six "
                       "separate rays because six is what can be told apart "
                       "on a screen; the real spectrum is continuous with no "
                       "gaps and no boundaries. Screen colours can only "
                       "approximate spectral colours, and the band in the "
                       "figure is an illustration rather than a measurement. "
                       # ⊕ MRB-297 · 1 Sep 2026 — THIS SENTENCE DESCRIBED A
                       # BENCH THAT NO LONGER EXISTS, AND IT WAS THIS RUN
                       # THAT CHANGED THE BENCH. It read "The recombining
                       # prism is shown returning the beam exactly to
                       # white, which a real pair of prisms does only
                       # approximately." The "Blue and red" input added on
                       # this branch sends "one pinky-purple beam" through
                       # the second prism, not white, so a student who
                       # chose it read a convention note denying what was
                       # on the screen in front of them. The honest point
                       # about real prisms is kept.
                       "The recombining prism is shown putting the beam "
                       "back together exactly — to white when the whole "
                       "spectrum went in, and to one blended colour when "
                       "only part of it did. A real pair of prisms manages "
                       "that only approximately.",

    "ws": ["measurement"],
}
