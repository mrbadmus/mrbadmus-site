"""P1 L8 — Simple machines: force for distance (QUANTITATIVE).

The unit's only QUANTITATIVE lesson and the one that proves the MRB-204
machinery in both of its branches. `KS3.P.ECT.01` reads:

    "simple machines give bigger force but at the expense of smaller movement
     (and vice versa): product of force and displacement unchanged"

which is two statements in one bullet — a claim about the trade, and a claim
about what is conserved through it — and they are two DIFFERENT SHAPES.

── ⚖️ MRB-204: THIS LESSON DRAWS A TRIANGLE AND A BEAM, AND THE CHOICE IS
      MADE PER BLOCK AGAINST THE ARITHMETIC ─────────────────────────────

    work done = force x distance          A GENUINE PRODUCT.  TRIANGLE.
                                          One quantity is the other two
                                          multiplied together, the triangle
                                          means exactly that, and covering a
                                          corner gives the right rearrangement
                                          every time.

    work in = work out                    A CONSERVATION STATEMENT.  BEAM.
                                          Two equal wholes with nothing
                                          multiplied by anything.

⚠️ **The second one is the trap, and it is the trap physics has and chemistry
did not.** Both sides of `work in = work out` ARE products, so the pattern-
matching answer is "products get triangles". That is wrong. A triangle asserts
that one of three quantities equals the other two multiplied — put work-in,
work-out and anything else in one and you have told a student that
`work in = work out x something`, which is false and which they will then use.
The relationship here is an EQUALITY BETWEEN two products, and the shape for
an equality of two equal things is a level beam.

⚠️ **And the beam takes NO part-whole bar**, which is the other half of the
check. `c2-06`'s and `p1-03`'s conservation statements split their after-side
into parts, so they get a bar as well. This one does not split into anything:
there is one whole on each side of the beam and no parts, so a bar would have
to invent a division that is not in the physics. `r_formula` allows the figure
without the cover, and that is what is authored.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**A machine never reduces the work. It changes the deal.** `ENER-16` is the
misconception and it is what everybody believes about a ramp: that pushing a
barrel up a slope is *less work* than lifting it. It is exactly the same work,
done with a smaller force over a longer distance. The bench is built so this
is unmissable — every one of its nine set-ups reads 120 J, because the load
and the height never change and the load and the height are the only things
that decide it.

**The bench is IDEAL and the page says so.** Every reading assumes no friction
and a weightless machine, so work in equals work out exactly. Real machines
are worse, always, and the closing panel says which way the error runs and
why: friction means you put MORE in than you get out, never less. Leaving that
out would let a student meet a real ramp, measure 135 J in for 120 J out, and
conclude the rule is broken.

── The numbers, and why they are all the same ──────────────────────────

One load throughout: **600 N raised 0.20 m**, so the useful work is
`600 x 0.20 = 120 J` in every set-up on the bench. Nine multipliers across
three machines, and each one divides the force and multiplies the distance by
the same number. `ks3_art/p1.py` computes both products from the multiplier
and REFUSES to render a row whose two products differ — the identity is the
whole lesson, and a row that quietly broke it would render perfectly.

⚠️ **A multiplier of 1 is on the bench, twice, and it is not padding.** An
equal-armed lever and a single fixed pulley both give exactly 600 N over
exactly 0.20 m: no force advantage, no distance penalty. They are real
machines that people really use, and they are the state that makes the
derived comparative honest — a bench whose readout can only ever say "less
force, further" has an authored comparative wearing a computed one's clothes.
The ramp has no 1x setting because a ramp with no slope is not a ramp, and
the close says so rather than leaving the gap unexplained.
"""

