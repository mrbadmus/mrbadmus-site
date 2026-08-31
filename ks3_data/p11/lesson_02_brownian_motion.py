"""P11 L2 — Brownian motion (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p11/p11-02-brownian-motion.dc.html`.

Her page wins outright. The smoke cell, the four suspensions, the three
bars and all four rungs are hers, ported from her JavaScript constants
rather than from her HTML.

── ⚖️ RULED · HER SPEEDS STAND; THE WORD "ROOT-MEAN-SQUARE" DOES NOT ──

500 m/s for air and 590 m/s for water at 20 °C are both real figures and
both are kept. Her legal line calls BOTH root-mean-square, and that is
true of the air figure only: 590 m/s is the MEAN speed of a water
molecule and its root-mean-square speed is about 640. The instrument is
the measurement and the prose is what changes (5A.1), so the line now
reads *typical molecular speeds*. Registered.

⚠️ **"FASTER THAN A RIFLE BULLET" IS FALSE AT EVERY REACHABLE STATE.**
Her note says it; her own bench reads 483 m/s at the cold end and 647 m/s
at the hot end, and a rifle bullet leaves the muzzle at 800–1000 m/s. The
comparison is changed to a handgun bullet, which is 340–400 m/s and is
therefore true across the whole slider — same image, same job, and the
figure a student can check is the one the bench prints. Registered.

── ⚖️ THE JIGGLE IS THE ONLY BAR YOU COULD WATCH ─────────────────────

Design marks it, and marks it with `var(--ks3-alert)`. That is a CATEGORY
use of amber, which MRB-252 sends to `--ks3-data` — whose value is the
same `#8FB7FF` as the two bars beside it, so the token alone would erase
the mark. It takes the data token AND the structural focus ring; see the
long note in `ks3_art/p11.py`.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP ──────────────────────────────

Design's `DONE` reads `s.answers.r1 !== null || s.hookChoice !== null` —
the hook, or ladder rung 1. The section takes P11's `matter-think` shell
so it declares `data-stage-done="0"` in the shipped bytes, and
`wireMatterThink` watches exactly those two things. See the package note
for why `mirrors` and `band_anchor` are both wrong here.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0. **Her
option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices **0 and 2** — rung 1 stays where she drew it,
because a unit that moved every rung would be balancing the corpus by
reflex rather than by measurement.

── ⚠️ MRB-177 · TWO DISTRACTORS FINISHED, ON HER SETS ────────────────

Both marked rungs are length tells (24w against 12w; 31w against 11w).
Remedied at the DISTRACTOR in both cases, never at the correct answer and
never at the index, and in both cases her own correction already answers
the finished sentence. Registered in `DEPARTURES-P11.md`.

── ⚠️ NO CHILDLINE BLOCK. NO DRAFT MARKINGS. ─────────────────────────
"""

