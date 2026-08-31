"""P6 L4 — Sound is longitudinal (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-04-sound-is-longitudinal.dc.html`.

Her page wins outright. The slinky, the two drives, the marked coil, the
contrast table and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

A contrast. Nothing here is calculated.

── ⚖️ RULED · THE SAME 60 mm AND THE SAME 300 mm IN BOTH DRIVES ──────

That is the whole design of the bench: nothing about the SIZE of the
disturbance changes between the two, only its DIRECTION relative to
travel. A bench whose two drives differed in amplitude would let a student
explain the contrast with the wrong variable and never notice.

── ⚖️ RULED · THE LONGITUDINAL DRIVE DRAWS COIL TICKS, NEVER A SINE ──

`WAVE-13` is *sound is transverse, because it is drawn as a wavy line*,
and a bench that drew the longitudinal case as a curve would be committing
the misconception the lesson exists to kill. Design draws a row of ticks
at varying spacing — bunched in a compression, spread in a rarefaction.

⚖️ The wavy line is not banned from the page, though, and rung 2 defends
it: a graph of how squeezed the air is against distance is a legitimate
drawing and physicists use it constantly. What is wrong is reading it as a
photograph. That distinction is the harder half of the lesson.

── ⚖️ RULED · THE `mid` STATES ARE NOT FILLER ────────────────────────

A coil passing through its rest position is still in a transverse wave,
because what makes it transverse is the direction it TRAVELS, not where it
happens to be at one instant. Both `mid` branches say so, and
`r_slinky_dual` requires all six.

── ⚠️ FOUR RAIL STOPS, AND `s-compare` TICKS ON THE GATE ─────────────

    s-hook · s-slinky · s-compare · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-13  sound is transverse, because it is drawn as a wavy line
    WAVE-14  in a compression the air travels to your ear
    WAVE-15  a longitudinal wave has no amplitude
    WAVE-16  a compression is a place where the air is hotter

`WAVE-15` is not in Design's table — it arrived with rung 1's fourth
option, *"the wave is longer than it is tall"*, which treats amplitude as
a property only a drawn hump can have. `WAVE-16` arrived with her own
`long-comp` note and is confronted by the bench: a compression is
crowding, not heating.
"""

