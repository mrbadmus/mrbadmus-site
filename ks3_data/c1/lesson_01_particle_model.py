"""C1 L1 — The particle model (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-01-particle-model.dc.html` (842 lines), and its
measured specification, `docs/ks3/c1-inventory/PAYLOAD-MAP.md` §1.

Every student-facing string is byte-identical to the approved page. The
module-scope constants (`RAIL`, `FLOOR`, `GAP_TESTS`, `RUNGS`, `SELF_RUNGS`)
were taken from the machine lift, `scratchpad/payloads/c1/c1-01-particle-model.json`;
the strings that live inside `renderVals()` — the four `cutNote` branches, the
two `gapNote` fallbacks, the three option sets, the two computed aria-labels —
were lifted from the line ranges the payload map records, because a lift of the
top-level constants alone loses them silently.

── Two instruments, both new ────────────────────────────────────────────

`halving-bench` (`#s-cut`) and `gap-test-rig` (`#s-gap`). Neither is in
`ACTIVITY_KIND_RENDERERS`, and the `sim` path is closed to both: `r_sim`
refuses any control not in `SIM_CONTROLS`, and `cut`, `undo`, `cut-ten` and the
three gap tests are none of those (map §1.6 e).

The shells are MEASURED, not guessed. `#s-cut` is a light `ks3-block` → `check`;
`#s-gap` is `ks3-block ks3-dark ks3-practical` → `practical`. `ks3_data/c1/__init__.py`
carries the same table and lifts these inline blocks into `activities[]`.

── FLOOR = 24 is load-bearing ───────────────────────────────────────────

It is not a dial. 1 cm / 2²⁴ = 0.596 nm, which the size ladder formats as
`0.6 nm` — about the width of a sucrose molecule — and Rung 2's stem says
"twenty-four times" in words. Change the constant and the ladder question stops
being true. It is authored ONCE here and read by the head counter, by the
instrument, by the canvas's end label and by nothing else.

── `#s-think` asks for a commitment, so it ticks (ruling R1) ────────────

`build_ks3.py`'s own comment above `ACTIVITY_KIND_RENDERERS` says `#s-think` is
a rail stop on none of the six lessons "because a confrontation asks for
nothing". C1 contradicts that on all six pages: every `#s-think` carries four
options and a reveal gated behind them. Authored here as a **`predict`**, which
is a generic kind — prompt, options, reveal IS its drawn component — so it
takes no `data-stage-done` and `doneByDom()` ticks it on the commitment. The
misconception SHELL is unchanged, so the badge, the "Think again" eyebrow and
the amber ground are all still Design's.

⚑ For Mide's science gate:
  * The canvas prints `ONE PARTICLE` / `N PARTICLES LEFT` from the count across
    ONE FACE (map §1.6 science note 1). At n = 20 it draws a 16 × 16 face and
    says `256 PARTICLES LEFT`; a cube 16 particles on an edge holds 16³ = 4,096.
    The drawing is a cross-section, so the face count is defensible and Design's
    wording is kept exactly as drawn rather than silently corrected.
  * The deliberate line — you CAN cut a particle, you just do not get sugar —
    is carried twice on purpose: in `#s-think`'s reveal and in Rung 2's key.
  * The key note says "tonight", which frames the lesson as homework.
"""