LESSON = {
    "slug": "brownian-motion",
    "title": "Brownian motion",
    "discipline": "physics",
    "unit": "Matter and the particle model",
    "family": "MODEL",

    "covers": ["KS3.P.PHYC.03"],
    "touches": ["KS3.WS.ATT.02"],
    "beyond_statutory": False,
    "threads": [{"id": "particles", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["density"],
    "assumes": [],
    "references": [{"unit": "C1", "lesson": "diffusion",
                    "why": "The same random molecular motion, followed over "
                           "a room rather than under a microscope."},
                   {"unit": "C1", "lesson": "solids-liquids-and-gases",
                    "why": "Where the constant motion of the particles in a "
                           "fluid is established."},
                   {"unit": "P1", "lesson": "heating-and-thermal-equilibrium",
                    "why": "Why warming the cell speeds every molecule up."}],
    "ks4_links": [],

    "meta_description": "Some specks in a drop of water refuse to settle. "
                        "Explaining that jiggle is how the world was talked "
                        "into believing in atoms.",

    "big_question": "Some specks in a drop of water refuse to settle. They "
                    "jiggle, hour after hour, with nothing touching them and "
                    "nothing alive inside them. Explaining that jiggle is how "
                    "the world was talked into believing in atoms.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Specks that will not settle", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "The smoke cell",  "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` for this stop is `s.answers.r1 !== null ||
        # s.hookChoice !== null` — a PAGE-LEVEL predicate, not a sibling of
        # the bench. `matter-think` + `wireMatterThink` is what expresses it;
        # `mirrors` would fail `check_rail_matches_design` outright.
        {"anchor": "s-think",  "short": "THINK",
         "label": "What is pushing them", "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",  "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The specks have been jiggling for an hour and they will not "
                 "stop.",
        "prompt": "A sealed cell of still air with a wisp of smoke in it, lit "
                  "from the side and viewed under a microscope. The bright "
                  "specks never settle. They jerk a short way, stop, jerk "
                  "somewhere else — never in the same direction twice, and "
                  "never coming to rest.",
        "commit": "What is moving them?",
        "options": [
            "Tiny air currents are blowing them about",
            "Something alive inside them is swimming",
            "Invisible particles are hitting them from every side",
            "The microscope lamp is heating one side of each speck",
        ],
        "answer": 2,
        "reveal": "Invisible particles, hitting them from every side. At any "
                  "instant a smoke speck is being struck by billions of air "
                  "molecules; the strikes very nearly cancel, and the small "
                  "leftover imbalance shoves it a short way in a random "
                  "direction. A moment later the imbalance points somewhere "
                  "else. Nothing is alive, nothing is blowing and nothing has "
                  "a plan — the jiggle is direct visible evidence that air is "
                  "made of separate moving particles.",
    },

    "misconceptions": [
        {"id": "PART-17",
         "statement": "The smoke specks are moving under their own power.",
         "elicited_by": "s-hook",
         "confronted_by": "think-nothing-is-swimming"},
        {"id": "PART-18",
         "statement": "You are watching the air molecules hit the specks.",
         "elicited_by": "s-ladder",
         "confronted_by": "think-nothing-is-swimming"},
        {"id": "PART-19",
         "statement": "Tiny air currents are blowing the specks about — "
                      "something has to be moving the air for them to move.",
         "elicited_by": "s-hook",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Brownian motion</strong> is the constant random "
                 "jiggling of small specks suspended in a fluid. It happens "
                 "in air and in liquids, it never stops, and it has nothing "
                 "to do with currents, with life or with the observer."},
        {"type": "explainer",
         "text": "The explanation is entirely about size. A fluid is made of "
                 "molecules in constant motion, and a suspended speck is "
                 "being struck by enormous numbers of them at once — from the "
                 "left, the right, above and below, all at the same instant. "
                 "Those strikes almost cancel. What is left over is a small "
                 "unbalanced push in a direction that nobody chose, and a "
                 "moment later the leftover points somewhere else."},
        {"type": "explainer",
         "text": "This is why the speck has to be the right size. Something "
                 "as small as a molecule would be knocked clean across the "
                 "cell; something as large as a grain of sand is struck so "
                 "evenly that the imbalance is nothing against its weight. A "
                 "smoke speck sits in the narrow band where the imbalance is "
                 "big enough to shift it and the speck is big enough to see."},

        # ── #s-bench · a smoke cell under a microscope ─────────────────
        {"type": "matter-bench",
         "id": "bench",
         "anchor": "s-bench",
         "model": "brownian",
         "eyebrow": "At the bench · a smoke cell under a microscope",
         "heading": "You can see the specks. You cannot see what is hitting "
                    "them.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Choose what is under the microscope and how warm it is. "
                 "Only the second bar is anything you could actually watch — "
                 "the other two are what the model says is going on "
                 "underneath.",
         "gate": {
             "prompt": "Commit first. You warm the cell from 20 °C to 80 °C. "
                       "What happens to the jiggling?",
             "options": [
                 "Nothing — temperature has no effect on it",
                 "It slows down, because warm air is thinner",
                 "It gets faster and wilder, because the molecules are moving "
                 "faster",
                 "It stops, because the smoke evaporates",
             ],
             "answer": 2,
         },
         "tabs_label": "What is under the microscope",
         "start_tab": 0,
         "tabs": [
             {"id": "smoke",  "label": "Smoke in air",
              "name": "smoke in air", "speck": "a smoke speck",
              "hidden": "air molecules", "v_mol": "500", "ratio": "5000"},
             {"id": "pollen", "label": "Pollen in water",
              "name": "pollen in water", "speck": "a pollen grain",
              "hidden": "water molecules", "v_mol": "590", "ratio": "100000"},
             {"id": "dust",   "label": "Dust in a sunbeam",
              "name": "dust in a sunbeam", "speck": "a dust grain",
              "hidden": "air molecules", "v_mol": "500", "ratio": "50000"},
             {"id": "milk",   "label": "Fat droplets in milk",
              "name": "fat droplets in milk", "speck": "a fat droplet",
              "hidden": "water molecules", "v_mol": "590", "ratio": "3000"},
         ],
         "slider": {"label": "Temperature of the cell",
                    "values": [0, 20, 40, 60, 80],
                    "start": 1,
                    "value_label": "{v} °C"},
         "bars_caption": "Three quantities, one of them visible",
         "bars_alt": "Three bars: molecule speed about {vmol} metres per "
                     "second, visible jiggle {jig} micrometres per second, "
                     "and the speck about {ratio} times wider than a "
                     "molecule.",
         "bars": [
             {"id": "speed",
              "label": "Speed of the {hidden}",
              "value": "{vmol} m/s",
              "sub": "far too small and far too fast to see"},
             # ⚠️ THE ONLY AUTHORED `focus` IN THE UNIT. On the other three
             # benches the focus follows the control; here it is a fixed
             # CATEGORY claim — this is the one quantity a microscope could
             # actually show — and it is true whatever is selected.
             {"id": "jiggle",
              "label": "Jiggle of {speck}",
              "value": "{jig} µm each second",
              "sub": "this is the only part you can watch",
              "focus": True},
             {"id": "size",
              "label": "{Speck} against one molecule",
              "value": "{ratio} × wider",
              "sub": "which is why the strikes almost cancel"},
         ],
         "readouts": [
             {"id": "seen", "label": "What you can see",
              "value": "{speck_bare}", "sub": "jiggling on a random path"},
             {"id": "unseen", "label": "What you cannot see",
              "value": "{hidden}", "sub": "about {vmol} m/s at {v} °C"},
             {"id": "temp", "label": "Temperature",
              "value": "{v} °C", "sub": "sets how fast they move"},
             {"id": "strikes", "label": "Strikes each second",
              "value": "billions", "sub": "nearly, but never exactly, "
                                          "balanced"},
         ],
         "words": {},
         "notes": {
             # ⚠️ ONE BRANCH, BECAUSE THE MODEL HAS ONE. Nothing on this
             # bench changes in KIND — every suspension at every temperature
             # tells the same story with different numbers — so a second
             # branch would be authored copy no student could reach.
             "always": "At {v} °C the {hidden} are moving at roughly {vmol} "
                       "m/s — faster than a bullet from a handgun, in every "
                       "direction at once. {Speck} is about {ratio} times "
                       "wider than one of them, so it is struck from all "
                       "sides at once and almost all of those pushes cancel. "
                       "Almost. The tiny leftover is what you see, and it "
                       "changes direction constantly because the imbalance is "
                       "random. Warm the cell and every molecule speeds up, "
                       "so the leftover gets bigger and the path gets wilder "
                       "— which is exactly what the microscope shows.",
         }},

        {"type": "key-fact", "ref": "brownian-is-evidence"},

        {"type": "misconception", "id": "think-nothing-is-swimming",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        # ⚠️ `matter-think`, NOT `predict`. `#s-think` is a RAIL STOP on this
        # page, so the section has to declare `data-stage-done="0"` in the
        # shipped bytes. The drawer renders nothing — `r_activity` has
        # already emitted both quotes and both bodies from the BLOCK TYPE.
        # See `ks3_art/p11.py`.
        {"id": "think-nothing-is-swimming",
         "kind": "matter-think",
         "demand": "explain",
         "targets": "PART-17",
         "ticks_when": "The hook is committed, or ladder rung 1 is answered "
                       "— Design's own predicate for this stop, and neither "
                       "control is inside this section.",
         "statements": [
             {"quote": "The smoke specks are moving under their own power.",
              "targets": "PART-17",
              "body": [
                  "They have no power. A smoke speck is a fragment of burnt "
                  "material with no store of energy it can use and no "
                  "mechanism to use one; it moves only because it is pushed. "
                  "Brown himself worried about exactly this, and settled it "
                  "by finding the same jiggling in dust from a piece of "
                  "window glass and in a fragment of the Sphinx — neither of "
                  "which had ever been alive.",
              ]},
             {"quote": "You are watching the air molecules hit the specks.",
              "targets": "PART-18",
              "body": [
                  "You are watching one side of the collision only. A "
                  "molecule is a few tenths of a nanometre across, thousands "
                  "of times below what any light microscope can resolve, and "
                  "no lens will ever show one. What the microscope shows is "
                  "the effect: a speck you can see, moving in a way that only "
                  "makes sense if something you cannot see is hitting it. "
                  "That is the whole force of the argument, and it is why the "
                  "experiment mattered so much.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "brownian-is-evidence",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Brownian motion is the random jiggling of a visible speck "
                 "caused by unbalanced strikes from the invisible molecules "
                 "of the fluid around it. It never stops, it gets more "
                 "violent as the temperature rises, and it is direct evidence "
                 "that fluids are made of separate moving particles."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 2.
    # Rung 1 stays where Design drew it; rung 2 moves. Every option's TEXT
    # and every correction is hers.
    "ladder": {
        "recall": {
            "q": "A student watches smoke specks jiggling and says the specks "
                 "are being pushed by other smoke specks. What is wrong with "
                 "that?",
            "options": [
                "The pushes come from air molecules, which are far smaller "
                "and far more numerous than the smoke specks and cannot be "
                "seen at all.",
                "Nothing is wrong — smoke specks are the only particles "
                "present.",
                "The specks are pushed by light from the microscope lamp.",
                # ⚠️ MRB-177 — Design's distractor, FINISHED. Her correct
                # option is 24 words against a longest distractor of 12.
                # Remedied at the distractor; the added clause completes the
                # wrong rule rather than padding it, and her own correction
                # already answers it.
                "The specks push each other, but only when the cell is warm, "
                "because warming them is what gives them enough energy to "
                "shove their neighbours.",
            ],
            "answer": 0,
            "feedback": {
                1: "The cell is full of air, and air is molecules. The smoke "
                   "is only there to give you something big enough to see.",
                2: "Light does exert a tiny push, far too small to matter "
                   "here — and the jiggling continues when the lamp is "
                   "dimmed.",
                3: "The jiggling happens at every temperature, and it happens "
                   "when the specks are far apart from one another.",
            },
            "title": "Rung 1 · Read the model"},
        "apply": {
            "q": "Why do we watch smoke specks rather than watching the air "
                 "molecules themselves?",
            "options": [
                "Air molecules move too slowly to notice.",
                "Air molecules are transparent and smoke specks are not.",
                "A molecule is thousands of times too small to see in any "
                "light microscope. The speck is big enough to see and small "
                "enough to be shifted by unbalanced molecular strikes.",
                # ⚠️ MRB-177 — finished, for the same reason. 31w against
                # 11w before; her own correction answers this sentence.
                "There are not enough air molecules in the cell to see, "
                "because a sealed cell that small only holds a few hundred of "
                "them at any one moment.",
            ],
            "answer": 2,
            "feedback": {
                0: "They move at hundreds of metres per second. Speed is not "
                   "the problem; size is.",
                1: "Being transparent is not the issue — a molecule is far "
                   "below the size any optical microscope can resolve, "
                   "whatever it is made of.",
                3: "There are around 10^25 of them in a cubic metre. There "
                   "are far too many to count and each is far too small to "
                   "see.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Describe what you would see through the microscope in a "
                 "smoke cell, and explain the movement in terms of particles.",
            "field_label": "Your explanation",
            "placeholder": "The bright specks appear to…",
            "success": [
                "Says the visible specks are smoke, lit up against a dark "
                "background.",
                "Describes the movement as random, jerky and in no fixed "
                "direction.",
                "Says the specks are being hit by air molecules that are far "
                "too small to see.",
                "Says the strikes come from all directions and very nearly "
                "cancel out.",
                "Says the movement you see is the small leftover imbalance, "
                "which keeps changing direction.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Robert Brown first saw this in 1827 with pollen in water "
                 "and could not explain it; Einstein explained it in 1905 and "
                 "it was taken as proof that atoms are real. Explain why a "
                 "jiggling speck counts as evidence for atoms.",
            "field_label": "Your answer",
            "placeholder": "If water were a smooth continuous fluid, then…",
            "success": [
                "Says that if water were smooth and continuous, the pushes on "
                "a grain would be even and it would not move.",
                "Says the jiggling means the water must be made of separate "
                "lumps arriving one at a time.",
                "Says the lumps must be small enough that their strikes "
                "nearly cancel, and numerous enough that they arrive "
                "constantly.",
                "Notes that the effect is visible without ever seeing an "
                "atom.",
                "Says a prediction that matched measurement — the size of the "
                "jiggle — is what turned a plausible model into accepted "
                "evidence.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Brownian motion is the random jiggling of small visible "
                "specks suspended in a fluid, caused by unbalanced collisions "
                "from the fluid’s own molecules. The strikes come from every "
                "direction and nearly cancel; the tiny leftover imbalance "
                "moves the speck, and changes direction constantly. Warming "
                "the fluid speeds the molecules up and makes the jiggling "
                "wilder. Nothing alive and no current is involved, and the "
                "molecules themselves are never seen — only their effect.",

    "stretch": [
        {"id": "einstein-and-perrin",
         "type": "explainer",
         "text": "Einstein’s 1905 paper did not simply say that molecules "
                 "were doing it. It predicted how far a speck of a given size "
                 "should wander in a given time, at a given temperature, in a "
                 "fluid of a given thickness — a number that could be "
                 "measured. Jean Perrin spent four years measuring it, found "
                 "the prediction held, and used it to work out how many "
                 "molecules there are in a mole. Both men have Nobel prizes "
                 "partly for this, and the atomic hypothesis stopped being a "
                 "hypothesis."},
        {"id": "the-random-walk",
         "type": "explainer",
         "text": "The same mathematics turns up wherever something takes a "
                 "large number of small random steps. It is used to model how "
                 "a pollutant spreads through groundwater, how a share price "
                 "wanders, and how proteins find their way about inside a "
                 "cell. The name for the general case is a random walk, and "
                 "the smoke cell is the cheapest place to see one."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Brownian motion",
         "definition": "The constant random jiggling of small specks "
                       "suspended in a fluid, caused by unbalanced strikes "
                       "from the fluid's own molecules. It never stops."},
        {"term": "fluid",
         "definition": "A liquid or a gas — anything whose particles are free "
                       "to move past one another. Brownian motion happens in "
                       "both."},
        {"term": "molecule",
         "definition": "A particle made of atoms joined together. The "
                       "molecules of air and water are a few tenths of a "
                       "nanometre across, far below what any light microscope "
                       "can show."},
        {"term": "random walk",
         "definition": "A path built out of a large number of small steps, "
                       "each in a direction nothing chose. A jiggling speck "
                       "is following one."},
    ],

    "tutor": {
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure why a speck you can see proves something you "
                "cannot?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The kinetic theory of gases, diffusion rates and Graham’s "
                   "law, and Brownian motion as evidence for the particle "
                   "model.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Teacher demonstration. The smoke cell uses a lit taper "
                   "and a small glass cell — watch, don't handle.",

    "convention_note": "The bench is a teaching model. Typical molecular "
                       "speeds are quoted for the gas or liquid named, scaled "
                       "with the square root of absolute temperature from "
                       "about 500 m/s for air and about 590 m/s for water at "
                       "20 °C; real distributions are broad and no molecule "
                       "holds one speed for long. The jiggle figure is an "
                       "illustrative displacement rate, not a measurement, "
                       "and is scaled with the same square root. Size ratios "
                       "are order-of-magnitude comparisons between a typical "
                       "speck and a typical molecule.",

    "ws": ["scientific-attitudes", "analysis-and-evaluation"],
}
