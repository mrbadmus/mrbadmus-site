"""P6 L9 — Ultrasound at work (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-09-ultrasound-at-work.dc.html`.

Her page wins outright. The hidden weld, the three blocks, the four-panel
energy/information split, both misconception quotes, all four rungs and
the Childline block are hers.

── ⚖️ NO FORMULA BLOCK — DESIGN'S FLAG 3, AND SHE IS RIGHT ──────────

The gauge computes a depth from an echo time, which is `d = v × t`
followed by halving. `p6-06` owns the triangle for the first half and
`p6-07` owns the bar for the second, one and two lessons back. A third
speed block here would be the fourth `d = v × t` block in two units.
Instead the readouts print the path and the time line by line, and both
owning lessons are carried as edges.

Design flagged this herself and asked for a ruling: *"If a reviewer rules
that a page which computes must carry a block, this one needs one and it
will be a duplicate."* That is Mide's call, not a lane's. Passed through
to the report unresolved; nothing here changes.

── ⊖ HER FLAG 6 · STEEL IS 5000 m/s AND STAYS ───────────────────────

Same figure as `p6-06`, and this page's own foot line states the 5000–5900
published range. The two pages agree; standardising on 5900 would need
both pages and one rung changing together.

── ⚖️ RULED · TWO PIPS, TO SCALE, IN A FIXED WINDOW ─────────────────

0.30 ms, always. A faster material visibly brings the two pips together,
which is the whole of what the material control does — and it is why a
gauge has to be told which material it is standing on before it can read
a depth at all.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-gauge · s-uses · s-ladder

⚖️ **THE USES STOP IS TICKED BY THE BENCH**, at Design's own earlier
threshold — her `s-uses` ticks on the gate alone while `s-gauge` also
wants a control touched.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-33  ultrasound is a special wave that gets through solids
    WAVE-34  a scan shines ultrasound through you and reads the far side
    WAVE-35  ultrasound is used because it travels faster
    WAVE-36  the gel is there to make the probe slide
"""

