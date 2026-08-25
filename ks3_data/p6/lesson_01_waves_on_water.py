"""P6 L1 — Waves on water: what a wave is (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-01-waves-on-water.dc.html`.

Her page wins outright. The gull, the four-part figure, the ripple tank
and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA FIGURE, AND NONE IS OWED ──────────────────

`OBW.01` is qualitative. Wave speed = frequency × wavelength is GCSE and
**was not invented to have something to put in a triangle.** Design draws
none, and the word "triangle" appears zero times on her page.

── ⚖️ RULED · THIS LESSON NAMES NO FREQUENCY (her FLAG 2) ────────────

A wave has one, and this lesson is about the SHAPE of a wave rather than
its rate. A hertz readout on the tank would make `p6-01` a second claimant
of `SND.01`, which `p6-05` owns. The tank reports amplitude and wavelength
in millimetres and the paddle rate in words only, and `p6-05` is carried
as an edge. `r_ripple_tank` refuses a payload with a frequency in it.

── ⚖️ RULED · BOTH AXES TO ONE SCALE (her FLAG 7) ────────────────────

That makes the largest amplitude 35 px on a 1000-wide viewBox — small,
and deliberately so. The 1-in-7 steepness claim is drawable only if the
drawing is honest in both directions, and exaggerating the vertical would
make the geometry contradict the label beside it.

── ⚖️ RULED · "ROUGHLY 1 IN 7" KEEPS ITS HEDGE ───────────────────────

The breaking steepness varies with depth, wind and how the wave was made.
The foot line says so.

── ⚖️ RULED · THE CIRCLES ARE IN *GOING FURTHER*, NOT IN THE MODEL ───

Water in a wave travels round small near-circles rather than straight up
and down. Design puts that in the stretch layer and in the foot line, and
draws the straight version — because the straight version is what shows
what TRANSVERSE means, and the circles are a correction a student can only
appreciate once they have the idea. Kept exactly there.

── ⚠️ FOUR RAIL STOPS, AND `s-parts` IS ONE OF THEM ──────────────────

    s-hook · s-parts · s-tank · s-ladder

Design's `DONE`: `s-parts` is `s.part !== null` — the anatomy figure is a
real demand, not a diagram. It ticks when the student picks a part.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-01  the water travels along with the wave
    WAVE-02  a bigger wave is a longer wave
    WAVE-03  the amplitude runs from the trough up to the crest
    WAVE-04  a wave that moves the surface up and down is standing still

`WAVE-03` is not in Design's proposed table — it arrived with her own
trough note, *"crest to trough is 0.16 m, and that is not the
amplitude"*, and with rung 1's second option. It is the single most common
misreading of a wave diagram and it is separate from `WAVE-02`.
`WAVE-04` arrived with the hook's third option.
"""

