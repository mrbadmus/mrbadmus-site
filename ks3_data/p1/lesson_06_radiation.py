"""p1-06 — *Radiation*.

Ported from Claude Design's `p1-06-radiation.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.ECT.02c` — the "or radiation" quarter of the compound heating bullet.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

This lesson takes **3 and 1**. Design puts the correct option first in both
marked rungs; her option text and every correction are verbatim, and only
the button order moves.

── ⚑ MISCONCEPTIONS · `ENER-16` AND `ENER-17` ─────────────────────────

Design's `NOTES-P1.md` §2 calls them `ENERGY-08` and `ENERGY-09`. The prefix
is `ENER` and the numbering continues from `ENER-15`.

    ENER-16  heating always travels upwards          — the three-routes bench
    ENER-17  radiation means the dangerous kind      — the word sort

── ⚖️ HER SCIENCE FLAGS 16 AND 17 ─────────────────────────────────────

Flag 16: infrared is placed at the HARMLESS end and ultraviolet is named as
the boundary. Examiner-sensitive, and the word sort is the mechanism rather
than the prose — a student sorts six cards and finds the boundary themselves
rather than being told where it is.

Flag 17: *"heat rises"* is quoted as STUDENT WORDING and corrected to *"warm
air rises"*. It is never used approvingly anywhere on the page.

── ⊖ WHAT THIS LESSON DOES NOT CONTAIN, AND WHY IT IS NOT AN OMISSION ──

An earlier MRB-223 run authored a Leslie's-cube emissivity bench for this
slot and a science ruling to go with it: that for infrared it is SHINE that
decides emissivity, colour being a second-order effect, so matt white sits
within 8% of matt black.

**Design's page has no Leslie's cube and no emissivity bench at all.** Her
two instruments are the three-routes bench and the six-card word sort. Her
only emissivity content in the whole lesson is one key-fact line — *"more
from matt black ones than from shiny silver ones"* — which contrasts matt
black with SHINY SILVER and never raises matt white.

So the ruling corrects a claim her page does not make, and there is no
instrument for it to attach to. Recorded in `DEPARTURES-P1.md` row A as
considered-and-not-applied rather than silently dropped.
"""

