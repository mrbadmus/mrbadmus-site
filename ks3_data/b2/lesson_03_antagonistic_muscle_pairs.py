"""B2 L3 — Antagonistic muscle pairs (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b2/b2-03-antagonistic-muscle-pairs.dc.html`
(823 lines), and its measured specification,
`docs/ks3/b2-inventory/PAYLOAD-MAP.md` §3.

⚠ **This page keeps the least of its prose in named constants and the most
inside `renderVals()`.** `MOVES`, `RUNGS`, `SELF_RUNGS` and `RAIL` were lifted
with `tools/extract_design_payload.js`; everything in `muscle_pair` below —
the seven-branch interpretation ladder, the four status lines, the three state
words, the two tab label sets and the two canvas label stems — was lifted from
the line ranges §3.2 records. A lift that took only the constants would have
lost the science.

── The mechanism IS the teaching, and it is authored, not hard-coded ─────

    both pulling → the joint LOCKS wherever it is
    biceps only  → 135°        triceps only → 6°        neither → 6°
    pulling 90 °/s · FALLING 55 °/s

NOTES §3.3's "gravity straightens a hanging arm for free" is that rate
difference and nothing else: a student meets it by pressing **Neither** and
watching the arm come down more slowly than it went up. Equalise the two rates
and the lesson is gone, leaving the animation.

── One correction to Design's page (contract R4) ────────────────────────

Design's b2-03 reads `prefers-reduced-motion` once in `componentDidMount` and
never consults it in the tick, so the arm animates under reduced motion. Its
own sibling b2-02 checks correctly inside the loop, so this is a slip rather
than an intention, and R6 already rules that reduced motion is a COMPLETE
experience rather than a lesser one. `shared/ks3.js` asks every frame and snaps
straight to `target()` when motion is reduced: the arm still ends where the
mechanism says, it just does not travel there.
"""

