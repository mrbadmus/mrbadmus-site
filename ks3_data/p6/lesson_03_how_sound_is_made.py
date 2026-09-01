"""P6 L3 — How sound is made (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-03-how-sound-is-made.dc.html`.

Her page wins outright. The fingers on the throat, the four-stage strip,
the five sources, the two detectors and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

A process. Nothing here is calculated, and no relationship was invented in
order to have something to put in a triangle.

── ⚖️ RULED · THE HOOK IS A NEGATIVE CONTROL, AND IT IS THE LESSON ───

*Hum with your fingers on your throat, then breathe out through an open
mouth.* Air is still pouring past exactly the same place and there is no
note. That is `WAVE-09` — *sound is made by the air, not by the object* —
confronted before it is stated, by an experiment a student can run in
their own throat in four seconds.

── ⚖️ RULED · THE BENCH REPORTS "HOW MANY TIMES A SECOND" (her FLAG 2)

It teaches no pitch and claims no clause of `SND.01`, which `p6-05` owns.
Design's reason: the alternative is a bench that names a quantity it will
not let a student read. She asks a reviewer who reads Hz-anywhere as a
claim on `SND.01` to say so — *"it is a two-line change"* — and nothing
here pre-empts that.

── ⚖️ RULED · THE MOVEMENT IS EXAGGERATED AND THE PAGE SAYS SO ───────

A tuning fork's prongs move about half a millimetre. Drawn to scale the
figure would be a straight line, so every source is drawn far larger than
life and the readout carries *"typical, and greatly exaggerated in the
drawing"* under it.

── ⚠️ FOUR RAIL STOPS, AND `s-stages` TICKS ON THE HOOK ──────────────

    s-hook · s-stages · s-chain · s-ladder

Design's `DONE`: `if (id === 's-stages') return s.hookChoice !== null`.
The strip sits ABOVE the bench on her page, so it cannot wait on the
bench's gate. Measured off her drawing; the hook marks it.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-09  sound is made by the air, not by the object
    WAVE-10  if you cannot see it moving it is not vibrating
    WAVE-11  a microphone is a quiet loudspeaker
    WAVE-12  sound is stored in an object and gets out

`WAVE-12` is not in Design's table — it arrived with rung 1's second
option, *"the hand blocks the sound and stops it getting out of the
glass"*, and it is separate from `WAVE-09`: not "the air makes it" but
"the object holds it".
"""