LESSON = {
    "slug":  "ultrasound-at-work",
    "title": "Ultrasound at work",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "SYSTEM",

    "covers": ["KS3.P.EAW.01"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 4}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["hearing-and-auditory-range"],
    "assumes": [],
    "references": ["sound-needs-a-medium", "echoes-reflection-and-absorption",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "Nothing about ultrasound is exotic. It is ordinary "
                        "sound at a frequency our ears stop short of — and "
                        "every job it does is one of two things: deliver "
                        "energy, or bring back information.",

    "big_question": "Nothing about ultrasound is exotic. It is ordinary "
                    "sound at a frequency our ears happen to stop short of — "
                    "and every job it does is one of the two things any wave "
                    "can do: deliver energy, or bring back information.",

    "rail": [
        {"anchor": "s-hook",   "short": "WELD",
         "label": "The weld you cannot open", "done_when": "committed"},
        {"anchor": "s-gauge",  "short": "GAUGE",
         "label": "Probe on a block",         "done_when": "gate_and_a_control"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Energy or information",    "done_when": "sibling_marked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",           "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The weld looks perfect. That is the problem.",
        "prompt": "A steel weld on a bridge girder has been ground smooth "
                  "and painted. From the outside it is flawless. Somewhere "
                  "inside it there may be a crack a couple of millimetres "
                  "across, and if there is, it matters enormously. Nobody is "
                  "going to cut the girder open to find out.",
        "commit": "How would you find out what is inside a solid block of "
                  "steel, and where?",
        "options": [
            "Tap it all over and listen for the place where the note "
            "sounds dull",
            "Warm one end and see where along it the heat gets held up "
            "on the way",
            "Send a short pulse of sound into it and time anything that "
            "comes back",
            "Weigh it very precisely, since a crack means some metal must "
            "be missing",
        ],
        "answer": 2,
        "reveal": "Sound goes into steel perfectly well, and it reflects "
                  "wherever it meets a boundary between one material and "
                  "another — and a crack is a boundary, steel against air. "
                  "Time the echo, use the speed of sound in steel, and halve "
                  "it. <strong>The whole method is the echo you already "
                  "know, at a frequency chosen so that something two "
                  "millimetres across is big enough to reflect it.</strong>",
    },

    "misconceptions": [
        {"id": "WAVE-33",
         "statement": "Ultrasound is a special kind of wave that can get "
                      "through solids where ordinary sound cannot.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "WAVE-34",
         "statement": "A scan works by shining ultrasound through you and "
                      "seeing what comes out the other side.",
         "confronted_by": "s-think"},
        {"id": "WAVE-35",
         "statement": "Ultrasound is used because it travels faster than "
                      "audible sound.",
         "elicited_by": "s-ladder",
         "confronted_by": "gauge"},
        {"id": "WAVE-36",
         "statement": "The gel on the skin is there to help the probe slide "
                      "about.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Ultrasound</strong> is sound above the top of the "
                 "human range, so above about 20 000 Hz. Nothing else about "
                 "it is unusual. It is made by something vibrating, it needs "
                 "a material to travel through, it moves at that material's "
                 "speed of sound, and it reflects wherever it meets a "
                 "boundary between one material and another. Every one of "
                 "those is the ordinary behaviour of sound, and every one of "
                 "them is what the applications rely on."},
        {"type": "explainer",
         "text": "What ultrasound is useful for splits neatly in two. "
                 "Sometimes what is wanted is the <strong>energy</strong> "
                 "the wave carries: enough of it, concentrated in a small "
                 "space, will shake dirt off a surface or warm tissue "
                 "several centimetres under the skin. Sometimes what is "
                 "wanted is the <strong>information</strong> it brings back: "
                 "send in a short pulse, time what returns, and the timing "
                 "tells you where the boundaries are. A microphone does the "
                 "information job at ordinary frequencies, turning the "
                 "pattern in the air into a matching pattern of electricity."},

        # ── #s-gauge · the flaw gauge ──────────────────────────────────
        {"type": "flaw-gauge",
         "id": "gauge",
         "anchor": "s-gauge",
         "eyebrow": "At the bench · a probe on a block, and a screen showing "
                    "two pips",
         "heading": "Send a pulse in. Time what comes out.",
         "progress": "Change a control to begin",
         "lead": "A probe pressed to the top of a block sends a short pulse "
                 "of ultrasound straight down and listens. The screen shows "
                 "the moment it left and the moment it came back. Set the "
                 "material, and set how deep the reflector is.",
         "window_ms": 0.30,
         "mat_label": "What the block is",
         "start_mat": 0,
         "probe_label": "PROBE",
         "sent_label": "SENT",
         "axis_label": "TIME AFTER THE PULSE LEFT",
         # ⚠️ `band_anchor` / `band_at` ARE THE KEYS `_sibling` READS.
         # These said `sibling` / `sibling_at`, which the drawer ignored in
         # silence — the wrapper shipped with no `data-sibling`, so nothing
         # ever ticked `#s-uses` and the rail carried a stop that could not
         # complete. MRB-208's gate cannot see it: the band section carries
         # `data-stage-done="0"`, which IS a signal `doneByDom()` reads, so
         # the stop looks reachable and never becomes true.
         # `band_at` is 1 because Design's own DONE gives this stop the
         # GATE alone, while the bench also wants a control touched.
         "band_anchor": "s-uses",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. The same reflector sits 100 mm down in "
                       "a block of steel and in a block of water. Which echo "
                       "comes back sooner?",
             "options": [
                 "The water, because a liquid lets sound through more "
                 "easily than a solid",
                 "The steel, because a solid reflects more of the pulse "
                 "than a liquid does",
                 "They come back together, because the depth is the same in "
                 "both",
                 "The steel, because its particles are closer together and "
                 "more strongly linked",
             ],
             "answer": 3,
         },
         "depth": {"label": "How deep the reflector is", "min": 10,
                   "max": 200, "step": 5, "start": 100, "value": "100 mm"},
         "materials": [
             {"id": "steel", "label": "Steel", "v": 5000,
              "state": "a solid, strongly bonded",
              "caption": "STEEL BLOCK — SOUND AT ABOUT 5000 m/s",
              "note": "Steel passes the pulse on quickly, at about 5000 m/s, "
                      "so the echo is back almost at once and the two pips "
                      "sit close together. Reading a depth from a gap this "
                      "small is why the timing has to be measured in "
                      "thousandths of a second."},
             {"id": "aluminium", "label": "Aluminium", "v": 6300,
              "state": "a solid, lighter than steel",
              "caption": "ALUMINIUM BLOCK — SOUND AT ABOUT 6300 m/s",
              "note": "Aluminium is the fastest material here at about "
                      "6300 m/s, so the same reflector at the same depth "
                      "sends its echo back sooner than steel would. A gauge "
                      "set up for steel and used on aluminium reads every "
                      "depth too deep, which is why the material has to be "
                      "dialled in first."},
             {"id": "water", "label": "Water", "v": 1500,
              "state": "a liquid",
              "caption": "WATER TANK — SOUND AT ABOUT 1500 m/s",
              "note": "Water is much slower than either metal at about "
                      "1500 m/s, so the two pips are far apart and the depth "
                      "is easy to read. Soft tissue is close to water, which "
                      "is why the same trick works on a body."},
         ],
         "readouts": [
             {"id": "depth", "label": "Depth of the reflector",
              "sub": "below the probe face"},
             {"id": "speed", "label": "Speed in this material", "sub": "—"},
             {"id": "path", "label": "Total path, down and back"},
             {"id": "time", "label": "Time between the pips"},
         ]},

        # ── #s-uses · energy against information ───────────────────────
        {"type": "wave-band",
         "id": "uses-split",
         "anchor": "s-uses",
         "eyebrow": "The figure",
         "heading": "Carrying energy, or carrying information",
         "panels": [
             {"num": "1", "name": "Energy · cleaning bath",
              "tell": "about 40 000 Hz",
              "body": "The wave's energy makes microscopic bubbles form and "
                      "collapse against every surface in the tank, scrubbing "
                      "dirt out of places no brush reaches. Jewellery, "
                      "spectacles, engine parts and surgical instruments."},
             {"num": "2", "name": "Energy · physiotherapy",
              "tell": "about 1 000 000 to 3 000 000 Hz",
              "body": "The energy is absorbed a few centimetres into the "
                      "tissue and warms it there, which is hard to do from "
                      "the surface. Used on strained muscles and stiff "
                      "joints, under the direction of a physiotherapist."},
             {"num": "3", "name": "Information · medical scan",
              "tell": "about 2 000 000 to 15 000 000 Hz",
              "body": "Every boundary inside the body sends part of the "
                      "pulse back. Timing each echo gives its depth, and "
                      "thousands of them together are assembled into a "
                      "picture. No cutting, and no ionising radiation."},
             {"num": "4", "name": "Information · microphone",
              "tell": "ordinary audible sound, about 20 to 20 000 Hz",
              "body": "The arriving wave sets a diaphragm vibrating, and its "
                      "movement becomes a changing voltage with the same "
                      "pattern in it. The information in the sound is now in "
                      "a wire, and can be stored, sent or amplified."},
         ],
         "close": "The energy uses want as much of the wave delivered into "
                  "one place as possible. The information uses want as "
                  "little disturbance as possible and care only about what "
                  "comes back, and when. Same physics, opposite priorities — "
                  "which is why a scanner runs at a tiny fraction of a "
                  "cleaning bath's power."},

        {"type": "key-fact", "ref": "what-ultrasound-is-for"},

        {"type": "misconception", "id": "think-ultrasound-special",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-ultrasound-special",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-33",
         "statements": [
             {"quote": "Ultrasound is a special kind of wave that can get "
                      "through solids where ordinary sound cannot.",
              "targets": "WAVE-33",
              "body": [
                  "Ordinary sound gets through solids extremely well \u2014 "
                  "better than through air, in fact, because the particles "
                  "are closer together and more strongly linked. Put your "
                  "ear against a wall and you will hear the room next door "
                  "more clearly than through the doorway. Ultrasound is not "
                  "a different kind of wave at all: it is the same "
                  "longitudinal pressure wave, just at a frequency above "
                  "the top of our hearing. What the high frequency buys is "
                  "a short wavelength, and a short wavelength reflects off "
                  "small things. That is why a scanner can pick out a "
                  "two-millimetre crack and a shout cannot.",
              ]},
             {"quote": "A scan works by shining ultrasound through you and "
                      "seeing what comes out the other side.",
              "targets": "WAVE-34",
              "body": [
                  "Almost nothing comes out of the other side, and the "
                  "machine is not looking there anyway. The probe sends a "
                  "pulse and then listens with the same face it sent from, "
                  "timing every echo that returns from a boundary inside. "
                  "That is also why the operator puts gel between the probe "
                  "and the skin: a thin layer of air between two solids "
                  "reflects almost the entire pulse straight back off the "
                  "surface, and the machine would see the skin and nothing "
                  "else. The gel removes the air and lets the pulse into "
                  "the body at all.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "what-ultrasound-is-for",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Ultrasound is sound above the top of the human range, above "
                 "about 20 000 Hz, and it behaves like any other sound: it "
                 "needs a material, travels at that material's speed of "
                 "sound, and reflects at a boundary. It is used either for "
                 "the energy it carries — ultrasonic cleaning and "
                 "physiotherapy — or for the information it brings back, "
                 "where the time an echo takes gives the depth of whatever "
                 "sent it. A microphone does the same information job for "
                 "audible sound, turning it into a matching electrical "
                 "signal."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 0.
    "ladder": {
        "recall": {
            "q": "A probe on a steel block sends a pulse down and the echo "
                 "returns 0.060 ms after it left. Sound travels at about "
                 "5000 m/s in steel. How deep is the reflector?",
            "options": [
                "About 300 mm — speed times time gives the depth",
                "About 75 mm — halve the time and then halve the distance",
                "About 150 mm",
                "About 150 mm/s",
            ],
            "answer": 2,
            "feedback": {
                0: "Speed times time gives the whole journey, down and back "
                   "again. The reflector is halfway along it, so halve the "
                   "300 mm.",
                1: "Halving twice takes a quarter. Halve once: either use "
                   "half the time for the downward trip, or work out the "
                   "full 300 mm path and take half of that.",
                3: "The number is right and the unit is wrong. The question "
                   "asked how deep, which is a distance, and metres per "
                   "second is a speed.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A student says ultrasound is used inside metal and inside "
                 "bodies because ordinary sound cannot travel through "
                 "solids. Which statement is right?",
            "options": [
                "Ultrasound is used because it travels faster than audible "
                "sound and so returns sooner.",
                "Ordinary sound travels through solids very well; "
                "ultrasound is used because its short wavelength reflects "
                "off small features, giving detail a low frequency could "
                "not.",
                "Ultrasound is used because it is much louder, so more of "
                "it survives the journey.",
                "The student is right — audible sound is stopped by solid "
                "material, which is why walls keep noise out, so only a "
                "frequency above our hearing can get into something solid "
                "at all",
            ],
            "answer": 1,
            "feedback": {
                0: "Every frequency travels at the same speed through the "
                   "same material. The pulse would come back at exactly the "
                   "same moment at any frequency — it just would not tell "
                   "you as much.",
                2: "Loudness is amplitude and it is not what changes here. "
                   "Scanners run at very low power on purpose; the useful "
                   "property is the short wavelength.",
                3: "Walls reduce noise rather than stop it, and sound "
                   "actually travels faster in a solid than in air. "
                   "Ultrasound is chosen for the detail it gives, not for "
                   "getting in at all.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain how an engineer uses a probe and a timer to find "
                 "a crack hidden inside a steel girder, and how they work "
                 "out how deep it is.",
            "field_label": "Your explanation",
            "placeholder": "The probe sends a short pulse…",
            "success": [
                "Says the probe sends a short pulse of ultrasound into the "
                "steel.",
                "Says the pulse reflects at the boundary where the crack "
                "is.",
                "Says the probe listens for the echo and the time between "
                "sending and receiving is measured.",
                "Uses the speed of sound in steel with that time to get the "
                "total path.",
                "Halves the total path to get the depth, because the pulse "
                "went down and came back.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Before a scan the operator squeezes a cold gel onto the "
                 "skin and presses the probe into it. Explain why the scan "
                 "would not work with a thin layer of air between the probe "
                 "and the skin.",
            "field_label": "Your answer",
            "placeholder": "At a boundary between two materials…",
            "success": [
                "Says sound is partly reflected wherever it meets a "
                "boundary between two different materials.",
                "Says a probe-to-air boundary reflects almost all of the "
                "pulse straight back.",
                "Says almost none of the pulse would get into the body, so "
                "there would be nothing to make a picture from.",
                "Says the gel fills the gap so the pulse passes from the "
                "probe into the skin without a layer of air in the way.",
                "Mentions that the returning echoes would face the same "
                "problem coming back out.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Ultrasound is sound above about 20 000 Hz, and it obeys all "
                "the ordinary rules of sound: it needs a material, it travels "
                "at that material's speed of sound, and it reflects at a "
                "boundary between materials. It is used for the energy it "
                "carries, in ultrasonic cleaning baths and in physiotherapy, "
                "and for the information it brings back, where timing an echo "
                "gives the depth of whatever reflected it. The pulse travels "
                "down and back, so the depth is half the total path. A "
                "microphone does the information job for audible sound, "
                "turning the pattern in the air into a matching electrical "
                "signal.",

    "stretch": [
        {"id": "detail-costs-frequency",
         "type": "explainer",
         "text": "Why the frequency has to be so high is a question about "
                 "wavelength. A wave reflects usefully off something roughly "
                 "its own size or larger, and at 5 MHz in soft tissue the "
                 "wavelength is about 0.3 mm, so features a fraction of a "
                 "millimetre across show up. Drop to an audible 5000 Hz and "
                 "the wavelength in the same tissue is about 300 mm — the "
                 "width of the whole abdomen — and the pulse would sail past "
                 "everything inside without noticing it. <strong>Detail "
                 "costs frequency</strong>, which is why a scanner looking "
                 "deep into a body uses a lower frequency than one looking "
                 "at something just under the skin: high frequencies are "
                 "absorbed faster and do not reach as far, so every scan is "
                 "a trade between how deep and how sharp."},
        {"id": "the-bat-makes-the-same-trade",
         "type": "explainer",
         "text": "The same trade turns up in nature. A bat hunting in the "
                 "open uses a lower call that reaches further; the same bat "
                 "closing on a moth switches to a higher, shorter call and "
                 "fires it many times a second, giving up range for detail "
                 "exactly when it needs the detail."},
    ],

    "support": [],

    # ⊕ §8.10 · same treatment as `p6-08`, and the same reasoning: a quiet
    # `.ks3-legal` foot line, not a callout, and not the `support[]` layer.
    "safeguarding_note": "If a scan or a course of treatment has been "
                         "mentioned to you and you are anxious about it, "
                         "asking what it is for and what will happen is "
                         "always reasonable. You can talk to a doctor, a "
                         "school nurse or any adult you trust. Childline is "
                         "free, confidential and open at any hour, on 0800 "
                         "1111, and you do not have to give your name.",

    "vocabulary": [
        {"term": "ultrasound",
         "definition": "Sound above the top of the human range, over about "
                       "20 000 Hz. Ordinary sound in every other respect."},
        {"term": "boundary",
         "definition": "The place where one material meets another. Some of "
                       "a wave is always reflected there."},
        {"term": "pulse",
         "definition": "A very short burst of sound, sent so that its echo "
                       "can be timed separately from it."},
    ],

    "tutor": {
        "anchor": "s-gauge",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got an echo time and a material, and want the depth?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Ultrasound imaging and echo sounding calculations, "
                   "reflection and transmission at a boundary, and how "
                   "ultrasound compares with X-rays for medical imaging.",

    "convention_note": "The bench is a teaching model. The speeds are round "
                       "values for one ordinary sample of each material at "
                       "about 20 degrees Celsius, and they shift with alloy, "
                       "temperature and, in a real inspection, with the kind "
                       "of wave the probe launches; published figures for "
                       "steel run from about 5000 to about 5900 m/s. The "
                       "block is drawn to scale in depth from 0 to 200 mm, "
                       "and the timing trace is to scale over a fixed 0.30 "
                       "millisecond window; the pulse is treated as leaving "
                       "at an instant and reflecting cleanly off one "
                       "boundary, whereas a real trace also shows the far "
                       "face of the block, edge reflections and noise. How "
                       "much of a pulse a boundary sends back depends on the "
                       "two materials either side of it and is not modelled "
                       "here. Physiotherapy and medical scanning are "
                       "described, not instructed, and both are carried out "
                       "by trained practitioners.",

    "ws": ["measurement"],
}