# ── the four options offered against every movement ─────────────────────
# Per item, not shared: m1/m2 are about the knee, m3 the ankle, m4 the elbow,
# so the option set changes with the joint.
_KNEE = [
    "Quadriceps, on the front of the thigh",
    "Hamstrings, on the back of the thigh",
    "Both together",
    "Neither — gravity does it",
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 73 character for character.
    "slug":        "antagonistic-muscle-pairs",
    "title":       "Antagonistic muscle pairs",
    "discipline":  "biology",
    "unit":        "movement-skeleton-and-muscles",
    "family":      "SYSTEM",

    "covers":      ["KS3.B.SKEL.03"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    "requires":    ["joints"],
    "assumes":     [],
    "references":  ["biomechanics-forces-in-the-body"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    "big_question": "Every muscle you own can do exactly one thing. So how "
                    "does an arm come back?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Page lines 359–365; tick conditions 643–650.
    #
    # ⚠ Stage 2's counter runs over a MIXED KEY SPACE: `tried` takes keys from
    # the four mode ids AND the two kill ids, so "4 of 4 settings tried" is
    # reachable as two modes plus two kills. That is Design's own behaviour
    # under Design's own label, and it is honest about "settings touched" while
    # being loose about "all four contraction modes tried". Reproduced as
    # drawn, and reported — tightening it to the four modes would contradict
    # the label printed on the page.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Only ever a pull",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Two muscles, one elbow", "done_when": "four_settings_tried"},
        {"anchor": "s-pairs",  "short": "PAIRS",  "label": "Four movements",
         "done_when": "all_moves_decided"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Relax or stretch",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "A digger can push its arm out. You cannot.",
        "prompt": "A hydraulic ram does both jobs: pump oil in and it extends, "
                  "let oil out and it retracts. A muscle has one move. It "
                  "shortens, and it pulls. There is nothing it can do to push.",
        "commit": "You push a door open, straightening your arm. What "
                  "straightens it?",
        "options": [
            "The biceps pushes the forearm out",
            "The biceps gets longer on its own",
            "A different muscle, behind the arm, pulls",
            "Nothing does — the arm falls straight",
        ],
        "reveal": "A second muscle, on the other side of the same bone, "
                  "pulling the opposite way. The biceps cannot push your "
                  "forearm out any more than a rope can push a bucket up a "
                  "well. Everything you do twice — up and down, open and shut "
                  "— needs two muscles.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    "misconceptions": [
        {"id": "BODY-07",
         "statement": "Muscles push as well as pull.",
         "elicited_by": "hook",
         "confronted_by": "muscle-pair"},
        {"id": "BODY-08",
         "statement": "To straighten your arm, the triceps contracts and the "
                      "biceps stretches itself back out.",
         "elicited_by": "relax-or-stretch",
         "confronted_by": "relax-or-stretch"},
        {"id": "BODY-09",
         "statement": "If both muscles of a pair contract, the movement is "
                      "faster or stronger.",
         "elicited_by": "muscle-pair",
         "confronted_by": "muscle-pair"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Muscles are attached to bones by tendons, across a joint. "
                 "When a muscle contracts it gets shorter and fatter, and the "
                 "bone it is attached to has no choice but to move."},

        # #s-bench — ink-dark `practical` shell (page line 108).
        {"type": "muscle-pair", "id": "muscle-pair", "anchor": "s-bench",
         "eyebrow": "At the bench · drive the arm, then break it",
         "heading": "Two muscles, one elbow",
         "head_counter": {"format": "{n} of 4 settings tried", "total": 4},
         "demand": "investigate",
         "targets": "BODY-09",
         "prompt": "Contract one, contract the other, contract both, contract "
                   "neither. Then switch a muscle off and find out exactly "
                   "what is lost.",
         "gate": {
             "prompt": "Commit first. If both muscles contract hard at the "
                       "same time, what does the arm do?",
             "options": [
                 "It bends twice as fast",
                 "It goes to halfway and stops there",
                 "It stiffens and stays where it is",
                 "Nothing happens in either muscle",
             ]},
         "labels": {
             "contract": "Contract",
             "kill": "Switch a muscle off",
             "angle": "Elbow angle",
             "biceps": "Biceps · in front",
             "triceps": "Triceps · behind",
             "note": "What this tells you:",
         },
         # An exclusive four-tab group and a NON-exclusive two-toggle group,
         # whose product decides every readout. No shipped instrument has this
         # control topology, which is most of why this is not a `sim`.
         "start_mode": "none",
         "settings_total": 4,
         "modes": [
             {"id": "biceps", "label": "Biceps"},
             {"id": "triceps", "label": "Triceps"},
             {"id": "both", "label": "Both"},
             {"id": "none", "label": "Neither"},
         ],
         "kills": [
             {"id": "biceps", "label": "Biceps off"},
             {"id": "triceps", "label": "Triceps off"},
         ],
         # The mechanism, as data. `both` is absent from `targets` on purpose:
         # when both pull the joint holds wherever it already is, which is a
         # rule about the CURRENT angle and not a number.
         "start_angle": 10,
         "targets": {"biceps": 135, "triceps": 6, "none": 6},
         "rates": {"pull": 90, "fall": 55},
         # The status line under the canvas — four branches, page lines
         # 719–722.
         "status": {
             "both": "Both are pulling. Nothing moves, and both are using energy.",
             "biceps": "The biceps is shortening. Watch which way the forearm goes.",
             "triceps": "The triceps is shortening, and the forearm swings the other way.",
             "none": "Nothing is pulling. The arm is falling under its own weight.",
         },
         "states": {
             "dead": "switched off",
             "contracted": "contracted",
             "relaxed": "relaxed",
         },
         # ⚑ The seven-branch interpretation ladder — the single most important
         # authored block on this page (lines 623–638). The `none` branch is
         # the gravity line NOTES flag 15 names, and it is the only place the
         # 55-vs-90 rate difference is put into words.
         "notes": {
             "biceps_dead": "With the biceps switched off, nothing can bend the elbow. The triceps can straighten it and gravity can drop it, and that is the whole repertoire.",
             "triceps_dead": "With the triceps switched off, the arm still bends. It can only straighten by relaxing and letting the weight of the forearm take it down — so it works while the arm hangs, and fails the moment you try to push anything.",
             "both_dead": "Both switched off. The arm hangs, and nothing you decide changes anything.",
             "both": "Both pulling. The elbow does not move — it stiffens. Nothing has cancelled out inside the muscles; both are working hard, and both are using energy.",
             "biceps": "The biceps pulls the forearm up and the triceps relaxes. Relaxing is not doing nothing: it is letting go so the partner can lengthen it.",
             "triceps": "The triceps pulls on the bone behind the elbow, and the forearm swings down. This is the only muscle that can straighten the arm against a resistance.",
             "none": "Neither is pulling, so the arm falls under its own "
                     "weight. Gravity will straighten a hanging arm for "
                     "free — which is one reason the triceps does less work "
                     "than you would expect.",
         },
         # Drawn on the canvas at (600, 44) and (40, 44). Stem plus suffix,
         # exactly as the page composes them.
         "canvas_labels": {
             "biceps": "BICEPS · IN FRONT",
             "triceps": "TRICEPS · BEHIND",
             "off": " — SWITCHED OFF",
             "pulling": " — PULLING",
             "relaxed": " — RELAXED",
         },
         "alt": {
             "template": "A model arm at the elbow, with the biceps drawn in "
                         "front of the upper arm and the triceps behind it. "
                         "The biceps is {biceps} and the triceps is {triceps}.",
             "words": {
                 "dead": "switched off",
                 "biceps_pulling": "contracted and pulling the forearm up",
                 "triceps_pulling": "contracted and pulling the forearm down",
                 "relaxed": "relaxed",
             }}},

        {"type": "key-fact", "ref": "only-a-pull"},

        # #s-pairs — the sorter again, per-item options, NO closing band on
        # this one (measured: the page draws none).
        {"type": "job-sort", "id": "four-movements", "anchor": "s-pairs",
         "ground": "inset",
         "eyebrow": "Your turn · four movements",
         "heading": "Which muscle is doing the work?",
         "head_counter": {"format": "{n} of 4 decided", "total": 4},
         "demand": "classify",
         "prompt": "In every pair, one muscle contracts and its partner "
                   "relaxes. Decide which one is contracting. The last one is "
                   "not what most people say.",
         "items": [
             {"id": "m1",
              "text": "Someone stands up from a chair. The knee "
                      "straightens.",
              "options": _KNEE,
              "answer": "The quadriceps contract.",
              "why": "They pull the lower leg straight while the hamstrings relax. Gravity is pulling the other way here, which is why standing up is work and sitting down is not."},
             {"id": "m2",
              "text": "Someone pulls their heel up towards their bottom, "
                      "bending the knee.",
              "options": _KNEE,
              "answer": "The hamstrings contract.",
              "why": "The same joint, the opposite muscle. Every pair is one muscle for each direction, and neither can do the other one’s job."},
             {"id": "m3",
              "text": "Someone rises onto their tiptoes.",
              "options": [
                  "The calf muscle, behind the shin",
                  "The muscle down the front of the shin",
                  "Both together",
                  "Neither — gravity does it",
              ],
              "answer": "The calf muscle contracts.",
              "why": "It pulls upwards on the heel bone through the Achilles tendon, and the whole body pivots over the toes. The muscle at the front relaxes; its job is lifting the toes, which is the opposite movement."},
             # The eccentric-contraction case (NOTES flag 13) — the one most
             # people get wrong, and the reason the sorter reveals per row.
             {"id": "m4",
              "text": "Someone lowers a heavy box slowly to the floor, "
                      "straightening their arms as it goes down.",
              "options": [
                  "The biceps, still contracting",
                  "The triceps, contracting",
                  "Both together",
                  "Neither — gravity does it",
              ],
              "answer": "The biceps — still contracting.",
              "why": "This is the one most people get wrong. Gravity is doing the moving; the biceps is holding on and letting the box down a little at a time, getting longer while it pulls. Let go and the box drops. The triceps has nothing to do here at all."},
         ]},

        {"type": "misconception", "id": "relax-or-stretch", "anchor": "s-think",
         "targets": "BODY-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "only-a-pull",
         "text": "A muscle can only pull. Moving a bone back again needs a "
                 "second muscle pulling the other way — an antagonistic pair.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "activities": [
        {"id": "relax-or-stretch",
         "kind": "predict",
         "demand": "explain",
         "targets": "BODY-08",
         "prompt": "Half of that sentence is right. Commit to which half "
                   "before you read on.",
         "options": [
             "Both halves are right",
             "The triceps part is right; the biceps part is not",
             "The biceps part is right; the triceps part is not",
             "Neither half is right",
         ],
         "reveal": [
             "The triceps contracting is right. The biceps stretching itself "
             "is not: a muscle has no way of making itself longer. It can "
             "shorten, or it can stop shortening. What lengthens it is "
             "<strong>being pulled</strong> — by its partner, or by the weight "
             "of whatever it is holding.",
             "This is why the word is <em>relaxes</em>, not <em>stretches</em>. "
             "Relaxing is a muscle letting go so that something else can "
             "lengthen it. If both muscles refuse to let go, the joint locks — "
             "you felt that on the bench.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "Which pair of muscles works the knee?",
            "options": [
                "Biceps and triceps",
                "The calf and the Achilles",
                "Quadriceps and the calf muscle",
                "Quadriceps and hamstrings",
            ],
            "answer": 3,
            "feedback": {
                0: "That pair works the elbow. The same arrangement, a "
                   "different joint and different muscles.",
                1: "The Achilles is a tendon, not a muscle — it is how the "
                   "calf muscle reaches the heel bone.",
                2: "Both real muscles, but they act on different joints, so "
                   "neither can undo the other.",
            }},
        "apply": {
            "q": "The biceps and the triceps both contract hard at the same "
                 "time. What is the main effect?",
            "options": [
                "The elbow stiffens and becomes hard to move in either "
                "direction",
                "The arm bends twice as fast",
                "The arm moves to halfway and stops",
                "Nothing at all is happening in either muscle",
            ],
            "answer": 0,
            "feedback": {
                1: "They pull opposite ways, so nothing is added. Two people "
                   "pulling on opposite ends of a rope do not move it faster.",
                2: "It holds wherever it already was. Nothing moves it to a "
                   "halfway position.",
                3: "A great deal is happening — both are working hard and "
                   "using energy. It is just that nothing moves.",
            }},
        "explain": {
            "q": "Explain why one muscle at the elbow could never be enough, "
                 "however strong it was.",
            "field_label": "Your explanation",
            "placeholder": "A muscle can only…",
            "success": [
                "Says a muscle can only pull — it shortens, and cannot push.",
                "Says one muscle could therefore move the forearm in one "
                "direction only.",
                "Says a second muscle on the other side of the joint is needed "
                "to move it back.",
                "Says that when one contracts the other relaxes and is "
                "lengthened by the pull.",
                "Says strength does not help, because the problem is direction "
                "and not force.",
            ]},
        "produce": {
            "q": "A nerve injury leaves someone with a working biceps and a "
                 "triceps that will not contract at all. Describe what they "
                 "can and cannot do with that arm, and how they could still "
                 "get it straight.",
            "field_label": "Your answer",
            "placeholder": "They can still…",
            "success": [
                "Says they can still bend the elbow, because the biceps works.",
                "Says they cannot straighten it by their own muscle action.",
                "Says the arm can still straighten by relaxing the biceps and "
                "letting gravity pull it down.",
                "Says that only works when the arm is hanging, so pushing a "
                "door open or reaching upwards fails.",
                "Uses the words contract and relax correctly, and does not say "
                "the biceps pushes.",
            ]},
    },

    "key_note": "Muscles pull and never push. They work in antagonistic pairs "
                "on either side of a joint: as one contracts, the other "
                "relaxes and is lengthened. Biceps and triceps at the elbow; "
                "quadriceps and hamstrings at the knee.",

    # The co-contraction extension (NOTES flag 14).
    "stretch": [
        {"type": "explainer", "id": "co-contraction",
         "text": "Contracting both muscles of a pair at once is not a mistake "
                 "— it is how you hold something steady. A surgeon's hand, a "
                 "gymnast on the rings and a hand steadying a phone camera are "
                 "all doing it. The joint stiffens because both sides are "
                 "pulling, so a small knock cannot move it. It costs energy "
                 "and it tires you quickly, which is why you cannot hold a "
                 "heavy tray at arm's length for long even though the tray is "
                 "not going anywhere."},
    ],

    "support": [],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a muscle cannot push?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Muscle fibres and how a contraction actually happens, and "
                   "respiration supplying the energy for it.",

    "ws": ["analysis-and-evaluation"],

    "review_state": "draft",
}