LESSON = {
    "slug":  "radiation",
    "title": "Radiation",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "PROCESS",

    "covers": ["KS3.P.ECT.02c"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 6}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": ["conduction"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "Sunlight crosses 150 million kilometres of nothing "
                        "to reach your face. Conduction needs particles and "
                        "convection needs a fluid — so how does it get "
                        "here? And is “radiation” dangerous?",

    "big_question": "Conduction needs particles touching. Convection needs a "
                    "fluid that can move. Between here and the Sun there is "
                    "neither — and yet you can feel sunlight on your face.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Across empty space", "done_when": "committed"},
        {"anchor": "s-routes", "short": "ROUTES",
         "label": "Three routes",       "done_when": "vacuum_scenario_run"},
        {"anchor": "s-word",   "short": "WORD",
         "label": "The word radiation", "done_when": "all_six_sorted"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Conduction and convection both fail here.",
        "prompt": "Conduction needs particles touching. Convection needs a "
                  "fluid that can move. Between here and the Sun there is "
                  "neither — space is empty. And yet you can feel sunlight "
                  "on your face, and it arrives eight minutes after it "
                  "leaves.",
        "commit": "Commit to how it crosses.",
        "options": [
            "Space is not really empty — thin gas conducts it",
            "As a wave that needs no material at all",
            "Convection currents in the solar wind",
            "The Sun heats the atmosphere, which heats the ground",
        ],
        # ⊕ MRB-297 — THE HOOK'S ANSWER INDEX, ADDED SO THE GATES CAN SEE IT.
        # P1's eight hooks were the only ones in physics with no `answer`,
        # which is why `verify_answer_lengths` and any position check skipped
        # them: the audit recorded them as "the 8 that do not resolve". They
        # resolve perfectly well — every reveal names one option — so the key
        # is written down rather than left to prose-matching. It is INERT to
        # the page: `data-correct` is emitted only by `_rung_marked`, the
        # ladder renderer, and nothing in build_ks3 reads `phenomenon.answer`.
        "answer": 1,
        "reveal": "By <strong>radiation</strong> — a wave that needs no "
                  "material at all and travels perfectly well through "
                  "nothing. It is the same family of thing as visible "
                  "light, just at a wavelength your eyes cannot see, and it "
                  "is the only one of the three routes that works across a "
                  "vacuum. Everything in the room you are sitting in is "
                  "emitting it right now, including you.",
    },

    "misconceptions": [
        {"id": "ENER-16",
         "statement": "Heat rises, so heating always travels upwards.",
         "elicited_by": "three-routes",
         "confronted_by": "think-heat-rises"},
        {"id": "ENER-17",
         "statement": "Radiation means the dangerous kind — anything called "
                      "radiation can harm you.",
         "elicited_by": "radiation-word-sort",
         "confronted_by": "radiation-word-sort"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Radiation is the third and last of the routes, and it is "
                 "the odd one out twice over: it needs no particles, and it "
                 "travels in straight lines in every direction rather than "
                 "following the material. Everything above absolute zero "
                 "emits it — you, this page, a block of ice — and what "
                 "changes with temperature is only how much."},

        # ── #s-routes — bare `ks3-block` → `check`.
        {"type": "three-routes", "id": "three-routes",
         "anchor": "s-routes",
         "demand": "investigate",
         "targets": "ENER-16",
         "eyebrow": "Three routes · take them away one at a time",
         "heading": "Which routes survive?",
         "prompt": "Move the detector and take the air away. Watch which of "
                   "the three routes can still deliver anything — and note "
                   "which one never stops working.",
         "routes": [
             {"id": "cond", "label": "Conduction"},
             {"id": "conv", "label": "Convection"},
             {"id": "rad",  "label": "Radiation"},
         ],
         "scenarios": [
             {"id": "sc1", "label": "Detector above, in air",
              "cond": False, "conv": True, "rad": True,
              "note": "All the routes that can work are working. Warm air "
                      "rises straight into the detector, and radiation "
                      "arrives as well — which is why this is the situation "
                      "that convinces people heat only goes up."},
             {"id": "sc2", "label": "Detector beside, in air",
              "cond": False, "conv": False, "rad": True,
              "note": "Convection has gone — the warm air is going up, not "
                      "sideways. The detector still registers, and the only "
                      "route left is radiation. This is your hand at the "
                      "side of a campfire."},
             {"id": "sc3", "label": "Detector beside, in a vacuum",
              "cond": False, "conv": False, "rad": True,
              "note": "No particles at all, so conduction and convection are "
                      "both impossible. The detector still registers, at "
                      "full strength. Radiation does not need matter — this "
                      "is the Sun and the Earth, in a box."},
             {"id": "sc4", "label": "Touching, in a vacuum",
              "cond": True, "conv": False, "rad": True,
              "note": "Now they touch, so conduction works again even in a "
                      "vacuum — conduction needs particles in contact, not "
                      "air. Two routes running, and convection still has "
                      "nothing to move."},
         ]},

        {"type": "key-fact", "id": "radiation-needs-nothing",
         "ground": "card",
         "text": "Infrared radiation is an electromagnetic wave. It needs no "
                 "particles at all, crosses a vacuum, and is emitted by "
                 "every object — more from hotter surfaces, and more from "
                 "matt black ones than from shiny silver ones."},

        # ── #s-word — `ks3-block ks3-dark ks3-practical` → `practical`.
        {"type": "radiation-word-sort", "id": "radiation-word-sort",
         "anchor": "s-word",
         "demand": "classify",
         "targets": "ENER-17",
         "eyebrow": "The word “radiation” · where is the boundary?",
         "heading": "Six kinds of radiation. Three of them are harmless.",
         "prompt": "Everything here is radiation. Sort each one, then find "
                   "the line — it is not where most people put it.",
         "choices": ["Harmless", "Risky"],
         "sort_items": [
             {"id": "w1", "text": "Infrared from a radiator",
              "answer": "Harmless",
              "right": "Harmless. This is the radiation in this lesson — it "
                       "warms things and cannot break a molecule.",
              "wrong": "Harmless, in fact. It is the same kind of wave as "
                       "visible light, just longer, and it has nowhere near "
                       "the energy needed to damage anything."},
             {"id": "w2", "text": "Visible light from a lamp",
              "answer": "Harmless",
              "right": "Harmless. Light is radiation — you are being "
                       "irradiated by your lamp as you read this.",
              "wrong": "This is radiation and it is harmless. If light were "
                       "dangerous, reading would be a hazard."},
             {"id": "w3", "text": "Radio waves from a phone mast",
              "answer": "Harmless",
              "right": "Harmless. Longer wavelength than infrared, so even "
                       "less energy per wave.",
              "wrong": "Radio waves sit at the very lowest-energy end of the "
                       "family — below infrared, which is itself below "
                       "visible light."},
             {"id": "w4", "text": "Ultraviolet from the Sun",
              "answer": "Risky",
              "right": "Risky. Just past violet, and now there is enough "
                       "energy per wave to damage skin cells. This is the "
                       "boundary.",
              "wrong": "This one genuinely is risky — UV carries enough "
                       "energy to damage DNA, which is why sunburn and skin "
                       "cancer exist."},
             {"id": "w5", "text": "X-rays in a hospital", "answer": "Risky",
              "right": "Risky, which is why doses are controlled and the "
                       "radiographer leaves the room.",
              "wrong": "X-rays carry far more energy per wave than light and "
                       "can ionise atoms. Useful, and used carefully for "
                       "that reason."},
             {"id": "w6", "text": "Gamma rays from a nuclear source",
              "answer": "Risky",
              "right": "Risky — the highest energy of the family, and the "
                       "meaning most people have in mind when they hear the "
                       "word.",
              "wrong": "This is the dangerous end, and it is the one that "
                       "gives the whole word its frightening reputation."},
         ],
         # ⚖️ Flag 16 — the boundary is FOUND by sorting, not announced.
         "close": "The boundary is between visible light and ultraviolet, "
                  "and it is about energy per wave rather than about the "
                  "word. Below it — radio, infrared, light — a wave can warm "
                  "something and nothing more. Above it, a single wave "
                  "carries enough energy to break a molecule apart, and that "
                  "is what makes UV, X-rays and gamma rays a hazard. Three "
                  "of the six on this bench are the kind you are sitting in "
                  "right now."},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # A REFERENCE; the payload is in `activities[]`.
        {"type": "misconception", "id": "think-heat-rises",
         "anchor": "s-think", "targets": "ENER-16"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        # ⊕ #s-think — one "Think again", two wrong ideas, the second behind
        # the amber divider. Design's shape; `r_confrontation`'s `statements`.
        {"id": "think-heat-rises",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-16",
         "statements": [
             # ⚖️ Flag 17 — "heat rises" is quoted as STUDENT WORDING and is
             # never used approvingly. The correction is "warm air rises".
             {"targets": "ENER-16",
              "quote": "Heat rises, so heating always travels upwards.",
              "body": [
                  "What rises is warm air, because it is less dense than the "
                  "cold air around it and floats on it. That is convection, "
                  "and it genuinely does go upwards. But it is one route out "
                  "of three, and the other two ignore gravity entirely.",
                  "Radiation travels in straight lines in every direction at "
                  "once — up, down, sideways. Stand beside a bonfire and one "
                  "side of you is warm; lie under a patio heater and the "
                  "warmth comes down. Conduction is equally indifferent: "
                  "hold a metal rod pointing downwards into a flame and the "
                  "far end still gets hot.",
                  "“Heat rises” is a fact about air, stated as "
                  "if it were a law about energy. Say “warm air "
                  "rises” and the confusion disappears.",
              ]},
             {"quote": "Only hot things give out infrared radiation.",
              "body": [
                  "Everything above absolute zero emits it, including you, "
                  "this page and a block of ice. What changes with "
                  "temperature is how much: a hotter surface emits far more, "
                  "and at shorter wavelengths. A thermal camera pointed at a "
                  "snowy field still sees a picture, because the snow is "
                  "radiating too — it is simply radiating less than "
                  "everything around it.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "Which method of energy transfer does not need any material "
                 "to travel through?",
            # MRB-278: correct at index 3.
            "options": [
                "Conduction",
                "Convection",
                "All three work in a vacuum",
                "Radiation",
            ],
            "answer": 3,
            "feedback": {
                0: "Conduction needs particles in contact to pass the "
                   "vibration along.",
                1: "Convection needs a fluid — a liquid or gas — that can "
                   "physically move.",
                2: "Only one does, and the vacuum setting on the bench shows "
                   "which.",
            }},
        "apply": {
            "q": "You stand to the side of a bonfire, level with the flames, "
                 "and feel warmth on your face. Which transfer is reaching "
                 "you?",
            # MRB-278: correct at index 1.
            "options": [
                "Convection",
                "Radiation",
                "Conduction",
                "None — you would feel nothing standing to the side",
            ],
            "answer": 1,
            "feedback": {
                0: "The warm air is going straight up, not sideways to your "
                   "face.",
                2: "Air is a poor conductor and you are not touching the "
                   "fire.",
                3: "Anyone who has stood near a bonfire knows otherwise. "
                   "Something is arriving.",
            }},
        "explain": {
            "q": "Explain how energy from the Sun reaches the Earth, and why "
                 "the other two methods of transfer cannot be responsible.",
            "field_label": "Your explanation",
            "placeholder": "The space between the Sun and the Earth is…",
            "success": [
                "Says the space between is a vacuum with no particles.",
                "Says conduction cannot work because it needs particles in "
                "contact.",
                "Says convection cannot work because it needs a fluid that "
                "can move.",
                "Says radiation travels as a wave and needs no material.",
                "Says the radiation travels in straight lines and includes "
                "infrared as well as visible light.",
            ]},
        "produce": {
            "q": "A news report describes a new patio heater as "
                 "“using radiation to warm your garden” and a "
                 "reader complains it sounds unsafe. Write a reply that is "
                 "accurate about both the physics and the risk.",
            "field_label": "Your reply",
            "placeholder": "Radiation means energy spreading out from a "
                           "source…",
            "success": [
                "Says radiation means energy spreading out from a source, "
                "and covers many kinds of wave.",
                "Says the heater emits infrared, at the low-energy end of "
                "the family.",
                "Says visible light and radio are also radiation and are "
                "harmless.",
                "Explains that danger comes from having enough energy per "
                "wave to damage molecules — UV and above.",
                "Concludes the heater is safe, and notes the word is being "
                "used narrowly in everyday speech.",
            ]},
    },

    "key_note": "Radiation needs no material and travels in every direction, "
                "which is why it is the only route across a vacuum and why "
                "warmth does not only go upwards. Everything emits it. Only "
                "the high-energy end of the family — ultraviolet and beyond "
                "— can do harm.",

    "stretch": [
        {"type": "explainer", "id": "why-the-sky-is-not-on-fire",
         "text": "If everything emits radiation, why is the night sky dark? "
                 "The question is older than it looks — it is called Olbers' "
                 "paradox, and it goes like this: in an infinitely old, "
                 "infinitely large universe full of stars, every line of "
                 "sight would eventually end on a star, and the whole sky "
                 "would blaze as brightly as the Sun. It does not. The "
                 "resolution is that the universe is neither infinitely old "
                 "nor unchanging: there has not been enough time for light "
                 "from the most distant parts to reach us, and the "
                 "expansion of space has stretched what does arrive to "
                 "wavelengths far below visible. The dark sky is evidence "
                 "that the universe had a beginning — which is a great deal "
                 "to get from looking up."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "radiation",
         "definition": "Energy travelling as an electromagnetic wave. Needs "
                       "no particles, crosses a vacuum, and travels in "
                       "straight lines in all directions."},
        {"term": "infrared",
         "definition": "The part of the electromagnetic family just beyond "
                       "red, emitted by every object. What a thermal camera "
                       "sees."},
        {"term": "vacuum",
         "definition": "A space with no particles in it. Conduction and "
                       "convection are both impossible in one; radiation is "
                       "unaffected."},
        {"term": "emit",
         "definition": "To give out. Every object above absolute zero emits "
                       "infrared radiation, whatever its temperature."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still expecting warmth to travel upwards?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "The electromagnetic spectrum in full, with wavelength "
                   "and frequency attached to each band, and absorption and "
                   "emission treated as a rate.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
}