LESSON = {
    "slug":  "waves-on-water",
    "title": "Waves on water: what a wave is",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "MODEL",

    "covers": ["KS3.P.OBW.01a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": [],
    "before_this": "Nothing — this is where the unit starts.",
    "assumes": [],
    "references": ["transverse-waves-and-superposition",
                   "frequency-pitch-and-loudness"],
    "ks4_links": [],

    "meta_description": "A wave crosses a pond in seconds and the gull "
                        "sitting on it finishes exactly where it started. "
                        "Both are true at once, and the second one is the "
                        "more useful.",

    "big_question": "A wave crosses a pond in seconds. Drop a cork in and it "
                    "bobs a hundred times and stays exactly where you put "
                    "it. Both of those are true at once, and the second one "
                    "is the more useful.",

    "rail": [
        {"anchor": "s-hook",   "short": "GULL",
         "label": "The gull that stays put", "done_when": "committed"},
        {"anchor": "s-parts",  "short": "PARTS",
         "label": "The parts of a wave",     "done_when": "a_part_chosen"},
        {"anchor": "s-tank",   "short": "TANK",
         "label": "Ripple tank",             "done_when": "gate_and_a_slider"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The wave crosses the whole pond. The gull does not.",
        "prompt": "A gull is sitting on open water. A line of waves comes in "
                  "under it, one after another, for a full minute. The waves "
                  "reach the far side. The gull is exactly where it started.",
        "commit": "Something clearly travelled from one side to the other. "
                  "What was it?",
        "options": [
            "Nothing travelled — the water only went up and down, so the "
            "wave was standing still",
            "The water travelled across the pond, and the gull was too "
            "light to be carried with it",
            "The disturbance travelled across the pond; the water and the "
            "gull moved up and down on the spot",
            "The wind travelled across the pond and the water simply "
            "followed it",
        ],
        "answer": 2,
        "reveal": "The water did not go anywhere. Each patch of it lifted and "
                  "dropped and finished where it began, and so did the gull. "
                  "What crossed the pond was the <strong>disturbance</strong> "
                  "— the pattern of lifting and dropping, handed on from one "
                  "patch of water to the next, carrying energy with it. That "
                  "travelling disturbance is a <strong>wave</strong>.",
    },

    "misconceptions": [
        {"id": "WAVE-01",
         "statement": "The water travels along with the wave.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "WAVE-02",
         "statement": "A bigger wave is a longer wave.",
         "elicited_by": "tank",
         "confronted_by": "s-think"},
        {"id": "WAVE-03",
         "statement": "The amplitude runs from the trough up to the crest.",
         "elicited_by": "s-ladder",
         "confronted_by": "parts"},
        {"id": "WAVE-04",
         "statement": "A wave whose water only goes up and down is standing "
                      "still.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>wave</strong> is a disturbance that travels, "
                 "carrying energy from one place to another without carrying "
                 "the material with it. On water the disturbance is an "
                 "<strong>undulation</strong>: the surface rises into a "
                 "<strong>crest</strong> and drops into a "
                 "<strong>trough</strong>, over and over. The water itself "
                 "moves up and down — at right angles to the direction the "
                 "wave is travelling — which is what makes a water wave a "
                 "<strong>transverse</strong> wave."},
        {"type": "explainer",
         "text": "Two measurements describe the shape of it, and they are "
                 "independent of each other. The <strong>amplitude</strong> "
                 "is how far the surface rises above the still level, "
                 "measured in millimetres or metres. The "
                 "<strong>wavelength</strong> is the distance from one crest "
                 "to the next crest, measured the same way. <strong>Changing "
                 "one does not change the other.</strong>"},

        # ── #s-parts · the anatomy figure ──────────────────────────────
        {"type": "wave-anatomy",
         "id": "parts",
         "anchor": "s-parts",
         "eyebrow": "The figure",
         "heading": "Pick a part to measure",
         "travel_label": "the wave travels this way",
         "alt_base": "A wave drawn to scale: wavelength 0.40 metres, "
                     "amplitude 0.08 metres, with a dashed still level "
                     "through the middle and an arrow showing the direction "
                     "of travel.",
         "resting_note": "Nothing is marked yet. This wave is drawn to one "
                         "scale in both directions: 0.40 m from crest to "
                         "crest, and 0.08 m from the still level up to a "
                         "crest.",
         "parts": [
             {"id": "crest", "label": "Crest",
              "note": "The crest is the highest point of the undulation. On "
                      "this wave three crests fall inside the figure, each "
                      "one 0.08 m above the still level and 0.40 m from the "
                      "next."},
             {"id": "trough", "label": "Trough",
              "note": "The trough is the lowest point, 0.08 m below the "
                      "still level — the same distance down as the crest is "
                      "up. Crest to trough is 0.16 m, and that is not the "
                      "amplitude."},
             {"id": "amp", "label": "Amplitude",
              "note": "Amplitude is measured from the still level to a "
                      "crest: 0.08 m here. It is how far the surface is "
                      "displaced, not how far it travels from top to "
                      "bottom."},
             {"id": "wav", "label": "Wavelength",
              "note": "Wavelength is one whole wave: 0.40 m from this crest "
                      "to the next. Trough to trough gives the same 0.40 m, "
                      "and so does any point to the matching point on the "
                      "following wave."},
         ]},

        # ── #s-tank · the ripple tank ──────────────────────────────────
        {"type": "ripple-tank",
         "id": "tank",
         "anchor": "s-tank",
         "eyebrow": "At the bench · a ripple tank one metre across",
         "heading": "One paddle. Two things you can change about it.",
         "progress": "Move a control to begin",
         "lead": "A motor dips a paddle into one end of the tank. How deep "
                 "it dips, and how far apart it lays the crests, are set "
                 "separately. A float sits at the middle of the tank.",
         "width_m": 1.0,
         "width_label": "1.00 m ACROSS",
         "break_at": 0.143,
         "px_per_mm": 0.88,
         "gate": {
             "prompt": "Commit first. The paddle dips deeper but keeps "
                       "exactly the same rhythm. What happens on the water?",
             "options": [
                 "The crests get taller and stay the same distance apart",
                 "The crests get taller and move closer together",
                 "The crests stay the same height and move closer together",
                 "Nothing changes on the water — a deeper dip just pushes "
                 "the wave further along the tank",
             ],
             "answer": 0,
         },
         "amp": {"label": "How deep the paddle dips", "min": 5, "max": 40,
                 "step": 5, "start": 20, "value": "20 mm"},
         "wav": {"label": "How far apart it lays the crests", "min": 100,
                 "max": 500, "step": 50, "start": 300, "value": "300 mm"},
         # ⚖️ THREE BRANCHES, KEYED TO STEEPNESS — height ÷ wavelength —
         # so every reachable state falls in exactly one, and the breaking
         # band is the one the 1-in-7 figure exists for.
         "branches": {
             "breaking": "{head}Water cannot hold a shape steeper than about "
                         "1 in 7: past that the crest spills forward and the "
                         "wave breaks, which is why surf exists. {waves} "
                         "waves fit across the 1.00 m tank, and the float "
                         "still finishes where it started — it rises and "
                         "falls through {swing} mm and goes nowhere.",
             "ordinary": "{head}That is an ordinary ripple: steep enough to "
                         "see clearly, well short of the roughly 1 in 7 at "
                         "which a crest spills over and breaks. {waves} "
                         "waves fit across the 1.00 m tank, and the float "
                         "rises and falls through {swing} mm without moving "
                         "along.",
             "swell": "{head}That is a low, long swell — the shape open "
                      "ocean carries between storms. It lifts the float "
                      "{swing} mm and sets it down again, and only {waves} "
                      "waves fit across the 1.00 m tank.",
         },
         "readouts": [
             {"id": "amp", "label": "Amplitude",
              "sub": "above the still level"},
             {"id": "wav", "label": "Wavelength", "sub": "—"},
             {"id": "swing", "label": "The float rises and falls through",
              "sub": "and stays in the same place"},
             {"id": "steep", "label": "Steepness"},
         ]},

        {"type": "key-fact", "ref": "a-wave-is-a-travelling-disturbance"},

        {"type": "misconception", "id": "think-water-travels",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-water-travels",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-01",
         "statements": [
             {"quote": "The water travels along with the wave.",
              "targets": "WAVE-01",
              "body": [
                  "Drop a cork in a tank and send a hundred waves under it. "
                  "The cork bobs a hundred times and ends up where it "
                  "started. If the water were travelling, the far end of "
                  "the tank would fill up and the near end would empty, and "
                  "a swimmer would be carried out to sea by every passing "
                  "swell. What travels is the disturbance, handed from each "
                  "patch of water to the next; each patch lifts its "
                  "neighbour, gets lifted in turn, and settles back. Energy "
                  "moves across the tank. Water does not.",
              ]},
             {"quote": "A bigger wave is a longer wave.",
              "targets": "WAVE-02",
              "body": [
                  "Two different measurements are hiding inside the word "
                  "<em>bigger</em>. Amplitude is how far the surface lifts; "
                  "wavelength is how far apart the crests are. A wave can "
                  "be tall and short — a steep chop with crests a hand's "
                  "width apart — or low and long, like an ocean swell that "
                  "lifts a boat a few centimetres over a hundred metres. "
                  "The bench above sets the two independently, and moving "
                  "one leaves the other exactly where it was.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-wave-is-a-travelling-disturbance",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A wave carries energy from place to place without carrying "
                 "the material with it. On water the surface rises into "
                 "crests and drops into troughs at right angles to the "
                 "direction of travel, which makes it transverse. Amplitude "
                 "is the rise above the still level; wavelength is the "
                 "distance from one crest to the next. Neither one sets the "
                 "other."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. P6 has eighteen rungs; they cycle
    # so that the unit closes on [5, 5, 4, 4]. This lesson takes 0 and 1.
    "ladder": {
        "recall": {
            "q": "A wave on a tank has crests 0.60 m apart. A float on it "
                 "rises 0.05 m above the still level and drops 0.05 m below "
                 "it. Give the wavelength and the amplitude.",
            "options": [
                "Wavelength 0.60 m, amplitude 0.10 m — amplitude runs from "
                "the trough up to the crest",
                "Wavelength 0.05 m, amplitude 0.60 m — the bigger number is "
                "the size of the wave",
                "Wavelength 0.60 m, amplitude 0.05 m",
                "Wavelength 0.30 m, amplitude 0.05 m — wavelength runs from "
                "a crest to the next trough",
            ],
            "answer": 2,
            "feedback": {
                0: "Amplitude is measured from the still level, not from "
                   "trough to crest. Trough to crest is 0.10 m here, which "
                   "is twice the amplitude.",
                1: "The two measurements are in fixed places, not in order "
                   "of size. Wavelength is along the water; amplitude is up "
                   "from the still level.",
                3: "Crest to trough is half a wave. Wavelength is one whole "
                   "wave: crest to the next crest, which is the 0.60 m you "
                   "were given.",
            },
            "title": "Rung 1 · Read the wave"},
        "apply": {
            "q": "Waves pass under a gull for a minute and the gull "
                 "finishes exactly where it started. Which statement is "
                 "right?",
            "options": [
                "The water travelled along with the wave, but a gull is too "
                "light to be dragged with it.",
                "Each patch of water lifted and dropped on the spot and "
                "passed the disturbance on, so energy crossed the water and "
                "the water did not.",
                "Each wave carried the gull forward and the next one "
                "carried it back the same distance, so the two cancelled "
                "out, and the gull finished where a floating thing always "
                "finishes: at the place the water left it",
                "The waves cannot have been moving, because a moving wave "
                "would have moved the gull.",
            ],
            "answer": 1,
            "feedback": {
                0: "A heavier object would have finished in the same place. "
                   "Nothing floating is dragged along, because the water "
                   "underneath is not going anywhere.",
                2: "The verdict is right and the rule underneath it is "
                   "wrong. There is no forward carry to cancel: the water "
                   "lifts and drops, and the gull rides up and down with "
                   "it.",
                3: "The waves moved and the water did not go with them. A "
                   "wave is a travelling disturbance in the water, not a "
                   "lump of water in transit.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A cork floats in a ripple tank while waves cross from one "
                 "end to the other. Explain what the cork does and what the "
                 "wave does, using the words disturbance, energy and "
                 "transverse.",
            "field_label": "Your explanation",
            "placeholder": "The cork moves…",
            "success": [
                "Says the cork moves up and down and returns to the same "
                "place.",
                "Says the wave, not the water, travels across the tank.",
                "Says what travels is a disturbance, passed from one patch "
                "of water to the next.",
                "Says the wave carries energy from one end of the tank to "
                "the other.",
                "Says the water moves at right angles to the direction the "
                "wave travels, which is what transverse means.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A crowd in a stadium sends a wave right round the ground "
                 "in 40 seconds, and nobody leaves their seat. Say what "
                 "plays the part of the amplitude and what plays the part "
                 "of the wavelength, then give one way this is not like a "
                 "wave on water.",
            "field_label": "Your answer",
            "placeholder": "Each person stands and sits, so…",
            "success": [
                "Says each person stands and sits and stays in their own "
                "seat.",
                "Says the disturbance travels round the ground while the "
                "people do not.",
                "Names the amplitude as how far each person rises — how far "
                "out of the seat they stand.",
                "Names the wavelength as the distance between one standing "
                "group and the next.",
                "Gives one real difference, such as: people decide when to "
                "stand, whereas water is pushed by its neighbours; or the "
                "crowd wave only goes one way round.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A wave is a travelling disturbance that carries energy from "
                "place to place without carrying the material with it. Waves "
                "on water are undulations: the surface rises into crests and "
                "drops into troughs, moving at right angles to the direction "
                "the wave travels, which makes them transverse. Amplitude is "
                "the rise above the still level and wavelength is the "
                "distance from one crest to the next; changing one does not "
                "change the other.",

    "stretch": [
        {"id": "the-tsunami-that-a-ship-misses",
         "type": "explainer",
         "text": "The independence of amplitude and wavelength is what makes "
                 "deep-ocean tsunamis so dangerous. Out over deep water a "
                 "tsunami has an amplitude of well under a metre and a "
                 "wavelength that can reach 200 km, which is a steepness of "
                 "about 1 in 200 000 — <strong>a ship rides over it and the "
                 "crew notice nothing at all.</strong> The energy is still "
                 "there; it is simply spread through a very long, very low "
                 "undulation. When that undulation reaches shallow water it "
                 "slows, the back of it catches the front, and the same "
                 "energy is repacked into something short and tall."},
        {"id": "the-circles-under-a-swell",
         "type": "explainer",
         "text": "One honest limit of the picture drawn above: the water in "
                 "a wave does not move in a straight line up and down. Each "
                 "patch travels round a small near-circle, forward at the "
                 "crest and backward in the trough, returning to about where "
                 "it began. The straight up-and-down version is close enough "
                 "to see what transverse means, and it is what the bench "
                 "draws, but a diver watching sand grains under a swell sees "
                 "the circles."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "wave",
         "definition": "A travelling disturbance that carries energy from "
                       "place to place without carrying the material with "
                       "it."},
        {"term": "amplitude",
         "definition": "How far the surface rises above the still level. NOT "
                       "the distance from trough to crest, which is twice "
                       "as much."},
        {"term": "wavelength",
         "definition": "The distance from one crest to the next — one whole "
                       "wave. Trough to trough gives the same answer."},
        {"term": "transverse",
         "definition": "The material moves at right angles to the direction "
                       "the wave is travelling."},
    ],

    "tutor": {
        "anchor": "s-tank",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a wave of your own to describe — a rope, a pond, the "
                "sea?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Frequency and period, the wave equation linking wave "
                   "speed to frequency and wavelength, and measuring wave "
                   "speed in a ripple tank.",

    "convention_note": "The tank is a teaching model. Both figures are drawn "
                       "to a single scale in both directions, so the "
                       "steepness you see is the steepness the numbers claim; "
                       "the tank is taken as exactly 1.00 m across and the "
                       "float as weightless, riding the surface without "
                       "disturbing it. The paddle is treated as making one "
                       "steady train of identical waves, which a real paddle "
                       "only approximates. The roughly 1-in-7 limit at which "
                       "a crest spills over and breaks is an approximate "
                       "figure for deep water and shifts with depth, wind and "
                       "how the wave was made. Real water in a wave moves "
                       "round small near-circles rather than straight up and "
                       "down.",

    "ws": [],
}