# ── the cut floor (page line 359) ────────────────────────────────────────
# Authored once and referenced from both places that need it: the head
# counter's total and the instrument's own floor. Two literals here would be
# two places for the lesson's central number to drift.
FLOOR = 24

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 158 character for character.
    "slug":        "particle-model",
    "title":       "The particle model",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # Carried across unchanged from the superseded body in
    # `ks3_data/chemistry_c1_particles.py`. `KS3.C.PNM.01a` is the clause-level
    # sub-ID this lesson has always owned; coverage is exactly-once across the
    # key stage, so this is not a free choice.
    "covers":      ["KS3.C.PNM.01a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 35,

    # ── progression edges ───────────────────────────────────────────────────
    # `requires` is empty — this is where the unit starts — so `before_this`
    # speaks in the first end-matter card instead (§4.8.1 D).
    "requires":    [],
    "assumes":     [],
    "references":  ["solids-liquids-and-gases"],
    "connects_heading": "Next in this unit",
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Pour 50 ml of water into 50 ml of alcohol and you get 97 "
                    "ml. Nothing leaked, nothing evaporated. Where did the "
                    "three millilitres go?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, all five anchors emitted by this lesson. `done_when` is a GATE
    # field (ruling R2) — the runtime ticks from `data-stage-done` — so each one
    # names the real predicate the page implements, not a wish.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "50 + 50 = 97",
         "done_when": "committed"},
        # ⚖️ STICKY. The floor has to have been REACHED, once; undoing a cut
        # does not untick it, because the thing the student found out cannot be
        # un-found. Design's own `reachedFloor` is a one-way flag and this
        # reproduces it rather than tightening it to "is at the floor now".
        {"anchor": "s-cut",    "short": "CUT",    "label": "Keep cutting",
         "done_when": "floor_reached"},
        {"anchor": "s-gap",    "short": "GAP",    "label": "What is in the gap",
         "done_when": "one_test_run"},
        # R1 — a commitment, so it is a real stop rather than a decorative one.
        {"anchor": "s-think",  "short": "THINK",  "label": "A sharper knife",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "demo",
        "title": "Fifty and fifty makes ninety-seven.",
        "prompt": "Two measuring cylinders, both read to the millilitre. 50 ml "
                  "of water, 50 ml of pure alcohol. Tip one into the other, "
                  "wait for the froth to settle and read the level: 97 ml. Do "
                  "it again tomorrow and you get 97 ml again.",
        "commit": "Three millilitres of liquid are missing. Commit to a reason.",
        "options": [
            "Some of it evaporated while you were pouring",
            "The two liquids reacted and made something smaller",
            "Particles of one liquid settled into gaps between particles of "
            "the other",
            "The measuring cylinder is not accurate enough",
        ],
        "reveal": "Nothing is missing. Every drop you poured is still in the "
                  "cylinder. The only way 50 and 50 can make 97 is if liquids "
                  "are not solid stuff all the way through — if there are "
                  "gaps, and the small particles of one liquid can settle into "
                  "the gaps between the large particles of the other. That is "
                  "the whole model, arrived at by arithmetic.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # IDs carried across from the superseded body — PAYLOAD-MAP §7.4 confirms
    # the register does not move for this rebuild — and repointed at the blocks
    # that now elicit and confront each one.
    #
    # ⚠️ PART-01's `statement` is Design's own line from page 211, not the
    # superseded wording. `r_confrontation` renders the register's statement as
    # the quote whenever the activity authors none of its own, so this string IS
    # the sentence on the page and has to be the page's. It says the same thing
    # in a student's voice, which is what the register asks for anyway.
    "misconceptions": [
        {"id": "PART-01",
         "statement": "You stopped cutting because the knife was not sharp "
                      "enough. A better knife would keep going.",
         "elicited_by": "cut-bench",
         "confronted_by": "think-commit-knife"},
        # PART-02 is confronted by the gap rig itself: every test the student
        # runs with something in the gap contradicts something they already
        # know. It carries no quote on this page, so its statement is the
        # superseded body's, unchanged.
        {"id": "PART-02",
         "statement": "There is air (or dust, or something) in the gaps between "
                      "particles.",
         "elicited_by": "gap-rig",
         "confronted_by": "gap-rig"},
    ],

    # Carried from the superseded body. Design draws no keyword block on any of
    # the six C1 pages (PAYLOAD-MAP §0.7), so no block on this page names this
    # list and none of the definitions reach the lesson body. It is not dead
    # weight: the TERMS render as the unit page's "Words this unit gives you"
    # chips (build_ks3.py:7851), the reading-age gate reads them as its
    # exclusion list, and it is the lesson's term record for the day a support
    # layer is authored.
    "vocabulary": [
        {"term": "particle",
         "definition": "One of the tiny pieces that all matter is made from, far "
                       "too small to see.",
         "note": "In this unit 'particle' means atoms or molecules. You will "
                 "meet those names properly in C2."},
        {"term": "matter",
         "definition": "Anything that has mass and takes up space.",
         "note": None},
        {"term": "model",
         "definition": "A simple picture or idea that helps explain something we "
                       "cannot see directly.",
         "note": "A model does not have to be a perfect copy to be useful. "
                 "L6 asks how far this one can be pushed."},
        # ⊕ ADDED by the rebuild. The opening explainer rests the entire unit on
        # this one word — "matter is not continuous" — and the stretch layer
        # uses it again for the rival idea Democritus argued against. The
        # superseded body carried the notion inside PART-01 but never named it,
        # and the rebuilt page names it twice.
        {"term": "continuous",
         "definition": "All one piece, with no gaps and no separate bits, "
                       "however closely you look.",
         "note": "This is the idea the particle model replaces. Matter looks "
                 "continuous; it is not."},
    ],

    # Nothing on the rebuilt page references a figure: the cutting bench and the
    # gap rig draw themselves on canvas, `phenomenon` names no `art`, and Design
    # draws no figure slot anywhere in C1 (§0.7). The two the superseded body
    # commissioned — `c1-particles-three-states` and `c1-mixing-volumes` — drop
    # out of the diagram manifest with it rather than standing as sourcing tasks
    # for drawings no block would show. Present and empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Everything in this unit rests on one claim: matter is not "
                 "continuous. It is made of separate particles, far too small "
                 "to see, with nothing at all in between them, and they never "
                 "stop moving. That claim is worth nothing to you until you "
                 "have tried to break it — so the rest of this lesson is "
                 "two attempts to break it."},

        # ── #s-cut · halving-bench ──────────────────────────────────────────
        # A LIGHT block. The bench does not exist until the gate is answered:
        # gating by absence, so the instrument arrives in the space the question
        # was occupying.
        {"type": "halving-bench", "id": "cut-bench", "anchor": "s-cut",
         "eyebrow": "The cutting bench · attempt one",
         "heading": "Keep cutting it in half.",
         # The head row's live readout. `{total}` is baked at build time and
         # `{n}` moves; at the floor the instrument swaps in `progress_full`,
         # because "24 of 24 possible cuts" is not what Design says there.
         "head_counter": {"format": "{n} of {total} possible cuts",
                          "total": FLOOR},
         "progress_full": "floor reached",
         "prompt": "A sugar cube, one centimetre on each side. A knife with a "
                   "perfect edge, and no limit on your patience. Cut it in "
                   "half, throw one half away, cut what is left in half again.",

         "floor": FLOOR,
         # The edge of the starting cube, in centimetres. The size ladder is
         # 1 cm / 2ⁿ formatted mm → µm → nm, which is engine (map §1.2); the
         # length it starts from is this lesson's, and the lede says it out loud.
         "start_cm": 1,
         # How many cuts before the floor the piece stops being a smooth block
         # and resolves into countable particles. Design's threshold is
         # `n >= FLOOR - 4`, and the near-floor note says "four cuts ago" — one
         # number, authored once.
         "grain_at": 4,

         "gate": {"prompt": "Commit before you start. With a perfect knife and "
                            "forever to work, how many times could you cut?",
                  "options": [
                      "Forever — there is always a smaller half",
                      "Millions of times, then the piece is too small to see",
                      "A few dozen times, then no smaller piece of sugar exists",
                      "Until it turns into a liquid",
                  ]},

         "readouts": [
             {"label": "Cuts made", "source": "count"},
             {"label": "Edge of the piece", "source": "size"},
             {"label": "Still sugar?", "source": "verdict"},
         ],
         # Both words are in the document from the start and one is hidden, so
         # no readout is ever assembled in JS.
         "verdict": {"open": "Yes", "floor": "Floor"},

         "buttons": [
             {"label": "Cut it in half", "action": "cut", "step": 1,
              "disabled_when": "at_floor"},
             {"label": "Undo a cut", "action": "undo", "step": 1,
              "disabled_when": "at_start"},
             {"label": "Cut ten more times", "action": "cut", "step": 10,
              "disabled_when": "at_floor"},
         ],

         # Four authored branches, tested in Design's own order: the floor
         # first, then the grain, then the untouched cube, then everything else.
         "notes": {
             "at_floor": "Twenty-four cuts. Not twenty-four thousand, not "
                         "forever — twenty-four. The knife has not gone "
                         "blunt and your hand has not got tired. There is "
                         "simply no piece of sugar smaller than this one, "
                         "because this one is a single particle, and halving "
                         "matter runs out.",
             "near_floor": "The edge has stopped being smooth. What looked "
                           "like a solid block four cuts ago is a countable "
                           "number of particles, and you can see the end "
                           "coming.",
             "at_start": "A centimetre of sugar. Cut it and watch the size, "
                         "not the picture — the numbers are where this "
                         "lesson happens.",
             "mid": "Still sugar, still sweet, still white, still behaving "
                    "exactly like sugar. Halving does not seem to be getting "
                    "you anywhere. Keep going.",
         },

         # The readouts are drawn in the DOM, but the piece, the scale bar and
         # the progress ticks are on the canvas, so this label is the whole
         # drawing for a screen reader.
         "alt": {"template": "A piece of sugar after {n} halvings, {size} "
                             "across{tail}",
                 "smooth": ", still a smooth solid block.",
                 "grainy": ", now visibly made of separate round particles."},

         # Type set INTO the drawing. `{n}` is the particle count across the
         # face; `{floor}` is the last tick on the progress strip.
         "canvas_labels": {"ghost": "the piece before this cut",
                           "one": "ONE PARTICLE",
                           "many": "{n} PARTICLES LEFT",
                           "start": "CUT 0",
                           "end": "CUT {floor}"}},

        {"type": "key-fact", "ref": "nothing-between"},

        # ── #s-gap · gap-test-rig ───────────────────────────────────────────
        # INK-DARK. Pick what is in the gap, then run the test that would tell
        # the answers apart — and watch every answer but one fail.
        {"type": "gap-test-rig", "id": "gap-rig", "anchor": "s-gap",
         "eyebrow": "Attempt two · the gap",
         "heading": "What is between the particles?",
         "prompt": "Zoom into the sugar until you can see individual particles "
                   "with spaces between them. Pick what is in the space, then "
                   "run the test that would tell them apart.",

         # Not `options`: that key is the activity shell's own, and the shell
         # emits it AFTER the instrument, which would put the question below the
         # answer. The rig renders its own list, in Design's position.
         "choices": [
             "Air",
             "A gas we have not discovered yet",
             "Dust and moisture, too small to see",
             "Nothing at all",
         ],
         # ⚠️ POSITIONAL, and carried explicitly for that reason. Design's
         # discriminator is `gapChoice !== null && gapChoice !== 3` — a bare
         # index, three lines away from the list it indexes. Reordering the
         # choices there silently inverts every test on the page. Here the index
         # is authored beside the list and validated against it at build time.
         "empty_choice": 3,

         "caption": "Take the gap away and see what happens",
         # Three tests, two outcome paragraphs each. `on` is what happens when
         # the gap is genuinely empty; `off` is what happens when the student
         # has filled it — which is the failure, every time.
         "tests": [
             {"id": "squash", "label": "Squash the gas",
              "on": "With gaps: the particles are pushed closer and the gas "
                    "takes up a fifth of the space. That is why a bike pump "
                    "works.",
              "off": "Fill the gaps with air and there is nothing left to "
                     "squash — the air would need gaps of its own, and so "
                     "would that air, forever."},
             {"id": "mix", "label": "Pour the water in",
              "on": "With gaps: small particles drop into the spaces between "
                    "large ones, and 50 + 50 comes out at 97.",
              "off": "Fill the gaps with something and the volumes must simply "
                     "add. 50 and 50 would make 100, and it does not."},
             {"id": "smell", "label": "Let the smell spread",
              "on": "With gaps: a moving particle has somewhere to go, and it "
                    "works its way across the room without any draught.",
              "off": "Pack the space solid and nothing can move anywhere. A "
                     "smell would never cross a still room, and it does."},
         ],
         # Before any test has been run — one line for the answer that survives
         # and one for the answers that do not. Neither marks the student: the
         # first says the right answer is hard to accept, the second says run
         # the test rather than "wrong".
         "notes": {"empty": "Nothing is the hard answer to accept and the only "
                            "one that survives. Run a test and see why the "
                            "alternatives do not.",
                   "filled": "You have put something in the gap. Now run a "
                             "test and watch it fail."},

         "canvas_labels": {"empty": "GAPS EMPTY",
                           "filled": "GAPS FILLED IN",
                           "foot_filled": "your answer, on the right",
                           "foot_empty": "your answer says nothing is there "
                                         "— both boxes agree"},
         "alt": {"template": "Two particle boxes side by side. Left: particles "
                             "with empty space between them. Right: {right}",
                 "filled": "the same particles with the space packed solid.",
                 "empty": "the same picture, because the answer was that "
                          "nothing is there."}},

        {"type": "misconception", "id": "think-commit-knife", "anchor": "s-think",
         "targets": "PART-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⚠️ `ground: "card"` and no geometry. Design's box on all six C1 pages is
    # 28px/22px 26px/6px shadow/25px body against the shipped 24px/18px 22px/5px
    # shadow/22px — drift 5 is reopened by C1 and needs a ruling (map §1.6 c).
    # Until it has one the stylesheet wins: one stylesheet serves 183 lesson
    # slots, and chasing a page's numbers here restyles six approved lessons.
    "key_facts": [
        {"id": "nothing-between",
         "text": "All matter is made of particles, far too small to see, with "
                 "nothing between them, and they are always moving.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The two instruments are authored inline in `core` above and lifted here by
    # `ks3_data/c1/__init__.py`. This list holds the one activity that is not an
    # instrument.
    "activities": [
        # R1 — a `predict`, not a `confrontation`. It asks for a commitment and
        # gates a two-paragraph reveal behind it, so it ticks its rail stop.
        {"id": "think-commit-knife",
         "kind": "predict",
         "demand": "explain",
         "targets": "PART-01",
         "prompt": "This is the sensible objection, and it is worth taking "
                   "seriously before you answer it. Commit.",
         "options": [
             "True — a sharper knife would just keep going",
             "The knife could cut it, but what comes out is not sugar any more",
             "False — particles cannot be cut by anything",
             "The piece would be too small for the knife to touch",
         ],
         "reveal": [
             "A sharper knife would keep going. Cut a sugar particle in half "
             "and you will get something — but not sugar. You get carbon, "
             "hydrogen and oxygen, and they are not sweet, not white, and one "
             "of them is a gas. The cut is possible; what is impossible is a "
             "smaller piece <em>that is still sugar</em>.",
             "That is what the model claims, and it is a much stronger claim "
             "than \"things are small\". It says matter comes in units with a "
             "floor, and below that floor the substance stops existing. "
             "Everything you meet in this unit — melting, pressure, "
             "diffusion — is that floor doing work.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # No `title` overrides: the engine's defaults are already Design's wording
    # for all four rungs on this page — Recall / The one that catches people /
    # Explain / Take it somewhere new.
    "ladder": {
        "recall": {
            "q": "What does the particle model say is between the particles of "
                 "a gas?",
            "options": [
                "Nothing at all",
                "Air",
                "A very thin gas",
                "Dust too small to see",
            ],
            "answer": 0,
            "feedback": {
                1: "Air is itself a gas made of particles. Saying the gaps are "
                   "full of air just asks the same question one layer down.",
                2: "Same problem: that gas would have gaps too, and you would "
                   "never finish.",
                3: "Dust is matter, made of particles, with gaps of its own. "
                   "Nothing is nothing.",
            }},
        # ⚖️ This rung is why FLOOR is 24 and not a round number: the stem
        # counts the cuts in words.
        "apply": {
            "q": "A student cuts a sugar cube in half twenty-four times and "
                 "reaches one particle. Why can they not make the twenty-fifth "
                 "cut?",
            "options": [
                "They can cut it, but what comes out is no longer sugar",
                "No knife is thin enough to fit",
                "Particles are too hard to cut",
                "The piece is too small to see, so the cut cannot be aimed",
            ],
            "answer": 0,
            "feedback": {
                1: "A sharp enough tool can split a particle. The limit is not "
                   "mechanical.",
                2: "Hardness is a property of a large lump of a substance, not "
                   "of one particle.",
                3: "Difficulty in aiming is a practical problem. The model "
                   "makes a stronger claim than that.",
            }},
        "explain": {
            "q": "Explain, using the particle model, why 50 ml of water added "
                 "to 50 ml of alcohol gives 97 ml and not 100 ml.",
            "field_label": "Your explanation",
            "placeholder": "Both liquids are made of…",
            "success": [
                "Says both liquids are made of particles with gaps between them.",
                "Says the particles of the two liquids are different sizes.",
                "Says the smaller particles fit into the gaps between the "
                "larger ones.",
                "Says no particles are lost or destroyed — the total "
                "amount of matter is unchanged.",
                "Says the volume drops because the particles pack more closely, "
                "not because anything disappears.",
            ]},
        "produce": {
            "q": "A student says the gaps between particles in a gas must "
                 "contain air, \"because otherwise it would be a vacuum in "
                 "there, and you cannot have a vacuum in the middle of a "
                 "room.\" Reply to them.",
            "field_label": "Your reply",
            "placeholder": "If the gaps were full of air…",
            "success": [
                "Points out that air is itself made of particles.",
                "Says that filling the gaps with air only pushes the same "
                "question down a level, and never ends.",
                "Says the gaps genuinely contain nothing.",
                "Uses evidence: a gas can be squashed, which would be "
                "impossible if the space were already full.",
                "Notes that this is not the same as a vacuum you could stand "
                "in — the space is smaller than a particle.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Matter is made of particles with a floor you cannot cut past, "
                "nothing at all between them, and constant motion. Three "
                "claims. You have tested two of them tonight and the third is "
                "the next five lessons.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: history of science and how a claim becomes evidence live HERE,
    # and this paragraph is exactly that. Nothing in it retracts the lesson body.
    "stretch": [
        {"type": "explainer", "id": "democritus",
         "text": "The Greeks got here by argument alone, around 400 BC — "
                 "Democritus reasoned that cutting must stop somewhere and "
                 "called the last piece <em>atomos</em>, uncuttable. He had no "
                 "evidence, and for two thousand years his idea sat next to the "
                 "equally reasonable one that matter is continuous, with "
                 "nothing to choose between them. What broke the tie was not a "
                 "better argument but a measurement: gases combining in fixed "
                 "whole-number ratios, mass balancing exactly through a "
                 "reaction, and eventually the water-and-alcohol arithmetic you "
                 "did at the top of this page. An idea does not become science "
                 "when someone thinks of it. It becomes science when a number "
                 "forces it."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still think something must be in the gap?",
              "cta": "Ask about this lesson",
              "anchor": "s-gap"},

    "before_this": "Nothing — this is where the unit starts",

    # ⚠️ AUTHORED AND CURRENTLY UNRENDERED, and flagged rather than dropped.
    # `r_endmatter` shows `ks4_becomes` only when `ks4_links` is empty, and this
    # lesson's KS4 edge is carried across from the superseded body. So the third
    # card renders the link, and Design's sentence — which is the one that says
    # what the model becomes and where it stops — is held here for the ruling.
    # Emptying `ks4_links` would print it; that is a product decision, not mine.
    "ks4_becomes": "The kinetic theory of matter, ionic and covalent "
                   "structure, and the limits of the simple particle picture.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