LESSON = {
    "slug":  "how-sound-is-made",
    "title": "How sound is made",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "PROCESS",

    "covers": ["KS3.P.SND.03a", "KS3.P.SND.03b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["transverse-waves-and-superposition"],
    "assumes": [],
    "references": ["sound-is-longitudinal", "frequency-pitch-and-loudness"],
    "ks4_links": [],

    "meta_description": "A guitar string, a loudspeaker cone and two folds "
                        "of tissue in your throat have one thing in common: "
                        "all three are moving to and fro, fast, and pushing "
                        "on the air while they do it.",

    "big_question": "A guitar string, a loudspeaker cone and two folds of "
                    "tissue in your throat have nothing in common except the "
                    "one thing that matters: all three are moving to and "
                    "fro, fast, and pushing on the air while they do it.",

    "rail": [
        {"anchor": "s-hook",   "short": "THROAT",
         "label": "Fingers on your throat", "done_when": "committed"},
        {"anchor": "s-stages", "short": "STAGES",
         "label": "Four stages, every time", "done_when": "hook_committed",
         # ⊕ MRB-249 · THIS STOP MIRRORS THE HOOK, and that is the
         # engine's own mechanism rather than a new one. Design's
         # `isDone()` returns `s.hookChoice !== null` for this id,
         # which `ks3_parity` reads as a mirror map of
         # `{s-stages: s-hook}` and gates against. A bespoke
         # `after_anchor` was built here first, in ignorance of
         # `mirrors`, and the gate said so.
         "mirrors": "s-hook"},
        {"anchor": "s-chain",  "short": "CHAIN",
         "label": "Source and detector",    "done_when": "gate_and_a_control"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Hum with your fingers on your throat.",
        "prompt": "Two fingers on the front of your throat, and hum. "
                  "Something under the skin is buzzing. Stop humming but "
                  "keep breathing out through an open mouth: air is still "
                  "pouring past exactly the same place, and there is no buzz "
                  "and no note.",
        "commit": "Air moving is not enough on its own. What has to be "
                  "happening for there to be a sound?",
        "options": [
            "The air has to be pushed out fast enough to carry the note",
            "Something has to be vibrating — moving quickly to and fro",
            "Air has to be moving past the place where the sound comes from",
            "Your mouth has to be open, so the sound has a way out",
        ],
        "answer": 1,
        "reveal": "Breathing out moves far more air than humming does, and "
                  "it makes no note at all. What the hum adds is two folds "
                  "of tissue snapping open and shut about 120 times a "
                  "second. <strong>Every sound starts with something "
                  "vibrating</strong>, and the air is what carries the "
                  "result — not what makes it.",
    },

    "misconceptions": [
        {"id": "WAVE-09",
         "statement": "Sound is made by the air, not by the object.",
         "elicited_by": "s-hook",
         "confronted_by": "chain"},
        {"id": "WAVE-10",
         "statement": "If you cannot see it moving it is not vibrating.",
         "elicited_by": "chain",
         "confronted_by": "s-think"},
        {"id": "WAVE-11",
         "statement": "A microphone is a quiet loudspeaker.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "WAVE-12",
         "statement": "Sound is stored inside an object and gets out.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every sound starts with something <strong>vibrating</strong> "
                 "— moving quickly to and fro about one place. The vibrating "
                 "surface pushes on the air touching it, then pulls away "
                 "from it, then pushes again. That gives the air a "
                 "shove-and-release, over and over, and the disturbance "
                 "travels outwards."},
        {"type": "explainer",
         "text": "At the far end the same thing happens in reverse. The "
                 "arriving disturbance pushes and releases whatever it "
                 "meets, so a thin stretched sheet is set vibrating in time "
                 "with the source. In a <strong>microphone</strong> that "
                 "sheet is called a <strong>diaphragm</strong>, and its "
                 "movement is turned into a changing electrical signal. In "
                 "your ear it is the <strong>eardrum</strong>, and its "
                 "movement is turned into signals along a nerve. A "
                 "<strong>loudspeaker</strong> runs the same chain the other "
                 "way: a changing electrical signal drives a cone back and "
                 "forth, and the cone does to the air what your vocal folds "
                 "do."},

        # ── #s-stages · four stages, every time ────────────────────────
        {"type": "wave-band",
         "id": "four-stages",
         "anchor": "s-stages",
         # ⚖️ TICKED BY THE HOOK, WHICH IS DESIGN'S OWN EXPRESSION. Her DONE
         # for this stop reads `s.hookChoice !== null`, because the strip
         # sits ABOVE the bench and there is no instrument before it to
         # give it a sibling tick. That is declared where the engine reads
         # it — `"mirrors": "s-hook"` on this stop's row in `rail` above —
         # and not with an attribute here.
         "eyebrow": "The figure",
         "heading": "Four stages, every time",
         "strip": {
             "aria_label": "Four stages in a row, each with an arrow to the "
                           "next: something vibrating, the air being pushed "
                           "and released, the disturbance travelling, and a "
                           "detector turning the movement into a signal.",
             "columns": [
                 {"title": "1 · SOMETHING VIBRATES",
                  "caption": "the source",
                  "glyph": "M60 135 Q125 75 190 135 M60 135 Q125 195 190 135"},
                 {"title": "2 · THE AIR IS PUSHED",
                  "caption": "and released, over and over",
                  "glyph": "M320 100 V170 M350 100 V170 M375 100 V170 "
                           "M415 100 V170 M460 100 V170"},
                 {"title": "3 · IT TRAVELS",
                  "caption": "outwards, in every direction",
                  "glyph": "M560 135 q34 -46 68 0 q34 46 68 0 q34 -46 68 0"},
                 {"title": "4 · SOMETHING DETECTS IT",
                  "caption": "and it stops being sound",
                  "glyph": "M830 90 V180 M860 105 V165 M890 118 V152"},
             ],
         },
         "close": "Take away stage one and there is nothing to send. Take "
                  "away stage two and there is nothing to carry it. "
                  "<strong>Stage four is the only stage that is not "
                  "sound</strong>: by then it is electricity, or a nerve "
                  "signal, and it is on its way somewhere else."},

        # ── #s-chain · one source, one detector, the air in between ────
        {"type": "vibration-chain",
         "id": "chain",
         "anchor": "s-chain",
         "eyebrow": "At the bench · one source, one detector, the air in "
                    "between",
         "heading": "Change what vibrates. The chain does not change.",
         "progress": "Change a control to begin",
         "lead": "A source at one end of the bench and a detector at the "
                 "other, half a metre apart in ordinary air.",
         "travel_label": "THE DISTURBANCE TRAVELS THIS WAY",
         "start_source": 0,
         "start_det": 0,
         "source_label": "What is vibrating",
         "det_label": "What is listening",
         "gate": {
             "prompt": "Commit first. A tuning fork is struck and rings. "
                       "Someone lays a finger on the prongs and the note "
                       "stops instantly. Why?",
             "options": [
                 "The finger cools the metal, and cool metal cannot carry a "
                 "note",
                 "The finger blocks the sound before it can leave the "
                 "prongs",
                 "The finger takes the energy out of the air around the "
                 "fork",
                 "The finger stops the prongs vibrating, so there is "
                 "nothing left to disturb the air",
             ],
             "answer": 3,
         },
         "sources": [
             {"id": "string", "label": "Guitar string",
              "caption": "PLUCKED STRING", "moves": "The string",
              "driven": "set going by a pluck, then left alone",
              "amp": "about 3 mm at first",
              "freq": "about 82 times a second",
              "path": "M70 170 Q160 96 250 170",
              "ghost": "M70 170 Q160 244 250 170 M70 170 H250",
              "arrow": "M160 74 V52 M160 52 l-9 13 M160 52 l9 13 "
                       "M160 266 V288 M160 288 l-9 -13 M160 288 l9 -13",
              "note": "A plucked string swings widest the instant you let go "
                      "and gets quieter from then on, because every push it "
                      "gives the air takes energy out of the string. Nothing "
                      "is topping it up."},
             {"id": "cone", "label": "Loudspeaker cone",
              "caption": "SPEAKER CONE", "moves": "The cone",
              "driven": "driven back and forth by an electrical signal",
              "amp": "about 1 mm on a loud bass note",
              "freq": "whatever the signal says, often about 200 times a "
                      "second",
              "path": "M96 96 L200 148 V192 L96 244",
              "ghost": "M126 96 L230 148 V192 L126 244",
              "arrow": "M244 170 H286 M286 170 L274 161 M286 170 L274 179 "
                       "M60 170 H18 M18 170 L30 161 M18 170 L30 179",
              "note": "A cone is the one source here that is told what to do "
                      "from outside: the electrical signal sets both how far "
                      "and how often it moves, and it keeps going for as "
                      "long as the signal does. Everything downstream of it "
                      "is the same as for a plucked string."},
             {"id": "fork", "label": "Tuning fork",
              "caption": "TUNING FORK", "moves": "The two prongs",
              "driven": "struck once, then left to ring",
              "amp": "about 0.5 mm",
              "freq": "exactly 440 times a second for a concert A fork",
              "path": "M120 84 V190 Q160 236 200 190 V84",
              "ghost": "M96 84 V190 Q160 260 224 190 V84",
              "arrow": "M92 130 H56 M56 130 L68 121 M56 130 L68 139 "
                       "M228 130 H264 M264 130 L252 121 M264 130 L252 139",
              "note": "A fork is built to vibrate at one rate and almost "
                      "nothing else, which is why it is used for tuning. Its "
                      "prongs move much less far than a plucked string, and "
                      "two thin prongs push very little air, so a fork held "
                      "up on its own is quiet; stand its base on a table and "
                      "the whole table pushes the air for it."},
             {"id": "drum", "label": "Drum skin",
              "caption": "DRUM SKIN", "moves": "The stretched skin",
              "driven": "set going by a hit, then left alone",
              "amp": "about 0.5 mm",
              "freq": "about 80 times a second for a large drum",
              "path": "M74 110 H246 M74 110 Q160 202 246 110",
              "ghost": "M74 110 Q160 18 246 110 M74 110 V250 M246 110 V250",
              "arrow": "M160 232 V266 M160 266 l-9 -13 M160 266 l9 -13 "
                       "M160 60 V26 M160 26 l-9 13 M160 26 l9 13",
              "note": "A big skin moves a lot of air at once, which is why a "
                      "drum is loud without moving far. The skin is heavy "
                      "and slow compared with a fork, so it goes to and fro "
                      "fewer times a second."},
             {"id": "folds", "label": "Vocal folds",
              "caption": "VOCAL FOLDS",
              "moves": "Two folds of tissue in your throat",
              "driven": "blown open and snapped shut by air from your lungs",
              "amp": "about 1 mm",
              "freq": "about 120 times a second for a low voice",
              "path": "M112 90 Q166 170 112 250 M208 90 Q154 170 208 250",
              "ghost": "M88 90 Q142 170 88 250 M232 90 Q186 170 232 250",
              "arrow": "M74 170 H40 M40 170 L52 161 M40 170 L52 179 "
                       "M246 170 H280 M280 170 L268 161 M280 170 L268 179",
              "note": "Your folds are the only source here that needs a "
                      "supply of air to keep going, which is why you run out "
                      "of breath and a fork does not. Breathing out with the "
                      "folds held open moves far more air and makes no note "
                      "at all."},
         ],
         "detectors": [
             {"id": "mic", "label": "Microphone diaphragm",
              "caption": "MICROPHONE",
              "out": "A changing electrical signal",
              "note": "The diaphragm moves in time with the arriving air and "
                      "a coil behind it turns that movement into a changing "
                      "voltage. A loudspeaker is the same parts wired the "
                      "other way round."},
             {"id": "ear", "label": "Your eardrum", "caption": "EARDRUM",
              "out": "Signals along a nerve to your brain",
              "note": "The eardrum moves in time with the arriving air, "
                      "three small bones pass that movement inwards, and "
                      "nerve signals go to your brain. The movement is far "
                      "too small to see."},
         ],
         "readouts": [
             {"id": "moves", "label": "What moves at the source",
              "sub": "—"},
             {"id": "amp", "label": "How far it moves",
              "sub": "typical, and greatly exaggerated in the drawing"},
             {"id": "freq", "label": "How many times a second"},
             {"id": "out", "label": "What comes out at the far end"},
         ]},

        {"type": "key-fact", "ref": "every-sound-starts-with-a-vibration"},

        {"type": "misconception", "id": "think-air-makes-the-sound",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-air-makes-the-sound",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-10",
         "statements": [
             {"quote": "Sound is made by the air.",
              "targets": "WAVE-10",
              "body": [
                  "The air is the delivery, not the maker. Hold a struck "
                  "tuning fork in front of a candle flame and the flame "
                  "flickers in time with the prongs: the fork is doing "
                  "something to the air, not the other way round. That is "
                  "why touching the prongs kills the note at once, while "
                  "the air in the room is untouched and carries on exactly "
                  "as before. Something has to vibrate first. The air is "
                  "what is next in the chain.",
              ]},
             {"quote": "If you cannot see it moving, it cannot be vibrating.",
              "targets": "WAVE-11",
              "body": [
                  "Almost every vibration that makes a sound is far too "
                  "small and far too fast to see. A guitar string is the "
                  "rare exception, and even then you only see a blur. Rest "
                  "a struck tuning fork on a table top and the note jumps "
                  "in volume, because the whole table is now vibrating too "
                  "— and the table looks perfectly still. Sprinkle a few "
                  "grains of rice on a loudspeaker cone playing a bass note "
                  "and they jump about; the rice is doing the seeing for "
                  "you.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "every-sound-starts-with-a-vibration",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Every sound begins with something vibrating. The vibration "
                 "pushes and releases the air, the disturbance travels "
                 "through it, and at the far end it sets a thin sheet "
                 "vibrating in time — a microphone diaphragm or your eardrum "
                 "— which passes the pattern on as an electrical or a nerve "
                 "signal. Stop the vibration and the sound stops at that "
                 "instant."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A wine glass is tapped and rings. Someone grips the rim "
                 "and the note stops instantly. What has happened?",
            "options": [
                "The grip stops the glass vibrating, and with nothing "
                "vibrating there is nothing left to disturb the air.",
                "The hand absorbs the sound as it comes off the rim.",
                "The hand blocks the sound and stops it getting out of the "
                "glass.",
                "The hand takes the energy out of the air around the glass, "
                "so the air can no longer carry the sound.",
            ],
            "answer": 0,
            "feedback": {
                1: "Absorption is a real thing, but it would muffle the "
                   "note rather than end it instantly, and it would not "
                   "need contact with the rim. The vibration itself has "
                   "stopped.",
                2: "Sound is not stored in the glass waiting to get out. It "
                   "only exists while something is vibrating, and the grip "
                   "ends the vibration.",
                3: "The right idea in the wrong place. The energy is taken "
                   "out of the glass, not out of the air — the air in the "
                   "room is untouched and would carry any other sound "
                   "perfectly well.",
            },
            "title": "Rung 1 · Apply the rule"},
        "apply": {
            "q": "A microphone and a loudspeaker contain almost the same "
                 "parts. Which statement is right?",
            "options": [
                "A microphone stores the sound and a loudspeaker plays it "
                "back, so the parts inside must be different: one is built "
                "to hold a sound until it is wanted and the other to let "
                "one out again",
                "A microphone makes the sound and a loudspeaker detects it.",
                "Both turn electricity into sound, and a microphone simply "
                "does it much more quietly.",
                "A loudspeaker turns an electrical signal into a vibrating "
                "cone, and a microphone lets a vibrating diaphragm make an "
                "electrical signal — the same chain, run in opposite "
                "directions.",
            ],
            "answer": 3,
            "feedback": {
                0: "Neither one stores anything. Both convert while the "
                   "sound is happening, which is why the same "
                   "sheet-and-coil works for either job.",
                1: "The two jobs are the right pair and the wrong way "
                   "round. The microphone is the detector at the end of the "
                   "chain; the loudspeaker is the source at the start of "
                   "it.",
                2: "A microphone is not a quiet loudspeaker. Sound goes in "
                   "and electricity comes out, which is the chain running "
                   "backwards, not the same chain turned down.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Describe the whole chain from plucking a guitar string to "
                 "hearing the note, naming what happens at each stage.",
            "field_label": "Your explanation",
            "placeholder": "The plucked string…",
            "success": [
                "Says the plucked string vibrates — moves quickly to and "
                "fro.",
                "Says the string pushes and releases the air next to it.",
                "Says the disturbance travels out through the air.",
                "Says the arriving disturbance makes the eardrum vibrate in "
                "time with the string.",
                "Says the eardrum passes the pattern on as nerve signals to "
                "the brain.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "You phone a friend. Trace the chain from your mouth to "
                 "their ear, and say clearly which parts of it are sound "
                 "and which parts are not.",
            "field_label": "Your answer",
            "placeholder": "My vocal folds vibrate, which…",
            "success": [
                "Starts with the vocal folds vibrating and pushing on the "
                "air.",
                "Says the microphone diaphragm in the phone is set "
                "vibrating by that air.",
                "Says the diaphragm movement becomes an electrical signal, "
                "and that this part of the journey is not sound.",
                "Says a loudspeaker in the other phone turns the signal "
                "back into a vibrating cone, which pushes on the air again.",
                "Ends with the air setting the listener’s eardrum "
                "vibrating, and says sound exists only in the two stretches "
                "where something material is being pushed and released.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Sound is produced by objects vibrating. The vibrating "
                "surface pushes and releases the air touching it, and the "
                "disturbance travels outwards. At the far end it makes a thin "
                "sheet vibrate in time with the source: a microphone "
                "diaphragm, which turns that movement into a changing "
                "electrical signal, or your eardrum, which turns it into "
                "signals along a nerve. A loudspeaker runs the same chain "
                "backwards, its cone driven by an electrical signal.",

    "stretch": [
        # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's *Going further*,
        # verbatim, both paragraphs. What had been here was different
        # content of this lane's own: good physics, and not hers, and
        # "a different example" is not a defect anyone can name.
        {"id": "the-reversibility-of-the",
         "type": "explainer",
         "text": "The reversibility of the chain is not a curiosity, it is "
                 "engineering. A cheap intercom uses one small loudspeaker "
                 "as both speaker and microphone, switching which end of "
                 "the wire is driving which. Older headphones can be "
                 "plugged into a microphone socket and shouted into, and "
                 "they work — badly, but they work — because a coil moving "
                 "near a magnet generates a voltage whether you meant it to "
                 "or not."},
        {"id": "not-everything-that-vibrates",
         "type": "explainer",
         "text": "Not everything that vibrates gets its own sound out into "
                 "the room. A tuning fork held in the air is quiet, because "
                 "two thin prongs push very little air; stand its base on a "
                 "table and the note leaps in volume, since the whole table "
                 "top is now being driven and a table top pushes a great "
                 "deal of air. Nothing has been added to the fork, and it "
                 "dies away faster than before. The same energy is simply "
                 "being handed to the air more quickly."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "vibrating",
         "definition": "Moving quickly to and fro about one place. Every "
                       "sound starts with something doing it."},
        {"term": "diaphragm",
         "definition": "The thin stretched sheet in a microphone, set moving "
                       "by the arriving air."},
        {"term": "eardrum",
         "definition": "The stretched sheet in your ear that does the same "
                       "job as a microphone's diaphragm."},
    ],

    "tutor": {
        "anchor": "s-chain",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a source you cannot work out the chain for?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The range of human hearing, sound as a longitudinal wave "
                   "in a solid, liquid or gas, and how the ear converts "
                   "pressure changes into electrical impulses.",

    "convention_note": "The bench is a teaching model. Every vibration in it "
                       "is drawn many times larger than it really is: a "
                       "tuning fork prong moving half a millimetre would be "
                       "invisible at this size. The distances the sources "
                       "move and the number of times a second they move are "
                       "typical values for one ordinary example of each and "
                       "vary widely with size, tension and how hard the thing "
                       "was struck; only the 440 times a second of a concert "
                       "A tuning fork is a fixed figure, and that is a "
                       "convention rather than a measurement. The loudspeaker "
                       "and microphone drawings leave out the coil and magnet "
                       "that do the converting. The columns of air are drawn "
                       "bunched and spread to show where the air is squeezed; "
                       "real air is not in rows.",

    "ws": [],
}
