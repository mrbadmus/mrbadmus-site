"""C1 L5 — Diffusion (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-05-diffusion.dc.html` (744 lines), and its
measured specification, `docs/ks3/c1-inventory/PAYLOAD-MAP.md` §5.

Every student-facing string is byte-identical to the approved page. The
module-scope constants (`RAIL`, `SCALE_CARDS`, `RUNGS`, `SELF_RUNGS`) were
lifted by `tools/extract_design_payload.js` rather than retyped.

── The document order is not the unit's ────────────────────────────────

c1-05 is the ONLY C1 lesson where `#s-think` sits BEFORE the dark practical
block (map §5.3). Every other lesson runs practical → think. Design's order is
kept: the misconception is confronted while the bench is still in the reader's
hand — the reveal at page line 193 argues from the crossing counters directly —
and the scale panel is the pay-off that follows, not a set-up for it.

── The rail lost a stage, and that is the fix ─────────────────────────

Design's rail has five stops and stage 4 (`s-scale`) ticks on stage 3's
predicate (`thinkChoice !== null`, page line 593). `#s-scale` is three static
cards and two paragraphs: it has no control, no commitment and nothing to
reveal, so there is nothing a student could do there that a rail stop could
record. Under MRB-208 a rail stop must require the student to do something, so
`s-scale` COMES OFF THE RAIL — this lesson's rail is four stops.

The alternative was to give the section a demand, and the page does not support
one: `scaleCards` is passed straight through to a static grid (page line 677).
Inventing a commit there would be inventing a component Design did not draw.
The section keeps its `id` and its `scroll-margin-top`, so every hash link into
it still lands; it simply is not a thing the rail claims a student finished.

── The bench's two counters, and why they never reset ─────────────────

NOTES §3 flag 8, verified in the frozen page: `crossR` / `crossL` are instance
fields cleared ONLY by `reset()` (page lines 439–440) and never when `even`
flips. That is the whole confrontation of `PART-11` — the spreading finishes
and the moving does not — and the reveal in `#s-think` argues from it in words.
The renderer, the wiring and the parity rows all treat it as load-bearing.

⚑ For Mide's science gate, from Design's NOTES and the map:
  * flag 8 — the counters keep climbing after the tank evens out. Reproduced.
  * §5.5.2 — `--ks3-alert` (amber) labels the scale cards' distances on ink.
    Amber-on-dark is established for CONTROLS since B1; this is amber for BODY
    LABELLING, which is new. Flagged in the map, unresolved, and reproduced as
    Design drew it rather than quietly recoloured.
"""