LESSON = {
    "slug":  "sound-is-longitudinal",
    "title": "Sound is longitudinal",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "CONTRAST",

    "covers": ["KS3.P.SND.03c"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["how-sound-is-made"],
    "assumes": [],
    "references": ["waves-on-water", "sound-needs-a-medium"],
    "ks4_links": [],

    "meta_description": "Every drawing of sound you have seen was a wavy "
                        "line. Almost none of them meant the air goes up and "
                        "down. Drive one slinky two ways and watch a single "
                        "coil.",

    "big_question": "Every drawing of sound you have ever seen was a wavy "
                    "line. Almost none of them meant that the air goes up "
                    "and down, and this lesson is about the difference.",

    "rail": [
        {"anchor": "s-hook",    "short": "SLINKY",
         "label": "One slinky, two waves", "done_when": "committed"},
        {"anchor": "s-slinky",  "short": "BENCH",
         "label": "Drive it two ways",     "done_when": "gate_and_a_control"},
        {"anchor": "s-compare", "short": "COMPARE",
         "label": "Same job, two directions", "done_when": "gate_committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "One slinky. Two completely different waves.",
        "prompt": "A long slinky stretched across the floor with someone "
                  "holding each end. Flick your end sideways and a hump runs "
                  "down it. Instead, shove your end sharply towards your "
                  "partner and pull it straight back, and something runs "
                  "down it again — but this time there is no hump at all. "
                  "What travels is a squashed-up patch of coils.",
        "commit": "In that second wave, which way does each individual coil "
                  "move as the disturbance goes past it?",
        "options": [
            "Along the slinky, in the same line as the disturbance is going",
            "Round in a small circle, each coil looping back to where it "
            "started",
            "The coils do not move at all — only the squashed patch travels",
            "Across the slinky, at right angles to the way the disturbance "
            "is going",
        ],
        "answer": 0,
        "reveal": "Each coil shuffles a little way <em>along</em> the slinky "
                  "and back, in the same line the wave is travelling, and "
                  "finishes where it started. Nothing goes to the far end "
                  "except the pattern of crowding and spreading. A wave "
                  "whose material moves along the line of travel is "
                  "<strong>longitudinal</strong>, and <strong>sound is "
                  "one</strong>.",
    },

    "misconceptions": [
        {"id": "WAVE-13",
         "statement": "Sound is transverse, because it is drawn as a wavy "
                      "line.",
         "elicited_by": "s-hook",
         "confronted_by": "slinky"},
        {"id": "WAVE-14",
         "statement": "In a compression the air travels to your ear.",
         "elicited_by": "slinky",
         "confronted_by": "s-think"},
        {"id": "WAVE-15",
         "statement": "A longitudinal wave has no amplitude, because there "
                      "is no hump to measure.",
         "elicited_by": "s-ladder",
         "confronted_by": "slinky"},
        {"id": "WAVE-16",
         "statement": "A compression is a place where the air is hotter.",
         "confronted_by": "slinky"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Both of those are waves: both carry energy from one end to "
                 "the other, and neither one moves any coil permanently "
                 "along the slinky. What separates them is the <em>direction"
                 "</em> the material moves compared with the direction the "
                 "wave travels."},
        {"type": "explainer",
         "text": "In a <strong>transverse</strong> wave the material moves "
                 "across the line of travel, at right angles to it. A shaken "
                 "rope and a wave on water both do this, and both show "
                 "crests and troughs. In a <strong>longitudinal</strong> "
                 "wave the material moves along the same line the wave is "
                 "travelling, backwards and forwards. There are no crests: "
                 "instead there are places where the material is bunched "
                 "together, called <strong>compressions</strong>, and places "
                 "where it is pulled apart, called "
                 "<strong>rarefactions</strong>."},
        {"type": "explainer",
         "text": "<strong>Sound is longitudinal.</strong> A vibrating "
                 "surface pushes the air in front of it into a compression, "
                 "then pulls back and leaves a rarefaction, and that pattern "
                 "travels away. Each patch of air shuffles a tiny distance "
                 "to and fro along the line the sound is going, and finishes "
                 "where it began."},

        # ── #s-slinky · one slinky, driven two ways ────────────────────
        {"type": "slinky-dual",
         "id": "slinky",
         "anchor": "s-slinky",
         "eyebrow": "At the bench · one slinky, 1.20 m long, driven at the "
                    "left-hand end",
         "heading": "Drive it two ways. Watch one coil.",
         "progress": "Change a control to begin",
         "lead": "The same slinky, driven at the same size of movement — "
                 "60 mm — and with the same 300 mm from one repeat to the "
                 "next. Choose how it is driven, then choose which coil to "
                 "mark.",
         "amp_mm": 60,
         "lam_mm": 300,
         "length_mm": 1200,
         "start_drive": "trans",
         "drive_label": "How the end is driven",
         "travel_label": "the wave travels this way",
         "band_anchor": "s-compare",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. A loudspeaker cone moves forwards and "
                       "backwards along the direction the sound is going. "
                       "Which way does the air next to it move?",
             "options": [
                 "Across the sound’s path, up and down",
                 "It does not move; the sound passes through it",
                 "Along the sound’s path, backwards and forwards",
                 "It travels all the way from the cone to the listener",
             ],
             "answer": 2,
         },
         "drives": [
             {"id": "trans", "kind": "transverse", "label": "Sideways",
              "caption": "TRANSVERSE — THE COIL MOVES ACROSS"},
             {"id": "long", "kind": "longitudinal", "label": "Along",
              "caption": "LONGITUDINAL — THE COIL MOVES ALONG"},
         ],
         "mark": {"label": "Where the marked coil sits", "min": 0,
                  "max": 100, "step": 5, "start": 25, "value": "25%"},
         "branches": {
             "trans-crest": "This coil is at a crest: it has been carried "
                            "sideways, and nothing here is bunched up. The "
                            "wave is driven 60 mm across the slinky, but a "
                            "coil can only be marked where one is drawn, and "
                            "no drawn coil sits exactly on the top of a "
                            "crest. That is why the reading stops short of "
                            "60 mm: 57 mm is the closest any drawn coil "
                            "comes.",
             "trans-trough": "This coil is at a trough, carried across the "
                             "slinky the other way. A crest and a trough are "
                             "the same size of movement in opposite "
                             "directions, and both are at right angles to "
                             "the way the wave is going. The wave is driven "
                             "60 mm each way, and the reading stops a little "
                             "short of that because no drawn coil sits "
                             "exactly at the bottom of a trough.",
             "trans-mid": "This coil is passing through its rest place, so "
                          "at this instant it is exactly where it would be "
                          "with the slinky still. It is still a transverse "
                          "wave: what makes it transverse is the direction "
                          "the coil travels, not how far it happens to be at "
                          "one moment.",
             "long-comp": "This coil is inside a compression — the coils "
                          "here are crowded closer than their rest spacing, "
                          "because the coil behind has been pushed forwards "
                          "into the coil in front. There is no crest to see. "
                          "Switch the drive to sideways and the same 60 mm "
                          "of movement makes a hump instead.",
             "long-rare": "This coil is inside a rarefaction — the coils "
                          "here are further apart than their rest spacing, "
                          "because the driven end pulled back and left them "
                          "room. A rarefaction is the longitudinal wave\u2019s "
                          "version of a trough, and it is a gap rather than "
                          "a dip.",
             "long-mid": "This coil is at its rest spacing at this instant, "
                         "halfway between a compression and a rarefaction, "
                         "but it has been displaced along the slinky from "
                         "where it started. Along the slinky, not across it "
                         "— which is what longitudinal means. The wave is "
                         "driven 60 mm; the reading is a little less, "
                         "because no drawn coil sits exactly at the far end "
                         "of that swing.",
         },
         "readouts": [
             {"id": "travel", "label": "Which way the wave travels",
              "value": "Along the slinky, to the right"},
             {"id": "coildir", "label": "Which way the marked coil has moved",
              "sub": "—"},
             {"id": "region", "label": "Where the marked coil sits"},
             {"id": "kind", "label": "Kind of wave"},
         ]},

        # ── #s-compare · same job, two directions ──────────────────────
        {"type": "wave-band",
         "id": "compare",
         "anchor": "s-compare",
         # ⊕ PHASE 3, 25 Aug 2026. This was a two-column table of
         # sentences; Design draws it. Her figure is a pair of cards, each
         # with the wave drawn, one marked particle, an arrow for the way
         # that particle moves and a second arrow for the way the wave
         # goes. **The whole lesson is the angle between those two
         # arrows**, and no table can make an angle. Her closing sentence
         # was missing too, and it is the one that says what the two share.
         "eyebrow": "The figure",
         "heading": "Same job, two directions",
         "pair": {
             "travel_label": "travels",
             "cards": [
                 {"title": "Transverse",
                  "kind": "transverse",
                  "aria_label": "A rope shaken sideways: a wavy line with "
                                "one point marked and an up-and-down arrow "
                                "through it, at right angles to a "
                                "left-to-right arrow showing the direction "
                                "of travel.",
                  "body": "The material moves <em>across</em> the line of "
                          "travel. Crests and troughs. Waves on water, a "
                          "shaken rope, light."},
                 {"title": "Longitudinal",
                  "kind": "longitudinal",
                  "aria_label": "A chain of coils bunched in places and "
                                "spread in others, with one coil marked and "
                                "a back-and-forth arrow through it along "
                                "the same line as the left-to-right arrow "
                                "showing the direction of travel.",
                  "body": "The material moves <em>along</em> the line of "
                          "travel. Compressions and rarefactions. Sound, in "
                          "air, in water and in solids."},
             ],
         },
         "close": "What the two share: both carry energy from one place to "
                  "another, both leave the material where they found it, "
                  "both have an amplitude and a wavelength, and both "
                  "reflect off a barrier. The direction of the material's "
                  "movement is the only thing that separates them."},

        {"type": "key-fact", "ref": "sound-is-longitudinal"},

        {"type": "misconception", "id": "think-sound-is-wavy",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-sound-is-wavy",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-13",
         "statements": [
             {"quote": "Sound must be transverse — it is always drawn as a "
                      "wavy line.",
              "targets": "WAVE-13",
              "body": [
                  "That wavy line is a graph, not a picture. What is "
                  "plotted up the page is how squeezed the air is, or how "
                  "far each patch of air has shuffled from its rest place; "
                  "what runs across the page is distance along the sound, "
                  "or time. Nothing in the air is going up and down. "
                  "Reading a graph of a longitudinal wave as a photograph "
                  "of it is the single commonest mistake in this topic, and "
                  "it is worth checking what the axes of a wave diagram "
                  "actually say before believing your eyes.",
              ]},
             {"quote": "In a compression, air travels from the loudspeaker "
                      "to your ear.",
              "targets": "WAVE-14",
              "body": [
                  "A compression is a place where the air is momentarily "
                  "squeezed, and the place travels; the air does not go "
                  "with it. Each patch of air shuffles a fraction of a "
                  "millimetre forwards, then the same distance back, and "
                  "stays where it was — exactly like the coil you marked on "
                  "the slinky, and exactly like a cork on a pond. If air "
                  "really did travel from the speaker to your ear, a loud "
                  "concert would leave a vacuum on stage and a gale at the "
                  "back of the hall.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "sound-is-longitudinal",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "In a transverse wave the material moves at right angles to "
                 "the direction of travel, giving crests and troughs. In a "
                 "longitudinal wave it moves back and forth along the "
                 "direction of travel, giving compressions where the material "
                 "is bunched and rarefactions where it is pulled apart. Sound "
                 "is longitudinal, in air, in liquids and in solids."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "Which of these describes a longitudinal wave?",
            "options": [
                "The wave is longer than it is tall, so the wavelength is "
                "bigger than the amplitude.",
                "The material moves at right angles to the direction of "
                "travel, giving compressions and rarefactions.",
                "The material travels along with the wave, from one end to "
                "the other.",
                "The material moves backwards and forwards along the same "
                "line the wave is travelling, giving compressions and "
                "rarefactions.",
            ],
            "answer": 3,
            "feedback": {
                0: "That is a description of the shape, and both kinds of "
                   "wave can have any shape. Longitudinal names the "
                   "direction the material moves, not the proportions of "
                   "the drawing.",
                1: "The two halves belong to different waves. Movement at "
                   "right angles is transverse, and transverse waves give "
                   "crests and troughs, not compressions.",
                2: "No wave carries its material along. Each patch shuffles "
                   "to and fro and finishes where it started — that is true "
                   "of both kinds.",
            },
            "title": "Rung 1 · Classify"},
        "apply": {
            "q": "A textbook draws a sound wave as a wavy line. A student "
                 "says this proves the air moves up and down as sound goes "
                 "past. Which statement is right?",
            "options": [
                "The wavy line is a graph of how squeezed the air is "
                "against distance, so its ups and downs are amounts, not "
                "directions — the air moves along the line of travel.",
                "The drawing is simply wrong, and a sound wave should never "
                "be drawn as a wavy line.",
                "The student is right: air really does move up and down as "
                "a sound goes past, which is why a sound wave looks like a "
                "wave on water and is drawn with crests and troughs in "
                "exactly the same way",
                "The air moves up and down near a loudspeaker and along the "
                "line of travel further away.",
            ],
            "answer": 0,
            "feedback": {
                1: "The drawing is a legitimate graph and physicists use it "
                   "constantly. What is wrong is reading it as a "
                   "photograph.",
                2: "It is drawn the same way because a graph of anything "
                   "that repeats looks like that. In air, the movement is "
                   "along the direction of travel, never across it.",
                3: "Nothing changes with distance. The air moves along the "
                   "line of travel from the cone onwards, at every point of "
                   "the journey.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A loudspeaker cone moves forwards and backwards. Explain "
                 "how that makes a longitudinal wave in the air, using the "
                 "words compression and rarefaction.",
            "field_label": "Your explanation",
            "placeholder": "When the cone moves forwards…",
            "success": [
                "Says the cone moving forwards pushes the air in front of "
                "it closer together, making a compression.",
                "Says the cone moving back leaves the air behind more "
                "spread out, making a rarefaction.",
                "Says the pattern of compressions and rarefactions travels "
                "away from the cone.",
                "Says each patch of air moves backwards and forwards along "
                "the direction the sound is travelling.",
                "Says each patch of air ends up where it started, so no air "
                "travels from the speaker to the listener.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A long queue of people is standing still. The person at "
                 "the back steps forward and bumps the next, who bumps the "
                 "next, and a bunching-up travels all the way to the front. "
                 "Say which kind of wave this is like and why, then give "
                 "one way the queue is not a good model of sound.",
            "field_label": "Your answer",
            "placeholder": "The bunching travels up the queue, so…",
            "success": [
                "Says the bunching-up travels up the queue while no one "
                "changes their place in it.",
                "Says each person moves forwards and back along the "
                "direction the bunching travels.",
                "Names it as longitudinal, and matches the bunched-up group "
                "to a compression.",
                "Names the gap left behind as the rarefaction.",
                "Gives one real limitation — for example: the queue is one "
                "line rather than air spreading in every direction, people "
                "move a long way compared with air, or a person choosing to "
                "step forward is not the same as being pushed.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A transverse wave moves its material at right angles to the "
                "direction of travel and shows crests and troughs; a "
                "longitudinal wave moves its material backwards and forwards "
                "along the direction of travel and shows compressions, where "
                "the material is bunched, and rarefactions, where it is "
                "pulled apart. Sound is longitudinal. Each patch of air "
                "shuffles to and fro along the line the sound is going and "
                "finishes where it started, so no air travels from the source "
                "to the listener.",

    "stretch": [
        # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's *Going further*,
        # verbatim, both paragraphs. What had been here was different
        # content of this lane's own: good physics, and not hers, and
        # "a different example" is not a defect anyone can name.
        {"id": "the-distinction-earns-its",
         "type": "explainer",
         "text": "The distinction earns its keep in seismology. An "
                 "earthquake sends out two kinds of wave through the rock "
                 "at once: P waves, which are longitudinal, and S waves, "
                 "which are transverse. P waves are faster, so they always "
                 "arrive first — that is what the P is for. The useful part "
                 "is that a transverse wave needs the material to resist "
                 "being sheared sideways, and a liquid does not, so S waves "
                 "cannot cross a liquid at all. Seismometers all over the "
                 "world record P waves arriving from an earthquake on the "
                 "far side of the planet and no S waves at all, and the "
                 "size of that S wave shadow is the main evidence that the "
                 "Earth's outer core is liquid. Nobody has been anywhere "
                 "near it."},
        {"id": "water-waves-are-the",
         "type": "explainer",
         "text": "Water waves are the awkward case. On the surface of deep "
                 "water each patch travels round a small near-circle rather "
                 "than straight up and down, which makes it partly "
                 "transverse and partly longitudinal at once. The "
                 "transverse description is close enough for the "
                 "crest-and-trough picture and it is the one used at this "
                 "stage, but the honest version is that a surface wave is "
                 "not purely either."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "longitudinal",
         "definition": "The material moves backwards and forwards ALONG the "
                       "direction the wave is travelling. Sound is this "
                       "kind."},
        {"term": "compression",
         "definition": "A place where the material is bunched closer than "
                       "its rest spacing."},
        {"term": "rarefaction",
         "definition": "A place where the material is pulled further apart "
                       "than its rest spacing. A gap, not a dip."},
    ],

    "tutor": {
        "anchor": "s-slinky",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a wave you cannot decide the kind of?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Longitudinal and transverse waves compared in detail, "
                   "wave speed in different materials, and the P wave and S "
                   "wave evidence for the structure of the Earth.",

    "convention_note": "The bench is a teaching model and both drives are "
                       "shown at the same 60 mm of movement and the same 300 "
                       "mm from one repeat to the next, so the two pictures "
                       "can be compared directly; a real slinky driven those "
                       "two ways would not match so neatly. Everything is "
                       "drawn to one scale of about 0.73 pixels per "
                       "millimetre in both directions. The pictures are "
                       "frozen snapshots rather than animations, so the "
                       "marked coil shows where it has been displaced to at "
                       "one instant and not how fast it is going. The coil "
                       "you mark is always one of the coils drawn, so it "
                       "samples the wave rather than sitting on the exact "
                       "top of a crest: the largest reading any drawn coil "
                       "gives is 57 mm, not the full 60 mm. Air is "
                       "drawn as evenly spaced columns for clarity; real air "
                       "is not in rows, and the distance a patch of air "
                       "actually shuffles in ordinary sound is a small "
                       "fraction of a millimetre.",

    "ws": [],
}