LESSON = {
    "slug":        "simple-machines",
    "title":       "Simple machines: force for distance",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "QUANTITATIVE",

    "covers":      ["KS3.P.ECT.01"],
    # ⚠️ The lesson uses the term "work done", which `KS3.P.FORCES.07` also
    # names and which P4 owns. `touches` records the overlap: this lesson is
    # not answerable for FORCES.07 (deformation) and does not teach it.
    "touches":     ["KS3.P.FORCES.07"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "forces", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["conservation-of-energy"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "Work done = force × distance. A lever, a ramp and a pulley "
                        "all trade force for distance, and none of them reduces the "
                        "work.",

    "big_question": "One person with a crowbar can lift a corner of a car. "
                    "The crowbar has no engine and no battery. Something has "
                    "to be paying for it.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "One hand, six hundred newtons", "done_when": "committed"},
        {"anchor": "s-machine", "short": "BENCH",
         "label": "Nine set-ups, one number", "done_when": "all_setups_run"},
        {"anchor": "s-build",   "short": "STEPS",
         "label": "Your own four steps", "done_when": "steps_opened"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Is a ramp less work?", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A crowbar, one hand, and the corner of a car comes off the "
                 "ground.",
        "prompt": "The corner of a small car pushes down with about 600 "
                  "newtons — more than most people can lift. Slide a long "
                  "crowbar under it, put a block near the car as a pivot, and "
                  "one hand on the far end lifts it easily.",
        "commit": "The bar has no motor. Where did the extra force come "
                  "from?",
        "options": [
            "The bar multiplies the energy you put in",
            "Nowhere — you moved your end much further than the car moved",
            "The pivot supplies the difference",
            "The bar stores force from earlier pushes and releases it",
        ],
        "reveal": "Nowhere. Watch the two ends: your hand travels more than "
                  "a metre and the car rises twenty centimetres. You "
                  "pushed with a sixth of the force through six times the "
                  "distance, and force multiplied by distance came out "
                  "exactly the same at both ends. The bar traded you one for "
                  "the other.",
    },

    "misconceptions": [
        {"id": "ENER-16",
         "statement": "A ramp means you do less work than lifting the load "
                      "straight up.",
         "elicited_by": "think-commit-ramp",
         "confronted_by": "think-commit-ramp"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Pushing something and getting nowhere transfers nothing. "
                 "What counts is a force that actually moves something, and "
                 "the amount transferred depends on two things: how big the "
                 "force is, and how far it moves whatever it is pushing. "
                 "Multiply those two and you have the number, in joules."},

        # ── formula 1 (MRB-204 part 1) — A PRODUCT, SO A TRIANGLE. ─────────
        # Not a rail stop: it is read, not done.
        {"type": "formula", "id": "work-done",
         "statement": "work done = force × distance moved",
         "support": ["force in newtons (N)",
                     "distance in metres (m)",
                     "work done in joules (J)"],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle: work done on top, force and "
                           "distance moved underneath, multiplied together.",
             "top":   {"label": "W", "button": "Cover W",
                       "result": "W = F × d",
                       "text": "W is on its own at the top with the other two "
                               "side by side underneath. Cover it and you are "
                               "left with F × d — multiply."},
             "left":  {"label": "F", "button": "Cover F",
                       "result": "F = W ÷ d",
                       "text": "F sits underneath with W above it. Cover it "
                               "and you are left with W over d — divide."},
             "right": {"label": "d", "button": "Cover d",
                       "result": "d = W ÷ F",
                       "text": "d sits underneath with W above it. Cover it "
                               "and you are left with W over F — divide."},
             # F first and pre-covered: every question on this page is a
             # question about the force a machine lets you get away with.
             "order": ["left", "top", "right"],
             "covered": "left",
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["W — work done, in J",
                           "F — force, in N",
                           "d — distance moved, in m"],
                 "condition": "The distance is how far the force moved "
                              "whatever it was pushing — never how far you "
                              "walked."}}},

        # #s-machine — the flagship. Ink-dark practical.
        {"type": "machine-bench", "id": "nine-setups", "anchor": "s-machine",
         "eyebrow": "At the bench · one load, three machines",
         "heading": "600 newtons, raised 20 centimetres, nine ways",
         "head_counter": {"format": "{n} of 9 set-ups run", "total": 9},
         "demand": "investigate",
         "targets": "ENER-16",
         "prompt": "The load and the height never change. Pick a machine and "
                   "a setting, and read all four numbers before you move on.",
         "gate": {"prompt": "Commit first. A machine lets you lift the same "
                            "load with a quarter of the force. What happens "
                            "to the distance you have to move?",
                  "options": ["It stays the same",
                              "It is a quarter as far",
                              "It is four times as far",
                              "It depends which machine it is"]},
         "resting": "Pick a machine and a setting.",
         "load": 600,
         "height": 0.20,
         "units": {"force": "N", "distance": "m", "work": "J"},
         "labels": {"fin": "Force you apply", "din": "Distance you move it",
                    "fout": "Force on the load", "dout": "Distance it rises",
                    "win": "Work you do", "wout": "Work done on the load",
                    "machine": "Machine", "setting": "Setting"},
         # ⚖️ `multiplier` IS THE ONLY AUTHORED NUMBER PER SET-UP. Both forces,
         # both distances and both products are computed from it and from the
         # load and height above, in `ks3_art/p1.py`, and the renderer refuses
         # a row whose two products differ. The identity is the lesson.
         "machines": [
             {"id": "lever", "name": "A lever",
              "how": "A bar on a pivot. The further your end is from the "
                     "pivot compared with the load's end, the bigger the "
                     "multiplier.",
              "settings": [
                  {"id": "equal", "label": "Arms equal", "multiplier": 1,
                   "detail": "A see-saw. Your end and the load's end are the "
                             "same distance from the pivot."},
                  {"id": "three", "label": "Your arm 3× longer",
                   "multiplier": 3,
                   "detail": "A short crowbar, with the pivot close to the "
                             "load."},
                  {"id": "six", "label": "Your arm 6× longer", "multiplier": 6,
                   "detail": "A long crowbar. This is the one in the hook."},
              ]},
             {"id": "ramp", "name": "A ramp",
              "how": "A slope you push the load up instead of lifting it. "
                     "The longer the slope for the same height, the bigger "
                     "the multiplier.",
              "settings": [
                  {"id": "steep", "label": "Slope 2× the height",
                   "multiplier": 2,
                   "detail": "A steep ramp — 40 cm of slope to rise 20 cm."},
                  {"id": "medium", "label": "Slope 3× the height",
                   "multiplier": 3,
                   "detail": "60 cm of slope to rise 20 cm."},
                  {"id": "long", "label": "Slope 5× the height",
                   "multiplier": 5,
                   "detail": "A metre of slope to rise 20 cm. A wheelchair "
                             "ramp is gentler still."},
              ]},
             {"id": "pulley", "name": "A pulley system",
              "how": "The load hangs from several lengths of the same rope. "
                     "Each length carries a share of the weight, and the "
                     "multiplier is how many lengths hold it up.",
              "settings": [
                  {"id": "one", "label": "1 rope holding the load",
                   "multiplier": 1,
                   "detail": "A single fixed pulley. It changes the "
                             "direction you pull in and nothing else — which "
                             "is often exactly what you want."},
                  {"id": "two", "label": "2 ropes holding the load",
                   "multiplier": 2,
                   "detail": "One fixed pulley and one moving with the load."},
                  {"id": "four", "label": "4 ropes holding the load",
                   "multiplier": 4,
                   "detail": "A block and tackle. The rope has to come in "
                             "four times as fast as the load goes up."},
              ]},
         ],
         "close": [
             "Nine set-ups, three machines, and the last two columns read "
             "120 joules every single time. The load and the height are what "
             "decide the work, and neither of them ever changed.",
             "Two of the nine gave no advantage at all — the equal-armed "
             "lever and the single fixed pulley. Both are real machines that "
             "people use every day, and what they buy you is a change of "
             "direction rather than a change of force. There is no 1× ramp "
             "on the bench because a ramp with no slope is not a ramp.",
             "Every reading here assumes no friction and a machine that "
             "weighs nothing. A real crowbar or a real ramp always needs "
             "<strong>more</strong> in than it delivers out, never less — "
             "the extra warms the pivot, the rope and the surfaces. The rule "
             "is not broken by that; it is why nobody has ever built a "
             "machine that gives out more than it takes in.",
         ]},

        # ── formula 2 (MRB-204 part 1 again) — A CONSERVATION STATEMENT,
        # SO A BEAM. No triangle, and no bar: there are no parts to split.
        {"type": "formula", "id": "in-equals-out",
         "eyebrow": "The rule the bench just showed",
         "statement": "work you do = work done on the load",
         "support": ["with no friction and a machine that weighs nothing",
                     "a real machine always needs a little more in"],
         "figure": {
             "shape": "balance",
             "aria_label": "A balance beam, level. On the left pan: the work "
                           "you do, which is your force multiplied by the "
                           "distance you move. On the right pan: the work "
                           "done on the load, which is the load's weight "
                           "multiplied by how far it rises. The two are "
                           "equal.",
             "pans": {"left": "what you put in", "right": "what comes out"},
             "caption": "always level"}},

        # ── the worked example (MRB-204 part 3) — read, not done ───────────
        {"type": "worked-example", "id": "crowbar-worked"},

        # ── #s-build (MRB-204 part 4) ──────────────────────────────────────
        {"type": "fifa-pick", "id": "your-four-steps", "anchor": "s-build",
         "ground": "inset",
         "eyebrow": "Your turn · the same four steps",
         "heading": "A ramp 1.00 m long is used to raise a 600 N barrel "
                    "0.20 m onto a lorry.",
         "demand": "construct",
         "prompt": "Work out the force needed to push the barrel up the "
                   "ramp. Commit to each line, then open the worked version.",
         "picks": [
             {"label": "Step 1 · The rule",
              "options": [
                  "work you do = work done on the load",
                  "work you do = work done on the load + the load's weight",
                  "work you do = the load's weight × the ramp length",
              ]},
             {"label": "Step 2 · Insert",
              "options": [
                  "your force × 1.00 = 600 × 0.20",
                  "your force × 0.20 = 600 × 1.00",
                  "your force × 1.00 = 600 × 1.00",
              ]},
         ],
         "field": {"label": "Steps 3 and 4 · Work it out, then answer",
                   "hint": "Your answer as a number",
                   "placeholder": "0",
                   "unit_hint": "Unit",
                   "unit_placeholder": "choose a unit",
                   "units": ["N", "J", "m", "kg"]},
         "button": "Show the four steps",
         "progress": {"format": "{n} of 3 lines committed", "done": "Opened"},
         "reveal_head": "The barrel and the ramp, done four ways",
         "steps": [
             {"letter": "F", "label": "Formula",
              "line": "work you do = work done on the load",
              "note": "And work done is force × distance moved, on both "
                      "sides."},
             {"letter": "I", "label": "Insert",
              "line": "your force × 1.00 = 600 × 0.20",
              "note": "You push along the whole metre of slope. The barrel "
                      "only rises 0.20 m, and 600 N is what it takes to lift "
                      "it straight up."},
             {"letter": "F", "label": "Fine-tune",
              "line": "your force = 120 ÷ 1.00",
              "note": "The right-hand side works out to 120 J. Rearranged "
                      "so the unknown is on its own — cover F on the "
                      "triangle."},
             {"letter": "A", "label": "Answer",
              "line": "your force = 120 N",
              "note": "A fifth of the weight, over five times the distance. "
                      "The work is 120 J either way, which is the whole "
                      "point of the machine and the whole cost of it."},
         ],
         "close": {"template": "You wrote {answer} {unit}. The worked answer "
                               "is 120 N.",
                   "blank": "—"}},

        {"type": "key-fact", "ref": "force-for-distance"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Work done", "Newton", "Simple machine", "Pivot"]},

        {"type": "misconception", "id": "think-commit-ramp",
         "anchor": "s-think", "targets": "ENER-16"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "force-for-distance",
         "text": "A simple machine trades force for distance. It can give "
                 "you a bigger force, but only by making you move further — "
                 "and force multiplied by distance comes out the same at "
                 "both ends. No machine reduces the work.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Work done",
         "definition": "Force multiplied by the distance the force moves "
                       "something, measured in joules.",
         "note": "Same unit as energy, because it is the same thing: work "
                 "done is the amount transferred."},
        {"term": "Newton",
         "definition": "The unit of force, written N.",
         "note": "A 100 g apple is pulled down with about 1 N. A small car "
                 "corner presses down with about 600 N."},
        {"term": "Simple machine",
         "definition": "A device that changes the size or direction of a "
                       "force without changing the work done.",
         "note": "A lever, a ramp, a pulley, a screw, a wedge, a wheel and "
                 "axle."},
        {"term": "Pivot",
         "definition": "The fixed point a lever turns about.",
         "note": "Move it closer to the load and the lever's multiplier goes "
                 "up."},
    ],

    "activities": [
        {"id": "crowbar-worked",
         "kind": "worked-example",
         "demand": "explain",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A crowbar lifts a 600 N car corner by 0.20 m, and your "
                    "hand moves 1.20 m.",
         "head_counter": {"format": "Step {n} of 4", "total": 4},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All four shown",
                     "done_note": "Now the same four steps on a ramp."},
         "fifa": [
             {"letter": "F", "label": "Formula",
              "line": "work you do = work done on the load",
              "note": "The bar has no engine, so nothing is added. Whatever comes out at the load's end went in at yours."},
             {"letter": "I", "label": "Insert",
              "line": "your force × 1.20 = 600 × 0.20",
              "note": "Your hand travels 1.20 m. The car corner rises 0.20 m against a weight of 600 N."},
             {"letter": "F", "label": "Fine-tune",
              "line": "your force = 120 ÷ 1.20",
              "note": "The right-hand side is 120 J. Cover F on the triangle: W over d."},
             {"letter": "A", "label": "Answer",
              "line": "your force = 100 N",
              "note": "A sixth of the weight, through six times the distance. 100 N is about what a full ten-litre bucket of water weighs, which is why one hand can do it."},
         ]},

        {"id": "think-commit-ramp",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-16",
         "prompt": "A removal firm can carry a 600 N crate straight up 0.20 m "
                   "onto a lorry, or push it up a 1.00 m ramp instead. "
                   "Commit before you read on.",
         "options": [
             "The ramp is less work, which is why ramps exist",
             "The ramp is more work, because the crate travels further",
             "The ramp is the same work, done with a smaller force",
             "The ramp is less work only if the crate has wheels",
         ],
         "reveal": [
             "Exactly the same work: 120 joules either way. Lifting it "
             "straight up is 600 N through 0.20 m. Pushing it up the ramp is "
             "120 N through 1.00 m. Both come to 120 J, and they have to — "
             "the crate ends up in the same place, so the same amount has "
             "gone into its gravitational store.",
             "What the ramp changes is whether one person can do it at all. "
             "600 N is beyond most people; 120 N is a firm push. Ramps do "
             "not exist to save work and never did — they exist because a "
             "force you can actually produce is worth far more than a short "
             "distance. And a real ramp is worse than this, not better: "
             "friction means you push with rather more than 120 N, and the "
             "extra warms the crate and the ramp.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "A force of 20 N pushes a box 3 m across a floor. How much "
                 "work is done?",
            "options": [
                "23 J",
                "6.7 J",
                "20 J",
                "60 J",
            ],
            "answer": 3,
            "feedback": {
                0: "That is 20 + 3. Work done is force multiplied by "
                   "distance, not added to it.",
                1: "That is 20 ÷ 3. Cover W on the triangle: it sits alone "
                   "at the top, so the other two are side by side — multiply.",
                2: "That is the force on its own. The distance has to come "
                   "into it, or pushing something one metre and pushing it a "
                   "kilometre would be the same.",
            }},
        "apply": {
            "q": "A pulley system lets a builder raise a 400 N load using a "
                 "force of 100 N. The load rises 2 m. How far does the "
                 "builder have to pull the rope?",
            "options": [
                "8 m",
                "2 m",
                "0.5 m",
                "4 m",
            ],
            "answer": 0,
            "feedback": {
                1: "That is how far the LOAD rose. If the rope moved the "
                   "same distance, the builder would be getting the force "
                   "for nothing.",
                2: "That is 2 ÷ 4, which is the trade the wrong way round. "
                   "A smaller force always means a longer distance.",
                3: "Close, but check the multiplier: the force went from "
                   "400 N to 100 N, which is four times smaller, not two.",
            }},
        "explain": {
            "q": "A student says: \"A block and tackle is brilliant — you get "
                 "four times as much force out as you put in, so you get "
                 "energy for free.\" Explain what is right and what is wrong "
                 "about that.",
            "field_label": "Your explanation",
            "placeholder": "The force part is right, because…",
            "success": [
                "Agrees that the force really is four times bigger.",
                "Says the rope has to be pulled four times as far.",
                "Says force × distance is the same at both ends.",
                "Says no energy is created — the work in equals the work "
                "out.",
                "Says a real block and tackle needs slightly more in than it "
                "gives out, because of friction.",
            ]},
        "produce": {
            "q": "A wheelchair ramp must let someone push a 900 N chair and "
                 "occupant up a 0.30 m step using no more than 90 N. Work "
                 "out how long the ramp has to be, show your four steps, and "
                 "then say one reason a real ramp would need to be longer "
                 "than your answer.",
            "field_label": "Your working and your reason",
            "placeholder": "Formula: work you do = work done on the load…",
            "success": [
                "States work in = work out.",
                "Inserts 90 × length = 900 × 0.30.",
                "Rearranges to length = 270 ÷ 90.",
                "Answers 3 m, with the unit.",
                "Gives a real reason for making it longer — friction in the "
                "wheels, or a safe gradient that is gentler than the "
                "arithmetic minimum.",
            ]},
    },

    "key_note": "Work done = force × distance moved, in joules. A simple "
                "machine trades one for the other: a bigger force always "
                "costs a longer distance, and the two multiplied together "
                "come out the same at both ends. No machine ever reduces the "
                "work, and a real one needs a little more in than it gives "
                "out.",

    "stretch": [
        {"type": "explainer", "id": "perpetual-motion",
         "text": "People have been trying to build a machine that gives out "
                 "more than it takes in for at least eight hundred years, "
                 "and the drawings are wonderful — overbalancing wheels, "
                 "self-filling water screws, magnets pulling a ball round a "
                 "loop for ever. Every one of them fails, and every one "
                 "fails at the same place: somewhere in the cycle a part has "
                 "to be returned to where it started, and returning it costs "
                 "exactly what the clever part gained. The British and "
                 "American patent offices both stopped accepting them "
                 "outright — not because the idea is banned, but because "
                 "conservation of energy has never once been beaten and they "
                 "got tired of reading the same wheel."},
    ],

    "support": [],

    "safety_note": "A load held up by a lever or a pulley falls the moment "
                   "the force is released, and it falls onto whatever is "
                   "under it.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a ramp is not less work?",
              "cta": "Ask about this lesson",
              "anchor": "s-machine"},

    "ks4_becomes": "Work done, power, and efficiency calculated for real "
                   "machines, and moments used to analyse a lever "
                   "quantitatively.",

    "ws": ["measurement", "analysis-and-evaluation"],

    "review_state": "draft",
}