# ── Design's module-scope constants, lifted from the frozen page ─────────
# `SCALE_CARDS` is page lines 340–347 and holds nine authored strings. It is
# named here rather than inlined because it is the one payload on this page
# that is passed straight through untouched (page line 677), and a named
# constant says so.
SCALE_CARDS = [
    {"distance": "Across a cell · 0.01 mm", "time": "Under a millisecond",
     "text": "Fast enough that a cell needs no delivery system at all. Oxygen "
             "simply arrives."},
    {"distance": "Across a fingertip · 10 mm", "time": "About three hours",
     "text": "Already hopeless. This is why you have a bloodstream, and why "
             "the blood is never more than a fraction of a millimetre from "
             "any cell."},
    {"distance": "Across a room · 4 m", "time": "Minutes, in a gas",
     "text": "Gas particles move far faster and travel further between "
             "collisions, so a smell crosses a room while a dye crawls across "
             "a tank."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 165 character for character.
    "slug":        "diffusion",
    "title":       "Diffusion",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # Carried unchanged from the superseded body in
    # `ks3_data/chemistry_c1_particles.py`. `covers` is load-bearing: the build
    # validates exactly-once statutory coverage across the whole key stage, so
    # a wrong pair here fails every unit, not this one.
    "covers":      ["KS3.C.PIS.03", "KS3.P.PHYC.04"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    # ⊕ `requires` moves from `solids-liquids-and-gases` to `gas-pressure`.
    # Design draws exactly one "Before this lesson" row and it is Gas pressure
    # (page line 303), and the science agrees with the drawing: this lesson
    # opens on particles that are already moving at hundreds of metres per
    # second, which is the fact c1-04 establishes and measures.
    "requires":    ["gas-pressure"],
    "assumes":     [],
    # A bare slug is read as "a lesson in this unit" — Design's forward link
    # (page line 309), under Design's own heading.
    "references":  ["testing-the-model"],
    "connects_heading": "Next in this unit",
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Someone opens a bottle of perfume at the far end of a "
                    "sealed, still room with no draught at all. Two minutes "
                    "later you can smell it. What carried it to you?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, not Design's five — see the module docstring. `done_when` is
    # a gate field (R2); the runtime ticks from `data-stage-done`.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "The still room",
         "done_when": "committed"},
        # The tank has evened out at least once. Design reads live `even`,
        # which UNTICKS the stage when a student presses "Put the drop back" —
        # the same defect already ruled on c1-06 stage 4. A reset restarts the
        # run; it does not un-earn what the student already reached.
        {"anchor": "s-walk",   "short": "WALK",   "label": "Random walk",
         "done_when": "tank_has_evened_out"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Wanting to spread",
         "done_when": "committed"},
        {"anchor": "s-scale", "short": "SCALE", "label": "Distance and time",
         "mirrors": "s-think", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # The candle is the CONTROL, not scenery: it is what rules out the draught
    # the student is about to be offered as option A.
    "phenomenon": {
        "kind": "demo",
        "title": "No draught. No fan. No one waving.",
        "prompt": "The windows are shut, the air is dead still, and a candle "
                  "flame at the centre of the room stands perfectly upright — "
                  "so there is genuinely no air current. The perfume still "
                  "reaches you.",
        "commit": "Commit to what moved it.",
        "options": [
            "A draught too small to see",
            "The perfume particles moved there themselves, bouncing off air "
            "particles",
            "Warm air rising carried it across",
            "The particles were attracted towards the empty part of the room",
        ],
        "reveal": "Nothing carried it. Each perfume particle was already "
                  "moving — hundreds of metres per second — and it bounced "
                  "its way across the room off air particles, in a path so "
                  "tangled that covering four metres took two minutes. No "
                  "push was needed, because the movement never stopped in the "
                  "first place.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # IDs and statements carried unchanged from the superseded body; map §7.4
    # confirms coverage does not move in this rebuild. What moves is only which
    # activity elicits and confronts each one, because the activities changed.
    "misconceptions": [
        {"id": "PART-10",
         "statement": "Diffusion needs a draught, a current, or someone to "
                      "waft it — something has to push the particles along.",
         "elicited_by": "hook",
         "confronted_by": "walk-bench"},
        {"id": "PART-11",
         "statement": "Particles move in order to spread out — they 'want' to "
                      "fill the space, or they move from crowded to empty on "
                      "purpose.",
         "elicited_by": "think-spread",
         "confronted_by": "walk-bench"},
    ],

    # Carried unchanged from the superseded body. Design draws no keyword block
    # anywhere in C1 (map §0.7), so nothing here renders on the page; it is the
    # lesson's vocabulary record and the reading-age gate's exclusion list.
    "vocabulary": [
        {"term": "diffusion",
         "definition": "The spreading out of particles from where there are "
                       "many to where there are few, caused by their own "
                       "random movement.",
         "note": None},
        {"term": "concentration",
         "definition": "How many particles of a substance there are in a "
                       "given space.",
         "note": None},
        {"term": "random",
         "definition": "With no pattern and no set direction.",
         "note": "In science 'random' does not mean 'strange'. It means "
                 "genuinely unpredictable, direction by direction."},
    ],

    # Empty, and that is a statement: the lesson is carried by the bench and
    # the scale panel, and Design draws no figure slot anywhere in C1 (§0.7).
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Diffusion is the one piece of the particle model that people "
                 "find hardest to accept, because it looks purposeful. "
                 "Something spreads out and fills a space, evenly, every time "
                 "— and evenly-and-every-time is what deliberate things do. "
                 "This lesson takes the purpose out of it and leaves nothing "
                 "but random movement, which turns out to be enough."},

        # ══ #s-walk · the flagship, authored inline ═══════════════════════
        # `__init__._normalise` lifts this into `activities[]` and leaves a
        # LIGHT `check` shell behind it — the segment its own table already
        # names for this kind. That matters: Design draws the tank on cream
        # inside a card-ground frame, and painting it on ink would resolve
        # every text token in the instrument wrong.
        #
        # A drop of dye, 130 particles, and nothing else happening. Every
        # number below is Design's, read out of the frozen page's `reset()`,
        # `step()` and `draw()`; every string is Design's too.
        {"type": "random-walk-bench", "id": "walk-bench", "anchor": "s-walk",
         "targets": "PART-10",
         "eyebrow": "The random-walk bench · watch one particle, then all of "
                    "them",
         "heading": "No one is steering.",
         # The block-head readout. It is a PHASE, not a count — Design's
         # `walkProgress` is one of three words (page line 629) — so the count
         # slot is unused and the live word arrives through `{phase}`. The
         # renderer refuses to build if this opening word and `progress.idle`
         # below ever drift apart.
         "head_counter": {"format": "{phase}", "total": 0,
                          "start_extra": {"phase": "not started"}},
         "prompt": "A drop of dye released on the left of a sealed tank of "
                   "still water. Every particle takes a step in a random "
                   "direction, over and over. Nothing else is happening.",

         # C6's commit gate: answered, it is GONE and the bench arrives in the
         # space the question was occupying. Option B is the answer the rest of
         # the lesson is about, and it is offered before anything is watched.
         "gate": {
             "prompt": "Commit first. Once the dye has spread out completely "
                       "and the tank looks even, what are the particles doing?",
             "options": [
                 "Nothing — they have stopped where they are",
                 "Still moving randomly, equal numbers crossing each way",
                 "Slowly sinking to the bottom",
                 "Moving, but only away from where they started",
             ]},

         # ── the physics, all of it Design's ──
         "particles": 130,
         # Seeded in the left strip, as a drop rather than a wash.
         "seed": {"x": [0.04, 0.17], "y": [0.18, 0.82]},
         # Step length per tick. Warm is exactly double cool, and the vertical
         # step is 1.5× the horizontal so the drop opens out rather than
         # crawling along one line.
         "step": {"cool": 0.0055, "warm": 0.011, "y_scale": 1.5},
         # Reflecting walls — a sealed tank. A particle that would leave is put
         # back the distance it overshot, which conserves the step length.
         "bounds": {"x": [0.015, 0.985], "y": [0.03, 0.97]},
         # "Even" is a tolerance, not an equality: within 9% of half the
         # particles on each side. `hz` is the sampling rate, and the rate the
         # two counters repaint at — see the wiring for why it is deliberate.
         "even": {"tolerance": 0.09, "hz": 3},
         "trail_max": 900,
         "bins": 18,
         # Reduced motion SCALES the walk, it does not stop it (R4/R6): the
         # counters still climb and the tank still evens out, more slowly.
         "reduced_scale": 0.4,

         "labels": {
             "cross_right": "Crossings left to right",
             "cross_left":  "Crossings right to left",
             "even":        "Spread out?",
             "even_yes":    "Yes",
             "even_no":     "Not yet",
             "run_start":    "Start the run",
             "run_pause":    "Pause",
             "run_continue": "Continue",
             "reset":        "Put the drop back",
             "trace_on":     "Follow one particle",
             "trace_off":    "Stop following one particle",
             "warm_on":      "Warm the water",
             "warm_off":     "Cool the water",
         },
         # The two readouts that are DRAWN, above and below the tank. They
         # reach a screen reader only through the canvas `alt` below.
         "canvas_labels": {
             "left_half":  "LEFT HALF: ",
             "right_half": "RIGHT HALF: ",
             "profile":    "HOW CROWDED, ALONG THE TANK",
         },

         # Four authored branches, in the order the renderer emits them. All
         # four are in the document at once and one is shown, so no science
         # sentence is ever rebuilt from an attribute.
         "notes": {
             "idle": "The drop is sitting on the left. Nothing is pushing it, "
                     "nothing is stirring, and there is no current in the "
                     "tank. Press start and watch what randomness alone does.",
             "spreading": "Early on, more particles cross left-to-right "
                          "than right-to-left — not because they know where "
                          "to go, but because there are more of them on the "
                          "left available to make the crossing. Watch the "
                          "GAP between the two counters rather than their "
                          "size: a single particle near the middle crosses "
                          "the line again and again, so both totals run "
                          "away. The gap is the net movement, and it is the "
                          "whole of diffusion.",
             "even": "Evened out — and look at the two crossing counters. They "
                     "are still climbing, at the same rate as each other. "
                     "Particles are pouring across the middle in both "
                     "directions, in equal numbers, forever. Nothing has "
                     "stopped; the two flows have simply balanced.",
             "tracing": "The single traced particle is not going anywhere in "
                        "particular. Its path doubles back on itself "
                        "constantly — and the tangle is exactly why crossing a "
                        "few centimetres takes so long when the particle "
                        "itself is fast.",
         },
         "progress": {"idle": "not started", "spreading": "spreading",
                      "even": "evened out"},

         # The canvas is the whole instrument, so its label is the whole
         # readout. `{left}` and `{right}` are an ADDITION: the half counts are
         # drawn inside the canvas and reach a screen reader nowhere else,
         # which is the same defect the c1-04 ruling corrects.
         "alt": {
             "template": "A tank of water with dye particles {state}, and a "
                         "bar chart underneath showing how crowded each part "
                         "of the tank is. {left} particles in the left half, "
                         "{right} in the right.",
             "even":   "spread evenly throughout",
             "uneven": "concentrated towards the left",
         }},

        {"type": "key-fact", "ref": "spreading"},

        # #s-think BEFORE the dark block — this lesson only. The reveal argues
        # from the bench's counters, so it has to follow the bench and precede
        # nothing in particular.
        {"type": "misconception", "id": "think-spread", "anchor": "s-think",
         "targets": "PART-11"},

        # ══ #s-scale · a static three-up panel, authored inline ════════════
        # Lifted into a dark `practical` shell. Static, and NOT `reveal-cards`:
        # there is nothing to reveal and nothing to commit, so R4's declaration
        # ask (verify_ks3.py §5.1.2(a)) would fire on a block that asks for
        # nothing. Not a rail stop either — see the module docstring.
        {"type": "scale-cards", "id": "scale-panel", "anchor": "s-scale",
         "eyebrow": "Where this does real work",
         "heading": "Two minutes across a room, a fraction of a second across "
                    "a cell",
         "prompt": "Diffusion is hopeless over long distances and unbeatable "
                   "over short ones, and that single fact shapes a great deal "
                   "of biology.",
         "scale_cards": SCALE_CARDS,
         "close": "Double the distance and diffusion takes four times as long, "
                  "not twice. That is why every cell in your body is "
                  "microscopic, why lungs are folded into millions of tiny "
                  "sacs instead of two smooth bags, and why anything larger "
                  "than an insect needs a heart."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # R3: `ground: "card"` and no chasing the page's 6px/25px numbers — one
    # stylesheet serves 183 lesson slots.
    "key_facts": [
        {"id": "spreading",
         "text": "Diffusion is the spreading out of particles from where they "
                 "are crowded to where they are not, caused by their own "
                 "random movement. Nothing pushes them and nothing stops when "
                 "it is finished.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # ══ #s-think · the confrontation, which DOES tick (ruling R1) ══════
        # `predict`, not `confrontation`: it asks for a commitment, so it is a
        # rail stop and the generic Law 4 wiring gates the reveal behind it.
        {"id": "think-spread",
         "kind": "predict",
         "targets": "PART-11",
         # Design's quote, not the register's. An authored statement wins.
         "statements": [
             "The particles spread out because they want to fill the space "
             "evenly."],
         "prompt": "Every word of that sentence is doing damage, and it is the "
                   "sentence almost everyone writes. Commit to what is wrong "
                   "with it.",
         "options": [
             "Nothing — that is a fair description",
             "Particles cannot want anything; the evenness is what random "
             "movement produces",
             "They spread because they repel each other",
             "Only gases do this, not liquids",
         ],
         "reveal": [
             "A particle has no goal, no information about the rest of the "
             "tank, and no way to prefer one direction over another. It cannot "
             "want anything. The evenness is not aimed at — it is what "
             "randomness produces when you start with a crowd on one side.",
             "The counters on the bench are the proof. At the start, far more "
             "particles cross left-to-right than right-to-left — not because "
             "they are heading that way, but because there are more of them on "
             "the left to make the crossing. Once the two sides are even, the "
             "two counts climb at the same rate and keep climbing. The "
             "spreading has finished; the moving has not. If the particles "
             "were trying to fill the space, they would stop when the job was "
             "done.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's four rung titles are byte-identical to the engine's defaults
    # after MRB-228's relabel, so none is overridden here.
    "ladder": {
        "recall": {
            "q": "Diffusion is the movement of particles from where they are…",
            "options": [
                "More crowded to where they are less crowded",
                "Colder to where they are warmer",
                "Lower to where they are higher",
                "Heavier to where they are lighter",
            ],
            "answer": 0,
            "feedback": {
                1: "Temperature changes how fast diffusion happens, but the "
                   "direction is set by crowding.",
                2: "Diffusion works in every direction, including downwards.",
                3: "Mass affects speed, not the direction of the spread.",
            }},
        "apply": {
            "q": "A tank of dye has completely evened out. What is happening "
                 "to the particles now?",
            "options": [
                "They are still moving randomly, with equal numbers crossing "
                "each way",
                "They have stopped, because the job is done",
                "They slow down and settle to the bottom",
                "They keep moving but only sideways now",
            ],
            "answer": 0,
            "feedback": {
                1: "Nothing tells a particle the job is done. Movement does "
                   "not switch off.",
                2: "Settling is what happens to particles too big to be "
                   "jostled — sand, not dye.",
                3: "There is no mechanism that could restrict them to one "
                   "direction.",
            }},
        "explain": {
            "q": "Explain how the smell of perfume crosses a completely still "
                 "room, and why it takes minutes rather than seconds even "
                 "though the particles travel at hundreds of metres per "
                 "second.",
            "field_label": "Your explanation",
            "placeholder": "The perfume particles are already moving…",
            "success": [
                "Says the perfume particles are moving randomly on their own.",
                "Says no draught, push or carrier is needed.",
                "Says they collide constantly with air particles.",
                "Says each collision sends them off in a new direction, so the "
                "path is not straight.",
                "Says the actual distance travelled is enormous compared with "
                "the straight-line distance across the room.",
            ]},
        "produce": {
            "q": "A drop of food colouring is put into a glass of cold water "
                 "and an identical drop into a glass of hot water. The hot one "
                 "spreads much faster. Explain why — and explain why the cold "
                 "one still spreads completely if you wait.",
            "field_label": "Your answer",
            "placeholder": "In the hot water the particles…",
            "success": [
                "Says particles in hot water have more energy and move faster.",
                "Says faster movement means the colouring is jostled further "
                "in a given time.",
                "Says the direction of movement is random in both glasses.",
                "Says the cold glass spreads by exactly the same mechanism, "
                "only more slowly.",
                "Says neither needs stirring — stirring is a different process "
                "that moves whole regions of liquid at once.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Random movement, no pushing, no purpose. Particles go from "
                "crowded to less crowded because there are more of them to "
                "leave the crowded side. Warmer means faster. The movement "
                "never stops, even when the spreading looks finished.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: history of science lives in GOING FURTHER, and this is exactly
    # that — Brown's puzzle, Einstein's prediction, Perrin's measurement, and
    # the moment atoms stopped being arguable. Lifted unchanged from page 295.
    "stretch": [
        {"type": "explainer", "id": "brown-einstein-perrin",
         "text": "In 1827 the botanist Robert Brown watched pollen grains in "
                 "water through a microscope and found them jittering about, "
                 "endlessly, with nothing touching them. He could not explain "
                 "it and nor could anyone else for nearly eighty years. Then "
                 "in 1905 Einstein worked out that the jitter was exactly what "
                 "you would see if the water were made of invisible particles "
                 "battering the grain from every side, slightly unevenly, "
                 "millions of times a second — and he predicted precisely how "
                 "far a grain should wander in a given time. When Jean Perrin "
                 "measured it and the numbers matched, the last serious "
                 "scientific doubt that atoms exist was gone. A dancing speck "
                 "of pollen settled it."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still feels like something must be pushing them?",
              "cta": "Ask about this lesson",
              "anchor": "s-walk"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
