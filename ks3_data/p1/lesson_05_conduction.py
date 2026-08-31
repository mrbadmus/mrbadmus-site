"""p1-05 — *Conduction*.

Ported from Claude Design's `p1-05-conduction.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.ECT.02b` — the "through contact (conduction)" quarter of the compound
heating bullet.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

Running plan across the unit's sixteen marked rungs: `p1-01` 0,2 ·
`p1-02` 1,3 · `p1-03` 0,2 · `p1-04` 1,3 · this lesson **2,0** ·
`p1-06` 3,1 · `p1-07` 2,0 · `p1-08` 3,1. That lands 4/4/4/4.

── ⚠️ MRB-177 · HER `r1` IS MARGINAL AND IS LEFT ALONE ────────────────

Measured with the gate's own tokeniser: 6w against a longest distractor of
5w — gap 1, ratio 1.20, inside both limbs. It passes as drawn and is not
re-cut. Only rungs that actually trip the gate are touched.

── ⚑ MISCONCEPTION · `ENER-15` ────────────────────────────────────────

Design's `NOTES-P1.md` §2 calls it `ENERGY-07`; the prefix is `ENER` and the
numbering continues from `ENER-14`. It is the belief that some materials are
inherently colder than others — confronted at the touch test, where four
objects at the SAME temperature feel different.

── ⚖️ TWO OF HER SCIENCE FLAGS ARE LOAD-BEARING HERE ──────────────────

Flag 13: grey home-position rings show that particles never travel. Required
for Rung 3 criterion 3 — *"says the particles themselves do not travel along
the spoon"* — and not to be removed for visual tidiness.

Flag 14: free electrons are shown ONLY for metals, and the control says so
for non-metals rather than silently doing nothing.

Flag 15, recorded and NOT changed: her conduction times (Cu 9 s, Fe 22 s,
glass 150 s, wood never) are illustrative rather than measured. She labels
the limitation herself. See `DEPARTURES-P1.md` row B.
"""

LESSON = {
    "slug":  "conduction",
    "title": "Conduction",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "PROCESS",

    "covers": ["KS3.P.ECT.02b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 5}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": ["heating-and-thermal-equilibrium"],
    "assumes": ["solids-liquids-and-gases"],
    "references": [],
    "ks4_links": [],

    "meta_description": "A metal spoon and a wooden spoon spend the night in "
                        "the same drawer, and the metal one feels colder. "
                        "Both are at room temperature. Learn what your "
                        "fingers actually measure, and why metals win.",

    "big_question": "A metal spoon and a wooden spoon have been in the same "
                    "drawer all night. The metal one feels distinctly "
                    "colder. Which one is colder?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two spoons",       "done_when": "committed"},
        {"anchor": "s-bar",    "short": "ROD",
         "label": "Conduction bench", "done_when": "three_materials_run"},
        {"anchor": "s-touch",  "short": "TOUCH",
         "label": "Touch test",       "done_when": "all_four_judged"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two things in the same room, and one feels colder.",
        "prompt": "A metal spoon and a wooden spoon in the same drawer, "
                  "overnight, in the same kitchen. Pick up both. The metal "
                  "one feels distinctly colder against your fingers and "
                  "everyone agrees about it.",
        "commit": "Commit before you read on.",
        "options": [
            "The metal spoon — metal is a colder material",
            "The wooden spoon, but only slightly",
            "Neither — they are at the same temperature",
            "It depends which one you picked up first",
        ],
        # ⊕ MRB-297 — THE HOOK'S ANSWER INDEX, ADDED SO THE GATES CAN SEE IT.
        # P1's eight hooks were the only ones in physics with no `answer`,
        # which is why `verify_answer_lengths` and any position check skipped
        # them: the audit recorded them as "the 8 that do not resolve". They
        # resolve perfectly well — every reveal names one option — so the key
        # is written down rather than left to prose-matching. It is INERT to
        # the page: `data-correct` is emitted only by `_rung_marked`, the
        # ladder renderer, and nothing in build_ks3 reads `phenomenon.answer`.
        "answer": 2,
        "reveal": "Neither. Put a thermometer on both and they read the "
                  "same, to within a fraction of a degree — they have had "
                  "all night to reach the room's temperature. What differs "
                  "is <strong>how fast each one takes energy out of your "
                  "hand</strong>. Your fingers are not thermometers; they "
                  "are rate detectors, and the metal is winning a race, not "
                  "reporting a temperature.",
    },

    "misconceptions": [
        {"id": "ENER-15",
         "statement": "Metal is a colder material than wood — some "
                      "materials are inherently colder than others.",
         "elicited_by": "s-hook",
         "confronted_by": "touch-test"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Conduction is energy moving through a material by "
                 "particles knocking into their neighbours — <strong>no "
                 "substance travels, only the movement is passed "
                 "along</strong>. In metals there is a second, much faster "
                 "route as well, and that difference is why this lesson has "
                 "a misconception attached to it that survives into "
                 "adulthood."},

        # ── #s-bar — bare `ks3-block` → `check`.
        {"type": "conduction-bench", "id": "conduction-bench",
         "anchor": "s-bar",
         "demand": "investigate",
         "eyebrow": "The conduction bench · race four rods",
         "heading": "Four materials, one flame, four very different times",
         "prompt": "Pick a material, light the flame, and watch the wax blob "
                   "at the far end. Then switch the free electrons on and "
                   "see which materials change.",
         # ⚖️ Flag 15 — illustrative, and the bench says so rather than
         # implying it was measured. Her ratios are right; the absolute
         # values are not a measurement claim.
         "model_note": "These times are illustrative, not measured. The "
                       "ORDER and the rough ratios are right; the exact "
                       "seconds are chosen so a lesson can watch them.",
         # ⚖️ Flag 13 — the grey home-position rings are required for
         # Rung 3 criterion 3 and must not be removed for tidiness.
         "home_ring_note": "The grey rings mark where each particle started. "
                           "Every particle stays on its own ring — the "
                           "energy travels, the matter does not.",
         # ⚖️ Flag 14 — free electrons are shown ONLY for metals, and the
         # control SAYS SO for a non-metal rather than silently doing
         # nothing, which would read as a broken button.
         "electrons": {
             "label": "Show the free electrons",
             "alt": "Hide the free electrons",
             "non_metal_note": "No free electrons in a non-metal — that is "
                               "the whole difference. Nothing to show.",
         },
         "materials": [
             {"id": "cu", "label": "Copper", "metal": True, "wax": 9,
              "note": "Copper is the best of these by a wide margin. The wax "
                      "goes in about nine seconds — and if you switch the "
                      "free electrons on you can see why: two routes working "
                      "at once instead of one."},
             {"id": "fe", "label": "Iron", "metal": True, "wax": 22,
              "note": "Iron is a metal and conducts well, but only about a "
                      "third as well as copper. Same two mechanisms, fewer "
                      "electrons moving as freely."},
             {"id": "gl", "label": "Glass", "metal": False, "wax": 150,
              "note": "No free electrons at all, so the wobble has to be "
                      "passed particle to particle the whole way. Two and a "
                      "half minutes, and the flame end is glowing while the "
                      "far end is barely warm."},
             {"id": "wd", "label": "Wood", "metal": False, "wax": None,
              "note": "Wood barely conducts. The far end never gets there — "
                      "the rod will scorch at the flame end long before the "
                      "wax notices anything. This is why a wooden spoon can "
                      "be left in a hot pan."},
         ]},

        {"type": "key-fact", "id": "energy-travels-matter-does-not",
         "ground": "card",
         "text": "In conduction the energy travels and the matter does not. "
                 "Each particle vibrates about a fixed position and hands "
                 "energy on to its neighbour."},

        # ── #s-touch — `ks3-block ks3-dark ks3-practical` → `practical`.
        {"type": "touch-test", "id": "touch-test",
         "anchor": "s-touch",
         "demand": "classify",
         "targets": "ENER-15",
         "eyebrow": "The touch test · four objects, one temperature",
         "heading": "Every one of these is at 20 °C",
         "prompt": "Say how each one feels. Every object here has been in "
                   "the same room all night and every one is at 20 °C — so "
                   "anything you notice is about your hand, not about the "
                   "object.",
         "choices": ["Feels cold", "Feels neutral"],
         "sort_items": [
             {"id": "t1", "text": "A steel table leg", "answer": "Feels cold",
              "right": "Feels cold, and is at 20 °C. Steel pulls energy from "
                       "your fingers quickly, so your nerves report a fast "
                       "loss and your brain calls it cold.",
              "wrong": "It does feel cold — and it is still at 20 °C. Steel "
                       "takes energy from you fast, and that speed is what "
                       "you are detecting."},
             {"id": "t2", "text": "A wooden desk top",
              "answer": "Feels neutral",
              "right": "Feels neutral, and is at 20 °C — the same as the "
                       "steel. Wood takes energy from you slowly, so almost "
                       "nothing is reported.",
              "wrong": "It feels neutral rather than cold, at the same 20 °C "
                       "as the steel. Wood removes energy from your hand too "
                       "slowly for you to notice."},
             {"id": "t3", "text": "A ceramic tile", "answer": "Feels cold",
              "right": "Feels cold, and is at 20 °C. Ceramic is not a metal "
                       "but it is still a far better conductor than wood, "
                       "which is why a tiled floor feels colder than a "
                       "carpeted one at the same temperature.",
              "wrong": "It feels cold. Ceramic is not a metal, but it "
                       "conducts far better than wood — good enough to pull "
                       "energy from your hand noticeably fast."},
             {"id": "t4", "text": "A woollen jumper",
              "answer": "Feels neutral",
              "right": "Feels neutral or even warm, and is at 20 °C. Wool "
                       "traps air, which is a terrible conductor — the "
                       "jumper is not warm, it is just very bad at taking "
                       "your energy away.",
              "wrong": "It feels neutral or warm, at the same 20 °C. Wool "
                       "traps air and air conducts terribly, so almost no "
                       "energy leaves your hand."},
         ],
         "close": "Four objects, one temperature, two different verdicts "
                  "from your hand. Your skin does not measure temperature at "
                  "all — it measures how fast energy is leaving it. That is "
                  "why the question “which is colder?” had no "
                  "answer, and why a thermometer settles in seconds what "
                  "your fingers will insist on forever."},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # A REFERENCE; the payload is in `activities[]`.
        {"type": "misconception", "id": "think-metal-is-colder",
         "anchor": "s-think", "targets": "ENER-15"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        {"id": "think-metal-is-colder",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-15",
         "statements": [
             {"targets": "ENER-15",
              "quote": "Metal is a colder material than wood.",
              "body": [
                  "A material does not have a temperature of its own. Leave "
                  "anything in a room long enough and it ends up at the "
                  "room's temperature — that is thermal equilibrium, from "
                  "last lesson, and it applies to every object in the room "
                  "without exception.",
                  "What metal has is a second route for conduction that "
                  "non-metals do not. Alongside the particle-to-particle "
                  "wobble, metals contain electrons that are free to move "
                  "through the whole structure, and they carry energy across "
                  "the material far faster than vibration alone. That is why "
                  "metals conduct roughly a thousand times better than wood, "
                  "why they are used for saucepans and heat sinks, and why "
                  "they feel cold — one property, doing every job on that "
                  "list.",
              ]},
             {"quote": "In conduction the hot particles travel along the bar "
                       "to the cold end.",
              "body": [
                  "They do not go anywhere. Each particle vibrates about a "
                  "fixed position and hands energy on to the next by "
                  "colliding with it — the energy travels, the matter does "
                  "not. That is exactly what makes conduction different from "
                  "convection, where the heated material really does move "
                  "and carry its energy with it. A steel bar does not get "
                  "shorter at the hot end.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "In conduction, what moves through the material?",
            # MRB-278: correct at index 2.
            # MRB-177: 6w against 5w — gap 1, ratio 1.20. Passes as drawn.
            "options": [
                "The particles themselves, travelling along",
                "Heat, as a substance",
                "Energy, passed from particle to particle",
                "Cold, in the opposite direction",
            ],
            "answer": 2,
            "feedback": {
                0: "That is convection, and it needs a liquid or gas. In a "
                   "solid the particles stay put.",
                1: "There is no substance called heat — that was the caloric "
                   "theory, and a cannon disproved it in 1798.",
                3: "Cold is not a thing that moves. There is only one flow, "
                   "and it is energy.",
            }},
        "apply": {
            "q": "A metal chair and a plastic chair have been in the same "
                 "classroom all night. Which is at the lower temperature?",
            # MRB-278: correct at index 0.
            "options": [
                "Neither — they are at the same temperature",
                "The metal one",
                "The plastic one, because it holds less energy",
                "It depends on the colour",
            ],
            "answer": 0,
            "feedback": {
                1: "It feels colder, which is a different thing. Both have "
                   "reached the room’s temperature — that is thermal "
                   "equilibrium.",
                2: "Both are at room temperature. Holding less total energy "
                   "is not the same as being colder.",
                3: "Colour matters for radiation, which is next lesson, and "
                   "not for two objects sitting in the dark all night.",
            }},
        "explain": {
            "q": "Explain, in terms of particles, how energy travels from "
                 "the hot end of a metal spoon to the cool end — and "
                 "explain the extra reason metals do this faster than wood.",
            "field_label": "Your explanation",
            "placeholder": "At the hot end the particles…",
            "success": [
                "Says particles at the hot end vibrate more.",
                "Says they collide with neighbouring particles and pass "
                "energy on.",
                "Says the particles themselves do not travel along the "
                "spoon.",
                "Says metals also contain free electrons that move through "
                "the structure.",
                "Says those electrons carry energy much faster than "
                "vibration alone, giving metals two routes instead of one.",
            ]},
        "produce": {
            "q": "A tiled bathroom floor and a carpeted bedroom floor are "
                 "both at 18 °C. Barefoot, the tiles feel unpleasantly cold "
                 "and the carpet does not. Explain, and then explain why "
                 "standing on a metal bench in a hot sauna is dangerous when "
                 "the air at the same temperature is not.",
            "field_label": "Your answer",
            "placeholder": "Your skin does not measure temperature…",
            "success": [
                "Says skin detects the rate energy leaves it, not "
                "temperature.",
                "Says tiles conduct well and so remove energy from the foot "
                "quickly.",
                "Says carpet traps air and conducts badly, so removes energy "
                "slowly.",
                "Says in the sauna the flow reverses — energy travels into "
                "you.",
                "Says metal delivers that energy fast enough to burn, while "
                "air at the same temperature delivers it slowly.",
            ]},
    },

    "key_note": "Conduction passes energy from particle to particle without "
                "the particles going anywhere. Metals have a second route — "
                "free electrons — which is why they conduct far faster and "
                "why they feel cold to touch at room temperature.",

    "stretch": [
        {"type": "explainer", "id": "why-a-saucepan-has-two-materials",
         "text": "Look at a good saucepan and you are looking at this "
                 "lesson solved twice. The base is copper or aluminium, "
                 "chosen because it conducts fast enough to spread the "
                 "hob's energy evenly instead of leaving a hot ring where "
                 "the flame is. The handle is wood or a plastic, chosen for "
                 "exactly the opposite property — it must conduct so badly "
                 "that the energy never reaches your hand. Same object, two "
                 "materials, and the entire design decision is which end you "
                 "want the energy to arrive at. A pan made entirely of "
                 "copper would cook beautifully and be unusable."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "conduction",
         "definition": "Energy transfer through a material by particles "
                       "colliding with their neighbours. The energy travels; "
                       "the particles stay where they are."},
        {"term": "conductor",
         "definition": "A material that lets energy pass through it quickly. "
                       "Metals are the best, because they have free "
                       "electrons as well as vibration."},
        {"term": "insulator",
         "definition": "A material that lets energy through only slowly. "
                       "Most non-metals, and anything that traps air."},
        {"term": "free electrons",
         "definition": "Electrons in a metal that are not held to one atom "
                       "and can move through the whole structure, carrying "
                       "energy with them."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why metal feels colder than wood at "
                      "the same temperature?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Thermal conductivity as a measured property, and the "
                   "rate of energy transfer through a material calculated "
                   "from it.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
}
